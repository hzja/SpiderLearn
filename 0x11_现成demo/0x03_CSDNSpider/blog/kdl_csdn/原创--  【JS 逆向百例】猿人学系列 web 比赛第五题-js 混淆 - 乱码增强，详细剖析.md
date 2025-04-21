# 原创
：  【JS 逆向百例】猿人学系列 web 比赛第五题：js 混淆 - 乱码增强，详细剖析

# 【JS 逆向百例】猿人学系列 web 比赛第五题：js 混淆 - 乱码增强，详细剖析

### 逆向目标

### 逆向过程

#### 抓包分析

进入网页，点击右键查看页面源代码，搜索不到直播间相关数据信息，证明是通过 ajax 加载的数据，ajax 加载有特殊的请求类型 XHR，打开开发者人员工具，刷新网页进行抓包，在 Network 的筛选栏中选择 XHR，数据接口为 5?m=XXX&amp;f=XXX，在响应预览中可以看到各直播间热度数据：

接口 url 有两个请求参数 m 和 f，现在还不知道具体怎么来的：

本题提示 cookie 有效期仅为 50 秒钟，即 cookie 值是在动态变化的，经过对比分析，cookie 中有两个动态变化的参数 m 和 RM4hZBv0dDon443M，接下来需要定位到其生成的位置：

### 逆向分析

#### Cookie 加密参数分析

可以通过 Hook Cookie 的方式定位参数位置，这里通过 Fiddler 编程猫插件进行 Hook，相关插件在 K哥爬虫公众号发送【**Fiddler插件**】即可获取，Hook 代码如下：

```
(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('RM4hZBv0dDon443M') != -1) {
        debugger;
      }
      console.log('Hook捕获到cookie的值-&gt;', val);
      cookieTemp = val;
      return val;
    },
    get: function () {
      return cookieTemp;
    },
  });
})();

```

将以上代码写入插件中，注入 Hook：

清除网页缓存，勾选开启框，打开 Fiddler 进行 Hook 注入，可以发现成功断住：

从右侧堆栈中向上跟栈，会发现跟到了虚拟机 VMXXX 中，点击右下角 { } 格式化，跳转到了第 978 行，代码部分如下：

```
_0x3d0f3f[_$Fe] = 'R' + 'M' + '4' + 'h' + 'Z' + 'B' + 'v' + '0' + 'd' + 'D' + 'o' + 'n' + '4' + '4' + '3' + 'M=' + _0x4e96b4['_$ss'] + ';\x20path=/';

```

在该行打下断点进行调试，控制台打印相关参数：

前面各字母组成起来就是 RM4hZBv0dDon443M=，此处就是 RM4hZBv0dDon443M 参数加密后赋值给 cookie 的位置，所以关键的加密部分为 `_0x4e96b4['_$ss']`，打印相关内容会发现 _0x4e96b4 是 window 对象，window. _$ss 即加密后的值：

直接搜索 _$ss 没有结果，同样尝试 Hook，Hook 代码：

```
(function () {
  'use strict'
  Object.defineProperty(window, '_$ss', {
    set: function (val) {
      console.log('Hook捕获到_$ss的值-&gt;', val);
      debugger;
    },
    });
})();

```

成功断住：

同样向上跟栈，找到其定义位置，跟到了虚拟机中，格式化后跳到第 1229 行：

```
_0x4e96b4['_$' + _$UH[0x348][0x1] + _$UH[0x353][0x1]] = _0x29dd83[_$UH[0x1f]]();

```

在该行打下断点调试分析各自含义：

因此关键的加密位置肯定在 _0x29dd83 中，往上看， _0x29dd83 定义在第 1225 行，这时候眼前一亮，看到了 mode 和 padding 两个关键字，这里大概率为 AES 或者 DES 加密，将代码解混淆替换后的结果如下：

```
_$Ww = _$Tk['enc']['utf-8']['parse'](_0x4e96b4['_$pr']['toString']()),
_0x29dd83 = _$Tk['AES'](_$Ww, _0x4e96b4['_$qF'], {
    'mode': _$Tk['mode']['ECB'],
    'padding': _$Tk['pad']['pkcs7']
}),
_0x4e96b4['_$ss'] = _0x29dd83['toString']();

```

现在就很明显了，这里为 AES 加密，加密内容为 ` _$Ww`，key 值为 `_0x4e96b4['_$qF']`，加密模块为 ECB，填充方式为 pkcs7：

`_$Ww` 的值由 `_0x4e96b4['_$pr']` 转换为字符串后经过 utf-8 编码得到，其与 key 值 `_0x4e96b4['_$qF']` 都是数组，需要知道这两个数组是怎么生成的，先 ctrl + f 搜索 `_0x4e96b4['_$qF']`，定义在第 1444 行，内容如下：

```
_0x4e96b4['_$qF'] = CryptoJS['enc']['Utf8'][_$UH[0xff]](_0x4e96b4['btoa'](_0x4e96b4['_$is'])['slice'](0x0, 0x10));

```

在该行打下断点，控制台打印分析一下：

由此可见，`_0x4e96b4['_$qF']` 是通过 CryptoJS 库将字符串经过 base64 加密后取前 16 位的结果，搜索 `_0x4e96b4['_$is']`，找到字符串生成的位置，在第 674 行，由 _KaTeX parse error: Expected group after '_' at position 19: …赋值，在上一行可以看到熟悉的 _̲Fe，即 cookie，发现 cookie 中的 m 参数是在这里定义的：

```
_0x3d0f3f[_$Fe] = 'm=' + _0x474032(_$yw) + ';\x20path=/';

```

参数 m 的值也与 `_$yw` 有关，m 参数是将 `_$yw ` 经过 `_0x474032` 函数处理后得到，后面再专门进行分析，`_$yw ` 定义在第 672 行：

```
_$yw = _0x2d5f5b()[_$UH[0x1f]]();

```

`_$UH[0x1f]` 为 “toString”，`_$yw` 的值是将 `_0x2d5f5b()` 函数的返回值转换成了字符串得到的，跟进到该函数定义的位置，搜索后发现在第 279 行，控制台打印后发现这里就是时间戳，所以 `_$yw` 即时间戳：

因此 `_0x4e96b4['_$qF']`的值是将时间戳经过 base64 加密后取了前 16 位的结果，接下来只需要知道 `_0x4e96b4['_$pr']`是如何生成的，就能复现出 RM4hZBv0dDon443M 参数的加密过程，在第 1224 行打断点调试发现此时的 `_0x4e96b4['_$pr']` 数组包含五个值：

现在就需要知道这五个值是在哪传进去的，搜索 `_0x4e96b4['_$pr']` 看看哪里对其进行了赋值，每个都打下断下，该数组定义在第 270 行：

```
_0x4e96b4['_$pr'] = new _0x4d2d2c();

```

`_0x4d2d2c` 在第 224 行定义为 Array，所以这里是创建了一个数组 `_0x4e96b4['_$pr']`，接着往后找传值的地方，继续运行断点调试，第 1717 行的断点运行了四次传入了四个值：

```
_0x4e96b4['_$pr']['push'](_0x474032(_$Wa));

```

跟进 _$Wa 定义的位置，在第 1715 行，由 _0x12eaf3 函数生成，跟进到这个函数的位置，在第 275 行，返回值解混淆后如下：

```
Date['parse'](new Date());

```

再次下一步调试断点会跳转到第 868 行，这时候数组被传入了第五个值，`_$yw` 为时间戳，由于 `m = _0x474032(_$yw)`，所以第五个值也就是参数 m 的值，记住这里出现的 `_0x4e96b4['_$is']`：

```
_0x3d0f3f[_$Fe] = 'm=' + _0x474032(_$yw) + ';\x20path=/';
_0x4e96b4['_$is'] = _$yw;
_0x4e96b4['_$pr']['push'](_0x474032(_$yw));

```

数组值的生成位置都找到了，跟 m 参数一样，传入的值都经过了 _0x474032 函数的处理，因此需要跟进 _0x474032 函数，鼠标选中，点击即可跳转到该函数定义的位置：

在第 455 行，返回值为三目表达式：

```
function _0x474032(_0x233f82, _0xe2ed33, _0x3229f9) {
        return _0xe2ed33 ? _0x3229f9 ? v(_0xe2ed33, _0x233f82) : y(_0xe2ed33, _0x233f82) : _0x3229f9 ? _0x41873d(_0x233f82) : _0x37614a(_0x233f82);
}

```

在 return 处打下断点调试，_0x233f82 为传入的 _$yw 的值，即时间戳，后面两个参数均为 undefined，所以不妨将函数简化下：

```
function _0x474032(_0x233f82, _0xe2ed33, _0x3229f9) {
    return _0x37614a(_0x233f82);
}

```

接下来需要跟进到 _0x37614a 函数的位置：

```
function _0x37614a(_0x32e7c1) {
        return _0x499969(_0x41873d(_0x32e7c1));
}

```

这里就需要跟出 `_0x499969` 函数和 `_0x41873d` 函数的内容，接下来就是扣，缺啥补啥，缺函数补函数，缺环境补环境，若报错提示 ` _$UH is not defined`，`_$UH` 是个大数组，直接将其整体解混淆替换掉就行了，例如：

```
_$UH[0x6c] ---&gt; "length" 

```

或者写成键值对形式：

```
_$UH = {
    8: 'prototype',
    15: 'charCodeAt',
    31: 'toString',
    108: 'length'
}

```

值得注意的是 _0x11a7a2 函数，运行时会报错 `op is not defined`，op 定义在第 308 行：

op 的值为 26，这里直接将其定义成固定值即可，即 var op = 26;

同样将 `_0x42fb36` 和 b64pad 也写成固定值，即 `_0x42fb36 = 16;` 、`b64pad = 1`;

调试过程中还发现 `window['_$6_']`、`window['_$tT']`、`window['_$Jy'] ` 这几个参数的值是在动态变化的，不进行改写甚至将相关部分注释掉，在本地 node 环境中都是可以运行出结果的，但是用 python 调用的话会报错，证明在前端会对这几个参数进行校验，这几个参数在 `_0x11a7a2` 函数中定义，该函数溯源后最终被 `_0x474032` 函数调用，`_0x474032` 函数对 `_$yw` 的值进行处理，生成了 `_0x4e96b4['_$pr']` 数组的最后一个值及 m 参数的值，所以如果这几个参数的值匹配错误的话会导致校验失败，我们只需要打断点看 m 参数的值生成的时候，这三个参数的值是多少，然后写成固定值就行了：

```
window['_$6_'] = -389564586;
window['_$tT'] = -660478335;
window['_$Jy'] = -405537848;

```

至此 Cookie 中 RM4hZBv0dDon443M 参数和 m 参数的生成逻辑就疏通了，以下通过 JavaScript 对其复现：

```
// 以下函数部分内容过长，此处省略
// 完整代码关注 GitHub：https://github.com/kgepachong/crawler

var CryptoJS = require('crypto-js');
 
function rm4Encrypt(_$yw, pr){
    var value = Buffer.from(_$yw).toString('base64').slice(0, 16);
    var srcs = CryptoJS.enc.Utf8.parse(pr);
    var key = CryptoJS.enc.Utf8.parse(value);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

var _$yw = new Date().valueOf().toString();
var _$Wa = Date.parse(new Date())
function pr(){
    pr = [];
    for (i = 1; i &lt; 5; i++) {
        // _$Wa 传入四个值
        pr.push(_0x474032(_$Wa))
    }
    // _$yw 传入一个值
    pr.push(_0x474032(_$yw));
    return pr.toString();
}

var RM4hZBv0dDon443M = rm4Encrypt(_$yw, pr());
// m 为数组传入的最后一个值
var m = pr[4];
console.log('RM4hZBv0dDon443M 参数加密后的值为: ' + RM4hZBv0dDon443M)
console.log('m 参数的值为: ' + m)

```

运行结果：

#### 请求头参数分析

Cookie 中的参数分析完了，还有两个请求参数 m 和 f 没有解决，直接从接口处跟栈，从 Initiator 中跟到 request 里：

点击右下角 { } 格式化后会跳转到 `5:formatted` 文件的第 856 行，在第 883 行的 list 中可以找到参数 m 和 f 的定义位置：

```
"m": window._$is,
"f": window.$_zw[23]

```

m 的值是 `window._$is`，有没感觉似曾相识，就是上文所说的 `_0x4e96b4['_$is']` ，`_0x4e96b4` 就是 window，所以这里 m 的值其实就是 `_$yw` ；f 的值是 `window.$_zw[23]` ，现在需要知道 `$_zw[23]` 的值怎么生成的，局部搜索 `$_zw` 会发现该数组定义在第 611 行，接着往后找，看看数组中的第 23 个是什么，先控制台打印一下内容：

第 633 行内容是第六个，顺下去找会发现第 23 个的内容如下：

```
$_aiding.$_zw.push($_t1);

```

在此处打下断点调试验证一下，可以发现结果是一样的：

接下来只需要找到 `$_t1` 的定义位置即可，ctrl + f 局部搜索 `$_t1` ，其定义在第 613 行，是个时间戳：

```
let $_t1 = Date.parse(new Date());

```

可以发现与 _$Wa 的定义方式一致，对比一下 m 和 f 两个参数的值会发现差值接近于 50 秒，与题目中提示的 Cookie 有效期仅 50 秒钟对应上了：

在虚拟机文件的第 1975 行也有个 50 秒的定时器：

至此所有参数生成的逻辑都调理清晰了，本题并不难，但是扣代码的过程中有许多需要注意的细节，猿人学给大家提供了一个优质的练习平台，做题也是一个很好的自我提升的方式。

### 完整代码

bilibili 关注 K 哥爬虫，小助理手把手视频教学：https://space.bilibili.com/1622879192

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

以下只演示部分关键代码，不能直接运行！

#### JavaScript 代码

```
var _0x4e96b4 = window = {};
var _0x1171c8 = 0x67452301;
var _0x4dae05 = -0x10325477;
var _0x183a1d = -0x67452302;
var _0xcfa373 = 0x10325476;
var _0x30bc70 = String;

// 以下函数部分内容过长，此处省略
// 完整代码关注 GitHub：https://github.com/kgepachong/crawler

var CryptoJS = require('crypto-js');
 
function rm4Encrypt(_$yw, pr){
    var value = Buffer.from(_$yw).toString('base64').slice(0, 16);
    var _$Ww = CryptoJS.enc.Utf8.parse(pr);
    var key = CryptoJS.enc.Utf8.parse(value);
    var encrypted = CryptoJS.AES.encrypt(_$Ww, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

function getParamers() {
    pr = []; 
    for (i = 1; i &lt; 5; i++) {
        var _$Wa = Date.parse(new Date());
        pr.push(_0x474032(_$Wa))
    }
    var _$yw = new Date().valueOf().toString(); 
    pr.push(_0x474032(_$yw));
    cookie_m = pr[4];
    cookie_rm4 = rm4Encrypt(_$yw, pr.toString());
    return{
        "cookie_m": cookie_m,
        "cookie_rm4": cookie_rm4,
        "m": _$yw,
        "f": Date.parse(new Date()).toString()
    }
}
 
console.log(getParamers());

```

#### Python 代码

```
# =======================
# --*-- coding: utf-8 --*--
# @Time    : 2022/9/8
# @Author  : 微信公众号：K哥爬虫
# @FileName: yrx5.py
# @Software: PyCharm
# =======================

import execjs
import requests
import re


def encrypt_yrx5():
    room_heat_all = []
    for page_num in range(1, 6):
        with open('yrx5.js', 'r', encoding='utf-8') as f:
            encrypt = f.read()
            encrypt_params = execjs.compile(encrypt).call('getParamers')
        headers = {
            "user-agent": "yuanrenxue,project",
        }
        cookies = {
        	# 填入自己的 sessionid
            "sessionid": " your sessionid ",
            "m": encrypt_params['cookie_m'],
            "RM4hZBv0dDon443M": encrypt_params['cookie_rm4']
        }
        params = {
            "m": encrypt_params['m'],
            "f": encrypt_params['f']
        }
        url = "https://match.yuanrenxue.com/api/match/5?page=%s" % page_num
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        for i in range(10):
            value = response.json()['data'][i]
            room_heat = re.findall(r"'value': (.*?)}", str(value))[0]
            room_heat_all.append(room_heat)
    room_heat_all.sort(reverse=True)
    top_five_total = 0
    for i in range(5):
        top_five_total += int(room_heat_all[i])
    print(top_five_total)


if __name__ == '__main__':
    encrypt_yrx5()

```
