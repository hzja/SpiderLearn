# 原创
：  【JS 逆向百例】有道翻译接口参数逆向

# 【JS 逆向百例】有道翻译接口参数逆向

#### 文章目录

---


### 逆向目标

### 逆向过程

#### 抓包分析

我们在有道翻译页面随便输入文字，可以看到没有刷新页面，翻译结果就出来了，由此可以推断是 Ajax 加载的，打开开发者工具，选择 XHR 过滤 Ajax 请求，可以看到有一条 URL 为 https://fanyi.youdao.com/translate_o?smartresult=dict&amp;smartresult=rule 的 POST 请求，当我们输入“测试”的时候，他返回的数据类似于如下结构：

```
{
	"translateResult": [
		[{
			"tgt": "test",
			"src": "测试"
		}]
	],
	"errorCode": 0,
	"type": "zh-CHS2en",
	"smartResult": {
		"entries": ["", "[试验] test\r\n", "measurement\r\n"],
		"type": 1
	}
}

```

`translateResult` 是翻译的结果，`smartResult` 是智能推荐的其他翻译，那么这个 URL 就是我们需要的翻译接口了。

由于是 POST 请求，我们观察它的 Form Data：

#### 参数逆向

`salt`、`sign`、`bv` 三个加密参数，全局搜索任意一个，搜索结果比较多，依次对比，可以发现 fanyi.min.js 文件第 8969 行左右开始，Form Data 所有的参数都齐全了，埋下断点调试一下，可以看到所有数据和最终结果一致，加密的四个参数都在 `r` 当中取值，跟踪 `r`，往上找可以看到 `r = v.generateSaltSign(n);`，其中 n 是输入的待翻译的字符串：

继续跟进 `generateSaltSign` 函数，点击跳转到 `r` 函数，这里可以看到关键的加密代码：

```
var r = function(e) {
    var t = n.md5(navigator.appVersion)
      , r = "" + (new Date).getTime()
      , i = r + parseInt(10 * Math.random(), 10);
    return {
        ts: r,
        bv: t,
        salt: i,
        sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
    }
};

```

分析这段关键加密代码：

这个过程比较简单，可以直接使用 Python 来复现：

```
import time
import random
import hashlib


query = "待翻译字符串"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

lts = str(int(time.time() * 1000))                                # 以毫秒为单位的 13 位时间戳
salt = lts + str(random.randint(0, 9))                            # 13 位时间戳+随机数字，生成 salt 值
sign = "fanyideskweb" + query + salt + "Y2FYu%TNSbMCxc3t2u^XT"    # 拼接字符串组成 sign
sign = hashlib.md5(sign.encode()).hexdigest()                     # 将 sign 进行 MD5 加密，生成最终 sign 值
bv = hashlib.md5(user_agent.encode()).hexdigest()                 # 对 UA 进行 MD5 加密，生成 bv 值

```

或者直接引用 JS，使用 nodejs 里面的加密模块 CryptoJS 来进行 MD5 加密，改写 JS 如下：

```
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getEncryptedParams(data, ua) {
    var bv = CryptoJS.MD5(ua).toString()
        , lts = "" + (new Date).getTime()
        , salt = lts + parseInt(10 * Math.random(), 10)
    var sign = CryptoJS.MD5('fanyideskweb'+data+salt+']BjuETDhU)zqSxf-=B#7m').toString()
    return {bv: bv, lts: lts, salt: salt, sign: sign}
}

```

### 完整代码

#### youdao_encrypt.js

获取加密参数 `salt`、`sign`、`bv`：

```
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getEncryptedParams(data, ua) {
    var bv = CryptoJS.MD5(ua).toString(),
        lts = "" + (new Date).getTime(),
        salt = lts + parseInt(10 * Math.random(), 10)
    var sign = CryptoJS.MD5('fanyideskweb' + data + salt + ']BjuETDhU)zqSxf-=B#7m').toString()
    return { bv: bv, lts: lts, salt: salt, sign: sign }
}

// var ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
// var data = "测试"
// console.log(getEncryptedParams(data, ua));

```

#### youdaofanyi.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import random
import hashlib

import execjs
import requests


translate_url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&amp;smartresult=rule'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


def get_translation_result(parameters):
    headers = {
        'User-Agent': user_agent,
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Cookie': 'OUTFOX_SEARCH_USER_ID="-1848382357@10.169.0.84"; ___rl__test__cookies=1625907853887; OUTFOX_SEARCH_USER_ID_NCOO=132978720.55854891'
    }
    response = requests.post(url=translate_url, headers=headers, data=parameters)
    result = response.json()['translateResult'][0][0]['tgt']
    return result


def get_parameters_by_python(query, translate_from, translate_to):
    lts = str(int(time.time() * 1000))                                # 以毫秒为单位的 13 位时间戳
    salt = lts + str(random.randint(0, 9))                            # 13 位时间戳+随机数字，生成 salt 值
    sign = "fanyideskweb" + query + salt + "Y2FYu%TNSbMCxc3t2u^XT"    # 拼接字符串组成 sign
    sign = hashlib.md5(sign.encode()).hexdigest()                     # 将 sign 进行 MD5 加密，生成最终 sign 值
    bv = hashlib.md5(user_agent.encode()).hexdigest()                 # 对 UA 进行 MD5 加密，生成 bv 值
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return parameters


def get_parameters_by_javascript(query, translate_from, translate_to):
    with open('youdao_encrypt.js', 'r', encoding='utf-8') as f:
        youdao_js = f.read()
    params = execjs.compile(youdao_js).call('get_params', query, user_agent)    # 通过 JavaScript 代码获取各个参数
    bv = hashlib.md5(user_agent.encode()).hexdigest()                           # 对 UA 进行 MD5 加密，生成 bv 值
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': params['salt'],
        'sign': params['sign'],
        'lts': params['lts'],
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return parameters


def main():
    query = input('请输入要翻译的文字：')
    # 原始语言，目标语言，默认自动处理
    translate_from = translate_to = 'AUTO'
    # 通过 Python 获取加密参数或者通过 JavaScript 获取参数，二选一
    param = get_parameters_by_python(query, translate_from, translate_to)
    # param = get_parameters_by_javascript(query, translate_from, translate_to)
    result = get_translation_result(param)
    print('翻译的结果为：', result)


if __name__ == '__main__':
    main()

```
