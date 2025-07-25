## 逆向目标

+ 目标：某米账号登录

+ 主页：aHR0cHM6Ly9hY2NvdW50LnhpYW9taS5jb20v
+ 接口：aHR0cHM6Ly9hY2NvdW50LnhpYW9taS5jb20vcGFzcy9zZXJ2aWNlTG9naW5BdXRoMg==

+ 逆向参数：Form Data:<code>hash:A5CF6D92A2E2EA2527E04E180C103AA6</code>



## 抓包分析

来到X米的登录页面，随便输入一个账号密码登陆，抓包定位到登录接口为<code>aHR0cHM6Ly9hY2NvdW50LnhpYW9taS5jb20vcGFzcy9zZXJ2aWNlTG9naW5BdXRoMg==</code>

![微信截图_20250523211555](./img/微信截图_20250523211555.png)

POST 请求，Form Data 里的参数比较多，分析一下主要参数：

+ **serviceParam**: `{"checkSafePhone":false,"checkSafeAddress":false,"lsrp_score":0.0}`，从参数的字面意思来看，似乎是在检查手机和地址是否安全，至于具体是什么含义，暂时不得而知，也不知道是在哪个地方设置的。
+ **callback**: `https://account.xiaomi.com/sts?sign=ZvAtJIzsDsFe60LdaPa76nNNP58%3D&followup=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fauth%2Fsecurity%2Fhome&sid=passport`，回调链接，一般来说是固定的，后面带有 followup 和 sid 参数。
+ **qs**: `%3Fcallback%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fsts%253Fsign%253DZvAtJIzsDsFe60LdaPa76nNNP58%25253D%2526followup%253Dhttps%25253A%25252F%25252Faccount.xiaomi.com%25252Fpass%25252Fauth%25252Fsecurity%25252Fhome%2526sid%253Dpassport%26sid%3Dpassport%26_group%3DDEFAULT`，把 qs 的值格式化一下可以发现，其实是 callback、sign、sid、_qrsize 四个值按照 URL 编码进行组合得到的。
+ **_sign**: `2&V1_passport&BUcblfwZ4tX84axhVUaw8t6yi2E=`，这个一串看起来是经过某种加密后得到的，也有可能是网页源码中的值。
+ **user**: `k5PbpD4SbVHewBnjYF2ijQ==`，加密后的用户名
+ **hash**: `FCEA920F7412B5DA7BE0CF42B8C93759`，加密后的密码。



## 参数逆向

### 基本参数

先来看一下 `serviceParam` 等基本参数，一般思路我们是先直接搜索一下看看能不能直接找到这个值，搜索发现 `serviceParam` 关键字在一个 302 重定向请求里：

![微信截图_20250524152230](./img/微信截图_20250524152230.png)



我们注意到，当只输入登录的主页 aHR0cHM6Ly9hY2NvdW50LnhpYW9taS5jb20v，它会有两次连续的 302 重定向，来重点分析一下这两次重定向。

第一次重定向，新的网址里有 `followup`、`callback`、`sign`、`sid` 参数，这些我们都是在后面的登录请求中要用到的。

![微信截图_20250524152444](./img/微信截图_20250524152444.png)

第二次重定向，新的网址里同样有 `followup`、`callback`、`sign`、`sid` 参数，此外还有 `serviceParam`、`qs` 参数，同样也是后面的登录请求需要用到的。

![微信截图_20250524152230](./img/微信截图_20250524152230.png)

找到了参数的来源，直接从第二次重定向的链接里提取各项参数，这里用到了 `response.history[1].headers['Location']` 来提取页面第二次重定向返回头里的目标地址，`urllib.parse.urlparse` 来解析重定向链接 URL 的结构，`urllib.parse.parse_qs` 提取参数，返回字典，代码样例：

~~~ python
import requests
import urllib.parse

headers = {
    'Host': 'account.xiaomi.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
}
index_url = 'https://account.xiaomi.com/'
response = requests.get(url=index_url, headers=headers)
location_url = response.history[1].headers['Location']
urlparse = urllib.parse.urlparse(location_url)
query_dict  = urllib.parse.parse_qs(urlparse.query)

need_theme = query_dict['needTheme'][0]
show_active_x = query_dict['showActiveX'][0]
service_param = query_dict['serviceParam'][0]
callback = query_dict['callback'][0]
qs = query_dict['qs'][0]
sid = query_dict['sid'][0]
_sign = query_dict['_sign'][0]
~~~

![微信截图_20250524162019](./img/微信截图_20250524162019.png)

![微信截图_20250524161215](./img/微信截图_20250524161215.png)

![微信截图_20250524162005](./img/微信截图_20250524162005.png)

![微信截图_20250524162453](./img/微信截图_20250524162453.png)



### hash

其他参数都齐全了，现在还差一个加密后的密码 hash，一般来讲这种都是通过 JS 加密的，老方法，全局搜索 `hash` 或者 `hash:`，可以在 `2395.f58d7844.chunk.js` 文件里面看到有一句：` hash: v()(i.password).toUpperCase()`，很明显是将明文的密码经过加密处理后再全部转为大写：

![微信截图_20250524163226](./img/微信截图_20250524163226.png)

在这里打上断点后发现重点是这个 S()，鼠标移上去会发现其实是调用了 `runtime-main.33ae4da8.js` 的一个匿名函数，我们在匿名函数的 return 位置埋下断点进行调试：

![微信截图_20250524163828](./img/微信截图_20250524163828.png)

最终定位到这个函数：

![微信截图_20250524164020](./img/微信截图_20250524164020.png)

实际是下面这个函数：

~~~ javascript
e.exports = function(e, n) {
    if (void 0 === e || null === e)
        throw new Error("Illegal argument " + e);
    var r = t.wordsToBytes(u(e, n));
    return n && n.asBytes ? r : n && n.asString ? s.bytesToString(r) : t.bytesToHex(r)
}
~~~

可以看到传进来的 e 是明文的密码，最后的 return 语句是一个三目运算符，由于 n 是 undefined，所以最后 return 的实际上是 `t.bytesToHex(r)`，其值正是加密后的密码，只不过所有字母都是小写，按照正常思维，我们肯定是开始扣 JS 了，这里传入了参数 r，`var r = t.wordsToBytes(u(e, n));`，先跟进 u 这个函数看看：

![微信截图_20250524170205](./img/微信截图_20250524170205.png)

可以看到 u 函数比较复杂，挨个去扣比较麻烦而且还容易出错并且代码太多也不好定位错误的地方，所以这里需要转变一下思路，先来看看 `t.bytesToHex(r)` 是个什么东西，跟进到这个函数：

![微信截图_20250524170418](./img/微信截图_20250524170418.png)

~~~ javascript
 bytesToHex: function(e) {
          for (var t = [], n = 0; n < e.length; n++)
            t.push((e[n] >>> 4).toString(16)),
            t.push((15 & e[n]).toString(16));
          return t.join("")
        },
~~~

解读一下这段代码，传进来的 e 是一个 16 位的 Array 对象，定义了一个 t 空数组，经过一个循环，依次取 Array 对象里的值，第一次经过无符号右移运算（>>>）后，转为十六进制的字符串，将结果添加到 t 数组的末尾。第二次进行位运算（&）后，同样转为十六进制的字符串，将结果添加到 t 数组的末尾。也就是说，原本传进来的 16 位的 Array 对象，每一个值都经过了两次操作，那么最后结果的 t 数组中就会有 32 个值，最后再将 t 数组转换成字符串返回。

结合一下调用的函数名称，我们来捋一下整个流程，首先调用 `wordsToBytes()` 方法将明文密码字符串转为 byte 数组，无论密码的长度如何，最后得到的 byte 数组都是 16 位的，然后调用 `bytesToHex()` 方法，循环遍历生成的 byte 类型数组，让其生成 32 位字符串。

无论密码长度如何，最终得到的密文都是 32 位的，而且都由字母和数字组成，这些特点很容易让人想到 MD5 加密，将明文转换成 byte 数组后进行随机哈希，对 byte 数组进行摘要，得到摘要 byte 数组，循环遍历 byte 数组，生成固定位数的字符串，这不就是 MD5 的加密过程么？

直接把密码拿来进行 MD5 加密，和网站的加密结果进行对比，可以发现确实是一样的，验证了猜想是正确的：

![微信截图_20250524170804](./img/微信截图_20250524170804.png)

![微信截图_20250524170804](./img/微信截图_20250524170751.png)



既然如此，直接可以使用 Python 的 hashlib 模块来实现就 OK 了，根本不需要去死扣代码，代码样例：

~~~ python
import hashlib

password = "647561"
encrypted_password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest().upper()
print(encrypted_password)
~~~

![微信截图_20250524171235](./img/微信截图_20250524171235.png)



### user参数加密

​	从找到密码加密的地方发现，参数`user `已经被加密了，稍微往上追溯，找到了加密的点

![微信截图_20250524174129](./img/微信截图_20250524174129.png)



加密函数如图

![微信截图_20250524174418](./img/微信截图_20250524174418.png)

~~~ javascript
    function yt(t) {
      t = t || {};
      var e = function(t) {
        for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
          var n = Math.floor(Math.random() * e.length);
          i += e.substring(n, n + 1)
        }
        return i
      }(16)
        , i = new gt({});
      i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
      var r = i.encrypt(window.btoa(e))
        , s = o().parse("0102030405060708")
        , h = o().parse(e)
        , u = window.btoa(Object.keys(t).join(","))
        , c = {};
      return Object.keys(t).forEach((function(e) {
        var i = t[e]
          , r = n().encrypt(i, h, {
          iv: s,
          padding: a()
        });
        r = r.toString(),
        c[e] = r
      }
      )),
      {
        EUI: "".concat(r, ".").concat(u),
        encryptedParams: c
      }
    }
~~~



稍微更改一下形式

~~~ javascript
window = global;
const JSEncrypt = require('jsencrypt'); //暂时不知道为啥要导入这个库
const CryptoJS = require('crypto-js'); //暂时不知道为啥要导入这个库

function EncryptParams(t) {
    t = t || {};
    var e = function(t) {
      for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
        var n = Math.floor(Math.random() * e.length);
        i += e.substring(n, n + 1)
      }
      return i
    }(16)
      , i = new JSEncrypt({}); //不知道为啥要用JSEncrypt
    i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    var r = i.encrypt(window.btoa(e))
      , s = CryptoJS.enc.Utf8.parse("0102030405060708") //不知道为啥要用CryptoJS.enc.Utf8
      , h = CryptoJS.enc.Utf8.parse(e) //不知道为啥要用CryptoJS.enc.Utf8
      , u = window.btoa(Object.keys(t).join(","))
      , c = {};
    return Object.keys(t).forEach((function(e) {
      var i = t[e]
        , r = CryptoJS.AES.encrypt(i, h, {
        iv: s,
        padding: CryptoJS.pad.Pkcs7 //这里的padding暂时不知道为啥要这样写
      });
      r = r.toString(),
      c[e] = r
    }
    )),
    {
      EUI: "".concat(r, ".").concat(u),
      encryptedParams: c
    }
  }
  
  const user = "18814317942"
  const EncryptParam = EncryptParams({
      "user":user 
    })
 console.log(EncryptParam)
 console.log("EUI:" + EncryptParam.EUI)
 console.log("EncryptedParams:" + EncryptParam.encryptedParams["user"])
~~~

如此即可成功加密得到参数



## 登录代码

如下：

~~~ python
import requests
import urllib.parse
import hashlib
import execjs

def get_encrypted_params(user):
        with open('EasyEncrpyt.js', 'r', encoding='utf-8') as f:
                www_xiaomiaccount_js = f.read()
        encrypted_params = execjs.compile(www_xiaomiaccount_js).call('EncryptParams', {"user":user})
        return encrypted_params

def Login(user,password):
    headers = {
        'Host': 'account.xiaomi.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    }

    index_url = 'https://account.xiaomi.com/'
    response = requests.get(url=index_url, headers=headers)
    location_url = response.history[1].headers['Location']
    referer = location_url.replace("https://account.xiaomi.com/fe/service/login","https://account.xiaomi.com/fe/service/login/password") + "&_locale=zh_CN"
    cookie = response.history[1].headers['set-cookie'].split(";")[0] + ";pass_ua=web; uLocale=zh_CN; passInfo=login-end;"
    cookies = {
        "deviceId": response.history[1].headers['set-cookie'].split(";")[0],
        "pass_ua":"web",
        "uLocale":"zh_CN",
        "passInfo":"login-end"
    }
    urlparse = urllib.parse.urlparse(location_url)
    query_dict  = urllib.parse.parse_qs(urlparse.query)

    EncryptParams = get_encrypted_params(user)
    user = EncryptParams["encryptedParams"]["user"]

    encrypted_password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest().upper()

    data = {
        "bizDeviceType": '',
        "need_theme": query_dict['needTheme'][0],
        "theme": '',
        "show_active_x":query_dict['showActiveX'][0],
        "service_param": query_dict['serviceParam'][0],
        "callback": query_dict['callback'][0],
        "qs": query_dict['qs'][0],
        "sid": query_dict['sid'][0],
        "_sign": query_dict['_sign'][0],
        "user": user,
        'cc': '+86',
        "password": encrypted_password,
        '_json': True,
        "policyName": "miaccount",
        "captCode": ""
    }

    login_url = "https://account.xiaomi.com/pass/serviceLoginAuth2"

    login_headers = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding": "gzip,deflate,br,zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection":"keep-alive",
        "Content-Length": "878",
        'Host': 'account.xiaomi.com',
        "Origin":"https://account.xiaomi.com",
        "EUI": EncryptParams["EUI"],
        "Referer":referer,
        "Cookie":cookie,
        "sec-ch-ua":'"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":'"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        "x-requested-with":"XMLHttpRequest"
    }
    login_headers["Content-Length"] = "880"

    response = requests.session().post(url=login_url, headers=login_headers,cookies=cookies, data=data)
    print(response.text)

user  = input("请输入账号：")
password = input("请输入密码：")
Login(user, password)

~~~



<code>EasyEncrpyt.js</code>

~~~ javascript
window = global;
const JSEncrypt = require('jsencrypt'); //暂时不知道为啥要导入这个库
const CryptoJS = require('crypto-js'); //暂时不知道为啥要导入这个库

function EncryptParams(t) {
    t = t || {};
    var e = function(t) {
      for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
        var n = Math.floor(Math.random() * e.length);
        i += e.substring(n, n + 1)
      }
      return i
    }(16)
      , i = new JSEncrypt({}); //不知道为啥要用JSEncrypt
    i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    var r = i.encrypt(window.btoa(e))
      , s = CryptoJS.enc.Utf8.parse("0102030405060708") //不知道为啥要用CryptoJS.enc.Utf8
      , h = CryptoJS.enc.Utf8.parse(e) //不知道为啥要用CryptoJS.enc.Utf8
      , u = window.btoa(Object.keys(t).join(","))
      , c = {};
    return Object.keys(t).forEach((function(e) {
      var i = t[e]
        , r = CryptoJS.AES.encrypt(i, h, {
        iv: s,
        padding: CryptoJS.pad.Pkcs7 //这里的padding暂时不知道为啥要这样写
      });
      r = r.toString(),
      c[e] = r
    }
    )),
    {
      EUI: "".concat(r, ".").concat(u),
      encryptedParams: c
    }
  }
  
  const user = "" //输入账号
  const EncryptParam = EncryptParams({
      "user":user 
    })
 console.log(EncryptParam)
 console.log("EUI:" + EncryptParam.EUI)
 console.log("EncryptedParams:" + EncryptParam.encryptedParams["user"])
~~~



## 总结

有的时候需要我们转变思路，不一定每次都要死扣 JS 代码，相对较容易的站点的加密方式无非就是那么几种，有的是稍微进行了改写，有的是把密钥、偏移量等参数隐藏了，有的是把加密解密过程给你混淆了，让你难以理解，如果你对常见的加密方式和原理比较熟悉的话，有时候只需要搞清楚他用的什么加密方式，或者拿到了密钥、偏移量等关键参数，就完全可以自己还原整个加密过程！



## 结果

不知道为啥，输入正确的账号密码却提示验证失败。。。难受



## 登录成功

改变了一下<code>python</code>代码，如下：

~~~ python
import requests
import execjs
from loguru import logger
from urllib.parse import unquote

session = requests.Session()

with open("Encrypt.js", "r", encoding='utf-8') as f:
    js_code = execjs.compile(f.read())

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

def get_index() -> str:
    url = "https://account.xiaomi.com/"
    response = requests.get(url, headers=headers, allow_redirects=False)
    logger.success(response)
    callback_url = response.headers.get("Location")
    logger.debug(callback_url)
    return callback_url

def get_second() -> str:
    callback_url = get_index()
    response = requests.get(callback_url, headers=headers, allow_redirects=False)
    logger.success(response)

    start_data = response.headers.get('Location')
    logger.debug(start_data)

    logger.debug(response.cookies)
    session.cookies.update(response.cookies)
    return start_data

def get_data(start_data: str):
    js_data = js_code.call("get_user_info", "", "")  # 账号密码
    logger.debug(js_data)

    data_dict = start_data.split("&")
    data_dict = [i.split("=") for i in data_dict]
    data_dict = {i[0]: i[1] for i in data_dict}
    logger.debug(data_dict)

    headers["Accept"] = "application/json, text/plain, */*"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["Referer"] = start_data + "&_locale=zh_CN"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Origin"] = "https://account.xiaomi.com"
    
    url = "https://account.xiaomi.com/pass/serviceLoginAuth2"

    headers["EUI"] = js_data["EUI"]

    data = {
        "bizDeviceType": data_dict["bizDeviceType"],
        "needTheme": data_dict["needTheme"],
        "theme": data_dict["theme"],
        "showActiveX": data_dict["showActiveX"],
        "serviceParam": unquote(data_dict["serviceParam"]),
        "callback": unquote(data_dict["callback"]),
        "qs": unquote(data_dict["qs"]),
        "sid": data_dict["sid"],
        "_sign": unquote(data_dict["_sign"]),
        "user": js_data["user"],
        "cc": "+86",
        "hash": js_data["password"],
        "_json": "true",
        "policyName": "miaccount",
        "captCode": ""
    }

    response = session.post(url, headers=headers, data=data)

    logger.success(response)
    logger.info(response.text)
    logger.debug(response.cookies)

def main():
    start_data = get_second()
    get_data(start_data)

if __name__ == "__main__":
    main()

~~~



重新从官网扣了一遍代码

~~~ javascript
  window = global;
  navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
  }
  const CryptoJS = require('crypto-js'); 

    var X = function() {
            function t() {
                this.i = 0,
                this.j = 0,
                this.S = []
            }
            return t.prototype.init = function(t) {
                var e, i, r;
                for (e = 0; e < 256; ++e)
                    this.S[e] = e;
                for (i = 0,
                e = 0; e < 256; ++e)
                    i = i + this.S[e] + t[e % t.length] & 255,
                    r = this.S[e],
                    this.S[e] = this.S[i],
                    this.S[i] = r;
                this.i = 0,
                this.j = 0
            }
            ,
            t.prototype.next = function() {
                var t;
                return this.i = this.i + 1 & 255,
                this.j = this.j + this.S[this.i] & 255,
                t = this.S[this.i],
                this.S[this.i] = this.S[this.j],
                this.S[this.j] = t,
                this.S[t + this.S[this.i] & 255]
            }
            ,
            t
        }();
        var $, J, tt = 256, et = null;
        if (null == et) {
            et = [],
            J = 0;
            var it = void 0;
            if (window.crypto && window.crypto.getRandomValues) {
                var rt = new Uint32Array(256);
                for (window.crypto.getRandomValues(rt),
                it = 0; it < rt.length; ++it)
                    et[J++] = 255 & rt[it]
            }
            var nt = 0
              , st = function t(e) {
                if ((nt = nt || 0) >= 256 || J >= tt)
                    window.removeEventListener ? window.removeEventListener("mousemove", t, !1) : window.detachEvent && window.detachEvent("onmousemove", t);
                else
                    try {
                        var i = e.x + e.y;
                        et[J++] = 255 & i,
                        nt += 1
                    } catch (r) {}
            };
            window.addEventListener ? window.addEventListener("mousemove", st, !1) : window.attachEvent && window.attachEvent("onmousemove", st)
        };
    function ot() {
            if (null == $) {
                for ($ = new X; J < tt; ) {
                    var t = Math.floor(65536 * Math.random()); //卡住的地方，这里是随机数无法做到一模一样
                    et[J++] = 255 & t
                }
                for ($.init(et),
                J = 0; J < et.length; ++J)
                    et[J] = 0;
                J = 0
            }
            return $.next()
        };
    var ht = function() {
            function t() {}
            return t.prototype.nextBytes = function(t) {
                for (var e = 0; e < t.length; ++e)
                    t[e] = ot()
            }
            ,
            t
        }();
    function W(t) {
            var e, i = 1;
            return 0 != (e = t >>> 16) && (t = e,
            i += 16),
            0 != (e = t >> 8) && (t = e,
            i += 8),
            0 != (e = t >> 4) && (t = e,
            i += 4),
            0 != (e = t >> 2) && (t = e,
            i += 2),
            0 != (e = t >> 1) && (t = e,
            i += 1),
            i
        };
    var v = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", m = "=";
    function b(t) {
            var e, i, r = "";
            for (e = 0; e + 3 <= t.length; e += 3)
                i = parseInt(t.substring(e, e + 3), 16),
                r += v.charAt(i >> 6) + v.charAt(63 & i);
            for (e + 1 == t.length ? (i = parseInt(t.substring(e, e + 1), 16),
            r += v.charAt(i << 2)) : e + 2 == t.length && (i = parseInt(t.substring(e, e + 2), 16),
            r += v.charAt(i >> 2) + v.charAt((3 & i) << 4)); (3 & r.length) > 0; )
                r += m;
            return r
        }
  var T, E, w = function(t) {
            var e;
            if (void 0 === T) {
                var i = "0123456789ABCDEF"
                  , r = " \f\n\r\t\xa0\u2028\u2029";
                for (T = {},
                e = 0; e < 16; ++e)
                    T[i.charAt(e)] = e;
                for (i = i.toLowerCase(),
                e = 10; e < 16; ++e)
                    T[i.charAt(e)] = e;
                for (e = 0; e < r.length; ++e)
                    T[r.charAt(e)] = -1
            }
            var n = []
              , s = 0
              , o = 0;
            for (e = 0; e < t.length; ++e) {
                var h = t.charAt(e);
                if ("=" == h)
                    break;
                if (-1 != (h = T[h])) {
                    if (void 0 === h)
                        throw new Error("Illegal character at offset " + e);
                    s |= h,
                    ++o >= 2 ? (n[n.length] = s,
                    s = 0,
                    o = 0) : s <<= 4
                }
            }
            if (o)
                throw new Error("Hex encoding incomplete: 4 bits missing");
            return n
        },D = {
            decode: function(t) {
                var e;
                if (void 0 === E) {
                    var i = "= \f\n\r\t\xa0\u2028\u2029";
                    for (E = Object.create(null),
                    e = 0; e < 64; ++e)
                        E["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(e)] = e;
                    for (E["-"] = 62,
                    E._ = 63,
                    e = 0; e < i.length; ++e)
                        E[i.charAt(e)] = -1
                }
                var r = []
                  , n = 0
                  , s = 0;
                for (e = 0; e < t.length; ++e) {
                    var o = t.charAt(e);
                    if ("=" == o)
                        break;
                    if (-1 != (o = E[o])) {
                        if (void 0 === o)
                            throw new Error("Illegal character at offset " + e);
                        n |= o,
                        ++s >= 4 ? (r[r.length] = n >> 16,
                        r[r.length] = n >> 8 & 255,
                        r[r.length] = 255 & n,
                        n = 0,
                        s = 0) : n <<= 6
                    }
                }
                switch (s) {
                case 1:
                    throw new Error("Base64 encoding incomplete: at least 2 bits missing");
                case 2:
                    r[r.length] = n >> 10;
                    break;
                case 3:
                    r[r.length] = n >> 16,
                    r[r.length] = n >> 8 & 255
                }
                return r
            },
            re: /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
            unarmor: function(t) {
                var e = D.re.exec(t);
                if (e)
                    if (e[1])
                        t = e[1];
                    else {
                        if (!e[2])
                            throw new Error("RegExp out of sync");
                        t = e[2]
                    }
                return D.decode(t)
            }
        }, x = 1e13, B = function() {
            function t(t) {
                this.buf = [+t || 0]
            }
            return t.prototype.mulAdd = function(t, e) {
                var i, r, n = this.buf, s = n.length;
                for (i = 0; i < s; ++i)
                    (r = n[i] * t + e) < x ? e = 0 : r -= (e = 0 | r / x) * x,
                    n[i] = r;
                e > 0 && (n[i] = e)
            }
            ,
            t.prototype.sub = function(t) {
                var e, i, r = this.buf, n = r.length;
                for (e = 0; e < n; ++e)
                    (i = r[e] - t) < 0 ? (i += x,
                    t = 1) : t = 0,
                    r[e] = i;
                for (; 0 === r[r.length - 1]; )
                    r.pop()
            }
            ,
            t.prototype.toString = function(t) {
                if (10 != (t || 10))
                    throw new Error("only base 10 is supported");
                for (var e = this.buf, i = e[e.length - 1].toString(), r = e.length - 2; r >= 0; --r)
                    i += (x + e[r]).toString().substring(1);
                return i
            }
            ,
            t.prototype.valueOf = function() {
                for (var t = this.buf, e = 0, i = t.length - 1; i >= 0; --i)
                    e = e * x + t[i];
                return e
            }
            ,
            t.prototype.simplify = function() {
                var t = this.buf;
                return 1 == t.length ? t[0] : this
            }
            ,
            t
        }(),R = "\u2026", A = /^(\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/, O = /^(\d\d\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/;
        function _(t, e) {
            return t.length > e && (t = t.substring(0, e) + R),
            t
        }
        var V, I = function() {
            function t(e, i) {
                this.hexDigits = "0123456789ABCDEF",
                e instanceof t ? (this.enc = e.enc,
                this.pos = e.pos) : (this.enc = e,
                this.pos = i)
            }
            return t.prototype.get = function(t) {
                if (void 0 === t && (t = this.pos++),
                t >= this.enc.length)

                    throw new Error("Requesting byte offset " + t + " on a stream of length " + this.enc.length);
                return "string" === typeof this.enc ? this.enc.charCodeAt(t) : this.enc[t]
            }
            ,
            t.prototype.hexByte = function(t) {
                return this.hexDigits.charAt(t >> 4 & 15) + this.hexDigits.charAt(15 & t)
            }
            ,
            t.prototype.hexDump = function(t, e, i) {
                for (var r = "", n = t; n < e; ++n)
                    if (r += this.hexByte(this.get(n)),
                    !0 !== i)
                        switch (15 & n) {
                        case 7:
                            r += "  ";
                            break;
                        case 15:
                            r += "\n";
                            break;
                        default:
                            r += " "
                        }
                return r
            }
            ,
            t.prototype.isASCII = function(t, e) {
                for (var i = t; i < e; ++i) {
                    var r = this.get(i);
                    if (r < 32 || r > 176)
                        return !1
                }
                return !0
            }
            ,
            t.prototype.parseStringISO = function(t, e) {
                for (var i = "", r = t; r < e; ++r)
                    i += String.fromCharCode(this.get(r));
                return i
            }
            ,
            t.prototype.parseStringUTF = function(t, e) {
                for (var i = "", r = t; r < e; ) {
                    var n = this.get(r++);
                    i += n < 128 ? String.fromCharCode(n) : n > 191 && n < 224 ? String.fromCharCode((31 & n) << 6 | 63 & this.get(r++)) : String.fromCharCode((15 & n) << 12 | (63 & this.get(r++)) << 6 | 63 & this.get(r++))
                }
                return i
            }
            ,
            t.prototype.parseStringBMP = function(t, e) {
                for (var i, r, n = "", s = t; s < e; )
                    i = this.get(s++),
                    r = this.get(s++),
                    n += String.fromCharCode(i << 8 | r);
                return n
            }
            ,
            t.prototype.parseTime = function(t, e, i) {
                var r = this.parseStringISO(t, e)
                  , n = (i ? A : O).exec(r);
                return n ? (i && (n[1] = +n[1],
                n[1] += +n[1] < 70 ? 2e3 : 1900),
                r = n[1] + "-" + n[2] + "-" + n[3] + " " + n[4],
                n[5] && (r += ":" + n[5],
                n[6] && (r += ":" + n[6],
                n[7] && (r += "." + n[7]))),
                n[8] && (r += " UTC",
                "Z" != n[8] && (r += n[8],
                n[9] && (r += ":" + n[9]))),
                r) : "Unrecognized time: " + r
            }
            ,
            t.prototype.parseInteger = function(t, e) {
                for (var i, r = this.get(t), n = r > 127, s = n ? 255 : 0, o = ""; r == s && ++t < e; )
                    r = this.get(t);
                if (0 === (i = e - t))
                    return n ? -1 : 0;
                if (i > 4) {
                    for (o = r,
                    i <<= 3; 0 == (128 & (+o ^ s)); )
                        o = +o << 1,
                        --i;
                    o = "(" + i + " bit)\n"
                }
                n && (r -= 256);
                for (var h = new B(r), a = t + 1; a < e; ++a)
                    h.mulAdd(256, this.get(a));
                return o + h.toString()
            }
            ,
            t.prototype.parseBitString = function(t, e, i) {
                for (var r = this.get(t), n = "(" + ((e - t - 1 << 3) - r) + " bit)\n", s = "", o = t + 1; o < e; ++o) {
                    for (var h = this.get(o), a = o == e - 1 ? r : 0, u = 7; u >= a; --u)
                        s += h >> u & 1 ? "1" : "0";
                    if (s.length > i)
                        return n + _(s, i)
                }
                return n + s
            }
            ,
            t.prototype.parseOctetString = function(t, e, i) {
                if (this.isASCII(t, e))
                    return _(this.parseStringISO(t, e), i);
                var r = e - t
                  , n = "(" + r + " byte)\n";
                r > (i /= 2) && (e = t + i);
                for (var s = t; s < e; ++s)
                    n += this.hexByte(this.get(s));
                return r > i && (n += R),
                n
            }
            ,
            t.prototype.parseOID = function(t, e, i) {
                for (var r = "", n = new B, s = 0, o = t; o < e; ++o) {
                    var h = this.get(o);
                    if (n.mulAdd(128, 127 & h),
                    s += 7,
                    !(128 & h)) {
                        if ("" === r)
                            if ((n = n.simplify())instanceof B)
                                n.sub(80),
                                r = "2." + n.toString();
                            else {
                                var a = n < 80 ? n < 40 ? 0 : 1 : 2;
                                r = a + "." + (n - 40 * a)
                            }
                        else
                            r += "." + n.toString();
                        if (r.length > i)
                            return _(r, i);
                        n = new B,
                        s = 0
                    }
                }
                return s > 0 && (r += ".incomplete"),
                r
            }
            ,
            t
        }(), M = function() {
            function t(t) {
                var e = t.get();
                if (this.tagClass = e >> 6,
                this.tagConstructed = 0 !== (32 & e),
                this.tagNumber = 31 & e,
                31 == this.tagNumber) {
                    var i = new B;
                    do {
                        e = t.get(),
                        i.mulAdd(128, 127 & e)
                    } while (128 & e);
                    this.tagNumber = i.simplify()
                }
            }
            return t.prototype.isUniversal = function() {
                return 0 === this.tagClass
            }
            ,
            t.prototype.isEOC = function() {
                return 0 === this.tagClass && 0 === this.tagNumber
            }
            ,
            t
        }(),N = function() {
            function t(t, e, i, r, n) {
                if (!(r instanceof M))
                    throw new Error("Invalid tag value.");
                this.stream = t,
                this.header = e,
                this.length = i,
                this.tag = r,
                this.sub = n
            }
            return t.prototype.typeName = function() {
                switch (this.tag.tagClass) {
                case 0:
                    switch (this.tag.tagNumber) {
                    case 0:
                        return "EOC";
                    case 1:
                        return "BOOLEAN";
                    case 2:
                        return "INTEGER";
                    case 3:
                        return "BIT_STRING";
                    case 4:
                        return "OCTET_STRING";
                    case 5:
                        return "NULL";
                    case 6:
                        return "OBJECT_IDENTIFIER";
                    case 7:
                        return "ObjectDescriptor";
                    case 8:
                        return "EXTERNAL";
                    case 9:
                        return "REAL";
                    case 10:
                        return "ENUMERATED";
                    case 11:
                        return "EMBEDDED_PDV";
                    case 12:
                        return "UTF8String";
                    case 16:
                        return "SEQUENCE";
                    case 17:
                        return "SET";
                    case 18:
                        return "NumericString";
                    case 19:
                        return "PrintableString";
                    case 20:
                        return "TeletexString";
                    case 21:
                        return "VideotexString";
                    case 22:
                        return "IA5String";
                    case 23:
                        return "UTCTime";
                    case 24:
                        return "GeneralizedTime";
                    case 25:
                        return "GraphicString";
                    case 26:
                        return "VisibleString";
                    case 27:
                        return "GeneralString";
                    case 28:
                        return "UniversalString";
                    case 30:
                        return "BMPString"
                    }
                    return "Universal_" + this.tag.tagNumber.toString();
                case 1:
                    return "Application_" + this.tag.tagNumber.toString();
                case 2:
                    return "[" + this.tag.tagNumber.toString() + "]";
                case 3:
                    return "Private_" + this.tag.tagNumber.toString()
                }
            }
            ,
            t.prototype.content = function(t) {
                if (void 0 === this.tag)
                    return null;
                void 0 === t && (t = 1 / 0);
                var e = this.posContent()
                  , i = Math.abs(this.length);
                if (!this.tag.isUniversal())
                    return null !== this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + i, t);
                switch (this.tag.tagNumber) {
                case 1:
                    return 0 === this.stream.get(e) ? "false" : "true";
                case 2:
                    return this.stream.parseInteger(e, e + i);
                case 3:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(e, e + i, t);
                case 4:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + i, t);
                case 6:
                    return this.stream.parseOID(e, e + i, t);
                case 16:
                case 17:
                    return null !== this.sub ? "(" + this.sub.length + " elem)" : "(no elem)";
                case 12:
                    return _(this.stream.parseStringUTF(e, e + i), t);
                case 18:
                case 19:
                case 20:
                case 21:
                case 22:
                case 26:
                    return _(this.stream.parseStringISO(e, e + i), t);
                case 30:
                    return _(this.stream.parseStringBMP(e, e + i), t);
                case 23:
                case 24:
                    return this.stream.parseTime(e, e + i, 23 == this.tag.tagNumber)
                }
                return null
            }
            ,
            t.prototype.toString = function() {
                return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
            }
            ,
            t.prototype.toPrettyString = function(t) {
                void 0 === t && (t = "");
                var e = t + this.typeName() + " @" + this.stream.pos;
                if (this.length >= 0 && (e += "+"),
                e += this.length,
                this.tag.tagConstructed ? e += " (constructed)" : !this.tag.isUniversal() || 3 != this.tag.tagNumber && 4 != this.tag.tagNumber || null === this.sub || (e += " (encapsulates)"),
                e += "\n",
                null !== this.sub) {
                    t += "  ";
                    for (var i = 0, r = this.sub.length; i < r; ++i)
                        e += this.sub[i].toPrettyString(t)
                }
                return e
            }
            ,
            t.prototype.posStart = function() {
                return this.stream.pos
            }
            ,
            t.prototype.posContent = function() {
                return this.stream.pos + this.header
            }
            ,
            t.prototype.posEnd = function() {
                return this.stream.pos + this.header + Math.abs(this.length)
            }
            ,
            t.prototype.toHexString = function() {
                return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
            }
            ,
            t.decodeLength = function(t) {
                var e = t.get()
                  , i = 127 & e;
                if (i == e)
                    return i;
                if (i > 6)
                    throw new Error("Length over 48 bits not supported at position " + (t.pos - 1));
                if (0 === i)
                    return null;
                e = 0;
                for (var r = 0; r < i; ++r)
                    e = 256 * e + t.get();
                return e
            }
            ,
            t.prototype.getHexStringValue = function() {
                var t = this.toHexString()
                  , e = 2 * this.header
                  , i = 2 * this.length;
                return t.substr(e, i)
            }
            ,
            t.decode = function(e) {
                var i;
                i = e instanceof I ? e : new I(e,0);
                var r = new I(i)
                  , n = new M(i)
                  , s = t.decodeLength(i)
                  , o = i.pos
                  , h = o - r.pos
                  , a = null
                  , u = function() {
                    var e = [];
                    if (null !== s) {
                        for (var r = o + s; i.pos < r; )
                            e[e.length] = t.decode(i);
                        if (i.pos != r)
                            throw new Error("Content size is not correct for container starting at offset " + o)
                    } else
                        try {
                            for (; ; ) {
                                var n = t.decode(i);
                                if (n.tag.isEOC())
                                    break;
                                e[e.length] = n
                            }
                            s = o - i.pos
                        } catch (h) {
                            throw new Error("Exception while decoding undefined length content: " + h)
                        }
                    return e
                };
                if (n.tagConstructed)
                    a = u();
                else if (n.isUniversal() && (3 == n.tagNumber || 4 == n.tagNumber))
                    try {
                        if (3 == n.tagNumber && 0 != i.get())
                            throw new Error("BIT STRINGs with unused bits cannot encapsulate.");
                        a = u();
                        for (var c = 0; c < a.length; ++c)
                            if (a[c].tag.isEOC())
                                throw new Error("EOC is not supposed to be actual content.")
                    } catch (f) {
                        a = null
                    }
                if (null === a) {
                    if (null === s)
                        throw new Error("We can't skip over an invalid tag with undefined length at offset " + o);
                    i.pos = o + Math.abs(s)
                }
                return new t(r,h,s,n,a)
            }
            ,
            t
        }(),
        at = function() {
            function t() {
                this.n = null,
                this.e = 0,
                this.d = null,
                this.p = null,
                this.q = null,
                this.dmp1 = null,
                this.dmq1 = null,
                this.coeff = null
            }
            return t.prototype.doPublic = function(t) {
                return t.modPowInt(this.e, this.n)
            }
            ,
            t.prototype.doPrivate = function(t) {
                if (null == this.p || null == this.q)
                    return t.modPow(this.d, this.n);
                for (var e = t.mod(this.p).modPow(this.dmp1, this.p), i = t.mod(this.q).modPow(this.dmq1, this.q); e.compareTo(i) < 0; )
                    e = e.add(this.p);
                return e.subtract(i).multiply(this.coeff).mod(this.p).multiply(this.q).add(i)
            }
            ,
            t.prototype.setPublic = function(t, e) {
                null != t && null != e && t.length > 0 && e.length > 0 && (this.n = z(t, 16),
                this.e = parseInt(e, 16))
            }
            ,
            t.prototype.encrypt = function(t) {
                var e = this.n.bitLength() + 7 >> 3
                  , i = function(t, e) {
                    if (e < t.length + 11)
                        return null;
                    for (var i = [], r = t.length - 1; r >= 0 && e > 0; ) {
                        var n = t.charCodeAt(r--);
                        n < 128 ? i[--e] = n : n > 127 && n < 2048 ? (i[--e] = 63 & n | 128,
                        i[--e] = n >> 6 | 192) : (i[--e] = 63 & n | 128,
                        i[--e] = n >> 6 & 63 | 128,
                        i[--e] = n >> 12 | 224)
                    }
                    i[--e] = 0;
                    for (var s = new ht, o = []; e > 2; ) {
                        for (o[0] = 0; 0 == o[0]; )
                            s.nextBytes(o);
                        i[--e] = o[0]
                    }
                    return i[--e] = 2,
                    i[--e] = 0,
                    new H(i)
                }(t, e);
                if (null == i)
                    return null;
                var r = this.doPublic(i);
                if (null == r)
                    return null;
                for (var n = r.toString(16), s = n.length, o = 0; o < 2 * e - s; o++)
                    n = "0" + n;
                return n
            }
            ,
            t.prototype.setPrivate = function(t, e, i) {
                null != t && null != e && t.length > 0 && e.length > 0 && (this.n = z(t, 16),
                this.e = parseInt(e, 16),
                this.d = z(i, 16))
            }
            ,
            t.prototype.setPrivateEx = function(t, e, i, r, n, s, o, h) {
                null != t && null != e && t.length > 0 && e.length > 0 && (this.n = z(t, 16),
                this.e = parseInt(e, 16),
                this.d = z(i, 16),
                this.p = z(r, 16),
                this.q = z(n, 16),
                this.dmp1 = z(s, 16),
                this.dmq1 = z(o, 16),
                this.coeff = z(h, 16))
            }
            ,
            t.prototype.generate = function(t, e) {
                var i = new ht
                  , r = t >> 1;
                this.e = parseInt(e, 16);
                for (var n = new H(e,16); ; ) {
                    for (; this.p = new H(t - r,1,i),
                    0 != this.p.subtract(H.ONE).gcd(n).compareTo(H.ONE) || !this.p.isProbablePrime(10); )
                        ;
                    for (; this.q = new H(r,1,i),
                    0 != this.q.subtract(H.ONE).gcd(n).compareTo(H.ONE) || !this.q.isProbablePrime(10); )
                        ;
                    if (this.p.compareTo(this.q) <= 0) {
                        var s = this.p;
                        this.p = this.q,
                        this.q = s
                    }
                    var o = this.p.subtract(H.ONE)
                      , h = this.q.subtract(H.ONE)
                      , a = o.multiply(h);
                    if (0 == a.gcd(n).compareTo(H.ONE)) {
                        this.n = this.p.multiply(this.q),
                        this.d = n.modInverse(a),
                        this.dmp1 = this.d.mod(o),
                        this.dmq1 = this.d.mod(h),
                        this.coeff = this.q.modInverse(this.p);
                        break
                    }
                }
            }
            ,
            t.prototype.decrypt = function(t) {
                var e = z(t, 16)
                  , i = this.doPrivate(e);
                return null == i ? null : function(t, e) {
                    var i = t.toByteArray()
                      , r = 0;
                    for (; r < i.length && 0 == i[r]; )
                        ++r;
                    if (i.length - r != e - 1 || 2 != i[r])
                        return null;
                    ++r;
                    for (; 0 != i[r]; )
                        if (++r >= i.length)
                            return null;
                    var n = "";
                    for (; ++r < i.length; ) {
                        var s = 255 & i[r];
                        s < 128 ? n += String.fromCharCode(s) : s > 191 && s < 224 ? (n += String.fromCharCode((31 & s) << 6 | 63 & i[r + 1]),
                        ++r) : (n += String.fromCharCode((15 & s) << 12 | (63 & i[r + 1]) << 6 | 63 & i[r + 2]),
                        r += 2)
                    }
                    return n
                }(i, this.n.bitLength() + 7 >> 3)
            }
            ,
            t.prototype.generateAsync = function(t, e, i) {
                var r = new ht
                  , n = t >> 1;
                this.e = parseInt(e, 16);
                var s = new H(e,16)
                  , o = this;
                setTimeout((function e() {
                    var h = function() {
                        if (o.p.compareTo(o.q) <= 0) {
                            var t = o.p;
                            o.p = o.q,
                            o.q = t
                        }
                        var r = o.p.subtract(H.ONE)
                          , n = o.q.subtract(H.ONE)
                          , h = r.multiply(n);
                        0 == h.gcd(s).compareTo(H.ONE) ? (o.n = o.p.multiply(o.q),
                        o.d = s.modInverse(h),
                        o.dmp1 = o.d.mod(r),
                        o.dmq1 = o.d.mod(n),
                        o.coeff = o.q.modInverse(o.p),
                        setTimeout((function() {
                            i()
                        }
                        ), 0)) : setTimeout(e, 0)
                    }
                      , a = function t() {
                        o.q = F(),
                        o.q.fromNumberAsync(n, 1, r, (function() {
                            o.q.subtract(H.ONE).gcda(s, (function(e) {
                                0 == e.compareTo(H.ONE) && o.q.isProbablePrime(10) ? setTimeout(h, 0) : setTimeout(t, 0)
                            }
                            ))
                        }
                        ))
                    };
                    setTimeout((function e() {
                        o.p = F(),
                        o.p.fromNumberAsync(t - n, 1, r, (function() {
                            o.p.subtract(H.ONE).gcda(s, (function(t) {
                                0 == t.compareTo(H.ONE) && o.p.isProbablePrime(10) ? setTimeout(a, 0) : setTimeout(e, 0)
                            }
                            ))
                        }
                        ))
                    }
                    ), 0)
                }
                ), 0)
            }
            ,
            t.prototype.sign = function(t, e, i) {
                var r = function(t, e) {
                    if (e < t.length + 22)
                        return null;
                    for (var i = e - t.length - 6, r = "", n = 0; n < i; n += 2)
                        r += "ff";
                    return z("0001" + r + "00" + t, 16)
                }((ut[i] || "") + e(t).toString(), this.n.bitLength() / 4);
                if (null == r)
                    return null;
                var n = this.doPrivate(r);
                if (null == n)
                    return null;
                var s = n.toString(16);
                return 0 == (1 & s.length) ? s : "0" + s
            }
            ,
            t.prototype.verify = function(t, e, i) {
                var r = z(e, 16)
                  , n = this.doPublic(r);
                return null == n ? null : function(t) {
                    for (var e in ut)
                        if (ut.hasOwnProperty(e)) {
                            var i = ut[e]
                              , r = i.length;
                            if (t.substr(0, r) == i)
                                return t.substr(r)
                        }
                    return t
                }(n.toString(16).replace(/^1f+00/, "")) == i(t).toString()
            }
            ,
            t
        }();
     pt = function() {
            var t = function(e, i) {
                return t = Object.setPrototypeOf || {
                    __proto__: []
                }instanceof Array && function(t, e) {
                    t.__proto__ = e
                }
                || function(t, e) {
                    for (var i in e)
                        Object.prototype.hasOwnProperty.call(e, i) && (t[i] = e[i])
                }
                ,
                t(e, i)
            };
            return function(e, i) {
                if ("function" !== typeof i && null !== i)
                    throw new TypeError("Class extends value " + String(i) + " is not a constructor or null");
                function r() {
                    this.constructor = e
                }
                t(e, i),
                e.prototype = null === i ? Object.create(i) : (r.prototype = i.prototype,
                new r)
            }
        }()
        ;
        function F() {
            return new H(null)
        }
        function Y(t) {
            var e = F();
            return e.fromInt(t),
            e
        };
        j = function() {
            function t(t) {
                this.m = t
            }
            return t.prototype.convert = function(t) {
                return t.s < 0 || t.compareTo(this.m) >= 0 ? t.mod(this.m) : t
            }
            ,
            t.prototype.revert = function(t) {
                return t
            }
            ,
            t.prototype.reduce = function(t) {
                t.divRemTo(this.m, null, t)
            }
            ,
            t.prototype.mulTo = function(t, e, i) {
                t.multiplyTo(e, i),
                this.reduce(i)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
            ,
            t
        }(), L = function() {
            function t(t) {
                this.m = t,
                this.mp = t.invDigit(),
                this.mpl = 32767 & this.mp,
                this.mph = this.mp >> 15,
                this.um = (1 << t.DB - 15) - 1,
                this.mt2 = 2 * t.t
            }
            return t.prototype.convert = function(t) {
                var e = F();
                return t.abs().dlShiftTo(this.m.t, e),
                e.divRemTo(this.m, null, e),
                t.s < 0 && e.compareTo(H.ZERO) > 0 && this.m.subTo(e, e),
                e
            }
            ,
            t.prototype.revert = function(t) {
                var e = F();
                return t.copyTo(e),
                this.reduce(e),
                e
            }
            ,
            t.prototype.reduce = function(t) {
                for (; t.t <= this.mt2; )
                    t[t.t++] = 0;
                for (var e = 0; e < this.m.t; ++e) {
                    var i = 32767 & t[e]
                      , r = i * this.mpl + ((i * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                    for (t[i = e + this.m.t] += this.m.am(0, r, t, e, 0, this.m.t); t[i] >= t.DV; )
                        t[i] -= t.DV,
                        t[++i]++
                }
                t.clamp(),
                t.drShiftTo(this.m.t, t),
                t.compareTo(this.m) >= 0 && t.subTo(this.m, t)
            }
            ,
            t.prototype.mulTo = function(t, e, i) {
                t.multiplyTo(e, i),
                this.reduce(i)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
            ,
            t
        }();
        var gaibian2 = "0123456789abcdefghijklmnopqrstuvwxyz";
        function gaibian1(t) {
            return gaibian2.charAt(t)
        };
        var H = function() {
            function t(t, e, i) {
                null != t && ("number" == typeof t ? this.fromNumber(t, e, i) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
            }
            return t.prototype.toString = function(t) {
                if (this.s < 0)
                    return "-" + this.negate().toString(t);
                var e;
                if (16 == t)
                    e = 4;
                else if (8 == t)
                    e = 3;
                else if (2 == t)
                    e = 1;
                else if (32 == t)
                    e = 5;
                else {
                    if (4 != t)
                        return this.toRadix(t);
                    e = 2
                }
                var i, r = (1 << e) - 1, n = !1, s = "", o = this.t, h = this.DB - o * this.DB % e;
                if (o-- > 0)
                    for (h < this.DB && (i = this[o] >> h) > 0 && (n = !0,
                    s = gaibian1(i)); o >= 0; )
                        h < e ? (i = (this[o] & (1 << h) - 1) << e - h,
                        i |= this[--o] >> (h += this.DB - e)) : (i = this[o] >> (h -= e) & r,
                        h <= 0 && (h += this.DB,
                        --o)),
                        i > 0 && (n = !0),
                        n && (s += gaibian1(i));
                return n ? s : "0"
            }
            ,
            t.prototype.negate = function() {
                var e = F();
                return t.ZERO.subTo(this, e),
                e
            }
            ,
            t.prototype.abs = function() {
                return this.s < 0 ? this.negate() : this
            }
            ,
            t.prototype.compareTo = function(t) {
                var e = this.s - t.s;
                if (0 != e)
                    return e;
                var i = this.t;
                if (0 != (e = i - t.t))
                    return this.s < 0 ? -e : e;
                for (; --i >= 0; )
                    if (0 != (e = this[i] - t[i]))
                        return e;
                return 0
            }
            ,
            t.prototype.bitLength = function() {
                return this.t <= 0 ? 0 : this.DB * (this.t - 1) + W(this[this.t - 1] ^ this.s & this.DM)
            }
            ,
            t.prototype.mod = function(e) {
                var i = F();
                return this.abs().divRemTo(e, null, i),
                this.s < 0 && i.compareTo(t.ZERO) > 0 && e.subTo(i, i),
                i
            }
            ,
            t.prototype.modPowInt = function(t, e) {
                var i;
                return i = t < 256 || e.isEven() ? new j(e) : new L(e),
                this.exp(t, i)
            }
            ,
            t.prototype.clone = function() {
                var t = F();
                return this.copyTo(t),
                t
            }
            ,
            t.prototype.intValue = function() {
                if (this.s < 0) {
                    if (1 == this.t)
                        return this[0] - this.DV;
                    if (0 == this.t)
                        return -1
                } else {
                    if (1 == this.t)
                        return this[0];
                    if (0 == this.t)
                        return 0
                }
                return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
            }
            ,
            t.prototype.byteValue = function() {
                return 0 == this.t ? this.s : this[0] << 24 >> 24
            }
            ,
            t.prototype.shortValue = function() {
                return 0 == this.t ? this.s : this[0] << 16 >> 16
            }
            ,
            t.prototype.signum = function() {
                return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
            }
            ,
            t.prototype.toByteArray = function() {
                var t = this.t
                  , e = [];
                e[0] = this.s;
                var i, r = this.DB - t * this.DB % 8, n = 0;
                if (t-- > 0)
                    for (r < this.DB && (i = this[t] >> r) != (this.s & this.DM) >> r && (e[n++] = i | this.s << this.DB - r); t >= 0; )
                        r < 8 ? (i = (this[t] & (1 << r) - 1) << 8 - r,
                        i |= this[--t] >> (r += this.DB - 8)) : (i = this[t] >> (r -= 8) & 255,
                        r <= 0 && (r += this.DB,
                        --t)),
                        0 != (128 & i) && (i |= -256),
                        0 == n && (128 & this.s) != (128 & i) && ++n,
                        (n > 0 || i != this.s) && (e[n++] = i);
                return e
            }
            ,
            t.prototype.equals = function(t) {
                return 0 == this.compareTo(t)
            }
            ,
            t.prototype.min = function(t) {
                return this.compareTo(t) < 0 ? this : t
            }
            ,
            t.prototype.max = function(t) {
                return this.compareTo(t) > 0 ? this : t
            }
            ,
            t.prototype.and = function(t) {
                var e = F();
                return this.bitwiseTo(t, f, e),
                e
            }
            ,
            t.prototype.or = function(t) {
                var e = F();
                return this.bitwiseTo(t, p, e),
                e
            }
            ,
            t.prototype.xor = function(t) {
                var e = F();
                return this.bitwiseTo(t, l, e),
                e
            }
            ,
            t.prototype.andNot = function(t) {
                var e = F();
                return this.bitwiseTo(t, d, e),
                e
            }
            ,
            t.prototype.not = function() {
                for (var t = F(), e = 0; e < this.t; ++e)
                    t[e] = this.DM & ~this[e];
                return t.t = this.t,
                t.s = ~this.s,
                t
            }
            ,
            t.prototype.shiftLeft = function(t) {
                var e = F();
                return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
                e
            }
            ,
            t.prototype.shiftRight = function(t) {
                var e = F();
                return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
                e
            }
            ,
            t.prototype.getLowestSetBit = function() {
                for (var t = 0; t < this.t; ++t)
                    if (0 != this[t])
                        return t * this.DB + g(this[t]);
                return this.s < 0 ? this.t * this.DB : -1
            }
            ,
            t.prototype.bitCount = function() {
                for (var t = 0, e = this.s & this.DM, i = 0; i < this.t; ++i)
                    t += y(this[i] ^ e);
                return t
            }
            ,
            t.prototype.testBit = function(t) {
                var e = Math.floor(t / this.DB);
                return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
            }
            ,
            t.prototype.setBit = function(t) {
                return this.changeBit(t, p)
            }
            ,
            t.prototype.clearBit = function(t) {
                return this.changeBit(t, d)
            }
            ,
            t.prototype.flipBit = function(t) {
                return this.changeBit(t, l)
            }
            ,
            t.prototype.add = function(t) {
                var e = F();
                return this.addTo(t, e),
                e
            }
            ,
            t.prototype.subtract = function(t) {
                var e = F();
                return this.subTo(t, e),
                e
            }
            ,
            t.prototype.multiply = function(t) {
                var e = F();
                return this.multiplyTo(t, e),
                e
            }
            ,
            t.prototype.divide = function(t) {
                var e = F();
                return this.divRemTo(t, e, null),
                e
            }
            ,
            t.prototype.remainder = function(t) {
                var e = F();
                return this.divRemTo(t, null, e),
                e
            }
            ,
            t.prototype.divideAndRemainder = function(t) {
                var e = F()
                  , i = F();
                return this.divRemTo(t, e, i),
                [e, i]
            }
            ,
            t.prototype.modPow = function(t, e) {
                var i, r, n = t.bitLength(), s = Y(1);
                if (n <= 0)
                    return s;
                i = n < 18 ? 1 : n < 48 ? 3 : n < 144 ? 4 : n < 768 ? 5 : 6,
                r = n < 8 ? new j(e) : e.isEven() ? new q(e) : new L(e);
                var o = []
                  , h = 3
                  , a = i - 1
                  , u = (1 << i) - 1;
                if (o[1] = r.convert(this),
                i > 1) {
                    var c = F();
                    for (r.sqrTo(o[1], c); h <= u; )
                        o[h] = F(),
                        r.mulTo(c, o[h - 2], o[h]),
                        h += 2
                }
                var f, p, l = t.t - 1, d = !0, g = F();
                for (n = W(t[l]) - 1; l >= 0; ) {
                    for (n >= a ? f = t[l] >> n - a & u : (f = (t[l] & (1 << n + 1) - 1) << a - n,
                    l > 0 && (f |= t[l - 1] >> this.DB + n - a)),
                    h = i; 0 == (1 & f); )
                        f >>= 1,
                        --h;
                    if ((n -= h) < 0 && (n += this.DB,
                    --l),
                    d)
                        o[f].copyTo(s),
                        d = !1;
                    else {
                        for (; h > 1; )
                            r.sqrTo(s, g),
                            r.sqrTo(g, s),
                            h -= 2;
                        h > 0 ? r.sqrTo(s, g) : (p = s,
                        s = g,
                        g = p),
                        r.mulTo(g, o[f], s)
                    }
                    for (; l >= 0 && 0 == (t[l] & 1 << n); )
                        r.sqrTo(s, g),
                        p = s,
                        s = g,
                        g = p,
                        --n < 0 && (n = this.DB - 1,
                        --l)
                }
                return r.revert(s)
            }
            ,
            t.prototype.modInverse = function(e) {
                var i = e.isEven();
                if (this.isEven() && i || 0 == e.signum())
                    return t.ZERO;
                for (var r = e.clone(), n = this.clone(), s = Y(1), o = Y(0), h = Y(0), a = Y(1); 0 != r.signum(); ) {
                    for (; r.isEven(); )
                        r.rShiftTo(1, r),
                        i ? (s.isEven() && o.isEven() || (s.addTo(this, s),
                        o.subTo(e, o)),
                        s.rShiftTo(1, s)) : o.isEven() || o.subTo(e, o),
                        o.rShiftTo(1, o);
                    for (; n.isEven(); )
                        n.rShiftTo(1, n),
                        i ? (h.isEven() && a.isEven() || (h.addTo(this, h),
                        a.subTo(e, a)),
                        h.rShiftTo(1, h)) : a.isEven() || a.subTo(e, a),
                        a.rShiftTo(1, a);
                    r.compareTo(n) >= 0 ? (r.subTo(n, r),
                    i && s.subTo(h, s),
                    o.subTo(a, o)) : (n.subTo(r, n),
                    i && h.subTo(s, h),
                    a.subTo(o, a))
                }
                return 0 != n.compareTo(t.ONE) ? t.ZERO : a.compareTo(e) >= 0 ? a.subtract(e) : a.signum() < 0 ? (a.addTo(e, a),
                a.signum() < 0 ? a.add(e) : a) : a
            }
            ,
            t.prototype.pow = function(t) {
                return this.exp(t, new k)
            }
            ,
            t.prototype.gcd = function(t) {
                var e = this.s < 0 ? this.negate() : this.clone()
                  , i = t.s < 0 ? t.negate() : t.clone();
                if (e.compareTo(i) < 0) {
                    var r = e;
                    e = i,
                    i = r
                }
                var n = e.getLowestSetBit()
                  , s = i.getLowestSetBit();
                if (s < 0)
                    return e;
                for (n < s && (s = n),
                s > 0 && (e.rShiftTo(s, e),
                i.rShiftTo(s, i)); e.signum() > 0; )
                    (n = e.getLowestSetBit()) > 0 && e.rShiftTo(n, e),
                    (n = i.getLowestSetBit()) > 0 && i.rShiftTo(n, i),
                    e.compareTo(i) >= 0 ? (e.subTo(i, e),
                    e.rShiftTo(1, e)) : (i.subTo(e, i),
                    i.rShiftTo(1, i));
                return s > 0 && i.lShiftTo(s, i),
                i
            }
            ,
            t.prototype.isProbablePrime = function(t) {
                var e, i = this.abs();
                if (1 == i.t && i[0] <= P[P.length - 1]) {
                    for (e = 0; e < P.length; ++e)
                        if (i[0] == P[e])
                            return !0;
                    return !1
                }
                if (i.isEven())
                    return !1;
                for (e = 1; e < P.length; ) {
                    for (var r = P[e], n = e + 1; n < P.length && r < C; )
                        r *= P[n++];
                    for (r = i.modInt(r); e < n; )
                        if (r % P[e++] == 0)
                            return !1
                }
                return i.millerRabin(t)
            }
            ,
            t.prototype.copyTo = function(t) {
                for (var e = this.t - 1; e >= 0; --e)
                    t[e] = this[e];
                t.t = this.t,
                t.s = this.s
            }
            ,
            t.prototype.fromInt = function(t) {
                this.t = 1,
                this.s = t < 0 ? -1 : 0,
                t > 0 ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
            }
            ,
            t.prototype.fromString = function(e, i) {
                var r;
                if (16 == i)
                    r = 4;
                else if (8 == i)
                    r = 3;
                else if (256 == i)
                    r = 8;
                else if (2 == i)
                    r = 1;
                else if (32 == i)
                    r = 5;
                else {
                    if (4 != i)
                        return void this.fromRadix(e, i);
                    r = 2
                }
                this.t = 0,
                this.s = 0;
                for (var n = e.length, s = !1, o = 0; --n >= 0; ) {
                    var h = 8 == r ? 255 & +e[n] : Q(e, n);
                    h < 0 ? "-" == e.charAt(n) && (s = !0) : (s = !1,
                    0 == o ? this[this.t++] = h : o + r > this.DB ? (this[this.t - 1] |= (h & (1 << this.DB - o) - 1) << o,
                    this[this.t++] = h >> this.DB - o) : this[this.t - 1] |= h << o,
                    (o += r) >= this.DB && (o -= this.DB))
                }
                8 == r && 0 != (128 & +e[0]) && (this.s = -1,
                o > 0 && (this[this.t - 1] |= (1 << this.DB - o) - 1 << o)),
                this.clamp(),
                s && t.ZERO.subTo(this, this)
            }
            ,
            t.prototype.clamp = function() {
                for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t; )
                    --this.t
            }
            ,
            t.prototype.dlShiftTo = function(t, e) {
                var i;
                for (i = this.t - 1; i >= 0; --i)
                    e[i + t] = this[i];
                for (i = t - 1; i >= 0; --i)
                    e[i] = 0;
                e.t = this.t + t,
                e.s = this.s
            }
            ,
            t.prototype.drShiftTo = function(t, e) {
                for (var i = t; i < this.t; ++i)
                    e[i - t] = this[i];
                e.t = Math.max(this.t - t, 0),
                e.s = this.s
            }
            ,
            t.prototype.lShiftTo = function(t, e) {
                for (var i = t % this.DB, r = this.DB - i, n = (1 << r) - 1, s = Math.floor(t / this.DB), o = this.s << i & this.DM, h = this.t - 1; h >= 0; --h)
                    e[h + s + 1] = this[h] >> r | o,
                    o = (this[h] & n) << i;
                for (h = s - 1; h >= 0; --h)
                    e[h] = 0;
                e[s] = o,
                e.t = this.t + s + 1,
                e.s = this.s,
                e.clamp()
            }
            ,
            t.prototype.rShiftTo = function(t, e) {
                e.s = this.s;
                var i = Math.floor(t / this.DB);
                if (i >= this.t)
                    e.t = 0;
                else {
                    var r = t % this.DB
                      , n = this.DB - r
                      , s = (1 << r) - 1;
                    e[0] = this[i] >> r;
                    for (var o = i + 1; o < this.t; ++o)
                        e[o - i - 1] |= (this[o] & s) << n,
                        e[o - i] = this[o] >> r;
                    r > 0 && (e[this.t - i - 1] |= (this.s & s) << n),
                    e.t = this.t - i,
                    e.clamp()
                }
            }
            ,
            t.prototype.subTo = function(t, e) {
                for (var i = 0, r = 0, n = Math.min(t.t, this.t); i < n; )
                    r += this[i] - t[i],
                    e[i++] = r & this.DM,
                    r >>= this.DB;
                if (t.t < this.t) {
                    for (r -= t.s; i < this.t; )
                        r += this[i],
                        e[i++] = r & this.DM,
                        r >>= this.DB;
                    r += this.s
                } else {
                    for (r += this.s; i < t.t; )
                        r -= t[i],
                        e[i++] = r & this.DM,
                        r >>= this.DB;
                    r -= t.s
                }
                e.s = r < 0 ? -1 : 0,
                r < -1 ? e[i++] = this.DV + r : r > 0 && (e[i++] = r),
                e.t = i,
                e.clamp()
            }
            ,
            t.prototype.multiplyTo = function(e, i) {
                var r = this.abs()
                  , n = e.abs()
                  , s = r.t;
                for (i.t = s + n.t; --s >= 0; )
                    i[s] = 0;
                for (s = 0; s < n.t; ++s)
                    i[s + r.t] = r.am(0, n[s], i, s, 0, r.t);
                i.s = 0,
                i.clamp(),
                this.s != e.s && t.ZERO.subTo(i, i)
            }
            ,
            t.prototype.squareTo = function(t) {
                for (var e = this.abs(), i = t.t = 2 * e.t; --i >= 0; )
                    t[i] = 0;
                for (i = 0; i < e.t - 1; ++i) {
                    var r = e.am(i, e[i], t, 2 * i, 0, 1);
                    (t[i + e.t] += e.am(i + 1, 2 * e[i], t, 2 * i + 1, r, e.t - i - 1)) >= e.DV && (t[i + e.t] -= e.DV,
                    t[i + e.t + 1] = 1)
                }
                t.t > 0 && (t[t.t - 1] += e.am(i, e[i], t, 2 * i, 0, 1)),
                t.s = 0,
                t.clamp()
            }
            ,
            t.prototype.divRemTo = function(e, i, r) {
                var n = e.abs();
                if (!(n.t <= 0)) {
                    var s = this.abs();
                    if (s.t < n.t)
                        return null != i && i.fromInt(0),
                        void (null != r && this.copyTo(r));
                    null == r && (r = F());
                    var o = F()
                      , h = this.s
                      , a = e.s
                      , u = this.DB - W(n[n.t - 1]);
                    u > 0 ? (n.lShiftTo(u, o),
                    s.lShiftTo(u, r)) : (n.copyTo(o),
                    s.copyTo(r));
                    var c = o.t
                      , f = o[c - 1];
                    if (0 != f) {
                        var p = f * (1 << this.F1) + (c > 1 ? o[c - 2] >> this.F2 : 0)
                          , l = this.FV / p
                          , d = (1 << this.F1) / p
                          , g = 1 << this.F2
                          , y = r.t
                          , v = y - c
                          , m = null == i ? F() : i;
                        for (o.dlShiftTo(v, m),
                        r.compareTo(m) >= 0 && (r[r.t++] = 1,
                        r.subTo(m, r)),
                        t.ONE.dlShiftTo(c, m),
                        m.subTo(o, o); o.t < c; )
                            o[o.t++] = 0;
                        for (; --v >= 0; ) {
                            var b = r[--y] == f ? this.DM : Math.floor(r[y] * l + (r[y - 1] + g) * d);
                            if ((r[y] += o.am(0, b, r, v, 0, c)) < b)
                                for (o.dlShiftTo(v, m),
                                r.subTo(m, r); r[y] < --b; )
                                    r.subTo(m, r)
                        }
                        null != i && (r.drShiftTo(c, i),
                        h != a && t.ZERO.subTo(i, i)),
                        r.t = c,
                        r.clamp(),
                        u > 0 && r.rShiftTo(u, r),
                        h < 0 && t.ZERO.subTo(r, r)
                    }
                }
            }
            ,
            t.prototype.invDigit = function() {
                if (this.t < 1)
                    return 0;
                var t = this[0];
                if (0 == (1 & t))
                    return 0;
                var e = 3 & t;
                return (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) > 0 ? this.DV - e : -e
            }
            ,
            t.prototype.isEven = function() {
                return 0 == (this.t > 0 ? 1 & this[0] : this.s)
            }
            ,
            t.prototype.exp = function(e, i) {
                if (e > 4294967295 || e < 1)
                    return t.ONE;
                var r = F()
                  , n = F()
                  , s = i.convert(this)
                  , o = W(e) - 1;
                for (s.copyTo(r); --o >= 0; )
                    if (i.sqrTo(r, n),
                    (e & 1 << o) > 0)
                        i.mulTo(n, s, r);
                    else {
                        var h = r;
                        r = n,
                        n = h
                    }
                return i.revert(r)
            }
            ,
            t.prototype.chunkSize = function(t) {
                return Math.floor(Math.LN2 * this.DB / Math.log(t))
            }
            ,
            t.prototype.toRadix = function(t) {
                if (null == t && (t = 10),
                0 == this.signum() || t < 2 || t > 36)
                    return "0";
                var e = this.chunkSize(t)
                  , i = Math.pow(t, e)
                  , r = Y(i)
                  , n = F()
                  , s = F()
                  , o = "";
                for (this.divRemTo(r, n, s); n.signum() > 0; )
                    o = (i + s.intValue()).toString(t).substr(1) + o,
                    n.divRemTo(r, n, s);
                return s.intValue().toString(t) + o
            }
            ,
            t.prototype.fromRadix = function(e, i) {
                this.fromInt(0),
                null == i && (i = 10);
                for (var r = this.chunkSize(i), n = Math.pow(i, r), s = !1, o = 0, h = 0, a = 0; a < e.length; ++a) {
                    var u = Q(e, a);
                    u < 0 ? "-" == e.charAt(a) && 0 == this.signum() && (s = !0) : (h = i * h + u,
                    ++o >= r && (this.dMultiply(n),
                    this.dAddOffset(h, 0),
                    o = 0,
                    h = 0))
                }
                o > 0 && (this.dMultiply(Math.pow(i, o)),
                this.dAddOffset(h, 0)),
                s && t.ZERO.subTo(this, this)
            }
            ,
            t.prototype.fromNumber = function(e, i, r) {
                if ("number" == typeof i)
                    if (e < 2)
                        this.fromInt(1);
                    else
                        for (this.fromNumber(e, r),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), p, this),
                        this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(i); )
                            this.dAddOffset(2, 0),
                            this.bitLength() > e && this.subTo(t.ONE.shiftLeft(e - 1), this);
                else {
                    var n = []
                      , s = 7 & e;
                    n.length = 1 + (e >> 3),
                    i.nextBytes(n),
                    s > 0 ? n[0] &= (1 << s) - 1 : n[0] = 0,
                    this.fromString(n, 256)
                }
            }
            ,
            t.prototype.bitwiseTo = function(t, e, i) {
                var r, n, s = Math.min(t.t, this.t);
                for (r = 0; r < s; ++r)
                    i[r] = e(this[r], t[r]);
                if (t.t < this.t) {
                    for (n = t.s & this.DM,
                    r = s; r < this.t; ++r)
                        i[r] = e(this[r], n);
                    i.t = this.t
                } else {
                    for (n = this.s & this.DM,
                    r = s; r < t.t; ++r)
                        i[r] = e(n, t[r]);
                    i.t = t.t
                }
                i.s = e(this.s, t.s),
                i.clamp()
            }
            ,
            t.prototype.changeBit = function(e, i) {
                var r = t.ONE.shiftLeft(e);
                return this.bitwiseTo(r, i, r),
                r
            }
            ,
            t.prototype.addTo = function(t, e) {
                for (var i = 0, r = 0, n = Math.min(t.t, this.t); i < n; )
                    r += this[i] + t[i],
                    e[i++] = r & this.DM,
                    r >>= this.DB;
                if (t.t < this.t) {
                    for (r += t.s; i < this.t; )
                        r += this[i],
                        e[i++] = r & this.DM,
                        r >>= this.DB;
                    r += this.s
                } else {
                    for (r += this.s; i < t.t; )
                        r += t[i],
                        e[i++] = r & this.DM,
                        r >>= this.DB;
                    r += t.s
                }
                e.s = r < 0 ? -1 : 0,
                r > 0 ? e[i++] = r : r < -1 && (e[i++] = this.DV + r),
                e.t = i,
                e.clamp()
            }
            ,
            t.prototype.dMultiply = function(t) {
                this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
                ++this.t,
                this.clamp()
            }
            ,
            t.prototype.dAddOffset = function(t, e) {
                if (0 != t) {
                    for (; this.t <= e; )
                        this[this.t++] = 0;
                    for (this[e] += t; this[e] >= this.DV; )
                        this[e] -= this.DV,
                        ++e >= this.t && (this[this.t++] = 0),
                        ++this[e]
                }
            }
            ,
            t.prototype.multiplyLowerTo = function(t, e, i) {
                var r = Math.min(this.t + t.t, e);
                for (i.s = 0,
                i.t = r; r > 0; )
                    i[--r] = 0;
                for (var n = i.t - this.t; r < n; ++r)
                    i[r + this.t] = this.am(0, t[r], i, r, 0, this.t);
                for (n = Math.min(t.t, e); r < n; ++r)
                    this.am(0, t[r], i, r, 0, e - r);
                i.clamp()
            }
            ,
            t.prototype.multiplyUpperTo = function(t, e, i) {
                --e;
                var r = i.t = this.t + t.t - e;
                for (i.s = 0; --r >= 0; )
                    i[r] = 0;
                for (r = Math.max(e - this.t, 0); r < t.t; ++r)
                    i[this.t + r - e] = this.am(e - r, t[r], i, 0, 0, this.t + r - e);
                i.clamp(),
                i.drShiftTo(1, i)
            }
            ,
            t.prototype.modInt = function(t) {
                if (t <= 0)
                    return 0;
                var e = this.DV % t
                  , i = this.s < 0 ? t - 1 : 0;
                if (this.t > 0)
                    if (0 == e)
                        i = this[0] % t;
                    else
                        for (var r = this.t - 1; r >= 0; --r)
                            i = (e * i + this[r]) % t;
                return i
            }
            ,
            t.prototype.millerRabin = function(e) {
                var i = this.subtract(t.ONE)
                  , r = i.getLowestSetBit();
                if (r <= 0)
                    return !1;
                var n = i.shiftRight(r);
                (e = e + 1 >> 1) > P.length && (e = P.length);
                for (var s = F(), o = 0; o < e; ++o) {
                    s.fromInt(P[Math.floor(Math.random() * P.length)]);
                    var h = s.modPow(n, this);
                    if (0 != h.compareTo(t.ONE) && 0 != h.compareTo(i)) {
                        for (var a = 1; a++ < r && 0 != h.compareTo(i); )
                            if (0 == (h = h.modPowInt(2, this)).compareTo(t.ONE))
                                return !1;
                        if (0 != h.compareTo(i))
                            return !1
                    }
                }
                return !0
            }
            ,
            t.prototype.square = function() {
                var t = F();
                return this.squareTo(t),
                t
            }
            ,
            t.prototype.gcda = function(t, e) {
                var i = this.s < 0 ? this.negate() : this.clone()
                  , r = t.s < 0 ? t.negate() : t.clone();
                if (i.compareTo(r) < 0) {
                    var n = i;
                    i = r,
                    r = n
                }
                var s = i.getLowestSetBit()
                  , o = r.getLowestSetBit();
                if (o < 0)
                    e(i);
                else {
                    s < o && (o = s),
                    o > 0 && (i.rShiftTo(o, i),
                    r.rShiftTo(o, r));
                    setTimeout((function t() {
                        (s = i.getLowestSetBit()) > 0 && i.rShiftTo(s, i),
                        (s = r.getLowestSetBit()) > 0 && r.rShiftTo(s, r),
                        i.compareTo(r) >= 0 ? (i.subTo(r, i),
                        i.rShiftTo(1, i)) : (r.subTo(i, r),
                        r.rShiftTo(1, r)),
                        i.signum() > 0 ? setTimeout(t, 0) : (o > 0 && r.lShiftTo(o, r),
                        setTimeout((function() {
                            e(r)
                        }
                        ), 0))
                    }
                    ), 10)
                }
            }
            ,
            t.prototype.fromNumberAsync = function(e, i, r, n) {
                if ("number" == typeof i)
                    if (e < 2)
                        this.fromInt(1);
                    else {
                        this.fromNumber(e, r),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), p, this),
                        this.isEven() && this.dAddOffset(1, 0);
                        var s = this;
                        setTimeout((function r() {
                            s.dAddOffset(2, 0),
                            s.bitLength() > e && s.subTo(t.ONE.shiftLeft(e - 1), s),
                            s.isProbablePrime(i) ? setTimeout((function() {
                                n()
                            }
                            ), 0) : setTimeout(r, 0)
                        }
                        ), 0)
                    }
                else {
                    var o = []
                      , h = 7 & e;
                    o.length = 1 + (e >> 3),
                    i.nextBytes(o),
                    h > 0 ? o[0] &= (1 << h) - 1 : o[0] = 0,
                    this.fromString(o, 256)
                }
            }
            ,
            t
        }();
        H.ZERO = Y(0);
        H.ONE = Y(1);
        function F() {
            return new H(null)
        };
        function z(t, e) {
            return new H(t,e)
        };
        var K = "undefined" !== typeof navigator;
        K && "Microsoft Internet Explorer" == navigator.appName ? (H.prototype.am = function(t, e, i, r, n, s) {
            for (var o = 32767 & e, h = e >> 15; --s >= 0; ) {
                var a = 32767 & this[t]
                  , u = this[t++] >> 15
                  , c = h * a + u * o;
                n = ((a = o * a + ((32767 & c) << 15) + i[r] + (1073741823 & n)) >>> 30) + (c >>> 15) + h * u + (n >>> 30),
                i[r++] = 1073741823 & a
            }
            return n
        }
        ,
        V = 30) : K && "Netscape" != navigator.appName ? (H.prototype.am = function(t, e, i, r, n, s) {
            for (; --s >= 0; ) {
                var o = e * this[t++] + i[r] + n;
                n = Math.floor(o / 67108864),
                i[r++] = 67108863 & o
            }
            return n
        }
        ,
        V = 26) : (H.prototype.am = function(t, e, i, r, n, s) {
            for (var o = 16383 & e, h = e >> 14; --s >= 0; ) {
                var a = 16383 & this[t]
                  , u = this[t++] >> 14
                  , c = h * a + u * o;
                n = ((a = o * a + ((16383 & c) << 14) + i[r] + n) >> 28) + (c >> 14) + h * u,
                i[r++] = 268435455 & a
            }
            return n
        }
        ,
        V = 28),
        H.prototype.DB = V,
        H.prototype.DM = (1 << V) - 1,
        H.prototype.DV = 1 << V;
        H.prototype.FV = Math.pow(2, 52),
        H.prototype.F1 = 52 - V,
        H.prototype.F2 = 2 * V - 52;
        var U, G, Z = [];
        for (U = "0".charCodeAt(0),
        G = 0; G <= 9; ++G)
            Z[U++] = G;
        for (U = "a".charCodeAt(0),
        G = 10; G < 36; ++G)
            Z[U++] = G;
        for (U = "A".charCodeAt(0),
        G = 10; G < 36; ++G)
            Z[U++] = G;
        function Q(t, e) {
            var i = Z[t.charCodeAt(e)];
            return null == i ? -1 : i
        };
    lt = function(t) {
            function e(i) {
                var r = t.call(this) || this;
                return i && ("string" === typeof i ? r.parseKey(i) : (e.hasPrivateKeyProperty(i) || e.hasPublicKeyProperty(i)) && r.parsePropertiesFrom(i)),
                r
            }
            return pt(e, t),
            e.prototype.parseKey = function(t) {
                try {
                    var e = 0
                      , i = 0
                      , r = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/.test(t) ? w(t) : D.unarmor(t)
                      , n = N.decode(r);
                    if (3 === n.sub.length && (n = n.sub[2].sub[0]),
                    9 === n.sub.length) {
                        e = n.sub[1].getHexStringValue(),
                        this.n = z(e, 16),
                        i = n.sub[2].getHexStringValue(),
                        this.e = parseInt(i, 16);
                        var s = n.sub[3].getHexStringValue();
                        this.d = z(s, 16);
                        var o = n.sub[4].getHexStringValue();
                        this.p = z(o, 16);
                        var h = n.sub[5].getHexStringValue();
                        this.q = z(h, 16);
                        var a = n.sub[6].getHexStringValue();
                        this.dmp1 = z(a, 16);
                        var u = n.sub[7].getHexStringValue();
                        this.dmq1 = z(u, 16);
                        var c = n.sub[8].getHexStringValue();
                        this.coeff = z(c, 16)
                    } else {
                        if (2 !== n.sub.length)
                            return !1;
                        var f = n.sub[1].sub[0];
                        e = f.sub[0].getHexStringValue(),
                        this.n = z(e, 16),
                        i = f.sub[1].getHexStringValue(),
                        this.e = parseInt(i, 16)
                    }
                    return !0
                } catch (p) {
                    return !1
                }
            }
            ,
            e.prototype.getPrivateBaseKey = function() {
                var t = {
                    array: [new ft.asn1.DERInteger({
                        int: 0
                    }), new ft.asn1.DERInteger({
                        bigint: this.n
                    }), new ft.asn1.DERInteger({
                        int: this.e
                    }), new ft.asn1.DERInteger({
                        bigint: this.d
                    }), new ft.asn1.DERInteger({
                        bigint: this.p
                    }), new ft.asn1.DERInteger({
                        bigint: this.q
                    }), new ft.asn1.DERInteger({
                        bigint: this.dmp1
                    }), new ft.asn1.DERInteger({
                        bigint: this.dmq1
                    }), new ft.asn1.DERInteger({
                        bigint: this.coeff
                    })]
                };
                return new ft.asn1.DERSequence(t).getEncodedHex()
            }
            ,
            e.prototype.getPrivateBaseKeyB64 = function() {
                return b(this.getPrivateBaseKey())
            }
            ,
            e.prototype.getPublicBaseKey = function() {
                var t = new ft.asn1.DERSequence({
                    array: [new ft.asn1.DERObjectIdentifier({
                        oid: "1.2.840.113549.1.1.1"
                    }), new ft.asn1.DERNull]
                })
                  , e = new ft.asn1.DERSequence({
                    array: [new ft.asn1.DERInteger({
                        bigint: this.n
                    }), new ft.asn1.DERInteger({
                        int: this.e
                    })]
                })
                  , i = new ft.asn1.DERBitString({
                    hex: "00" + e.getEncodedHex()
                });
                return new ft.asn1.DERSequence({
                    array: [t, i]
                }).getEncodedHex()
            }
            ,
            e.prototype.getPublicBaseKeyB64 = function() {
                return b(this.getPublicBaseKey())
            }
            ,
            e.wordwrap = function(t, e) {
                if (!t)
                    return t;
                var i = "(.{1," + (e = e || 64) + "})( +|$\n?)|(.{1," + e + "})";
                return t.match(RegExp(i, "g")).join("\n")
            }
            ,
            e.prototype.getPrivateKey = function() {
                var t = "-----BEGIN RSA PRIVATE KEY-----\n";
                return t += e.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
                t += "-----END RSA PRIVATE KEY-----"
            }
            ,
            e.prototype.getPublicKey = function() {
                var t = "-----BEGIN PUBLIC KEY-----\n";
                return t += e.wordwrap(this.getPublicBaseKeyB64()) + "\n",
                t += "-----END PUBLIC KEY-----"
            }
            ,
            e.hasPublicKeyProperty = function(t) {
                return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e")
            }
            ,
            e.hasPrivateKeyProperty = function(t) {
                return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e") && t.hasOwnProperty("d") && t.hasOwnProperty("p") && t.hasOwnProperty("q") && t.hasOwnProperty("dmp1") && t.hasOwnProperty("dmq1") && t.hasOwnProperty("coeff")
            }
            ,
            e.prototype.parsePropertiesFrom = function(t) {
                this.n = t.n,
                this.e = t.e,
                t.hasOwnProperty("d") && (this.d = t.d,
                this.p = t.p,
                this.q = t.q,
                this.dmp1 = t.dmp1,
                this.dmq1 = t.dmq1,
                this.coeff = t.coeff)
            }
            ,
            e
        }(at)
        ,
    dt = "3.2.0"
        ,        
    gt = function() {
            function t(t) {
                t = t || {},
                this.default_key_size = t.default_key_size ? parseInt(t.default_key_size, 10) : 1024,
                this.default_public_exponent = t.default_public_exponent || "010001",
                this.log = t.log || !1,
                this.key = null
            }
            return t.prototype.setKey = function(t) {
                this.log && this.key,
                this.key = new lt(t)
            }
            ,
            t.prototype.setPrivateKey = function(t) {
                this.setKey(t)
            }
            ,
            t.prototype.setPublicKey = function(t) {
                this.setKey(t)
            }
            ,
            t.prototype.decrypt = function(t) {
                try {
                    return this.getKey().decrypt(S(t))
                } catch (e) {
                    return !1
                }
            }
            ,
            t.prototype.encrypt = function(t) {
                try {
                    return b(this.getKey().encrypt(t))
                } catch (e) {
                    return !1
                }
            }
            ,
            t.prototype.sign = function(t, e, i) {
                try {
                    return b(this.getKey().sign(t, e, i))
                } catch (r) {
                    return !1
                }
            }
            ,
            t.prototype.verify = function(t, e, i) {
                try {
                    return this.getKey().verify(t, S(e), i)
                } catch (r) {
                    return !1
                }
            }
            ,
            t.prototype.getKey = function(t) {
                if (!this.key) {
                    if (this.key = new lt,
                    t && "[object Function]" === {}.toString.call(t))
                        return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, t);
                    this.key.generate(this.default_key_size, this.default_public_exponent)
                }
                return this.key
            }
            ,
            t.prototype.getPrivateKey = function() {
                return this.getKey().getPrivateKey()
            }
            ,
            t.prototype.getPrivateKeyB64 = function() {
                return this.getKey().getPrivateBaseKeyB64()
            }
            ,
            t.prototype.getPublicKey = function() {
                return this.getKey().getPublicKey()
            }
            ,
            t.prototype.getPublicKeyB64 = function() {
                return this.getKey().getPublicBaseKeyB64()
            }
            ,
            t.version = dt,
            t
        }();
        s = Object.create || function() {
            function t() {}
            return function(e) {
                var i;
                return t.prototype = e,
                i = new t,
                t.prototype = null,
                i
            }
        }()
        , o = {}
        , h = o.lib = {}
        , a = h.Base = {
            extend: function(t) {
                var e = s(this);
                return t && e.mixIn(t),
                e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                    e.$super.init.apply(this, arguments)
                }
                ),
                e.init.prototype = e,
                e.$super = this,
                e
            },
            create: function() {
                var t = this.extend();
                return t.init.apply(t, arguments),
                t
            },
            init: function() {},
            mixIn: function(t) {
                for (var e in t)
                    t.hasOwnProperty(e) && (this[e] = t[e]);
                t.hasOwnProperty("toString") && (this.toString = t.toString)
            },
            clone: function() {
                return this.init.prototype.extend(this)
            }
        }
        , u = h.WordArray = a.extend({
            init: function(t, e) {
                t = this.words = t || [],
                this.sigBytes = void 0 != e ? e : 4 * t.length
            },
            toString: function(t) {
                return (t || f).stringify(this)
            },
            concat: function(t) {
                var e = this.words
                    , i = t.words
                    , r = this.sigBytes
                    , n = t.sigBytes;
                if (this.clamp(),
                r % 4)
                    for (var s = 0; s < n; s++) {
                        var o = i[s >>> 2] >>> 24 - s % 4 * 8 & 255;
                        e[r + s >>> 2] |= o << 24 - (r + s) % 4 * 8
                    }
                else
                    for (var h = 0; h < n; h += 4)
                        e[r + h >>> 2] = i[h >>> 2];
                return this.sigBytes += n,
                this
            },
            clamp: function() {
                var e = this.words
                    , i = this.sigBytes;
                e[i >>> 2] &= 4294967295 << 32 - i % 4 * 8,
                e.length = t.ceil(i / 4)
            },
            clone: function() {
                var t = a.clone.call(this);
                return t.words = this.words.slice(0),
                t
            },
            random: function(t) {
                for (var e = [], i = 0; i < t; i += 4)
                    e.push(n());
                return new u.init(e,t)
            }
        })
        , c = o.enc = {}
        , f = c.Hex = {
            stringify: function(t) {
                for (var e = t.words, i = t.sigBytes, r = [], n = 0; n < i; n++) {
                    var s = e[n >>> 2] >>> 24 - n % 4 * 8 & 255;
                    r.push((s >>> 4).toString(16)),
                    r.push((15 & s).toString(16))
                }
                return r.join("")
            },
            parse: function(t) {
                for (var e = t.length, i = [], r = 0; r < e; r += 2)
                    i[r >>> 3] |= parseInt(t.substr(r, 2), 16) << 24 - r % 8 * 4;
                return new u.init(i,e / 2)
            }
        },        
        p = c.Latin1 = {
                    stringify: function(t) {
                        for (var e = t.words, i = t.sigBytes, r = [], n = 0; n < i; n++) {
                            var s = e[n >>> 2] >>> 24 - n % 4 * 8 & 255;
                            r.push(String.fromCharCode(s))
                        }
                        return r.join("")
                    },
                    parse: function(t) {
                        for (var e = t.length, i = [], r = 0; r < e; r++)
                            i[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
                        return new u.init(i,e)
                    }
                }
                  ,
        l = c.Utf8 = {
                    stringify: function(t) {
                        try {
                            return decodeURIComponent(escape(p.stringify(t)))
                        } catch (e) {
                            throw new Error("Malformed UTF-8 data")
                        }
                    },
                    parse: function(t) {
                        return p.parse(unescape(encodeURIComponent(t)))
                    }
                }
    
        function EncryptParams(t) {
            t = t || {};
            var e = function(t) {
                for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
                    var n = Math.floor(Math.random() * e.length);
                    i += e.substring(n, n + 1)
                }
                return i
            }(16);
            var e = "KaXZRWDkW&gJwSOE",i = new gt({});
            i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
            var r = i.encrypt(window.btoa(e))
              , s = l.parse("0102030405060708")
              , h = l.parse(e)
              , u = window.btoa(Object.keys(t).join(","))
              , c = {};
            return Object.keys(t).forEach((function(e) {
                var i = t[e]
                  , r = CryptoJS.AES.encrypt(i, h, {
                    iv: s,
                    padding: CryptoJS.pad.Pkcs7
                });
                r = r.toString(),
                c[e] = r
            }
            )),
            {
                EUI: "".concat(r, ".").concat(u),
                encryptedParams: c
            }
        }

function get_user_info() {
    const user = ""  //小米账号明文，手机明文没有用
    const password =""  //密码明文
    const EncryptParam = EncryptParams({
      "user":user 
    })
    const EncrpytPass = CryptoJS.MD5(password).toString().toUpperCase()

    return {
        "user":EncryptParam.encryptedParams.user,
        "password":EncrpytPass,
        "EUI":EncryptParam.EUI
    }

}
~~~

非常神奇的是，帐号处输入手机号明文会登录失败但是用小米账号明文则登录成功，密码则正常输入密码明文即可。

![微信截图_20250610190209](./img/微信截图_20250610190209.png)



## 参考链接

[某米商城登录逆向，user，hash 参数解密_小米登录 逆向](https://blog.csdn.net/Yy_Rose/article/details/125767465?ops_request_misc=%7B%22request%5Fid%22%3A%22c7a2f280a6ef798490057b66f9332356%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=c7a2f280a6ef798490057b66f9332356&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-125767465-null-null.142^v102^pc_search_result_base9&utm_term=某米商城&spm=1018.2226.3001.4187)