# 原创
：  【0基础学爬虫】爬虫基础之HTTP协议的基本原理介绍

# 【0基础学爬虫】爬虫基础之HTTP协议的基本原理介绍

> 
大数据时代，各行各业对数据采集的需求日益增多，网络爬虫的运用也更为广泛，越来越多的人开始学习网络爬虫这项技术，K哥爬虫此前已经推出不少爬虫进阶、逆向相关文章，为实现从易到难全方位覆盖，特设【0基础学爬虫】专栏，帮助小白快速入门爬虫，本期为 HTTP 协议的基本原理介绍。


#### 计算机网络模型

计算机网络是指由通信线路互相连接的许多自主工作的计算机构成的集合体，各个部件之间以何种规则进行通信，就是网络模型研究的问题，除了标准的 OSI 七层模型以外，常见的网络层次划分还有 TCP/IP 四层协议以及 TCP/IP 五层协议，它们之间的对应关系如下图所示：

#### HTTP 发展史

#### HTTP 协议和 HTTPS 协议

HTTP（Hypertext Transfer Protocol）中文名为**超文本传输协议**，其作用是把超文本数据从网络传输到本地浏览器，能够高效而准确地传输超文本文档。HTTP 是由万维网协会（World Wide Web Consortium）和 Internet 工作小组 IETF（Interner Engineering Task Force）合作制定的规范，目前被广泛使用的是 HTTP 1.1 版本，如今也有不少网站支持 HTTP 2.0 版本。

HTTP 协议的特点：

HTTPS（Hypertext Transfer Protocol over Secure Socket Layer）是一种通过计算机网络进行安全通信的传输协议，经由 HTTP 进行通信，利用 SSL/TLS 建立全信道，加密数据包，HTTPS 使用的主要目的是提供对网站服务器的身份认证，同时保护交换数据的隐私与完整性，相当于 HTTP 协议的安全版。

HTTPS 协议的特点：

时势发展：

HTTP 和 HTTPS 的区别主要如下：

上述 HTTPS 看起来是加强版的 HTTP，可圈可点，但并不是完美无缺的：

#### HTTP 请求过程

HTTP 由请求和响应构成，是一个标准的客户端服务器模型（B/S），HTTP 协议永远都是客户端发起请求，服务器回送响应，HTTP 是一个无状态的协议，无状态是指客户机（Web 浏览器）和服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后服务器返回响应（response），连接就被关闭了，在服务器端不保留连接的有关信息，HTTP 遵循请求(Request)/应答(Response)模型，客户机（浏览器）向服务器发送请求，服务器处理请求并返回适当的应答，所有 HTTP 连接都被构造成一套请求和应答。

HTTP 请求/响应的步骤：
1. 客户端连接到 Web 服务器：一个 HTTP 客户端，通常是浏览器，与 Web 服务器的 HTTP 端口（默认为80）建立一个 TCP 套接字连接；1. 发送 HTTP 请求：通过 TCP 套接字，客户端向 Web 服务器发送一个文本的请求报文，一个请求报文由请求行、请求头部、空行和请求数据四部分组成；1. 服务器接受请求并返回 HTTP 响应：Web 服务器解析请求，定位请求资源，服务器将资源复本写到 TCP 套接字，由客户端读取。一个响应由状态行、响应头部、空行和响应数据四部分组成；1. 释放连接 TCP 连接：若 connection 模式为 close，则服务器主动关闭 TCP 连接，客户端被动关闭连接，释放 TCP 连接;若 connection 模式为 keepalive，则该连接会保持一段时间，在该时间内可以继续接收请求；1. 客户端浏览器解析 HTML 内容：客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码，然后解析每一个响应头，响应头告知以下为若干字节的 HTML 文档和文档的字符集，客户端浏览器读取响应数据 HTML，根据 HTML 的语法对其进行格式化，并在浏览器窗口中显示。
步骤简述：
1. 浏览器向 DNS 服务器请求解析该 URL 中的域名所对应的 IP 地址；1. 解析出 IP 地址后，根据该 IP 地址和默认端口 80，和服务器建立 TCP 连接；1. 浏览器发出读取文件(URL 中域名后面部分对应的文件)的 HTTP 请求，该请求报文作为 TCP 三次握手的第三个报文的数据发送给服务器；1. 服务器对浏览器请求作出响应，并把对应的 HTML 文本发送给浏览器；1. 释放 TCP 连接；1. 浏览器将该 HTML 文本并显示内容。
HTTP 请求/响应模型:

通俗点讲就是在浏览器地址栏输入一个 URL，按下回车之后便可观察到对应的页面内容，实际上，这个过程是浏览器先向网站所在的服务器发送一个请求，网站服务器接收到请求后对其进行处理和解析，然后返回对应的响应，接着传回浏览器，由于响应里包含页面的源代码等内容，所以浏览器在对其进行解析，便将网页呈现出来。

#### HTTP 请求方法

HTTP/1.1 协议中共定义了八种方法（有时也叫“动作”），来表明 Request-URL 指定的资源不同的操作方式，HTTP1.0 定义了三种请求方法：GET，POST 和 HEAD 方法，HTTP1.1 新增的五种请求方法：OPTIONS，PUT，DELETE，TRACE 和 CONNECT 方法：
1. OPTIONS：返回服务器针对特定资源所支持的 HTTP 请求方法，也可以利用向 web 服务器发送 ‘*’ 的请求来测试服务器的功能性；1. HEAD：向服务器索与 GET 请求相一致的响应，只不过响应体将不会被返回，这一方法可以再不必传输整个响应内容的情况下，就可以获取包含在响应报头中的元信息；1. GET：向特定的资源发出请求，并返回实体主体；1. POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求体中，POST 请求可能会导致新的资源的建立和/或已有资源的修改；1. PUT：向指定资源位置上传其最新内容；1. DELETE：请求服务器删除 Request-URL 所标识的资源；1. TRACE：回显服务器收到的请求，主要用于测试或诊断；1. CONNECT：把服务器仿作跳板，让服务器代替客户端访问其他网页。
最为常见的请求方法是 GET 和 POST，在浏览器地址栏输入一个 URL，按下回车，即发起了一个 GET 请求，请求的参数会直接包含到 URL 里；POST 请求大多在提交表单时发起，例如登录，输入用户名和密码，点击登录即发起一个 POST 请求，其数据通常以表单的形式传输，而不会体现在 URL 中，GET 和 POST 请求方法区别如下：

#### HTTP 请求头

HTTP 请求头（HTTP Request Header）提供了关于请求，响应或者其他的发送实体的信息，HTTP 的头信息包括通用头、请求头、响应头和实体头四个部分：
1. 通用头标：即可用于请求，也可用于响应，是作为一个整体而不是特定资源与事务相关联；1. 请求头标：允许客户端传递关于自身的信息和希望的响应形式；1. 响应头标：服务器和于传递自身信息的响应；1. 实体头标：定义被传送资源的信息，即可用于请求，也可用于响应。
每个头域由一个域名，冒号（:）和域值三部分组成，常用的 HTTP 请求头如下：

#### HTTP 响应头

HTTP 响应头（HTTP Responses Header）中包含了服务器对请求的应答信息，HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文：
1. 状态行：由 HTTP 协议版本号， 状态码， 状态消息 三部分组成；1. 消息报头：用来说明客户端要使用的一些附加信息；1. 空行：消息报头后面的空行是必须的；1. 响应正文：服务器返回给客户端的文本信息。
常用的 HTTP 响应头如下：

#### HTTP 响应状态码

**1xx：**该状态码表示临时响应并需要请求者继续执行操作

**2xx：**该状态码表示成功

**3xx：**该状态码表示要完成请求，需要进一步操作，通常这些状态码用来重定向

**4xx：**表示请求可能出错，妨碍了服务器的处理

**5xx：**表示服务器在尝试处理请求时发生内部错误，这些错误可能是服务器本身的错误，并不是请求出错，当然也有可能是请求者的故意为之，使服务器本身出现错误
