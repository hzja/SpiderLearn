# 原创
：  【JS 逆向百例】吾爱破解2022春节解题领红包之番外篇 Web 中级题解

# 【JS 逆向百例】吾爱破解2022春节解题领红包之番外篇 Web 中级题解

> 
关注微信公众号：K哥爬虫，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 逆向目标

本次逆向的目标来源于吾爱破解 2022 春节解题领红包之番外篇 Web 中级题，吾爱破解每年都会有派送红包活动（送吾爱币），需要大家使出看家逆向本领来分析内容获得口令红包，今年一共有五个题，一个送分题，两个 Windows 题、一个 Android 题和一个 Web 题，本文分析的正是 Web 题，**吾爱有规定活动结束前不要外泄口令、讨论分享分析过程，所以本文在活动结束后才发出来。**

此 Web 题题目是：小 D 最爱看的视频网站最近关站了，关站前他用 Fiddler 和 Web Archive 保存了一位主播的视频，但他发现存下来的文件无法播放。你能帮小 D 找回他的回忆吗？（.saz 与 .wacz 任选其一即可解题）

为防止吾爱后期关闭解题通道，K哥将 .saz 和 .wacz 文件保存了一份，可在公众号后台回复**吾爱破解**获取！

### HLS 流媒体传输协议

本题涉及到 HLS 流媒体传输协议，先简单介绍一下，了解的同志可直接跳过。

HLS 全称 HTTP Live Streaming，即基于 HTTP 的自适应码率流媒体传输协议，是苹果研发的动态码率自适应技术，它包括一个 M3U(8) 的索引文件，若干 TS 视频流文件，如果视频流文件是加密的，那就还会存在一个 key 加密串文件。

M3U8 文件是 M3U 的一种，只不过文件中存储的文本使用 UTF-8 字符编码，在极少数情况下，M3U8 文件可能会以 M3UP 扩展名保存。M3U8 文件是各种音频和视频播放程序使用的播放列表文件，它包含了媒体文件或媒体文件夹的路径或 URL，以及有关播放列表的相关信息。

TS 全称为 MPEG2-TS，TS 即 Transport Stream 传输流，又称 MPEG-TS、MTS、TP，这种格式的特点就是从视频流的任一片段开始都是可以独立解码的。

针对 TS 格式的文件，如果是未加密的，一般的播放器就能够直接播放，也可以使用 FFmpeg 等工具转换为其他格式，FFmpeg 也可以直接处理 M3U8 文件，自动解密合并转换 TS 文件，当然也有其他大佬写好的小工具，拖入 M3U8 文件就直接给你处理好了。

M3U8 文件内容的大致格式示例如下：

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-ALLOW-CACHE:YES
#EXT-X-KEY:METHOD=AES-128,URI="https://www.example.com/m3u8.key"
#EXT-X-TARGETDURATION:5
#EXTINF:4.200000,
https://www.example.com/hls/live_00000.ts
#EXTINF:4.166667,
https://www.example.com/hls/live_00001.ts
#EXTINF:3.600000,
https://www.example.com/hls/live_00002.ts
#EXTINF:2.516667,
https://www.example.com/hls/live_00003.ts
#EXTINF:4.166667,
https://www.example.com/hls/live_00004.ts
#EXTINF:4.166667,
https://www.example.com/hls/live_00005.ts
#EXTINF:4.166667,
https://www.example.com/hls/live_00006.ts
#EXTINF:1.716667,
https://www.example.com/hls/live_00007.ts
#EXT-X-ENDLIST

```

各标签含义如下：

完整格式、标准标签可参考 HLS 标准协议中，对 Playlist file 的介绍：https://datatracker.ietf.org/doc/html/draft-pantos-http-live-streaming-08

### SAZ 分析

在 Fiddler 软件中，使用 SAZ 格式用来保存和读取 HTTP/HTTPS 请求信息，打开该文件可以注意到一些重要的请求：script.bundle.js、live.m3u8、drm 以及八个 ts 视频流文件。

先来看看 m3u8 文件，可以看到是 AES-128 加密，加密的 key 文件地址为 `key://live`，如下图所示：

一般情况下，要想解密 ts，必然会去请求 key 的地址，拿到 key 后再解密 ts，很显然此题的 key 地址不是一个合法的 URL 地址，当然此题的抓包记录可能是出题人伪造的，因为这个 Host 是 52tube.mmxxii，也不是一个合法的域名，最主要的是，抓包记录里没有 `key://live` 这条请求，那么很大概率真实的地址隐藏在 JS 里，从另一个方面来思考，如果这是完整的抓包记录，不管真实的 key 地址是啥，必然会在记录里出现！

有经验的朋友应该一眼就能看出来 drm 这条请求最有可能是拿 key 的操作了，第一是 drm 这个关键词在 ts 解密里经常会出现，搞得多的朋友应该见过不少，第二 ping 请求返回的 success，通过其名称和返回值来看也不像 key，剩下就只有 drm 了，查看返回值是乱码的，查看 Hex 值，32 位 16 进制数据，而正常的 key 应该是 16 位 16 进制数据，所以你如果直接拿这个数据当作 key 去解密，肯定也是失败的。

到这里我们应该有如下猜想：drm 返回的数据，经过了 script.bundle.js 二次处理就能得到正确的 key。

### JS 逆向

我们把抓包记录的 script.bundle.js，右键，save - response - response body，保存到本地。

格式化之后有 15000+ 行代码，又不能动态调试，从哪里找加密入口呢？可以大胆尝试一下：

通过搜索可以发现如下可疑代码片段：

将关键代码提炼一下：

```
function n(t) {
    return [...new Uint8Array(t)].map((t =&gt; t.toString(16).padStart(2, "0"))).join("")
}

function s(t, e) {
    let r = new Uint8Array(t.length);
    for (let i = 0; i &lt; t.length; i++) r[i] = t[i] ^ e[i];
    return r
}

let e = "/api/ping/",
    i = "/api/drm/";

class a extends t.DefaultConfig.loader {
    let e = await async function() {
        let t = new Uint8Array(16);
        crypto.getRandomValues(t);
        let e = n(t.buffer) + Date.now() + Math.random();
        return new Uint8Array((await async function(t) {
            const e = (new TextEncoder).encode(t);
            return await crypto.subtle.digest("SHA-256", e)
        } (e)).slice(0, 16))
    }();
    var r = new URLSearchParams;
    r.append("h", n(e.buffer)),
        r.append("id", t);
    var a = {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: r
    };
    let o = await fetch(i, a),
        l = await o.arrayBuffer();
    if (32 !== l.byteLength) throw new Error("Invalid response");
    let u = new Uint8Array(l.slice(0, 16)),
        c = new Uint8Array(l.slice(16, 32));
    return s(s(u, e), c)
}

```

可以看到事实上在发送 `/api/drm/` 请求拿到结果后，先后取前后 16 位数据，然后经过了 s 方法的处理，最后返回的 `s(s(u, e), c)` 应该才是正确的 key，这里的重点在于 e 的值，上面有个方法，取了当前时间+随机值，经过 SHA-256 加密，再取前 16 位。

这里可以思考一下，这个 e 的值是不固定的，那么最后的 key 应该也是不固定的，同一个 TS 对应有无数个 key，我反正是没见过，不信的话尝试就用那个方法生成 e，你会发现最终的 key 是错误的。

仔细看一下，发送 post 请求对 h 值赋值的地方：`r.append("h", n(e.buffer))`，n 方法是转 16 进制，那么我们直接将 h 值倒推，从16进制转为10进制，这才是正确的 e 的值！然后 l 的值是 `/api/drm/` 请求返回的 32 位 16 进制数据转为 10 进制，剩下的就好说了，直接改写一下 JS 代码拿到正确的 key：

```
function s(t, e) {
    let r = new Uint8Array(t.length);
    for (let i = 0; i &lt; t.length; i++)
        r[i] = t[i] ^ e[i];
    return r
}

function getKey(){
    // /api/drm/ 请求表单的 h 值，16进制数据
    const h = ["7b", "10", "31", "1e", "6e", "31", "0f", "0d", "f0", "68", "d9", "ed", "e1", "04", "75", "a8"];
    // /api/drm/ 请求返回的32位16进制数据
    const drm = ["08", "A5", "E6", "C2", "C2", "61", "A8", "AC", "B4", "D7", "9C", "49", "AF", "16", "0A", "3A", "DA", "4E", "5C", "EA", "E1", "6F", "ED", "46", "EB", "6F", "49", "8C", "9B", "63", "D5", "3B"]
    // 转换为10进制数据，为 e 和 l 赋值
    const e = [];
    const l = [];
    for (let i=0; i&lt;h.length; i++)
    {
        e.push(parseInt(h[i],16))
    }
    for (let i=0; i&lt;drm.length; i++)
    {
        l.push(parseInt(drm[i],16))
    }

    const u = new Uint8Array(l.slice(0, 16));
    const c = new Uint8Array(l.slice(16, 32));

    const keyArray = s(s(u, e), c);
    const keyHex = new Buffer.from(keyArray).toString('hex');
    const keyBase64 = new Buffer.from(keyArray).toString('base64');

    console.log("keyArray: ", keyArray)
    console.log("keyHex: ", keyHex)
    console.log("keyBase64: ", keyBase64)
}

getKey()

// 输出
// keyArray:  Uint8Array(16) [
//   169, 251, 139,  54,  77,
//    63,  74, 231, 175, 208,
//    12,  40, 213, 113, 170,
//   169
// ]
// keyHex:  a9fb8b364d3f4ae7afd00c28d571aaa9
// keyBase64:  qfuLNk0/Suev0Awo1XGqqQ==

```

### TS 解密合并转换

通过 JS 逆向我们拿到了 16进制和 base64 形式的 key，不管什么形式都可以拿来解密，这里介绍两种对 TS 媒体流解密、合并、转换的方法。

第一种方法是使用 FFmpeg 工具，FFmpeg 是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。官网地址：https://ffmpeg.org/ ，下载编译好的程序，将 bin 目录添加到环境变量即可，该工具也可以直接在K哥爬虫公众号后台回复 M3U8 获取。

首先我们要把 m3u8 文件和 ts 媒体流保存到同一个文件夹，由于是虚假的 Host，所以不能直接浏览器访问保存，可以直接在 Fiddler 里，右键，save - response - response body，保存到本地，如下图所示：

然后就是保存密钥文件，这里要求密钥文件必须是16进制的数据，如果你直接将 key 以字符串形式保存的话，解密也是失败的，编辑 16 进制文件有专门的工具，比如 HxD、010 editor、winhex 等，以 HxD 为例，新建文件，写入我们前面通过 JS 逆向得到的 key 的 16 进制数据，存为 .key 文件，如下图所示：

然后修改 m3u8 文件里 key 的地址、名称，建议将 key、m3u8、ts 文件都放同一个文件夹，这样 m3u8 文件里就不用添加资源路径了，不容易出错。

然后在当前文件夹，打开命令行输入命令：`ffmpeg -allowed_extensions ALL -i live.m3u8 -c copy live.mp4`，即可自动解密 ts，并合并转换为 .mp4 格式：

第二种方法就是使用大佬写的第三方小工具，这里推荐吾爱大佬逍遥一仙写的 M3U8 批量下载器，下载地址、使用方法见原贴：https://www.52pojie.cn/thread-1374045-1-1.html ，也可以在K哥爬虫公众号后台回复 M3U8 获取。

我们可以直接拖入处理好的 M3U8 文件，自动处理：

也可以选择其他 - 工具 - 合并助手，添加所有 TS 文件，输入 key 后自动处理：

处理完毕后的 mp4 文件默认在软件目录的 output 文件夹里面，解密后是一段动画，往后看会找到 flag：`flag{like_sub_52tube}` 为正确答案。

<img alt="16" src="https://i-blog.csdnimg.cn/blog_migrate/bcd7b5226bb50cd8a603598366b743b2.png"/><br/> <img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/40d8772cafcdb31fff6083592add9d7d.png"/>
