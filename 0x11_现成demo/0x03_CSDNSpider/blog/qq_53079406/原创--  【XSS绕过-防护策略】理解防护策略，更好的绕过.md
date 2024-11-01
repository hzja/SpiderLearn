# 原创
：  【XSS绕过-防护策略】理解防护策略，更好的绕过

# 【XSS绕过-防护策略】理解防护策略，更好的绕过

**目录**

[一、简述](#%E4%B8%80%E3%80%81%E7%AE%80%E8%BF%B0)

[二、特定标签过滤](#%E4%BA%8C%E3%80%81%E7%89%B9%E5%AE%9A%E6%A0%87%E7%AD%BE%E8%BF%87%E6%BB%A4)

[2.1、缺点：](#2.1%E3%80%81%E7%BC%BA%E7%82%B9%EF%BC%9A)

[2.2、现状：](#2.2%E3%80%81%E7%8E%B0%E7%8A%B6%EF%BC%9A)

[2.3、利用：](#2.3%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[三、事件过滤](#%E4%B8%89%E3%80%81%E4%BA%8B%E4%BB%B6%E8%BF%87%E6%BB%A4)

[3.1、简介：](#3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.2、常用的事件属性：](#3.2%E3%80%81%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BA%8B%E4%BB%B6%E5%B1%9E%E6%80%A7%EF%BC%9A)

[3.3、非事件属性的标签](#3.3%E3%80%81%E9%9D%9E%E4%BA%8B%E4%BB%B6%E5%B1%9E%E6%80%A7%E7%9A%84%E6%A0%87%E7%AD%BE)

[四、敏感关键字（字符）过滤](#%E5%9B%9B%E3%80%81%E6%95%8F%E6%84%9F%E5%85%B3%E9%94%AE%E5%AD%97%EF%BC%88%E5%AD%97%E7%AC%A6%EF%BC%89%E8%BF%87%E6%BB%A4)

[五、XSS Auditor](#%E4%BA%94%E3%80%81XSS%20Auditor)

[5.1、概述：](#5.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[六、内容安全策略（CSP）](#%E5%85%AD%E3%80%81%E5%86%85%E5%AE%B9%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5%EF%BC%88CSP%EF%BC%89)

[6.1、概述：](#6.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[七、推荐](#%E4%B8%83%E3%80%81%E6%8E%A8%E8%8D%90)

---


## 一、简述

> 
现在Web应用层有很多策略去处理XSS危害
eg：
特定标签过滤、事件过滤、敏感关键字过滤……
浏览器也会对XSS漏洞的利用进行限制（XSS Auditor、CSP等）


---


---


## 二、特定标签过滤

> 
<h3>2.1、缺点：</h3>
过滤掉危险标签（如script、iframe等）就会导致无法执行脚本
<hr/>
<h3>2.2、现状：</h3>
任何一种标签，无论是否合法，都可以构造出XSS代码
&lt;标签 οnclick="alert(/xss/)"&gt;快点我呀&lt;/标签&gt;
<hr/>
<h3>2.3、利用：</h3>
属性值：输出点在HTML标签的属性中或在Javascript代码中，简单地闭合、拼接属性或Javascript代码就可以执行XSS代码
HTML：&lt;video&gt;&lt;source οnerrοr="alert(/xss/)"&gt;


### 2.2、现状：

---


---


---


## 三、事件过滤

> 
<h3>3.1、简介：</h3>
一般会过滤掉许多HTML标签的事件属性，需要对所有可利用的事件属性进行遍历，测试是否存在遗漏（测试：Burp或编写脚本进行Fuzz）
<hr/>
<h3>3.2、常用的事件属性：</h3>
onafterprint、oninput、onscroll、onbeforeprint 、oninvalid 、onabort、onbeforeunload 、onreset 、oncanplay、onerror、 onselect 、oncanplaythrough、onhaschange、 onsubmit、 ondurationchange、onload 、onkeydown 、onemptied、onmessage 、onkeypress、 onended、onoffline、 onkeyup、 onerror、ononline 、onclick、 onloadeddata、onpagehide、 ondblclick、 onloadedmetadata、onpageshow 、ondrag、 onloadstart、onpopstate、 ondragend、 onpause、onredo、 ondragenter、 onplay、onresize 、ondragleave 、onplaying、onstorage 、ondragover 、onprogress、onundo、 ondragstart 、onratechange、onunload、 ondrop、 onreadystatechange、onblur 、onmousedown、 onseeked、onchange 、onmousemove 、onseeking、oncontextmenu 、onmouseout、 onstalled、onfocus、 onmouseover 、onsuspend、onformchange 、onmouseup 、ontimeupdate、onforminput、onmousewheel、 onvolumechange
<hr/>
<h3>3.3、非事件属性的标签</h3>
作用：可用于执行JavaScript代码
eg：JavaScript伪协议
&lt;a href="javascript:alert(/xss/)"&gt;快点我呀&lt;/a&gt;


### 3.2、常用的事件属性：

---


---


---


## 四、敏感关键字（字符）过滤

> 
（1）过滤“.”
（2）过滤“()”
（3）过滤空格
……


---


---


## 五、XSS Auditor

> 
<h3>5.1、概述：</h3>
负责扫描网站的源代码，寻找类似跨站点脚本（XSS）攻击的模式，这种攻击可能试图在用户的浏览器中运行恶意代码 。通过检查输入的内容，判断该内容是否在输出中出现。如果符合XSS Auditor的过滤条件，则会直接阻止脚本执行。使反射型XSS漏洞的作用被逐步弱化。


---


---


## 六、内容安全策略（CSP）

> 
<h3>6.1、概述：</h3>
内容安全策略（CSP）是目前最主要的Web安全保护机制之一，内容安全策略 (CSP) 是一个额外的安全层，用于检测并削弱某些特定类型的攻击，包括跨站脚本 (XSS) 和数据注入攻击等。
<hr/>
为了缓解潜在的跨站脚本问题，浏览器的扩展程序系统引入了内容安全策略（CSP），会使扩展程序在默认情况下更加安全，开发者可以创建并强制应用一些规则，管理网站允许加载的内容。开发人员可以使用这种工具以各种方式锁定其应用程序，降低内容注入漏洞（如跨站点脚本）的风险，并降低其应用程序执行的权限
<hr/>
内容安全策略以白名单的机制来管理网站要加载或执行的资源。在网页中，这样的策略是通过HTTP头信息或者meta标签来定义的。
<hr/>
虽然这个策略可以防止攻击者从外部网站跨域加载恶意代码，但是CSP并不能防止数据泄露。目前已经有很多安全研究人员提出了各种各样的技术来绕过内容安全策略，并利用该技术从目标网站中提取出所需数据。


---


---


---


## 七、推荐

[【XSS跨站合集】反射型、存储型、DOM类XSS原理；输出在HTML、CSS、Javascript代码中<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165672818516782248534754%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165672818516782248534754&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.185^v2^control&amp;utm_term=xss&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165672818516782248534754%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165672818516782248534754&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.185%5Ev2%5Econtrol&amp;utm_term=xss&amp;spm=1018.2226.3001.4450)[【xss工具绕过】xss之burpsuite、前端、字典……<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/123901334?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165672818516782248534754%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165672818516782248534754&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123901334-null-null.185^v2^control&amp;utm_term=xss&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123901334?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165672818516782248534754%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165672818516782248534754&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123901334-null-null.185%5Ev2%5Econtrol&amp;utm_term=xss&amp;spm=1018.2226.3001.4450)
