# 转载
：  记一次XSS攻击绕过

# 记一次XSS攻击绕过

### 前言

最近一直在看国外的赏金平台，绕waf是真的难受, 记录一下绕过的场景。

### 初步测试

一开始尝试XSS，发现用户的输入在title中展示，那么一般来说就是看能否闭合，我们从下面图中可以看到，输入尖括号后被转成了实体。

### 绕过html实体编码

解释一下什么是html实体编码

HTML实体编码，也即HTML中的转义字符。

在 HTML 中，某些字符是预留的，例如在 HTML 中不能使用小于号&lt;和大于号&gt;，这是因为浏览器会误认为它们是标签。 如果希望正确地显示预留字符，我们必须在HTML源代码中使用字符实体（character entities）。 HTML 中的常用字符实体是不间断空格。（注意：实体名称对大小写敏感！） 字符实体类似这样：&amp;entity_name; 或者 &amp;#entity_number;如需显示小于号，我们必须这样写：&lt; 或 &lt; 常见的实体编码：

继续尝试是发现我们讲html10进制实体编号输入转义会闭合title标签

原本以为事情逐渐简单了起来，结果更大的一个坑在等着我。

### WAF层面

原本想着&lt;img/src=1 οnerrοr=alert(1) /&gt;直接秒杀 结果来了个waf 贼厉害。

下一步按照往常一样 fuzz事件，结果全是403，这时候那没办法了那就不能用img标签了

改换其他标签，fuzz以下 发现可用的还不少。

然后使用a标签进行绕过

常用的payload，基于下面payload改就行了

原本是一番风顺的 到后面发先还有过滤，真吐了，看图就好

绕过javascript，到这里了可能一部分人觉得已经结束了，但实际上没那么简单

前面其实花的时间并不多主要绕alert的时候，此处我尝试的多种方式包括html实体绕过，基本都不行。

然后就在此处卡了很久，我也想过不使用alert使用prompt这些函数但就是不行，后面发现后面就是不能跟括号和反引号

这时候就在想，还有不能用括号进行弹窗的函数？给我整懵逼了，找了一大圈一个都没找到都需要用括号,alert后不需要括号和反引号的也过不了。

最后在推特上看到了这个最终完成绕过

[aurebesh.js](https://aem1k.com/aurebesh.js/#java)

本地测试payload

最终效果

> 
本文作者：蚁景科技， 转载请注明来自[FreeBuf.COM](https://www.freebuf.com/)


** 点击下方链接可免费获得渗透工具，应急响应笔记，学习路线技术文档、书籍，面试题，视频基础到进阶，环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等**[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
