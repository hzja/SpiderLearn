# 原创
：  漏洞挖掘 | 记一个信息泄露到RCE

# 漏洞挖掘 | 记一个信息泄露到RCE

### 打点

开局一个登录框

### 信息收集

发现了一处接口泄露了部分信息

不过只有支付宝密钥的信息无法扩大危害，此时尝试寻找了一下其他同类型系统同样的接口，查看一下是否泄露的信息相同
1.  `因为如果相同就说明是静态的，没有价值` 
### 横向收集

此时访问其他系统，发现里面有不一样的东西，包含了数据库的账号以及密码
1.  `说明不是静态的` 
### 利用尝试

此时回到之前的系统，扫了一下端口，发现确实开放了数据库端口

利用工具Sylas：https://github.com/Ryze-T/Sylas/releases/tag/beta

直接连接数据库，然后RCE

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
