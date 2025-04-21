# 原创
：  【JS 逆向百例】医保局 SM2+SM4 国产加密算法实战

# 【JS 逆向百例】医保局 SM2+SM4 国产加密算法实战

> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


#### 文章目录

---


### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### 逆向过程

#### 抓包分析

来到公共查询页面，点击翻页，就可以看到一个 POST 请求，Request Payload 的参数部分是加密的，主要是 appCode、encData 和 signData 参数，同样返回的数据也有这些参数，其加密解密方法是一样的，其中 encType 和 signType 分别为 SM4 和 SM2，所以大概率这是国密算法了，有关国密算法 K 哥前期文章有介绍：[《爬虫逆向基础，认识 SM1-SM9、ZUC 国密算法》](https://mp.weixin.qq.com/s/IsoXn_jZI6YdqC7uXVDYiQ)，此外请求头还有 x-tif-nonce 和 x-tif-signature 参数，如下图所示：

#### 参数逆向

直接全局搜索 encData 或 signData，搜索结果仅在 app.1634197175801.js 有，非常明显，上面还有设置 header 的地方，所有参数都在这里，埋下断点，可以看到这里就是加密的地方，如下图所示：

这里的加密函数，主要都传入了一个 e 参数，我们可以先看一下这个 e，里面的参数含义如下：

等级代码、类型代码、所在地代码，都是通过请求加密接口得到的，他们的加密和解密方法都一样，在最后的完整代码里有分享，这里不再赘述。其他参数比如 appCode，是在 JS 里写死的。

我们再观察一下整个 JS 文件，在头部可以看到 .call 语句，并且有 exports 关键字，很明显是一个 webpack 形式的写法。

我们回到加密的地方，从上往下看，整个函数引用了很多其他模块，如果想整个扣下来，花费时间肯定是无比巨大的，如果想直接拿下整个 JS，再将参数导出，这种暴力做法可是可以，但是整个 JS 有七万多行，运行效率肯定是有所影响的，所以观察函数，将不用的函数去掉，有用的留下来，是比较好的做法，观察 function d，第一行 `var t = n("6c27").sha256`，点进去来到 createOutputMethod 方法，这里整个是一个 SHA256 算法，从这个方法往下整个 copy 下来即可，如下图所示：

这里要注意的是，观察这个函数后面导出的 sha256 实际上是调用了 createMethod 这个方法，那么我们 copy 下来的方法直接调用 createMethod 即可，即 `var t = createMethod()`，不需要这些 exports 了。

另外还有一些变量需要定义，整个 copy 下来的结构如下：

接着前面的继续往下看，还有一句 `o = Object(i.a)()`，同样点进去直接 copy 下来即可，这里没有什么需要注意的地方。

再往下看就来到了 `e.data.signData = p(e)`，点进 function p，将整个函数 copy 下来，这时候你本地调试会发现没有任何错误，实际上他这里使用了 try-catch 语句，捕获到了异常之后就没有任何处理，可以自己加一句 `console.log(e)` 来输出异常，实际上他这里会在 o.doSignature、e.from 两个位置提示未定义，同样的我们可以点进去将函数扣出来，但是后面会遇到函数不断引用其他函数，为了方便，我们可以将其写到 webpack 里，下面的 e.from 也是一样。

将模块写成 webpack 形式，在自执行方法里调用，然后定义全局变量来接收，再将原来的 o, e 换成全局变量即可，这里还需要注意的一个地方，那就是 o.doSignature 传入的 h，是一个定值，需要定义一下，不然后面解密是失败的。如下图所示：

这里扣 webpack 模块的时候也需要注意，不要把所有原方法里有的模块都扣出来，有些根本没用到，可以直接注释掉，这个过程是需要有耐心的，你如果全部扣，那将会是无穷无尽的，还不如直接使用整个 JS 文件，所有有用的模块如下（可能会多，但不会少）：

接着原来的说，`encData: v("SM4", e)` 这里用到了 function v，v 里面又用到了 A、g 等函数，全部扣下来即可，同时还需要注意，前面所说的 e 在 A 函数里也用到了，同样需要换成我们自己定义的全局变量，如下图所示：

到此加密用到的函数都扣完了，此时我们可以写一个方法，对加密的过程进行封装，使用时只需要传入类似以下参数即可：

```
{
    "addr": "", 
    "regnCode": "110000", 
    "medinsName": "", 
    "sprtEcFlag": "", 
    "medinsLvCode": "", 
    "medinsTypeCode": "", 
    "pageNum": 1, 
    "pageSize": 10
}

```

如下图所示 getEncryptedData 就是加密方法：

那么解密方法呢？很明显返回的数据是 encData，直接搜索 encData 就只有三个结果，很容易找到就行 function y，同样的，这里要注意把 `e.from` 改成我们自定义的 `e_.Buffer.from`，另外我们也可以将 header 参数的生成方法也封装成一个函数，便于调用。

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码，不能直接运行！** 完整代码仓库地址：https://github.com/kgepachong/crawler/

#### JavaScript 加密关键代码架构

```
var sm2, sm4, e_;
!function (e) {
    var n = {},
        i = {app: 0},
        r = {app: 0};

    function o(t) {}

    o.e = function (e) {}
    o.m = e
    o.c = n
    o.d = function (e, t, n) {}
    o.r = function (e) {}
    o.n = function (e) {}
    o.o = function (e, t) {}

    sm2 = o('4d09')
    e_ = o('b639')
    sm4 = o('e04e')

}({
    "4d09": function (e, t, n) {},
    'f33e': function (e, t, n) {},
    "4d2d": function (e, t, n) {},
    'b381': function (e, t, n) {},
    // 此处省略 N 个模块
})

// 此处省略 N 个变量

var createOutputMethod = function (e, t) {},
    createMethod = function (e) {},
    nodeWrap = function (method, is224) {},
    createHmacOutputMethod = function (e, t) {},
    createHmacMethod = function (e) {};

function Sha256(e, t) {}

function HmacSha256(e, t, n) {}

// 此处省略 N 个方法

function i() {}

function p(t) {}

function m(e) {}

var c = {
    paasId: undefined,
    appCode: "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    version: "1.0.0",
    appSecret: "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P",
    publicKey: "BEKaw3Qtc31LG/hTPHFPlriKuAn/nzTWl8LiRxLw4iQiSUIyuglptFxNkdCiNXcXvkqTH79Rh/A2sEFU6hjeK3k=",
    privateKey: "AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC",
    publicKeyType: "base64",
    privateKeyType: "base64"
    },
    l = c.appCode,
    u = c.appSecret,
    f = c.publicKey,
    h = c.privateKey,
    t = createMethod(),
    // t = n("6c27").sha256,
    r = Math.ceil((new Date).getTime() / 1e3),
    o = i(),
    a = r + o + r;

function getEncryptedData(data) {
    var e = {"data": data}
    return e.data = {
            data: e.data || {}
        },
        e.data.appCode = c.appCode,
        e.data.version = c.version,
        e.data.encType = "SM4",
        e.data.signType = "SM2",
        e.data.timestamp = r,
        e.data.signData = p(e),
        e.data.data = {
            encData: v("SM4", e)
        },
        // e.data = JSON.stringify({
        //     data: e.data
        // }),
        e
}

function getDecryptedData(t) {
    if (!t)
        return null;
    var n = e_.Buffer.from(t.data.data.encData, "hex")
      , i = function(t, n) {
        var i = sm4.decrypt(n, t)
          , r = i[i.length - 1];
        return i = i.slice(0, i.length - r),
        e_.Buffer.from(i).toString("utf-8")
    }(g(l, u), n);
    return JSON.parse(i)
}

function getHeaders(){
    var headers = {}
    return headers["x-tif-paasid"] = c.paasId,
        headers["x-tif-signature"] = t(a),
        headers["x-tif-timestamp"] = r.toString(),
        headers["x-tif-nonce"] = o,
        headers["Accept"] = "application/json",
        headers["contentType"] = "application/x-www-form-urlencoded",
        headers
}

```

#### Python 获取数据关键代码

```
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-03
# @Author  : 微信公众号：K哥爬虫
# @FileName: nhsa.py
# @Software: PyCharm
# ==================================


import execjs
import requests


regn_code_url = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
lv_and_type_url = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
result_url = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

with open('nhsa.js', 'r', encoding='utf-8') as f:
    nhsa_js = execjs.compile(f.read())


def get_headers():
    """获取 header 参数，每次请求改变"""
    headers = nhsa_js.call("getHeaders")
    headers["User-Agent"] = UA
    headers["Content-Type"] = "application/json"
    headers["Host"] = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
    headers["Origin"] = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
    headers["Referer"] = "脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler"
    # print(headers)
    return headers


def get_regn_code():
    """获取城市代码，返回结果无加密"""
    payload = {"data": {"transferFlag": ""}}
    response = requests.post(url=regn_code_url, json=payload, headers=get_headers())
    print(response.text)


def get_medins_lv_or_type_code(key):
    """获取医疗机构等级 (LV) or 类型 (TYPE) 代码"""
    if key == "LV":
        payload = {"type": "MEDINSLV"}
    elif key == "TYPE":
        payload = {"type": "MEDINS_TYPE"}
    else:
        print("输入有误!")
        return
    encrypted_payload = nhsa_js.call("getEncryptedData", payload)
    encrypted_data = requests.post(url=lv_and_type_url, json=encrypted_payload, headers=get_headers()).json()
    decrypted_data = nhsa_js.call("getDecryptedData", encrypted_data)
    print(decrypted_data)


def get_result():
    addr = input("请输入医疗机构详细地址(默认无): ") or ""
    medins_lv_code = input("请输入医疗机构等级代码(默认无): ") or ""
    medins_name = input("请输入医疗机构名称(默认无): ") or ""
    medins_type_code = input("请输入医疗机构类型代码(默认无): ") or ""
    regn_code = input("请输入医疗机构所在地代码(默认北京市): ") or "110000"
    page_num = input("请输入要爬取的页数(默认1): ") or 1

    for page in range(1, int(page_num)+1):
        payload = {
            "addr": addr,
            "medinsLvCode": medins_lv_code,
            "medinsName": medins_name,
            "medinsTypeCode": medins_type_code,
            "pageNum": page,
            "pageSize": 10,
            "regnCode": regn_code,
            "sprtEcFlag": ""
        }
        page += 1
        encrypted_payload = nhsa_js.call("getEncryptedData", payload)
        encrypted_data = requests.post(url=result_url, json=encrypted_payload, headers=get_headers()).json()
        decrypted_data = nhsa_js.call("getDecryptedData", encrypted_data)
        print(decrypted_data)


def main():
    # 获取城市代码
    # get_regn_code()
    # 获取医疗机构等级代码
    # get_medins_lv_or_type_code("LV")
    # 获取医疗机构类型代码
    # get_medins_lv_or_type_code("TYPE")
    # 获取搜索结果
    get_result()


if __name__ == "__main__":
    main()

```
