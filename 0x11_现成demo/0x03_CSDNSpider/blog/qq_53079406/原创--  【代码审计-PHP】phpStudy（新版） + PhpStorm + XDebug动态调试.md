# 原创
：  【代码审计-PHP】phpStudy（新版） + PhpStorm + XDebug动态调试

# 【代码审计-PHP】phpStudy（新版） + PhpStorm + XDebug动态调试

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
（1）PHPStudy环境（√）
（2）PhpStorm（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|审计博文|类型|状态
|[【代码审计-PHP】phpStudy（新版） + PhpStorm + XDebug动态调试](https://blog.csdn.net/qq_53079406/article/details/127728220)|PHP|已发布
|[【代码审计-PHP】审计方法、敏感函数、功能点](https://blog.csdn.net/qq_53079406/article/details/127819601)|PHP|已发布
|[【代码审计-PHP】基于Thinkphp框架开发的](https://blog.csdn.net/qq_53079406/article/details/127826862)|PHP|已发布
|[【代码审计-.NET】基于.NET框架开发的基本特征](https://blog.csdn.net/qq_53079406/article/details/128257403)| .NET |已发布
|[【代码审计-.NET】基于.NET框架开发的代码审计](https://blog.csdn.net/qq_53079406/article/details/128262502)|.NET|已发布
|[【代码审计-JAVA】基于javaweb框架开发的](https://blog.csdn.net/qq_53079406/article/details/128267950)|JAVA|已发布
|[【代码审计-JAVA】javaweb代码审计思路](https://blog.csdn.net/qq_53079406/article/details/128270053)|JAVA|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、PHPStudy环境](#%E4%B8%80%E3%80%81PHPStudy%E7%8E%AF%E5%A2%83)

[1.1、版本:](#1.1%E3%80%81%E7%89%88%E6%9C%AC%3A)

[1.2、步骤: ](#1.2%E3%80%81%E6%AD%A5%E9%AA%A4%3A%C2%A0)

[二、PhpStorm](#%E4%BA%8C%E3%80%81PhpStorm)

[2.1、PHP源码](#2.1%E3%80%81PHP%E6%BA%90%E7%A0%81)

[2.2、PhpStorm配置](#2.2%E3%80%81PhpStorm%E9%85%8D%E7%BD%AE)

[2.3、Debug](#2.3%E3%80%81Debug)

---


## 一、PHPStudy环境

> 
<h3>1.1、版本:</h3>
PHP8.1.1.3-Apache2.4.39



> 
<h3>1.2、步骤: </h3>
(1)phpStudy ---&gt;网站---&gt; 管理---&gt; PHP扩展 ---&gt; Xdebug


(2)PHP.ini---配置文件---点击对应的php


低版本就是添加的XDbug(或者高版本就是修改)
<pre><code>[XDebug]
 
 
xdebug.profiler_append = 0
;效能监测的设置开关
xdebug.profiler_enable = 1
xdebug.profiler_enable_trigger = 0
;profiler_enable设置为1的时候，效能监测信息写入文件所在的目录
xdebug.profiler_output_dir="D:\BaiduNetdiskDownload\phpstudy\tmp\xdebug"
;设置的函数调用监测信息的输出路径
xdebug.trace_output_dir="D:\BaiduNetdiskDownload\phpstudy\tmp\xdebug"
;生成的效能监测文件的名字
xdebug.profiler_output_name ="cache.out.%t-%s"
; IDE与XDebug协作
xdebug.remote_enable = 1
xdebug.remote_handler = "dbgp"
xdebug.remote_host = "127.0.0.1"
xdebug.remote_port = 9000
xdebug.idekey = phpstorm-xdebug
;.dll文件的路径
zend_extension="D:\BaiduNetdiskDownload\phpstudy\phpstudy_pro\Extensions\php\php5.4.45nts\ext\php_xdebug.dll"</code></pre>





## 二、PhpStorm

> 
<h3>2.1、PHP源码</h3>
快速打开php文件方法
将php源码目录拖到phpstorm快捷键图标上


> 
<h3>2.2、PhpStorm配置</h3>
(1)PHP版本配置
File ---&gt;Settings


 languages &amp; Frameworks ---&gt; php

选择自己使用的PHP版本
 ​​​​​<img alt="" height="900" src="https://img-blog.csdnimg.cn/5222374bdc8140dba0efcdd539323b63.png" width="1200"/>



> 
<h3>2.3、Debug</h3>
(1)Debug端口
与php.ini中xdebug.remote_port值一致

<hr/>
(2)设置服务器

<hr/>
(3)配置host端口
IDE key 同 php.ini中xdebug. idekey
Port 同 php.ini中xdebug.remote_port
 最后点击ok

<hr/>
(4)Run---&gt; Edit Configurations

<hr/>
(5)点击新建(+)----PHP Web Application


<hr/>
(6)前提:是安装好的网站

或者可以在PHPMyAdmin直接新建数据库后导入.sql.zip格式文件
（也可直接终端操作）

<hr/>

(7)PHP Web Application配置
我发现配置的是8080端口
重新将Server端口改为8080端口
Name随便写，Server选择自己刚刚创建的那个
Start URL为开始路径，可以进行点击下面的链接进行预览



<hr/>
(8)点击进行预览<img alt="" height="874" src="https://img-blog.csdnimg.cn/d6b2c26e43984d949d0edea66cb0a8e6.png" width="1200"/>
<hr/>
(9)打开监听（图中表示已经开启监听）

<hr/>
(10)打断点

<hr/>
(11)点击调试
 <img alt="" height="203" src="https://img-blog.csdnimg.cn/2f93342963b54f62abd4df53d2078894.png" width="367"/>
<hr/>
(12)对应的效果图<img alt="" height="276" src="https://img-blog.csdnimg.cn/1c2f1da5fbe94857af42ba26ec82a618.png" width="1003"/>
 <img alt="" height="359" src="https://img-blog.csdnimg.cn/10ac2f368742421a94eaa7d7009065f3.png" width="1139"/>



---


---


---


---


---


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
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

