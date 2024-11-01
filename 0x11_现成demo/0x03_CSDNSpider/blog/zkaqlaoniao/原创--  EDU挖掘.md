# 原创
：  EDU挖掘

# EDU挖掘

### 1.信息搜集

没事干，准备找个证书站挖挖看，没想到碰到一个小通用系统。<br/> 看样子还挺多功能可以测，

这里利用F12 查看前端源码js 或者css文件，直接用hunter或者fofa搜索到同一类型的网站。<br/> Hunter语法：web.body=”styles.0205b85caa51097542ba.bundle.css”

我水平有限挖不到太多，剩下就看你们了，直接去挖挖看哦。

### 2.漏洞挖掘

首先是找到一个未授权的接口，一开始通过bp 的历史记录找到的，就是要仔细看啊！<br/>[http://ip:8080/pmis/getOrganizationSelectInfo](http://ip:8080/pmis/getOrganizationSelectInfo) （后面通过nmap扫描端口，发现不同端口有不同的后台。嘿嘿！）

通过这个接口里面的敏感信息泄露，随便找到一个注册的用户手机，就可以去测试了忘记密码这个点

通过抓包修改返回码，绕过验证码 code改成0 data改成true

<br/> 这样就可以任意更改用户密码<br/>  

<br/> 找到account，尝试新密码登陆<br/>  

<br/> 登陆成功，完结撒花！！

**没看够~？欢迎关注！**<img alt="" height="567" src="https://img-blog.csdnimg.cn/f86102ca146d4bdaa6d098991c6e7216.jpeg" width="1015"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/af9db44a09ef4ece9a9acd2b43baefc3.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/03490a919e2a4e02a6663374ff80bb71.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/f7004f5ea63740528f6c430e62b80fc1.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/f03dfc3f02164ccea224765f69a60f51.png" width="665"/>
