# 原创
：  【数据库连接问题】【靶场访问错误】Table ‘xxx‘ doesn‘t exist，文件‘Not Find‘ 可能是管理软件与终端本身的一个连接问题

# 【数据库连接问题】【靶场访问错误】Table ‘xxx‘ doesn‘t exist，文件‘Not Find‘ 可能是管理软件与终端本身的一个连接问题

**目录**

[问题一：Table ‘xxx‘ doesn‘t exist](#%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9ATable%20%E2%80%98xxx%E2%80%98%20doesn%E2%80%98t%20exist)

[前言：](#%E5%89%8D%E8%A8%80%EF%BC%9A)

[问题重现：](#%E9%97%AE%E9%A2%98%E9%87%8D%E7%8E%B0%EF%BC%9A)

[问题分析：](#%E9%97%AE%E9%A2%98%E5%88%86%E6%9E%90%EF%BC%9A)

[问题解决：](#%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[ ​](#%C2%A0%E2%80%8B)

[问题二：文件Not Find问题](#%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9A%E6%96%87%E4%BB%B6Not%20Find%E9%97%AE%E9%A2%98)

[问题重现：](#%E9%97%AE%E9%A2%98%E9%87%8D%E7%8E%B0%EF%BC%9A)

[原因分析：](#%E5%8E%9F%E5%9B%A0%E5%88%86%E6%9E%90%EF%BC%9A)

[问题解决：](#%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

---


## 问题一：Table ‘xxx‘ doesn‘t exist

## 前言：

> 
我使用的phpstudy的MySQL因为3306端口被占用
我就将MySQL端口设置为3307
然后每次在phpstudy中新建数据库啥的时候，在数据库终端都看不见
在PHPmyadmin中可以看见phpstudy中的，但是在数据库终端却没有

简而言之，我们数据好像留在了phpstudy上面一样，并保存调用，并且好像不在我电脑上一样，在电脑里都搜不到，而MySQL终端找不到


## 问题重现：

> 
Table 'pikachu.member' doesn't exist
就是数据库没有这个表


而且涉及到数据库的表都是空的



## 问题分析：

> 
在pikachu文件夹里搜也找不到这个文件



手动启动MySQL终端
启动方法：[手动打开数据库终端](https://blog.csdn.net/qq_53079406/article/details/123047469?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164922262016782089311052%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164922262016782089311052&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123047469.nonecase&amp;utm_term=%E6%89%8B%E5%8A%A8%E6%89%93%E5%BC%80%E6%95%B0%E6%8D%AE%E5%BA%93&amp;spm=1018.2226.3001.4450)
直接进入MySQL下bin里面，按住shift右键空白处open inwindows Terminal
输入.\mysql.exe -u root -p
输入密码



在终端查看是否存在该表
show databases;
use pikachu;
show tables;
pikachu中没有任何表
 <img alt="" height="642" src="https://img-blog.csdnimg.cn/f3d3ffe21a6544c7a0e8b390cc268762.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_11,color_FFFFFF,t_70,g_se,x_16" width="454"/>



phpstudy中的集成的phpmyadmin中进入到数据库的管理
可以查看到pikachu数据库不是空表，里面有相关数据表
接下来，我们尝试一下，将其用sql文件的格式到处，在从终端导入到数据库中试试



## 问题解决：

> 
<h2> <img alt="" height="606" src="https://img-blog.csdnimg.cn/adfcdc3b5b42427587383916b27661c6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1045"/></h2>
导出的SQL文件，以及所在的地址<img alt="" height="392" src="https://img-blog.csdnimg.cn/c995aeec9c5242d2bbb65331cd6a60ac.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="749"/>


在数据库终端中带入SQL文件
显示导入成功



再次在终端复查，出现的导入的SQL文件，问题基本解决了


查看到了表中的数据



再次登录就能发现，没有同样的报错的
SQL文件导入了



## 问题二：文件Not Find问题

## 问题重现：

> 
**Not Found**
The requested URL /pikachu-master/vul/ssrf/ssrf_info/info1.php was not found on this server.
Additionally, a 404 Not Found error was encountered while trying to use an ErrorDocument to handle the request.



## 原因分析：

> 
①连接问题：能访问靶场文件，说明连接到数据库
②浏览器访问控制：这个是在本地，一般没什么控制
③phpstudy集成环境的网站php开放功能模块：这个一般自己不随便改就没什么限制（我是没有怎么改过的）
④URL访问问题：这个可能是关键：因为每个人配置的不一样，可能URL会不一样


## 问题解决：

> 
我把端口号也带上去了，最后就显示出来，虽然是和数据库配置成功
但是再次使用URL访问的时候，就还是要正确的输入端口


