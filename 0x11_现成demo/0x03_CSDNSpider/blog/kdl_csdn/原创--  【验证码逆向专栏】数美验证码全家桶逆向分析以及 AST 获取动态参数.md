# 原创
：  【验证码逆向专栏】数美验证码全家桶逆向分析以及 AST 获取动态参数

# 【验证码逆向专栏】数美验证码全家桶逆向分析以及 AST 获取动态参数

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 目标

```
// 官网体验地址
aHR0cHM6Ly93d3cuaXNodW1laS5jb20vdHJpYWwvY2FwdGNoYS5odG1s
// 官方隐藏地址
aHR0cHM6Ly9jYXN0YXRpYy5mZW5na29uZ2Nsb3VkLmNuL3ByL3YxLjAuNC9kZW1vLmh0bWw=
// 某红书验证页面
aHR0cHM6Ly93d3cueGlhb2hvbmdzaHUuY29tL3dlYi1sb2dpbi9jYXB0Y2hh
```

数美不同类型验证码核心的 JS 都是一样的，只是个别参数有微小差别，主要以滑块为例来分析，通过 JS 代码以及官方文档可以看出数美是有无感验证的，但是官网体验地址里并没有放出来，官方有一个隐藏地址，里面的 demo 是最全的，包括无感，可以去上面给出的第二个地址里查看；数美的加密参数包含了 DES 加密算法，参数名以及 DES Key 不定时会变化，本文也会分析如何利用 AST 来获取动态的参数。

### 抓包分析

`conf` 接口，获取配置，主要是获取核心的 `captcha-sdk.min.js` 的地址，请求参数解释：

|参数|含义
|------
|`organization`|数美分配的公司标识，一般是每个网站唯一，写死即可
|`appId`|应用标识，区分不同应用，数美后台可以管理
|`callback`|回调参数
|`lang`|语言，`zh-cn` 简体中文、`zh-tw` 繁体中文、`en` 英文
|`model`|模式，`slide` 滑块、`auto_slide` 无感验证、`select` 文字点选、`icon_select` 图标点选、`seq_select` 语序点选、`spatial_select` 空间推理
|`sdkver`|这个 sdk 版本是 `captcha-sdk.min.js` 内部写死的
|`channel`|推广渠道，数美后台可以管理
|`captchaUuid`|32位随机字符串，与业务方自身埋点数据配合，便于后续定位问题或进行数据统计
|`rversion`|`captcha-sdk.min.js` 版本号

返回结果重点看 `captcha-sdk.min.js` 文件地址，如下图所示有个 `v1.0.4-171`，本文中我们称 `v1.0.4` 为大版本，`171` 为小版本，小版本不定时会更新，版本号不断升高。

然后就是 `register` 接口，不同类型，返回的数据都大同小异，其中 `bg` 是背景图片，`fg` 是滑块，文字点选、空间推理中 `order` 是提示信息，`k`、`l`、`rid` 三个参数后续会用到。

最后就是 `fverify` 验证接口，有类似下图红框中的 12 个参数，都是通过 JS 生成的，其参数名会根据 `captcha-sdk.min.js` 的变化而变化，其中有个最长的类似于下图的 `ep` 值，包含了轨迹加密。返回值里参数解释：

|参数|含义
|------
|`code`|`1100`：成功；`1901`：QPS超限；`1902`：参数不合法；`1903`：服务失败；`9101`：无权限操作
|`riskLevel`|处置建议，`PASS`：正常，建议直接放行；`REJECT`：违规，建议直接拦截

### 逆向分析

跟栈会发现核心逻辑在 `captcha-sdk.min.js` 里，这个 JS 类似于 OB 混淆（以前的文章介绍过，此处不再细说）：

这里可以自己写 AST 还原一下，为了方便我们直接使用 v_jstools 解混淆：

然后替换掉原来的 `captcha-sdk.min.js`，如果你测试的是官网的体验页面，使用 Fiddler 替换时要注意可能有跨域问题，需要利用 Filters 功能，设置响应头 `Access-Control-Allow-Origin` 字段值为当前域名：

如果你没注意到这个跨域问题，可能会替换之后发现没替换成功，原因是数美的资源有四个域名，其中一个宕了便会启用另一个，你替换其中一个报错了就会自动跳转另一个，所以看起来你并没有替换成功：

**PS：若替换的 JS 格式化了，那么你在网页上滑动也是校验失败的，因为 JS 里检测了格式化，将 JS 压缩成一行再替换即可，具体检测的位置后文会讲到。**

#### captchaUuid

直接搜索关键词下断点，经过多次调试会发现第一个出现 `captchaUuid` 的地方是在 `smcp.min.js`，如下图所示：

这里的栈并不多，来回跟栈也没发现是哪里生成的，此时可以从初始位置也就是 `embed.html` 初始化验证码的地方开始单步跟：

单步跟进去会发现一个 `getCaptchaUuid()` 的方法，将此方法扣出来即可。

```
function generateTimeFormat() {
    var e = new Date()
    , t = function(n) {
        return +n &lt; 10 ? "0" + n : n.toString();
    };
    return ((e.getFullYear().toString() + t(e.getMonth() + 1)) + t(e.getDate()) + t(e.getHours()) + t(e.getMinutes())) + t(e.getSeconds());
}

function getCaptchaUuid() {
    var c = "";
    var o = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678";
    var s = o.length;
    for (var a = 0; a &lt; 18; a++) {
        c += o.charAt(Math.floor(Math.random() * s));
    }
    return generateTimeFormat() + c;
}
```

#### 12 个加密参数

直接跟栈就很容易找到，如下图所示的位置，D 就是生成的所有参数，此外，也可以通过搜索关键字 `getEncryptContent` 或者直接搜索参数名称来定位。

可以发现上图里就有四个加密参数，都用到了 `getEncryptContent` 这个加密方法，加密方法传入两个参数，一个是待加密参数，一个是 DES Key，这四个待加密参数分别为 `appId` 值、`channel` 值、`lang` 值和一个 `getSafeParams` 方法。

重点跟进 `getEncryptContent` 方法看看，一个控制流，挑几个重点的讲一下，第一步是获取一个 `key`，这个 `key` 是在前面设置的，后续会讲到，实际上这个 `key` 没啥用。

然后会有一个 `isJsFormat` 的格式化检测函数，正常应该是 false 的，如果你格式化了就为 true，也就会导致 f 的值为时间戳加数美的域名，这个 f 值后续是 DES 的 Key，不对的话自然怎么滑都不会通过。

然后就是 DES 加密了，这个 DES 是标准的加密算法，下图中传入的 1 和 0 表示的是加密，0 和 0 则表示解密，解密的情况也有，后续会遇到，`mode` 为 `ECB`，`padding` 为 `ZeroPadding`，不需要 `iv`，可以直接扣代码，或者直接引库即可。

```
var CryptoJS = require("crypto-js")

function DESEncrypt(key, word) {
    var key_ = CryptoJS.enc.Utf8.parse(key);
    var srcs = CryptoJS.enc.Utf8.parse(word);
    var encrypted = CryptoJS.DES.encrypt(srcs, key_, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.ZeroPadding
    });
    return encrypted.toString();
}

function DESDecrypt(key, word) {
    var key_ = CryptoJS.enc.Utf8.parse(key);
    var decrypt = CryptoJS.DES.decrypt(word, key_, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.ZeroPadding
    });
    return decrypt.toString(CryptoJS.enc.Utf8);
}
```

这里的四个值就分析完了，还有八个值是在前面生成的，如下图所示 x 的值即为其他八个值，往前看是一个函数生成的，往里面跟即可。

跟进来是一个 `getMouseAction` 方法，里面先是挨个取值，后续会对这些值进行 DES 加密，下图中的 a、c 参数就是 `register` 接口返回的 k、l 值，s 参数是对 `register` 接口返回的 k 值进行解密操作：

上图中 `u = this._data` 里面的值，根据滑块、点选、无感模式的不同，也有所差异，以下代码中，以 `baseData` 来表示 `this._data` 的值，根据模式的不同，可分为三类，大致构成如下：

滑块（`slide`）：

```
/* 
track：滑动轨迹（x, y, t），distance：滑动距离，randomNum：生成两数之间的随机值，示例：
var track = [[0, -2, 0], [62, 1, 98], [73, 4, 205], [91, 3, 303], [123, -3, 397], [136, 8, 502], [160, 0, 599], [184, 0, 697], [169, 0, 797]]
var distance = 169
 */

var baseData = {}
baseData.mouseData = track
baseData.startTime = 0
baseData.endTime = track[track.length - 1][2] + randomNum(100, 500)
baseData.mouseEndX = distance
baseData.trueWidth = 300
baseData.trueHeight = 150
baseData.selectData = []
baseData.blockWidth = 40
```

滑块轨迹生成代码：

```
def get_sm_track(distance):
    track_length = random.randint(4, 10)
    track = [[0, -2, 0]]
    m = distance % track_length
    e = int(distance / track_length)
    for i in range(track_length):
        x = (i + 1) * e + m + random.randint(20, 40)
        y = -2 + (random.randint(-1, 10))
        t = (i + 1) * 100 + random.randint(-3, 5)
        if i == track_length - 1:
            x = distance
            track.append([x, y, t])
        else:
            track.append([x, y, t])
    logger.info("track: %s" % track)
    return track
```

点选类（文字点选 `select`、图标点选 `icon_select`、语序点选 `seq_select`、空间推理 `spatial_select`）：

```
/*
coordinate：点选坐标（x, y），randomNum：生成两数之间的随机值，示例：
var coordinate = [[171, 101], [88, 102], [138, 109], [225, 100]]
 */

var baseData = {}
var time_ = new Date().getTime()
coordinate.forEach(function(co) {
    co[0] = co[0] / 300
    co[1] = co[1] / 150
    co[2] = time_
    time_ += randomNum(100, 500)
})
baseData.mouseData = coordinate
baseData.startTime = time_ - randomNum(800, 20000)
baseData.endTime = coordinate[coordinate.length - 1][2]
baseData.mouseEndX = 0
baseData.trueWidth = 300
baseData.trueHeight = 150
baseData.selectData = coordinate
baseData.blockWidth = undefined
```

无感（`auto_slide`）：

```
/*
randomNum：生成两数之间的随机值
*/

var baseData = {}
baseData.mouseData = [[0, 0, 0]]
baseData.startTime = 0
baseData.endTime = randomNum(100, 500)
baseData.mouseEndX = 260
baseData.trueWidth = 300
baseData.trueHeight = 150
baseData.selectData = []
baseData.blockWidth = 40
```

这些值生成完了之后，就是挨个通过 `getEncryptContent` 进行加密，前面已经分析过，实际上就是 DES 加密，可以看到分为点选、滑块和无感三类，其中 DES Key 也是会每隔一段时间变化的：

再往下走还有三个加密参数，待加密值是定值，然后将 s 的值（也就是前面 `register` 接口返回的 k 经过 DES 解密后的值赋值给了 `this._data.__key`）。

至此所有加密参数就搞完了。

### 结果验证

### AST 获取动态参数

前面说了，`/v1.0.4-171/captcha-sdk.min.js` 文件地址，我们称 `v1.0.4` 为大版本，`171` 为小版本，小版本每隔一段时间会更新，版本号会不断升高，具体更新周期是多少？这里推荐一个方法 `document.lastModified`，该方法记录的是物理网页的最后修改时间，我们直接访问 JS 地址，就可以直接查看不同版本的 JS 是啥时候更新的了，多对比几个版本，发现更新间隔时间并没有太明显的规律，如下图所示：

不同版本里面的 12 个加密参数的名称和 DES 加密的 Key 都不一样，我们可以利用 AST 来动态获取这 12 个参数，经过测试，以下版本均可正常提取：

截止本文发布，小版本 `171` 为最新，`v1.0.4` 小版本从 `148` 开始，`v1.0.3`、`v1.0.1` 在 `147` 以前没有混淆，可自行正则匹配，暂未发现其他大版本，如有遇到不能适配的，可联系我瞅瞅，完整的代码在公众号 `k哥爬虫` 中，有需要的可以点击下方链接。 [【验证码逆向专栏】数美验证码全家桶逆向分析以及 AST 获取动态参数](https://mp.weixin.qq.com/s/uPqcS2GuMPJKUV5ngb7bGw)

**PS：此 AST 代码仅实现对动态参数的提取，并非还原所有的混淆，提取出来的结果是有序、未去重的，后续按索引取就行。**
