# 原创
：  网络安全工具篇之Nmap中一些常用的脚本

# 网络安全工具篇之Nmap中一些常用的脚本

Nmap是最著名的渗透工具之一 ，一款标志性的跨平台扫描器。它的原意为Network Mapper（网络映射器），具有相当强大的扫描功能，几乎适用于任何渗透场景。不少人甚至认为它就是全球最好的扫描软件。除了常规的网络扫描，Nmap还可根据NSE (Nmap scripting Engine)的脚本进行大量渗透工作，这种脚本是基于Lua编程语言，有点像javascript。正是NSE，使得Nmap不再普通

首先，我们扫描目标主机，检测开放的端口：

```
root@kali:~# nmap site.test.lan
Starting Nmap 7.70 ( https://nmap.org ) at 2019–05–31 11:58 MSK
Nmap scan report for site.test.lan (192.168.60.50)
Host is up (0.000030s latency).
Not shown: 995 closed ports
PORT STATE SERVICE
21/tcp open ftp
22/tcp open ssh
80/tcp open http
90/tcp open dnsix
3306/tcp open mysql
MAC Address: 6E:93:12:AA:1F:6D (Unknown)
```

接着，让我们瞄准80端口，通常web服务就在这里。一旦启用Nmap中的http-enum脚本，它将收集web服务的所有有用的信息，就如漏洞扫描器Nikto一般:

> 
nmap site.test.lan --script http-enum


### **信息收集**

从上图中，我们可以了解到该站点使用了WordPress。于是，我们可以使用针对WordPress的脚本http-wordpress-enum进行深度扫描。这个脚本还会确定网站使用了多少和WordPress相关的插件。

> 
`nmap -p80 --sc ript http-wordpress-enum --script-args http-wordpress-enum.search-limit=all site.test.lan`


<img alt="" src="https://img-blog.csdnimg.cn/2d487fcc4df24957a1b5b7a0e89d2a84.jpg"/>一般来说，标准的Nmap中集成了近600个脚本，如果没有你需要的，也可以自己编写脚本。

### 权限

假如我们想在站点上寻找登录授权页面，还可使用如下脚本http-auth-finder

 <img alt="" src="https://img-blog.csdnimg.cn/27e79301cfa64b4dbc755c02e2fd36df.jpg"/>

你也可以使用命令参数–script=auth，所有和授权有关的脚本都将被启用，对目标主机进行探测。而一旦找到和登录授权有关的页面，我们就可以尝试使用类似于http-form-brute的脚本爆破出一些账户密码：

> 
`nmap -p-80 --script=http-form-brute --script-args=http-form-brute.path=/wp-login.php site.test.lan`


<img alt="" src="https://img-blog.csdnimg.cn/ed41677e89bb4e40ad408fb7e87dc8e4.jpg"/> 

从上图可以看到，网站site.test.lan的管理员密码为12345。

对于WordPress来说，Nmap已做的足够出色，它获取了大量和渗透有关的信息，而如果想对WordPress进行更深一步的漏洞探测，你也可以使用已集成在kali linux中的WPScan，这款软件有大量专门针对WordPress的PoC。

### SSH

此外，我们也可以对22端口（SSH服务）进行密码爆破，涉及脚本为ssh-brute

> 
`nmap -p22 --script ssh-brute site.test.lan`


 <img alt="" src="https://img-blog.csdnimg.cn/01d9ceb5e2fc4e588c687256e11e2c83.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_14,color_FFFFFF,t_70,g_se,x_16"/>

### FTP

而通常开放在21端口的FTP服务也往往是爆破对象，我们可以先使用脚本ftp-syst获取一些服务信息:

> 
`nmap -p21 --script ftp-syst site.test.lan`


 <img alt="" src="https://img-blog.csdnimg.cn/b38699babec84e6dbbe4319545947861.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_10,color_FFFFFF,t_70,g_se,x_16"/>

之后使暴力破解脚本得到FTP服务的用户密码:

> 
`nmap -p21 192.168.60.50 --script ftp-brute --script-args userdb=/root/user.txt,passdb=/root/pass.txt`


### MySQL

Nmap也可对MySQL服务（通常开放在端口3306上）进行扫描爆破，脚本mysql-info将探测出一些MySQ服务的详细信息(需要带上命令参数-sV -sC)：

> 
`nmap -p3306 -sV -sC site.test.lan`


你可以看到MySQL服务的协议版本号、流标识符、状态和密码salt等信息。更重要的是，你还可以列出有效的MySQL用户：

> 
`nmap -p3306 --script mysql-enum site.test.lan`


在得到有效用户名后，你就可以配合密码字典进行密码暴力破解。

希望这篇文章能对你有所帮助，感谢阅读

**[获取2021最新网络安全学习资源（学习视频、渗透工具、面试题、书籍等等）](https://docs.qq.com/doc/DRHFnVWJjTU50ZVhG)**

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
