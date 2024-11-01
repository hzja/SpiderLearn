# 原创
：  （25）【XSS跨站合集】反射型、存储型、DOM类XSS原理；输出在HTML、CSS、Javascript代码中

# （25）【XSS跨站合集】反射型、存储型、DOM类XSS原理；输出在HTML、CSS、Javascript代码中

**目录**

[一、理解XSS：](#%E7%90%86%E8%A7%A3XSS%EF%BC%9A)

[1.1、介绍：](#XSS%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[1.2、原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.3、利用地方：](#%E5%88%A9%E7%94%A8%E7%9A%84%E5%9C%B0%E6%96%B9%EF%BC%9A)

[1.4、成功执行条件：](#%E6%88%90%E5%8A%9F%E6%89%A7%E8%A1%8C%E7%9A%84%E6%9D%A1%E4%BB%B6%EF%BC%9A)

[1.5、XSS跨站危害：](#XSS%E8%B7%A8%E7%AB%99%E8%83%BD%E5%B9%B2%E4%BB%80%E4%B9%88%EF%BC%88%E5%8D%B1%E5%AE%B3%EF%BC%89%EF%BC%9A)

[1.6、利用的过程：](#%E5%88%A9%E7%94%A8%E7%9A%84%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：先判断是否可能存在XSS漏洞](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%85%88%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%8F%AF%E8%83%BD%E5%AD%98%E5%9C%A8XSS%E6%BC%8F%E6%B4%9E)

[第二步：构造漏洞利于语句](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9E%84%E9%80%A0%E6%BC%8F%E6%B4%9E%E5%88%A9%E4%BA%8E%E8%AF%AD%E5%8F%A5)

[二、XSS分类：](#XSS%E5%88%86%E7%B1%BB%EF%BC%9A)

[按漏洞成因：](#%E6%8C%89%E6%BC%8F%E6%B4%9E%E6%88%90%E5%9B%A0%EF%BC%9A)

[输出点的不同：](#%E8%BE%93%E5%87%BA%E7%82%B9%E7%9A%84%E4%B8%8D%E5%90%8C%EF%BC%9A)

[三、漏洞成因分类](#%E5%88%86%E7%B1%BB%EF%BC%9A)

[3.1、分类：](#3.1%E3%80%81%E5%88%86%E7%B1%BB%EF%BC%9A)

[3.2、反射型XSS（非持久型）：](#%E5%8F%8D%E5%B0%84%E6%80%A7XSS%EF%BC%88%E9%9D%9E%E6%8C%81%E4%B9%85%E5%9E%8B%EF%BC%89%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[利用过程：](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[3.3、存储型XSS（持久型）：](#%E5%AD%98%E5%82%A8%E5%9E%8BXSS%EF%BC%88%E6%8C%81%E4%B9%85%E5%9E%8B%EF%BC%89%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[利用过程：](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[3.4、DOM型XSS：](#DOM%E5%9E%8BXSS%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[利用过程：](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[onmouseover 事件（补充）：](#onmouseover%20%E4%BA%8B%E4%BB%B6%EF%BC%88%E8%A1%A5%E5%85%85%EF%BC%89%EF%BC%9A)

[onclick 事件（补充）：](#onclick%20%E4%BA%8B%E4%BB%B6%EF%BC%88%E8%A1%A5%E5%85%85%EF%BC%89%EF%BC%9A)

[四、按输出点分类](#%E5%9B%9B%E3%80%81%E6%8C%89%E8%BE%93%E5%87%BA%E7%82%B9%E5%88%86%E7%B1%BB)

[4.1、输出在HTML标签中](#4.1%E3%80%81%E8%BE%93%E5%87%BA%E5%9C%A8HTML%E6%A0%87%E7%AD%BE%E4%B8%AD)

[4.2、输出在CSS代码中](#4.2%E3%80%81%E8%BE%93%E5%87%BA%E5%9C%A8CSS%E4%BB%A3%E7%A0%81%E4%B8%AD)

[4.3、输出在Javascript代码中](#4.3%E3%80%81%E8%BE%93%E5%87%BA%E5%9C%A8Javascript%E4%BB%A3%E7%A0%81%E4%B8%AD)

---


## 一、理解XSS：

### 1.1、介绍：

> 
跨站脚本攻击，英文全称（Cross-Site Scripting），缩写为CSS（因为层叠样式表Cascading Style Sheets，缩写为CSS），所以就改为XSS了。
它也是代码注入的一种，XSS漏洞一直被评估为web漏洞中危害较大的漏洞，在OWASP TOP10的排名中一直属于前三的江湖地位。


### 1.2、原理：

> 
由于服务器对用户提交的数据过滤不严，导致用户将恶意Script代码插入到Web页面的HTML代码中，并被浏览器当成了JS代码并返回给客户端执行，进而实现对了客户端的攻击
（注：XSS跨站漏洞利用不仅仅限于JavaScript语言，还包括flash等其它的脚本语言）


### 1.3、利用地方：

> 
现代网站为了提高用户体验往往会包含大量的动态内容，即Web应用程序根据用户环境和需要来输出相应的内容。
<hr/>
经常遭受跨站脚本攻击的典型应用有：邮件、论坛、即时通信、留言板、社交平台等。
浏览器URL地址中提交了参数的地方
留言、提交表单、订单……


### 1.4、成功执行条件：

> 
1、成功在web页面中插入恶意代码
2、被插入的恶意代码能够被浏览器成功执行并返回给用户
3、等待或欺骗用户去访问含有XSS漏洞的页面


### 1.5、XSS跨站危害：

> 
窃取cookies
读取用户未公开的资料
模拟GET、POST请求操作用户的浏览器。使用JavaScript模拟浏览器发包
钓鱼、挂马
通过CSS，来发现用户曾经访问过的网站
劫持浏览器会话，达到执行任意操作，如非法转账、发送电子邮件等
进行大量的客户端攻击，如DDoS攻击
获取用户电脑的真实IP
重定向页面
获取键盘记录


## 1.6、利用的过程：

> 
<h4>第一步：先判断是否可能存在XSS漏洞</h4>
就是进行上传一些特殊的数据字符等，查看是否上传成功（即检测是否存在过滤机制）
如果没有过滤机制，则说明可能存在XSS漏洞
<hr/>
<h4>第二步：构造漏洞利于语句</h4>
视情况而定，根据不同的XSS分类，进行区别对待


#### 第二步：构造漏洞利于语句

---


---


## 二、XSS分类：

> 
<h3>按漏洞成因：</h3>
分为反射型、存储型、DOM型。
<hr/>
<h3>输出点的不同：</h3>
输出在HTML属性中、输出在CSS代码中、输出在JavaScript中


### 输出点的不同：

---


---


## 三、漏洞成因分类

### 3.1、分类：

> 
是否存储在服务器中：反射型XSS、存储型XSS
第三类：DOM型XSS（基于DOM树）


> 
<h3> 3.2、反射型XSS（非持久型）：</h3>
[【XSS跨站脚本】反射型xss（非持久型）<img alt="icon-default.png?t=M7J4" src="https://csdnimg.cn/release/blog_editor_html/release2.1.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M7J4"/>https://blog.csdn.net/qq_53079406/article/details/126482371?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126482371?spm=1001.2014.3001.5501)

<hr/>
<h3>3.3、存储型XSS（持久型）：</h3>
[【XSS跨站脚本】存储型XSS（持久型）<img alt="icon-default.png?t=M7J4" src="https://csdnimg.cn/release/blog_editor_html/release2.1.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M7J4"/>https://blog.csdn.net/qq_53079406/article/details/126483144?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126483144?spm=1001.2014.3001.5501)

<hr/>
<h3> 3.4、DOM型XSS：</h3>
[【XSS跨站脚本】DOM型XSS<img alt="icon-default.png?t=M7J4" src="https://csdnimg.cn/release/blog_editor_html/release2.1.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M7J4"/>https://blog.csdn.net/qq_53079406/article/details/126486385?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126486385?spm=1001.2014.3001.5501)


### 3.3、存储型XSS（持久型）：

---


---


---


## 四、按输出点分类

> 
<h3>4.1、输出在HTML标签中</h3>
XSS攻击Payload输出在HTML属性中时，攻击者需要在闭合相应的HTML属性后注入新<br/> 属性，或者在闭合标签后直接注入新标签
eg：输入：" οnclick="alert(/xxs/)
<hr/>
原型：&lt;input name="user" value="{{ your input }}"/&gt;
输出：&lt;input name="user" value="" οnclick="alert(/xss/)"/&gt;
<hr/>
eg：输入："&gt;&lt;script&gt;alert(/xss/)&lt;/script&gt;
直接闭合input标签，注入新的script标签
输出：&lt;input name="user" value=""&gt;&lt;script&gt;alert(/xss/)&lt;/script&gt;"/&gt;


---


> 
<h3>4.2、输出在CSS代码中</h3>
XSS攻击Payload输出在CSS代码中时，攻击者需要闭合相应的CSS代码
eg：输入：#000; background-image: url('javascript:alert(/xss/)')
闭合前面的color属性，注入background-image属性
<hr/>
原型：
&lt;style type="text/css"&gt;<br/> body {<br/> color: {{ your input }};<br/> }<br/> &lt;/style&gt;
<hr/>
输出：
&lt;style type="text/css"&gt;<br/> body {<br/> color: #000; background-image: url('javascript:alert(/xss/)');<br/> }<br/> &lt;/style&gt;


---


> 
<h3>4.3、输出在Javascript代码中</h3>
XSS攻击Payload输出在Javascript代码中时，攻击者需要闭合相应的Javascript代<br/> 码
eg：输入：'+alert(/xss/)+'
闭合前面的单引号，注入攻击代码
<hr/>
原型：
&lt;script&gt;<br/> var name='{{ your input }}';<br/> &lt;/script&gt;
<hr/>
输出：
&lt;script&gt;<br/> var name=''+alert(/xss/)+'';<br/> &lt;/script&gt;


---

