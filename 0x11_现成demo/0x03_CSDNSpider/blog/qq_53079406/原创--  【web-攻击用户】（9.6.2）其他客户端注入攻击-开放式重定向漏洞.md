# 原创
：  【web-攻击用户】（9.6.2）其他客户端注入攻击：开放式重定向漏洞

# 【web-攻击用户】（9.6.2）其他客户端注入攻击：开放式重定向漏洞

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
（1）查找并利用开放式重定向（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[开放式重定向漏洞](#%E5%BC%80%E6%94%BE%E5%BC%8F%E9%87%8D%E5%AE%9A%E5%90%91%E6%BC%8F%E6%B4%9E)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、查找并利用开放式重定向漏洞](#1.2%E3%80%81%E6%9F%A5%E6%89%BE%E5%B9%B6%E5%88%A9%E7%94%A8%E5%BC%80%E6%94%BE%E5%BC%8F%E9%87%8D%E5%AE%9A%E5%90%91%E6%BC%8F%E6%B4%9E)

[1.3、过程1：](#1.3%E3%80%81%E8%BF%87%E7%A8%8B1%EF%BC%9A)

[1.4、过程2：](#1.4%E3%80%81%E8%BF%87%E7%A8%8B2%EF%BC%9A)

[1.5、利用：](#1.5%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[阻止绝对URL](#%E9%98%BB%E6%AD%A2%E7%BB%9D%E5%AF%B9URL)

[附加绝对前缀](#%E9%99%84%E5%8A%A0%E7%BB%9D%E5%AF%B9%E5%89%8D%E7%BC%80)

[防止开放式重定向漏洞](#%E9%98%B2%E6%AD%A2%E5%BC%80%E6%94%BE%E5%BC%8F%E9%87%8D%E5%AE%9A%E5%90%91%E6%BC%8F%E6%B4%9E)

---


## 开放式重定向漏洞

> 
<h3>1.1、简介：</h3>
1、如果应用程序提取用户可控制的输入并使用这个数据执行重定向，指示用户的浏览器访问不同于用户所请求的URL，这时就会导致开放重定向油洞。相比于可执行大量恶意操作的跨站点脚本漏洞，攻击者通常对这些漏洞不太感兴趣，攻击者主要利用开放式重定向漏洞实施钓鱼攻击，诱使受害者访问欺骗性Web站点并输入敏感信息，对潜在的受害者而言，重定向漏洞提点了攻击者的可信度因为它允许攻击者创建一个指向他所针对的可信Web站点的URL，因此更具有说服力，但任何访问这个URL的用户将被悄悄重定向到攻击者控制的Web站点。
<hr/>
2、现实世界中的大多数钓鱼攻击都使用其他技巧来获得不受所针对的应用程序控制的可信度。这类技巧包括注册类似的域名、使用官方形式的子域，以及在HTML电子邮件中在定位文本与链接的目标URL之间造成不匹配。研究表明，多数用户都无法或不太可能基于URL结构作出安全决策。因此典型的开放式项定向漏洞对钓鱼攻击者而言并无多大价值
<hr/>
3、开放式重定向漏洞一直被攻击者以相对良性的方式加以利用，用于实施“瑞克摇摆"攻击。在这种攻击中，受害者在不知情的情况下被重定向到视频中


---


> 
<h3>1.2、查找并利用开放式重定向漏洞</h3>
查找重定向漏洞的第一步是确定应用程序中的所有重定向，应用程序可以通过几种方式使用户的浏览器重定向到不同的URL
<hr/>
1、HTTP重定向使用一条状态码为3xx的消息与一个指定重定向目标的Location消息头
————
2、HTTPRefresh消息头可在固定时间间隔后使用任意URL重新加载某个页面，该间隔可以为零，也就是能立即触发重定向
————
3、HTML&lt;meta&gt;标签可复制任何HTTP消息头的行为，因此可用于建立重定向
————
4、JavaScript中的各种API可用于将浏览器重定向到任意URL


> 
<h3>1.3、过程1：</h3>
1、确定应用程序中使用重定向的所有位置。
————
2、要确定所有重定向，一个有效的方法是使用拦截代理服务器浏览应用程序，并监控访问页面请求（与其他资源，如图像、样式表、脚本文件等不同）
————
3、如果一个导航操作导致了几个连续请求，应分析它使用什么方法进行重定向。
<hr/>
绝大多数的重定向都不受用户控制，如在典型的登录机制中，向/login.jsp提交有效的证书将返回一个指向/myhome.jsp的HTTP重定向，这时重定向的目标始终相同，因此不会受到任何重定向漏洞的影响。
但在有些情况下，用户提交的数据以某种方式用于设置重定向的目标。一个常见的例子是应用程序强制使会话已经终止的用户返回登录页面，然后在用户重新成功通过验证后将他们重定向到最初的URL。如果遇到这种行为，就表明应用程序可能易于受到重定向攻击，因此应当对这种行为进行深入分析，以确定它是否可被攻击者利用。


> 
<h3>1.4、过程2：</h3>
1、如果用户数据在包含绝对URL的重定向中进行处理，则应修改URL中的域名，并测试应用程序是否将用户重定向到另一个域。
<hr/>
2、如果所处理的用户数据包含相对URL，应将此URL修改为指向另一个域的绝对URL，并测试应用程序是否将用户重定向到这个域
<hr/>
3、无论是哪一种情况， 如果有以下行为，那么应用程序肯定容易受到重定向攻击：
GET /updates/8/?redir=http://xxx.com/ HTTP/1.1
Host:
HTTP/1.1 302 Object moved
Loation:http://xxx.com


---


> 
<h3>1.5、利用：</h3>
1、如果应用程序使用可由用户控制的数据指定框架的目标URL，这时会发生一种与重定向并非完全相同但相似现象，如果可以构建一个URL，将外部URL的内容加载到子框架中，就可以相当隐秘地实施重定向攻击。这时可以使用其他内容仅替换应用程序的部分界面，并使浏览器地址栏中的域保持不变
————
2、以下情况很常见：用户控制的数据用于设置重定向的目标，但却被应用程序以某种方式过滤或净化掉， 以阻止重定向攻击，这时并没有办法确定应用程序是否易于受到攻击； 因此，接下来应该探查应用程序采用的防御机制，确定是否能够避开它们以执行任意重定向。通常会遇到以下两种防御尝试阻止绝对URL、附加一个特殊的绝对URL前缀
<hr/>
<h4>阻止绝对URL</h4>
1、应用程序可能会检查用户提交的字符串是否以http://开头，如果是就阻止该请求，这时使用下面的技巧可以成功创建一个指向外部Web站点的重定向（第三行开头有空格）
HtTp://xx.com
%00http://xx.com
 http://xx.com
//xx.com
%68%74%74%70%3a%2f%2fxx.com
%2568%2S74%2574%2570%253a%252f%252fxxx.com
https://xx.com
http:\\xx.ccom
http:///xx.com
————
2、应用程序可能会删除http及任何指定的外部域，尝试净化绝对URL。这时使用上面的技巧可以成功进开净化；同时还应测试下面的攻击是否可行
http://http://xx.com
http://xx.com/http://xx.com
hthttp://tp://xx.com
————
3、有时应用程序可能会检验用户提交的字符串是否以指向它自己的域名的绝对URL开头，或是否包含这个URL。这时下面的攻击可能有效：
http://mdsec.net.xx.net
http://xx.net/?http://mdsec.net
http://xx.net/%23http://mdsec.net
<hr/>
<h4>附加绝对前缀</h4>
1、应用程序可能会在用户提交的字符串前附加一个绝对URL前缀，从而建立重定向的目标
2、这时无法确定应用程序是否易于受到攻击，如果所使用的前缀由http://与应用程序的域名组成， 但在域名后没有斜线字符，那么它就易于受到攻击(如http://xx.net/updates/24/?redir=xx.com)
会重定向到http://xx.net.xx.com
它由攻击者控制，前提是攻击者控制着域xx.com的DNS记录。
————

3、如果绝对URL前缀确实包含斜线字符(/)或服务器上的某个子目录，那么应用程序可能不会受到针对外部域的顶定向攻击。这时攻击者最多只能构建一个URL,将用户煎定向到同一应用程序中的另一个URL。通常这种攻击并不能取得任何成果，因为如果攻击者能够诱使用户访问应用程序中的一个URL，那么他大概也只能向他们直接传送另一个URL
————

4、如果使用从DOM中查询数据的客户端JavaScript实现重定向，则负责执行重定向与相关确认的所有代码通常将在客户端上可见。因此应仔细检查这些代码，确定它如何将用户控制的数据合并到URL中，以及它是否执行了任何确认，是否有什么办法可以避开确认。注意，和基于DOM的XSS漏洞一样，在将脚本返回浏览器之前，服务器可能对其执行了其他确认。
JavaScnptAPI可用于执行重定向：
<pre><code>document.location
document.URL
document.open()
window.location.href
window.navigate()
window.open()</code></pre>
<hr/>
<h4>防止开放式重定向漏洞</h4>
绝不将用户提交的数据合并到重定向目标中，是避免开放式重定向漏洞的最有效方法。开发者这样做出于各种原因，但通常我们都可以找到替代办法。例如，用户界面中常常包含一组链接，每个链接指向一个重定向页面，并以目标URL为参数。这时可能的替代方法如下
————
1、从应用程序中删除重定向页面，用直接指向相关目标URL的链接替代指向重定向页面的链接
2、建立一个包含所有有效重定向URL的列表，不以参数的形式向重定向页面传送目标URL，而是传送这个列表的索引。重定向页面应在它的列表中查询这个索引，并返回一个指向相关URL的重定向
<hr/>
如果重定向页面不可避免地要收到用户提交的输入并将它合并到重定向目标中，应使用以下措施降低重定向攻击的风险
————
1、应用程序应在所有重定向中使用相对URL，重定向页面应严格确认它收到的URL为相对URL 。它应当确保用户提交的URL或者以其后接一个字母的斜线字符开头，或者以一个字母开头，并且在第一个斜线前没有冒号。应拒绝，而不是净化任何其他输入。
2、应用程序应该在所有重定向中使用相对于Web根目录的URL ，在发布重定向之前，重定向页面应在所有用户提交的URL前附加http//youdomainname.com。如果用户提交的URL并不以斜线字符开头， 应在它的前面附加http//youdomainname.com/
3、应用程序应对所有重定向使用绝对URL，重定向页面在发布重定向之前，应确认用户提交的URL以http//youdomainname.com/开头。此外应拒绝任何其他输入
————
和基于DOM的XSS漏洞一样，建议应用程序不要根据DOM数据通过客户端脚本执行重定向，因为这些数据不在服务器的立接控制范围内


---


#### 附加绝对前缀

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
|看雪众测（物联网）|[https://ce.kanxue.com/](https://ce.kanxue.com/)
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

