# 原创
：  SRC之若依系统恰分攻略-3

# SRC之若依系统恰分攻略-3

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


### 前言

---


本文将介绍一些奇怪情况下若依系统恰分druid的场景

#### 权限校验回显500

该回显不是严格意义上服务器回显500，与之前遇到的回显401弱校验类似

拼接了/druid/login.html

 一看图标，尝试若依弱口令 123456 直接进去了

** 进系统捡漏硬恰**

有时候/druid/login.html界面是无法直接访问到的，进行了权限校验，要登录系统才可以

那我们需要获取权限，最好的方法是先登录若依<img alt="" height="280" src="https://img-blog.csdnimg.cn/c9b737fa5321441c93e701b773bb6c41.png" width="1080"/>往往大部分能直接登录若依的弱口令被恰的差不多了，我们可以进系统恰druid，这是大部分人忽略的地方

<img alt="" height="433" src="https://img-blog.csdnimg.cn/ceae0173255c4070b9676e196b5ecbcd.png" width="1080"/>往往内嵌在系统数据监控中，这是一种捡漏的方法 

**没看够~？欢迎关注！**

**  **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
