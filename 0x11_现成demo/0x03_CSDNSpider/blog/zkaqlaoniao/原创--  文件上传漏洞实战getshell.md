# 原创
：  文件上传漏洞实战getshell

# 文件上传漏洞实战getshell

**目录**

[0x01 信息收集](#0x01%20%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[0x02 寻找接口](#0x02%20%E5%AF%BB%E6%89%BE%E6%8E%A5%E5%8F%A3)

[0x03 拼接路径](#0x03%20%E6%8B%BC%E6%8E%A5%E8%B7%AF%E5%BE%84)

[0x04 权限](#0x04%20%E6%9D%83%E9%99%90)

---


## 0x01 信息收集

<br/> 通过fofa，子域名收集等相关工具搜索域名<br/> 定位到站点：htps://xx..edu.cn/x/xx/

## 0x02 寻找接口

通过f12寻找相关的js，发现有其他的页面

## 0x03 拼接路径

<br/> https://xx.xx.edu.cn/xx/xx/repairResgister<br/> 之后未授权获取到注册用户的页面中，发现有一个上传图片进行上传

由于站点已修复，简单阐述一下<br/> html，jpg，txt，png等相关后缀可以进行上传，但进行jsp等相关的后缀并不能成功。如果是白名单，返回的页面只会显示：只能上传jpg，png等相关图片的后缀，但他并没有显示，所以初步判断这里是黑名单，之后进行上传图片马，还有通过空格，.，%00截断，来进行绕过。

## 0x04 权限

<br/> 成功getshell

> 

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/a7b9d9facf3344afacf2ac9604b888e1.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/597c1ab675304877a4a0920626541fe4.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/df2f0a96deb54b3cbd1b3a6ed30b57ec.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/7745935a25cc45ebb592fe4c9d466637.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/03a84ced42ba4f30b5edc548c845d654.png" width="665"/>

应急响应笔记

学习路线
