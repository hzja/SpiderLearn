# 原创
：  【MySQL无法启动】【靶场连接不到数据库】踩坑过来人~~检查config.inc.php配置文件是关键

# 【MySQL无法启动】【靶场连接不到数据库】踩坑过来人~~检查config.inc.php配置文件是关键

**目录**

[前言：](#%E5%89%8D%E8%A8%80%EF%BC%9A)

[错误重现：](#%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[ 问题一：](#%C2%A0%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9A)

[问题二：](#%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9A)

[问题分析：](#%E9%97%AE%E9%A2%98%E5%88%86%E6%9E%90%EF%BC%9A)

[操作一：](#%E6%93%8D%E4%BD%9C%E4%B8%80%EF%BC%9A)

[操作二：](#%E6%93%8D%E4%BD%9C%E4%BA%8C%EF%BC%9A)

[逆向分析问题，并排除不可能：](#%E9%80%86%E5%90%91%E5%88%86%E6%9E%90%E9%97%AE%E9%A2%98%EF%BC%8C%E5%B9%B6%E6%8E%92%E9%99%A4%E4%B8%8D%E5%8F%AF%E8%83%BD%EF%BC%9A)

[解决办法：](#%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95%EF%BC%9A)

[推荐：](#%E6%8E%A8%E8%8D%90%EF%BC%9A)

---


 

## 前言：

【离奇】：一直用都好好地，突然有一天它无法启动，并且连接不上了

【离谱】：最后试出真相的我，直呼……（无语，居然没有第一反应想到）

【完事】：最后我是成功解决了

## 错误重现：

> 
<h3> 问题一：</h3>
数据库连接失败，请检查config.inc.php配置文件（应该数据库出现了问题）



> 
<h3>问题二：</h3>
在phpstudy面板上启动MySQL后，就自动停止了（打开日志文件看了看）


 PHP Parse error:  syntax error, unexpected end of file in Command line code on line 1
（PHP解析错误：语法错误，在第1行中的命令行代码中的意外结束）
这个意外结束，我就很无奈了


## 问题分析：

### 操作一：

> 
 首先我考虑了是不是MySQL数据库自身出了问题
我进入到数据库文件夹
在命令里面手动打开了MySQL发现没问题
[手动打开数据库](https://blog.csdn.net/qq_53079406/article/details/123047469?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164812593816782094898615%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164812593816782094898615&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-123047469.nonecase&amp;utm_term=%E6%89%8B%E5%8A%A8&amp;spm=1018.2226.3001.4450)
 .\mysql.exe -uroot -p
然后输入密码，就进入数据库了

 （无果，因为还没有找到真正的问题所在）


### 操作二：

> 
分析是不是MySQL数据库和phpstudy之间连接状态啥的出问题了
尝试在phpstudy中再下另一个版本的数据库
我下了最新的MySQL8.0版本


再尝试启动MySQL8.0版本数据库

（不负众望，失败了，还是会自动停止） 


 

 

## 逆向分析问题，并排除不可能：

> 
 想到靶场数据库连接失败，检查config.inc.php配置文件


打开config.inc.php配置文件
我注意到了默认端口问题 （突破口来了）



<img alt="" src="https://img-blog.csdnimg.cn/3619e3accceb457fa1c6e653f250e491.png"/> 

## 解决办法：

> 
 netstat -ano（查看所端口）
netstat -aon|findstr "3306"（查看指定端口）
（下图是我换成3307后的截图）


然后把端口换成了3307，没有选择结束掉3306



在把靶场的连接数据库的config.inc.php配置文件修改新的端口


再次查看，已经能连接到数据库了


如果靶场没初始化的，就初始化一下



## 推荐：

> 
 1、
[【XSS跨站合集】反射型、存储型、DOM类XSS原理+利用过程](https://blog.csdn.net/qq_53079406/article/details/123694180?spm=1001.2014.3001.5501)
2、
[文件上传【绕WAF】【burpsuite才是王道】数据溢出、符号字符变异……](https://blog.csdn.net/qq_53079406/article/details/123525882?spm=1001.2014.3001.5501)
3、
[Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…](https://blog.csdn.net/qq_53079406/article/details/123590641?spm=1001.2014.3001.5501)

