# 原创
：  【XSS跨站脚本】反射型xss（非持久型）

# 【XSS跨站脚本】反射型xss（非持久型）

**目录**

[反射型XSS（非持久型）](#%E5%8F%8D%E5%B0%84%E6%80%A7XSS%EF%BC%88%E9%9D%9E%E6%8C%81%E4%B9%85%E5%9E%8B%EF%BC%89%EF%BC%9A)

[1.1、简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、原理：](#1.2%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.3、利用原理：](#1.3%E3%80%81%E5%88%A9%E7%94%A8%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.4、利用过程：](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.5、pikachu靶场小插曲](#1.5%E3%80%81pikachu%E9%9D%B6%E5%9C%BA%E5%B0%8F%E6%8F%92%E6%9B%B2)

---


## 反射型XSS（非持久型）

### 1.1、简介：

> 
等待或诱骗用户点击，当用户点击了含有恶意JavaScript脚本的URL才可以触发，并且只能触发一次，所以也被称为“非持久性XSS”


### 1.2、原理：

> 
恶意代码并没有存储到服务器数据库中。因为服务器不加处理的把该恶意脚本“反射”回点击用户的浏览器，然后在点击用户的浏览器上解析执行相应的恶意脚本，从而到达攻击者想要的功能。


> 
<h3>1.3、利用原理：</h3>


最简单的一种攻击，也是常用于说明XSS漏洞潜在影响的一种攻击， 可导致攻击者截获通过验证的用户的会话令牌。劫持用户的会话后， 攻击者就可以访问该用户经授权访问的所打数据和功能
1、用户正常登录应用程序， 得到一个包含会话令牌的cookie
2、攻击者通过某种方法向用户提交以下URL（和生成一个对话框消息的示例一样，这个URL包含嵌人式JavaScnpt代码）
3、用户从应用程序中请求攻击者传送给他们的URL
4、服务器响应用户的请求。由于应用程序中存在XSS漏洞， 响应中包含攻击者创建的JavaScnpt代码
5、用户浏览器收到攻击者的JavaScript代码，像执行从应用程序收到的其他代码一样， 浏览器执行这段代码
6、攻击者创建的恶意JavaScript代码，让用户浏览器向攻击者拥有的一个域，提出一个请求，请求中包含用户访问应用程序的当前会话令牌
7、攻击者监控访问这个域的请求，并收到用户的请求。攻击者使用截获的令牌劫持用户的会话， 从而访问该用户的个人信息，并代表该用户执行任意操作
<hr/>
攻击者能够诱使用户访问他选择的URL，不能简单的在域中保存一段恶意脚本，并向用户传送一个直接指向这段脚本的链接，通过应用程序中的XSS漏洞传送自己的恶意JavaScript代码

同源策略：为防止不同域在用户浏览器中彼此干扰， 浏览器对从不同来源（域）收到的内容进行隔离。攻击者的目的不是单纯地执行任意脚本， 而是截获用户的会话令牌。浏览器不允许任何原有脚本访问一个站点的cookie，避免会话被劫持。且只有发布cookie的站点能够访问这些cookie，仅在返回发布站点的HTTP请求中提交cookie；只有通过该站点返回的页面所包含或加载JavaScript能访问cookie。因此域上的一段脚本查询将无法获得cookie，劫持攻击将失败
就用户的浏览器而言，利用XSS漏洞的攻击之所以取得成功， 是因为攻击者的恶意JavaScript是由域送交给它的。当用户请求攻击者的URL时，浏览器向域提交一个请求， 然后应用程序返回一个包含一段JavaScript的页面。和从域收到的任何JavaScript一样， 浏览器执行这段脚本， 因为用户信任域，这也就是为何攻击的脚本能够访问cookie的原因，它实际来自其他地方（跨站脚本的由来）


> 
<h3>1.4、利用过程：</h3>
我开始使用一个虚拟机搭建的OWASP靶机环境进行测试



安全等级用的低

 <img alt="" height="197" src="https://img-blog.csdnimg.cn/a3a78c9c449e458f834a6ee6287157ac.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="874"/>

貌似我的&lt;script&gt;还是被吃了
被HTML实体编码




> 
<h3>1.5、pikachu靶场小插曲</h3>
注：会被HTML实体编码
<hr/>
第一步：我先测试有没有有没有对上传过滤
（大吃一惊，这是把我的字符给转义了）








该不会是被我自己的<img alt="" height="48" src="https://img-blog.csdnimg.cn/45dc15d200044264912d0b3abb7cb73c.png" width="48"/>给拦住了（我自己没启动<img alt="" height="48" src="https://img-blog.csdnimg.cn/f9ba88e756d2452c96a8424c6fd3ccfa.png" width="48"/>） 
<img alt="" height="820" src="https://img-blog.csdnimg.cn/1eafcac08f42464f8ce7081f03c25f1e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/> 发现真是它拦截的
给他关了 






 我复制这个URL地址在其他浏览器上打开，（）/都被编码了<img alt="" height="485" src="https://img-blog.csdnimg.cn/b40d4318b7f646c889ff40ab6bfd8f32.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


