# 原创
：  【web-代码审计】(14.5)PHP

# 【web-代码审计】(14.5)PHP

**目录**

[PHP](#PHP)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、确定用户提交的数据](#1.2%E3%80%81%E7%A1%AE%E5%AE%9A%E7%94%A8%E6%88%B7%E6%8F%90%E4%BA%A4%E7%9A%84%E6%95%B0%E6%8D%AE)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.3、会话交互](#1.3%E3%80%81%E4%BC%9A%E8%AF%9D%E4%BA%A4%E4%BA%92)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.4、潜在危险的APl](#1.4%E3%80%81%E6%BD%9C%E5%9C%A8%E5%8D%B1%E9%99%A9%E7%9A%84APl)

[文件访问](#%E6%96%87%E4%BB%B6%E8%AE%BF%E9%97%AE)

[数据库访问](#%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BF%E9%97%AE)

[动态代码执行](#%E5%8A%A8%E6%80%81%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

[OS命令执行](#OS%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)

[URL重定向](#URL%E9%87%8D%E5%AE%9A%E5%90%91)

[套接字](#%E5%A5%97%E6%8E%A5%E5%AD%97)

[1.5、配置PHP环境](#1.5%E3%80%81%E9%85%8D%E7%BD%AEPHP%E7%8E%AF%E5%A2%83)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[使用全局变量注册](#%E4%BD%BF%E7%94%A8%E5%85%A8%E5%B1%80%E5%8F%98%E9%87%8F%E6%B3%A8%E5%86%8C)

[安全模式](#%E5%AE%89%E5%85%A8%E6%A8%A1%E5%BC%8F)

[magic quotes](#magic%20quotes)

[其他](#%E5%85%B6%E4%BB%96)

---


## PHP

> 
<h3>1.1、简介：</h3>
在PHP平台上获取用户提交的输入的方法，与用户会话交互的方式、其中存在潜在危险的API以及与平台安全相关的配置选项


> 
<h3>1.2、确定用户提交的数据</h3>
<h4>简述：</h4>
1、PHP使用一系列数组变量保存用户提交的数据
$_GET       
$HTTP_GET_VARS
//这个数组包含在查询字符串中提交的参数。这些参数根据其名称访问($＿GET['x'])
$_POST
$HTTP_POST_VARS
//这个数组包含在请求主体中提交的参数


<hr/>
2、当尝试确定PHP应用程序如何访问用户提交的输入时，应该记住以下反常情况
A、$GLOBALS是一个包含在脚本全局范围内定义的所有变量的引用的数组，使用它可以根据名称访问其他变量
B、如果配置指令register_globals被激活，PHP会为所有请求参数（即$_REQUEST数组中的全部数据）建立全局变量，这表示应用程序可通过与相关参数相同的名称引用一个变量，从而访问用户输入，如果应用程序使用这种方法访问用户提交的数据，那么只有仔细地逐行审查代码，才能确定以这种方式使用的变量
C、除前面提到的标准HTTP消息头外，PHP还在$_SERVER数组中增加了一个数据，用于处理在请求中收到的任何定制HTTP消息头
D、名称包含下标（方括号内）的输入参数被自动转换为数组


> 
<h3>1.3、会话交互</h3>
<h4>简述：</h4>
1、PHP使用$_SESSION数组保存和检索用户会话中的信息
$＿SESSION['MyName'] = $_GET['username'];
echo "welcome" = $＿SESSION['MyName'];
$HTTP_SESSION_VARS数组的用法也相同

2、如果register_globals被激活，那么全局变员将通过以下方式保存在当前会话中
$MyName = $_GET['username'];
session_register("MyName");


> 
<h3>1.4、潜在危险的APl</h3>
<h4>文件访问</h4>
1、PHP中包含大量用于访问文件的函数，其中许多接受可用于访问远程文件的URL和其他结构。
2、下面的函数用于读取或写入一个指定文件的内容，如果向这些API提交用户可控制的数据，攻击者就可以利用这些API访问服务器文件系统上的任意文件
fopen、readfile、file、fpassthru、gzopen、gzfile、gzpassthru、readgzfile、copy、rename、rmdir、mkdir、unlink、file_get_contents、file_put_contents、parse_ini_file

3、下面的函数用于包含并执行一个指定的PHP脚本，如果攻击者能够使应用程序执行受控的文件，就可以在服务器上执行任意命令
include、include_once、require、require_once、virtual
4、即使无法包含远程文件，但如果攻击者可向服务器上传任意文件，仍然能够执行任意命令
5、PHP配置选项allow_url_fopen可用于防止一些文件函数访问远程文件。但在默认情况下设为1（表示允许远程文件），可用于检索远程文件的网络协议：HTTP、HTTPS、FTP、SSH
即使allow_url_fopen设为0，攻击者仍然可以访问远程文件（取决于所安装的扩展），此时远程访问方法有：SMB、PHP输入/输出流、压缩流、音频流

6、PHP5.2以后的版本引入了一个新的选项allow_url_include ，默认情况下，该选项被禁用。这个默认的配置防止前面提到的方法在调用文件包含函数时用于指定一个远程文件
<hr/>
<h4>数据库访问</h4>
1、下面的函数用于向数据库发送一个查询并检查查询结果：
mysql_query、mssql_query、pg_query
SQL语句以一个简单的字符串提交，如果用户可控制的数据属于字符串参数的一部分，那么应用程序就可能容易受到SQL注入攻击


2、下面的函数可用于创建预处理语句，允许应用程序建立一个包含参数占位符的SQL查询，并以可靠而且类型安全的方式设定这些占位符的值
mysql-&gt;prepare、stmt-&gt;prepare、stmt-&gt;bind_param、stmt-&gt;execute、odbc-&gt;Prepare
<hr/>
<h4>动态代码执行</h4>
1、下面的函数可用于动态执行PHP代码：
eval、call_user_func、call_user_func_array、call_user_method、call_user_method_array、create_function
2、分号分隔符用于将几个语句连接在一起，如果向这些函数提交用户可控制的数据，那么应用程序可能易于受到脚本注入攻击
3、搜索与替代正则表达式的preg_replace函数，如果以/e选项调用，可用于运行一段特殊的PHP代码，如果用户可控制的数据出现在动态执行的PHP代码中，应用程序可能易于受到攻击。
4、PHP也可以通过一个包含函数名称的变量动态调用该函数，使应用程序调用任意一个函数
<hr/>
<h4>OS命令执行</h4>
下面这些函数可用于执行操作系统命令：
exec、passthru、popen、proc_open、shell_exec、system、反单引号(`)
所有这些命令都可以使用I字符连接在一起，如果未经过滤就向这些函数提交用户可控制的数据，那么攻击者就可以在应用程序中执行任意命令
<hr/>
<h4>URL重定向</h4>
1、下面的API用于在PHP中发布一个HTTP重定向：
http_redirect、header、HttpMessage::setResponseCode、HttpMessage::setHeaders
2、通常使用http_redirect函数可以实现一个重定向，该函数接受一个包含相对或绝对URL的字符串，如果这个字符串的值由用户控制，那么应用程序可能易于受到钓鱼攻击。
3、通过调用包含适当Location消息头的header函数也可以实现重定向，它让PHP得出结论，认为需要一个HTTP重定向
4、还应仔细审查setResponseCode与setHeaders API的用法。如果某个项定向包含一个含有HTTP Location消息头的3xx响应，应用程序就可能使用这些API执行重定向
<hr/>
<h4>套接字</h4>
1、下面的API用于在PHP中建立和使用网络套接字：
socket_create、socket_connect、socket_write、socket_send、socket_recv、fsockopen、pfsockopen
2、使用socket_create创建一个套接字后，再通过调用socket_connect与远程主机建立连接，这个API接受目标主机的IP与端口信息为参数，如果用户能够以某种方式控制这些主机信息攻击者就可以利用应用程序与任意主机建立网络连接，无论这些主机位于公共因特网上、私有DMZ中还是应用程序运行的内部网络
3、fsockopen与pfsockopen函数可用于打开连接指定主机与端口的套接字，并返回一个可用在fwrite和fgets等标准文件函数中的文件指针，如果向这些函数提交用户数据，应用程序就可能易于受到攻击


#### 数据库访问

---


#### OS命令执行

---


#### 套接字

> 
<h3>1.5、配置PHP环境</h3>
<h4>简述：</h4>
PHP配置选项在php.ini文件中指定，该文件使用与Windows INI文件相同的结构，有各种选项都会影响一个应用程序的安全，最新版的PHP删除了许多以前引起问题的选项
<hr/>
<h4>使用全局变量注册</h4>
1、如果register_globals指令被激活，PHP会为所有请求参数建立全局变量，如果PHP不要求变量在使用前被初始化，这个选项就会导致安全漏洞，使攻击者能够将一个变量初始化为任意一个值

2、从PHP4.2.0开始，regiscer_globals指令默认被禁用。然而由于许多老式应用权序依赖于register_globals执行的正常操作， 因此通常php.ini会明确激活该指今。PHP6完全删除了register_globals指令
<hr/>
<h4>安全模式</h4>
1、如果safe_mode指令被激活，那么PHP会对使用某些危险的函数施加限制,一些函数被完全禁用，其他一些函数的使用也受到限制
A、shell_exec函数被禁用，因为这个函数可用于执行操作系统命令
B、mail函数的additional_parameters参数被禁用， 因此如果以不安全的方式使用这个参数可能导致SMTP注入漏洞
C、exec函数仅能够执行safe_mode_exec _dir指定目标下的可执行程序，命令字符串中的元字符被自动转义

2、并非所有危险函数都受到安全模式的眼制，一些限制受到其他配置选项的影响。且有各种方法可以避开一些安全模式限制。安全模式并不能完全解决PHP应用程序中的安全问题，PHP6已删除安全模式
<hr/>
<h4>magic quotes</h4>
1、如果激活magic_quotes_gpc指令，那么请求参数中包含的任何单引号、双引号、反斜线和空字符都会用一个反斜线自动转义，如果magic_quotes_sybase指令被禁用，那么PHP就会用一个单引号转义所有单引号，这个选项旨在保护包含不安全的数据库调用的危险代码，以防它被恶意的用户输入利用，在应用程序的代码中在找SQL注入漏洞时，应该检查magic quotes是否被激活，因为它会影响应用程序处理输入的方式

2、使用magic quotes并不能防止所有SQL注入攻击。如注入一个数字字段的攻击并不需要使用单引号。且如果其中包含的引号没有被转义的数据随后又从数据库中读回，那么仍可以利用这些数据实施二阶攻击

3、在不需要任何转义的情况下处理数据时，激活magic quotes选项可能会使PHP对用户输入进行不必要的修改，导致代码中多出斜线，还要使用stripslashes函数删除

4、在必要时，一些应用程序通过addslashes函数提交参数，自行对相关输入进行转义，如果PHP配置激活了magic quotes，那么这种方法就会导致双重转义字符，这时就会将配对的斜线解释为字面量反斜线，潜在恶意字符不会转义

5、由于magic quotes选项的局限性与不规则性，建议禁用该选项，使用预处理语句安全访问数据库
<hr/>
<h4>其他</h4>
其他一些可能影响PHP应用程序安全的配置选项




#### 使用全局变量注册

---


#### magic quotes

---

