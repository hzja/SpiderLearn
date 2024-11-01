# 原创
：  XSS漏洞详解

# XSS漏洞详解

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[self型XSS的原理](#self%E5%9E%8BXSS%E7%9A%84%E5%8E%9F%E7%90%86)

[1.功能需要支持Markdown语法](#1.%E5%8A%9F%E8%83%BD%E9%9C%80%E8%A6%81%E6%94%AF%E6%8C%81Markdown%E8%AF%AD%E6%B3%95)

[2.能执行html标签写法](#2.%E8%83%BD%E6%89%A7%E8%A1%8Chtml%E6%A0%87%E7%AD%BE%E5%86%99%E6%B3%95)

[(DOM型XSS另一个名字罢了)](#%28DOM%E5%9E%8BXSS%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%90%8D%E5%AD%97%E7%BD%A2%E4%BA%86%29)

[Don型XSS总结](#Don%E5%9E%8BXSS%E6%80%BB%E7%BB%93)

---


Markdown是一种轻量级标记语言，创始人为约翰·格鲁伯（John Gruber）。它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的 XHTML（或者HTML）文档。这种语言吸收了很多在电子邮件中已有的纯文本标记的特性。

### self型XSS的原理

---


##### 1.功能需要支持Markdown语法

##### 2.能执行html标签写法

#### (DOM型XSS另一个名字罢了)

1.看到这个#、##、-、``发现能支持是Markdown语法<br/> Markdown语法是可以直接执行html标签的！！！也就是能尝试JavaScript代码

<img alt="" height="638" src="https://img-blog.csdnimg.cn/600f9308acef4f398d309f1f0d72af37.png" width="1064"/>2.用户输入：1 —&gt; 渲染导图 -&gt; 页面显示：1 (符合XSS原理)<img alt="" height="593" src="https://img-blog.csdnimg.cn/7054def16fc549fcaf19935f55914a26.png" width="1061"/>

3.用户输入：JS —&gt; 渲染导图 -&gt; 页面显示：JS (JS代码被执行)

&lt;font color="red"&gt;红色&lt;/font&gt;<img alt="" height="600" src="https://img-blog.csdnimg.cn/6677ac58219f45efb15431d0cc66a5be.png" width="1080"/>

4.1 第一步：用户输入：JavaScript代码 ：&lt;img src="x"&gt;<br/> 4.2 第二步：用户点击：渲染导图<br/> 4.3 第三步：浏览器网站：插入到HTML标签,显示在网页上<br/> 4.4 第四步：浏览器网站：网页执行JavaScript弹窗代码<img alt="" height="645" src="https://img-blog.csdnimg.cn/dba6069e1c154a748bfabc3a9df9f61d.png" width="1080"/>

#### Don型XSS总结

###### 原理：用户输入的内容(在前端：构造的JavaScript代码内容！！！) -&gt; 被前端代码执行(在前端：被网页JavaScript代码解析执行构造的JavaScript代码内容！！！) -&gt; 最后又在前端显示

点赞+在看支持一下吧~感谢看官老爷~ 

你的点赞是我更新的动力

**  **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>

---

