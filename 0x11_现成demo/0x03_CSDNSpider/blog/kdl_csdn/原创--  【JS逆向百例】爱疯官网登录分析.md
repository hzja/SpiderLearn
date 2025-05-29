# 原创
：  【JS逆向百例】爱疯官网登录分析

# 【JS逆向百例】爱疯官网登录分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近有些小伙伴在微信群交流，关于爱疯登录相关加密参数的问题，同时，也有粉丝私信，想让 K 哥出关于 m1、m2 相关参数逆向的系列教程。众所周知，K 哥一向会尽力满足粉丝们的需求，本文就对该站进行逆向研究，该案例综合性较强，适合作为逆向案例来练手：

### 逆向目标

### 逆向过程

#### 抓包分析

进入 store 登录页，输入邮箱后点击箭头，发现有数据包产生，此处我们称为 init 包，该数据包需要提交 a 等加密参数：

<img alt="7VlVAq.jpg" src="https://i-blog.csdnimg.cn/img_convert/5b74a4ea362aba81c4ec9d46558792e7.jpeg"/><br/> 该接口响应返回 iteration、salt、protocol、b、c 等参数：

<img alt="7VlWCs.jpg" src="https://i-blog.csdnimg.cn/img_convert/88393c6dab07bea0932d54f269581f30.jpeg"/><br/> 最后经过 `/signin/complete` 接口由 c、m1、m2 等参数完成登录校验：

### 逆向分析

#### a 参数

由于该站属于全异步，该参数的定位，我们还是采用跟栈的方式，在 send 接口处打断点，向上跟栈：

我们发现在匿名函数这里，data 于 t 中，已经生成了，继续向上跟栈，最终发现 a 值的生成逻辑如下：

```
a: btoa(String.fromCharCode.apply(String, o(new Uint8Array(f.buffer))))

```

经过分析，f.buffer 生成方式如下：

```
c = u.accountName,
r = new n.a(c),
f = r.publicValue,

```

f 是通过 new 了一个 n.a 对象，然后将用户名传入后生成的，所以我们就需要找到 n 是如何生成的：

经过分析，n 是一个模块，按照之前扣 webpack 的逻辑，我们将分发器找到，在该处下断点，刷新浏览器成功在该处断下：

最终复现如下：

f 参数解决后，我们将 o 函数扣出，复现如下：

```
function o(t) {
   
    return function (t) {
   
        if (Array.isArray(t))
            return i(t)
    }(t) || function (t) {
   
        if ("undefined" != typeof Symbol &amp;&amp; null != t[Symbol.iterator] || null != t["@@iterator"])
            return Array.from(t)
    }(t) || function (t, r) {
   
        if (!t)
            return;
        if ("string" == typeof t)
            return i(t, r);
        var e = Object
```
