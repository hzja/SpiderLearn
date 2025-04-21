# 原创
：  【JS 逆向百例】建筑市场监管平台企业数据

# 【JS 逆向百例】建筑市场监管平台企业数据

### 声明

本文章中所有内容仅供学习交流，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关。

### 逆向目标

### 逆向过程

本次的逆向目标是建筑市场监管平台的企业数据，来到全国建筑市场监管公共服务平台首页，依次点击数据服务 —&gt; 企业数据，尝试抓包一下所有企业的数据，可以看到返回的数据是经过加密的：

数据看不出来是什么加密方式，但是加密分析得多了，就知道一般都是经过 `CryptoJS` 加密模块加密得到的，那么我们可以尝试直接搜索 `CryptoJS`，`decrypt` 等关键字，或者搜索加密算法中经常用到的偏移量 `iv`、模式 `mode`、填充方式 `padding` 等，还有一般的 JSON 数据可以搜索 `JSON.parse` 等，这里直接搜索 `JSON.parse`，在 app.a9f6bb6d.js 文件里定位到可疑代码，埋下断点进行调试：

可以看到 e 就是解密后的数据，观察语句 `var e = JSON.parse(h(t.data));`，直接跟进 h 函数，可以看到很明显的 AES 加密：

```
function h(t) {
    var e = d.a.enc.Hex.parse(t)
    , n = d.a.enc.Base64.stringify(e)
    , a = d.a.AES.decrypt(n, f, {
        iv: m,
        mode: d.a.mode.CBC,
        padding: d.a.pad.Pkcs7
    })
    , r = a.toString(d.a.enc.Utf8);
    return r.toString()
}

```

加密模式为 CBC，填充方式为 Pkcs7，而缺少的偏移量 m、f 的值，在上面也可以找到：

```
f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
m = d.a.enc.Utf8.parse("0123456789ABCDEF")

```

在 Python 当中，直接引入 CryptoJS，重写这个函数即可。

### 完整代码

完整代码可在 GitHub 下载：https://github.com/kuaidaili/crawler/tree/main/jzsc_mohurd_gov_cn

#### jzsc_mohurd_decrypt.js

```
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getDecryptedData(t) {
    var m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF"),
        f = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn"),
        e = CryptoJS.enc.Hex.parse(t),
        n = CryptoJS.enc.Base64.stringify(e),
        a = CryptoJS.AES.decrypt(n, f, {
            iv: m,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
    }),
        r = a.toString(CryptoJS.enc.Utf8);
    return r.toString()
}

// 测试样例
// var t = '95780ba094xxxxxxxxxx'
// console.log(getDecryptedData(t))

```

#### jzsc_mohurd.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

import execjs
import requests


data_url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=%s&amp;pgsz=15&amp;total=450'


def get_encrypted_data(page):
    headers = {
        'Host': 'jzsc.mohurd.gov.cn',
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    encrypted_data = requests.get(url=data_url % page, headers=headers).text
    return encrypted_data


def get_decrypted_data(encrypted_data):
    with open('jzsc_mohurd_decrypt.js', 'r', encoding='utf-8') as f:
        jzsc_mohurd_js = f.read()
    decrypted_data = execjs.compile(jzsc_mohurd_js).call('getDecryptedData', encrypted_data)
    return json.loads(decrypted_data)


def main():
    # 30页数据
    for page in range(30):
        encrypted_data = get_encrypted_data(page)
        decrypted_data = get_decrypted_data(encrypted_data)
        print(decrypted_data)


if __name__ == '__main__':
    main()

```
