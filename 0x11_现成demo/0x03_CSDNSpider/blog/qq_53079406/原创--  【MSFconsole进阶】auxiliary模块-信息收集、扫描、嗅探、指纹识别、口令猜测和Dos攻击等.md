# 原创
：  【MSFconsole进阶】auxiliary模块：信息收集、扫描、嗅探、指纹识别、口令猜测和Dos攻击等

# 【MSFconsole进阶】auxiliary模块：信息收集、扫描、嗅探、指纹识别、口令猜测和Dos攻击等

**目录**

[auxiliary（辅助模块）](#auxiliary%EF%BC%88%E8%BE%85%E5%8A%A9%E6%A8%A1%E5%9D%97%EF%BC%89)

[一、介绍：](#%E4%B8%80%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、提示：](#%E4%BA%8C%E3%80%81%E6%8F%90%E7%A4%BA%EF%BC%9A)

[三、信息收集：](#%E4%B8%89%E3%80%81%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%EF%BC%9A)

[3.1、使用过程：](#3.1%E3%80%81%E4%BD%BF%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[3.2、示例](#3.2%E3%80%81%E7%A4%BA%E4%BE%8B)

[四、端口扫描](#%E5%9B%9B%E3%80%81%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[4.1、使用过程](#4.1%E3%80%81%E4%BD%BF%E7%94%A8%E8%BF%87%E7%A8%8B)

[五、探测服务详细信息](#%E4%BA%94%E3%80%81%E6%8E%A2%E6%B5%8B%E6%9C%8D%E5%8A%A1%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF)

[六、服务查点](#%E5%85%AD%E3%80%81%E6%9C%8D%E5%8A%A1%E6%9F%A5%E7%82%B9)

[6.1、介绍：](#6.1%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[6.2、SSH服务扫描](#6.2%E3%80%81SSH%E6%9C%8D%E5%8A%A1%E6%89%AB%E6%8F%8F)

[6.3、Telnet服务扫描](#6.3%E3%80%81Telnet%E6%9C%8D%E5%8A%A1%E6%89%AB%E6%8F%8F)

[其他服务查点](#%E5%85%B6%E4%BB%96%E6%9C%8D%E5%8A%A1%E6%9F%A5%E7%82%B9)

[七、口令猜测](#%E4%B8%83%E3%80%81%E5%8F%A3%E4%BB%A4%E7%8C%9C%E6%B5%8B)

[7.1、字典（也可自己下载）](#7.1%E3%80%81%E5%AD%97%E5%85%B8%EF%BC%88%E4%B9%9F%E5%8F%AF%E8%87%AA%E5%B7%B1%E4%B8%8B%E8%BD%BD%EF%BC%89)

[7.2、口令爆破：SSH](#7.2%E3%80%81%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4%EF%BC%9ASSH)

[7.3、其他服务口令猜解](#7.3%E3%80%81%E5%85%B6%E4%BB%96%E6%9C%8D%E5%8A%A1%E5%8F%A3%E4%BB%A4%E7%8C%9C%E8%A7%A3)

[八、网站敏感目录扫描](#%E5%85%AB%E3%80%81%E7%BD%91%E7%AB%99%E6%95%8F%E6%84%9F%E7%9B%AE%E5%BD%95%E6%89%AB%E6%8F%8F)

[九、扫描内网中存在特定目录的主机](#%E4%B9%9D%E3%80%81%E6%89%AB%E6%8F%8F%E5%86%85%E7%BD%91%E4%B8%AD%E5%AD%98%E5%9C%A8%E7%89%B9%E5%AE%9A%E7%9B%AE%E5%BD%95%E7%9A%84%E4%B8%BB%E6%9C%BA)

---


---


 

## auxiliary（辅助模块）

> 
<h3>一、介绍：</h3>
负责执行信息收集、扫描、嗅探、指纹识别、口令猜测和Dos攻击等功能
（功能特别多，要摸索完，革命尚未成功，同志仍需努力）




> 
<h3>二、提示：</h3>
在使用大多数命令的时候，都需要管理员权限
需要先进入到root权限下
输入su root再输入密码

（单一的命令，可以考虑使用sudo命令）



> 
<h3>三、信息收集：</h3>
<h4>3.1、使用过程：</h4>
 第一步：
进入到管理模式下
sudo root

<hr/>
第二步：
再进入到msfconsole

输入：
use auxiliary/scanner/discovery/

 有0-7（一共7个信息收集的脚本）
Interact with a module by name or index. For example info 6, use 6 or use auxiliary/scanner/discovery/udp_sweep<br/> 通过名称或索引与模块进行交互。
<hr/>
例如
use 6
use auxiliary/scanner/discovery/udp_sweep
（下面的使用模块方法都一样）
<hr/>
<h4>3.2、示例</h4>
**选择模块**
use auxiliary/scanner/discovery/arp_sweep
show options

** **
**设置**
set RHOSTS 192.168.1.1/24  #设置网段
set threads 50   #设置线程数50，设置少了要等半天
run  #运行

我扫的结果是：
You don't have permission to capture on that device
（您无权在该设备上捕获）
（这是我之前忘记进入到管理员模式）


---


#### 3.2、示例

> 
<h3>四、端口扫描</h3>
<h4>4.1、使用过程</h4>
第一步：
进入到管理模式下
sudo root

<hr/>
第二步：
再使用msfconsole
 
use auxiliary/scanner/portscan/
#查看可用模块

<hr/>
use auxiliary/scanner/portscan/syn
#选择模块
show options
#显示选项

<hr/>

set RHOSTS 192.168.190.131
set PORTS 1-65535
#全部扫描需要很长时间
set threads 50000
#设置线程，设置少了要等半天
run

You don't have permission to capture on that device
（您无权在该设备上捕获）
 （我没有进入到管理员模式）
<hr/>
进入管理员模式下后结果：

 


---


---


> 
<h3>五、探测服务详细信息</h3>

sudo nmap A -p- -sS sC -T4 -Pn 192.168.1.1




 

> 
<h3>六、服务查点</h3>
<h4>6.1、介绍：</h4>
在metasploit中scanner辅助模块中服务扫描和查点工具
命名方法：
[service_name]_version（遍历网络中包含了某种服务的主机）
[service_name]_login（对某种服务进行口令探测攻击）

<hr/>
<h4>6.2、SSH服务扫描</h4>
**选择模块**
search ssh_version


auxiliary/scanner/ssh/ssh_version
选择，或者使用use 3
show options

<hr/>
**设置**

set RHOSTS 192.168.190.131/24
#设置自己要扫描的网段
set threads 50 #设置线程数50
run


<hr/>

<h4>6.3、Telnet服务扫描</h4>
**第一步：选择模块**
search telnet_version
use auxiliary/scanner/telnet/telnet_version

**第二步： 设置**
设置网段，线程，运行


<hr/>

<h4>其他服务查点</h4>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|服务|模块
|oracle服务扫描|use auxiliary/scanner/oracle/tnslsnr_version
|mssql扫描|use auxiliary/scanner/mssql/mssql_ping
|mysql扫描|use auxiliary/scanner/mysql/mysql_version
|ftp扫描|use auxiliary/scanner/ftp/ftp_version
|http扫描|use auxiliary/scanner/http/http_version
</tbody></table>



#### 6.2、SSH服务扫描

---


---


#### 其他服务查点

> 
<h3>七、口令猜测</h3>
<h4>7.1、字典（也可自己下载）</h4>
/usr/share/wordlists #kail中位置

<hr/>
<h4>7.2、口令爆破：SSH</h4>
**第一步：选择模块**
search ssh_login
auxiliary/scanner/ssh/ssh_login
（show option）


**第二步：设置**
set RHOST 192.168.190.131
set USERname kail
set PASS_FILE /home/kali/tools/wordlist/top3000.txt
#路径为字典位置，这是我自己下载的字典
run


<hr/>

<h4>7.3、其他服务口令猜解</h4>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|口令猜解|模块
|telnet|use auxiliary/scanner/telnet/telnet_login
|mssql|use auxiliary/scanner/mssql/mssql_login
|smb|use auxiliary/scanner/smb/smb_login
</tbody></table>




#### 7.2、口令爆破：SSH

---


> 
<h3>八、网站敏感目录扫描</h3>
**选择模块**
需要提供一个目录字典(kail中有)
use auxiliary/scanner/http/dir_scanner
show options


**设置**
set RHOST 192.168.190.131
set PATH /home/kali/tools/wordlist/(目录字典)
run

 可能是我使用的字典的原因，就出错了吧


> 
<h3>九、扫描内网中存在特定目录的主机</h3>
use auxiliary/scanner/smb/smb_ms17_010
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
<hr/>

host likely vulnerable to MS17-010
#存在这个漏洞，可利用攻击
host does not appear vulnerable
#不易受到攻击 / 不存在这个漏洞

