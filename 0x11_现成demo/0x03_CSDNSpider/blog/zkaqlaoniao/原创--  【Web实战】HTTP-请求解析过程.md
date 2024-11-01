# 原创
：  【Web实战】HTTP-请求解析过程

# 【Web实战】HTTP-请求解析过程

**目录**

[0x00 前言](#0x00%20%E5%89%8D%E8%A8%80)

[0x01 "畸形scheme"HTTP请求](#0x01%20%22%E7%95%B8%E5%BD%A2scheme%22HTTP%E8%AF%B7%E6%B1%82)

[0x02 其他](#0x02%20%E5%85%B6%E4%BB%96)

---


## 0x00 前言

Reactor Netty HttpClient 是 Reactor Netty 框架提供的一个用于进行异步 HTTP 请求的客户端库。它基于 Reactor 框架，采用响应式编程模型，允许以非阻塞的方式执行 HTTP 请求和处理响应。

通过引入对应的依赖，即可通过使用Reactor Netty从HttpClient获取目标的响应报文：

下面是一个具体的例子,首先创建了一个 HttpClient 对象，通过Reactor Netty 的链式调用 API 来构建我们的请求，发起了一个 GET 请求访问了target并打印对应响应的内容，完成了整个请求与响应处理过程：

```
HttpClient httpClient = HttpClient.create().wiretap(true);
httpClient.get().uri(target).responseContent().aggregate().asString().doOnSuccess(s -&gt; {
    System.out.println("s1=" + s);
}).block();

```

上述代码串联了多个Reactor Netty的方法，下面是简单的说明：

当然除了block以外，还可以通过类似subscribe获取响应报文。

## 0x01 "畸形scheme"HTTP请求

以GET请求为例，下面对reactor netty httpclient请求解析过程进行简单的分析：

在 Reactor Netty 框架中，MonoHttpConnect是一个用于表示 HTTP 连接的 Mono 类型。它代表了一个异步的 HTTP 请求，并返回一个 Mono 类型的结果。通过调用 subscribe 方法，可以触发实际的 HTTP 请求，并通过订阅者来处理响应结果：

首先这里会实例化HttpClientConnect，这里会调用`uriEndpointFactory.createUriEndpoint`创建 UriEndpoint，UriEndpoint是一个用于表示网络请求的目标地址的类。它封装了 URI 的相关信息，包括协议、主机名、端口号、路径等。reactor.netty.http.client.UriEndpointFactory#createUriEndpoint方法根据传入的参数，创建一个 UriEndpoint 对象，并返回该对象：

可以看到，在createUriEndpoint方法中，主要是通过正则匹配的方式获取URI 的相关信息：

创建完HttpClientHandler后，会通过配置对象（_config）来设置一些参数：

这里会调用resolverInternal方法用于获取地址解析器组。它负责将主机名解析为一个或多个 IP 地址，以便 HttpClient 可以与目标服务器建立连接：

实际调用的是其父类ClientTransportConfig的方法：

这里会create一系列的组件：

例如创建ConnectionProvider用来管理连接池，Builer这里硬编码传入对应的name为http，后续会创建一组连接并存储在连接池中。 当需要进行网络通信时，可以从连接池中获取一个连接并使用它来发送请求：

又例如PooledConnectionProvider，这个在后面会用到：

调用完后，此时会调用`_config.httpConnectionProvider().acquire`从 HTTP 连接提供者中获取一个可用的连接。以便进行 HTTP 请求：

查看具体的过程，这里最终会调用PooledConnectionProvider的acquire方法：

reactor.netty.resources.PooledConnectionProvider的作用是提供连接池管理功能。在使用 Reactor Netty 进行网络通信时，可以通过 PooledConnectionProvider 来管理和复用连接，以提高性能和资源利用率，这里会调用 acquire 方法获取一个可用的连接，以便进行网络通信。获取到的连接可以用于发送请求、接收响应等操作，如果连接池中没有可用的连接，它可能会创建一个新的连接：

从对应的调试信息可以知道，这里创建的是http client pool，结合前面解析请求target的过程，这里name的值并不是从请求target的schema获取的，是从前面Builer里硬编码获取的：

后面是HttpClientOperations的处理，也没有对schema进行相应检查操作，那么这里有没有可能reactor netty httpclient可以以任意符合正则匹配的schema进行请求呢？

验证下前面的猜想：

正常情况下，通过reactor netty httpclient请求`http://127.0.0.1:8080/health`正常返回：

将scheme替换成任意字符，可以发现依旧能正常请求并返回：

查看reactor netty httpclient的日志，确实没有考虑用户输入的协议，在PooledConnectionProvider创建了新的http client pool，同时也没有发现关于schema的检查：

结合前面请求target解析的正则：

scheme还支持下划线匹配，所以类似`anyt____hing`的schema同样能正常请求：

## 0x02 其他

WebClient是从Spring WebFlux 5.0版本开始提供的一个非阻塞的基于响应式编程的进行Http请求的客户端工具。 它的响应式编程的基于Reactor的。 WebClient中提供了标准Http请求方式对应的get、post、put、delete等方法，可以用来发起相应的请求。

通过引入如下依赖即可使用WebClient:

从依赖关系可以看到，实际上spring-boot-starter-webflux也是基于reactor-netty-http来发起相应的请求的：

下面的代码是一个简单的WebClient请求示例。可以通过`WebClient.create()`创建一个WebClient的实例，然后选择调用方式get，在`uri()`指定需要请求的路径，然后调用`retrieve()`发起请求并获得响应，`bodyToMono(String.class)`用来指定请求结果需要处理为String:

```
WebClient webClient = WebClient.builder().build();
String response = webClient.get().uri(url).retrieve().bodyToMono(String.class).block();
return response;

```

简单看下WebClient的处理过程，首先会在org.springframework.web.util.UriComponentsBuilder#fromUriString方法处理需要请求的目标：

可以看到这里也是通过正则的方式进行匹配：

若未匹配相关信息，会抛出`throw new IllegalArgumentException("[" + uri + "] is not a valid URI");`异常，否则进行进一步的封装，同时这里对scheme和host进行了一定的合法性检查：

但是并没有强制校验scheme是否是http/https，所以同样的当尝试请求`anything://127.0.0.1:8080/health`，WebClient同样也是能正常解析并正常返回：

可以看到结合reactor netty httpclient解析过程中的一些处理方式，可以构造类似上述任意协议的“畸形”的请求样式，在某种情况下可以绕过现有ssrf的一些安全防护措施。开发人员应该避免将不受信任且未经验证的数据从 HTTP 请求传递给reactor netty httpclient，避免不必要的绕过导致ssrf风险。

```
原文链接：https://forum.butian.net/share/2557
```

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/9874c27ea9c849898e30cedd9581944c.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/4c55bc73919f4834a0affe8c55a6de63.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/4464c170419e44af8aff783cdb0e47a5.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/1709799e4c1a49b7b79bde09a1771029.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/ce16d81a33614f8287ea2bc028ee8304.png" width="665"/>

应急响应笔记

学习路线
