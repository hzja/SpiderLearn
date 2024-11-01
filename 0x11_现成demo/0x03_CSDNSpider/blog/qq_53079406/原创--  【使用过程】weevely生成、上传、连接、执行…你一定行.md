# 原创
：  【使用过程】weevely生成、上传、连接、执行…你一定行

# 【使用过程】weevely生成、上传、连接、执行…你一定行

**目录**

[weevely前言：](#weevely%E5%89%8D%E8%A8%80%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[使用方法：](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[第一步：查看是否安装weevely，并查看版本信息](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%98%AF%E5%90%A6%E5%AE%89%E8%A3%85weevely%EF%BC%8C%E5%B9%B6%E6%9F%A5%E7%9C%8B%E7%89%88%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第二步：生成shell（php）文件](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90shell%EF%BC%88php%EF%BC%89%E6%96%87%E4%BB%B6)

[第二步：上传文件到目标服务器 ](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6%E5%88%B0%E7%9B%AE%E6%A0%87%E6%9C%8D%E5%8A%A1%E5%99%A8%C2%A0)

[第三步：在终端使用weevely，连接到shell（php文件）](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%9C%A8%E7%BB%88%E7%AB%AF%E4%BD%BF%E7%94%A8weevely%EF%BC%8C%E8%BF%9E%E6%8E%A5%E5%88%B0shell%EF%BC%88php%E6%96%87%E4%BB%B6%EF%BC%89)

[第四步：执行相关系统命令，获取相关信息](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%89%A7%E8%A1%8C%E7%9B%B8%E5%85%B3%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%EF%BC%8C%E8%8E%B7%E5%8F%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF)

[第五步：调用weevely模块](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%B0%83%E7%94%A8weevely%E6%A8%A1%E5%9D%97)

[小白初试使用方法：](#%E5%B0%8F%E7%99%BD%E5%88%9D%E8%AF%95%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[模块大全：](#%E6%A8%A1%E5%9D%97%E5%A4%A7%E5%85%A8%EF%BC%9A)

[推荐：](#%E6%8E%A8%E8%8D%90%EF%BC%9A)

---


 

## weevely前言：

> 
Webshell是经常被使用的攻击手法，一般会将asp或php后门文件与网站服务器WEB目录下正常的网页文件混在一起，然后就可以使用浏览器来访问asp或php后门，得到一个命令执行环境，以达到控制网站服务器的目的


## 简介：

> 
（在Linux中已经集成安装了）
weevely是一款使用python编写针对PHP的webshell工具，采用c/s模式构建，能模拟一个类似于telnet的连接shell。
使用的是比较主流的base64加密结合字符串变形技术，后门中所使用的函数均是常用的字符串处理函数，有很好的隐蔽性。
weevely具有生成shell文件、连接后台、资源搜索、信息探测、文件管理操作、错误配置审计、暴力破解、数据库操作、端口扫描等功能


## 使用方法：

### 第一步：查看是否安装weevely，并查看版本信息

> 
打开终端，输入weevely，检查是否安装了weevely，如果安装过，就能看见版本信息，并能看见基本的使用说明



### 第二步：生成shell（php）文件

> 
 weevely generate &lt;password&gt;  &lt;path&gt;/xx.php
我这里输入的是weevely generate 111 /root/1.php 
(这个path是已经存在的路径，而后面的文件是将要在这个目录下生成的shell文件)

 <img alt="" height="477" src="https://img-blog.csdnimg.cn/f6d70ee3773b4167968f2c40c55b10e9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_15,color_FFFFFF,t_70,g_se,x_16" width="645"/>


### 第二步：上传文件到目标服务器 

> 
我这里使用owaspbwa靶机来试


找到upload上传地方，然后上传生成的shell（php）文件


查看上传文件所在的地址（真实中，文件目录啥的都可以扫出来）



### 第三步：在终端使用weevely，连接到shell（php文件）

> 
weevely  &lt;url&gt;  &lt;password&gt;
我这里输入的是weevely http://192.168.190.130/dvwa/hackable/uploads/1.php 111
这里的URL指文件上传后的文件所在地址



### 第四步：执行相关系统命令，获取相关信息

> 
 第一次执行的提示Permission denied（权限不够）
然后下面就进入到上传到的那个文件夹里面了

 然后再加上ls
就成功了 



### 第五步：调用weevely模块

> 
执行更多的操作，输入help命令可以查看相关的命令


 随机试一个幸运儿



 

### 小白初试使用方法：

> 
不知道模块的命令的话，就可以把命令输入，然后查看给出的提示



### 模块大全：

> 
:backdoor_reversetcp          执行反向TCP shell
:backdoor_tcp                 在TCP端口产生一个壳
:file_cp                      复制单个文件
 :file_grep                    打印线与多个文件中的模式匹配
 :file_zip                     压缩或展开ZIP文件
 :file_bzip2                   压缩或展开Bzip2文件
:file_tar                     压缩或展开tar文件
 :file_gzip                    压缩或展开Gzip文件
:file_mount                   使用httpfs安装远程文件系统
 :file_cd                      更改当前工作目录
 :file_clearlog                从文件中删除字符串
 :file_read                    从远程文件系统中读取远程文件
:file_download                从远程文件系统下载文件
 :file_touch                   更改文件时间戳
 :file_ls                      列表目录内容
 :file_enum                    检查存在列表列表的存在和权限
:file_upload                  将文件上传到远程文件系统
 :file_find                    查找具有给定名称和属性的文件
 :file_check                   获取文件的属性和权限
 :file_edit                    在本地编辑器上编辑远程文件
 :file_webdownload             下载URL.
 :file_upload2web              将文件自动上传到Web文件夹并获得相应的URL
:file_rm                      删除远程文件
 :shell_php                    执行php命令
 :shell_sh                     执行shell命令
:shell_su                     执行su的命令
:sql_dump                     多DBMS MySqldump更换
:sql_console                  执行SQL查询或运行控制台
 :bruteforce_sql               BruteForce SQL数据库
:net_ifconfig                 获取网络接口地址
:net_mail                     发送邮件
 :net_curl                     执行类似卷曲的HTTP请求。
 :net_scan                     TCP端口扫描。
 :net_proxy                    运行本地代理以通过目标浏览HTTP / HTTPS浏览。
 :net_phpproxy                 在目标上安装PHP代理。
:system_info                  收集系统信息。
 :system_extensions            收集PHP和WebServer扩展列表。
 :system_procs                 列出运行进程。
:audit_phpconf               审核PHP配置。
 :audit_suidsgid               查找suid或sgid标志的文件。
 :audit_disablefunctionbypass  旁路禁用与mod_cgi和.htaccess的限制。
 :audit_filesystem             审核文件系统以获取弱权限。        
 :audit_etcpasswd              用不同的技术读取/ etc / passwd。


### 推荐：

[【XSS跨站合集】反射型、存储型、DOM类XSS原理+利用过程](https://blog.csdn.net/qq_53079406/article/details/123694180?spm=1001.2014.3001.5501)

[Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…](https://blog.csdn.net/qq_53079406/article/details/123590641?spm=1001.2014.3001.5501)

[【数据隐藏】一起入门隐写吧，宝？word、图像、移动设备、文件压缩数据隐藏](https://blog.csdn.net/qq_53079406/article/details/123537834?spm=1001.2014.3001.5501)
