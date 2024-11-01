# 原创
：  哈希处理介绍-使用Mimikatz以及John对Windows用户密码破解

# 哈希处理介绍-使用Mimikatz以及John对Windows用户密码破解

## 一、哈希处理介绍

Windows系统使用两种算法对用户的密码进行哈希处理， 它们分别是LM-hash算法和NTLMhash算法。

所谓哈希(hash) ， 就是使用一种加密函数对其进行加密。这个加密函数对一个任意长度的字符串数据进行一次数学加密函数运算，然后返回一个固定长度的字符串。

Windows的系统密码hash默认情况下一般由两部分组成：第一部分是LM-hash， 第二部分是NTLM-hash。

通常可从Windows系统中的SAM文件和域控制器的NTDS.dit文件中获得所有用户的hash。

黑客可以使用很多工具抓取Windows的密码hash或直接破解hash获得明文密码。这些工具有：mimi katz、pw dump 7、Quarks pw dump、SAM Inside等。

## 二、使用Mimikatz获取Windows用户密码

### 1.“Mimikatz”的介绍

Mimikatz是一款功能强大的轻量级调试神器，通过它你可以提升进程权限注入进程读取进程内存，当然他最大的亮点就是他可以直接从Isass.exe进程中获取当前登录系统用户名的密码。

Isass是微软Windows系统的安全机制，它主要用于本地安全和登陆策略，通常我们在登陆系统时输入密码之后，密码便会储存在lsass内存中，经过其wdigest和tspkg两个模块调用后，对其使用可逆的算法进行加密并存储在内存之中。

而Mimikatz正是通过对Isass逆算获取到明文密码，也就是说只要你不重启电脑，就可以通过他获取到登陆密码，只限当前登陆系统。

### 2.“Mimikatz”的使用
1. 杀毒软件认为Mimikatz.exe执行程序为病毒， 请务必关闭任何杀毒软件即windows系统防护。1. 将Mimikatz.exe拖入虚拟机内解压。1. 提升至debug权限（右键Mimikatz.exe以管理员身份运行）在提示符下，输入命令"privilege::debug”。1. 输入抓取密码命令"sekurlsa::logonpasswords"。可以看到本机面已经获取， 同时还解析出账户的SID、NL TM等关键信息。
补充：值得注意的是当主机安装了KB2871997补丁或者系统版本大于Windows server 2012时， 系统的内存中就不再保存明文的密码，这样利用mimi katz就不能从内存中读出明文密码了，除非修改注册表，然后用户在重新登录。

详细操作过程如下：
1. 右键左下角徽标，打开“命令提示符（管理员）”，执行“reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f”命令添加注册表。1. 注销后使用Mimikatz.exe抓取明文密码。
## 三、使用获取Jhon获取Windows用户密码

### 1.“Jhon”的介绍

John the Ripper是一个快速的密码破解工具， 该工具用于在已知密文的情况下尝试破解出明文， 其支持目前大多数的加密算法包括：DES、MD 4、MD 5等。

同时， 它还支持多种不同类型的系统架构， 包括：Unix、Linux、Windows、DOS模式等。除了在各种Unix系统上最常见的几种密码哈希类型之外， 它还支持Windows LM散列， 以及社区增强版本中的许多其他哈希和密码。该工具是一款Kali Linux系统自带的开源软件。

### 2.“Jhon”的使用
1. 打开命令提示符后先通过“cd c:\”命令退出到“c:\&gt;”。1. 执行命令“reg save hklm\sam sam.hive”和“reg save hklm\system system.hive”通过reg的save选项将注册表中的SAM、System文件导出到本地磁盘(该步骤需要用户具有管理员权限)。1. 把sam.hive和system.hive两个文件粘贴到kali的Desktop内。1. 执行以下如图所示的命令来查看这两个文件：1. 执行命令“samdump2 system.hive sam.hive &gt; hash.txt”将哈希提取到hash.txt文件中（其使用了sam dump 2工具将sam数据库文件破解成可识别的NTLM hash）。1. 查看hash.txt1. 使用John破解NTLM hash。用命令“john-format=NT hash.txt”使用Jhon自带的字典碰撞hash值进行破解。1. 使用命令“john--show-format=NT hash.txt”查看破解结果。
### 3.注意

破解过的用户的密码保存在/home文件夹下的隐藏文件./john/john.pot里,删除后才可以再次运行。操作过程如下:
