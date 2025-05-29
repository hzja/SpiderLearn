# 原创
：  【JS逆向百例】cebupacificair 航空逆向分析

# 【JS逆向百例】cebupacificair 航空逆向分析

### 前言

近期在知识星球中，有位星友在逆向一个航司的时候，遇到了点阻碍，向我提问，本期就对该网站进行逆向分析：

### 逆向目标

目标：cebupacificair 航空查询逆向分析

网站：`aHR0cHM6Ly93d3cuY2VidXBhY2lmaWNhaXIuY29tL2VuLVBILw==`

### 抓包分析

打开网站，找到返回机票信息的机票查询接口 `ceb-omnix_proxy`：

目测，有这四个参数需要分析，分析之前先搜索，免得是接口返回，发现 `Authorization` 和 `X-Auth-Token` 是另外一个 `ceb-omnix_proxy` 接口返回的：

该接口有四个参数需要分析，也是有两个 `content`，估计都大差不差，我们继续先搜索，发现 `authorization` 是 `main.xxx.js` 文件返回的：

而 `main.xxx.js` 文件是通过首页加载的，大致流程都梳理清晰了，我们开始进行逆向分析：

### 逆向分析

#### cookie 值

从头开始，我们请求首页，发现他并没有返回 `main.xxx.js` 文件，而是返回的下图内容：

发现里面的 JavaScript 代码就是设置了两个 cookie 值，而且仔细就看会发现，它首页接口请求了两次：

请求 cookie 里面就有设置的两个 cookie 值，所以我们照着来操作就可以：

```
__eccha_str = re.findall(r'var val = (.*?);', response.text)[0]
__ecbmchid = re.findall(r'__ecbmchid=(.*?)\"', response.text)[0]
__eccha = execjs.eval(__eccha_str)

cookies = {
    '__eccha':str(__eccha),
    '__ecbmchid': __ecbmchid
}

```

我们需要逆向分析的参数，就是两个 `ceb-omnix_proxy` 接口的两个 `content`，分布在请求头和请求参数中。

可以通过搜索 `ceb-omnix_proxy` 或者 `content:` 就能定位到生成位置，也可以通过下 xhr 断点或者 hook 等手段来跟值，本文都会提到。

#### 第一个 ceb-omnix_proxy 接口

第一个 `ceb-omnix_proxy` 接口我们用 xhr 断点来跟：

清空缓存，刷新网站，跟到第一次进入 `main.xxx.js` 文件的位置，发现 e 变量中已经生成了 `content `值：

重新在 handle 下的位置上打下断点，继续往上跟：

发现 m 由 i 生成，我们继续重新打下断点，清空缓存，刷新网页：

定位到 t 为 `ceb-omnix_proxy` 接口，继续往上跟：

就找到生成位置了：

然后开始逆向分析，过程非常清晰，`uniqueId` 由 ` window.crypto.randomUUID()` 生成，Us 是由 `main.xxx.js` 文件返回，通过搜索就可以找到。`message` 是标准的 `HmacSHA256` 算法加密生成，很容易就可以确认，重点就是两个 `content` 值的生成，都是同一个加密，跟进去发现是 AES，但是跟标准的 AES 有区别：

#### 第二个 ceb-omnix_proxy 接口

先不急，我们再来看第二个 `ceb-omnix_proxy` 接口，我们换个方式来跟，通过 `hook headers`：

```
(function () {
    var _setRequestHeader = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == 'content') {
            debugger;
        }
        return _setRequestHeader.apply(this, arguments);
    };
})();

```

点到 `main.xxx.js` 文件中，发现 e 变量中已经生成了 `content` 值：

我们重新下断点，继续跟：

跟到第二个 `intercept` 就发现参数 e 值中已经没有生成 `content` 值了，大概生成逻辑就在下面。

我们也能发现相关参数确实就是在下面生成的，找到位置重新打断点，进行分析：

后面的过程，也非常清晰，重点同样是 `content` 值的加密生成，这里是由 `this.cryptoService.eContent ` 函数加密生成的，跟进去后发现和第一个 `ceb-omnix_proxy` 接口的 `content` 值的加密函数一致：

重点是 `Is.AES.encrypt` 函数，可以发现 `var Is = ce(7206);`，进入 `ce` 后发现又是 `webpack`。

不过跟我们平常扣的 `webpack `又有点区别：

可以看到他的所有模块都是走的同一个函数，其实就是做的一个闭包：

跟进 `qa` 这个函数，就会发现 `D` 就是调用的模块函数：

流程搞清楚了，就好分析了，两种方式：
1. 手动扣 `webpack`：
可以只把 `main.xxx.js` 文件中的所有模块复制下来，经过测试，没问题：

或者一个个扣，缺啥补啥，都是可以的。
1. 自动扣 `webpack`：
跟以往不同，不过人是活的，既然我们知道 `D` 就是调用的模块函数，而且有属性 `name`，那还是跟之前一样的方法，只不过位置不同，在 `qa` 里添加一行代码，然后替换这个文件：

先断到 `var Is = ce(7206);` 处，控制台输入 `window.code = '';`，然后断到 `return Is.AES.encrypt(e, t).toString();` 的位置上结束，最后在控制台输入 `copy(window.code)`，这样就获得了需要的所有模块：

```
self = global;

var kkk;

!function (v) {
    var e,
    p = {};
  function n(e) {
    var a = p[e];
    if (void 0 !== a) return a.exports;
    var r = p[e] = {
      exports: {}
    };
    console.log(e)
    return v[e].call(r.exports, r, r.exports, n), r.exports;
  }
  n.m = v, e = [], n.O = (a, r, c, f) =&gt; {
    if (!r) {
      var u = 1 / 0;
      for (t = 0; t &lt; e.length; t++) {
        for (var [r, c, f] = e[t], s = !0, l = 0; l &lt; r.length; l++) (!1 &amp; f || u &gt;= f) &amp;&amp; Object.keys(n.O).every(h =&gt; n.O[h](r[l])) ? r.splice(l--, 1) : (s = !1, f &lt; u &amp;&amp; (u = f));
        if (s) {
          e.splice(t--, 1);
          var o = c();
          void 0 !== o &amp;&amp; (a = o);
        }
      }
      return a;
    }
    f = f || 0;
    for (var t = e.length; t &gt; 0 &amp;&amp; e[t - 1][2] &gt; f; t--) e[t] = e[t - 1];
    e[t] = [r, c, f];
  }, n.n = e =&gt; {
    var a = e &amp;&amp; e.__esModule ? () =&gt; e.default : () =&gt; e;
    return n.d(a, {
      a
    }), a;
  }, n.d = (e, a) =&gt; {
    for (var r in a) n.o(a, r) &amp;&amp; !n.o(e, r) &amp;&amp; Object.defineProperty(e, r, {
      enumerable: !0,
      get: a[r]
    });
  }, n.o = (e, a) =&gt; Object.prototype.hasOwnProperty.call(e, a), (() =&gt; {
    var e = {
      666: 0
    };
    n.O.j = c =&gt; 0 === e[c];
    var a = (c, f) =&gt; {
        var l,
          o,
          [t, u, s] = f,
          _ = 0;
        if (t.some(d =&gt; 0 !== e[d])) {
          for (l in u) n.o(u, l) &amp;&amp; (n.m[l] = u[l]);
          if (s) var b = s(n);
        }
        for (c &amp;&amp; c(f); _ &lt; t.length; _++) n.o(e, o = t[_]) &amp;&amp; e[o] &amp;&amp; e[o][0](), e[o] = 0;
        return n.O(b);
      },
      r = self.webpackChunkOMNIX_Project_EN = self.webpackChunkOMNIX_Project_EN || [];
    r.forEach(a.bind(null, 0)), r.push = a.bind(null, r.push.bind(r));
  })();
  kkk = n;
}({
   // 复制需要的所有模块
});

ha = kkk(7206);

function encrypt(e, t){
    return ha.AES.encrypt(e, t).toString()
};

```

剩下的明文就比较简单了，基本都是前面接口返回的东西，就不带着分析了。

**注意点** ： 最后两个 `ceb-omnix_proxy` 接口不要使用指纹库去请求，可能会被风控。

学习代码，可于知识星球中领取，仅供参考。

### 结果验证
