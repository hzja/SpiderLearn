# 原创
：  【JS逆向百例】某盾 Blackbox 逆向分析

# 【JS逆向百例】某盾 Blackbox 逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

目标：某盾 Blackbox 算法逆向分析

网站：`aHR0cHM6Ly93d3cuanVuZXlhb2Fpci5jb20v`

本文只对某盾 Blackbox 的其中一种算法进行逆向分析，不涉及指纹风控、环境部分。

### 逆向分析

通过搜索 `blackBox` 即可定位到如下位置：

往上跟栈，发现是由此函数生成的：

进入到该函数内，重新下断点刷新网站，单步往下跟，定位到最后 `return` 处：

发现 `Blackbox ` 值是由 `5WPH173561408225WrZh6Cf` 经过 `QOoooO` 函数生成的 ，搜索发现该值是

`profile.json` 接口返回的：

我们的重点就是 `profile.json` 接口的这些请求参数，非常之多，但是不要怕，慢慢来。

查看堆栈，发现和 `Blackbox ` 值最终生成的 js 文件一样，都是 `fm.js` 文件，也就是 `Blackbox ` 值生成的核心文件，点进去发现有一堆 `oQ0Qo0` 大数组混淆，定位到 `ooQGOO` 的生成位置 `oQ0Qo0 = ooQGOO(oQ0Qo0);`：

`oQ0Qo0` 就是传入的长字符串， 通过 `ooQGOO` 函数就生成了 `oQ0Qo0` 的大数组，可以把 `ooQGOO` 给扣下来，非常容易，也可以分析 `ooQGOO` 函数，对这类混淆熟悉的可以直接秒，基本都是一套逻辑：

```
// 传入的长字符串
en_txt = '';

// ooQGOO 函数部分
oQ0Qo0 = decodeURIComponent(atob(en_txt))['split']('##');

traverse(ast, {
   
    MemberExpression(path){
   
        let {
   object, property} = path.node;
        if (!t.isIdentifier(object) &amp;&amp; !t.isNumericLiteral(property)) return;
        if (object.name !== "oQ0Qo0") return;
        let _v = oQ0Qo0[property.value]
        path
```
