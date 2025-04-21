# 原创
：  【JS逆向百例】某赚网 WebSocket 套 Webpack 逆向分析

# 【JS逆向百例】某赚网 WebSocket 套 Webpack 逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

近期有粉丝私信，提到了某网站抓不到包的问题，之前还有不少新手粉丝提到不会 webpack。经过分析，发现这个网站属于 ws 协议，同时还是一个简单的 webpack，正好借此案例，解答粉丝们的疑惑：

### 逆向目标

### 抓包分析

进入首页，随机选择某个商品点击接单，然后进入订单列表，会发现有不同的订单在一直刷新，会发现 `/GetPendingOrderStatus` 这个数据包在不断的下发：

同时该数据是密文状态，经过断点调试发现这个接口并不是我们需要的，那么它的数据应该是从何而来呢？大胆猜测应该是走了不同的协议，因为这种实时获取数据的接口，一般大概率都是走的 ws 协议， 避免了每次通信都需要重新建立连接的开销。

再次刷新列表页，我们发现有一个 ws 通信的数据包 `/api/market`：

同时在消息接收里面，不断加载服务器给我们返回的消息，同样这个消息也是密文的状态，大胆猜测这个应该就是我们需要的列表数据：

其中协议头中的参数，是 ws 特有的：

完成握手以后，WebSocket 协议就在 TCP 协议之上，开始传送数据。

### WebSocket 回顾

关于 WebSocket 在往期文章有过介绍，不过时间久远，可能部分新粉不知道：

#### 协议对比

##### HTTP

##### WebSocket

#### 连接方式对比

##### HTTP

##### WebSocket

简单一句话总结，就是 WS 是长连接，HTTP 是短连接。

### 逆向分析

#### WebSocket 流程分析

再次刷新页面，按下 F12 选择 ws 选项，可以看到有关 WebSocket 协议的发包：

进入堆栈查看，从第一个堆栈进入：

我们找到 initWebSocket 与 websocketonopen 的地方：

我们发现在调用 open 建立连接时，会向服务器发送一段 `y.a.encryptDes(r()(t))` 数据，所以我们构造这个 ws 请求就必须完成里面加密参数的生成。

#### 参数加密分析

上面分析可知，ws 向服务器发送了一段密文数据，该数据是由 `y.a.encryptDes` 生成的，所以我们需要将 y 函数导出，经过分析 y 是一个 webpack 打包的一个模块：

在该处打上断点，重新刷新列表页，成功在此断住，还是进入 a 中将分发器扣下来，导出到 windows：

```
window = global;
!function(e) {
    var f = window.webpackJsonp;
    window.webpackJsonp = function(c, b, n) {
        for (var r, t, o, i = 0, u = []; i &lt; c.length; i++)
            t = c[i],
            a[t] &amp;&amp; u.push(a[t][0]),
            a[t] = 0;
        for (r in b)
            Object.prototype.hasOwnProperty.call(b, r) &amp;&amp; (e[r] = b[r]);
        for (f &amp;&amp; f(c, b, n); u.length; )
            u.shift()();
        if (n)
            for (i = 0; i &lt; n.length; i++)
                o = d(d.s = n[i]);
        return o
    }
    ;
    var c = {}
      , a = {
        113: 0
    };
    function d(f) {
        if (c[f])
            return c[f].exports;
        var a = c[f] = {
            i: f,
            l: !1,
            exports: {}
        };
        console.log(f)
        return e[f].call(a.exports, a, a.exports, d),
        a.l = !0,
        a.exports
    }window.kk=d;
    d.e = function(e) {
        var f = a[e];
        if (0 === f)
            return new Promise(function(e) {
                e()
            }
            );
        if (f)
            return f[2];
        var c = new Promise(function(c, d) {
            f = a[e] = [c, d]
        }
        );
        f[2] = c;
        var b = document.getElementsByTagName("head")[0]
          , n = document.createElement("script");
        n.type = "text/javascript",
        n.charset = "utf-8",
        n.async = !0,
        n.timeout = 12e4,
        d.nc &amp;&amp; n.setAttribute("nonce", d.nc),
        n.src = d.p + "static/js/" + e + "." + {
            0: "8400f3beade260525146",
        }[e] + ".js";
        var r = setTimeout(t, 12e4);
        function t() {
            n.onerror = n.onload = null,
            clearTimeout(r);
            var f = a[e];
            0 !== f &amp;&amp; (f &amp;&amp; f[1](new Error("Loading chunk " + e + " failed.")),
            a[e] = void 0)
        }
        return n.onerror = n.onload = t,
        b.appendChild(n),
        c
    }
    ,
    d.m = e,
    d.c = c,
    d.d = function(e, f, c) {
        d.o(e, f) || Object.defineProperty(e, f, {
            configurable: !1,
            enumerable: !0,
            get: c
        })
    }
    ,
    d.n = function(e) {
        var f = e &amp;&amp; e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return d.d(f, "a", f),
        f
    }
    ,
    d.o = function(e, f) {
        return Object.prototype.hasOwnProperty.call(e, f)
    }
    ,
    d.p = "/",
    d.oe = function(e) {
        throw console.error(e),
        e
    }
}({})

```

将我们所需的 u46b 模块找到，还是将断点断在 ` return e[f].call(a.exports, a, a.exports, d)` 处，控制台输出 `e["u46b "]` 即可找到相关模块的位置。

自动扣 webpack 可以在分发器的位置断住，将分发器改写为：

```
window.code = '';
a=function (c) {
        if (f[c])
            return f[c].exports;
        var d = f[c] = {
            i: c,
            l: !1,
            exports: {}
        };
        console.log(c)
window.code += c + ':' + e[c] + ',\r\n'
        return e[c].call(d.exports, d, d.exports, a),
        d.l = !0,
        d.exports
    }

```

全部流程走完以后，复制 window.code 即可将全部模块导出，最后运行发现报错，提示语法错误：

经过分析可知，源码中模块的命名存在不规范的情况，如果我们直接引用的话就会报语法错误：

<img alt="7xCmI4.jpg" src="https://img-blog.csdnimg.cn/img_convert/ccf179abaead367d1a12a106055b581d.jpeg"/><br/> <img alt="7xCL0h.jpg" src="https://img-blog.csdnimg.cn/img_convert/60298fbbdf02bbd5a5333b3c35687ad1.jpeg"/>

那么我们自动扣 webpack 的脚本就需要修改一下，修改后代码如下：

```
window.code = '';
a=function (c) {
        if (f[c])
            return f[c].exports;
        var d = f[c] = {
            i: c,
            l: !1,
            exports: {}
        };
        console.log(c)
window.code += '"' + c + '"' + ':' + e[c] + ',\r\n'
        return e[c].call(d.exports, d, d.exports, a),
        d.l = !0,
        d.exports
    }

```

不懂的小伙伴可以参考往期文章，<a>【JS逆向百例】某点数据逆向分析，多方法详解</a>，最终效果如下：

### Python 实现 WebSocket 请求

#### 创建 WebSocket 连接

```
import websocket

# 创建 WebSocket 连接
ws = websocket.WebSocket()
ws.connect("wss://example.com")

```

#### 发送连接请求

```
import websocket

# 创建 WebSocket 连接
ws = websocket.WebSocket()
ws.connect("wss://example.com")

# 发送连接请求
ws.send("************************")

```

#### 处理响应数据

```
import websocket

# 创建 WebSocket 连接
ws = websocket.WebSocket()
ws.connect("wss://example.com")

# 发送连接请求
ws.send("*************************")

# 接收和处理响应数据
while True:
    response = ws.recv()
    if response:
        print(response)
        # 在这里添加对响应数据的处理逻辑
    else:
        break

```

而我们这个案例向服务器 send 数据建立连接的时候需要发送密文数据，同时不断接收服务器返回的数据也是密文数据，所以我们需要在此基础上进行修改。

经过测试发现，当 send 内容错误，服务器依旧可以给我们返回数据，但是间隔时间很长，且数据内容都一致，没有列表数据：

只有完美构造 send 参数，我们才会接收到完整的数据，所以这可以用来检验我们的参数构造是否正确：

最终代码如下：

```
import execjs
import asyncio
import websockets

from loguru import logger

with open('pack.js', 'rb') as f:
    js = f.read().decode()
ctx = execjs.compile(js)

def des_decrypt(word):
    decode_word = ctx.call('des_decrypt', word)
    return decode_word

def des_encrypt(word):
    encode_word = ctx.call('des_encrypt', word)
    return encode_word

async def hello():
    url = "ws://脱敏处理"
    headers = {}
    async with websockets.connect(url, extra_headers=headers.items()) as websocket:
        encrypt_msg = Des_encode(word)
        # encrypt_msg="12345678900000000000000000000000"
        await websocket.send(encrypt_msg)
        while True:
            response = await websocket.recv()
            logger.success(f"密文:{response},明文:{des_decrypt(response)}")

asyncio.get_event_loop().run_until_complete(hello())

```
