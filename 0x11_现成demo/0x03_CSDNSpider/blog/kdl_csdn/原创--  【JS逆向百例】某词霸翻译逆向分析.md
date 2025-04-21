# 原创
：  【JS逆向百例】某词霸翻译逆向分析

# 【JS逆向百例】某词霸翻译逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

今天在查看某平台私信的时候，发现有位粉丝表示自己在逆向某站的过程中，有一些疑惑，态度十分友好，K哥一向是尽力满足粉丝需求的，本文就对该站进行逆向研究，该案例不难，不过为了便于粉丝理解，会写的相对详细点，大佬们直接跳过就可以了~

### 逆向目标

### 抓包分析

进入翻译页，左边输入查询单词，右边即会翻译出中文释义，很显然通过接口传输的数据：

F12 打开开发者人员工具，重新输入一个英文单词，比如 ratel，进行抓包，`/index.php` 接口的 Form Data 中有个 q 参数，很明显，就是我们输入的待翻译的英文单词，请求参数 sign 是经过加密的：

那么，响应返回的自然就是翻译后的中文释义，点到 Preview 响应预览中查看一下，发现并没有出现想象中的`蜜罐`两字，显然 content 就是翻译结果，只不过被加密处理了：

接下来，我们分别对 sign 参数和 content 参数进行逆向分析。

### 逆向分析

#### sign 参数

定位的方式有很多，由于该接口是 XHR（XMLHttpRequest）类型的请求，我们可以直接下个 XHR 断点，这样定位到的位置通常在加密处理完成之后，已经准备发送请求了，优点是便于踪栈，更容易找到加密的地方：

在开发者人员工具 Source 面板右侧的 XHR/fetch Breakpoints 中添加截取的接口 URL：

重新输入单词，即会断住，可以看到，此时 sign 参数已经生成了：

向上跟栈到 takeRusult 中，以下部分中，看起来相当像在拼接 sign 参数：

```
// encodeURIComponent —&gt; 将特殊字符（例如冒号、斜杠、问号、等号、以及非 ASCII 字符）转换成 UTF-8 编码的十六进制表示
"/index.php?c=trans&amp;m=fy&amp;client=6&amp;auth_user=key_web_new_fanyi&amp;sign=".concat(encodeURIComponent(r))

```

在该行打下断点，释放掉 XHR 断点，重新输入查询单词即会断住，encodeURIComponent® 就是 sign 值：

看看 r 参数是什么，就定义在上面：

```
r = (0, _.$Q)(r)

```

断到该行，先选中 `_.$Q`，跟进去，看看是什么加密算法：

很明显的 AES 加密，mode 为 ECB，padding 为 PKCS7，key 是经过一系列编码得到的，为定值 `L4fBtD5fLC9FQw22`：

直接引库复现即可：

```
// 引用 crypto-js 加密模块
const CryptoJS = require('crypto-js')

function aesEncrypt(aesKey, text) {
    let key = CryptoJS.enc.Utf8.parse(aesKey),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // ECB 加密方式，Pkcs7 填充方式
        encrypted = CryptoJS.AES.encrypt(srcs, key, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

// 结果验证
let aesKey = 'L4fBtD5fLC9FQw22';
let text = '679eddc40bc55be3'
let encryptResult = aesEncrypt(aesKey, text);
console.log(encryptResult);

```

再来分析下 `(0, _.$Q)(r)` 中的 r，定义在上一行，内容如下：

```
var r = u()("6key_web_new_fanyi".concat(s.LI).concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);

```

逐段分析一下这部分：

关键就在于这部分了：

```
u()("6key_web_new_fanyi".concat(s.LI).concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString()

```

这一段将 `6key_web_new_fanyi6dVjYLFyzfkFkkratel` 加密了，长度为 32 位：

32 位就比较特别了，根据经验，猜测是 MD5 加密，去 www.kgtools.cn 验证一下，果然，结果一致：

当然还可以搜索 MD5 摘要算法源码中的一些特征，1732584193、4023233417 之类的，大多数都是标准的算法，MD5 算法的源码可于公众号回复关键词 `MD5` 获取：

完整算法：

```
// 引用 crypto-js 加密模块
const CryptoJS = require('crypto-js')

function aesEncrypt(aesKey, text) {
    let key = CryptoJS.enc.Utf8.parse(aesKey),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // ECB 加密方式，Pkcs7 填充方式
        encrypted = CryptoJS.AES.encrypt(srcs, key, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

function getSign(){
    let searchWord = 'ratel'
    let aesKey = 'L4fBtD5fLC9FQw22';
    let concatSearchParams = '6key_web_new_fanyi' + '6dVjYLFyzfkFkk' + searchWord;
    let md5EncryptResult = CryptoJS.MD5(concatSearchParams).toString().substring(0, 16);
    let sign = aesEncrypt(aesKey, md5EncryptResult);
    return encodeURIComponent(sign);
}

console.log(getSign());  // C0W0FqJdhxUeFmgdJ162GdRriqVIAJSQ%2BxmfU0q7dIE%3D

```

当然，也可以直接使用 Python 复现：

```
import base64
import hashlib
import urllib.parse
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def aes_encrypt(aes_key: str, text: str) -&gt; str:
    key = aes_key.encode('utf-8')
    srcs = text.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    # 在加密之前进行填充
    padded_data = pad(srcs, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    # 返回 base64 编码后的密文
    return base64.b64encode(encrypted).decode('utf-8')


def get_sign() -&gt; str:
    search_word = 'ratel'
    aes_key = 'L4fBtD5fLC9FQw22'
    concat_search_params = '6key_web_new_fanyi' + '6dVjYLFyzfkFkk' + search_word
    md5_encrypt_result = hashlib.md5(concat_search_params.encode()).hexdigest()[:16]
    sign = aes_encrypt(aes_key, md5_encrypt_result)
    return urllib.parse.quote(sign)


logger.info(get_sign())  # C0W0FqJdhxUeFmgdJ162GdRriqVIAJSQ%2BxmfU0q7dIE%3D

```

#### content 参数

我们来看看 takeResult 的结构，这就是一个异步操作链：

```
takeResult: function (e) {
    ........
    v("/index.php?c=trans&amp;m=fy&amp;client=6&amp;auth_user=key_web_new_fanyi&amp;sign=".concat(encodeURIComponent(r)), {
        ........
    }).then((function (e) {
            var t = 1 === (null === e || void 0 === e ? void 0 : e.status) ? A(A({}, e), {}, {
                content: JSON.parse((0,
                    _.B6)(e.content))
            }) : e;
            return console.log(t),
                t
        }
    )).catch((function (e) {
            return e
        }
    ))
}

```

跟进到 v 函数中，返回了一个 Promise 对象，用于异步处理请求的结果：

Promise.then 用于注册当异步操作成功完成时执行的回调，这里接受了一个参数，即成功时的回调函数：

```
function (e) {
    var t = 1 === (null === e || void 0 === e ? void 0 : e.status) ? A(A({}, e), {}, {
        content: JSON.parse((0,
            _.B6)(e.content))
    }) : e;
    return console.log(t),
        t
}

```

大伙应该注意到了，`content: JSON.parse((0, _.B6)(e.content))`，这里是否就是 content 参数解密还原出释义的算法位置呢？跟进到 `_.B6` 中去看看，同样是 AES 算法，断住后就会发现，解密的位置确实是这里，out 经过了 Unicode 编码，key 为定值 `aahc3TfyfCEmER33`：

```
import base64
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def aes_decrypt(ciphertext):
    key = 'aahc3TfyfCEmER33'.encode('utf-8')
    # 将密文进行 base64 解码
    ciphertext = base64.b64decode(ciphertext)
    # 创建 AES 解密器对象
    cipher = AES.new(key, AES.MODE_ECB)
    # 对密文进行解密
    decrypted_data = cipher.decrypt(ciphertext)
    # 对解密后的数据进行去填充操作
    decrypted_data = unpad(decrypted_data, AES.block_size)
    # 返回解密后的明文
    return decrypted_data.decode('utf-8')


content = 'X2NheRsV7GVaBbfK/jxZ6h6rWRz0J268vfthunwKmlJIHB687XwU1lxRMBgI+YF5652luVBNTUhVKvlnLYwMqSstRS4f5IYpz1a9YcYdXa/rXx65frmbDe5TKkih255dl8RwKe97E/JowqGPq1d5qnpm1rhY96/4IBwcpvtQFVgVrvcAP+RyIHOwRAByBR30Pzh9NPptSnQZm/n0/GSpnPbmR1WWZ0v5WOlCsDSYjWgzXOg/54z83oI+Yj/bKoR66YbMab+mmtIXcnhp+Uwb2rCoWF0whrcrbM5CHyCEuZ52pHYJ3cRzPNgFvf6GqoEWgeF4SMo22JYGqDKK6VrhJyCvs1BFAUNdYrsGlLNmlrsQkuYxQlM40/3DTZX4cxav'
logger.info(aes_decrypt(content))

```

### 结果验证
