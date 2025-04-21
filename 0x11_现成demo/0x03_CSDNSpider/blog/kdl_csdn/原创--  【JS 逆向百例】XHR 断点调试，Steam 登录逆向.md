# 原创
：  【JS 逆向百例】XHR 断点调试，Steam 登录逆向

# 【JS 逆向百例】XHR 断点调试，Steam 登录逆向

#### 文章目录

---


> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### 逆向过程

#### 抓包分析

来到 Steam 的登录页面，随便输入一个账号密码登录，抓包定位到登录接口为 aHR0cHM6Ly9zdG9yZS5zdGVhbXBvd2VyZWQuY29tL2xvZ2luL2RvbG9naW4v ，POST 请求，Form Data 里，`donotcache` 是 13 位时间戳，密码 `password` 被加密处理了，`captchagid` 和 `rsatimestamp` 不知道是什么，`captcha_text` 是验证码：

我们注意到登录请求的上面，还有一个 getrsakey 的请求，很明显和 RSA 加密有关，应该是获取 key 之类的参数，可以看到其返回值类似于：

```
{
  "success":true,
  "publickey_mod":"b1ae3215684fd66207415e39810dcbda75c143dc8c4497994db51591ed5bd17dbaf75e1e......", 
  "publickey_exp":"010001",
  "timestamp":"288093900000",
  "token_gid":"c304e76a58481ad12"
}

```

这里可以发现登录请求的 `rsatimestamp` 参数就是这里的 `timestamp`，其他参数在后面会用到。

#### XHR 断点定位

本次案例我们使用 XHR 断点来定位加密的位置，首先了解一下什么是 XHR，XHR 全称 XMLHttpRequest，XHR 可以在不重新加载页面的情况下更新网页、在页面已加载后从服务器请求、接收数据，是 Ajax 的基础，属于 Ajax 特殊的请求类型，利用浏览器控制台可以过滤 XHR 请求。

既然是 XHR 断点，那么这种方法就只能用于 XHR 请求，这也是这种方法的缺点，通过 XHR 断点，**定位到的位置通常在加密处理完成之后**，已经准备发送请求了，这样的优点是我们可以跟踪栈，能比较容易地找到加密的地方。

XHR 断点定位有两种方法，第一种是找到发送请求的 URL 之后，截取 URL 的一部分，在 Source 面板下，右侧 XHR/fetch Breakpoints 里添加你截取的 URL，如下图所示，已成功断下：

第二种方法，在 Network 面板，点击 XHR 过滤 XHR 请求，在 Initiator 项里可以看到调用的 JS，鼠标移到 JS 上，可以看到调用栈，点击第一个，即可进入到发送请求的地方，定位到的位置和第一种方法是一样的。这种方法需要注意的是，XHR 过滤不一定准确，但是只要是 Initiator 项里可以看到 JS，就说明可以跟进去进行调试，如果是通过 Form 表单或者其他方式发送的请求，Initiator 项会显示 Other，此时就不能通过这种方法进行调试。

#### 参数逆向

前面 XHR 的两种方法，无论使用哪一种，定位到的位置都是一样的，查看右侧 Call Stack，即调用栈，一步一步往上查看调用的函数，在 login.js 里面，可以找到语句 `var encryptedPassword = RSA.encrypt(password, pubKey);`，非常明显的 RSA 加密：

可以关键代码改写一下，方便本地调试：

```
function getEncryptedPassword(password, results) {
    var pubKey = RSA.getPublicKey(results.publickey_mod, results.publickey_exp);
    password = password.replace(/[^\x00-\x7F]/g, '');
    var encryptedPassword = RSA.encrypt(password, pubKey);
    return encryptedPassword
}

```

找到加密的位置后，就可以埋下断点，取消 XHR 断点，重新进行调试，可以看到 `results` 就是前面 getrsakey 请求返回的数据：

`RSA.getPublicKey` 和 `RSA.encrypt` 分别是 rsa.js 里面 RSA 的 `getPublicKey` 和 `encrypt` 方法：

将整个 rsa.js 复制下来进行本地调试，会提示 `BigInteger` 未定义，鼠标放上去会看到是用到了 jsbn.js 里面的方法，如果一个一个函数去扣的话会比较麻烦，直接将整个 jsbn.js 文件代码复制下来即可：

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码，不能直接运行！**完整代码仓库地址：https://github.com/kgepachong/crawler/

#### JavaScript 加密关键代码架构

```
navigator = {};

var dbits;

// JavaScript engine analysis
var canary = 0xdeadbeefcafe;
var j_lm = ((canary &amp; 0xffffff) == 0xefcafe);

// (public) Constructor
function BigInteger(a, b, c) {}

// return new, unset BigInteger
function nbi() {}

// am: Compute w_j += (x*this_i), propagate carries,
// c is initial carry, returns final carry.
// c &lt; 3*dvalue, x &lt; 2*dvalue, this_i &lt; dvalue
// We need to select the fastest one that works in this environment.

// am1: use a single mult and divide to get the high bits,
// max digit bits should be 26 because
// max internal value = 2*dvalue^2-2*dvalue (&lt; 2^53)
function am1(i, x, w, j, c, n) {}

// 此处省略 N 个函数

var RSAPublicKey = function ($modulus_hex, $encryptionExponent_hex) {};

var Base64 = {};

var Hex = {};

var RSA = {};

function getEncryptedPassword(password, results) {
    var pubKey = RSA.getPublicKey(results.publickey_mod, results.publickey_exp);
    password = password.replace(/[^\x00-\x7F]/g, '');
    var encryptedPassword = RSA.encrypt(password, pubKey);
    return encryptedPassword
}

// 测试样例
// var results = {
//     publickey_exp: "010001",
//     publickey_mod: "b1c6460eb07d9a6a9de07e2d7afbbe36f30b7196a4a13b7f069e8bc6be3217fe368df46ee506ad4bbaf4190a13d3937b7cc19d081fa40c3cb431d94956804b2c80aad349fa9f95254c899d905aaaab54e7bbe95159b400fde541ec6828df76f0c7a226b38651853f6cdc67dc46e7fc3253d819e0ece8aae8551a27ebbb9f8a579ba1c4f52b69fc6605c8e11b0c00e32043c7675e268815f491be48ee644670d2d632077f8ff09d7a4928e5187d6e33279760f23b0b72a4e2928154f87326e5a57541b91862b3916e4972313ad764608d9628793eef3a0a8dcdd1ab6b908d32f56f830262fd33ed6b441e6b1e0c945508461e9c083cb10d8069f9539ca70fdd33",
//     success: true,
//     timestamp: "370921200000",
//     token_gid: "3d1df3e102d1a1d2"
// }
//
// console.log(getEncryptedPassword("12345678", results))

```

#### Python 登录关键代码

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

import execjs
import requests
from PIL import Image


index_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
login_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
get_rsa_key_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
render_captcha_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
refresh_captcha_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'

headers = {
    'Host': '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler',
    'Origin': '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler',
    'Referer': '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
session = requests.session()


def get_cookies():
    response = session.get(url=index_url, headers=headers)
    cookies = response.cookies.get_dict()
    print(cookies)
    return cookies


def get_captcha(cookies):
    # 首先获取 gid
    data = {'donotcache': str(int(time.time() * 1000))}
    refresh_captcha_response = session.post(url=refresh_captcha_url, data=data, cookies=cookies, headers=headers)
    gid = refresh_captcha_response.json()['gid']

    # 携带 gid 获取验证码
    params = {'gid': gid}
    render_captcha_response = session.get(url=render_captcha_url, params=params, cookies=cookies, headers=headers)

    with open('code.png', 'wb') as f:
        f.write(render_captcha_response.content)
    image = Image.open('code.png')
    image.show()
    captcha = input('请输入验证码: ')
    return captcha, gid


def get_rsa_key(username, cookies):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'username': username
    }
    response = session.post(url=get_rsa_key_url, data=data, cookies=cookies, headers=headers).json()
    print(response)
    return response


def get_encrypted_password(password, rsa_key_dict):
    with open('encrypt.js', 'r', encoding='utf-8') as f:
        steampowered_js = f.read()
    encrypted_password = execjs.compile(js).call('getEncryptedPassword', password, rsa_key_dict)
    print(encrypted_password)
    return encrypted_password


def login(username, encrypted_password, cookies, rsa_key_dict, captcha, gid):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'password': encrypted_password,
        'username': username,
        'twofactorcode': '',
        'emailauth': '',
        'loginfriendlyname': '',
        'captchagid': gid,
        'captcha_text': captcha,
        'emailsteamid': '',
        'rsatimestamp': rsa_key_dict['timestamp'],
        'remember_login': False,
        # 'tokentype': '-1'
    }
    print(data)
    response = session.post(url=login_url, data=data, cookies=cookies, headers=headers)
    print(response.text)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')

    # 获取 cookies
    cookies = get_cookies()

    # 获取验证码和 gid
    captcha, gid = get_captcha(cookies)

    # 获取 RSA 加密所需 key 等信息
    rsa_key_dict = get_rsa_key(username, cookies)

    # 获取加密后的密码
    encrypted_password = get_encrypted_password(password, rsa_key_dict)

    # 携带 用户名、加密后的密码、cookies、验证码等登录
    login(username, encrypted_password, cookies, rsa_key_dict, captcha, gid)


if __name__ == '__main__':
    main()

```
