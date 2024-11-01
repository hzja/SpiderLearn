# 原创
：  漏洞挖掘 | edu某大学未授权访问

# 漏洞挖掘 | edu某大学未授权访问

### 先利用在Track社区学习到的知识：

我在信息搜集时使用的hunter语法：domain=”edu.cn”&amp;&amp;web.body=”注册”

<br/> 为什么要这样搜？因为往往有注册功能的网站登录后可以有更多的功能点接口，权限也会上升为用户

比如这里登录后，才能访问网站：

<br/> 思路：传参点测sql注入、有回显内容可以测xss、文件上传点测测、框架看一下有无通用、逻辑漏洞想到的都试试<br/> 我比较菜鸡，没在这里找到什么漏洞，但是不要放弃，可以试试目录扫描：<br/> 这里用到老师推荐的**findsomething**插件：

<br/> 这些都是新的资产-接口，可以一个个访问看看<br/> 这里找到一处/advixxx，是班主任的管理后台，但是对用户没有鉴权，可以未授权访问：

<br/> 里面可以看到资金流水等敏感信息：

<br/> 对于这种信息泄露，利用bp抓包看看请求包和相应包，往往会有更多的数据、收获：

<br/> 而且未授权访问还会暴露更多的接口，比如这里：

<br/> 找到一处网站管理员的后台接口，并且用的是wordpress框架，这里可以用用kali的wpscan工具进行漏洞检测，说不定会有惊喜：

 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
