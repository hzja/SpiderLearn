# 原创
：  10-1 HTTP协议相关概念

# 10-1 HTTP协议相关概念

#### 定义

        HTTP协议（超文本传输协议）是一种用于从WWW服务器传输超文本到本地浏览器的传送协议。它采用请求与响应模式，是一个无连接、无状态的应用层协议，通常运行于TCP之上。HTTP协议的11版本及以上提供了一种长连接机制。

#### 请求与响应模式 

        HTTP协议规定了请求与响应模式，客户端发出请求，服务器端响应该请求并返回。换句话说，通信始于客户端发出的请求，服务器在未接收到请求前不会发送响应。

```
         +---------------------+         +---------------------+
         |       客户端        |          |      服务端        |
         +---------------------+         +---------------------+
                    │                               │
                    │      1 发送请求             │
                    ├──────────────────────▶│
                    │                               │
                    │                          处理请求             │
                    │                               │
                    │      2 返回响应             │
                    │◀
```
