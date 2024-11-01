# 原创
：  记一个src中危-图像大小与请求参数可修改

# 记一个src中危-图像大小与请求参数可修改

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


[目录](#%E7%9B%AE%E5%BD%95)

[漏洞描述](#%E6%BC%8F%E6%B4%9E%E6%8F%8F%E8%BF%B0)

[漏洞危害](#%E6%BC%8F%E6%B4%9E%E5%8D%B1%E5%AE%B3)

[发现方法](#%E5%8F%91%E7%8E%B0%E6%96%B9%E6%B3%95)

[案例 ](#%E6%A1%88%E4%BE%8B%C2%A0)

[加固建议](#%E5%8A%A0%E5%9B%BA%E5%BB%BA%E8%AE%AE)

---


### 漏洞描述

---


服务器生成了一个具有客户端指定尺寸的图像，如果未实施任何限制，则可能导致拒绝服务攻击。

### 漏洞危害

---


攻击者不需要在此类攻击中投入资源，但服务器可能会分配所需的像素缓冲区（导致内存不足）和/或执行随图像大小变化的计算（导致占用服务器CPU），可能导致拒绝服务攻击。

### 发现方法

---


Burp插件 - Image Size Issues | Url图片尺寸检测

选择Extender -&gt; BApp Store -&gt; 搜索 `Image Size lssues` 进行安装<img alt="" height="416" src="https://img-blog.csdnimg.cn/bd2c6c1caceb467bb39a2db9d1821aec.png" width="1080"/>

通过随意点点点，若存在此漏洞，Burp在Target中显示 `Image size matches request parameters`<img alt="" height="632" src="https://img-blog.csdnimg.cn/ddd13e2ba6544bd186999eb720d1fa70.png" width="1080"/>

## **案例 **

---


通过修改图片大小数值让服务器分配资源增加，具有拒绝服务攻击的隐患。

### 加固建议

---


限制可以作为请求参数请求的维度。

**没看够~？欢迎关注！**

** **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
