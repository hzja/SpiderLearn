# 原创
：  【JS 逆向百例】层层嵌套！某加速商城 RSA 加密

# 【JS 逆向百例】层层嵌套！某加速商城 RSA 加密

<img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/c6f19630d293fe3068310f555f80dd82.png#pic_center"/><br/> 

#### 文章目录

---


> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 声明

**本文章中所有内容仅供学习交流，敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### 逆向过程

#### 抓包分析

在首页点击登陆，来到登录页面，随便输入一个账号密码登陆，抓包定位到登录接口为 aHR0cDovL3d3dy4xNXl1bm1hbGwuY29tL3BjL2xvZ2luL2NoZWNr ，POST 请求，Form Data 里，密码 `u[password]` 被加密处理了，此外还有一个 `_csrfToken` 也是需要我们解决的，cookie 里面有一个 `PHPSESSID`，经过测试，如果不带此参数，最终的请求也是失败的。

#### 参数逆向

首先看看 `_csrfToken`，先尝试直接搜索一下它的值，可以发现其实在首页的源码里面就有，直接匹配拿过来即可：

再看一下 cookie 里面的 `PHPSESSID`，首先想到的，可能是第一次访问页面，Response Headers 返回的 Set-Cookie 得到的，查看第一次请求，确实是的，如果没有的话，需要清除缓存再访问（开发者工具 ——&gt; Application ——&gt; Storage ——&gt; Clear site data）。

最后一个密码参数 `u[password]`，肯定是通过 JS 加密得到的，直接 Ctrl+Shift+F 全局搜索，可以直接在 index 首页找到 RSA 加密的地方，埋下断点进行调试，最后的 res 正是加密后的密码：

我们将这段关键代码进行改写，封装成一个函数：

```
function getEncryptedPassword(password) {
    var public_key = "00bdf3db924714b9c4ddd144910071c282e235ac51371037cf89fa08f28b9105b6326338ed211280154c645bf81bae4184c2b52e2b02b0953e7aa8b25a8e212a0b";
    var public_length = "10001";
    var rsa = new RSAKey();
    rsa.setPublic(public_key, public_length);
    return rsa.encrypt(password);
}

```

这里主要用到的三个函数 `RSAKey()`、`setPublic()`、`encrypt()`，在开发者工具中，鼠标放到函数上，可以看到这里都是调用的 rsa.js 里面的方法，我们直接将整个文件剥离下来进行本地调试：

本地调试会发现提示 `BigInteger` 未定义，鼠标移到这个函数上面，可以发现是调用了 jsbn.js 里面的方法，同样的，直接将整个 jsbn.js 文件剥离下来进行本地调试。

这里其实在 rsa.js 文件的第一行有一句注释：`// Depends on jsbn.js and rng.js`，我们可以猜测 rsa.js 是可能依赖 jsbn.js 和 rng.js 这两个文件的。

有了 jsbn.js 的代码，再次进行调试，会发现又提示 `navigator` 和 `SecureRandom` 未定义，`navigator` 我们已经非常熟悉了，是浏览器的相关信息，一般情况下直接定义为空即可（`navigator = {};`）；将鼠标移到 `SecureRandom` 函数上面，可以发现是调用了 rng.js 里面的方法，同样的，直接将整个 rng.js 文件剥离下来进行本地调试。这里就证实了前面我们的猜想，rsa.js 确实是依赖 jsbn.js 和 rng.js 的。

我们注意到，这里在 rng.js 文件的第一行，同样有一句注释：`// Random number generator - requires a PRNG backend, e.g. prng4.js`，表明 rng.js 是随机数生成器，需要 PRNG 后端，例如 prng4.js，在密码学中，PRNG 全称是 pseudorandom number generator，即伪随机数生成器，是指通过特定算法生成一系列的数字，使得这一系列的数字看起来是随机的，但是实际是确定的，所以叫伪随机数，感兴趣的朋友可以深入研究一下，在这里我们知道 rng.js 可能还依赖于 prng4.js，需要进一步调试才清楚。

rsa.js、jsbn.js、rng.js 都齐全了，再次本地调试，会发现 rng.js 里面的 `rng_psize` 未定义，鼠标放上去看到 `rng_psize` 就是一个定值 256，在右边的 Global 全局变量里也可以看到值为 256，尝试搜索一下 `rng_psize`，可以发现在 prng4.js 里面有定义 `var rng_psize = 256;`，果然和注释说得一样，rng.js 是依赖 prng4.js 的，但是这里似乎直接定义一下 `rng_psize` 就行了。

直接在本地代码定义一下 `var rng_psize = 256;`，再次进行调试，此时又会提示 rng.js 里缺少 `prng_newstate()` 对象，再次回到开发者工具，可以看到 `prng_newstate()` 是 prng4.js 里面的方法，果然 rng.js 和 prng4.js 的关系并不简单，同样的，我们也直接将整个 prng4.js 文件剥离下来进行本地调试。

再次调试，运行无误，可以成功拿到加密后的密码了：

#### 逻辑总结
1.  加密入口可以在 index 首页找到，用到了 rsa.js 里面的三个加密函数 `RSAKey()`、`setPublic()`、`encrypt()`； 1.  rsa.js 里的 `BigInteger()` 函数依赖 jsbn.js，`SecureRandom()` 函数依赖 rng.js； 1.  rng.js 里的变量 `rng_psize` 在 prng4.js 中定义，`prng_newstate()` 函数也依赖 prng4.js； 
要将 rsa.js、jsbn.js、rng.js、prng4.js 这四个 JS 加密文件完整的剥离下来才能还原整个加密过程。

### 完整代码

GitHub 关注 K 哥爬虫：https://github.com/kuaidaili，持续分享爬虫相关代码！欢迎 star ！

**以下只演示部分关键代码**，完整代码仓库地址：https://github.com/kuaidaili/crawler/

#### 参数 JS 加密关键代码

```
navigator = {};

// ================== prng4.js begin ================== //

function Arcfour() {}

function ARC4init(key) {}

function ARC4next() {}

// 此处省略 N 个函数

var rng_psize = 256;

// ================== prng4.js end ================== //

// ================== rng.js begin ================== //

var rng_state;
var rng_pool;
var rng_pptr;

function rng_seed_int(x) {}

function rng_seed_time() {}

// 此处省略 N 个函数

function SecureRandom() {}

SecureRandom.prototype.nextBytes = rng_get_bytes;

// ================== rng.js end ================== //

// ================== jsbn.js begin ================== //

var dbits;

var canary = 0xdeadbeefcafe;
var j_lm = ((canary &amp; 0xffffff) == 0xefcafe);

function BigInteger(a, b, c) {}

function nbi() {}

// 此处省略 N 个函数

// protected
BigInteger.prototype.copyTo = bnpCopyTo;
BigInteger.prototype.fromInt = bnpFromInt;
BigInteger.prototype.fromString = bnpFromString;
BigInteger.prototype.clamp = bnpClamp;
BigInteger.prototype.dlShiftTo = bnpDLShiftTo;
BigInteger.prototype.drShiftTo = bnpDRShiftTo;
BigInteger.prototype.lShiftTo = bnpLShiftTo;
BigInteger.prototype.rShiftTo = bnpRShiftTo;
BigInteger.prototype.subTo = bnpSubTo;
BigInteger.prototype.multiplyTo = bnpMultiplyTo;
BigInteger.prototype.squareTo = bnpSquareTo;
BigInteger.prototype.divRemTo = bnpDivRemTo;
BigInteger.prototype.invDigit = bnpInvDigit;
BigInteger.prototype.isEven = bnpIsEven;
BigInteger.prototype.exp = bnpExp;

// public
BigInteger.prototype.toString = bnToString;
BigInteger.prototype.negate = bnNegate;
BigInteger.prototype.abs = bnAbs;
BigInteger.prototype.compareTo = bnCompareTo;
BigInteger.prototype.bitLength = bnBitLength;
BigInteger.prototype.mod = bnMod;
BigInteger.prototype.modPowInt = bnModPowInt;

// "constants"
BigInteger.ZERO = nbv(0);
BigInteger.ONE = nbv(1);

// ================== jsbn.js end ================== //

// ================== rsa.js begin ================== //

function parseBigInt(str, r) {}

function linebrk(s, n) {}

function byte2Hex(b) {}

function pkcs1pad2(s, n) {}

function RSAKey() {}

function RSASetPublic(N, E) {}

function RSADoPublic(x) {}

function RSAEncrypt(text) {}

// protected
RSAKey.prototype.doPublic = RSADoPublic;

// public
RSAKey.prototype.setPublic = RSASetPublic;
RSAKey.prototype.encrypt = RSAEncrypt;
//RSAKey.prototype.encrypt_b64 = RSAEncryptB64;

// ================== rsa.js end ================== //

function getEncryptedPassword(password) {
    var public_key = "00bdf3db924714b9c4ddd144910071c282e235ac51371037cf89fa08f28b9105b6326338ed211280154c645bf81bae4184c2b52e2b02b0953e7aa8b25a8e212a0b";
    var public_length = "10001";
    var rsa = new RSAKey();
    rsa.setPublic(public_key, public_length);
    return rsa.encrypt(password);
}

// 测试样例
console.log(getEncryptedPassword("123456"))

```

#### Python 登录关键代码

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import execjs
import requests

from lxml import etree
from PIL import Image


index_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/'
login_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/'
code_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/'

headers = {
    'Host': '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/',
    'Referer': '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/',
    'Origin': '脱敏处理，完整代码关注 GitHub：https://github.com/kuaidaili/crawler/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
session = requests.session()


def get_encrypted_password(password):
    with open('encrypt.js', 'r', encoding='utf-8') as f:
        yunmall_js = f.read()
    encrypted_password = execjs.compile(yunmall_js).call('getEncryptedPassword', password)
    return encrypted_password


def get_csrf_token_cookie():
    response = session.get(url=index_url, headers=headers)
    tree = etree.HTML(response.text)
    csrf_token = tree.xpath("//input[@name='_csrfToken']/@value")[0]
    cookies = response.cookies.get_dict()
    # print(csrf_token, cookies)
    return csrf_token, cookies


def get_very_code(cookies):
    response = session.get(url=code_url, cookies=cookies, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image.show()
    very_code = input('请输入验证码: ')
    return very_code


def login(csrf_token, very_code, cookies, username, encrypted_password):
    data = {
        'u[loginType]': 'name',
        'u[phone]': username,
        'u[password]': encrypted_password,
        'u[veryCode]': very_code,
        'u[token]': '',
        '_csrfToken': csrf_token
    }
    header_info = {
        'X-Requested-With': 'XMLHttpRequest',
    }
    headers.update(header_info)
    response = session.post(url=login_url, data=data, cookies=cookies, headers=headers)
    response.encoding = 'utf-8-sig'
    response_code = response.text
    # print(response_code)
    status_code = {
        '31': '恭喜，登陆成功。',
        '32': '登陆失败。',
        '33': '用户名或密码错误。',
        '35': '该用户已被管理员锁定。',
        '311': '该账号已绑定设备，请在绑定的设备登陆。',
        '20001': '验证码填写错误!'
    }
    try:
        print(status_code[response_code])
    except KeyError:
        print('请求超时！')


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    if len(password) &gt; 32:
        raise Exception('请输入正确的密码！')
    encrypted_password = get_encrypted_password(password)
    csrf_token, cookies = get_csrf_token_cookie()
    very_code = get_very_code(cookies)
    login(csrf_token, very_code, cookies, username, encrypted_password)


if __name__ == '__main__':
    main()

```
