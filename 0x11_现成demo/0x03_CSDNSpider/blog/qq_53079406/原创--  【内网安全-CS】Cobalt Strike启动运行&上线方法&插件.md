# 原创
：  【内网安全-CS】Cobalt Strike启动运行&上线方法&插件

# 【内网安全-CS】Cobalt Strike启动运行&amp;上线方法&amp;插件

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
（1）学会cs的基本使用方法（√）
（2）cs插件的使用（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|内网博文|目标|状态
|[【内网安全-CS】Cobalt Strike启动运行&amp;上线方法&amp;插件](https://blog.csdn.net/qq_53079406/article/details/128371064)|学会cs的基本使用方法、以及插件|已发布
|[【内网安全-基础】基础知识、信息收集、工具](https://blog.csdn.net/qq_53079406/article/details/128292587)|基础知识、基础常规信息收集（命令、工具等）|已发布
|[【内网安全-防火墙】防火墙、协议、策略](https://blog.csdn.net/qq_53079406/article/details/128314938)|防护墙的基础知识、出入站策略等|已发布
|[【内网安全-通讯&amp;上线】通讯&amp;上线基础知识](https://blog.csdn.net/qq_53079406/article/details/128320574)|基础知识、通讯、上线、代理|已发布
|[【内网安全-隧道技术】SMB、ICMP、DNS隧道、SSH协议](https://blog.csdn.net/qq_53079406/article/details/128328429)|常用的上线方法|已发布
|隧道搭建、穿透上线|2023将继续更新，敬请期待|——
|横向移动|2023将继续更新，敬请期待|——
|权限维持|2023将继续更新，敬请期待|——
|靶场练习|2023将继续更新，敬请期待|——
</tbody></table>


​​​​​​​

---


**目录**

[一、启动运行](#%E4%B8%80%E3%80%81%E5%90%AF%E5%8A%A8%E8%BF%90%E8%A1%8C)

[1、第一步：进入cs目录](#1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%BF%9B%E5%85%A5cs%E7%9B%AE%E5%BD%95)

[2、第二步：查看本机ip](#2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%9C%AC%E6%9C%BAip)

[3、第三步：启动"团队服务器"](#3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8%22%E5%9B%A2%E9%98%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%22)

[4、第四步：客户端连接](#4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%BF%9E%E6%8E%A5)

[二、上线方法](#%E4%BA%8C%E3%80%81%E4%B8%8A%E7%BA%BF%E6%96%B9%E6%B3%95)

[1、第一步：生成监听器](#1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90%E7%9B%91%E5%90%AC%E5%99%A8)

[2、第二步：生成木马](#2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90%E6%9C%A8%E9%A9%AC)

[3、第三步：上线](#3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E4%B8%8A%E7%BA%BF)

[三、加载插件](#%E4%B8%89%E3%80%81%E5%8A%A0%E8%BD%BD%E6%8F%92%E4%BB%B6)

[1、常用插件：](#1%E3%80%81%E5%B8%B8%E7%94%A8%E6%8F%92%E4%BB%B6%EF%BC%9A)

[2、加载步骤：](#2%E3%80%81%E5%8A%A0%E8%BD%BD%E6%AD%A5%E9%AA%A4%EF%BC%9A)

---


> 
<h2>一、启动运行</h2>
环境：linux+Cobalt Strike目录
<h3>1、第一步：进入cs目录</h3>
在cs目录打开终端


<hr/>
<hr/>
<h3>2、第二步：查看本机ip</h3>
Linux是ifconfig（ipconfig是window中的）



<hr/>
<hr/>
<h3>3、第三步：启动"团队服务器"</h3>
在cs目录中启动"团服务器teamserver"
./teamserver  ip  密码


<hr/>
<hr/>
<h3>4、第四步：客户端连接</h3>
（客户端可以在Linux中启动，也可以在windows中启动）
Linux：./cobaltstrike


windows:双击exe文件（或者bat批处理文件）


Alias：为别称，随便写
host：填写团服务器ip
port：默认50050
user：随便写
Password：启动团服务器时候设置的密码

第一次登陆会校验hash
 <img alt="" height="187" src="https://img-blog.csdnimg.cn/9041023575034bc4bb2669c7db81229d.png" width="583"/>
 客户端启动成功




---


### 2、第二步：查看本机ip

---


---


### 4、第四步：客户端连接

> 
<h2>二、上线方法</h2>
<h3>1、第一步：生成监听器</h3>


 <img alt="" height="592" src="https://img-blog.csdnimg.cn/df8687365be14547b88f2eaa1653b7fc.png" width="1200"/>

Name：命名
Payload：选类型
HTTP Hosts：反弹shell的主机，填kali的ip
HTTP Hosts（Stager）：Stager的马请求下载payload的地方
HTTP Port（c2）：c2监听的端口
 <img alt="" height="612" src="https://img-blog.csdnimg.cn/dbf0dc24ed1d459c9041a6052e64f866.png" width="472"/>
 <img alt="" height="123" src="https://img-blog.csdnimg.cn/32ac4d5111db48c4a7b3bfca764edc79.png" width="264"/>
 <img alt="" height="592" src="https://img-blog.csdnimg.cn/2385211d66ad4138b57ad660cca52535.png" width="784"/>

<hr/>
<hr/>
<h3>2、第二步：生成木马</h3>
木马生成（我用的魔改版的，原版的是Attacks-&gt;Packages-&gt;HTML Application）



 <img alt="" height="415" src="https://img-blog.csdnimg.cn/fb04f544ddb342ca9e21f1c0ae5079cf.png" width="622"/>
 <img alt="" height="125" src="https://img-blog.csdnimg.cn/594d137f93324b2b989f22afcc63225a.png" width="302"/>

<hr/>
<hr/>
<h3>3、第三步：上线</h3>
点击创建后会生成一个名为artifact.exe的文件，在受害机上运行后可直接在客户端看见目标上线


执行以后，可以在Cobalt Strike的日志里面看到一条日志，在Cobalt Strike 的主页面中可以看到一台机器上线

 <img alt="" height="592" src="https://img-blog.csdnimg.cn/8f6c4afbf0d7476397abe5a3e60fc365.png" width="784"/>
进一步的利用




---


### 2、第二步：生成木马

---


> 
<h2>三、加载插件</h2>
<h3>1、常用插件：</h3>

<hr/>
<h3>2、加载步骤：</h3>
第一步：点击 CobaltStrike---&gt; 脚本管理器---&gt;Load



 ————
第二步：加载脚本
然后选择.cna后缀的文件进行加载




### 2、加载步骤：

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

