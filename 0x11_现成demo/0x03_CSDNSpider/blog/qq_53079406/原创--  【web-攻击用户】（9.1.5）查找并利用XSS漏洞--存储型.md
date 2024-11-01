# 原创
：  【web-攻击用户】（9.1.5）查找并利用XSS漏洞--存储型

# 【web-攻击用户】（9.1.5）查找并利用XSS漏洞--存储型

**目录**

[查找并利用存储型XSS漏洞](#%E6%9F%A5%E6%89%BE%E5%B9%B6%E5%88%A9%E7%94%A8%E5%AD%98%E5%82%A8%E5%9E%8BXSS%E6%BC%8F%E6%B4%9E)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、过程：](#1.2%E3%80%81%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.3、在Web邮件应用程序中测试XSS](#1.3%E3%80%81%E5%9C%A8Web%E9%82%AE%E4%BB%B6%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E4%B8%AD%E6%B5%8B%E8%AF%95XSS)

[1.4、在上传文件中测试XSS](#1.4%E3%80%81%E5%9C%A8%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6%E4%B8%AD%E6%B5%8B%E8%AF%95XSS)

[混合文件攻击](#%E6%B7%B7%E5%90%88%E6%96%87%E4%BB%B6%E6%94%BB%E5%87%BB)

[在通过Ajax上传的文件中测试XSS](#%E5%9C%A8%E9%80%9A%E8%BF%87Ajax%E4%B8%8A%E4%BC%A0%E7%9A%84%E6%96%87%E4%BB%B6%E4%B8%AD%E6%B5%8B%E8%AF%95XSS)

---


## 查找并利用存储型XSS漏洞

> 
<h3>1.1、简介：</h3>
确定存储型XSS漏洞的过程与确定反射型XSS漏洞的过程有很多相似之处， 都包括在应用程序的每一个进入点提交一个特殊字符串。但这两个过程之间也存在一些重要的区别。在进行测试时， 必须记住这些区别， 以确定尽可能多的漏洞。


> 
<h3>1.2、过程：</h3>
1、向应用程序中的每一个可能的位置提交一个特殊的字符串后， 必须反复检查应用程序的全部内容与功能， 确定这个字符串在浏览器中显示的任何情况。在某个位置（如个人信息页面的姓名字段输入用户控制的数据， 这个数据可能会在应用程序的许多不同位置显示（如用户主页上、注册用户列表中、任务等工作流程项目中、其他用户的联系列表中、用户提交的消息或问题中、应用程序日志中等），应用程序可能对每个出现的字符串实施了不同的保<br/> 护性过滤，因此需要对它们进行单独分析

2、应检查管理员能够访问的所有应用程序区域，确定其中是否存在任何可被非管理用户控制的数据。如应用程序一般允许管理员在浏览器中检查日志文件。这种类型的功能极有可能包含XSS漏洞，攻击者通过生成含有恶意HTML的日志记录即可对其加以利用

3、在向应用程序中的每个位置提交一个测试字符串时，并不总是把它作为每个页面的每一个参数这样简单，在保存被提交的数据之前，许多应用程序功能需要经历几个阶段的操作。如注册新用户、处理购物订单、转账等操作往往需要按预定的顺序提交几个不同的请求。为避免遗漏任何漏洞，必须确保每次测试彻底完成。

4、在探查反射型XSS漏洞时，应该注意可控的受害者请求的每一个方面，包括请求的所有参数和每一个HTTP消息头，在探查存储型XSS漏洞时，还应该分析应用程序用于接收并处理可控输入的任何带外通道，任何这类通道都是引入存储型XSS攻击的适当攻击向量。同时，审查在应用程序解析过程中得到的结果，确定每一个可能的受攻击面。

5、如果应用程序允许文件上传与下载，应始终探查这种功能是否易于受到存储型XSS攻击

6、思考确定控制的数据是否可通过任何其他方法保存在应用程序中并显示给其他用户。如果应用程序的搜索功能显示常用的搜索项列表， 就可以通过多次搜素这个列表，引入存储型XSS有效载荷，即使主搜索功能本身安全地处理输入



确定用户控制的数据被应用程序保存并随后在浏览器中显示的每一种情况后，应当遵循与前面描述的探查潜在的反射型XSS漏洞时相同的过程，决定需要提交哪些输入，以在周围的HTML中嵌入有效的JavaScript，然后尝试避开干扰攻击有效载荷执行的过滤


在探查反射型XSS漏洞时，每次测试一个参数，并检查每个响应中是否出现输入，就可以轻易确定哪些请求参数易于受到攻击。但在探查存储型XSS漏洞时，要确定这一点并不容易。如果在每个页面的每一个参数提交相同的测试字符串，那么可能会发现，这个字符串在应用程序的许多位置重复出现，因而无法准确确定每个出现的字符串由哪个参数负责。为避免出现这个问题，在探查存储型XSS时，可以为每个参数提交一个不同的测试字符串，如把测试字符串与它提交到其中的字段名称连接起来


> 
<h3>1.3、在Web邮件应用程序中测试XSS</h3>

1、由于Web邮件应用程序将直接从第三方收到的内容包含在向用户显示的应用程序页面中，这种程序本身就存在存储型XSS攻击风险。要测试这种功能， 应该在该应用程序上创建自己的电子邮件账户，并通过电子邮件向自己实施大量xss攻击，然后在该应用程序中查看每封邮件， 确定是否有任何攻击取得成功

2、为彻底完成这一任务，需要通过电子邮件发送各种反常的HTML内容（如在测试避开输入过滤的方法）。如果仅限于使用标准电子邮件客户端，可能会发现，无法完全控制原始的邮件内容， 或者邮件客户端可能会净化有意设计的畸形语法

3、最好是采用其他方法来生成电子邮件，以便于直接控制邮件的内容。一种方法是使用UNIX sendmail命令。首先需要使用应当用于向外发送电子邮件的邮件服务器的详细信息配置电脑，再可以在文本编辑器中创建原始的电子邮件，并使用命令发送该邮件


> 
<h3>1.4、在上传文件中测试XSS</h3>
1、如果应用程序允许用户上传可被其他用户下载并查看的文件， 就会出现保存型XSS漏洞，这种漏洞常常被人们忽略，如今的应用程序通常都提供文件上传功能，除传统的用于文件共享的工作流功能外，文件还可以通过电子邮件附件的形式传送给Web邮件用户，图像文件则可以附加到文章中， 并且可以用作定制的头像或通过相册共享

2、影响因素
文件上传过程中，可能会限制可以上传的文件的扩展名
文件上传过程中，可能会检查文件内容， 以确认其是否为所需的格式， 如JPEG
文件下载过程中，可能会返回Content-Type消息头， 以指定文件所包含的内容的类型， 如image/jpeg
在文件下载过程中，可能会返回Concenc-Disposition消息头， 以指定浏览器应将文件保存到磁盘上。否则对于相关的内容类型，应用程序会处理并在用户的浏览器中显示文件

3、在测试文件上传功能时， 首先应该尝试上传一个包含概念验证脚本的简单HTML文件。如果该文件被接受，则尝试以正常方式下载该文件，如果应用程序按原样返回最初的文件，并且脚本得以执行， 则应用程序肯定易于受到攻击
如果应用程序阻止上传的文件， 则尝试使用各种文件扩展名， 包括.txt和.jpg。如果在使用其他扩展名时，应用程序接受包含HTML的文件，则应用程序可能仍然易于受到攻击，具体取决于其在下载过程中如何传送文件。Web邮件应用程序通常易于受到这类攻击，攻击者可以发送包含诱惑性图像附件的电子邮件， 如果用户查看该附件， 他们的会话将被攻破
即使应用程序返回Content-Type消息头，指定下载文件应为图像， 但如果文件实际包含的是HTML内容， 一些浏览器仍然会将该文件作为HTML处理
<hr/>
<h4>混合文件攻击</h4>
为防范上述攻击，应用程序会对上传文件的内容执行某种确认，以确保其确实包含所需格式的数据。但使用混合文件（在一个文件中组合多种不同的格式）仍然可以对这些应用程序实施攻击。
GIFAR文件就是一种常见的混合文件。GIFAR文件包含GIF图像格式和JAR(Java档案）格式的数据，并且是这两种格式的有效实例。这是因为， 与GIF格式相关的文件元数据位于文件的开始部分，与JAR格式相关的元数据则位于文件的结尾部分。如果应用程序允许包含GIF数据的文件， 那么，在确认上传文件的内容时，该应用程序也可能会接受GIFAR文件

使用GIFAR文件实施的上传文件攻击步骤
1、发现由一名用户上传的GIF文件可由其他用户下载（如社交网络应用程序中的用户头像）的应用程序功能。
2、构建一个GIFAR文件，在其中包含一段Java代码，用于劫持任何执行该代码的用户的会话
3、将该文件作为他的头像上传，因为其中包含有效的GIF图像，应用程序将接受该图像
4、确定可利用上传的文件对其实施攻击的适当外部网站，该网站可能为攻击者自己的网站， 或允许用户创建任意HTML（如博客）的第三方站点
5、在该外部网站上，攻击者使用&lt;applet&gt;和&lt;object&gt;标签从上述社交网络站点以Java applet的形式上传GIFAR文件
6、如果用户访问该外部站点，攻击者的Java applet将在其浏览器中执行，与包含正常脚本的文件不同，在遇到Java applet时，同源策略的执行方式会有所不同。Java apple将被视为属于加载它的域，而不是调用它的域。因此攻击者的applet将在社交网络应用程序的域中执行。如果受害用户在受到攻击时已登录该社交网络应用程序，或最近曾登录该应用程序并选中了保持登录状态选项， 则攻击者的applet将完全控制受害用户的会话，从而侵入该用户
<hr/>
<h4>在通过Ajax上传的文件中测试XSS</h4>
1、一些应用程序使用Ajax来检索和呈现在片段标识符之后指定的URL（如http://xxx.com/#profile）
当用户单击链接时， 客户端脚本将处理单击事件，使用Ajax来检索在片段标识符之后显示的件， 并在现有页面中的&lt;div&gt;元素的innerHtml中设置响应，这样可提供无缝的用户体验，因为单击用户界面中的选项卡将更新所显示的内容， 而无须重新加载整个页面

2、在这种情况下，如果应用程序还包含其他允许上传和下载图像文件（如用户头像）的功能，就可以上传一个包含嵌入式HTML标记的有效图像文件，并构建URL（http://xxx.com/#profile/image/13213.jpg），使客户端代码提取该图像并将其作为HTML显示
3、HTML可以嵌入到有效图像文件的各种位置，包括图像的注释部分，一些浏览器乐于将图像文件以HTML格式显示。图像的二进制部分将显示为乱码， 而任何嵌入的HTML将正常显示
4、假设潜在的受害者使用的是兼容HTML5的浏览器，如果所请求的域许可，该浏览器可用于跨域传送Ajax请示。在这种情况下，另一种可能的攻击方法，是在片段标识符后面放置一个绝对URL, 指定一个位于可与目标域进行Ajax交互的股务器上的、完全由攻击者控制的外部HTML文件。如果客户端脚本不确认所请示的URL是否在同一个域上， 客户端远程文件包含攻击将取得成功


#### 混合文件攻击

---

