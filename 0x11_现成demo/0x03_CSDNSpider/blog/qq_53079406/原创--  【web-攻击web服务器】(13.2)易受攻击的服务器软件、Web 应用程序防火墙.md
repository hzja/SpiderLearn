# 原创
：  【web-攻击web服务器】(13.2)易受攻击的服务器软件、Web 应用程序防火墙

# 【web-攻击web服务器】(13.2)易受攻击的服务器软件、Web 应用程序防火墙

**目录**

[一、易受攻击的服务器软件](#%E4%B8%80%E3%80%81%E6%98%93%E5%8F%97%E6%94%BB%E5%87%BB%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BD%AF%E4%BB%B6)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、应用程序框架缺陷](#1.2%E3%80%81%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E6%A1%86%E6%9E%B6%E7%BC%BA%E9%99%B7)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[.NET填充提示](#.NET%E5%A1%AB%E5%85%85%E6%8F%90%E7%A4%BA)

[1.3、内存管理漏洞](#1.3%E3%80%81%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86%E6%BC%8F%E6%B4%9E)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.4、编码与规范化漏洞](#1.4%E3%80%81%E7%BC%96%E7%A0%81%E4%B8%8E%E8%A7%84%E8%8C%83%E5%8C%96%E6%BC%8F%E6%B4%9E)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.5、查找Web服务器漏洞](#1.5%E3%80%81%E6%9F%A5%E6%89%BEWeb%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%BC%8F%E6%B4%9E)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.6、保障Web服务器软件的安全](#1.6%E3%80%81%E4%BF%9D%E9%9A%9CWeb%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BD%AF%E4%BB%B6%E7%9A%84%E5%AE%89%E5%85%A8)

[选择记录良好的软件](#%E9%80%89%E6%8B%A9%E8%AE%B0%E5%BD%95%E8%89%AF%E5%A5%BD%E7%9A%84%E8%BD%AF%E4%BB%B6)

[应用供应商发布的补丁](#%E5%BA%94%E7%94%A8%E4%BE%9B%E5%BA%94%E5%95%86%E5%8F%91%E5%B8%83%E7%9A%84%E8%A1%A5%E4%B8%81)

[实施安全强化](#%E5%AE%9E%E6%96%BD%E5%AE%89%E5%85%A8%E5%BC%BA%E5%8C%96)

[监控新的漏洞](#%E7%9B%91%E6%8E%A7%E6%96%B0%E7%9A%84%E6%BC%8F%E6%B4%9E)

[使用深层防御](#%E4%BD%BF%E7%94%A8%E6%B7%B1%E5%B1%82%E9%98%B2%E5%BE%A1)

[二、Web 应用程序防火墙](#%E4%BA%8C%E3%80%81Web%20%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%98%B2%E7%81%AB%E5%A2%99)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

---


## 一、易受攻击的服务器软件

> 
<h3>1.1、简介：</h3>
1、Web服务器软件的形式各异，包括仅用于显示静态页面的极其简单的轻量级软件，以及能够处理各种任务，提供除业务逻辑本身以外的所有功能的高度复杂的应用程序平台。就后者而言，大多认为这类框架是安全的。以前Web服务器软件被一系列严重的安全漏洞所困扰，使得攻击者能够执行任意代码，窃取文件和提升权限，主流Web服务器平台已变得日渐可靠。许多情况下，核心功能仍保持静态，甚至经过精简，因为供应商有意减少默认的受攻击面。
2、但即使这些漏洞越来越少，其背后的原理仍然适用，人们在各类软件（通常为并行技术或服务器产品）中均发现了新的漏洞，除一些小型个人Web服务器及其他次要目标外，这些新漏洞大多存在于以下软件之中：IIS和Apache中的服务器端扩展；从头开发的新型Web服务器，这类服务器主要用于支持特定的应用程序，或作为开发环境的一部分提供。它们可能较少受到现实世界中的黑客的关注，因而更可能存在上述问题。


> 
<h3>1.2、应用程序框架缺陷</h3>
<h4>简述：</h4>
Web应用程序框架一直存在各种严重的缺陷，常见缺陷导致在该框架上运行的许多应用程序都易于受到攻击
<hr/>
<h4>.NET填充提示</h4>
1、.NET对CBC分组密码使用PKCS #5填充，其操作方式如下
分组密码基于固定的分组大小进行操作，在NET中，这样的分组通常为8或16字节，.NET采用PKCS#5标准为每一个明文字符串添加填充字节，以确保生成的明文字符串长度可以被分组大小整除。这时.NET不是使用任意值进行填充，选择用于填充的值是填充字节的数量，每个字符串都会被填充，如果初始字符串是分组大小的倍数，将填充整个分组。因此如果分组大小为8，则必须使用1个0x01字节、2 个0x02字节，或最多8个0x08字节的任意组合进行填充。然后将第一条消息的明文与称为初始化向量(IV) 的预设消息分组进行XOR运算，接下来第二条消息将与第一条消息的密文进行XOR运算，从而开始循环分组链

2、整个.NET加密过程：
A、选择明文消息
B、使用所需的填充字符数作为填充字节值填充该消息
C、将第一个明文分组与初始化向量进行XOR运算
D、使用三重DES加密从第3步的XOR运算得到的值
从这时开始，将循环执行以下E、F步骤，以加密剩余的消息
E、将第二个明文分组与加密后的前一个分组进行XOR运算
F、使用三重DES加密XOR运算得到的值


#### .NET填充提示

> 
<h3>1.3、内存管理漏洞</h3>
<h4>简述：</h4>
由于攻击者可以利用缓冲区溢出控制易受攻击的进程， 因此这种漏洞是影响各种软件的最严重的漏洞。如果攻击者能够在Web服务器中执行任意代码， 就能攻破其中运行的任何应用程序
列举少数几种Web服务器缓冲区溢出漏洞；但这足以证明这种漏洞的普遍性，它存在于大量web服务器产品与组件中：Apache mod_isapi悬挂指针、Microsoft IIS ISAPI扩展、Apache分块编码溢出、WebDAV溢出、


> 
<h3>1.4、编码与规范化漏洞</h3>
<h4>简述：</h4>
1、可以使用各种编码方案对不常见的字符和内容进行编码，以方便通过HTTP安全传送。如果Web应用程序中存在几种类型的漏洞，攻击者就可以利用这些编码方案避开输入确认检查，实施其他攻击

2、许多Web服务器软件中都存在编码漏洞，如果用户提交的相同数据被使用各种技术的几个保护层处理，编码漏洞就会造成严重的威胁。一个典型的Web请求可能被Web服务器、应用程序平台、各种托管与非托管API 、其他软件组件与基础操作系统处理，如果不同的组件以不同的方式执行一种编码方案，或对部分编码的数据进行其他解码或注释，那么攻击者就可以利用这种行为避开过滤或造成其他反常行为

3、路径遍历是可通过规范化缺陷加以利用的最常见漏洞之一，因为它总是涉及与操作系统的通信，各种Web服务器软件中也可能存在这种类型的漏洞，导致攻击者能够读取或写入Web根目录以外的任何文件：Apple iDisk Server路径遍历、Ruby WEBrick Web服务器、Java Web服务器目录遍历、Allaire JRun目录列表漏洞、Microsoft IIS Unicode路径遍历漏洞、避开oracle PL/SQL排除列表


> 
<h3>1.5、查找Web服务器漏洞</h3>
<h4>简述：</h4>
1、在Web服务器等非定制产品中查找漏洞时，使用自动化扫描工具是一个不错的起点。与Web应用程序这些定制产品不同，几乎所有的Web服务器都使用第三方软件，并且有无数用户已经以相同的方式安装和配置了这些软件。在这种情况下，使用自动化扫描器发送大量专门设计的请求并监控表示已知漏洞的签名，就可以迅速、高效地确定最明显的漏洞。Nessus是一款非常不错的免费漏洞扫描器，当然也可以使用各种商业扫描器。
2、除使用扫描工具外，还应始终对所攻击的软件进行深人研究。同时浏览Security Focus、OSVDB、邮件列表Bugtraq和Full Disclosure等资源，在目标软件上查找所有最近发现的、尚未修复的漏洞信息。同时查看Exploit Database和Metasploit, 看看是不是有人已经做了相关工作， 并发现了相应的漏洞


3、一些Web应用程序产品中内置了开源Web服务器，如Apache或Jetty，因为管理员把服务器看作他们所安装的应用程序，而不是他们负责的基础架构的一部分，所以这些捆绑服务器的安全更新也应用得相对较为缓慢． 而且在这种情况下，标准的服务标题也已被修改。因此，对所针对的软件进行手动测试与研究，可以非常有效地确定自动化扫描工具无法发现的漏洞
4、尽可能考虑在本地安装所攻击的软件，并自己进行测试，查找任何尚未发现的新漏洞或广泛流传的漏洞


> 
<h3>1.6、保障Web服务器软件的安全</h3>
<h4>选择记录良好的软件</h4>
并非所有软件产品与供应商都提供同等优良的服务，分析几种不同的服务器产品的最近历史可以发现，它们在存在的严重漏洞数量、供应商修复这些漏洞是否及时以及发布的补丁在随后测试过程中表现的适应性等方面存在明显的差异，在选择部署何种Web服务器软件之前，应该研究这些差异， 并考虑如果所在的组织采用了选择的软件，它在近几年将会如何运转
<hr/>
<h4>应用供应商发布的补丁</h4>
任何有责任的软件供应商必须定期发布安全更新。有时这些补丁能够解决供应商自身在内部发现的问题，其他情况下，软件问题由专门的研究员上报，但无法确定他是否保留了一些信息。其他漏洞因为被攻击者广泛利用，因而引起供应商的注意。但无论是上述哪一种情况，一旦供应商发布补丁，任何强大的逆向工程方法都能立即查明它所解决的问题所在使攻击者能够着手设计利用这个问题的攻击。因此如果可行，应尽可能及时地应用安全补丁
<hr/>
<h4>实施安全强化</h4>
大多数Web服务器都拥有大量的配置选项，可控制在其中激活哪些功能，同时控制它们的运行状态。如果无用的功能（如默认ISAPI扩展）仍然被激活，那么只要攻击者在这项功能中发现新的漏洞，服务器就会受到严重的攻击威胁，用户应该查阅与所使用的软件有关的强化指南，同时还应考虑采用以下这些常用的强化步骤
1、禁用任何不需要的内置功能，配置剩下的功能尽可能严格地运行，与商业需求保持一致。这包括删除映射的文件扩展名 、Web服务器模块和数据库组件。可以使用IIS Lockdown等工具迅速完成这项任务
2、如果应用程序由任何其他以本地代码开发的定制服务器扩展组成，则应考虑是否可以使用托管代码重新编写这些扩展。如果不能，则应确保托管代码环境先执行其他输入确认，然后再将输入传递给这些功能
3、可以对需要保留的许多功能与资源进行重命名，以防止攻击者利用它们实施另一层障碍。即使攻击者仍然能够发现重命名后的名称，但这种模糊处理可以阻止攻击者新手与自动化蠕虫
4、在整个技术栈中应用最低权限原则。例如应配置Web服务器进程使用最低权限的操作系统账户。还可以在UNIX系统上使用chroot环境进一步限制任何攻击的影响范围
<hr/>
<h4>监控新的漏洞</h4>
应指派一名组织职员负责监控Bugtraq与FullD芯losure等资源，查找与所使用的软件中新发现的漏洞有关的公告与讨论。还可以祯订各种私人服务，由他们提供软件中已经发现但尚未公开披露的最新漏洞通知。通常如果了解与某个漏洞有关的技术细节，就可以在供应商发布完整的补丁前，有效地修改这个漏洞
<hr/>
<h4>使用深层防御</h4>
应该始终实施几层保护，减轻基础架构组件中的任何安全违反造成的影啊，可以采取各种措施，将针对Web服务器的成功攻击的影响限制在局部范围内，即使Web服务器被完全攻破，这些措施也让用户有足够的时间防止任何严重的数据泄露
1、可以限制Web服务器访问其他自治的应用程序组件。例如应只允许应用程序使用的数据库账户INSERT访问用于保存审计日志的表，这意味着，即使攻击者攻破Web服务器，也无法删除已经创建的任何日志记录
2、可以对进出Web服务器的流量实施严格的网络级过滤
3、可以使用一个入侵检测系统确定任何表明发生安全违反的反常网络活动，攻破Web服务器后许多攻击者会立即尝试建立反向连接，侵入因特网，或扫描DMZ网络中的其他主机。高效的入侵检测系统将实时通知这些事件，以便用户采取措施阻止攻击


#### 应用供应商发布的补丁

---


#### 监控新的漏洞

---


---


---


## 二、Web 应用程序防火墙

> 
<h3>2.1、简介：</h3>
许多应用程序都受到某种外部组件的保护，这些组件或位于应用程序所在的同一主机上或位于基于网络的设备上，它们要么执行入侵防御（应用程序防火墙）， 要么执行入侵检测（如传统的入侵检测系统），由于这类设备用于确定攻击的方法基本类似， 因此将把它们当做同一类设备对待。虽然许多人认为安装这类设备总比什么都不做要强，但许多时候它们会造成一种错误的安全意识，觉得既然实施了另一层防御，安全状况将会自动改善。虽然此类系统并不会降低安全防御，并且可以阻止目标明确的攻击（如因特网蠕虫），但在许多情况下，并不像人们认为的那样能够显著改善安全状况。

值得注意的是，除非此类防御设备采用大量定制规则，否则它们并不能防御一些漏洞，并且在防范业务逻辑中的潜在漏洞方面也没有任何实际用途。同时，它们也无法防范某些特定的攻击，如基于DOM的XSS。至于其他漏洞（利用这些漏洞的攻击会表现出某种攻击模式）
<hr/>
以下问题通常会降低Web应用程序防火墙的用处：
1、如果防火墙过于严格地遵循HTTP规范，它可能会对应用程序服务器如何处理请求做出假设。相反网络层防御中的防火墙或IDS设备通常并不了解某些HTTP传输方法的细节
2、请求通过防火墙后，在处理请求的过程中，应用程序服务器本身可能会修改用户输入，如对其进行解码、添加转义字符，或过滤掉特定字符串。许多攻击步骤均以避开输入确认为目标，应用程序层防火墙可能易于受到类似的攻击
3、许多防火墙和IDS警报基于特定的常见攻击有效载荷，而不是基于利用漏洞的常规方法。如果攻击者能够检索文件系统中的任意文件． 针对/manager/viewtempl?loc=/etc/passwd的请求可能会被阻止，但针对/manager/viewtempl?loc=/etc/log/syslog的请求并不会被视为攻击，即使其内容可能对攻击者更加有用
<hr/>
从整体看，并不需要区分全局输入确认过滤器、基于主机的代理或基于网络的Web应用程序防火墙
可以使用以下步骤推断是否安装了Web应用程序防火墙：
1、在参数值中使用明确的攻击有效载荷向应用程序（最好是响应中包含名称或值的某个应用程序位置）提交任意参数名称。如果应用程序阻止该攻击，这可能是由于外部防御机制所致。
2、如果可以提交在服务器响应中返回的变量，则提供一系列模糊测试字符串及这些字符串的编码形式可以确定应用程序的用户输入防御行为。
3、对应用程序中的变量实施相同的攻击来确认这一行为
<hr/>
在尝试避开Web应用程序防火墙时：
1、对于所有模糊测试字符串和请求，使用标准签名数据库中不可能存在的良性字符串作为有效载荷。根据定义，不可能提供这些字符串的示例。但在进行文件检索时，应避免将/etc/passwd或/windows/system32/config/sam作为有效载荷。此外应在XSS攻击中避免使用&lt;script&gt;，并避免将alert()或xss用作XSS有效载荷
2、如果特定请求被阻止，可以尝试在其他位置或上下文中提交相同的参数。例如在GET请求的URL中、在POST请求主体中，以及在POST请求的URL中提交相同的参数
3、应尝试在ASP.NET上将参数作为cookie提交。如果在查询字符串或消息主体中找不到参数foo，API Request.Params["foo"]会检索名为foo的cookie的值
4、引入用户输入的所有其他方法，选择其中任何不受保护的方法
5、确定以非标准格式（如序列化或编码）或可能以此类格式损交用户输入的位置。如果找不到此类位置，可以通过串联字符串和/或将字符串分布到多个参数中来构建攻击字符串


---

