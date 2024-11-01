# 原创
：  24-1 SQL 注入 - http头注入之UA头注入探测

# 24-1 SQL 注入 - http头注入之UA头注入探测

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、http头注入介绍

HTTP头注入是一种网络安全攻击手段，它利用了Web应用程序对HTTP头的处理不当或缺乏充分的验证和过滤。在这种攻击中，攻击者通过修改HTTP请求头中的某些字段，如User-Agent、Referer、Cookies等，插入恶意内容或代码，以达到攻击的目的。这类攻击可能导致多种安全问题，包括跨站脚本攻击（XSS）、跨站请求伪造（CSRF）、会话劫持和敏感信息泄露等。

**常见的HTTP头注入类型**

1.  User-Agent注入：User-Agent头通常用于标识发出请求的浏览器类型。如果Web应用程序将User-Agent头的内容直接反映在响应中，而未进行适当的过滤或编码，攻击者可能会注入恶意脚本，导致XSS攻击。 
1.  Referer注入：Referer头用于指示当前请求页面的来源URL。攻击者可以通过构造包含恶意代码的Referer头，如果Web应用程序将Referer头的内容直接用于页面内容或逻辑判断，可能会被利用进行钓鱼攻击或XSS攻击。 
1.  Cookies注入：Cookies通常用于存储用户会话信息。如果Web应用程序没有正确处理Cookies中的数据，攻击者可以通过注入恶意脚本到Cookies中，当这些Cookies被Web应用程序读取并反映到页面上时，可能导致XSS攻击或会话劫持。
