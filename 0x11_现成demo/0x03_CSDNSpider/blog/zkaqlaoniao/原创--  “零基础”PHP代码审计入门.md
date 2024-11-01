# 原创
：  “零基础”PHP代码审计入门

# “零基础”PHP代码审计入门

**目录**

[一、代码审计目的](#%E4%B8%80%E3%80%81%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E7%9B%AE%E7%9A%84)

[二、代码审计基础](#%E4%BA%8C%E3%80%81%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E5%9F%BA%E7%A1%80)

[三、 代码审计思路](#%E4%B8%89%E3%80%81%20%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E6%80%9D%E8%B7%AF)

[四、PHP核心配置](#%E5%9B%9B%E3%80%81PHP%E6%A0%B8%E5%BF%83%E9%85%8D%E7%BD%AE)

[五、 代码审计环境](#%E4%BA%94%E3%80%81%20%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E7%8E%AF%E5%A2%83)

[六、手动调试代码](#%E5%85%AD%E3%80%81%E6%89%8B%E5%8A%A8%E8%B0%83%E8%AF%95%E4%BB%A3%E7%A0%81)

[七、PHP的弱类型](#%E4%B8%83%E3%80%81PHP%E7%9A%84%E5%BC%B1%E7%B1%BB%E5%9E%8B)

[八、学习漏洞函数](#%E5%85%AB%E3%80%81%E5%AD%A6%E4%B9%A0%E6%BC%8F%E6%B4%9E%E5%87%BD%E6%95%B0)

[九、审计入门总结](#%E4%B9%9D%E3%80%81%E5%AE%A1%E8%AE%A1%E5%85%A5%E9%97%A8%E6%80%BB%E7%BB%93)

[推荐一些demo：](#%E6%8E%A8%E8%8D%90%E4%B8%80%E4%BA%9Bdemo%EF%BC%9A)

---


### 一、代码审计目的

代码审计指的是对源代码进行检查，寻找代码中的bug以及安全缺陷(漏洞)。代码审计这是一个需要多方面技能的技术，也是需要一定的知识储备。我们需要掌握编程，安全工具的使用、漏洞原理、漏洞的修复方式、函数的缺陷等等，如果再高级一些，我们需要学习不同的设计模式，编程思想、MVC框架以及常见的框架。

那么对于小白应该是需要一个路线，一个流程。

先记住一句话"一切存在用户输入的地方都有可能存在漏洞"[戳一戳免费获取网络安全资料腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)

### 二、代码审计基础

代码审计入门基础：html/js基础语法、PHP基础语法 ，面向对象思想，PHP小项目开发(Blog、注册登录、表单、文件上传、留言板等)，Web漏洞挖掘及利用，Web安全工具基本使用(burpsuite、sqlmap等)，代码审计工具(seay审计系统、zend studio+xdebug等)

代码审计两种基本方式：

代码审计两种基本方法：

现cms可分大体两类：

### 三、 代码审计思路

从个人角度出发，如果环境允许的话，可以先选择做一个”程序员“再来做代码审计。

因为从开发者的位置去思考问题，可以快速定位问题。学习面向对象编程以及面向过程编程，编写一些项目提升对代码的理解能力，再是对各种漏洞可以独立挖掘利用并能理解漏洞的危害，这里我们主要针对PHP源码做审计

接下来我们从三个层次开始我们的源码审计思路
1. 确定要审计的源码是什么语言1. 确定该源码是单入口还是多入口1. 确定该语言的各种漏洞诞生的函数
### 四、PHP核心配置

一个漏洞在不同环境造成的结果也是不一样的。

由于关于php.ini配置的内容过于多，这里推荐浏览官方文档 [https://www.php.net/manual/zh/ini.php](https://link.zhihu.com/?target=https%3A//www.php.net/manual/zh/ini.php)，我们在这里主要列下php.ini 主要使用的安全配置。

> 
  用来限制文档的存取,限制环境变量的存取,控制外部程序的执行. 
 **PHP5.4.0移除。**


> 
  指定php程序可以改变的环境变量的前缀,当这个选项的值为空时,那么php可以改变任何环境变量,如果 如:safe_mode_allowed_env_vars = PHP_,当这个选项的值为空时,那么php可以改变任何环境变量。 


> 
  当安全模式被激活，safe_mode_exec_dir参数限制通过exec()函数执行的可执行文件到指定的目录。举例来说，如果你想限制在/usr/local/bin目录执行功能，你可以使用这个指令： 
 <br/> safe_mode_exec_dir = "/usr/local/bin" 


> 
  为了更安全的运行PHP,可以用此指令来禁止一些敏感函数的使用,当你想用本指令禁止一些危险函数时,切记把dl()函数也加到禁止列表,攻击者可以利用dl()函数加载自定义的php扩展突破disable_functions.配置禁止函数时可以使用逗号分隔函数名。 


> 
  PHP设置在安全模式下(safe_mode),仍允许攻击者使用COM()函数来创建系统组件来还行任意命令,推荐关闭这个函数。 使用COM()函数需要在PHP.ini中配置 
 `extension=php_com_dotnet.dll`,如果PHPversion&lt;5.4.5则不需要。 


> 
  php.ini的register_globals选项的默认值为OFF,在4.2版本之前是默认开启的,当设定为On时,程序可以接收来自服务器的各种环境变量,包括表单提交的变量,这是对服务器分厂不安全的, register_globals = off时,服务器端获取数据的时候用$_GET['name']来获取数据。 register_globals = on时,服务端使用POST或GET提交的变量,豆浆自动使用全局变量的值来接受。 


> 
  PHP5.4.0被移除 magic_quotes_gpc = off 在php.ini中默认是关闭的,如果打开它,将自动把用户提交对sql的查询的语句进行转换,如果设置成ON,php会把所有的单引号,双引号,和反斜杠和空字符(NULL)加上反斜杠()进行转义 它会影响HTTP请求的数据(GET,POST.COOKIE),开启它会提高网站的安全性。 


> 
  该配置为ON的情况下,可以直接包含远程文件,若包含的变量为可控的情况下,可以直接控制变量来执行PHP代码。 


> 
  允许本地PHP文件通过调用url重写来打开或者关闭写权限,默认的封装协议提供的ftp和http协议来访问文件。 


> 
  防止通过http头泄漏php版本信息。 


> 
  上传文件临时保存的目录,如果不设置的话,则采用系统的临时目录。 


> 
  能够控制PHP脚本只能访问指定的目录,这样能够避免PHP脚本访问不应该访问的文件,一定程度上限制了。webshell的危害 


> 
  表明实现PHP脚本的内部错误,网站发布后建议关不PHP的错误回显。 


> 
  具体列表推荐： 
 [https://www.runoob.com/php/func-error-reporting.html](https://link.zhihu.com/?target=https%3A//www.runoob.com/php/func-error-reporting.html)
<br/> 这里设置的作用是将错误级别调到最高,显示所有问题,方便环境部署时候排错 


### 五、 代码审计环境

PHP源码部署环境：Phpstudy 2018

集成开发环境：Zend Studio/Phpstorm

数据库管理工具：Navicat for MySQL 12

MySQL实时监控工具：MySQLMonitor

文本编辑工具：Sublime_Text3

代码审计辅助工具：Seay源代码审计系统、Search and Replace、Rips 0.55

代码审计辅助安全工具：渗透版火狐、BurpSuite、Sqlmap

### 六、手动调试代码

```
echo
exit();
print_r
var_dump();
debug_zval_dump();
debug_print_backtrace();
echo "&lt;script&gt;alert($estr);&lt;/script&gt;"";
die("&lt;script&gt;alert($estr);&lt;/script&gt;");

```

### 七、PHP的弱类型

1.比较符号 == 与 ===

```
//字符串和数字比较
var_dump(0=="admin");   //true
echo '&lt;br&gt;';
var_dump(1=="1admin");  //true
echo '&lt;br&gt;';
var_dump(1=="admin1");  //false
echo '&lt;br&gt;';
var_dump(0=="admin1");  //true
echo '&lt;br&gt;';
//数字和数组
$arr = array();
var_dump(0==$arr);  //false
echo '&lt;br&gt;';
//字符串和数组
$arr = array();
var_dump("0"==$arr);    //false
echo '&lt;br&gt;';
//"合法数字+e+合法数字"类型的字符串
var_dump("0e123456"=="0e4456789");  //true
echo '&lt;br&gt;';
var_dump("1e1"=="10");  //true

```

2.array_search 与 is_array

```
if(!is_array($_GET['test'])){
exit();
}
​
$test = $_GET['test'];
​
for($i = 0;$i&lt;count($test) ;$i++ ){
if($test[$i] === "admin"){
echo "error";
exit();
}
$test[$i] = intval($test[$i]);
}
​
if(array_search("admin",$test) === 0){
echo "flag";
}else{
echo "false";
}

```

我们可以传入test[]=0来进行绕过，首先test是一个数组，符合is_array的判断，然后test=0；在array_search中0==admin为true，绕过了array_search

3.in_array()函数

```
$array=[0,1,2,'3'];
var_dump(in_array('abc', $array)); //true
var_dump(in_array('1bc', $array)); //true

```

4.is_number()函数

```
$temp = $_GET['password'];
is_numeric($temp) ? die("no numeric") : NULL;
if($temp&gt;9999){
echo '我giao';
}

```

在这里我们的payload需要的是一个大于9999的数字后面加上字符就可以了 这里构造的是10000+ 。

5.strcmp()函数

```
$pd = "6666";
if(strcmp($_GET['pwd'],$pd) == 0){
echo "giao";
}else{
echo "?";
}

```

函数接受到了不符合的类型，发生了错误，但是还是判断其相等。

6.switch()语句

```
$pwd = "1ad";
switch($pwd){
case 1:
echo "giao";
break;
case 2:
echo "?";
break;
}

```

7.md5()函数

```
var_dump(md5('240610708') == md5('QNKCDZO'));//true
​
$array1=[1,2,3];
$array2=[4,5,6];
var_dump(md5($array1)===md5($array2)) //true

```

8.sha1()函数

```
$array1=[1,2,3];
$array2=[4,5,6];
​
var_dump(sha1($array1)===sha1($array2)); //true

```

9.empty与isset

```
$a = null;
$b = 0;
$c = "";
var_dump(empty($a));
var_dump(empty($b));
var_dump(empty($c));
var_dump(isset($a));
var_dump(isset($b));
var_dump(isset($c));
```

10.类型比较问题以及类型转换问题

此处推荐文章：[https://www.jb51.net/article/93447.htm](https://link.zhihu.com/?target=https%3A//www.jb51.net/article/93447.htm)

### 八、学习漏洞函数

1.全局变量/超全局变量

全局变量：

超全局变量：

**常用的超全局变量有9个：**

此处推荐文章：[https://blog.csdn.net/zhichaosong/article/details/80507516](https://link.zhihu.com/?target=https%3A//blog.csdn.net/zhichaosong/article/details/80507516)

2.SQL注入

```
select
update
insert into
delete
```

注：此处非函数，主要找常用的SQL语句

3.代码执行

```
eval()
usort()
uasort()
assert()
array_map()
preg_replace()
array_filter()
call_user_func()
create_function()
call_user_func_array()
文件操作函数：
fputs(fopen('shell.php','w'),'&lt;?php eval($_POST[cmd])?&gt;'); 
动态函数：$_GET['a']($_GET['b'])
```

4. 命令执行

```
system()
exec()
passthru()
shell_exec()
```

5. XSS跨站脚本攻击

```
print
print_r
echo
printf
die
var_dump
var_export
```

6.文件上传漏洞

```
move_uploaded_file()
```

7.文件包含漏洞

```
include()
include_once()
require()
require_once()
```

伪协议

```
file:// — 访问本地文件系统
http:// — 访问 HTTP(s) 网址
ftp:// — 访问 FTP(s) URLs
php:// — 访问各个输入/输出流（I/O streams）
zlib:// — 压缩流
data:// — 数据（RFC 2397）
glob:// — 查找匹配的文件路径模式
phar:// — PHP 归档
ssh2:// — Secure Shell 2
rar:// — RAR
ogg:// — 音频流
expect:// — 处理交互式的流
```

此处推荐文章：[https://segmentfault.com/a/1190000018991087](https://link.zhihu.com/?target=https%3A//segmentfault.com/a/1190000018991087)

8.任意文件下载

```
fopen()
readfile()
file_get_contents()
```

9.任意文件删除

```
unlink()
```

10.任意文件读取

```
file()
fgets()
fgetss()
fopen()
readfile()
fpassthru()
parse_ini_file()
file_get_contents()
```

11.变量覆盖

```
$$
extract()
parse_str()
import_request_variables()//此函数只能用于PHP4.1 ~ PHP5.4
```

12.反序列化漏洞

```
unserialize()
```

魔术方法

### 九、审计入门总结

先从Web漏洞原理开始理解再到漏洞的挖掘以及利用，我们就来到了PHP代码审计这个方向进行进修。这里我们开始学习PHP开发，以及熟悉下开发者的开发思想，站在开发者角度去思索代码。再是掌握漏洞对应发生函数使用，再是学习正则表达式。

审计路线：Demo-&gt;综合漏洞靶场-&gt;网上审计过的CMS-&gt;多入口CMS-&gt;单入口CMS-&gt;框架-&gt;函数缺陷

### 推荐一些demo：

文章转载自：**Saint Michael**
