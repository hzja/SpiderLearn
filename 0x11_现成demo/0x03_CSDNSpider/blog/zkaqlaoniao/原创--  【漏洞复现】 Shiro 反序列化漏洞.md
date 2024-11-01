# 原创
：  【漏洞复现】 Shiro 反序列化漏洞

# 【漏洞复现】 Shiro 反序列化漏洞

### 一、漏洞介绍

Apache Shiro是一款开源安全框架，提供身份验证、授权、密码学和会话管理。Shiro框架直观、易用，同时也能提供健壮的安全性。

Apache Shiro 1.2.4及以前版本中，加密的用户信息序列化后存储在名为remember-me的Cookie中。攻击者可以使用Shiro的默认密钥伪造用户Cookie，触发Java反序列化漏洞，进而在目标机器上执行任意命令。

##### 漏洞原理

shiro默认使用了CookieRememberMeManager，其处理cookie的流程是：<br/> 得到rememberMe的cookie值 —&gt; Base64编码 —&gt; AES解密 —&gt; 反序列化<br/> 然而AES的密钥是硬编码的，就导致了攻击者可以构造恶意数据造成反序列化的RCE漏洞。<br/> payload 构造的顺序则就是相对的反着来：<br/> 恶意命令—&gt;序列化—&gt;AES加密—&gt;base64编码—&gt;发送cookie<br/> 在整个漏洞利用过程中，比较重要的是AES加密的密钥，该秘钥默认是默认硬编码的，所以如果没有修改默认的密钥，就自己可以生成恶意构造的cookie了。

##### 漏洞特征

未登陆的情况下，请求包的cookie中没有rememberMe字段，返回包set-Cookie里也没有deleteMe字段<br/> 登陆失败的话，不管勾选RememberMe字段没有，返回包都会有rememberMe=deleteMe字段<br/> 不勾选RememberMe字段，登陆成功的话，返回包set-Cookie会有rememberMe=deleteMe字段。但是之后的所有请求中Cookie都不会有rememberMe字段<br/> 勾选RememberMe字段，登陆成功的话，返回包set-Cookie会有rememberMe=deleteMe字段，还会有rememberMe字段，之后的所有请求中Cookie都会有rememberMe字段

### 二、漏洞复现

**1.先验证shiro漏洞是否存在，登陆页面存在记住我的功能大概率是存在shiro反序列化的。**<br/>  

<br/>**2.通过burp去抓包验证查看返回包，存在rememberme=deleteme**

<br/>**3.废话不多说直接上工具去爆破密钥**

<br/>**4.直接获取到权限命令执行**

### 三、工具介绍

**该款工具特别适合初学者，配置了各种OA漏洞利用板块，还有shiro、struts2等框架漏洞的漏洞利用板块，还有一键执行命令的功能！！**

### 四、shiro反序列化漏洞的修复

**方案1：升级shiro至最新版本1.7.1**<br/> 密钥硬编码问题存在于1.2.4版本及以下。通过观察最新版本1.7.1的源代码发现,如果不指定密钥shiro会初始化一个随机密钥，由于密钥是随机生成的，所以攻击者没办法猜测到密钥。<br/> **方案2：保持shiro版本不变

### 五工具分享

[阿里云盘分享<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://www.aliyundrive.com/s/qXnvT6nRZAa](https://www.aliyundrive.com/s/qXnvT6nRZAa)<br/>`提取码:33hu`

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/726cb462be7d4683b33a170f9d631604.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/eabe33ce4cd04c53a7366765aa932a4f.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/4e33444dd3124b509bb5272bf4c04f61.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/d843d64e82de4856aabaa2bcdd2ebb5b.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/281cc5eb27e54f59866cffd2b6053af6.png" width="665"/>

应急响应笔记

学习路线
