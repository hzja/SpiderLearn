# 原创
：  VulnHub渗透测试实战靶场 - ZICO2: 1

# VulnHub渗透测试实战靶场 - ZICO2: 1

#### VulnHub渗透测试实战靶场 - ZICO2: 1

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/zico/zico2.ova)


## ZICO2: 1靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324?spm=1001.2014.3001.5501)



## 渗透测试

### 信息搜集

> 
先用arp-scan扫描一下网段内目标靶机的IP地址：`sudo arp-scan -l`


> 
再用Nmap扫描一下目标靶机的信息：`sudo nmap -sS -A 192.168.56.105`


> 
发现靶机开放了`22`、`80`和`111`端口，系统为Linux，22端口为`SSH`服务，80端口为`http`服务，Web容器为`Apache/2.2.22`


### 漏洞挖掘

> 
用dirb扫描一下80端口的web目录：`dirb http://192.168.56.105`


> 
发现敏感目录`dbadmin`，访问 `http://192.168.56.105/dbadmin/`，发现目录遍历，且同时存在 `test_db.php`文件，发现是类似于MySQL的phpmyadmin，靶机的这个是sqlite的网页版管理，尝试弱口令`admin`登录成功


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d1b40c40377d4800895ee3b89e33cdb9.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8485ab9495394eb8a1d2ee91c4cf0367.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
查看 phpLiteAdmin原有的数据库，发现里面存在两个账号，解hash得到


```
root 34kroot34
zico zico2215@

```

> 
测试网站时发现一个链接页面存在文件包含漏洞：`http://192.168.56.105/view.php?page=tools.html`


### getshell

> 
根据前面得到的phpliteadmin和文件包含漏洞，可以将两者结合起来进行getshell，向phpliteadmin插入新的数据，利用文件包含漏洞来包含执行插入的恶意代码


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b16ef1f9458c415788349eb139ed5993.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20e73f9a8fa94db2b656a609ae135953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
新建数据库，将表名写成一句话木马，测试成功触发恶意代码


> 
利用Kali自带的php反弹shell：`sudo cp /usr/share/webshells/php/php-reverse-shell.php ~/Desktop/`，修改一下Host和Port


> 
用蚁剑将其上传到`/var/tmp`文件夹下


> 
起一个监听，利用burpsuite发包包含反弹shell的文件，成功接收到反弹的shell


### 提权

> 
采用溢出提权，利用命令`uname -a`查看内核版本信息，发现系统为 `Ubuntu 12.04 (Linux 3.2.0-23-generic)`


> 
搜索到相关漏洞利用exp：[https://github.com/FireFart/dirtycow](https://github.com/FireFart/dirtycow)，将exp上传到`/var/tmp`目录下


> 
使用命令：`gcc -pthread dirty.c -o dirty -lcrypt`来编译exp，执行编译好的exp


> 
切换到`firefart`用户组，成功拿到root权限


#### 补充

> 
拿到root权限后发现`/home/zico`文件夹内有wordpress，可以尝试通过这条途径来提权（有的大师傅就是这样做的）

