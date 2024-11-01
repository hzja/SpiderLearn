# 原创
：  HTTP请求走私漏洞浅析

# HTTP请求走私漏洞浅析

### 0x00 前言

HTTP请求走私漏洞(HTTP Request Smuggling)是发生协议层的一种攻击，最早于2005年就被发现并提出。漏洞发生的主要原因是不同的服务器，对于RFC标准的具体实现不一而导致的。

### 0x01 漏洞原理

HTTP 1.1协议相对于1.0主要引入了两个新的特性: Keep-Alive和pipline

1、Keep-Alive特性具体是指在HTTP请求头中，添加一个参数

`Connection: Keep-Alive`

告诉服务器在收到这个请求后不要关闭连接，后面再次发起请求时，继续使用这个TCP连接。

2、pipline特性是指在一次TCP连接中，可以连续不断地发送多个HTTP请求，而不必等待服务器响应。服务器会根据顺序进行处理。

有了这两个特性之后，HTTP 1.1相对于 HTTP 1.0来说，传输效率更高，如今HTTP 1.1也应用最为广泛。

---


在RFC 2616中规定，一个完整的数据包中需要在请求头部分包含”Content-Length”或者”Transfer-Encoding”来对数据包的长度进行说明。

1、Content-Length: 指明数据包的内容长度，一个字符长度为1，回车(\r\n)长度为2。如：

这个数据包的请求长度为10:

2、Transfer-Encoding: 当值为chunked时，服务器在读取到

`0\r\n\r\n`

后就会认为该请求已经结束。

而之后的内容会存在于服务器的缓存中，和下一个请求一起发送给服务器。

HTTP请求走私漏洞的核心就在于前端和后端对于请求的长度判断不一而引起的。

如当前端使用Content-Length来判断，而后端使用Transfer-Encoding:chunked来判断时，我们构造一个请求如:

前端认为请求长度为6，会将所有内容转发给后端，而后端读到”0\r\n\r\n”后就认为请求已经结束，因此最后一个”G”就会留到缓存服务器中，被拼接到下一个请求的开始，如

这样当下一个正常用户发起请求时，就会返回错误，因为服务器并不认得”GPOST”是什么请求方式。

这就是一个简单的HTTP请求走私攻击的例子。

上面这个例子中，前端使用Content-Length判断，后端使用Transfer-Encoding:chunked判断，因此属于CL-TE类型，与之对应的还有TE-CL、TE-TE。

### 0x02 漏洞复现

利用工具:Burpsuite

需要在Repeater中关闭更新Content-Length

以burp靶场CL-TE为例 : https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te

正常访问:

开启抓包，将请求改为POST方式

构造请求

放包。当下一个用户访问这个页面时

### 0x03 扩展

根据以上原理，我们可以更改下一个正常访问用户的请求内容，包括Cookie信息等。因此可以扩展出危害更大的攻击，如获取服务器敏感信息、获取用户登录信息、能交互的反射型XSS等。

### 0x04 缓解措施

对于前端，对所有请求进行规范化，避免模糊请求。

对于后端，拒绝掉一切模糊请求。

   申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
