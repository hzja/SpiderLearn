# 原创
：  【burpsuite安全练兵场-服务端7】访问控制漏洞和权限提升-11个实验（全）

# 【burpsuite安全练兵场-服务端7】访问控制漏洞和权限提升-11个实验（全）

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
（1）纵向权限提升、不受保护的功能、基于参数的访问控制方法、平台配置错误导致访问控制中断、横向权限提升（√）
（2）、横向到纵向权限提升、不安全的直接对象引用、、多步骤流程中的访问控制漏洞、基于引用的访问控制、基于位置的访问控制（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、访问控制](#%E4%B8%80%E3%80%81%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[1、定义：](#1%E3%80%81%E5%AE%9A%E4%B9%89%EF%BC%9A)

[2、危害](#2%E3%80%81%E5%8D%B1%E5%AE%B3)

[3、垂直访问控制](#3%E3%80%81%E5%9E%82%E7%9B%B4%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[4、水平访问控制](#4%E3%80%81%E6%B0%B4%E5%B9%B3%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[5、上下文相关的访问控制](#5%E3%80%81%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9B%B8%E5%85%B3%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[二、破坏访问控制的示例](#%E4%BA%8C%E3%80%81%E7%A0%B4%E5%9D%8F%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E7%9A%84%E7%A4%BA%E4%BE%8B)

[1、纵向权限提升](#1%E3%80%81%E7%BA%B5%E5%90%91%E6%9D%83%E9%99%90%E6%8F%90%E5%8D%87)

[2、不受保护的功能](#2%E3%80%81%E4%B8%8D%E5%8F%97%E4%BF%9D%E6%8A%A4%E7%9A%84%E5%8A%9F%E8%83%BD)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E4%B8%8D%E5%8F%97%E4%BF%9D%E6%8A%A4%E7%9A%84%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD)[实验1：不受保护的管理功能](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E4%B8%8D%E5%8F%97%E4%BF%9D%E6%8A%A4%E7%9A%84%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%B8%8D%E5%8F%97%E4%BF%9D%E6%8A%A4%E7%9A%84%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%EF%BC%8CURL%E4%B8%8D%E5%8F%AF%E9%A2%84%E6%B5%8B)[实验2：不受保护的管理功能，URL不可预测](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%B8%8D%E5%8F%97%E4%BF%9D%E6%8A%A4%E7%9A%84%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%EF%BC%8CURL%E4%B8%8D%E5%8F%AF%E9%A2%84%E6%B5%8B)

[3、基于参数的访问控制方法](#3%E3%80%81%E5%9F%BA%E4%BA%8E%E5%8F%82%E6%95%B0%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%E7%9A%84%E7%94%A8%E6%88%B7%E8%A7%92%E8%89%B2)[实验3：由请求参数控制的用户角色](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%E7%9A%84%E7%94%A8%E6%88%B7%E8%A7%92%E8%89%B2)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%8F%AF%E4%BB%A5%E5%9C%A8%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%B8%AD%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%E8%A7%92%E8%89%B2)[实验4：可以在用户配置文件中修改用户角色](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%8F%AF%E4%BB%A5%E5%9C%A8%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%B8%AD%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%E8%A7%92%E8%89%B2)

[4、平台配置错误导致访问控制中断](#4%E3%80%81%E5%B9%B3%E5%8F%B0%E9%85%8D%E7%BD%AE%E9%94%99%E8%AF%AF%E5%AF%BC%E8%87%B4%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E4%B8%AD%E6%96%AD)

[        ](#%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E5%8F%AF%E4%BB%A5%E7%BB%95%E8%BF%87%E5%9F%BA%E4%BA%8EURL%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)[实验10：可以绕过基于URL的访问控制](#%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E5%8F%AF%E4%BB%A5%E7%BB%95%E8%BF%87%E5%9F%BA%E4%BA%8EURL%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%8F%AF%E4%BB%A5%E7%BB%95%E8%BF%87%E5%9F%BA%E4%BA%8E%E6%96%B9%E6%B3%95%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)[实验11：可以绕过基于方法的访问控制](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%8F%AF%E4%BB%A5%E7%BB%95%E8%BF%87%E5%9F%BA%E4%BA%8E%E6%96%B9%E6%B3%95%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[5、横向权限提升](#5%E3%80%81%E6%A8%AA%E5%90%91%E6%9D%83%E9%99%90%E6%8F%90%E5%8D%87)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%E7%9A%84%E7%94%A8%E6%88%B7ID)[实验5：由请求参数控制的用户ID](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%E7%9A%84%E7%94%A8%E6%88%B7ID)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%EF%BC%8C%E7%94%A8%E6%88%B7ID%E4%B8%8D%E5%8F%AF%E9%A2%84%E6%B5%8B%C2%A0)[实验6：用户ID由请求参数控制，用户ID不可预测 ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%EF%BC%8C%E7%94%A8%E6%88%B7ID%E4%B8%8D%E5%8F%AF%E9%A2%84%E6%B5%8B%C2%A0)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%EF%BC%8C%E9%87%8D%E5%AE%9A%E5%90%91%E6%97%B6%E5%8F%91%E7%94%9F%E6%95%B0%E6%8D%AE%E6%B3%84%E6%BC%8F%C2%A0)[实验7：用户ID由请求参数控制，重定向时发生数据泄漏 ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6%EF%BC%8C%E9%87%8D%E5%AE%9A%E5%90%91%E6%97%B6%E5%8F%91%E7%94%9F%E6%95%B0%E6%8D%AE%E6%B3%84%E6%BC%8F%C2%A0)

[6、横向到纵向权限提升](#6%E3%80%81%E6%A8%AA%E5%90%91%E5%88%B0%E7%BA%B5%E5%90%91%E6%9D%83%E9%99%90%E6%8F%90%E5%8D%87)

[        ](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E5%AF%86%E7%A0%81%E6%B3%84%E9%9C%B2%E7%9A%84%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6)[实验8：用户ID由密码泄露的请求参数控制](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E7%94%A8%E6%88%B7ID%E7%94%B1%E5%AF%86%E7%A0%81%E6%B3%84%E9%9C%B2%E7%9A%84%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E6%8E%A7%E5%88%B6)

[7、不安全的直接对象引用](#7%E3%80%81%E4%B8%8D%E5%AE%89%E5%85%A8%E7%9A%84%E7%9B%B4%E6%8E%A5%E5%AF%B9%E8%B1%A1%E5%BC%95%E7%94%A8)

[        ](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E4%B8%8D%E5%AE%89%E5%85%A8%E7%9A%84%E7%9B%B4%E6%8E%A5%E5%AF%B9%E8%B1%A1%E5%BC%95%E7%94%A8)[实验9：不安全的直接对象引用](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E4%B8%8D%E5%AE%89%E5%85%A8%E7%9A%84%E7%9B%B4%E6%8E%A5%E5%AF%B9%E8%B1%A1%E5%BC%95%E7%94%A8)

[8、多步骤流程中的访问控制漏洞](#8%E3%80%81%E5%A4%9A%E6%AD%A5%E9%AA%A4%E6%B5%81%E7%A8%8B%E4%B8%AD%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E6%BC%8F%E6%B4%9E)

[        ](#%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E5%A4%9A%E6%AD%A5%E9%AA%A4%E6%B5%81%E7%A8%8B%EF%BC%8C%E5%85%B6%E4%B8%AD%E4%B8%80%E4%B8%AA%E6%AD%A5%E9%AA%A4%E6%B2%A1%E6%9C%89%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%C2%A0)[实验10：多步骤流程，其中一个步骤没有访问控制 ](#%E5%AE%9E%E9%AA%8C10%EF%BC%9A%E5%A4%9A%E6%AD%A5%E9%AA%A4%E6%B5%81%E7%A8%8B%EF%BC%8C%E5%85%B6%E4%B8%AD%E4%B8%80%E4%B8%AA%E6%AD%A5%E9%AA%A4%E6%B2%A1%E6%9C%89%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%C2%A0)

[9、基于引用的访问控制](#9%E3%80%81%E5%9F%BA%E4%BA%8E%E5%BC%95%E7%94%A8%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%9F%BA%E4%BA%8E%E5%BC%95%E7%94%A8%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%C2%A0)[实验11：基于引用的访问控制 ](#%E5%AE%9E%E9%AA%8C11%EF%BC%9A%E5%9F%BA%E4%BA%8E%E5%BC%95%E7%94%A8%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%C2%A0)

[10、基于位置的访问控制](#10%E3%80%81%E5%9F%BA%E4%BA%8E%E4%BD%8D%E7%BD%AE%E7%9A%84%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)

---


## 一、访问控制

> 
<h3>1、定义：</h3>
1、访问控制（或授权）是对谁可以执行尝试的操作或访问他们请求的资源施加约束。在Web应用程序的上下文中，访问控制取决于身份验证和会话管理：
（1）身份验证可识别用户并确认他们的身份<br/> （2）会话管理标识该用户正在发出哪些后续HTTP请求<br/> （3）访问控制确定是否允许用户执行他们尝试执行的操作
<hr/>
<h3>2、危害</h3>
1、破坏访问控制是一种常见的安全漏洞，通常是严重的安全漏洞。访问控制的设计和管理是一个复杂的动态问题，它将业务、组织和法律的约束应用于技术实现。访问控制设计决策必须由人而不是技术来做出，并且出错的可能性很高。
<hr/>
2、从用户的角度来看，访问控制可分为：垂直访问控制、水平访问控制、上下文相关的访问控制
<hr/>
<h3>3、垂直访问控制</h3>
1、原理：垂直访问控制是限制对其他类型用户不可用的敏感功能的访问的机制。
————
2、危害：利用垂直访问控制，不同类型的用户可以访问不同的应用程序功能。如管理员可以修改或删除任何用户的帐户，而普通用户则无权执行这些操作。垂直访问控制可以是安全模型的更细粒度的实现，这些安全模型被设计用于强制执行业务策略，如职责分离和最小特权。 
<hr/>
<h3>4、水平访问控制</h3>
1、原理：水平访问控制是将对资源的访问限制到被特别允许访问那些资源的用户的机制。
————
2、危害：通过水平访问控制，不同的用户可以访问同一类型的资源子集。例如，银行应用程序将允许用户查看交易并从自己的帐户进行支付，但不允许任何其他用户的帐户。 <br/>  
<hr/>
<h3>5、上下文相关的访问控制</h3>
1、原理：上下文相关的访问控制根据应用程序的状态或用户与应用程序的交互来限制对功能和资源的访问。
————
2、危害：上下文相关的访问控制可防止用户以错误的顺序执行操作。如零售网站可能会阻止用户在付款后修改其购物车的内容。 


### 2、危害

---


---


### 4、水平访问控制

---


---


## 二、破坏访问控制的示例

> 
<h3>1、纵向权限提升</h3>
如果用户可以访问不允许其访问的功能，则这是垂直权限提升。如一个非管理员用户实际上可以访问一个管理页面，在那里他们可以删除用户帐户，那么这就是垂直权限提升
<hr/>
<h3>2、不受保护的功能</h3>
1、最基本的情况是，当应用程序不对敏感功能实施任何保护时，会出现垂直权限提升。如管理功能可能从管理员的欢迎页面链接，而不是从用户的欢迎页面链接。然而用户可能仅仅能够通过直接浏览到相关的管理URL来访问管理功能<br/>  
<hr/>
2、示例：
如某个网站可能在以下URL上托管敏感功能：
<pre>`https://insecure-website.com/admin`</pre>
事实上，任何用户都可以访问该功能，而不仅仅是在其用户界面中具有指向该功能的链接的管理用户。在某些情况下，管理URL可能会在其他位置公开，如robots.txt文件：
<pre>`https://insecure-website.com/robots.txt`</pre>
即使URL没有在任何地方公开，攻击者也可以使用单词列表强行找到敏感功能的位置
<hr/>
涉及实验：
实验1：不受保护的管理功能
<hr/>
3、隐藏的接口
在某些情况下，敏感功能没有得到可靠的保护，而是通过提供一个不可预测的URL来隐藏：所谓的模糊安全。仅仅隐藏敏感功能并不能提供有效的访问控制，因为用户仍然可能以各种方式发现模糊的URL。
如在以下URL承载管理功能的应用程序：
<pre>`https://insecure-website.com/administrator-panel-yb556`</pre>
这可能无法被攻击者直接猜到。但应用程序仍可能将URL泄漏给用户。如URL可能在JavaScript中公开，JavaScript基于用户的角色构造用户界面：<br/>  
<pre><code>&lt;script&gt;
var isAdmin = false;
if (isAdmin) {
	...
	var adminPanelTag = document.createElement('a');
	adminPanelTag.setAttribute('https://insecure-website.com/administrator-panel-yb556');
	adminPanelTag.innerText = 'Admin panel';
	...
}
&lt;/script&gt;</code></pre>
如果用户是管理员用户，此脚本将向用户的UI添加链接。但包含URL的脚本对所有用户都可见，而不管其角色如何。 
<hr/>
涉及实验：
实验2：不受保护的管理功能，URL不可预测


### 2、不受保护的功能

---


---


> 
<h3>实验1：不受保护的管理功能</h3>
信息：
本实验有一个未受保护的管理面板。
通过删除用户carlos解决实验
<hr/>
part1：
将/robots. txt加到URL后查看robots.txt文件
Disallow行显示了管理面板的路径


<hr/>
part2:
在主URL后加上/administrator-panel以加载管理面板


删除carlos完成实验




---


> 
<h3>实验2：不受保护的管理功能，URL不可预测</h3>
信息：
本实验有一个未受保护的管理面板。它位于一个不可预测的位置，但该位置在应用程序中的某个地方公开。
通过访问管理面板并使用它删除用户carlos来解决实验
<hr/>
part1：
使用Burp Suite或Web浏览器的开发工具查看实验主页的源代码。
(Ctrl+U查看源码)注意到它包含一些JavaScript，公开了管理面板的URL
会有一个是否是admin的检测
检测成功则跳转



<hr/>
part2:
加载管理面板并删除carlos

 <img alt="" height="667" src="https://img-blog.csdnimg.cn/f8d3f6e6adce4cfaadda07f893d0558b.png" width="1200"/>



---


> 
<h3>3、基于参数的访问控制方法</h3>
1、某些应用程序在登录时确定用户的访问权限或角色，然后将此信息存储在用户可控制的位置，如隐藏字段、cookie或预设查询字符串参数。应用程序根据提交的值做出后续访问控制决策
<pre><code>例如：
https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1</code></pre>
这种方法从根本上讲是不安全的，因为用户可以简单地修改值并获得对他们未被授权的功能（如管理功能）的访问权限<br/>  
<hr/>
2、涉及实验：
实验3：由请求参数控制的用户角色
实验4：可以在用户配置文件中修改用户角色


> 
<h3>实验3：由请求参数控制的用户角色</h3>
信息：
本实验在/admin下有一个管理面板，用于识别使用可伪造Cookie的管理员。
通过访问管理面板并使用它删除用户carlos来解决实验
已有账号：wiener:peter
<hr/>
part1:
浏览到/admin，发现您无法访问管理面板




<hr/>
part2:
在Burp代理监听（完整的登陆流程中，在HTTP历史记录中可以发现有一个admin身份的验证）


使用BP拦截并将cookie Admin=false改为Admin=true
（第二个跳转到/my-account的数据包）
<img alt="" height="992" src="https://img-blog.csdnimg.cn/8a30a791f9d343ca90b0434a6d2cda4c.png" width="1200"/><br/> 改为true后关闭拦截，完成并提交登录页面
每次点击的时候都拦截请求

每一步都要修改为true

<hr/>
part3:
完成实验 
点击删除，然后再改为true

 <img alt="" height="638" src="https://img-blog.csdnimg.cn/c59f65ca989d43da8a34067c4bf2fadf.png" width="1200"/>



---


> 
<h3>实验4：可以在用户配置文件中修改用户角色</h3>
信息：
本实验在/admin下有一个管理面板。只有角色标识为2的登录用户才能访问。
通过访问管理面板并使用它删除用户carlos来解决实验
已有账号：wiener:peter
<hr/>
part1:
使用提供的凭据登录并访问您的帐户页面<br/> 使用提供的功能更新与帐户关联的电子邮件地址(有一个更新接口，尝试更新其他内容)
<img alt="" height="875" src="https://img-blog.csdnimg.cn/7b1b49f559e64f2897ea5ca8de98fcd2.png" width="1200"/><br/> 更新邮箱，并查看数据包

查看返回的数据包发现我们只修改了这么多参数中的其一

<hr/>
part2：
将电子邮件提交请求发送到repeater重发


增加参数将”roleid“:2添加到请求正文的JSON中，响应中已变为2


<hr/>
part3：
完成实验<br/> 浏览到/admin并删除carlos
 <img alt="" height="593" src="https://img-blog.csdnimg.cn/a47d0cdbb61746a8b362dbb4f1e6dc30.png" width="1200"/>



---


> 
<h3>4、平台配置错误导致访问控制中断</h3>
1、一些应用程序通过基于用户角色限制对特定URL和HTTP方法的访问，在平台层强制执行访问控制。
<pre><code>如应用程序可能配置如下规则：
DENY: POST, /admin/deleteUser, managers

</code></pre>
规则拒绝访问后URL上的方法/admin/deleteUser，适用于管理员组中的用户（在这种情况下，各种事情都可能出错，导致访问控制绕过）
<hr/>
2、一些应用程序框架支持各种非标准HTTP头，这些头可用于覆盖原始请求中的URL
<pre>`如X-Original-URL和X-Rewrite-URL`</pre>
如果网站使用严格的前端控制来限制基于URL的访问，但应用程序允许通过请求标头覆盖URL，则可能使用如下请求绕过访问控制：
<pre><code>POST / HTTP/1.1
X-Original-URL: /admin/deleteUser
...</code></pre>
<hr/>
3、另一种攻击可能与请求中使用的HTTP方法有关。上述前端控件根据URL和HTTP方法限制访问。某些网站在执行操作时允许使用其他HTTP请求方法。如果攻击者可以使用GET（或其他）方法对受限URL执行操作，那么他们就可以绕过在平台层实现的访问控制。 
<hr/>
4、涉及实验：
实验10：可以绕过基于URL的访问控制<br/> 实验11：可以绕过基于方法的访问控制



---


> 
<h3>实验10：可以绕过基于URL的访问控制</h3>
信息：
此网站在/admin处有一个未经身份验证的管理面板，但前端系统已配置为阻止对该路径的外部访问。但后端应用程序构建在支持X-Original-URL标头的框架上。
要解决实验问题，访问管理面板并删除用户carlos
已有账号：wiener:peter
<hr/>
part1:
尝试加载/admin并观察是否被阻止
（响应非常简单，表明可能来自前端系统）


<hr/>
part2:
发送请求到repeater
将请求行中的URL更改为/并添加HTTP标头X-Original-URL:/invalid
注意到应用程序返回“未找到”响应(表明后端系统正在处理来自X-Original-URL头的URL)

<br/><br/> 将X-Original-URL标头的值更改为/admin，并放包<img alt="" height="531" src="https://img-blog.csdnimg.cn/6db79c9238644d9a893b8e3184772ad1.png" width="850"/>
然后退回主页，现在可以访问管理页面了


<hr/>
part3：<br/> 要删除用户卡洛斯(可能要等很久)
添加?username=carlos设置为真实的的查询字符串，并将X-Original-URL路径更改为/admin/delete
<pre><code>?username=carlos
X-Original-URL:/admin/delete
</code></pre>
（抓一个包修改，或者重发后刷新）


 实验完成<img alt="" height="964" src="https://img-blog.csdnimg.cn/f0a1f0df07154e3bbfa41e33f981bcf6.png" width="1200"/>



---


> 
<h3>实验11：可以绕过基于方法的访问控制</h3>
信息：
本实验部分基于HTTP请求方法实现访问控制，可以通过使用凭据administrator：admin登录来熟悉管理面板（利用有缺陷的访问控制将自己提升为管理员）
已有账号：wiener/peter
<hr/>
part1:
使用管理员凭据登录（administrator：admin）


<br/> 浏览到管理面板，提升carlos，然后将HTTP请求发送到Burp Repeater



<hr/>
part2：<br/> 打开一个私有/匿名浏览器窗口，然后使用非管理员凭据登录（wiener/peter）
<img alt="" height="1021" src="https://img-blog.csdnimg.cn/31c4a1d913a4402998a3a2c033073430.png" width="1200"/><br/> 尝试通过将非管理员用户的会话cookie复制到现有的BurpRepeater请求中来重新提升卡洛斯，并观察到响应显示为“Unauthorized”（未经授权）
<img alt="" height="991" src="https://img-blog.csdnimg.cn/a9aa960dea9f4fb4992ac4d1d75025db.png" width="1200"/><br/> 将方法从POST更改为POSTX，并观察响应更改为“missing parameter”（缺少参数）
<img alt="" height="991" src="https://img-blog.csdnimg.cn/4fb0d1bbd79149638892008530bd676a.png" width="1200"/><br/> 通过右键单击并选择“更改请求方法”，将请求转换为使用GET方法




<hr/>
part3：
将username参数更改为我们的用户名并重新发送请求（wiener）
 <img alt="" height="991" src="https://img-blog.csdnimg.cn/019ae8fd5704482fa3bdb9e32c0f0836.png" width="1200"/>

 （如果没完成实验，就刷新一下页面）<img alt="" height="458" src="https://img-blog.csdnimg.cn/fc800326bc4e43b797220ab9e141f4a0.png" width="1200"/>



---


> 
<h3>5、横向权限提升</h3>
1、原理：当用户能够访问属于另一个用户的资源而不是他们自己的资源时，就会出现横向权限提升。如一个员工应该只能访问自己的雇佣和工资单记录，但实际上也可以访问其他员工的记录，那么这就是横向权限提升。
<hr/>
2、水平权限提升攻击可能使用与垂直权限提升类似的利用方法。
<pre><code>如用户通常可以使用如下URL访问自己的帐户页面：
https://insecure-website.com/myaccount?id=123
（如果攻击者将id参数值修改为另一个用户的值，那么攻击者就可能获得对另一个用户的帐户页面以及相关数据和函数的访问权限）</code></pre>
涉及实验：
实验5：由请求参数控制的用户ID 
<hr/>
3、在某些应用程序中，可利用参数不具有可预测的值。如应用程序可以使用全局唯一标识符（GUID）来标识用户，而不是使用递增的数字。在这里，攻击者可能无法猜测或预测其他用户的标识符。但属于其他用户的GUID可能会在引用用户的应用程序中的其他地方公开，例如用户消息或评论
————
涉及实验：
实验6：用户ID由请求参数控制，用户ID不可预测 
<hr/>
4、在某些情况下，应用程序会检测到用户何时不被允许访问资源，并返回到登录页的重定向。但包含重定向的响应仍可能包含属于目标用户的某些敏感数据，因此攻击仍会成功。 
————
涉及实验：
实验7：用户ID由请求参数控制，重定向时发生数据泄漏 



---


> 
<h3>实验5：由请求参数控制的用户ID</h3>
信息：
本实验的用户帐户页面上存在一个横向权限提升漏洞。
要解决实验问题，获取用户carlos的API密钥并将其作为解决方案提交<br/> 已有账号：wiener:peter
<hr/>
part1:
使用已有账号登陆

分析HTTP历史记录中数据包，无特殊参数
再次点击My account

 分析数据包，URL在“id”参数中包含用户名

<hr/>
part2：
发送请求到repeater，将“id”参数更改为carlos<br/> 检索并提交卡洛斯的API密钥
 <img alt="" height="927" src="https://img-blog.csdnimg.cn/a77b804180d14eebb22f7f813a863521.png" width="1200"/>
 <img alt="" height="787" src="https://img-blog.csdnimg.cn/d5cf25994e3a411ba106a0db0774970f.png" width="1200"/>



---


> 
<h3>实验6：用户ID由请求参数控制，用户ID不可预测 </h3>
信息：
这个实验室在用户账户页面上有一个水平的权限提升漏洞，但是用 GUID 来识别用户
已有账号：wiener:peter
<hr/>
part1：
找一篇 Carlos 的博文。

单击 Carlos 并观察 URL 包含他的用户 ID。记下这个 ID。
 <img alt="" height="819" src="https://img-blog.csdnimg.cn/eb4f646654b9461f8438fe32e095c1e3.png" width="1200"/>

<hr/>
part2:
使用已有账号登录并访问
wiener:peter

登陆后再次点击My account，分析数据包


<hr/>
part3：
完成实验
将“ ID”参数更改为保存的用户 ID。检索并提交 API 密钥。

<img alt="" height="927" src="https://img-blog.csdnimg.cn/49e77609598e43608b35f595b4492876.png" width="1200"/>如果卡住，就刷新一下页面<img alt="" height="811" src="https://img-blog.csdnimg.cn/824e9fc0fd7947269fd1c582a445ffe0.png" width="1200"/>
 <img alt="" height="542" src="https://img-blog.csdnimg.cn/2834c753845541ea8c5fc764c8cc6ba0.png" width="1200"/>



---


> 
<h3>实验7：用户ID由请求参数控制，重定向时发生数据泄漏 </h3>
该实验室包含一个访问控制漏洞，其中敏感信息在重定向响应的主体中泄露。
要解决该实验室的问题，获取用户 Carlos 的 API 密钥，并将其作为解决方案提交。
已有账号：wiener:peter
<hr/>
part1:
使用提供的凭据登录并访问您的帐户页面。

再次点击My account，分析数据包
发现通过参数名传参的参数

<hr/>
part2:
发送到bp的repeater
将“ id”参数更改为 Carlos
（虽然响应现在将重定向到主页，但是它有一个主体，其中包含属于 Carlos 的 API 密钥）


提交 API 密钥




---


> 
<h3>6、横向到纵向权限提升</h3>
1、危害：一般水平权限提升攻击可以通过危害更高权限的用户而转变为垂直权限提升。如横向升级可能允许攻击者重置或捕获属于其他用户的密码。如果攻击者以管理用户为目标并危害其帐户，则他们可以获得管理访问权限，从而执行垂直权限提升。
如攻击者可能能够使用已经描述的横向权限提升的参数篡改技术获得对另一个用户帐户页的访问权限：
<pre>`https://insecure-website.com/myaccount?id=456`</pre>
如果目标用户是应用程序管理员，则攻击者将获得对管理帐户页的访问权限。此页可能会泄漏管理员密码或提供更改密码的方法，或者可能提供对特权功能的直接访问。
<hr/>
2、涉及实验：
实验8：用户ID由密码泄露的请求参数控制



> 
<h3>实验8：用户ID由密码泄露的请求参数控制</h3>
信息：
这个实验室有一个用户账户页面，其中包含当前用户的现有密码，预先填写了一个掩码输入
要解决这个实验室，检索管理员的密码，然后用它来删除 Carlos。
已有账号：wiener:peter
<hr/>
part1：
使用提供的凭据登录并访问用户帐户页面。

发现页面会包含自己密码，再次点击My account，分析数据包
发现通过参数名传参的参数


<hr/>
part2：
发送到repeater
将 URL 中的“ id”参数更改为管理员，并找到管理员密码


<hr/>
part3：
登陆管理员账户，删除 Carlos
<pre>`iq8szu44yky140pdvu4b`</pre>

 <img alt="" height="684" src="https://img-blog.csdnimg.cn/28c459f33b8b4c57af768c6b24869dcd.png" width="1200"/>



---


> 
<h3>7、不安全的直接对象引用</h3>
1、不安全直接对象引用（IDOR）是访问控制漏洞的一个子类。当应用程序使用用户提供的输入直接访问对象，并且攻击者可以修改输入以获得未经授权的访问时，就会出现IDOR。它因出现在OWASP 2007 Top Ten中而流行，尽管它只是许多可能导致绕过访问控制的实现错误中的一个例子
<hr/>
2、涉及实验：<br/> 实验9：不安全的直接对象引用


> 
<h3>实验9：不安全的直接对象引用</h3>
信息：
这个实验室将用户聊天记录直接存储在服务器的文件系统中，并使用静态 URL 检索它们。
找到用户 Carlos 的密码，登陆他们的账户，解决实验室
<hr/>
part1：
选择 Live chat 选项卡。发送一条消息，然后选择 View transcript。

<img alt="" height="253" src="https://img-blog.csdnimg.cn/9d4c3e3bacdb46c4828d825b90f04fb0.png" width="798"/> 再次点击


分析HTTP历史记录
检查 URL 并观察到文本是分配给文件名的文本文件，其中包含一个递增的数字。

<hr/>
 part2:
将文件名更改为1.txt 并查看文本
注意聊天记录中的密码。


<hr/>
part3:
返回到主实验室页面，并使用被盗凭证登录。
<pre><code>carlos
jsj56afvshbm5ozfl4qg</code></pre>

 <img alt="" height="782" src="https://img-blog.csdnimg.cn/2cd33edb39df449aa9f836f6c5f66a36.png" width="1200"/>



---


> 
<h3>8、多步骤流程中的访问控制漏洞</h3>
1、许多网站通过一系列步骤实现重要功能。当需要捕获各种输入或选项时，或者当用户需要在执行操作之前查看和确认细节时，通常会执行此操作。
<pre><code>如更新用户详细信息的管理功能可能涉及以下步骤：
1、加载包含特定用户详细信息的表单。
2、提交更改
3、查看更改并确认。 </code></pre>
<hr/>
2、有时网站会对其中一些步骤实施严格的访问控制，但忽略其他步骤。如假设访问控制已正确应用于第一步和第二步，但未应用于第三步。实际上，网站假设用户只有在他们已经完成了被适当控制的第一步骤的情况下才将到达步骤3。在这里，攻击者可以跳过前两个步骤，直接提交包含所需参数的第三个步骤的请求，从而获得对函数的未授权访问。<br/>  
<hr/>
3、涉及实验：
实验10：多步骤流程，其中一个步骤没有访问控制 


---


> 
<h3>实验10：多步骤流程，其中一个步骤没有访问控制 </h3>
信息：
这个实验室有一个管理面板，它有一个有缺陷的改变用户角色的多步骤过程（可以通过使用凭据administrator: admin 登录来熟悉管理面板）
要解决实验室问题，使用凭据 wiener: peter 登录，并利用存在缺陷的访问控制来提升自己成为管理员
<hr/>
part：
使用管理凭据登录


浏览到管理面板，提升carlos，并将确认 HTTP 请求发送到bp的repeater
流程一：

流程二：

<hr/>

part2: 
打开一个私有/匿名浏览器窗口，并使用非管理员凭证登录。

 获取非管理员cookie


<hr/>
part3:
将非管理员用户的会话 cookie 复制到现有的转发请求中，将用户名更改为已有的用户名，然后重放
流程一：（会有鉴权）
提示未经授权


流程二：（提权成功）
302跳转和原始数据一致

 <img alt="" height="806" src="https://img-blog.csdnimg.cn/b434df9f26a14f64af672944f0b2f451.png" width="1200"/>



---


> 
<h3>9、基于引用的访问控制</h3>
1、原理：某些网站基于访问控制Referer HTTP请求中提交的标头。该Referer浏览器通常会在请求中添加一个标头，以指示发起请求的页面。
<hr/>
2、示例：如假设某个应用程序在主管理页上强制实施访问控制/admin，但对于子页面，如/admin/deleteUser用户只检查了Referer标题。如果Referer标头包含主/admin URL，则允许该请求。
<hr/>
3、利用：在这种情况下，由于Referer头可以完全由攻击者控制，他们可以伪造对敏感子页的直接请求，提供所需的Referer头，从而获得未经授权的访问
<hr/>
4、涉及实验：
实验11：基于引用的访问控制 


---


> 
<h3>实验11：基于引用的访问控制 </h3>
信息：
这个实验根据 Referer 头控制对某些管理功能的访问（可以通过使用凭据administrator: admin 登录来熟悉管理面板）
要解决实验室问题，使用凭据 wiener: peter 登录，并利用存在缺陷的访问控制来提升自己成为管理员
<hr/>
part1:
使用管理凭据登录


浏览到管理面板，提升 Carlos


然后将 HTTP 请求发送到BP的repeater

<hr/>
part2: 
打开一个私有/匿名浏览器窗口，并使用非管理员凭证登录
wiener: peter


在/admin-role?Username = carlos &amp; action = update请求中，如果缺少 Referer 头，请求被视为未授权

将非管理员用户的会话 cookie 复制到现有的 Burp Repeater 请求中，将用户名更改为已有的，然后重放

 和原有数据一样进行了跳转<img alt="" height="927" src="https://img-blog.csdnimg.cn/0b7f75cb980349029b37cd73387e0d33.png" width="1200"/>



---


> 
<h3>10、基于位置的访问控制</h3>
1、一些网站基于用户的地理位置对资源实施访问控制。如这可以应用于州立法或业务限制适用的银行应用或媒体服务。这些访问控制通常可以通过使用Web代理、VPN或操纵客户端地理定位机制来规避。 


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

