# 原创
：  【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(上)：构建匿名FTP扫描器

# 【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(上)：构建匿名FTP扫描器

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
（1）构建匿名FTP扫描器（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|抓肉鸡博文|目标|状态
|[【Python脚本进阶】利用FTP与Web批量抓“ 肉机”(上)：构建匿名FTP扫描器](https://blog.csdn.net/qq_53079406/article/details/126052839)|构建匿名FTP扫描器|已发布
|[【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(中)：使用Ftplib暴力破解FTP用户口令](https://blog.csdn.net/qq_53079406/article/details/126053636)|使用Ftplib暴力破解FTP用户口令|已发布
|[【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(下)：在FTP服务器上搜索网页+注入代码](https://blog.csdn.net/qq_53079406/article/details/126060388)|在FTP服务器上搜索网页+注入代码|已发布
|[【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(终）](https://blog.csdn.net/qq_53079406/article/details/126076401)|利用FTP与Web批量抓肉机|已发布
</tbody></table>



---


**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、历史：](#1.1%E3%80%81%E5%8E%86%E5%8F%B2%EF%BC%9A)

[1.2、分析：](#1.2%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[1.3、基础知识：](#1.3%E3%80%81%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%EF%BC%9A)

[二、构建匿名FTP扫描器](#%E4%BA%8C%E3%80%81%E6%9E%84%E5%BB%BA%E5%8C%BF%E5%90%8DFTP%E6%89%AB%E6%8F%8F%E5%99%A8)

[2.1、概述：](#2.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[2.2、函数：](#2.2%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、实现：](#2.3%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、历史：</h3>
一次被称为k985ytv 的批量入侵中， 攻击者使用了FTP 的匿名账户和偷来的用户名／密码获得了22400 个不同站点的控制权， 并在536000 个网页上挂了马(Huang,2011) 。利用获得的访问权限， 攻击者注入了一段JavaScript 代码， 将正常的网页重定向到乌克兰的一个恶意网站那里。一旦被黑掉的网站把浏览它的用户重定向到乌克兰的那台恶意主机那里之后， 恶意主机就会利用浏览器中的漏洞， 安装假的用来窃取用户信用卡信息的“ 防病毒程序” 。这次k985ytv 攻击最终取得了巨大的成功。


> 
<h3>1.2、分析：</h3>
通过检查被黑服务器的FTP 日志，某个自动执行的脚本先连接到目标主机， 攻击者上传一个新的含有恶意重定向脚本的index.htm。被黑掉的服务器就能给任何一台访问其网页的有漏洞的浏览器种木马。


> 
<h3>1.3、基础知识：</h3>
文件传输协议(FTP) 服务允许用户在一个基于TCP 的网络主机间传输文件。通常情况下， 用户使用用户名和相应的密码登录FTP 服务器。一些FTP 服务器提供匿名登录的能力。在这种情况下， 用户输入用户名“anonymous", 并提交一个电子邮件地址代替密码。


---


---


## 二、构建匿名FTP扫描器

> 
<h3>2.1、概述：</h3>
网站允许匿名FTP 访问是不安全的。但是许多网站为此提供的正当理由却是： 匿名FTP 访问有助于网站访问软件更新。


> 
<h3>2.2、函数：</h3>
ftp_login() ：登录 FTP 服务器，如果成功，该函数返回 TRUE。如果失败，则返回 FALSE 和一个警告。语法：ftp_login(ftp_connection,username,password)
<hr/>
FTP.quit ()：向服务器发送 QUIT 命令并关闭连接


> 
<h3>2.3、实现：</h3>
利用Python 中的ftplib 库编写一个小脚本， 确定一个服务器是否允许匿名登录。anonLogin()函数接收的参数是一个主机名， 并返回一个布尔值来描述该主机是不是提供匿名FTP 登录。具体的操作过程是， 该函数尝试建立一个匿名FTP 连接。如果成功， 则返回'true" 。如果在建立连接的过程中函数抛出了一个异常， 则返回“False" 。
<hr/>
运行 python anonLogin.py
<pre><code>import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'password')
        print('\n(*) ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('[*]' + str(e))
        print('\n[-]' + str(hostname) + 'FTP Anonymous Logon Failed.')
        return False
host = '192.168.190.131'
anonLogin(host)</code></pre>


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

