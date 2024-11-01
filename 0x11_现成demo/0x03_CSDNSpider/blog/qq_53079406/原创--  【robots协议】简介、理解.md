# 原创
：  【robots协议】简介、理解

# 【robots协议】简介、理解

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、robots文件](#%E4%BA%8C%E3%80%81robots%E6%96%87%E4%BB%B6)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[格式：](#%E6%A0%BC%E5%BC%8F%EF%BC%9A)

[ 常见Robots：](#%C2%A0%E5%B8%B8%E8%A7%81Robots%EF%BC%9A)

---


## 一、简介

> 
<h3>概述：</h3>
robots是网站跟爬虫间的协议，用简单直接的txt格式文本方式告诉对应的爬虫被允许的权限，也就是说robots.txt是搜索引擎中访问网站的时候要查看的第一个文件。
<hr/>
搜索引擎通过一种程序robot（又称spider），自动访问互联网上的网页并获取网页信息。Robots.txt协议并不是一个规范，而只是约定俗成的，所以并不能保证网站的隐私。
<hr/>
当一个搜索蜘蛛访问一个站点时：
首先检查该站点根目录下是否存在robots.txt
如果存在，搜索机器人就会按照该文件中的内容来确定访问的范围；
如果该文件不存在，所有的搜索蜘蛛将能够访问网站上所有没有被口令保护的页面
<hr/>
可以在自己的网站中创建一个纯文本文件robots.txt
在这个文件中声明该网站中不想被robot访问的部分，该网站的部分或全部内容就可以不被搜索引擎收录了，或者指定搜索引擎只收录指定的内容。
<hr/>
robots.txt（统一小写）是一种存放于网站根目录下的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称网络蜘蛛），此网站中的哪些内容是不能被搜索引擎的漫游器获取的，哪些是可以被（漫游器）获取的。 因为一些系统中的URL是大小写敏感的，所以robots.txt的文件名应统一为小写。robots.txt应放置于网站的根目录下。如果想单独定义搜索引擎的漫游器访问子目录时的行为，那么可以将自定的设置合并到根目录下的robots.txt，或者使用robots元数据。


---


---


---


---


## 二、robots文件

> 
<h3>示例：</h3>
User-agent: *
Disallow: /admin/ 后台管理文件
Disallow: /require/ 程序文件
Disallow: /attachment/ 附件
Disallow: /images/ 图片
Disallow: /data/ 数据库文件
Disallow: /template/ 模板文件
Disallow: /css/ 样式表文件
Disallow: /lang/ 编码文件
Disallow: /script/ 脚本文件


> 
<h3>格式：</h3>
"robots.txt"文件包含一条或更多的记录，这些记录通过空行分开（以CR,CR/NL, or NL作为结束符），每一条记录的格式如下所示：
"&lt;field&gt;:&lt;optionalspace&gt;&lt;value&gt;&lt;optionalspace&gt;"。
<hr/>
在该文件中可以使用#进行注解，具体使用方法和UNIX中的惯例一样。该文件中的记录通常以一行或多行User-agent开始，后面加上若干Disallow行,详细情况如下：
<hr/>
**1、User-agent:**
该项的值用于描述搜索引擎robot的名字，在"robots.txt"文件中，如果有多条User-agent记录说明有多个robot会受到该协议的限制，对该文件来说，至少要有一条User-agent记录。如果该项的值设为*，则该协议对任何机器人均有效，在"robots.txt"文件中，"User-agent:*"这样的记录只能有一条。
<hr/>
**2、Disallow:**
该项的值用于描述不希望被访问到的一个URL，这个URL可以是一条完整的路径，也可以是部分的，任何以Disallow开头的URL均不会被robot访问到。
eg：
"Disallow:/help"对/help.html 和/help/index.html都不允许搜索引擎访问，而"Disallow:/help/"则允许robot访问/help.html，而不能访问/help/index.html。任何一条Disallow记录为空，说明该网站的所有部分都允许被访问，在"/robots.txt"文件中，至少要有一条Disallow记录。如果"/robots.txt"是一个空文件，则对于所有的搜索引擎robot，该网站都是开放的。
<hr/>
**3、Allow:**
该项的值用于描述希望被访问的一组URL，与Disallow项相似，这个值可以是一条完整的路径，也可以是路径的前缀，以Allow项的值开头的URL是允许robot访问的。
eg：
"Allow:/hibaidu"允许robot访问/hibaidu.htm、/hibaiducom.html、/hibaidu/com.html。一个网站的所有URL默认是Allow的，所以Allow通常与Disallow搭配使用，实现允许访问一部分网页同时禁止访问其它所有URL的功能。
需要特别注意的是Disallow与Allow行的顺序是有意义的，robot会根据第一个匹配成功的Allow或Disallow行确定是否访问某个URL。
<hr/>
**4、使用"*"和"$"：**
robots支持使用通配符"*"和"$"来模糊匹配url：
"$" 匹配行结束符。
"*" 匹配0或多个任意字符。


---


---


> 
<h3> 常见Robots：</h3>
google蜘蛛： googlebot
百度蜘蛛：baiduspider
yahoo蜘蛛：slurp
alexa蜘蛛：ia_archiver
msn蜘蛛：msnbot
altavista蜘蛛：scooter
lycos蜘蛛： lycos_spider_(t-rex)
alltheweb蜘蛛： fast-webcrawler/
inktomi蜘蛛： slurp

