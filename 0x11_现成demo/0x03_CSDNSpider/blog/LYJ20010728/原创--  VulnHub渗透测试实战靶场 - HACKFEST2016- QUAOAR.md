# 原创
：  VulnHub渗透测试实战靶场 - HACKFEST2016: QUAOAR

# VulnHub渗透测试实战靶场 - HACKFEST2016: QUAOAR

#### VulnHub渗透测试实战靶场 - HACKFEST2016: QUAOAR

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/zico/zico2.ova)


## HACKFEST2016: QUAOAR靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324?spm=1001.2014.3001.5501)



> 
目标靶机的IP地址为：`192.168.56.106`


> 
攻击机的IP地址为：`192.168.56.102`


## 渗透测试

### 信息搜集

> 
用Nmap扫描一下目标靶机的端口信息：`sudo nmap -sS -A 192.168.56.106`


> 
用dirb扫描一下80端口web目录：`dirb http://192.168.56.106`


### 漏洞挖掘

> 
访问一下`http://192.168.56.106/robots.txt`，提示查看`/wordpress/`


> 
直接查看`http://192.168.56.106/wordpress/wp-admin/`（做习惯了），尝试`admin:admin`，成功登录


> 
修改404.php页面内容，访问`http://192.168.56.106/wordpress/wp-content/themes/twentyfourteen/404.php`发现成功触发恶意代码


### getshell

> 
在404页面写入一句话木马，蚁剑连接在`/var/www`目录下上传反弹shell文件：


> 
起一个监听，然后访问`http://192.168.56.106/php-reverse-shell.php`，成功反弹shell，将shell变成交互式的shell：`python -c 'import pty;pty.spawn("/bin/bash")'`


### 提权

> 
执行命令`uname -a`查看内核版本信息，发现系统为`3.2.0-23-generic-pae`，可以采用溢出提权的方式来进行提权操作，利用脏牛漏洞来进行提权操作


> 
exp：[https://github.com/FireFart/dirtycow](https://github.com/FireFart/dirtycow)，将exp上传到`/var/tmp`目录下


> 
使用命令：`gcc -pthread dirty.c -o dirty -lcrypt`来编译exp，但却发现没有gcc


> 
搜索可以利用的文件，在 `/var/www/wordpress/wp-config.php`中发现root的密码


> 
切换到root用户组：`root:rootpassword!`，成功拿到root权限

