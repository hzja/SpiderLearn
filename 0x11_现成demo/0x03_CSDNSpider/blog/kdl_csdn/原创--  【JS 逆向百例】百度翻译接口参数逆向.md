# 原创
：  【JS 逆向百例】百度翻译接口参数逆向

# 【JS 逆向百例】百度翻译接口参数逆向

<img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/95af9b01fc69d7befa548ea6bc52686f.png"/><br/> 

#### 文章目录

---


### 逆向目标

### 逆向过程

#### 抓包分析

我们在百度翻译页面随便输入文字，可以看到没有刷新页面，翻译结果就出来了，由此可以推断是 Ajax 加载的，打开开发者工具，选择 XHR 过滤 Ajax 请求，可以看到有一条 URL 为 https://fanyi.baidu.com/v2transapi?from=zh&amp;to=en 的 POST 请求，当我们输入“测试”的时候，他返回的数据经过 Unicode 转中文后类似于如下结构：

```
{
	"trans_result": {
		"data": [{
			"dst": "test",
			"prefixWrap": 0,
			"result": [
				[0, "test", ["0|6"],
					[],
					["0|6"],
					["0|4"]
				]
			],
			"src": "测试"
		}],
		"from": "zh",
		"status": 0,
		"to": "en",
		"type": 2
	},
	"dict_result": {
        // 略
    },
	"liju_result": {
        // 略
    }
}

```

`trans_result` 是翻译的结果，`dict_result` 是更多翻译结果，`liju_result` 是例句、标签等，那么这个 URL 就是我们需要的翻译接口了。

由于是 POST 请求，我们观察它的 Form Data：

在抓包过程中我们还注意到有一条 URL 为 https://fanyi.baidu.com/langdetect 的 POST 请求，而它返回的数据如下：

```
{"error":0,"msg":"success","lan":"zh"}

```

很明显，这个是自动检测待翻译字符串的语言，它的 Form Data 也很简单，`query` 就是待翻译的字符串，这个接口可以根据实际场景进行使用。

#### 获取 token

`token` 的值由于是固定的，所以我们可以尝直接搜索，可以在首页源码里面找到，使用正则表达式可以直接提取。

#### 获取 sign

`sign` 是会改变的，怀疑是 JS 动态生成，所以我们尝试全局搜索 `sign`，这里有个技巧，只搜索 `sign` 会出来很多结果，可以加上冒号或者等于号来缩小范围，搜索 `sign:` 可以在 index_a8b7098.js 里面找到 5 个符合的位置，观察可以发现在第 8392 行的位置处，数据最全面，和前面抓包看到的 Form Data 数据一致。

点击行号，在此处埋下断点，点击翻译按钮，可以看到成功断下，此时 `sign` 的值就是最终我们想要的的值：

这里将待翻译字符串传入了 `L` 函数，鼠标放到 `L` 函数上，直接点击跟进这个函数，可以发现 `sign` 的值其实是 `function e(r)` 这个函数进行一系列操作之后得到的，直接复制这个函数进行本地调试，调试过程中可以发现缺少一个 `i` 的值，在右边的 Closure 栏里，或者鼠标选中 `i`，可以看到 `i` 的值，多次调试发现它是固定的，可以直接写死：

继续调试 `function e(r)`，还会提示缺少一个函数 `n`，那么直接跟进这个函数，将函数 `n` 一同复制下来即可。

### 完整代码

#### baidu_encrypt.js

获取 `sign` 的值：

```
var i = '320305.131321201'

function n(r, o) {
    for (var t = 0; t &lt; o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a &gt;= "a" ? a.charCodeAt(0) - 87 : Number(a), a = "+" === o.charAt(t + 1) ? r &gt;&gt;&gt; a : r &lt;&lt; a, r = "+" === o.charAt(t) ? r + a &amp; 4294967295 : r ^ a
    }
    return r
}

function e(r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === o) {
        var t = r.length;
        t &gt; 30 &amp;&amp; (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h &gt; C; C++) "" !== e[C] &amp;&amp; f.push.apply(f, a(e[C].split(""))), C !== h - 1 &amp;&amp; f.push(o[C]);
        var g = f.length;
        g &gt; 30 &amp;&amp; (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
    }
    var u = void 0, l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
    u = null !== i ? i : (i = window[l] || "") || "";
    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v &lt; r.length; v++) {
        var A = r.charCodeAt(v);
        128 &gt; A ? S[c++] = A : (2048 &gt; A ? S[c++] = A &gt;&gt; 6 | 192 : (55296 === (64512 &amp; A) &amp;&amp; v + 1 &lt; r.length &amp;&amp; 56320 === (64512 &amp; r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 &amp; A) &lt;&lt; 10) + (1023 &amp; r.charCodeAt(++v)), S[c++] = A &gt;&gt; 18 | 240, S[c++] = A &gt;&gt; 12 &amp; 63 | 128) : S[c++] = A &gt;&gt; 12 | 224, S[c++] = A &gt;&gt; 6 &amp; 63 | 128), S[c++] = 63 &amp; A | 128)
    }
    for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b &lt; S.length; b++) p += S[b], p = n(p, F);
    return p = n(p, D), p ^= s, 0 &gt; p &amp;&amp; (p = (2147483647 &amp; p) + 2147483648), p %= 1e6, p.toString() + "." + (p ^ m)
}

// console.log(e('测试'))

```

#### baidufanyi.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import execjs
import requests


index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=3BE16D933E9C0182F2A6E93D7A9D1424; PSTM=1623723330; BAIDUID=8496908995397662040287D2CE1C4224:FG=1; __yjs_duid=1_779078c2c847bb3217554b8549ad49bd1623728424311; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDSFRCVID_BFESS=BkFOJeCT5G3_WP5eFqJ2T4D2p2KKN9OTTPjcTR5qJ04BtyCVNKsaEG0PtOgMNBDbJ2MRogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4toCPMJI_3fP36q45HMt00qxby26PDajn9aJ5nQI5nhU7505oqDJ0Z0ROOWhRute3i2DTvQUbmjRO206oay6O3LlO83h5wW57KKl0MLPbcep68LxODy6DI0xnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4D5_ae5O3DGRf-b-XKD600PK8Kb7VbUF6qfnkbft7jtteyhbTJCID-UQKQPnc_pC4yURFef473b3B5h3NJ66ZoIbPbPTTSlroKPQpQT8r5-nMWx6G3IrZoq64ab3vOpRTXpO13fAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjDjJRCOoI--f-3bfTrP-trf5DCShUFs3tnlB2Q-5M-a3KOrSUtGbfjay6D7j-8HbTjiW2_82MbmLncjSM_GKfC2jMD32tbpWfneKmTxoUJ2Bb3Y8loe-xCKXqDebPRiWPb9QgbP2pQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjKbDTvL3f; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1624438637,1624603638,1624928461,1624953786; H_PS_PSSID=34131_34099_31253_34004_33607_34107_34135; delPer=0; PSINO=6; BAIDUID_BFESS=8496908995397662040287D2CE1C4224:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1624962661; __yjs_st=2_MzJhZTMxZGU5MjZjNGJiZTJiZjQwYjVkMWM5ZjYyMGFjZDlkMDJmNTU3OGU5ZTM4N2JjNjNkODAwYWJiY2M3NDA1NWEyODNkMzNkMDEzNThiZTU4NzNhMTQxYzIxOTQyMzg3MjhiMzA5ZjY2MDczZTBhZDdmZDg4YTFhNjVmZTMwZTYyZTRjNmRhMWNmYzg3NDFjODYzYTRlZTE2NzBmODAyMWI4MTI3NTZmNjg1MDk4OWIxZTYzNTc4NzhjY2E3NzU3ZGYyZmI1ODdjZTM5ZDNlOGU0ZGQ2NzE5OGU2NzUzM2ZhZTcxZmVjNjI4MDIyN2Y1N2NlMzZmMmRlY2U4Yl83XzQ5NzQ4ZWE4; ab_sr=1.0.1_MmUwODU0NGE4NjIwZmY4NjgxZmM1NGYxOTI5ZWQwOGU2NjU3ZjgwNzhkMTNjNDI5NWE0ODQwYzlkZDVjY2Q1YWEyZDQyZWI0ZjNkMWQ0NTEyMGFjYzdiNDdmNzYxYjNiMjkxZTI1M2I3Y2VhZGE3NDEzOTgyMjY1MjBlZGM4OGJiZGVjMzFkYTM3ODgyMTRkZjJhMGYzNGM0MGJmMGY1Yg==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_token():
    response = requests.get(url=index_url, headers=headers).text
    token = re.findall(r"token: '([0-9a-z]+)", response)[0]
    return token


def get_sign(query):
    with open('baidu_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('e', query)
    return sign


def get_result(lang, query, sign, token):
    data = {
        'from': lang,
        'to': 'en',
        'query': query,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    response = requests.post(url=translate_api, headers=headers, data=data)
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字：')
    response = requests.post(url=lang_url, headers=headers, data={'query': query})
    lang = response.json()['lan']
    token = get_token()
    sign = get_sign(query)
    result = get_result(lang, query, sign, token)
    print('翻译成英文的结果为：', result)


if __name__ == '__main__':
    main()

```
