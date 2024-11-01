# 原创
：  【kali-密码攻击】（5.1.2）密码在线破解：Medusa

# 【kali-密码攻击】（5.1.2）密码在线破解：Medusa

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
（1）基于密码攻击工具的使用（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

<br/>  

---


**目录**

[一、密码在线破解](#%E4%B8%80%E3%80%81%E5%AF%86%E7%A0%81%E5%9C%A8%E7%BA%BF%E7%A0%B4%E8%A7%A3)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、Medusa](#%E4%BA%8C%E3%80%81Medusa)

[2.1、启动Medusa工具](#2.1%E3%80%81%E5%90%AF%E5%8A%A8Medusa%E5%B7%A5%E5%85%B7)

[2.2、语法：](#2.2%E3%80%81%E8%AF%AD%E6%B3%95%EF%BC%9A)

[2.3、命令：](#2.3%E3%80%81%E5%91%BD%E4%BB%A4%EF%BC%9A)

[2.4、支持的服务：](#2.4%E3%80%81%E6%94%AF%E6%8C%81%E7%9A%84%E6%9C%8D%E5%8A%A1%EF%BC%9A)

[2.5、示例：](#2.5%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 一、密码在线破解

> 
<h3>1.1、概述：</h3>
Medusa工具是通过并行登录暴力破解的方法，尝试枷取远程验证服务访问权限。
Medusa能够验证的远程服务， 如AFP、FTP 、HTTP、IM战、MSSQL 、NetWare、NNTP、PcAnyWhere 、POP3 、REXEC 、RLOGIN 、SMTPAUTH 、SNMP 、SSHv2 、Telnet 、VNC和Web Form等


---


---


## 二、Medusa

> 
<h3>2.1、启动Medusa工具</h3>
终端输入medusa
或者直接打开


输出的信息显示了medusa命令的帮助信息。包括meduas命令的语法、可使用的选项及参数



> 
<h3>2.2、语法：</h3>
Medusa [-h host|-H file] [-u username|-U file] [-p password|-P file] [-C file] -M module [OPT]
<hr/>
<h3>2.3、命令：</h3>
<pre><code>参数	  含义
-h	  目标主机名称或是IP地址
-H	  包含目标主机名称或是IP地址的文件绝对路径
-u	  测试用户名
-U	  包含测试用户名的文件绝对路径
-p	  测试用户名密码
-P	  包含测试用户名密码的文件绝对路径
-C	  组合条目文件的绝对路径
-O	  日志信息文件的绝对路径
-e[n/s/ns]	n代表空密码，s代表为密码与用户名相同
-M	  模块执行mingc
-m	  传递参数到模块
-d	  显示所有模块名称
-n	  使用非默认TCP端口
-s	  启用ssl
-r	  重试时间，默认3秒
-t	  设定线程数量
-T	  同时测试的主机总数
-L	  并行化，每个用户使用一个线程
-f	  在任何主机上找到第一个账号/密码后，停止破解
-F	  在任何主机上找到第一个有效的用户名/密码后停止审计
-q	  显示模块的使用信息
-v	  详细级别（0-6）
-w	  错误调试级别（0-10）
-V	  显示版本
-Z	  恢复之前终端的扫描</code></pre>


### 2.3、命令：

> 
<h3>2.4、支持的服务：</h3>



> 
<h3>2.5、示例：</h3>
使用字典对目标进行破解
mesuda -h 192.168.190.149 -U user.txt -P password.txt -n 40  -M ssh -f -t 5 -O ssh.txt
-h      目标主机名称或是IP地址
-u      测试用户名
-p      测试用户名密码
-n      使用非默认TCP端口
-M      模块执行mingc
-f      在任何主机上找到第一个账号/密码后，停止破解
-t      设定线程数量
-O    （输出）日志信息文件的绝对路径


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

