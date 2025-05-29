# 原创
：  【JS逆向百例】音乐 wasm 逆向

# 【JS逆向百例】音乐 wasm 逆向

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近在看知识星球群聊的时候，发现有小伙伴在讨论酷某音乐的相关问题，之前也有星球成员私信询问这个案例。K哥一向是尽力满足粉丝需求的，本文就对该站进行逆向研究，该案例较为新奇，既能满足粉丝需求，也是对 wasm 逆向案例的补充与完善：

### 逆向目标

### 抓包分析

进入首页，随机输入手机号，点击发送验证码，弹出验证码弹窗，进行抓包，有很多响应。经过分析，有用的接口为 `send_mobile`与`get_verfy_info`：

<img alt="7GZzbe.jpg" src="https://i-blog.csdnimg.cn/blog_migrate/ed407f75a5ed1ad52759cfe2b78b757c.jpeg"/><br/> 经过首次 send_mobile 接口后会在响应协议头里返回 ssa-code：

同时在 `get_verfy_info` 接口将会携带这个参数：

最终，通过该接口返回一个 `sessionid`，代表会话创建完毕，是全局唯一的标识符：

然后，通过易盾点选/滑块验证码，发现会经过 `v4/verify_user_info` 进行验证：

该接口参数很多，同时还观察到了有 wasm 相关的字样：

最终，再次调用 `send_mobile ` 接口，`status:1` 则代表发送成功：

经过抓包分析，我们需要逆向的参数为：`mid`、`uuid`、`signature`、`params`、`pk`、`sid`、`edt` 。

### 逆向分析

#### mid、uuid 参数

点击发送按钮，然后我们查看 send 的堆栈，从第一个进入：

然后搜索 `mid:` 发现有几处地方可疑，在这几处分别下断，最终在如下的地方成功断下来：

我们进入 `getKgMid` 方法，发现他取了 cookie 中的 kg_mid，且这个值与我们刚刚看到的值相同，如果 cookie 中不存在该参数，那么将会调用下面的方法取浏览器的指纹信息，通过 md5 算法生成该值：

所以我们直接利用 v_jstools 去 hook 一下该 cookie 参数是如何生成的，Hook 脚本如下：

```
(function () {
   
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
   
    set: function (val) {
   
      if (val.indexOf('kg_mid') != -1) {
   
        debugger;
      }
      console.log('Hook捕获到cookie设置-&gt;', val);
      cookieTemp = val;
      return val;
    },
    get: function () {
   
      return cookieTemp;
    },
  });
})();

```

清空浏览器缓存，刷新发现成功断下，向上跟栈，找到该参数生成的位置如下：

分析可知，该参数是通过生成 uuid 然后利用 md5 算法生成的，跟进 uuid 的生成函数中，其生成逻辑如下：

```
Guid: function() {
   
        function S4() {
   
            return (((1 + Math.random())&lt;
```
