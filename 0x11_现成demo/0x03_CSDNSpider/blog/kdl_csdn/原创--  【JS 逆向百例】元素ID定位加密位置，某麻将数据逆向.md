# 原创
：  【JS 逆向百例】元素ID定位加密位置，某麻将数据逆向

# 【JS 逆向百例】元素ID定位加密位置，某麻将数据逆向

#### 文章目录

---


### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### 逆向过程

#### 抓包分析

本次要逆向的对象于以往不同，不是某个接口的参数，而是网页中的数据，一般网页中的数据都可以在源码中看到，或者通过某个接口传过来，而本次的目标数据是通过 JS 加密得到的，先来抓包看看基本情况：

F12 检查，可以看到我们要的数据在 textarea 标签里面，看起来没什么毛病，那么直接使用 Xpath 提取试试看：

```
import requests
from lxml import etree


url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
headers = {
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
tree = etree.HTML(response.text)
data = tree.xpath('//textarea/text()')
print(data)

```

可以看到实际上提取到的数据是为空的，我们查看网页源代码，直接搜索 textarea，同样也是没有的，试试直接搜索数据也是没有的：

#### 加密逆向

既然这种数据不存在于网页源码中，也不是通过其他接口返回的，那么最有可能就是通过 JS 加密后直接插入到网页源码中的，那么这里应该如何定位加密的位置呢？对比一下插入数据后的网页源码和未插入数据的网页源码，可以看到蓝色框里的代码都是通过 JS 插入的，而且这个 1008.js 多半就是加密的 JS 文件：

这里我们想到一个 JavaScript 语法，如需从 JavaScript 访问某个 HTML 元素，可以使用 `document.getElementById(id)` 方法，这个 id 就是某个 HTML 元素的属性，然后使用 `innerHTML` 来获取或插入元素内容，可以看菜鸟教程的一个例子：

通过这种语法，结合前面源码中的几个标签，我们就可以猜测，某个 JS 里面可能会存在这样的语句：`document.getElementById("tehai").innerHTML`、`document.getElementById("tips").innerHTML`、`document.getElementById("m2").innerHTML`，直接全局搜索其中任意一个语句，就可以在 1008.js 里面找到对应的结果，当然直接搜索这个标签的 id 也是可以找到结果的，埋下断点进行调试：

可以发现第 913 行 `document.getElementById("m2").innerHTML = d + "&lt;br&gt;"` 是向 `m2` 标签里面插入值 `d` 和换行符，一步一步往上看，可以发现 `d` 包含了很多 html 的东西，而上面的 `g` 只有文本，刚好是目标数据，那么我们最终返回直接 return 这个 `g` 就好了。

继续往上跟踪 `g` 的值的来源，会发现步骤比较复杂，那么我们直接将这部分函数（fa 函数）整个复制下来运行调试（大约第 794 行至第 914 行）， 本地进行调试会提示 `ga` 和 `O` 未定义，我们在其定义的语句的下一行埋下断点进行调试，可以看到 `ga` 的值其实是固定的 `q`，`O` 就是 URL 后面 `q` 的值，如：`336m237p2479s167z3s`

将这两个变量进行定义后，接着本地调试，又会提示 `aa`、`ca` 等函数未定义，依赖的函数比较多，那么这种情况下就没必要去挨个扣，直接将 `fa` 以前的所有函数都 copy 下来进行调试即可，这样就直接解决了所有依赖。

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码**，完整代码仓库地址：https://github.com/kgepachong/crawler/

#### 关键 JS 加密代码架构

```
// Copyrights C-EGG inc.

var u = function () {}();

function w() {}

w.prototype = {};

function x(b, a, g, d) {}

// 此处省略 N 个函数

function M(b) {}

function N(b, a) {}

function ea(b) {}

function fa(O) {
    function b(a, b) {
        var c, d = 0;
        for (c = 0; c &lt; a.length; ++c) d += 4 - b[a[c]];
        return d
    }

    // var a = ga, g = O, d;
    var a = 'q', g = O, d;
    d = "&lt;hr size=1 color=#CCCCCC &gt;";
    switch (a.substr(0, 1)) {
        case "q":
            d += '標準形(七対国士を含む)の計算結果 / &lt;a href="?p' + a.substr(1) + "=" + g + '"&gt;一般形&lt;/a&gt;&lt;br&gt;';
            break;
        case "p":
            d += '一般形(七対国士を含まない)の計算結果 / &lt;a href="?q' + a.substr(1) + "=" + g + '"&gt;標準形&lt;/a&gt;&lt;br&gt;'
    }
    for (var c = "d" == a.substr(1, 1), a = a.substr(0, 1), g = g.replace(/(\d)(\d{0,8})(\d{0,8})(\d{0,8})(\d{0,8})(\d{0,8})(\d{0,8})(\d{8})(m|p|s|z)/g, "$1$9$2$9$3$9$4$9$5$9$6$9$7$9$8$9").replace(/(\d?)(\d?)(\d?)(\d?)(\d?)(\d?)(\d)(\d)(m|p|s|z)/g, "$1$9$2$9$3$9$4$9$5$9$6$9$7$9$8$9").replace(/(m|p|s|z)(m|p|s|z)+/g, "$1").replace(/^[^\d]/, ""), g = g.substr(0, 28), f = aa(g), r = -1; r = Math.floor(136 * Math.random()), f[r];) ;
    var m = Math.floor(g.length / 2) % 3;
    2 == m || c || (f[r] = 1, g += H(r));
    var f = ca(f),
        n = "",
        e = G(f, 34),
        n = n + N(e, 28 == g.length),
        n = n + ("(" + Math.floor(g.length / 2) + "枚)");
    -1 == e[0] &amp;&amp; (n += ' / &lt;a href="?" &gt;新しい手牌を作成&lt;/a&gt;');
    var n = n + "&lt;br/&gt;",
        q = "q" == a ? e[0] : e[1],
        k,
        p,
        l = Array(35);
    if (0 == q &amp;&amp; 1 == m &amp;&amp; c) k = 34,
        l[k] = K(f),
    l[k].length &amp;&amp; (l[k] = {
        i: k,
        n: b(l[k], f),
        c: l[k]
    });
    else if (0 &gt;= q) for (k = 0; 34 &gt; k; ++k) f[k] &amp;&amp; (f[k]--, l[k] = K(f), f[k]++, l[k].length &amp;&amp; (l[k] = {
        i: k,
        n: b(l[k], f),
        c: l[k]
    }));
    else if (2 == m || 1 == m &amp;&amp; !c) for (k = 0; 34 &gt; k; ++k) {
        if (f[k]) {
            f[k]--;
            l[k] = [];
            for (p = 0; 34 &gt; p; ++p) k == p || 4 &lt;= f[p] || (f[p]++, F(f, "p" == a) == q - 1 &amp;&amp; l[k].push(p), f[p]--);
            f[k]++;
            l[k].length &amp;&amp; (l[k] = {
                i: k,
                n: b(l[k], f),
                c: l[k]
            })
        }
    } else {
        k = 34;
        l[k] = [];
        for (p = 0; 34 &gt; p; ++p) 4 &lt;= f[p] || (f[p]++, F(f, "p" == a) == q - 1 &amp;&amp; l[k].push(p), f[p]--);
        l[k].length &amp;&amp; (l[k] = {
            i: k,
            n: b(l[k], f),
            c: l[k]
        })
    }
    var t = [];
    for (k = 0; k &lt; g.length; k += 2) {
        p = g.substr(k, 2);
        var v = ba(p),
            h = J(g.replace(p, "").replace(/(\d)(m|p|s|z)/g, "$2$1$1,").replace(/00/g, "50").split(",").sort().join("").replace(/(m|p|s|z)\d(\d)/g, "$2$1")),
            R = q + 1,
            I = l[v];
        I &amp;&amp; I.n &amp;&amp; (R = -1 == q ? 0 : q, void 0 == I.q &amp;&amp; t.push(I), I.q = h);
        2 == m &amp;&amp; (h += H(r));
        n += (2 == m || 2 != m &amp;&amp; !c ? da : L)(p, 2 == k % 3 &amp;&amp; k == g.length - 2 ? " hspace=3 " : "", a, h, v, R)
    }
    l[34] &amp;&amp; l[34].n &amp;&amp; (l[34].q = J(g), t.push(l[34]), n += '&lt;br&gt;&lt;br&gt;&lt;a href="?' + a + "=" + l[34].q + '"&gt;次のツモをランダムに追加&lt;/a&gt;');
    t.sort(function (a, b) {
        return b.n - a.n
    });
    // g = "" + (document.f.q.value + "\n");
    g = "" + (O + "\n");
    d += "&lt;table cellpadding=2 cellspacing=0 &gt;";
    q = 0 &gt;= q ? "待ち" : "摸";
    for (k = 0; k &lt; t.length; ++k) {
        v = t[k].i;
        d += "&lt;tr id=mda" + v + " &gt;&lt;td&gt;";
        34 &gt; v &amp;&amp; (d += "打&lt;/td&gt;&lt;td&gt;" + ('&lt;img src="https://cdn.tenhou.net/2/a/' + H(4 * v + 1) + '.gif" class=D /&gt;') + "&lt;/td&gt;&lt;td&gt;", g += "打" + H(4 * v + 1) + " ");
        d += q + "[&lt;/td&gt;&lt;td&gt;";
        g += q + "[";
        l = t[k].c;
        c = t[k].q;
        for (p = 0; p &lt; l.length; ++p) r = H(4 * l[p] + 1),
            d += '&lt;a href="?' + a + "=" + (c + r) + '" class=D οnmοuseοver="daFocus(this,' + v + ');" οnmοuseοut="daUnfocus();"&gt;&lt;img src="https://cdn.tenhou.net/2/a/' + r + '.gif" border=0 /&gt;&lt;/a&gt;',
            g += H(4 * l[p] + 1);
        d += "&lt;/td&gt;&lt;td&gt;" + t[k].n + "枚&lt;/td&gt;&lt;td&gt;]&lt;/td&gt;&lt;/tr&gt;";
        g += " " + t[k].n + "枚]\n"
    }
    d = d + "&lt;/table&gt;&lt;br&gt;&lt;hr&gt;&lt;br&gt;" + ('&lt;textarea rows=10 style="width:100%;font-size:75%;"&gt;' + g + "&lt;/textarea&gt;");
    -1 == e[0] &amp;&amp; (d = d + "&lt;hr size=1 color=#CCCCCC &gt;" + ea(f));
    // document.getElementById("tehai").innerHTML = n;
    // document.getElementById("tips").innerHTML = "";
    // document.getElementById("m2").innerHTML = d + "&lt;br&gt;"
    return g
}

// 测试样例
// console.log(fa('336m237p2479s167z3s'))

```

#### Python 代码

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import execjs


url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'


def main():
    q = url.split('=')[1]
    with open('decrypt.js', 'r', encoding='utf-8') as f:
        decrypt_js = f.read()
    data = execjs.compile(decrypt_js).call('fa', q)
    print(data)


if __name__ == '__main__':
    main()

```
