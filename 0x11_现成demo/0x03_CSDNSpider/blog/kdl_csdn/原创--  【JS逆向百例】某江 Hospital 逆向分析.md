# 原创
：  【JS逆向百例】某江 Hospital 逆向分析

# 【JS逆向百例】某江 Hospital 逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近又有小伙伴在逆向某网站的时候，碰到了点棘手的问题，过来询问 K 哥。经过分析，该网站既有加密参数，又使用了 WebSocket 协议来传输数据，正好可以丰富 JS 逆向百例专栏。本文将对其进行逆向分析，仅作为学习研究：

### 逆向目标

### 逆向过程

#### 抓包分析

打开开发者人员工具，刷新网页，会发现被断住了，经典的无限 debugger。不过，如果直接在 debugger 处，右键选择 Nerver pause here（永不在此处暂停），下步断点后，能正常抓到包，以为绕过了，但是当你调试的时候，再次刷新页面，就会发现，页面卡死，一直转圈圈：

向上跟栈看看，这里构造了一个 debugger 函数：

这部分代码，简单解混淆优化后，代码如下：

```
function S(t) {
    function s(t) {
        if (false) {
            return function (t) {
            }["constructor"]("while (true) {}")["apply"]("counter");
        }  // 永不执行
        ("" + (t / t))["length"] !== 1 || t % 20 === 0 ? function () {
            return !0;
        }["constructor"]("debugger")["call"]("action") : function () {
            return !1;
        }["constructor"]("debugger")["apply"]("stateObject"),
            s(++t);
    }

    try {
        if (t) {
            return s;
        }
        s(0);
    } catch (t) {
    }
}

```

这段代码的逻辑就是通过递归调用，和一些判断条件（如 `t` 是 `20` 的倍数时）来不断的触发 `debugger` 语句，使得 JavaScript 调试器被不断的激活，阻止正常的执行流程。

接着向上跟栈，看看哪调用了这个函数，跟到最后会发现，有个定时器 setInterval 每 4000 毫秒（4 秒）就执行一次 S 函数，这就实现了所谓的 `无限 debugger`：

```
setInterval((function () {
        ({
            rXNsL: function (t) {
                return t()
            }
        })["rXNsL"](S)
    }
), 4000)

// setInterval(function () {
//     S();  // 每 4 秒执行一次 S 函数
// }, 4000);

```

这个站的无限 debugger 较为普通，直接替换、改写，或者 hook 都可以，以下提供几个 hook 脚本，以供参考：

```
// ------------------- 1 -----------------------
Function.prototype.constructor = function(){}

// ------------------- 2 -----------------------
Function.prototype.constructor_ = Function.prototype.constructor;
Function.prototype.constructor = function (a) {
    if(a == "debugger") {
        return function (){};
    }
    return Function.prototype.constructor_(a);
};

// ------------------- 3 -----------------------
// 断到 s 函数处，将执行函数置空
function s(){}

```

或者直接使用火狐（Firefox）浏览器，具体操作，可参考 K 哥往期文章：

> 
通杀无限 debugger，目前只有 1% 的人知道：https://mp.weixin.qq.com/s/KQBn1C3ejlZ2Gbfs6k02ew


方法还有很多，就不一一列举了。

过掉之后，就能正常抓到包了，网页中的公告相关数据，直接 ctrl + f 搜索，是找不到的，翻了一会，看到一个很特别的接口，Type 为 websocket，那么是否可能是通过 websocket 协议传输的数据呢？

点到接口中，查看一下接收到的相关数据帧，筛选 Receive，简单查看后会发现，大部分文本内容都在 textContent 字段中，且是 URL 编码后的结果。

我们可以找个大点的数据帧，Copy as Base64 到 K 哥工具站中，再将页面中某一公告标题的文本，进行 URL 编码后，看能否搜索到对应的内容：

```
# 样例
%E4%B9%9D%E6%B1%9F%E5%B8%82%E7%AC%AC%E4%B8%80%E4%BA%BA%E6%B0%91%E5%8C%BB%E9%99%A2%E5%8C%BB%E7%94%A8%E7%94%B5%E5%8A%A8%E9%97%A8%E7%BB%B4%E4%BF%9D%E6%9C%8D%E5%8A%A1%E9%A1%B9%E7%9B%AE%E8%AF%A2%E4%BB%B7%E5%87%BD

```

> 
Base64 编码解码：https://www.kgtools.cn/secret/base64


成功找到了我们想要的文本数据，证明确实是通过 websocket 协议传输的关键数据，当然 hook 跟栈分析，也能验证。

接下来，先简单分析下这个 wss 接口，其构成如下：

```
wss://xxx.cn/1ywuKELSO2ahQuWZ/pr/Tifz8hd5p4O3AB%2BivrbJpGEutslSMrspRrA33vaPAp0%3D/b/ws/svmlr9q1rk/8f3effd8-0639-40f9-a4e6-9d19a82cbcc9

```

以这个链接为例，动态变化的，主要是以下这三个部分：

接下来看看 `/api/v1/sessions` 接口，其请求参数和响应内容，都经过了加密处理：

#### 逆向分析

先来看看 sessions 接口的加密参数是如何生成的，清空缓存，刷新网页，跟栈，从 `e.sessionData` 跟到 `app.07b0b337.js` 文件中，代码未经过混淆处理：

该处创建了一个 `Promise` 对象，往上跟，会发现，h 就是 post 请求中，data 参数的加密结果：

```
h = w["encryptSessions"](JSON["stringify"](T))

```

先将 T 转为字符串，然后再加密得到的结果，T 就定义在 new Promise 上方，包含了 uuid、cid、userAgent 等环境参数：

往上，就能跟踪到各自定义的位置：

简单分析下其中几个，uuid，对应 cookie 中的 `FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt` 参数的值：

common 中的 tabId 对应 `window.__wm_tab_id__`，可以写成固定值：

cid 也并非定值，断到上面对应的 a 参数的定义处，此时 cid 的值已经生成了，跟到函数中去：

可以看到，是从浏览器的 `localStorage` 获取已存储的数据：

那么是何时进行 `localStorage.setItem('uuid', 'xxx')` 操作的呢？

清空缓存，重新刷新网页，再次断到此处时，会发现此时的 h 为 null，下面 return 处有个简单的判断，检查 h 参数是否已经被赋值了，若没有，就赋值，然后进行 `localStorage.setItem` 操作：

```
return h || (h = this["_getUuid"](), localStorage["setItem"]("uuid", h), h)

```

跟到中去后，解混淆后的算法如下，就是将随机浮点数转换成基数为 36 的字符串，然后取后 8 位字符得到的 cid 参数的值：

```
Math["random"]()['toString'](36)["slice"](-8);

```

`_` 就是 userAgent、| 与 cid 拼接而成。

接下来，看看请求参数 data 是通过何种加密算法生成的：

```
var h = w["encryptSessions"](JSON["stringify"](T))

```

跟进到 `w["encryptSessions"]` 中去，生成位置如下：

```
return this['_dynamicEncrypt'](t, this['priKey'], this.iv);

```

有 key 和 iv，大致知道可能是哪些算法了，key 为固定值，`this.iv` 定义在上面，从索引 1 到 17 切割字符串 a 后得到的值，与 sessions 接口请求头中的 etag 值一致：

```
this.iv = a["substring"](1, 17)

```

a 字符串的生成方式如下，可以看到，和 data 参数一样，都是经过 `this["_dynamicEncrypt"]` 算法加密得到的，b、y 为固定值：

```
var o = Math["random"]()["toString"](36)["slice"](-8) + "-" + Math["random"]()["toString"](36)["slice"](-8) + (new Date)["getTime"]();
var a = this["_dynamicEncrypt"](o, b, y)["replace"]("_", "");

```

接着跟进到 `this['_dynamicEncrypt']` 函数中去，看到了熟悉的 `aes-128-cbc`：

到 K 哥工具站，验证一下，看看是否为标准的 AES 加密算法：

> 
AES 加解密：https://www.kgtools.cn/secret/aes


结果一致：

请求参数 data 的加密算法与 `this.iv` 一致，接下来，构造 websocket 请求即可。

### WebSocket

WebSocket 是一种网络通信协议，用于在客户端（如浏览器）和服务器之间建立持久的双向通信通道。

它于 2011 年成为标准（RFC 6455）。与传统的 HTTP 请求-响应模型不同，WebSocket 允许实时的、全双工的数据传输，适合需要高频数据交互的应用场景。

#### WebSocket 的特点

#### WebSocket 工作原理
<li> **握手（Handshake）**：
 示例： <pre><code>GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Version: 13
</code></pre> 服务器响应： <pre><code>HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
</code></pre> </li><li> **数据传输**：
 </li><li> **关闭连接**：
 </li>
对比一下本站的 wss 接口看看，很标准，`sec-websocket-extensions` 代表该 WebSocket 添加了扩展功能：

`Sec-WebSocket-Key` 是由客户端随机生成的一个 16 字节（随机生成的 base64 编码字符串），可以固定。

`Sec-WebSocket-Version` 是客户端在握手请求中声明的协议版本号，用于告诉服务器自己支持的 WebSocket 版本。本站使用的是主流版本 13，13 是 WebSocket 协议 RFC 6455 的正式版本。

#### WebSocket 和 HTTP 的区别

#### 构造 WebSocket 请求

Python 实现 WebSocket 客户端可以使用以下两种常用方式：
1. 同步实现：使用 `websocket-client` 库（import websocket）；1. 异步实现：使用 `websockets` 库（import websockets）。
`websocket-client` 与 `websockets` 库的区别：

这两个库各自实现 WebSocket 客户端的方式如下：

默认情况下，websockets 库会自动生成符合规范的 WebSocket 握手请求头，包括 `Sec-WebSocket-Version` 和 `Sec-WebSocket-Key`，用户可以通过传递自定义头覆盖默认行为，例如通过 extra_headers 参数，headers 为字典格式（手动添加 Key 或 Version，可能会导致握手失败）：

```
import asyncio
import websockets

async def websocket_client():
    url = "wss://example.com/socket"
    
    # 添加请求头
    headers = {
        "User-Agent": "MyCustomUserAgent/1.0",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Custom-Header": "CustomValue"
    }
    
    async with websockets.connect(url, extra_headers=headers) as websocket:
        await websocket.send("Hello!")
        response = await websocket.recv()
        print(response)

asyncio.run(websocket_client())

```

和 `websockets` 不一样的是， `websocket-client` 传入的 headers 为列表格式（Header: Value），若传入的 headers 是字典格式，库会自动转换为列表格式：

```
import websocket

headers = [
    "User-Agent: MyCustomUserAgent/1.0",
    "Authorization: Bearer YOUR_ACCESS_TOKEN",
    "Custom-Header: CustomValue"
]

# WebSocket URL
wss_url = "wss://example.com/socket"

# 创建 WebSocketApp 并添加自定义头
ws = websocket.WebSocketApp(
    wss_url,
    header=headers,  # 添加自定义请求头
    on_open=lambda ws: print("Connection opened"),
    on_message=lambda ws, msg: print(f"Received message: {msg}"),
    on_close=lambda ws, close_status_code, close_msg: print("Connection closed")
)

# 运行 WebSocket 客户端
ws.run_forever()

```

按需选择合适的 websocket 库发送请求即可。

### 结果验证
