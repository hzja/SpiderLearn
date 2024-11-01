# 原创
：  【kali-密码攻击】（5.1.1）密码在线破解：Hydra（图形界面）

# 【kali-密码攻击】（5.1.1）密码在线破解：Hydra（图形界面）

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

---


**目录** 

[一、密码在线破解](#%E4%B8%80%E3%80%81%E5%AF%86%E7%A0%81%E5%9C%A8%E7%BA%BF%E7%A0%B4%E8%A7%A3)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、Hydra](#%E4%BA%8C%E3%80%81Hydra)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、使用：](#2.2%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

[第一步：启动Hydra](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8Hydra)

[第二步：接口设置](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%8E%A5%E5%8F%A3%E8%AE%BE%E7%BD%AE)

[第三步：字典设置](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%AD%97%E5%85%B8%E8%AE%BE%E7%BD%AE)

[第四步：基本设置](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%9F%BA%E6%9C%AC%E8%AE%BE%E7%BD%AE)

[第五步：攻击](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%94%BB%E5%87%BB)

---


## 一、密码在线破解

> 
<h3>1.1、概述：</h3>
为了使用户能成功登录到目标系统， 所以需要获取一个正确的密码。在Kali中， 在线破解密码的工具很多， 其中最常用的两款分别是Hydra和Medusa


---


---


## 二、Hydra

> 
<h3>2.1、简介：</h3>
Hydra是一个相当强大的暴力密码破解工具。该工具支持儿乎所有协议的在线密码破解， 如FTP、HTTP 、HTTPS、MySQL 、MS SQL、Oracle、Cisco、IMAP和VNC等。其密码能否被破解， 关键在于字典是否足够强大。很多用户可能对Hydra比较熟悉， 因为该工具有图形界面， 且操作十分简单， 基本上可以“ 傻瓜” 操作
<hr/>
在次之前肯定是端口扫描，去探测服务


> 
<h3>2.2、使用：</h3>
<h4>第一步：启动Hydra</h4>
下面这个是图形界面的

<hr/>
<h4>第二步：接口设置</h4>
配置目标系统的地址、端口和协议等
（如果要查看密码攻击的过程，将Output Options框中的Show Attempts复选框勾上）

<hr/>
<h4>第三步：字典设置</h4>
点击Passwords选项卡，指定用户名和密码列表文件
可以使用Kali系统中存在的用户名和密码列表文件， 并选择Loop around users 选项
用户名文件<br/> /usr/share/wfuzz/wordlist/others/names.txt
密码文件
/usr/share/wfuzz/wordlist/others/common_pass.txt
(上面是我文件kali自带列表所在位置，如果不一样的话，就在/usr/share/wfuzz/wordlist/往后找，或者网上下一个)

<hr/>
<h4>第四步：基本设置</h4>
点击Tuning选项卡
设置任务的编号和超时时间，避免运行任务太多，导致服务的响应速率下降
默认任务编号16修改为3,超时时间30改为15
将Exitafter first found pair（首先找到对的）勾上， 即找到第一对匹配项时停止攻击

<hr/>
<h4>第五步：攻击</h4>
点击Start 选项卡进行攻击
在该界面显示了四个按钮， 分别是启动、停止、保存输出和消除输出。这里点击Start 按钮开始攻击，




#### 第二步：接口设置

---


#### 第四步：基本设置

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

