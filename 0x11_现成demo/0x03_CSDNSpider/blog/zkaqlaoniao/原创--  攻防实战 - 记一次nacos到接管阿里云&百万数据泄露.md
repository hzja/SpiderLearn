# 原创
：  攻防实战 | 记一次nacos到接管阿里云&百万数据泄露

# 攻防实战 | 记一次nacos到接管阿里云&amp;百万数据泄露

在某次攻防当中，通过打点发现了一台nacos，经过测试之后发现可以通过弱口令进入到后台，可以查看其中的配置信息

通过翻看配置文件，发现腾讯云的AK,SK泄露，以及数据库的账号密码。操作不就来了么，直接上云！

利用CF工具加上之前的AK，SK配置信息，创建腾讯云控制台账号密码，登录后直接上云！

翻看腾讯云的资源信息，发现5个存储桶，这一波直接加大分

还可以看一下账单信息，看看购买了什么资源

在私有网络当中，发现里面有两个子网，不过上不去也就没办法

因为客户开通了短信包，同时还可接管腾讯云短信，给自己发一条看看

接管后发送短信，可以篡改内容

同时泄露数据库账号密码，接管数据库，接管数十个数据库，泄露数据高达百万

数据库中泄露小程序APPID和相关的KEY，可接管小程序

##### 后续

后续没有深入，不让打了，对于云安全，其实相对于我们这种脚本小子来说，你会用cf工具，那么你就畅通无阻，但是你必须得找到AK/SK，那么AK/SK是什么玩意呢，它其实就是云服务给你的账号密码(相当于账号密码)不过不能直接登上去，需要用cf工具做做操作

关于cf工具，链接在这，大家自己下载即可<br/> https://github.com/teamssix/cf

非常滴好用!!

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
