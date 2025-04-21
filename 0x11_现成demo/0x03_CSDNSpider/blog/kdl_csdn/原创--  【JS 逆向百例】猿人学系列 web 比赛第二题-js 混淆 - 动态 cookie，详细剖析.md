# 原创
：  【JS 逆向百例】猿人学系列 web 比赛第二题：js 混淆 - 动态 cookie，详细剖析

# 【JS 逆向百例】猿人学系列 web 比赛第二题：js 混淆 - 动态 cookie，详细剖析

### 逆向目标

### 逆向过程

#### 抓包分析

进入网页，点击右键查看页面源代码，搜索不到直播间相关数据信息，证明是通过 ajax 加载的数据，ajax 加载有特殊的请求类型 XHR，打开开发者人员工具，刷新网页进行抓包，会跳转到虚拟机中，进入无限 debugger，过无限 debugger 的方式在往期文章中有详细介绍，感兴趣的可以去阅读学习一下，这里直接在 debugger 行右键选择 never pause here，然后下一步断点即可过掉：

在 Network 的筛选栏中选择 XHR，数据接口为 2，在响应预览中可以看到当前页各手机发布日的热度：

这时候点击第二页，会弹出提示框：cookie 失效，正在重置页面，证明 cookie 是有时效性的，并且会进行校验：

cookie 中有个关键加密参数 m，其内容如下：

#### 逆向分析

通过 hook cookie 中 m 参数的方式对其进行定位，hook 的方式有很多种，可以阅读 K 哥往期文章，对其有详细介绍，这里使用编程猫 Fiddler 插件进行 hook，相关插件在 K哥爬虫公众号发送【**Fiddler插件**】即可获取，Hook 代码如下：

```
(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('m') != -1) {
        debugger;
      }
      console.log('Hook捕获到cookie设置-&gt;', val);
      cookieTemp = val;
      return val;
    },
    get: function () {
      return cookieTemp;
    },
  });
})();

```

勾选开启框，启动 Fiddler 进行 hook 注入：

刷新网页，如果进入无限 debugger，则按上述方式解决，不过直接通过 m 参数定位并不是最好的方案，因为该 cookie 中还有其他参数包含 m 字母，位置不对则刷新网页，这里成功断在 m 参数的值生成的位置：

向上跟栈到 _0xdad69f (2:18) 处，然后点击左下角 { } 格式化代码，会跳转到 2:formatted 文件的第 4943 行，该行内容如下：

```
document[$dbsm_0x42c3(qqLQOq, iOiqII) + $dbsm_0x42c3(q1IoqQ, QQlLlq)] = _0x5500bb['\x4e\x74\x44' + '\x72\x43'](_0x5500bb[$dbsm_0x42c3(qqqQoq, oqQiiO) + '\x6d\x65'](_0x5500bb[$dbsm_0x42c3(Ioo0ql, olq0Oq) + '\x6d\x65'](_0x5500bb[$dbsm_0x42c3(qOIqQi, OOqIQi) + '\x72\x44'](_0x5500bb[$dbsm_0x42c3(Q1qoqQ, lILOOq) + '\x72\x44'](_0x5500bb[$dbsm_0x42c3(qOO1Q0, oiqlQQ) + '\x72\x44'](Ql1OO0, _0x5500bb['\x7a\x76\x67' + '\x6c\x77'](_0x3c9ca8)), Qoqq0I), _0x5500bb[$dbsm_0x42c3(iqOiQ0, QOiq0Q) + '\x47\x6b'](_0x313b78, _0x160e3a)), lOo0QQ), _0x160e3a), _0x5500bb[$dbsm_0x42c3(qiOOiO, liQIoQ) + '\x4e\x5a']),

```

控制台打印后可知这里就是 cookie 中 m 参数值生成的位置：

在控制台中进一步打印分析下其他部分含义：

m 参数值的格式如下：

```
0ef478cf61e0749d7444c7997c917679|1663213224000

```

可以依此将代码进行简化：

```
_0x5500bb[$dbsm_0x42c3(iqOiQ0, QOiq0Q) + '\x47\x6b'](_0x313b78,_0x160e3a) + lOo0QQ + _0x160e3a

```

控制台打印验证，结果匹配：

接下来先跟进到 _0x5500bb[$dbsm_0x42c3(iqOiQ0, QOiq0Q) + ‘\x47\x6b’] 中，鼠标选中后点击进入：

在该文件的第 3911 行，内容如下：

```
_0x434ddb[$dbsm_0x42c3(Iooo0l, Qq1oqI) + '\x47\x6b'] = function(_0x105ffe, _0x733be0) {
            return _0x105ffe(_0x733be0);
        }

```

返回值为 `_0x105ffe(_0x733be0)`，该函数传入的参数为 `_0x313b78` 和 `_0x160e3a`，所以可以进一步改写：

```
_0x313b78(_0x160e3a) + lOo0QQ + _0x160e3a

```

_0x160e3a 为时间戳，因此 m 参数的值是将时间戳作为参数传入 _0x313b78 函数后加密得到的，所以需要进一步跟进到 _0x313b78 函数定义的位置，同样鼠标选中，点击即可跳转到第 4933 行，到 node 环境中调试，初步代码为：

```
function _0x313b78(_0x575158, _0x1fa91a, _0x1cf5de) {
    // 以下部分内容过长，此处省略
    // 完整代码关注 GitHub：https://github.com/kgepachong/crawler
}

var _0x160e3a = Date.parse(new Date());
var m = _0x313b78(_0x160e3a) + lOo0QQ + _0x160e3a;

console.log(m);

```

运行后会提示 _0x5500bb 未定义，到原文件中 ctrl + f 局部搜索这个函数，在第 3940 行：

```
_0x5500bb = _0x434ddb

```

补上运行后会提示 `_0x434ddb` 未定义，搜索后发现 `_0x434ddb` 在第 2817 行定义为一个空对象，后面向其中传入了很多值，类似于一个大数组，不能只补 `_0x434ddb = {};`，需要把传值部分补进去，不然后面运行时会出现些报错，经测试有的部分不要也可以，但是细扣就很麻烦了，直接全补即可，这就很多了，从第 2817 行一直扣到第 3939 行，补完后接着运行程序，这次又提示 `$dbsm_0x42c3` 未定义，接着搜找其定义位置，在第 94 行，补了后提示 OooIi1 未定义，在第 209 行，需要从第 209 行到第 2816 行全部补上，不然会提示其中某一个未定义，同样的，虽然经调试有的不需要也行，但是一个个调麻烦且没有必要，补完后接着运行又会提示 `$dbsm_0x123c ` 未定义：

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-e2FdjCJ7-1668066078702)(https://s2.loli.net/2022/09/15/oOjAwDZmXuEkI2c.png)]

其在第 22 行，是个大数组，补了之后运行程序后发现卡住了，一段时间后程度报错：

这个报错可能是内存资源耗尽导致程序崩溃了，将这部分代码复制到浏览器中进行调试，开启一个新页面，打开开发者人员工具，在 Sources 中选择 Snippets，新建一个脚本，将已经扣下来的代码粘贴进去，在第一行写入 debugger；手动打断点调试，ctrl + s 保存文件后点击右下角按钮运行脚本即会在第一行断住：

点击单步调试，一步步查看是哪里出了问题：

点了几步后，卡了一下，跳到第 2711 行，是个 for 循环，右侧出现红框报错，意思是潜在的内存崩溃，即单步调试断到到此处时程序临近内存崩溃：

接着往后单步调试，会发现一直在第 2712 行和第 2713 行间来回执行，到后来甚至浏览器崩溃了，所以问题出在 WxzuQr 对象中出现了无限循环，直至耗尽了内存资源：

这部分内容在 $dbsm_0x42c3 函数中，接下来需要研究一下崩溃原因，右侧堆栈中向上跟栈，上两步分别通过构造函数创建了两个实例对象 WjJIeN 和 vnuqco，WjJIeN 部分如下：

```
_0x11a714['prototype']['WjJIeN'] = function(_0x4859ef) {
                if (!Boolean(~_0x4859ef)) {
                    return _0x4859ef;
                }
                return this['WxzuQr'](this['yewpLt']);
            }

```

这里进行了一个 if 判断，~ 为按位取反，意思是如果 !Boolean(~_0x4859ef) 的值为 false，则执行 WxzuQr 的无限循环行为，直至程序崩溃，接着跟进到 vnuqco 部分，查看 _0x4859ef 是啥，对什么进行了判断：

```
_0x11a714['prototype']['vnuqco'] = function() {
                _0x2940ac = new RegExp(this['PuKGlh'] + this['CTXIfT']),
                _0x3fba94 = _0x2940ac['test'](this['XxpyjG']['toString']()) ? --this['yHmSUE'][0x1] : --this['yHmSUE'][0x0];
                return this['WjJIeN'](_0x3fba94);
            }

```

返回值中给 WjJIeN 传入的参数为 _0x3fba94，其定义在第 2699 行，是个三目表达式：

```
_0x2940ac['test'](this['XxpyjG']['toString']()) ? --this['yHmSUE'][0x1] : --this['yHmSUE'][0x0];

```

到控制台打印输出一下，看看该行各部分什么含义：

`--this['yHmSUE'][0x1]` 的值固定为 -1，而每运行一次 `this['yHmSUE'][0x0]` 的值即减一：

```
console.log(!Boolean(~-1)) // true
console.log(!Boolean(~-2)) // false

```

所以只有当 `_0x2940ac['test'](this['XxpyjG']['toString']())` 的值为 true 时才不会进入无限循环，在控制台打印下 `this['XxpyjG']['toString']()` 部分内容：

这个函数在第 2689 行，再来看看对其进行了怎样的判断，跟进到 _0x2940ac 定义位置，在第 2698 行，是个正则表达式对象，控制台中打印后可知道表达式为：

```
/\w+ *\(\) *{\w+ *['|"].+['|"];? *}/

```

所以匹配样式大致如下：XXX( ){ XXX ’ XXX ’ ;}，并不匹配换行符、制表符、空格等，没格式化的代码会被压缩成一行，所以这里相当于格式化检测，由于一开始进行了格式化操作，因此判断结果为 false，从而进入了无限循环，导致程序崩溃，所以只需要将这部分内容压缩为一行即可，检验一下：

没有格式化后打印出的结果为 true，即不会调用到 WxzuQr 对象，从而进入无限循环，修改后再次运行程序，结束了吗，当然没有，上个问题倒是解决了，又出现了以下报错：

报错在第 3854 行，内容如下：

```
_0x5500bb[$dbsm_0x42c3(QoLq0i, q0Oqqo) + '\x5a\x49']

```

接着在浏览器中进行调试，在这一行上面打上 debugger；然后运行脚本，断住后打印分析一下：

‘\x5a\x49’ 即 ‘ZI’，QoLq0i、q0Oqqo 为定值，因此问题出在 `$dbsm_0x42c3` 函数中，其实如果对 OB 混淆了解的话会知道这种混淆方式有一些特征，其一般由三部分组成：大数组、移位自执行函数、解密字符串函数，大数组我们之前已经找到了，就是 `$dbsm_0x123c`，而 `$dbsm_0x42c3` 是解密字符串函数，这里差了个移位自执行函数，缺东西自然结果会不对，需要找到将其补上，在第 23 行到第 93 行，夹在 `$dbsm_0x123c` 和 `$dbsm_0x42c3` 之间，补完后运行程序，又到了熟悉的卡住，过了一会后报错：

报错在第 27 行，放到浏览器中进行调试，还是在开头打上 debugger；运行后单步向下执行，点了几下熟悉的卡住，然后跳到第 24 行 for 循环处：

右侧出现熟悉的警告提示，证明又进入到无限循环了，果不其然，过了一会浏览器页面就崩溃了：

根据之前的经验，看看是不是哪又有个格式化检测导致进入到这个循环里，果不其然，在第 55 行：

这里是对 removeCookie 处的代码进行了格式化检测，同样将函数体部分写成一行即可：

```
'removeCookie': function() {return 'dev';},

```

接着运行，又提示 _0x3c9ca8 未定义，ctrl + f 局部搜索找到函数定义位置扣下来即可，运行后又提示 _0x1316f4 未定义，这个扣下来之后记得将后面的自执行的括号删掉，接着会提示 _0x12a78e 未定义，扣下来的时候同样记得删掉末尾的括号，再接着就没什么特别需要注意的了，差哪个函数补哪个就行了，到后面提示 navigator 未定义，简单地补浏览器环境即可，node 环境下 window 设置为 global：

```
var window = global; 
window.navigator = {};

```

自然不会这么轻易的结束了，运行后又会提示 _0x184fb0 未定义，跟之前一样，搜到扣下来即可，后面就是漫长的补函数的过程，没别的技巧，就是需要耐心，手都 cv 酸了，直到出现如下报错：

报错提示 history 未定义，这是个浏览器对象，显示在 console.log 处报错，在 console.log 行打断点调试，运行到这里时会跳转到虚拟机中，其中代码如下：

history.pushState 是向浏览器的会话历史中添加记录，当使用 console.log 输出结果的时候，就会执行 history.pushState，但是我们并没有 history 环境，所以会报错，补了 history 环境后运行程序发现一直卡着，仔细看代码才发现有个 while 循环，最离谱的是里面的 for 循环设置了 1100000 次，几乎可以说是在不间断检测，等不得等到猴年马月去了，这里直接将 console.log 赋值给一个变量替换掉即可，记得放到前面：

```
var result = console.log;

```

至此，终于结束了！成功打印出 m 参数的值：

这个题倒是不难，逆向下来思路也很清晰，但是扣代码的过程繁杂且坑不少，还是很值得大家上手去练习的。

### 完整代码

bilibili 关注 K 哥爬虫，小助理手把手视频教学：https://space.bilibili.com/1622879192

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

以下只演示部分关键代码，不能直接运行！

#### JavaScript 代码

```
var window = global; 
window.navigator = {};
var result = console.log;

// 以下部分内容过长，此处省略
// 完整代码关注 GitHub：https://github.com/kgepachong/crawler

function _0x313b78(_0x575158, _0x1fa91a, _0x1cf5de) {
    if (_0x5500bb[$dbsm_0x42c3(QoLq0i, q0Oqqo) + '\x5a\x49'](_0x5500bb[$dbsm_0x42c3(LQOI0Q, QqOI00) + '\x73\x42'], _0x5500bb[$dbsm_0x42c3(Q00oiq, QIioOo) + '\x5a\x76'])) {
        VWQQuv['\x6f\x4f\x61' + '\x68\x47'](debuggerProtection, Q0LiqQ);
    } else {
        _0x5500bb[$dbsm_0x42c3(i1lQqq, q110Lq) + '\x62\x45'](_0x3c9ca8);
        return _0x1fa91a ? _0x1cf5de ? _0x5500bb[$dbsm_0x42c3(iqqLQO, LoOOOq) + '\x4b\x6b'](_0x21cf21, _0x1fa91a, _0x575158) : _0x5500bb['\x72\x71\x75' + '\x4b\x51'](y, _0x1fa91a, _0x575158) : _0x1cf5de ? _0x5500bb[$dbsm_0x42c3(qLQQ1q, I1oOQ1) + '\x4d\x6e'](_0x443ca7, _0x575158) : _0x5500bb[$dbsm_0x42c3(qLLoQi, iO0OQo) + '\x4d\x6e'](_0x184fb0, _0x575158);
    }
}

function getCookieM(){
    var _0x160e3a = Date.parse(new Date());
    var m = _0x313b78(_0x160e3a) + lOo0QQ + _0x160e3a;
    return m;
}

// var _0x160e3a = Date.parse(new Date());
// var m = _0x313b78(_0x160e3a) + lOo0QQ + _0x160e3a;

// result(m);

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


def get_cookie_m():
    heat_total = 0
    for page_num in range(1, 6):
        with open('yrx2.js', 'r', encoding='utf-8') as f:
            encrypt = f.read()
            cookie_m = execjs.compile(encrypt).call('getCookie')
        headers = {
            "user-agent": "yuanrenxue,project",
        }
        cookies = {
            "sessionid": " 填入自己的 sessionid ",
            "m": cookie_m
        }
        url = "https://match.yuanrenxue.com/api/match/2?page=%s" % page_num
        response = requests.get(url, headers=headers, cookies=cookies)
        for i in range(10):
            value = response.json()['data'][i]
            heat = re.findall(r"'value': (.*?)}", str(value))[0]
            heat_total += int(heat)
    print(heat_total)


if __name__ == '__main__':
    get_cookie_m()

```

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-sP1ILjxK-1668066078715)(https://s2.loli.net/2022/09/16/rghFTyRYDqNK8UH.gif)]<br/> <img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/e275b1b54e7f627440e5c566dc87881e.png"/>
