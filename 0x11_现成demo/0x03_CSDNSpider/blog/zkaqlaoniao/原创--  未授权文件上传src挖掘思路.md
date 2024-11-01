# 原创
：  未授权文件上传src挖掘思路

# 未授权文件上传src挖掘思路

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


### 前言

---


根据月佬对于`doc.html`与`knife4j接口文档`的讲解，在某处信息收集打点的时候发现该问题。

### 收集-knife4j

---


语法:图标搜索 + 学校资产

通过搜索该图标可以发现`knife4j接口文档`

如何搜索学校资产可以通过org搜索组织等方式

收集示例如下

首先输入关键词 `knife4j`<img alt="" height="183" src="https://img-blog.csdnimg.cn/081f0f906c27407187b045f3c831646a.png" width="1080"/>

发现前两个的资产最多，同时点击<img alt="" height="353" src="https://img-blog.csdnimg.cn/f457b9d2b1f741d7be3a1de79a32c253.png" width="1080"/>

然后点击部分资产内部，可以发现确实是输入`knife4j`的文档

接着收敛资产，添加组织`org`为教育，结合语法如下

> 
`1.org="China Education and Research Network Center" &amp;&amp; (icon_hash="-1776476841" || icon_hash="-327916044")`


但是这时候其实会发现资产并不多，因此在鹰图上也进行搜索

> 
`1.web.icon=="b917999252a8678e2dbee25a8274c504"`


接着收敛资产，以组织为例

> 
1.`cert.subject="edu"&amp;&amp;web.icon=="b917999252a8678e2dbee25a8274c504"`


### 发现-未授权文件上传点

---


发现资产之后进行接口翻阅，发现一处比较奇怪的接口

内部未发现鉴权参数，点开了调试尝试上传文件<img alt="" height="313" src="https://img-blog.csdnimg.cn/55ab7cddf880460dbd3901dc4a2a0115.png" width="1080"/> 通过上传接口，发现会直接暴露上传后的文件路径 

经过测试发现，该接口上传脚本文件后进行访问会变成下载，说明`文件类型`在上传之后已被修改

因此构造了`.html`后缀的`xss`文件

> 
`1.`
`2.`
`3.alert(1)`


  上传后访问路径触发存储`xss`

<img alt="" height="242" src="https://img-blog.csdnimg.cn/d0b30d8483634044821a404a7ee1953f.png" width="1080"/> 接着搜索C段又找到了几处上传接口 

---


                                                         **没看够~？欢迎关注！** 

---

