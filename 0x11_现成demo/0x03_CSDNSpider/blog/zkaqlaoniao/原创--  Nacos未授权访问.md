# 原创
：  Nacos未授权访问

# Nacos未授权访问

**漏洞描述**<br/> Nacos 是阿里巴巴推出来的一个新开源项目，是一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。致力于帮助发现、配置和管理微服务。Nacos 提供了一组简单易用的特性集，可以快速实现动态服务发现、服务配置、服务元数据及流量管理。<br/> 该漏洞发生在nacos在进行认证授权操作时，会判断请求的user-agent是否为”Nacos-Server”，如果是的话则不进行任何认证。开发者原意是用来处理一些服务端对服务端的请求。但是由于配置的过于简单，并且将协商好的user-agent设置为Nacos-Server，直接硬编码在了代码里，导致了漏洞的出现。并且利用这个未授权漏洞，攻击者可以获取到用户名密码等敏感信息。<br/>**漏洞危害**<br/> 通过版本漏洞，攻击者可以在不登陆系统的情况下读取已存在的用户或者添加用户，进而登陆系统，登陆系统后可获取大量配置信息以发起进一步攻击。<br/>**影响范围**<br/> Nacos &lt;= 2.0.0-ALPHA.1<br/>**环境搭建**<br/> 用的是在kali虚拟机中使用vulhub复现：<br/> 进入环境：<br/> cd vulhub/nacos/CVE-2021-29441<br/> 启动环境：<br/> docker-compose build<br/> docker-compose up -d<br/> 查看环境：<br/> docker-compose ps<br/> 访问环境：<br/>[http://ip:端口/nacos/#/login](http://ip/nacos/#/login)<br/> 默认端口号一般是：8848

<br/>**漏洞复现：**<br/> 这里就用线上现成的靶场了。<br/>**1、查看用户列表（包含密码）**<br/> 访问该路径可以查看到nacos目前已经注册过的账号和加密后的密码：<br/>[http://靶场ip/nacos/v1/auth/users?pageNo=1&amp;pageSize=1](http://xn--ip-bn8c494v/nacos/v1/auth/users?pageNo=1&amp;pageSize=1)<br/>  

<br/> 可以看到有nacos账户 密码为加盐后的密码。<br/>**新增用户**<br/> 火狐浏览器开启代理，burp抓包放入重放攻击模块<br/>  

<br/>**修改数据包**<br/> 修改数据包进行重放攻击：<br/> get请求变更为post请求<br/> 用户代理user-agent改为Nacos-Server<br/> 伪造用户：/xxx/xxx?username=test1&amp;password=test1<br/> 用户名：test1，密码：test1<br/>  

<br/> 访问[http://靶场ip/nacos/v1/auth/users?pageNo=1&amp;pageSize=10，有新添加好的账户](http://xn--ip-bn8c494v/nacos/v1/auth/users?pageNo=1&amp;pageSize=10%EF%BC%8C%E6%9C%89%E6%96%B0%E6%B7%BB%E5%8A%A0%E5%A5%BD%E7%9A%84%E8%B4%A6%E6%88%B7)<br/>  

<br/>**登录账户**<br/>  

<br/>  

<br/> 拿到flag值

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/7256d0bb34e34d479f89c529df46cb4a.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/45a0ea313e72443d9f8e89f1fc828586.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/ccf8113f909641f6a62fc2f95158d3ef.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/b6fc2e2c498d464a8cd835aa9d59e6ec.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/5a0caab7c536491cb30dde7b4079310d.png" width="665"/>

应急响应笔记

学习路线
