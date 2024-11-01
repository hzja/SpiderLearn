# 原创
：  MD5绕过

# MD5绕过

#### MD5绕过

## MD5弱类型比较

```
&lt;?php
highlight_file(__FILE__);
error_reporting(0);
$flag = "flag{H3rmesk1t_is_a_loser}";
$val1 = $_GET['val1'];
$val2 = $_GET['val2'];
if (isset($_GET['val1']) and isset($_GET['val2']))
{
	if ($_GET['val1'] != $_GET['val2'])
	{
		if ((md5($_GET['val1']) == md5($_GET['val2'])))
			echo $flag;
		else
			echo "you can't get flag";
	}
}
?&gt;

```

```
&lt;?php
highlight_file(__FILE__);
error_reporting(0);
$flag = "flag{H3rmesk1t_is_a_loser}";
$val1 = $_GET['val1'];
$val2 = $_GET['val2'];
if (isset($_GET['val1']) and isset($_GET['val2']))
{
	if ($_GET['val1'] != $_GET['val2'])
	{
		if ((md5($_GET['val1']) == md5($_GET['val2'])) and (md5(md5($_GET['val2'])) == md5(md5($_GET['val1']))))
			echo $flag;
		else
			echo "you can't get flag";
	}
}
?&gt;

```

### 方法一：数组绕过

> 
由于md5不能加密数组，在加密数组的时候会返回NULL，所以我们可以传入两个数组<br/> 数组绕过适用于源码中没有判断变量类型或内容，如果加上了过滤函数就不能使用了


```
常见过滤函数如下：

ctype_alnum ( string $text ) : bool
// 如果text中所有的字符全部是字母和(或者)数字，返回 TRUE 否则返回FALSE 

is_numeric ( mixed $var ) : bool
// 如果 var 是数字和数字字符串则返回 TRUE，否则返回 FALSE

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514090811201.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514091708399.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 方法二：科学计数法绕过

> 
可以传入两个md5加密后是0e开头的字符串，需要注意的地方是，这个以0e开头的字符串只能是纯数字，这样php在进行科学计算法的时候才会将它转化为0；可以查找以0e开头md5加密相等的字符串，也可以自己编写代码，提供以下脚本


```
&lt;?php
for($a=1;$a&lt;=1000000000;$a++){
   $md5 = md5($a);
   if(preg_match('/^0e\d+$/',$md5)){
      echo $a;
      echo "\n";
      echo $md5;
      echo "\n";
   }
}

```

> 
常见的字符串


```
byGcY
0e591948146966052067035298880982

QNKCDZO
0e830400451993494058024219903391

s878926199a
0e545993274517709034328855841020

s155964671a
0e342768416822451524974117254469

s214587387a
0e848240448830537924465865611904

s214587387a
0e848240448830537924465865611904

s878926199a
0e545993274517709034328855841020

s1091221200a
0e940624217856561557816327384675

s1885207154a
0e509367213418206700842008763514

240610708
0e462097431906509019562988736854

314282422
0e990995504821699494520356953734

571579406
0e972379832854295224118025748221

903251147
0e174510503823932942361353209384

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514092923920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514092934277.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 双MD5判断

> 
对于有些题目，可能会经过两次MD5值的判断


```
MD5和双MD5以后的值都是0e开头的

CbDLytmyGm2xQyaLNhWn
770hQgrBOjrcqftrlaZk
7r4lGXCH2Ksu2JNT3BYM

```

```
脚本

# -*- coding: utf-8 -*-
import multiprocessing
import hashlib
import random
import string
import sys
CHARS = string.letters + string.digits
def cmp_md5(substr, stop_event, str_len,. start=0, size=20):
    global CHARS
    while not stop_event.is_set():
        rnds = ''.join(random.choice(CHARS) for _ in range(size))
        md5 = hashlib.md5(rnds)
        value = md5.hexdigest()
        if value[start: start+str_len] == substr:
            print rnds
            stop_event.set()
            '''
            #碰撞双md5
            md5 = hashlib.md5(value)
            if md5.hexdigest()[start: start+str_len] == substr:
                print rnds+ "=&gt;" + value+"=&gt;"+ md5.hexdigest()  + "\n"
                stop_event.set()
            '''

if __name__ == '__main__':
    substr = sys.argv[1].strip()
    start_pos = int(sys.argv[2]) if len(sys.argv) &gt; 1 else 0
    str_len = len(substr)
    cpus = multiprocessing.cpu_count()
    stop_event = multiprocessing.Event()
    processes = [multiprocessing.Process(target=cmp_md5, args=(substr,
                                         stop_event, str_len, start_pos))
                 for i in range(cpus)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

```

## 扩展构造

> 
若有要求 md5 值的明文长度很小，其中只能出现一种字母，那么可以写脚本获取明文


```
$a = $_POST['a'];
$b = $_POST['b'];
$m = $_GET['m'];
$n = $_GET['n'];

if (!(ctype_alnum($a)) || (strlen($a) &gt; 5)  || !(ctype_alnum($b)) || (strlen($b) &gt; 6))
{
    echo "a OR b fail!";
    die();
}

if ((strlen($m) &gt; 1) || (strlen($n) &gt; 1))
{
    echo "m OR n fail";
    die();
}

$val8 = md5($a);
$val9 = strtr(md5($b), $m, $n);

echo PHP_EOL;
echo "&lt;p&gt;val8 : $val8&lt;/p&gt;";
echo PHP_EOL;
echo "&lt;p&gt;val9 : $val9&lt;/p&gt;";
echo PHP_EOL;
if (($val8 == $val9) &amp;&amp; !($a === $b) &amp;&amp; (strlen($b) === 5))
{
    echo "nice,good job,give you flag:";
    echo file_get_contents('/var/www/html/flag.php');
}

```

> 
代码的意思就是需要一个长度小于等于 5 的字符串的 md5 值是科学计数法样式<br/> 还需要一个长度等于 5 的字符串的 md5 值在替换一个字符后能变成科学计数法样式的 md5，这也是我们要求的


```
import hashlib
import string

str_list = list(string.letters + string.digits)

for i in range(0, len(str_list)):
    for j in range(0, len(str_list)):
        for k in range(0, len(str_list)):
            for l in range(0, len(str_list)):
                for m in range(0, len(str_list)):
                    tmp = str_list[i] + str_list[j] + str_list[k] + str_list[l] + str_list[m]
                    str_hash = hashlib.md5(tmp).hexdigest()
                    check = str_hash[0:2]
                    str_hash = str_hash[2:32]
                    a = str_hash.replace('a', '1')
                    b = str_hash.replace('b', '1')
                    c = str_hash.replace('c', '1')
                    d = str_hash.replace('d', '1')
                    e = str_hash.replace('e', '1')
                    f = str_hash.replace('f', '1')
                    g = str_hash.replace('g', '1')
                    h = str_hash.replace('h', '1')
                    i1 = str_hash.replace('i', '1')
                    j1 = str_hash.replace('j', '1')
                    k1 = str_hash.replace('k', '1')
                    l1 = str_hash.replace('l', '1')
                    m1 = str_hash.replace('m', '1')
                    n = str_hash.replace('n', '1')
                    o = str_hash.replace('o', '1')
                    p = str_hash.replace('p', '1')
                    q = str_hash.replace('q', '1')
                    r = str_hash.replace('r', '1')
                    s = str_hash.replace('s', '1')
                    t = str_hash.replace('t', '1')
                    u = str_hash.replace('u', '1')
                    v = str_hash.replace('v', '1')
                    w = str_hash.replace('w', '1')
                    x = str_hash.replace('x', '1')
                    y = str_hash.replace('y', '1')
                    z = str_hash.replace('z', '1')
                    if check == '0e' and (
                            a.isdigit() or b.isdigit() or c.isdigit() or d.isdigit() or e.isdigit() or f.isdigit() or g.isdigit() or h.isdigit() or i1.isdigit() or j1.isdigit() or k1.isdigit() or l1.isdigit() or m1.isdigit() or n.isdigit() or o.isdigit() or p.isdigit() or q.isdigit() or r.isdigit() or s.isdigit() or t.isdigit() or u.isdigit() or v.isdigit() or w.isdigit() or x.isdigit() or y.isdigit() or z.isdigit()):
                        print tmp
                        print str_hash

```

## MD5强类型比较

```
&lt;?php
highlight_file(__FILE__);
error_reporting(0);
$flag = "flag{H3rmesk1t_is_a_loser}";
$val1 = $_GET['val1'];
$val2 = $_GET['val2'];
if (isset($_GET['val1']) and isset($_GET['val2']))
{
	if ($_GET['val1'] != $_GET['val2'])
	{
		if ((md5($_GET['val1']) === md5($_GET['val2'])))
			echo $flag;
		else
			echo "you can't get flag";
	}
}
?&gt;

```

### 方法一：数组绕过

> 
因为是强类型比较，用0e开头的字符串是没办法绕过的了，但是PHP自身的特性使得可以提交一个数组<br/> 而md5函数传入数组的返回值都是NULL，这样就可以绕过强类型比较了


### 方法二：使用md5加密后两个完全相等的两个字符串绕过

> 
利用fastcoll_v1.0.0.5.exe来生成符合条件的字符串<br/> 构造：<br/> （1）创建一个文本文件，写入任意的文件内容，命名为ywj.txt （源文件）<br/> （2）运行fastcoll输出以下参数：-p 是源文件，-o是输出文件<br/> 执行命令：`fastcoll_v1.0.0.5.exe -p ywj.txt -o 1.txt 2.txt`<br/> 对产生的1.txt和2.txt文件进行测试


```
&lt;?php 
function  readmyfile($path){
    $fh = fopen($path, "rb");
    $data = fread($fh, filesize($path));
    fclose($fh);
    return $data;
}
echo '二进制md5加密 '. md5( (readmyfile("D:\\ctf工具\\fastcoll_v1.0.0.5.exe\\1.txt")))."\n";
echo  'url编码 '. urlencode(readmyfile("D:\\ctf工具\\fastcoll_v1.0.0.5.exe\\1.txt"))."\n";
echo '二进制md5加密 '.md5( (readmyfile("D:\\ctf工具\\fastcoll_v1.0.0.5.exe\\2.txt")))."\n";
echo  'url编码 '.  urlencode(readmyfile("D:\\ctf工具\\fastcoll_v1.0.0.5.exe\\2.txt"))."\n";

```

```
二进制md5加密 ecd33e3e09ff2a58e1d9ed7189dc186b
url编码 abc%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%D6%16y%AC%CE%C5%A1LrY5fn%94%10%D9%01%C3%AC%F8%AAN%21%D0%27%BE%3Ej%A7%22%0C%D08%D3%AF%DFRo%2F%A4%8B%E8%EB45j%E4h%9C%21%22%AB%7E%BC%8E%7C%17%9E%C3Xg%D7%A8%CDHt%BE%AB.%2FWb%3Eb%EA%FC%261%0F_%3D%AFo%3F%1E%DE%E8i%86%7D%BF%C7_Q%CDA%B4%CF%B8n%06Ir%7F%5C%A3k%F9%2AO%DFF%2A%F3%8BcH%FF%85%3F%0D%D0%9B%C7%C8-%12%92
二进制md5加密 ecd33e3e09ff2a58e1d9ed7189dc186b
url编码 abc%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%D6%16y%AC%CE%C5%A1LrY5fn%94%10%D9%01%C3%ACx%AAN%21%D0%27%BE%3Ej%A7%22%0C%D08%D3%AF%DFRo%2F%A4%8B%E8%EB45%EA%E4h%9C%21%22%AB%7E%BC%8E%7C%17%9E%C3%D8g%D7%A8%CDHt%BE%AB.%2FWb%3Eb%EA%FC%261%0F_%3D%AFo%BF%1E%DE%E8i%86%7D%BF%C7_Q%CDA%B4%CF%B8n%06Ir%7F%5C%A3k%F9%2A%CF%DEF%2A%F3%8BcH%FF%85%3F%0D%D0%9BG%C8-%12%92

```

> 
可以看到，1.txt和2.txt文件二进制md5加密后的结果完全相同。由于1.txt和2.txt文件中含有不可见字符，所以需要将其url编码后使用<br/> 可以看到url编码后的两个字符串不完全相同，满足我们输入两个不同参数的需要


## 哈希长度扩展攻击

### 用途

> 



### hash算法

> 
- MD5加密过程中512比特（64字节）为一组，属于分组加密，而且在运算的过程中，将512比特分为32bit*16块，分块运算- 我们关键利用的是MD5的填充，对加密的字符串进行填充(比特第一位为1其余比特为0)，使之(二进制)补到448模512同余，即长度为512的倍数减64，最后的64位在补充为原来字符串的长度，这样刚好补满512位的倍数，如果当前明文正好是512bit倍数则再加上一个512bit的一组。- MD5不管怎么加密，每一块加密得到的密文作为下一次加密的初始向量IV，这一点很关键


> 
比如说计算字符串`admin`，十六进制`0x64676d696e`，这里与448模512不同余，补位后数据如下：`0x61646d696e8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002800000000000000`


### 攻击原理

> 
这样的话，假设secret只知道位数的话，将其填充成secret1，其中n=hash(secret)=hash(secret1)已知，则hash(secret1+任意数据)都可以求出，因为(secret1+任意数据)会被分为很多组，第一组为secret1，则第一组生成的向量即为n,直接用于接下来的运算即可。所以hash扩展长度攻击我理解就是，已知secret长度和hash值，就可以求出(secret+任意数据)的hash值<br/> 如果一个应用程序是这样操作的：



### 已知salt长度

```
&lt;?php
if (!empty($_COOKIE["getmein"])) {
    if (urldecode($username) === "admin" &amp;&amp; urldecode($password) != "admin") {
        if ($COOKIE["getmein"] === md5($secret . urldecode($username . $password))) {
            echo "Congratulations! You are a registered user.\n";
            die ("The flag is ". $flag);
        }
        else {
            die ("Your cookies don't match up! STOP HACKING THIS SITE.");
        }
    }
    else {
        die ("You are not an admin! LEAVE.");
    }
}

setcookie("sample-hash", md5($secret . urldecode("admin" . "admin")), time() + (60 * 60 * 24 * 7));

```

> 
其中已知`sample-hash`，即`hash(secret+”adminadmin”)`，这时候构造`username=”admin”`，`password=”admin/x80/00…../00gg”`，其中使得`secret+username+password`恰好分为两组，第一组和`secret+adminadmin`一样(因为前面求`hash(secret+”adminadmin”)`时需要填充成`hash(secret+”adminadmin”+”/x80/00…”)`，第二组为`gg`，这时候求`hash(secret+username+password)`等价于求`hash(gg)`，但是初始向量变成第一组的hash值(已知)，然后构造cookie中的getmein提交即可


> 



> 
将得到的第一行设置到cookie的getmein中，第二行为username+password的值


### 未知salt长度

```
攻击代码

import hashpumpy
import urllib
import requests
for i in range(1,30):
	m=hashpumpy.hashpump('3a4727d57463f122833d9e732f94e4e0',';\"tseug\":5:s',';\"nimda\":5:s',i)
	print i		
	url='http://120.26.131.152:32778/'
	digest=m[0]
	
	message=urllib.quote(urllib.unquote(m[1])[::-1])
	cookie='role='+message+'; hsh='+digest
	#print cookie
	headers={
	'cookie': cookie,
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': ':zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate'
}
	print headers
	re=requests.get(url=url,headers=headers)
	print re.text
	if "Welcome" in re.text:
		print re;
		break

```

```
使用说明

&gt;&gt;&gt; import hashpumpy
&gt;&gt;&gt; help(hashpumpy.hashpump)
Help on built-in function hashpump in module hashpumpy:
hashpump(...)
    hashpump(hexdigest, original_data, data_to_add, key_length) -&gt; (digest, message)
    Arguments:
        hexdigest(str):      Hex-encoded result of hashing key + original_data.
        original_data(str):  Known data used to get the hash result hexdigest.
        data_to_add(str):    Data to append
        key_length(int):     Length of unknown data prepended to the hash
    Returns:
        A tuple containing the new hex digest and the new message.
&gt;&gt;&gt; hashpumpy.hashpump('ffffffff', 'original_data', 'data_to_add', len('KEYKEYKEY'))
('e3c4a05f', 'original_datadata_to_add')

```

## 例题

[例题解析链接](https://0clickjacking0.github.io/2020/08/24/CTF%E4%B8%AD%E5%85%B3%E4%BA%8Emd5%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93/)
