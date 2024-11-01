# 原创
：  （手工）【sqli-labs24】二次注入：原理、利用过程

# （手工）【sqli-labs24】二次注入：原理、利用过程

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less24（POST-Second Order injections *Real treat* - Stored injections）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[简介：（GET注入-二次注入）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[第一步：获知目标账号并注册](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%8E%B7%E7%9F%A5%E7%9B%AE%E6%A0%87%E8%B4%A6%E5%8F%B7%E5%B9%B6%E6%B3%A8%E5%86%8C)

[第二步：登录修改密码](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%99%BB%E5%BD%95%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81)

[第三步：登录目标账号](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%99%BB%E5%BD%95%E7%9B%AE%E6%A0%87%E8%B4%A6%E5%8F%B7)

---


> 
<h2>推荐：</h2>
[【SQL注入】二次注入：原理、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125284454?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165753485116782246435196%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165753485116782246435196&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125284454-null-null.185^v2^control&amp;utm_term=%E4%BA%8C%E6%AC%A1%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125284454?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165753485116782246435196%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165753485116782246435196&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125284454-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E4%BA%8C%E6%AC%A1%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450)


---


---


## 一、（手工）SQL注入基本步骤：

> 
第一步：获知目标账号并注册
第二步：登录修改密码
第三步：登录目标账号



---


---


## 二、Less24（POST-Second Order injections *Real treat* - Stored injections）

> 
<h3>简介：（GET注入-二次注入）</h3>
请求方法：GET
方法：二次注入（存储注入）


> 
<h3>第一步：获知目标账号并注册</h3>
假设我们知道账号名为admin
点击注册新用户


注册的账号名为admin'#或者admin' or 1=1#或者admin' -- -
密码随便写一个
如果注册成功，则说明单引号和注释符都没有带入数据库中
-----&gt;即后端（PHP）代码对语句进行了转义

第一次注入转义，看能不能第二次调用，如果未被过滤，从而实现了二次注入


 

 

（我无法注册任何账号，下面2步只能整理思路了）

> 
<h3>第二步：登录修改密码</h3>
登录账号admin’#
并进行修改密码



> 
<h3>第三步：登录目标账号</h3>
如果登录成功
说明修改admin’#的密码时
其实此时admin’#的密码并没有修改
但是admin的密码被修改了
----&gt;说明，在数据库（mysql）没有转义，实现了二次注入

