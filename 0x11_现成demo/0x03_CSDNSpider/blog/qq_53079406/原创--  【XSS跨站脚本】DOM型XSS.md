# 原创
：  【XSS跨站脚本】DOM型XSS

# 【XSS跨站脚本】DOM型XSS

**目录**

[DOM型XSS](#DOM%E5%9E%8BXSS%EF%BC%9A)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、原理：](#1.2%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.3、利用原理：](#1.3%E3%80%81%E5%88%A9%E7%94%A8%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.4、利用过程：](#1.4%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[onmouseover 事件（补充）：](#onmouseover%20%E4%BA%8B%E4%BB%B6%EF%BC%88%E8%A1%A5%E5%85%85%EF%BC%89%EF%BC%9A)

[onclick 事件（补充）：](#onclick%20%E4%BA%8B%E4%BB%B6%EF%BC%88%E8%A1%A5%E5%85%85%EF%BC%89%EF%BC%9A)

---


## DOM型XSS

> 
<h3>1.1、简介：</h3>
基于文档对象模型Document Objeet Model，DOM)的一种漏洞。DOM是一个接口（与平台、编程语言无关），能够通过程序或脚本动态地访问和更新文档内容、结构和样式，并将处理后结果返回到页面
<hr/>
DOM XSS与反射型XSS、存储型XSS的主要区别在于DOM XSS的XSS代码不需要服务端解<br/> 析响应的直接参与，触发XSS的是浏览器端的DOM解析
<hr/>
反射型和存储型XSS漏洞都表现出一种特殊的行为模式， 其中应用程序提取用户控制的数据<br/> 并以危险的方式将这些数据返回给用户。第三类XSS漏洞并不具有这种特点。在这种漏中， 攻击者的JavaScript执行：用户请求一个经过专门设计的URL，它由攻击者提交，且其中包含嵌人式JavaScript；服务器的响应中并不以任何形式包含攻击者的脚本；当用户的浏览器处理这个响应时， 上述脚本得以处理
<hr/>
由于客户端JavaScript可以访问浏览器的文本对象模型，因此它能够决定用于加载当前页面的URL。由应用程序发布的一段脚本可以从URL中提取数据， 对这些数据进行处理， 然后用它动态更新页面的内容。如果这样， 应用程序就可能易于受到基于DOM的XSS攻击


---


> 
<h3>1.2、原理：</h3>
其中一些是用户可以操纵的（URL，location，refelter等）。客户端的脚本程序可以通过DOM动态地检查和修改页面内容，不用请求服务器，而是直接从客户端获得DOM中的数据在本地执行，如果DOM中的数据没有经过严格过滤，就会产生DOM-based XSS漏洞。





> 
<h3>1.3、利用原理：</h3>
与存储型XSS漏洞相比， 基于DOM的XSS漏洞与反射型XSS漏洞有更大的相似性。利用它们通常需要攻击者诱使一名用户访问一个包含恶意代码的专门设计的URL ，并由服务器响应那个确保得恶意代码得以执行的特殊请求，但在利用反射型与基于DOM的XSS漏洞的细节方面，存在一些重要的差异




> 
<h3>1.4、利用过程：</h3>
**第一步：**提交一些文字，然后定位回显的位置，顺路提交一些特殊字符瞅瞅




**第二步：**通过输入精心构造的语句来达到预期效果




尝试给出的提示方法，闭合前面语句
<hr/>
<h4>onmouseover 事件（补充）：</h4>
会在鼠标指针移动到指定的元素上时发生
**语法：**
HTML：&lt;element οnmοuseοver="SomeJavaScriptCode"&gt;
JavaScript ：**object**.οnmοuseοver=function(){**SomeJavaScriptCode**};
**参数：**
**SomeJavaScriptCode **必需的，规定该事件发生时执行的JavaScript

'&gt;&lt;img src="#" οnmοuseοver="alert('xss')"&gt;


因为提交的并非真实图片，所以图片是裂开的，真正的是以js执行脚本代码



尝试第二个提示语句
<hr/>
<h4>onclick 事件（补充）：</h4>
会在元素被点击时发生
**语法：**
HTML：&lt;**element** οnclick="**SomeJavaScriptCode**"&gt;
JavaScript：**object**.οnclick=function(){**SomeJavaScriptCode**};
**参数：**
**SomeJavaScriptCode **必需的，规定该事件发生时执行的JavaScript

' οnclick="alert('xss')"&gt;


点击下面的what do you see？会出现弹窗


点击完以后就被清空了



#### onmouseover 事件（补充）：

---

