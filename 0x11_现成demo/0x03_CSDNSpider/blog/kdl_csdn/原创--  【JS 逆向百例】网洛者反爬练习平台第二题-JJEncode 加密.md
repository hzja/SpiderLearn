# 原创
：  【JS 逆向百例】网洛者反爬练习平台第二题：JJEncode 加密

# 【JS 逆向百例】网洛者反爬练习平台第二题：JJEncode 加密

> 
关注微信公众号：K哥爬虫，持续分享爬虫进阶、JS/安卓逆向等技术干货！


#### 文章目录

### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### JJEncode 简介

JJEncode 最初是由日本作者 Yosuke HASEGAWA 于 2009 年开发的一个 web 程序，它可以将任意 JavaScript 编码为仅使用 18 个符号的混淆形式 `[]()!+,\"$.:;_{}~=`，在线体验地址：https://utf-8.jp/public/jjencode.html ，如果你想深入探究其原理，可以在K哥爬虫公众号回复【JJEncode】获取其详细原理介绍的PDF。

作者有提示：JJEncode 易于解码，它不是实用的混淆，只是一个编码器，JJEncode 太有特点了，很容易被检测，而且还浏览器依赖，代码不能在某种浏览器上运行。它的缺点是压栈很严重，如果 JS 很大，去做加密可能内存溢出，所以只适合核心功能加密，事实上 JJEncode 商用的还是很少，不过认识一下并没有什么坏处。

正常的一段 JS 代码：

```
alert("Hello, JavaScript" )

```

经过 JJEncode 混淆（自定义变量名为 $）之后的代码：

```
$=~[];$={___:++$,$$$$:(![]+"")[$],__$:++$,$_$_:(![]+"")[$],_$_:++$,$_$$:({}+"")[$],$$_$:($[$]+"")[$],_$$:++$,$$$_:(!""+"")[$],$__:++$,$_$:++$,$$__:({}+"")[$],$$_:++$,$$$:++$,$___:++$,$__$:++$};$.$_=($.$_=$+"")[$.$_$]+($._$=$.$_[$.__$])+($.$$=($.$+"")[$.__$])+((!$)+"")[$._$$]+($.__=$.$_[$.$$_])+($.$=(!""+"")[$.__$])+($._=(!""+"")[$._$_])+$.$_[$.$_$]+$.__+$._$+$.$;$.$$=$.$+(!""+"")[$._$$]+$.__+$._+$.$+$.$$;$.$=($.___)[$.$_][$.$_];$.$($.$($.$$+"\""+$.$_$_+(![]+"")[$._$_]+$.$$$_+"\\"+$.__$+$.$$_+$._$_+$.__+"(\\\"\\"+$.__$+$.__$+$.___+$.$$$_+(![]+"")[$._$_]+(![]+"")[$._$_]+$._$+",\\"+$.$__+$.___+"\\"+$.__$+$.__$+$._$_+$.$_$_+"\\"+$.__$+$.$$_+$.$$_+$.$_$_+"\\"+$.__$+$._$_+$._$$+$.$$__+"\\"+$.__$+$.$$_+$._$_+"\\"+$.__$+$.$_$+$.__$+"\\"+$.__$+$.$$_+$.___+$.__+"\\\"\\"+$.$__+$.___+")"+"\"")())();

```

JJEncode 解混淆的方式很简单，以下介绍几种常见的方法：
1. 使用在线工具直接解密，比如：http://www.hiencode.com/jjencode.html1. JJEncode 的代码通常是一个自执行方法（IIFE），去掉代码最后面的 `()` 后，放到浏览器里面去直接执行就可以看到源码1. 在线调试，在 JJEncode 代码第一行下断点，然后一步一步执行，最终也会在虚拟机（VM）里看到源码
### 逆向参数

逆向的目标主要是翻页接口 `_signature` 参数，调用的加密方法仍然是 `window.get_sign()`，和第一题是一样的，本文不再赘述，不清楚的可以去看 K 哥上期的文章。

跟进 2.js 之后会发现是一个 JJEncode 混淆：

我们将其中混淆的部分，去掉最后的 `()` 放到浏览器控制台运行一下（建议单开一个无痕窗口，有时候可能会有影响），就可以看到源码了，点击源码来到虚拟机（VM），整个源码就展现在我们面前了：

除了直接去掉 `()` 运行以外，我们还可以在混淆代码第一行下断点，然后单步跟进，最后同样也会得到源码，如下图所示：

看源码就很简单了，就是一个魔改的 SHA1 匿名函数，将其代码 copy 下来改写一下即可，配合 Python 代码携带 _signature 挨个计算每一页的数据，最终提交成功：

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码，不能直接运行！** 完整代码仓库地址：https://github.com/kgepachong/crawler/

#### JavaScript 加密代码

```
/* ==================================
# @Time    : 2021-12-10
# @Author  : 微信公众号：K哥爬虫
# @FileName: challenge_2.js
# @Software: PyCharm
# ================================== */


var hexcase = 0;
var chrsz = 8;

function hex_sha1(s) {
    return binb2hex(core_sha1(AlignSHA1(s)));
}

function sha1_vm_test() {
    return hex_sha1("abc") == "a9993e364706816aba3e25717850c26c9cd0d89d";
}

function core_sha1(blockArray) {
    var x = blockArray;
    var w = Array(80);
    var a = 1732584173;
    var b = -271733877;
    var c = -1752584194;
    var d = 271733878;
    var e = -1009589776;
    for (var i = 0; i &lt; x.length; i += 16) {
        var olda = a;
        var oldb = b;
        var oldc = c;
        var oldd = d;
        var olde = e;
        for (var j = 0; j &lt; 80; j++) {
            if (j &lt; 16)
                w[j] = x[i + j];
            else
                w[j] = rol(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
            var t = safe_add(safe_add(rol(a, 5), sha1_ft(j, b, c, d)), safe_add(safe_add(e, w[j]), sha1_kt(j)));
            e = d;
            d = c;
            c = rol(b, 30);
            b = a;
            a = t;
        }
        a = safe_add(a, olda);
        b = safe_add(b, oldb);
        c = safe_add(c, oldc);
        d = safe_add(d, oldd);
        e = safe_add(e, olde);
    }
    return new Array(a, b, c, d, e);
}

function sha1_ft(t, b, c, d) {
    if (t &lt; 20) {
        return (b &amp; c) | ((~b) &amp; d);
    }
    if (t &lt; 40) {
        return b ^ c ^ d;
    }
    if (t &lt; 60) {
        return (b &amp; c) | (b &amp; d) | (c &amp; d);
    }
    return b ^ c ^ d;
}

function sha1_kt(t) {
    return (t &lt; 20) ? 1518500249 : (t &lt; 40) ? 1859775393 : (t &lt; 60) ? -1894007588 : -899497514;
}

function safe_add(x, y) {
    var lsw = (x &amp; 0xFFFF) + (y &amp; 0xFFFF);
    var msw = (x &gt;&gt; 16) + (y &gt;&gt; 16) + (lsw &gt;&gt; 16);
    return (msw &lt;&lt; 16) | (lsw &amp; 0xFFFF);
}

function rol(num, cnt) {
    return (num &lt;&lt; cnt) | (num &gt;&gt;&gt; (32 - cnt));
}

function AlignSHA1(str) {
    var nblk = ((str.length + 8) &gt;&gt; 6) + 1;
    var blks = new Array(nblk * 16);
    for (var i = 0; i &lt; nblk * 16; i++) {
        blks[i] = 0;
    }
    for (i = 0; i &lt; str.length; i++) {
        blks[i &gt;&gt; 2] |= str.charCodeAt(i) &lt;&lt; (24 - (i &amp; 3) * 8);
    }
    blks[i &gt;&gt; 2] |= 0x80 &lt;&lt; (24 - (i &amp; 3) * 8);
    blks[nblk * 16 - 1] = str.length * 8;
    return blks;
}

function binb2hex(binarray) {
    var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
    var str = "";
    for (var i = 0; i &lt; binarray.length * 4; i++) {
        str += hex_tab.charAt((binarray[i &gt;&gt; 2] &gt;&gt; ((3 - i % 4) * 8 + 4)) &amp; 0xF) + hex_tab.charAt((binarray[i &gt;&gt; 2] &gt;&gt; ((3 - i % 4) * 8)) &amp; 0xF);
    }
    return str;
}

function getSign() {
    return hex_sha1(Date.parse(new Date).toString());
}

// 测试输出
// console.log(getSign())

```

#### Python 计算关键代码

```
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-12-10
# @Author  : 微信公众号：K哥爬虫
# @FileName: challenge_2.py
# @Software: PyCharm
# ==================================


import execjs
import requests


challenge_api = "http://spider.wangluozhe.com/challenge/api/2"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "将 cookie 值改为你自己的！",
    "Host": "spider.wangluozhe.com",
    "Origin": "http://spider.wangluozhe.com",
    "Referer": "http://spider.wangluozhe.com/challenge/2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def get_signature():
    with open('challenge_2.js', 'r', encoding='utf-8') as f:
        ppdai_js = execjs.compile(f.read())
    signature = ppdai_js.call("getSign")
    print("signature: ", signature)
    return signature


def main():
    result = 0
    for page in range(1, 101):
        data = {
            "page": page,
            "count": 10,
            "_signature": get_signature()
        }
        response = requests.post(url=challenge_api, headers=headers, data=data).json()
        for d in response["data"]:
            result += d["value"]
    print("结果为: ", result)


if __name__ == '__main__':
    main()

```
