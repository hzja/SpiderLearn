# 原创
：  Openfire身份认证绕过漏洞

# Openfire身份认证绕过漏洞

**漏洞详情**：

Openfire是采用Java编程语言开发的实时协作服务器，Openfire的管理控制台是一个基于Web的应用程序，被发现可以使用路径遍历的方式绕过权限校验。未经身份验证的用户可以访问Openfire管理控制台中的后台页面。同时由于Openfire管理控制台的后台提供了安装插件的功能，攻击者可以通过安装恶意插件达成远程代码执行的效果。

**影响版本**：3.10.0&lt;= Openfire&lt;4.6.8 、 4.7.0&lt;=Openfire&lt;4.7.5

**靶场链接**：

https://hack.zkaq.cn/battle/target?id=c81af9c398223250

**ps**:目前靶场暂无Write Up，欢迎同学们来社区投稿wp，如果审核通过会有相应的金币奖励哦~[征集一篇该靶场的wp]，欢迎来玩~<img alt="" height="637" src="https://img-blog.csdnimg.cn/56b0b89c5bd54bbfa5161558261443bb.png" width="1142"/><img alt="" height="830" src="https://img-blog.csdnimg.cn/f0e8f6bfc3d84450a028ebad1bbd7705.png" width="1200"/>

声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！ 

看到这里了，点个“赞”、“再看”吧<img alt="" height="768" src="https://img-blog.csdnimg.cn/7eef5f29ba12416eb11d5d9134357dba.png" width="1024"/>

** **

 渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
