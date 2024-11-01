# 原创
：  web漏洞-渗透测试-加密解密注入-二次注入-DNSlog带外注入-中转注入-附SQLi-LABS靶场操作示例

# web漏洞-渗透测试-加密解密注入-二次注入-DNSlog带外注入-中转注入-附SQLi-LABS靶场操作示例

## 一、导图

## 二、加解密注入

### &lt;SQLi-LABS-Less21&gt;

Cookie注入+加解密注入

#### 1.靶场原码

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;

&lt;title&gt;Less-21 Cookie Injection- Error Based- complex - string&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;?php
//including the Mysql connect parameters.
    include("../sql-connections/sql-connect.php");
if(!isset($_COOKIE['uname']))
    {
    //including the Mysql connect parameters.
    include("../sql-connections/sql-connect.php");

    echo "&lt;div style=' margin-top:20px;color:#FFF; font-size:24px; text-align:center'&gt; Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color='#FF0000'&gt; Dhakkan &lt;/font&gt;&lt;br&gt;&lt;/div&gt;";
    echo "&lt;div  align='center' style='margin:20px 0px 0px 510px;border:20px; background-color:#0CF; text-align:center;width:400px; height:150px;'&gt;";
    echo "&lt;div style='padding-top:10px; font-size:15px;'&gt;";
 

    echo "&lt;!--Form to post the contents --&gt;";
    echo '&lt;form action=" " name="form1" method="post"&gt;';

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
    echo '&lt;img src="../images/Less-21.jpg" /&gt;';
    echo '&lt;/center&gt;';





    
function check_input($value)
    {
    if(!empty($value))
        {
        $value = substr($value,0,20); // truncation (see comments)
        }
        if (get_magic_quotes_gpc())  // Stripslashes if magic quotes enabled
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
            if($row1)
                {
                echo '&lt;font color= "#FFFF00" font size = 3 &gt;';
                setcookie('uname', base64_encode($row1['username']), time()+3600);    
                
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
                header ('Location: index.php');
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
            echo "&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;";
            echo '&lt;img src="../images/Less-21.jpg" /&gt;';
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
            
            $cookee = base64_decode($cookee);
            echo "&lt;br&gt;&lt;/font&gt;";
            $sql="SELECT * FROM users WHERE username=('$cookee') LIMIT 0,1";
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
            echo '&lt;form action="" method="post"&gt;';
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
                setcookie('uname', base64_encode($row1['username']), time()-3600);
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

#### 2.输入对应的账号和密码后点击登录

#### 3.使用BurpSuit抓包后可以看到Cookie值一栏uname后有下面结果

```
YWRtaW4%3D

其中“%3D”即为“=”

替换后为：YWRtaW4=

解密后可以得到：admin
```

#### 4.本题的注入点是Cookie注入，在注入时需要将注入内容写到Cookie后，同时要注意在写入注入内容时要先进行一次加密，再进行注入。

#### 5.分析原码

#### 6.先将要注入的内容进行加密

#### 7.加密后注入可以得到注入效果

#### 8.实例一

#### 9.实例二

#### 10.总结

加解密注入就是比常规注入多了一步，需要对网站加密方式进行还原，在注入过程中，所有的注入语句要按照网站的加密方式进行加密后再进行注入。

## 三、二次注入

### &lt;SQLi-LABS-Less24&gt;

#### 1.注入原理

二次注入是无法在黑盒测试（无源代码信息）中分析到的，需要在有一定代码的白盒的情况下才能分析到，用扫描工具也无法扫描到二次注入。

因此二次注入普遍产生在“代码审计”里，拿到代码后通过代码挖漏洞。

#### 2.靶场原码

```
密码修改部分的原码
&lt;html&gt;
&lt;head&gt;
&lt;/head&gt;
&lt;body bgcolor="#000000"&gt;
&lt;?PHP
session_start();
if (!isset($_COOKIE["Auth"]))
{
    if (!isset($_SESSION["username"])) 
    {
           header('Location: index.php');
    }
    header('Location: index.php');
}
?&gt;
&lt;div align="right"&gt;
&lt;a style="font-size:.8em;color:#FFFF00" href='index.php'&gt;&lt;img src="../images/Home.png" height='45'; width='45'&gt;&lt;/br&gt;HOME&lt;/a&gt;
&lt;/div&gt;
&lt;?php

//including the Mysql connect parameters.
include("../sql-connections/sql-connect.php");



if (isset($_POST['submit']))
{
    
    
    # Validating the user input........
    $username= $_SESSION["username"];
    $curr_pass= mysql_real_escape_string($_POST['current_password']);
    $pass= mysql_real_escape_string($_POST['password']);
    $re_pass= mysql_real_escape_string($_POST['re_password']);
    
    if($pass==$re_pass)
    {    
        $sql = "UPDATE users SET PASSWORD='$pass' where username='$username' and password='$curr_pass' ";
        $res = mysql_query($sql) or die('You tried to be smart, Try harder!!!! :( ');
        $row = mysql_affected_rows();
        echo '&lt;font size="3" color="#FFFF00"&gt;';
        echo '&lt;center&gt;';
        if($row==1)
        {
            echo "Password successfully updated";
    
        }
        else
        {
            header('Location: failed.php');
            //echo 'You tried to be smart, Try harder!!!! :( ';
        }
    }
    else
    {
        echo '&lt;font size="5" color="#FFFF00"&gt;&lt;center&gt;';
        echo "Make sure New Password and Retype Password fields have same value";
        header('refresh:2, url=index.php');
    }
}
?&gt;
&lt;?php
if(isset($_POST['submit1']))
{
    session_destroy();
    setcookie('Auth', 1 , time()-3600);
    header ('Location: index.php');
}
?&gt;
&lt;/center&gt;  
&lt;/body&gt;
&lt;/html&gt;
```

#### 3.首页

二次注入就容易出现在这种有数据互联的地方，即注册账号之后，可以登录这个注册的账号和密码，还可以修改注册的账号和密码，在这个过程中会有注册的信息被来回调用，

#### 4.首先注册一个账号和密码分别为“ceshi”、“ceshi1”的账号备用

```
mysql&gt; use security;
Database changed
mysql&gt; show tables;
+--------------------+
| Tables_in_security |
+--------------------+
| emails             |
| referers           |
| uagents            |
| users              |
+--------------------+
4 rows in set (0.00 sec)

mysql&gt; select * from users;    #注册“ceshi”账户前
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | Dumb     | Dumb       |
|  2 | Angelina | I-kill-you |
|  3 | Dummy    | p@ssword   |
|  4 | secure   | crappy     |
|  5 | stupid   | stupidity  |
|  6 | superman | genious    |
|  7 | batman   | mob!le     |
|  8 | admin    | admin      |
|  9 | admin1   | admin1     |
| 10 | admin2   | admin2     |
| 11 | admin3   | admin3     |
| 12 | dhakkan  | dumbo      |
| 14 | admin4   | admin4     |
+----+----------+------------+
13 rows in set (0.00 sec)

mysql&gt; select * from users;    #注册“ceshi”账户后
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | Dumb     | Dumb       |
|  2 | Angelina | I-kill-you |
|  3 | Dummy    | p@ssword   |
|  4 | secure   | crappy     |
|  5 | stupid   | stupidity  |
|  6 | superman | genious    |
|  7 | batman   | mob!le     |
|  8 | admin    | admin      |
|  9 | admin1   | admin1     |
| 10 | admin2   | admin2     |
| 11 | admin3   | admin3     |
| 12 | dhakkan  | dumbo      |
| 14 | admin4   | admin4     |
| 15 | ceshi    | ceshi1     |
+----+----------+------------+
14 rows in set (0.00 sec)
```

#### 5.再注册一个账号和密码分别为“ceshi'#”、“ceshi2”的账号

```
mysql&gt; select * from users;
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | Dumb     | Dumb       |
|  2 | Angelina | I-kill-you |
|  3 | Dummy    | p@ssword   |
|  4 | secure   | crappy     |
|  5 | stupid   | stupidity  |
|  6 | superman | genious    |
|  7 | batman   | mob!le     |
|  8 | admin    | admin      |
|  9 | admin1   | admin1     |
| 10 | admin2   | admin2     |
| 11 | admin3   | admin3     |
| 12 | dhakkan  | dumbo      |
| 14 | admin4   | admin4     |
| 15 | ceshi    | ceshi1     |
| 16 | ceshi'#  | ceshi2     |
+----+----------+------------+
15 rows in set (0.00 sec)
```

#### 6.登录账户“ceshi'#”后修改密码，将其密码修改为“ceshi3”

#### 7.在数据库命令行内进行查看

```
mysql&gt; select * from users;
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | Dumb     | Dumb       |
|  2 | Angelina | I-kill-you |
|  3 | Dummy    | p@ssword   |
|  4 | secure   | crappy     |
|  5 | stupid   | stupidity  |
|  6 | superman | genious    |
|  7 | batman   | mob!le     |
|  8 | admin    | admin      |
|  9 | admin1   | admin1     |
| 10 | admin2   | admin2     |
| 11 | admin3   | admin3     |
| 12 | dhakkan  | dumbo      |
| 14 | admin4   | admin4     |
| 15 | ceshi    | ceshi3     |
| 16 | ceshi'#  | ceshi2     |
+----+----------+------------+
15 rows in set (0.00 sec)
```

可以发现账户“ceshi'#”的密码并没有被修改掉，反而“ceshi”的密码被修改成了“ceshi3”。

#### 8.分析原码

修改密码部分的sql语句如下图所示。

当我们修改“ceshi'#”的密码时，将此用户名带入sql语句中可以看到sql语句如下图所示。

“#”将后面的sql语句给屏蔽掉了，前面的sql语句执行后，就将账用户“ceshi”的密码修改为了新设定的密码，而“ceshi'#”的密码不变。

#### 9.在数据库命令行内进行查看

```
mysql&gt; select * from users;
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | Dumb     | Dumb       |
|  2 | Angelina | I-kill-you |
|  3 | Dummy    | p@ssword   |
|  4 | secure   | crappy     |
|  5 | stupid   | stupidity  |
|  6 | superman | genious    |
|  7 | batman   | mob!le     |
|  8 | admin    | admin      |
|  9 | admin1   | admin1     |
| 10 | admin2   | admin2     |
| 11 | admin3   | admin3     |
| 12 | dhakkan  | dumbo      |
| 14 | admin4   | admin4     |
| 15 | ceshi    | ceshi3     |
| 16 | ceshi'#  | ceshi2     |
+----+----------+------------+
15 rows in set (0.00 sec)
```

#### 10.在此情况下，在用户名下输入对应的语句就可以实现sql注入

#### 11.这里就有一个问题了，许多网页都会对用户名的长度进行限制，那么该如何填写这么长的sql注入语句呢？

主要分为两种情况，一种是前端的长度限制，另一种是后端的长度限制。

如果是后端（php代码）的我们便无法突破了，前端（html代码）的我们可以突破。

只需要右键之后点击检查，之后将其长度限制修改大即可。

## 四、DNSlog带外注入

### &lt;SQLi-LABS-Less9&gt;

#### 1.简介

DNS(Domain Name System，域名系统)，因特网上作为域名和[IP地址](https://baike.so.com/doc/4252723-4455111.html)相互映射的一个[分布式数据库](https://baike.so.com/doc/6591740-6805519.html)，能够使用户更方便的访问[互联网](https://baike.so.com/doc/2011565-2128705.html)，而不用去记住能够被机器直接读取的IP数串。通过[主机](https://baike.so.com/doc/5331327-5566564.html)名，最终得到该主机名对应的IP地址的过程叫做域名解析(或主机名解析)。

Dnslog就是存储在DNS Server上的域名信息，它记录着用户对域名的访问信息。

#### 2.前提条件

需要注入的是一个高权限的注入点（如mysql的root权限），因为这里会涉及到文件读取，即dnslog带外注入需要有文件读取的操作权限才能进行。

那么就有一个问题了，都有文件读取操作的权限了，还需要其它注入干嘛呢？

是因为就算进行文件读写，后门也不一定可以成功写上去，因为在后面的渗透过程中可以发现，就算是你的后门写上去，也不一定可以连接上，可能会遇到各种各样的问题（如传上去的后门网站的脚本不解析），当然这种问题出现的机率不是很高，但是也可能会产生。

#### 3.优点

解决了盲注不能回显数据，效率低的问题。

#### 4.局限性

使用DnsLog盲注仅限于windos环境。

#### 5.参考链接

[https://www.cnblogs.com/xhds/p/12322839.html](https://www.cnblogs.com/xhds/p/12322839.html)

## 五、中转注入

#### 1.引入

因为在我们进行手工注入时，有些注入在注入的时候会出现一些很麻烦的问题。

以加解密为例，在进行加解密时，每次进行注入都需要将注入语句进行加密，对此有两种方案解决。

#### 2.方法

第一种是将其原有参数进行还原，在注入时通过工具加载加密插件，对注入语句进行加密，之后再进行注入。

但是这种办法需要注入工具有这种插件、脚本。

以sqlmap为例，sqlmap拥有很多功能强力的插件，插件的使用方法：-- tamper “插件名称”，在注入过程中可以采用下面的办法进行注入。

```
sqlmap -u http://xxxx.com/index.php?tel=LTEnIG9yICc4OCc9Jzg5 --tamper base64encode.py –dbs
```

第二种是当我们没有此插件还想使用工具注入时，就需要我们自己开发脚本。

在本地搭建一个网站，写一个脚本编码文件，就可以结合sqlmap工具进行注入测试了。

#### 3.原理

sqlmap注入本地搭建的服务器中转脚本内（不是直接向目标网站进行注入）。

中转脚本来接收sqlmap注入过来的payload，根据自己脚本内的配置将注入内容进行编码。

将编码后的payload与目标地址进行拼接后请求该URL。

#### 4.实例

注意：本实例仅供参考！！！

可以看到参数id后面的值为“MQ==”，即BASE64加密后的“1”。

假设我们的工具没有对应的插件、脚本，那么就需要我们自己来写一个脚本，这里以PHP的代码为例。

```
存放脚本的名称为test.php

&lt;?php

$url='http://job.gxu.edu.cn/job_bystjb/yjs_byszjs.asp?id=';
$payload=base64_encode($_GETI['x']);
echo $payload;
$urls=$url.$payload;
file_get_contents($urls);
echo $urls;

?&gt;
```

通过靶场靶场与刚刚写的脚本进行结合即可。
