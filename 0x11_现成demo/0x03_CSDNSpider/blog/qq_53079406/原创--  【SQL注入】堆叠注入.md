# 原创
：  【SQL注入】堆叠注入

# 【SQL注入】堆叠注入

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[优势](#%E4%BC%98%E5%8A%BF)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[防护：](#%E9%98%B2%E6%8A%A4%EF%BC%9A)

[二、分析堆叠注入](#%E4%BD%BF%E7%94%A8MySQL%E5%88%86%E6%9E%90%E5%A0%86%E5%8F%A0%E6%B3%A8%E5%85%A5%EF%BC%9A)

[使用MYSQL](#%E4%BD%BF%E7%94%A8MYSQL)

[第一步：使用堆叠查询构造多条语句](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E5%A0%86%E5%8F%A0%E6%9F%A5%E8%AF%A2%E6%9E%84%E9%80%A0%E5%A4%9A%E6%9D%A1%E8%AF%AD%E5%8F%A5)

[第二步：查看语句是否成功执行](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E8%AF%AD%E5%8F%A5%E6%98%AF%E5%90%A6%E6%88%90%E5%8A%9F%E6%89%A7%E8%A1%8C)

[第三步：删除test，再查询](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A0%E9%99%A4test%EF%BC%8C%E5%86%8D%E6%9F%A5%E8%AF%A2)

[ 第四步：执行其它查询语句](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%89%A7%E8%A1%8C%E5%85%B6%E5%AE%83%E6%9F%A5%E8%AF%A2%E8%AF%AD%E5%8F%A5)

---


## 一、简介

> 
<h3>概述：</h3>
顾名思义，就是多条语句堆叠在一起注入


> 
<h3>原理：</h3>
将多条语句堆叠在一起进行查询，且可以执行多条SQL语句
语句之间以分号(;)隔开，其注入攻击就是利用此特点，在第二条语句中构造payload


> 
<h3>优势</h3>
联合查询union也可拼接语句（有局限性）
但是堆叠注入能注入任意语句


> 
<h3>前提：</h3>
有注入点：即存在sql注入漏洞
未过滤：即未对";"号进行过滤
未禁用：即未禁止执行多条sql语句


> 
<h3>防护：</h3>
利用mysqli_multi_query()函数就支持多条sql语句同时执行
但实际情况中，PHP为了防止sql注入机制，往往使用调用数据库的函数是mysqli_ query()函数，其只能执行一条语句，分号后面的内容将不会被执行


---


---


## 二、分析堆叠注入

> 
<h3>使用MYSQL</h3>
<h4>第一步：使用堆叠查询构造多条语句</h4>
select * from users where id=1;create table test like users; 

<hr/>
<h4>第二步：查看语句是否成功执行</h4>
show tables;

<hr/>
<h4>第三步：删除test，再查询</h4>
select * from users where id=1;drop table test;
show tables;
(被成功执行了)

 <img alt="" height="270" src="https://img-blog.csdnimg.cn/63269b1a31e24328ac25dae66007576d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="769"/>
<hr/>
<h4> 第四步：执行其它查询语句</h4>
查数据库当前用户，版本
select * from user where id=1;select 1,user(),database();


加载文件
select * from user where id=1;select load_file('文件路径');
修改数据
select * from user where id=1;insert into user(username,password) values ('好好学习','123456');



#### 第一步：使用堆叠查询构造多条语句

---


#### 第三步：删除test，再查询
