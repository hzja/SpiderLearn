# 原创
：  【SQL注入】cookie注入：原理、步骤、示例

# 【SQL注入】cookie注入：原理、步骤、示例

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、cookie定义：](#1.1%E3%80%81cookie%E5%AE%9A%E4%B9%89%EF%BC%9A)

[二、cookie注入原理](#%E4%BA%8C%E3%80%81cookie%E6%B3%A8%E5%85%A5%E5%8E%9F%E7%90%86)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、原理：](#2.2%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[2.3、条件：](#2.3%E3%80%81%E6%9D%A1%E4%BB%B6%EF%BC%9A)

[2.4注入步骤：](#2.4%E6%B3%A8%E5%85%A5%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[第一步：寻找参数位置](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%AF%BB%E6%89%BE%E5%8F%82%E6%95%B0%E4%BD%8D%E7%BD%AE)

[第二步：去掉参数，观察参数影响](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%8E%BB%E6%8E%89%E5%8F%82%E6%95%B0%EF%BC%8C%E8%A7%82%E5%AF%9F%E5%8F%82%E6%95%B0%E5%BD%B1%E5%93%8D)

[第三步：（先清空网址）输入“javascript:alert(document.cookie=“id=”+escape(“xx”));”](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%EF%BC%88%E5%85%88%E6%B8%85%E7%A9%BA%E7%BD%91%E5%9D%80%EF%BC%89%E8%BE%93%E5%85%A5%E2%80%9Cjavascript%3Aalert%28document.cookie%3D%E2%80%9Cid%3D%E2%80%9D%2Bescape%28%E2%80%9Cxx%E2%80%9D%29%29%3B%E2%80%9D)

[第四步：判断是否存在漏洞](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E6%BC%8F%E6%B4%9E)

[第五步：cookie注入](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9Acookie%E6%B3%A8%E5%85%A5)

[三、插件示例](#%E4%B8%89%E3%80%81%E6%8F%92%E4%BB%B6%E7%A4%BA%E4%BE%8B)

[3.1、sqli-lasb21](#sqli-lasb-master%20less-21)

[方法一：用burpsuite进行抓包后修改](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E7%94%A8burpsuite%E8%BF%9B%E8%A1%8C%E6%8A%93%E5%8C%85%E5%90%8E%E4%BF%AE%E6%94%B9)

[方法二：安装火狐的cookie manager等插件进行修改cookie](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%AE%89%E8%A3%85%E7%81%AB%E7%8B%90%E7%9A%84cookie%20manager%E7%AD%89%E6%8F%92%E4%BB%B6%E8%BF%9B%E8%A1%8C%E4%BF%AE%E6%94%B9cookie)

[​编辑](#%E2%80%8B)

[​编辑](#%E2%80%8B%E7%BC%96%E8%BE%91)

---


## 一、简介

> 
<h3>1.1、cookie定义：</h3>
Cookie是在HTTP协议下，服务器或脚本可以维护客户工作站上信息的一种方式。
通常被用来辨别用户身份、进行session跟踪，最典型的应用就是保存用户的账号和密码用来自动登录网站


---


---


## 二、cookie注入原理

> 
<h3>2.1、简介：</h3>
cookie注入与传统的SQL注入基本上是一样，都是针对数据库的注入，就是注入的位置不同，注入形式不同


> 
<h3>2.2、原理：</h3>
ASP脚本中的request对象，被用于从用户那里获取信息。
Request对象的使用方法：request.[集合名称]（参数名称）效率低下，容易出错
eg获取从表单中提交的数据时：request.form("参数名称")
<hr/>
但ASP中规定也可以省略集合名称：request("参数名称")，当使用这样的方式获取数据时，ASP规定是按QueryString、Form、Cookies、ServerVariables的顺序来获取数据的。这样，当我们使用request("参数名称")方式获取客户端提交的数据，并且没有对使用request.cookies("参数名称")方式提交的数据进行过滤时，可能存在Cookie注入


> 
<h3>2.3、条件：</h3>
（从原理可以分析出存在cookie注入的条件）
1：cookie提交到数据库的语句未被过滤，或过滤不严谨
2：程序对提交数据获取方式是直接request("xxx")的方式，未指明使用request对象的具体方法进行获取


> 
<h3>2.4注入步骤：</h3>
<h4>第一步：寻找参数位置</h4>
eg：.asp?id=xx这样带参数id=xx
<hr/>
<h4>第二步：去掉参数，观察参数影响</h4>
eg：将“id=xx”删掉，看页面是否正常，正常，则说明参数不起作用。反之不正常，说明参数在数据传递中启直接作用
<hr/>
<h4>第三步：（先清空网址）输入“javascript:alert(document.cookie=“id=”+escape(“xx”));”</h4>
按Enter键后弹出一个对话框，内容是“id=xx”
然后重新输入原来URL回车
如果显示正常，说明是用Request(“id”)方式获取数据
//注释
document.cookie:表示当前浏览器中的cookie变量
alert（）:表示弹出一个对话框
escape():对字符串进行编码
<hr/>
<h4>第四步：判断是否存在漏洞</h4>
将SQL判断语句带入，并重复第三步
①“javascript:alert(document.cookie=“id=”+escape(“xx and 1=1”));”
②“javascript:alert(document.cookie=“id=”+escape(“xx and 1=2”));”。
若①正常，②不正常，则说明存在注入漏洞，并可以进行cookie注入
<hr/>
<h4>第五步：cookie注入</h4>
构造cookie注入payload
javascript:alert(document.cookie="smallclass="+escape("xx order by 2"));
javascript:alert(document.cookie="id="+escape("284 union select 1,…… from xx"));
……


#### 第二步：去掉参数，观察参数影响

---


#### 第四步：判断是否存在漏洞

---


---


---


## 三、插件示例

> 
<h3>3.1、sqli-lasb21</h3>
用admin登录进去，可以看出这是cookie注入，value一看就是加密过
YWRtaW4%3D 中的%3D 对应URL码中的 =
一般get和post的参数采用base64等加密方式将数据进行加密，再通过参数传递给服务器
-----&gt;YWRtaW4= ---------&gt; admin


<hr/>
<h4>方法一：用burpsuite进行抓包后修改</h4>
<h4>方法二：安装火狐的cookie manager等插件进行修改cookie</h4>
第一步：先将注入语句转换为base64加密后密文

<hr/>
第二步： 将加密后密文填到cookie  value里并保存


<hr/>
第三步：刷新页面，使cookie重新加载





#### 方法二：安装火狐的cookie manager等插件进行修改cookie

---

