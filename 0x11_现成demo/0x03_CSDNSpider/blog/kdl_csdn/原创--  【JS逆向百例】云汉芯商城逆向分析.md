# 原创
：  【JS逆向百例】云汉芯商城逆向分析

# 【JS逆向百例】云汉芯商城逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

继上次粉丝提问，K哥出了对应站点的分析文章之后，又有不少小伙伴提出了在逆向一些网站的时候碰到的问题，态度都很友好，K哥会尽力满足粉丝需求，不过只能一个个慢慢来，本文先对其中一个进行逆向分析：

### 逆向目标

### 逆向过程

#### 抓包分析

打开开发者人员工具，随便搜索一个型号的芯片，在 Network 中即会抓包到相应的数据接口，即 `/search/ajax-get-res-v001`：

请求参数如下，`keyword` 大概率就是加密的搜索内容，`v_` 是固定值，`font_ident`、`p`、`_csrf` 都会动态变化，需要逐个研究分析：

该网站存在风控，会弹出极验四代语序点选的验证码，这里就不赘述了，感兴趣的可以阅读K哥往期文章 [【验证码逆向专栏】极验三代、四代点选类验证码逆向分析](https://mp.weixin.qq.com/s/MTiaBvjvDXU_SXC0y429ZQ)：

### 逆向分析

#### keyword 参数

该接口是 XHR（XMLHttpRequest）类型的请求，可以直接下个 XHR 断点，这样定位到的位置通常在加密处理完成之后，已经准备发送请求了，优点是便于踪栈，更容易找到加密的地方。在开发者人员工具 Source 面板右侧的 XHR/fetch Breakpoints 中添加截取的接口 URL：

刷新网页即会断住：

向上跟栈到 ajax 中，于 send 处打下断点，F8 下步断点，断过来，可以看到，此时 keyword 参数的值是明文，也就是搜索的芯片型号：

接下来就需要找一下这段明文是在哪被加密的，向上跟栈到 `psB-acac185595.js` 中，很明显，该 js 经过了 OB 混淆（Obfuscator），感兴趣的可以使用 AST 技术解一下，关键的加密逻辑大概率就藏在这里面。跟到下图处，出现了几个接口所需的请求参数，这里的 keyword 仍是明文状态：

直接在 `psB-acac185595.js` 中 ctrl+f 搜索 keyword，总共有 23 个结果，不多，逐个分析下，在可能是加密算法的位置打断点分析，`ERJU03F1002V` 在下图处被加密成了 `RVJKVTAzRjEwMDJW`：

跟进到 `_0x7f9865[_0xfe4009(0x82c)]` 函数中，直接把算法扣下来：

```
function orOperator(_0x1e4532, _0x39fc6b) {
    return _0x1e4532 | _0x39fc6b;
}

function andOperator(_0x241af9, _0x10df1e) {
            return _0x241af9 &amp; _0x10df1e;
        }
function lessCompare(_0x58aa60, _0x251729) {
    return _0x58aa60 &lt; _0x251729;
}

function RightShiftOperator(_0x50cbd4, _0x2a3840) {
    return _0x50cbd4 &gt;&gt; _0x2a3840;
}

function addOperator(_0xea955f, _0x17d167) {
    return _0xea955f + _0x17d167;
}

function utf8Encode(_0xe407f5) {
    _0xe407f5 = _0xe407f5["replace"](/\r\n/g, '\x0a');
    for (var _0xeefa10 = '', _0x4fcfd7 = 0x0; _0x4fcfd7 &lt; _0xe407f5["length"]; _0x4fcfd7++) {
        var _0x1451bf = _0xe407f5["charCodeAt"](_0x4fcfd7);
        lessCompare(_0x1451bf, 0x80) ? _0xeefa10 += String["fromCharCode"](_0x1451bf) : _0x1451bf &gt; 0x7f &amp;&amp; _0x1451bf &lt; 0x800 ? (_0xeefa10 += String["fromCharCode"](_0x1451bf &gt;&gt; 0x6 | 0xc0),
            _0xeefa10 += String["fromCharCode"](orOperator(0x3f &amp; _0x1451bf, 0x80))) : (_0xeefa10 += String["fromCharCode"](orOperator(_0x1451bf &gt;&gt; 0xc, 0xe0)),
            _0xeefa10 += String["fromCharCode"](_0x1451bf &gt;&gt; 0x6 &amp; 0x3f | 0x80),
            _0xeefa10 += String["fromCharCode"](0x3f &amp; _0x1451bf | 0x80));
    }
    return _0xeefa10;
}

function encryptKeyword(_0x3a29c2) {
    let keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    let _0x40e006, _0x2e7dee, _0x2f707d, _0x70f89f, _0x1d4342, _0x55ace3, _0xee897c, _0x482490 = '',
        _0x4326f6 = 0x0;
    for (_0x3a29c2 = utf8Encode(_0x3a29c2); _0x4326f6 &lt; _0x3a29c2["length"];)
        _0x40e006 = _0x3a29c2["charCodeAt"](_0x4326f6++),
            _0x2e7dee = _0x3a29c2["charCodeAt"](_0x4326f6++),
            _0x2f707d = _0x3a29c2["charCodeAt"](_0x4326f6++),
            _0x70f89f = _0x40e006 &gt;&gt; 0x2,
            _0x1d4342 = (0x3 &amp; _0x40e006) &lt;&lt; 0x4 | RightShiftOperator(_0x2e7dee, 0x4),
            _0x55ace3 = (0xf &amp; _0x2e7dee) &lt;&lt; 0x2 | _0x2f707d &gt;&gt; 0x6,
            _0xee897c = andOperator(0x3f, _0x2f707d),
            isNaN(_0x2e7dee) ? _0x55ace3 = _0xee897c = 0x40 : isNaN(_0x2f707d) &amp;&amp; (_0xee897c = 0x40),
            _0x482490 = addOperator(addOperator(_0x482490, keyStr.charAt(_0x70f89f)) + keyStr.charAt(_0x1d4342), keyStr.charAt(_0x55ace3)) + keyStr.charAt(_0xee897c);
    return _0x482490;
}

let searchKeyWord = "ERJU03F1002V";
let searchKeyWordEncryptResult = encryptKeyword(searchKeyWord);
console.log(searchKeyWordEncryptResult);  // RVJKVTAzRjEwMDJW

```

我们来分析下这是什么算法，倒着看，`_0x70f89f`、`_0x1d4342` 之类的是一些十进制数，`keyStr.charAt(_0x70f89f)` 就是获取 keyStr 字符串特定位置的字符值，最后拼接起来：

```
_0x482490 = addOperator(addOperator(_0x482490, keyStr.charAt(_0x70f89f)) + keyStr.charAt(_0x1d4342), keyStr.charAt(_0x55ace3)) + keyStr.charAt(_0xee897c);

```

keyStr 就是源码中的 `this["_keyStr"]`，其值如下，长度为 65 位：

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=

```

这一串完全符合 Base64 编码索引表的特征，包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、加号（+）和斜杠（/），64 位，还有一个填充字符（=），Base64 编码的基本流程如下，例如编码 Hello 字符串：
1. 首先，将 Hello 转换为 ASCII 码，得到 `72 101 108 108 111`；1. 然后，每三个字节一组（数据块，不足三个则在末尾填充零），得到 `72 101 108` 和 `108 111 0`；1. 每组的三个 ASCII 码，分别转为八位二进制数，不足的在前面补 0，比如 `72 101 108` 得到 `01001000 01100101 01101100`，首尾相连，形成 24 位的二进制数；1. 将 24 位的二进制数，拆分为四个 6 位的小组；1. 将每组二进制数转换为十进制，并从 Base64 索引表中查找对应的字符；1. 使用填充字符 “=” 添加到编码结果的末尾，以保证编码结果的长度为 4 的倍数。
ASCII 码表和 Base64 索引表可于公众号回复关键词 ascii 或 base64 获取，Base64 编码图解：

其实该数据接口对于 Base64 编码也有所提示 乛◡乛：

可以去 [K哥爬虫工具站](https://www.kgtools.cn/secret/base64) 验证一下，结果一致：

至此 keyword 参数就分析完成了。

#### v 参数

前文提到几个加密参数都在一块，如下图所示，断住后观察一下，`v` 为 `_0x501622`，定义在上面几行，就是 13 位时间戳：

```
_0x501622 = JSON["stringify"](new Date()["getTime"]());

```

#### font_ident

font_ident 直接从 this 中取到，其值不是通过加密算法生成的，在该网页的源代码中，可以直接使用 xpath 或者正则表达式匹配出来：

#### p 参数

p 参数值长度为 32 位，看着很像是 MD5 加密，我们来跟一下，p 参数在下图处生成：

跟到 `_0x101cba[_0xfe4009(0x412)` 函数中去，p 参数的值就是 `window['x']`：

直接 hook 一下 window 中的 x 参数，断住后跟栈分析，使用 Fiddler 或者油猴之类的都可以，hook 脚本如下：

```
(function() {
    'use strict';
    Object.defineProperty(window, 'x', {
        get: function() {
            debugger;
            return "";
        },
        set: function(value) {
            debugger;
            return value;
        },
    });
})();

```

刷新网页，成功断住，此时 `window['x']` 的值已经生成了：

向上跟栈到 VM 中，可以看到 window.x = hex_md5(‘xxx’)，这里像是 MD5 加密的源码：

我们直接拿加密内容去爬虫工具站测试一下，发现值并不一样，这里的 MD5 算法可能经过了魔改：

先直接将整段代码扣下来，保存到本地，简单改改能直接运行：

来看看传入的 `17104110xxx` 是什么，接着向上跟栈到下图处，这里的逻辑就很有意思了，`_0x4c3be9` 就是 MD5 加密的参数：

```
eval(_0x24f5ec["decode"](_0x2b037f)["replace"]("mwqqppz", "'" + _0x4c3be9 + "'"));

```

跟进到 `_0x24f5ec["decode"]` 函数中分析一下，取消 hook，断进去，`_0xc8f1ce` 就是 `_0x2b037f`，是一个固定的字符串，这里的算法逻辑是不是很眼熟，和 keyword 参数一样，是 base64，不过这里是解码的过程，将一大串字符串还原成了刚刚的 MD5 算法，用 replace 方法替换 `mwqqppz` 字符串传入待加密值，最后使用 eval 方法执行解码出的 JavaScript 代码，实现加密操作：

接着跟栈分析 `17104110xxx`，跟到 `handleParamsV1` 中去，加密参数就是由 `p1`、`p2_`、`code` 三个参数拼接而成的：

往后跟下栈就会发现，`p1` 参数是个时间戳，其值和前文所讲的 `v` 参数的值相同，`p2_` 就是搜索的芯片型号经过 base64 编码后得到的值，`code` 定义如下：

```
tmp = $.md5(p1 + p2_)
, code = eval(window.relwarckcuf + '("' + tmp + '")');

```

与前面的不同，`$.md5` 使用的是标准的 MD5 加密算法：

`window.relwarckcuf` 的值会变化，其值需要从该页面的源代码中获取：

生成 code 同样使用到了 eval 方法，逻辑就是将 tmp 参数值传到了 `window.relwarckcuf` 函数中，生成了最终的 code 值，较为别致，跟进到这个函数中去：

跳转到 `79baf82e5b7315e32957b68b5b3d0260` 文件中，这个文件名是会动态变化的，每次刷新页面都不一样，同样可以从网页源代码中提取出来，完整链接 `https://search.ickey.cn/x/c/79baf82e5b7315e32957b68b5b3d0260`：

就是套了两个 switch，做了些运算，不同文件 `4|1|2|3|6|5|0` 的顺序会变，但算法的执行顺序其实是固定的，唯一会变的值就是 `_0x5b2c03['lQMEJ']`，先将函数部分扣下来：

JavaScript 代码：

```
function xb9397d46e271a79d37e14478d0bbd99d(_0x3589bd) {
    var _0x5b2c03 = {
        'NMqMe': function(_0xf40245, _0x5f3db1) {
            return _0xf40245 &lt; _0x5f3db1;
        },
        'dutuH': function(_0x305515, _0x16b9ff) {
            return _0x305515 % _0x16b9ff;
        },
        'FgcEp': function(_0x4f1496, _0x4a009b) {
            return _0x4f1496 / _0x4a009b;
        },
        'Krfyp': function(_0x5e7e97, _0x3a2b65) {
            return _0x5e7e97 - _0x3a2b65;
        },
        'cuUNs': function(_0x482dab, _0x2d4aa7) {
            return _0x482dab / _0x2d4aa7;
        },
        'KYiBU': function(_0x63165e, _0x35b40d) {
            return _0x63165e + _0x35b40d;
        },
        'vAfft': function(_0x59664e, _0x587b82) {
            return _0x59664e + _0x587b82;
        },
        'lQMEJ': "abcd"
    }
      , _0x34838f = "4|1|2|3|6|5|0"["split"]('|')
      , _0xdf0619 = 0x0;
    while (!![]) {
        switch (_0x34838f[_0xdf0619++]) {
        case '0':
            return _0x27369a;
        case '1':
            var _0x5c31de = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            continue;
        case '2':
            var _0x5e9e9b = 36;
            continue;
        case '3':
            var _0x7c3dbb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
            continue;
        case '4':
            var _0x27369a = '';
            continue;
        case '5':
            for (var _0xb3aee8 = 0x0; _0x5b2c03['NMqMe'](_0xb3aee8, 32); _0xb3aee8++) {
                var _0x34f9cc = "4|0|5|2|3|1|6"["split"]('|')
                  , _0x1ff8ce = 0x0;
                while (!![]) {
                    switch (_0x34f9cc[_0x1ff8ce++]) {
                    case '0':
                        _0x1da465 = _0x5b2c03["dutuH"](_0x3b7479, _0x5e9e9b);
                        continue;
                    case '1':
                        _0x3a7eff = _0x5b2c03["dutuH"](_0x3b7479, _0x5e9e9b);
                        continue;
                    case '2':
                        _0x38b5d0 = _0x5b2c03["dutuH"](_0x3b7479, _0x5e9e9b);
                        continue;
                    case '3':
                        _0x3b7479 = _0x5b2c03["FgcEp"](_0x5b2c03["Krfyp"](_0x3b7479, _0x38b5d0), _0x5e9e9b);
                        continue;
                    case '4':
                        _0x3b7479 = _0x3589bd["charCodeAt"](_0xb3aee8);
                        continue;
                    case '5':
                        _0x3b7479 = _0x5b2c03["cuUNs"](_0x5b2c03["Krfyp"](_0x3b7479, _0x1da465), _0x5e9e9b);
                        continue;
                    case '6':
                        _0x27369a += _0x5b2c03["KYiBU"](_0x5b2c03["KYiBU"](_0x5b2c03["vAfft"](_0x7c3dbb[_0x3a7eff], _0x7c3dbb[_0x38b5d0]), _0x7c3dbb[_0x1da465]), _0x5b2c03["lQMEJ"]);
                        continue;
                    }
                    break;
                }
            }
            continue;
        case '6':
            var _0x3b7479, _0x1da465, _0x38b5d0, _0x3a7eff;
            continue;
        }
        break;
    }
}
console.log(xb9397d46e271a79d37e14478d0bbd99d('9b6ed790af9bae4b109a79870590af51'));

```

Python 复现：

```
def get_md5_encrypt_str(_0x3589bd):
    dynamic_parameter = 'abcd'
    _0x27369a = ''
    _0x5e9e9b = 36
    _0x7c3dbb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    _0x3b7479, _0x1da465, _0x38b5d0, _0x3a7eff = 0, 0, 0, 0
    for _0xb3aee8 in range(len(_0x3589bd)):
        _0x3b7479 = ord(_0x3589bd[_0xb3aee8])
        _0x1da465 = _0x3b7479 % _0x5e9e9b
        _0x3b7479 = int((_0x3b7479 - _0x1da465) / _0x5e9e9b)
        _0x38b5d0 = _0x3b7479 % _0x5e9e9b
        _0x3b7479 = int((_0x3b7479 - _0x38b5d0) / _0x5e9e9b)
        _0x3a7eff = _0x3b7479 % _0x5e9e9b
        _0x27369a += _0x7c3dbb[_0x3a7eff] + _0x7c3dbb[_0x38b5d0] + _0x7c3dbb[_0x1da465] + dynamic_parameter
    return _0x27369a


print(get_md5_encrypt_str('9b6ed790af9bae4b109a79870590af51'))

```

前文提到，下图的这个值是会改变的：

我们来分析一下，这个值为什么会变，跟进到 `_0x2a0d2b` 函数中去，这里都是通过传一个整数和一个字符串，`_0x2c3e()` 就是个大数组，会变化，从数组中按索引取值然后计算得到最终的参数值，`0x1c2` 位置的值也并非固定的，数组和这个值都需要匹配出来：

`_0x7ebea5(大数组)` 以及一些值需要动态提取，这段代码简化后如下：

```
function _0x1497(_0x187038, _0x57dea3) {
    _0x7ebea5 = ["w3RcVeZcUG", "WPruWOZcQgu", "W741WO7cGCkw", "WOSBzhPY", "W78+WRNdM8oKuHpcImorWOOgWOa", "zmkojCkPja", "xCk4WRVcRce", "F0iPWR3cImkXAYRdV1pdKLC", "BvFdP2ldOW", "s8oSubiw", "WOD/W67cJSku", "WRJdNf1hW6tcNSoQ", "W5eaW414W5GRWPFdMG", "W4/dNtFcL8k/vCk6W5iaWRj8qG", "m8okEd9L", "WQ8SW6CsW6a", "CCk5W7xcVtO", "W7xdNLjHW5K", "imohcmkieq", "cmk7W49TEq", "WPvDCSoZW6u", "ChldUh4S", "WOVcS3tcKMi", "kf8Gdai", "mfjGWOFdNIe", "W6pcUqZdVmknW44", "k0vKWPm", "WQumW6ioW5a", "WOVcP8o3W5hdQ8oeEb4", "W7G+WPpcQSkD", "WQ1+W7/cUHnO", "DSklWQFdUM0", "WR4dE8kD", "qCozWPNcVCoY", "wmoQDSorWRK", "cSo/FqTr", "t8kqmSkIkG", "lxu9aXS", "EutcHmkGjW", "WOaCyKXC", "FmkEWOdcSXO", "aCoEomk5na", "W7lcVJ/cHCo8queWWOe", "Bd8oC8oc", "FCk6WQFcPHqf", "WQjuW5/cVmkg", "CNxdI8kXW6RcSW", "tvOZiu16W4VcVSouW4OgWPtcN8owpG", "lbFcUtJcUxLnW6OSW5rcWO7cTxNdQW", "W77dKg1iW4C", "WPn9WOtcK2m", "WPrKWRdcNre", "c8oyW6xdK8kY", "awS/gZW", "W6hcVrtdSSkEW4FdNg7dJW", "W7u/WRNdLCoKwWNcG8o1WOWmWRy", "CgxdN04+W5i", "WPSFBgTubGVdTSoXW4u", "qCkpW7rKWOPnWOm", "DSouzZal", "WPqeALT9", "WQ5vW6TmW5u", "WPnAuSozzeDjpbdcLmoD", "FrG8q8oSW6FdKtddGSku", "WQ1TWOFcGb8", "W6dcLsFdSmks", "W4hcIHRdUmk4", "lCozp8ozW4jZnSk8W5XQlCk7bW", "W7BdVJlcG8o+q0OSWQZcVmoeW69fWQLbWOTAW6i9WPRdK3BcKGv+qSonjq/dJtrLdmoGov3cVrpdTdr9EZq8DSk3fSotfqdcOW3cS8kLcvK9CsHNW6mlydGxWRxdRmoSwCoHWPbvW5OeWRFdQcqUW4/cVcxcI8kUDmofW43cJ10NdCovrbJcKWxdO8kWn8owWQ0nW6ZcHXeiWQ8wWP7cMSkbW6hcISo7W44PW78lWOymifNdKCoOnCkAzaWnhMq", "dmkEW7LSBG", "ACk7WPpcIHi", "WQNcVmkDwmoh", "FIijWRbh", "wCoaWPNcLSos", "W7uBWPLCW7y", "WR5LWOVcQgJcQK/dKrnd", "gmoXhmkmjmk8wG", "bcDOcgq", "BKFdQCkqW5G", "W5zuWQZcS2u6omkzWQFcSSocoq", "aCozW7VdV8kH", "WRnrumoZW7rAW65D", "DKZcI8kyhq", "WRrJWO7cV1pcIK0", "WQtcHuNdLSoD", "jCobqWHP", "DWmTw8oc", "WRdcJeBdVCoD", "WPHmWOtcLfS", "WQyCW5ykW7e", "WPfhWPpcNL0", "WPtcNwBdGq", "tfXIFdq5WQZdQG", "W60mfsLR", "vSkAWPtdH0NcVW", "xghdVCkrW6K", "W65fl8onW5dcGCo2iXDbWQ00", "tCorAWhcMxdcTSkuWPDtiCkiW7aSeSkdWRVcK8k/W7JcV8oJyxW2W5ldMNuFu8o0WP5nWRy0AG", "sv9SzGa+WRVdPq", "WRdcJwZdLSo1", "W6ZcLH/cTmoB", "WQLFWQhcLZq", "zSoRxW", "wCoJW7JdHmk6W4fm", "WRPcrmoJyq", "bmkOW75tDG", "jmk6bvLNWQBdPSorWQRdPCoLWQi", "WQdcMLxcO2m", "oCkWW5fIWPq", "WRmivSkXWQu", "WPrdW6VcQCkx", "W58QpYm", "W5SvWQHAW4m", "W5bFjtC8qetcUSkBWPGKka", "cmoRrIin", "w8ouWORcU8od", "gwjUWPtdKG", "tmooWP7cG8oCWPxcL8kMEmkkWO/dN8kuCf/cPdRdNSkJW4hdSqC3WQ3dPaPnWQXctLFdSmkbW7veW6ddUs4", "W7ZdPwH5W64", "W6vdkSolW5ZcH8oFhYH5WR4b", "iSoCW4FdOCkd", "uCk1W43cKX0", "WQdcPh3cGe0", "CKldPwZdOYe", "s8omrI4g", "zSkoWR3dTfi", "W6WnprXmW74SeSoBb8okWRP9CmkAW5L+WOVcMmktW4bzW5vwW4bDWQ7dJdq", "WQ94WOJcVgG", "eW9VDrCI", "nCkshMRdMG", "fSkOW6jwEW", "aJH8W6ldVq", "zwJcSGVcVqFcR3FcIG", "WRCbBSkxWP0", "WRf9W4pcOCkv", "t0JcMCkAdgZcPG", "WQuuF8kjWOFdMq", "u8k+WPJcNCoRWPLQnd5CdCoC", "WPXquSonzf0", "WRtcPNldVSo2", "W7q/WR3dN8oQuaRcSCoWWQCnWPu", "cXJcHmkcdNVcH8kp", "W6BdRcRdJtlcMGNdNc9IWP/dKq", "WO9ZWQFcGcaKs2y", "zCktWOFcJra", "WQfpW6VdOmoEWOS4CWRdPx/dNq", "CHuZvSoBW6a", "D1BdKSkfW78", "WPXFWRNcRMu", "aCoeW7ZdS8kI", "zLpdL1iq", "hNulWO1O", "WQD4W4P/W44", "WQubCSksWPa", "WQD/W53cOCki", "FSk6WP7cGYi", "d8odsbjR", "W7KAWRtcV8ktW5m", "fCkQkeldVW", "bSkuW5rRWOW", "WPdcP8kkr8oi", "WReKwN1K", "WPu5z8kDWO0", "s8oEWQtcGCo4WQtcG8kGsCoFWONdLG", "ecjpxs0", "b2mWWO9l", "F1FdU2FdRG", "WQxdSwnKW4S", "omoxoCkdiW", "haD8W4ldLSogtqZdSLBdGeFdRCkMCIywW6OMlmoVW7zAW7OzWOpcKSkEWPVcSq7dNCkZptP2qW1JAsfPW4VdPHbiq20vW6tdUhhcM0BcTqtdH8kfW4S5WORcHmoqW4BdHM5NvCkSW5VdJCowW6fqWQBdK13cHZ0HnapdJmkRWPtdQSkaWQbGpCoxkSkJW6dcVa", "WPu5t8k0WOS", "wCoEAraG", "smonWO3cVCow", "kxqHpG0", "WPZcTSkpvSot", "WQT/WQtcVN0", "tw7cQw3cIG", "W5JcTHFdLmk8", "W5m0W5ZdMNLKdIGZW6CjyW", "W7ZcJ2PEW5/cKmoefW", "WPbXWQ7cUbS", "jcjonwe", "xKlcH8kfgx3cTSkzWPDcWRG", "c2ldSxJdJrKjE8kBWP5h", "WQTrymoMW7jAW69u", "tvS1ivv4WOZdMmkIWPPVWQu", "WQZdJeniW7hcLmoGdG", "aSo8W43dJa", "W4BcJZxdV8kk", "w1FcGXRcQG", "D8oaymocWOjN", "WQP3W7JcH8kM", "WRhcI0NdHCoI", "DmkfW5JcVay", "lcTKqrm", "EmonB8oxWRvGymkLWQ1I", "mmo5vZWZ", "tSkNWRtdHfm", "F8oVWP7cJ8oD", "W5xcIc3dT8kS", "tCkwWQtdUfm", "f8kBW6XaWQi", "wSoCxISb", "wSkQbNDmWPbUW6ibbxHX", "uxVcKKBcVa", "WQ1iW4FcR8k7", "WRddVg9fW5i", "wCodWPJcMmojWQxcJmk1", "W6BcSGBdVSkbW6NdJG", "vYK7q8oH", "vCkbW6NcNW", "y8kyWQhdOf8", "W4W6WO3cVmkX", "uCogsay4", "f8kuW5XcWOe", "WQX4r8otW4C"];
    if (_0x187038 &gt; 0x1c2){
        _0x187038 = _0x187038 - 0x1c2;
    }
    var _0x979086 = _0x7ebea5[_0x187038];

    var _0x18815a = function (_0x12f3cc) {
        var _0x4baee4 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
        var _0x34cff1 = ''
            , _0x32f5a8 = ''
            , _0x5720b1 = _0x34cff1 + _0x18815a;
        for (var _0x5baceb = 0x0, _0x464e32, _0x444df3, _0x286151 = 0x0; _0x444df3 = _0x12f3cc['charAt'](_0x286151++); ~_0x444df3 &amp;&amp; (_0x464e32 = _0x5baceb % 0x4 ? _0x464e32 * 0x40 + _0x444df3 : _0x444df3,
        _0x5baceb++ % 0x4) ? _0x34cff1 += _0x5720b1['charCodeAt'](_0x286151 + 0xa) - 0xa !== 0x0 ? String['fromCharCode'](0xff &amp; _0x464e32 &gt;&gt; (-0x2 * _0x5baceb &amp; 0x6)) : _0x5baceb : 0x0) {
            _0x444df3 = _0x4baee4['indexOf'](_0x444df3);
        }
        for (var _0x2093c7 = 0x0, _0x3586f3 = _0x34cff1['length']; _0x2093c7 &lt; _0x3586f3; _0x2093c7++) {
            _0x32f5a8 += '%' + ('00' + _0x34cff1['charCodeAt'](_0x2093c7)['toString'](0x10))['slice'](-0x2);
        }
        return decodeURIComponent(_0x32f5a8);
    };
    
    var _0x39e653 = function (_0x218a50, _0x1ead99) {
        var _0x4ec5dd = [], _0x568ad6 = 0x0, _0x4d9de0, _0x4a61ba = '';
        _0x218a50 = _0x18815a(_0x218a50);
        var _0x590931;
        for (_0x590931 = 0x0; _0x590931 &lt; 0x100; _0x590931++) {
            _0x4ec5dd[_0x590931] = _0x590931;
        }
        for (_0x590931 = 0x0; _0x590931 &lt; 0x100; _0x590931++) {
            _0x568ad6 = (_0x568ad6 + _0x4ec5dd[_0x590931] + _0x1ead99['charCodeAt'](_0x590931 % _0x1ead99['length'])) % 0x100,
                _0x4d9de0 = _0x4ec5dd[_0x590931],
                _0x4ec5dd[_0x590931] = _0x4ec5dd[_0x568ad6],
                _0x4ec5dd[_0x568ad6] = _0x4d9de0;
        }
        _0x590931 = 0x0,
            _0x568ad6 = 0x0;
        for (var _0x2312e7 = 0x0; _0x2312e7 &lt; _0x218a50['length']; _0x2312e7++) {
            _0x590931 = (_0x590931 + 0x1) % 0x100,
                _0x568ad6 = (_0x568ad6 + _0x4ec5dd[_0x590931]) % 0x100,
                _0x4d9de0 = _0x4ec5dd[_0x590931],
                _0x4ec5dd[_0x590931] = _0x4ec5dd[_0x568ad6],
                _0x4ec5dd[_0x568ad6] = _0x4d9de0,
                _0x4a61ba += String['fromCharCode'](_0x218a50['charCodeAt'](_0x2312e7) ^ _0x4ec5dd[(_0x4ec5dd[_0x590931] + _0x4ec5dd[_0x568ad6]) % 0x100]);
        }
        return _0x4a61ba;
    };

    var _0x55e8a2 = _0x7ebea5[0x0]
        , _0x2a1bd8 = _0x187038 + _0x55e8a2;

    _0x979086 = _0x39e653(_0x979086, _0x57dea3);
    return _0x979086;
}

console.log(_0x1497(633, 'Wc%L'));

```

一般情况下，可以使用 AST 技术或者正则表达式，将上述动态变化的值匹配出来，然后传入到算法中，即可得到最终的结果：

#### _csrf 参数

跟到 `'_csrf': _0x66ec8(_0x506031(0x1e8) + 'rf')[_0x370168(0x7a1)]()` 中分析一下就会发现，`_csrf` 参数与 `font_ident` 参数一样，都是从网页源代码中获取到的：

至此，所有参数都分析完成了。

cookies 中有个参数值 seaut，如果该值或者加密参数不对，是无法获取到数据的（网页端的 cookies 可删除、修改参数值）：

### 结果验证
