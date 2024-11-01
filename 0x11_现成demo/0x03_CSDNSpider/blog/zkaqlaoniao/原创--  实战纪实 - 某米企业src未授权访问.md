# 原创
：  实战纪实 | 某米企业src未授权访问

# 实战纪实 | 某米企业src未授权访问

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


## 某米企业src漏洞挖掘

---


这一挖就挖到了一个未授权操作漏洞，写个文章记录下~~

通过信息收集，发现这么一个资产。<br/> 访问 http://xxx.com 如下图所示

1.点击头像-点击授权登录<img alt="" height="323" src="https://img-blog.csdnimg.cn/393e4bdf4b35475ab16f4b61d94d6d0a.png" width="1063"/>2.然后发现可删除大量授权的用户信息，总计全部1292条，最新时间实时更新<img alt="" height="550" src="https://img-blog.csdnimg.cn/7497a5c8128c4da4b6d088e5e747edc3.png" width="1080"/>发现可删除内部数据<img alt="" height="478" src="https://img-blog.csdnimg.cn/7ba87e5b93864f37a2a9260459d2fc96.png" width="1080"/>3.可授权所有用户登录<img alt="" height="553" src="https://img-blog.csdnimg.cn/e81c55bc72bf464ca7e49a30e261456f.png" width="1080"/><img alt="" height="472" src="https://img-blog.csdnimg.cn/d4d3d24f87664327ac3a6858213026a0.png" width="1080"/>

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
