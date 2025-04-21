# 转载
：  隧道代理无法更换IP？

# 隧道代理无法更换IP？

## 转载：

[为什么你的隧道代理没有更换IP](https://mp.weixin.qq.com/s/4sRmhtezyO0_ZnuW_H7SXA)

有部分小伙伴反馈在客户端使用隧道代理动态版（每次请求更换IP） 的过程中发现没有更换IP，遂怀疑是我们隧道代理服务器的问题，其实不然。今天我们就在这里谈谈，为什么会有隧道代理会出现没有更换IP的情况。

### **持久连接**

需要了解，HTTP/1.1（以及 HTTP/1.0 的各种增强版本）允许 HTTP 在请求处理结束之后将 TCP 连接保持在打开状态（并不会立即关闭），以便为未来的 HTTP 请求重用之前建立的连接。<br/> 在请求处理结束之后仍然保持在打开状态的 TCP 连接被称为持久连接。而非持久连接则会在每个请求结束之后关闭。持久连接会在不同请求之间保持打开状态，直到客户端或服务端决定将其关闭为止。<br/> 重用已对目标服务器打开的空闲持久连接，就可以避开缓慢的连接建立阶段。而且，已经打开的连接还可以避免慢启动的拥塞适应阶段，以便更快速地进行数据的传输。

### **HTTP客户端举例**

通过上面的内容我们了解到，开启Keep-Alive可以更快速的进行数据传输。<br/> 最常见的使用场景就是浏览器在打开一个网页，并不会为了每个资源都开打一个TCP连接，而是会同时打开少量TCP连接，利用Keep-Alive机制，不断利用少量连接传输多数HTTP请求。<br/> 由于去除了进行连接和关闭连接的开销，因此加快访问速度。

在一些编程语言开发的HTTP客户端，爬虫框架中，除了会使用异步方式发送请求，也会使用TCP连接复用来加速处理使用者的请求。

**Python-Requests**<br/> 使用Requests提供的Session发送请求时，除了会自动保存cookie，还会使用urllib3底层提供的connection-pooling（连接池）

例如利用requests-session配置隧道代理动态版连续发送3个请求并打印出当前使用的代理IP

```
import time
import requests


username = "txxxxxxxxxxxxx"
password = "password"
tunnel = "tpsXXX.kdlapi.com"
proxies = {
 "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
 "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}
s = requests.session()
for i in range(3):
    res = s.get('https://dev.kdlapi.com/testproxy', proxies=proxies)
    print(res.text)
    time.sleep(1)

```

```
sucess! client ip: 175.7.196.238 
sucess! client ip: 175.7.196.238 
sucess! client ip: 175.7.196.238 

```

可以发现三次都是同一个IP，并且使用Wireshark抓包查看，很明显这三次请求都走了一个TCP连接。

### **Python-Scrapy**

Scrapy底层采用的Twisted异步网络编程框架，在Twisted源码中就能找到对于连接复用的实现<br/> twisted/web/_newclient.py<br/> Class HTTP11ClientProtocol<br/> _finishResponse_WAITING()<br/><img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/3d38419293df51203a16f587b6841012.png"/>

•拿到目标网站响应后，在_finishResponse_WAITING函数中判断响应header中的connection是否为close•如果为close调用self._giveUp()，直接关闭本次连接•否则调用self.transport.resumeProducing()，继续重用这条TCP连接，读取响应或者发送HTTP请求。

### **原因**

由于隧道代理动态版底层的实现是只有在新建立连接的情况下，才能将请求转发给不同的代理服务器。如果使用代理的HTTP客户端在拿到响应后并没有直接关闭TCP连接，后续的HTTP请求可能会继续在这条TCP连接上发送，导致多个HTTP请求使用的是相同的代理IP。

### **解决方法**

那如何在请求结束后主动关闭连接呢？<br/> 在 HTTP/1.0 中，keep-alive 并 不 是 默 认 使 用 的。客 户 端 必 须 发 送 一 个Connection: Keep-Alive 请求首部来激活 keep-alive 连接。<br/> 而在HTTP/1.1中默认启用Keep-Alive， 默认情况下所在HTTP1.1中所有连接都被保持，除非在请求头或响应头中指明要在响应结束后关闭连接：Connection: Close 。<br/> 通常来说，只需要在请求头中加入Connection: Close，目标服务器识别后，在响应头中也会加入Connection: Close，并且在发送完响应后主动关闭连接。<br/> 所以如果你不能确定你所使用的HTTP客户端是否会在请求结束后关闭请求，是可以在发送请求的header中主动加上：Connection: Close

依旧是上述Python-Requests代码

```
# 使用隧道代理动态版发送请求
headers = {"Connection": "close"}
s = requests.session()
for i in range(3):
    res = s.get('https://dev.kdlapi.com/testproxy', proxies=proxies, headers=headers)
    print(res.text)
    time.sleep(1)

```

```
sucess! client ip: 121.205.214.213 
sucess! client ip: 27.148.203.221 
sucess! client ip: 114.99.131.98 

```

每次请求都更换了IP，再次查看Wireshark抓包数据，三次HTTP请求，每次都建立了新的TCP连接。

**总结**<br/> 使用隧道代理动态版发现没有更换IP很有可能是HTTP客户端复用了之前建立的TCP连接，由此来加快网络请求。<br/> 大家购买隧道带动态版就是为了每次请求更换IP，复用了之前的TCP连接就无法达到更换IP的效果，只需要在请求头中加入Connection: Close，显式地指出本次连接传输完成就立即关闭即可。<br/> 当然，如果您不需要每次请求都切换IP，使用keep_alive机制可以加快你的请求，需要您根据业务实际情况进行判断。

更多爬虫技术好文<br/><img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/3760daf68558bc423a06d0e2c2410f60.jpeg"/>
