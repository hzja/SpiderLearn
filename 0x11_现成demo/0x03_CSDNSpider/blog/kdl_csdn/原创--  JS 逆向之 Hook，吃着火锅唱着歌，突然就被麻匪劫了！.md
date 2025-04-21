# 原创
：  JS 逆向之 Hook，吃着火锅唱着歌，突然就被麻匪劫了！

# JS 逆向之 Hook，吃着火锅唱着歌，突然就被麻匪劫了！

> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


#### 文章目录

---


### 什么是 Hook？

Hook 中文译为钩子，Hook 实际上是 Windows 中提供的一种用以替换 DOS 下“中断”的系统机制，Hook 的概念在 Windows 桌面软件开发很常见，特别是各种事件触发的机制，在对特定的系统事件进行 Hook 后，一旦发生已 Hook 事件，对该事件进行 Hook 的程序就会收到系统的通知，这时程序就能在第一时间对该事件做出响应。在程序中将其理解为“劫持”可能会更好理解，我们可以通过 Hook 技术来劫持某个对象，把某个对象的程序拉出来替换成我们自己改写的代码片段，修改参数或替换返回值，从而控制它与其他对象的交互。

通俗来讲，Hook 其实就是拦路打劫，马邦德带着老婆，出了城，吃着火锅，还唱着歌，突然就被麻匪劫了，张麻子劫下县长马邦德的火车，摇身一变化身县长，带着手下赶赴鹅城上任。Hook 的过程，就是张麻子顶替马邦德的过程。

---


### JS 逆向中的 Hook

在 JavaScript 逆向中，替换原函数的过程都可以被称为 Hook，以下先用一段简单的代码理解 Hook 的过程：

```
function a() {
  console.log("I'm a.");
}

a = function b() {
  console.log("I'm b.");
};

a()  // I'm b.

```

直接覆盖原函数是最简单的做法，以上代码将 a 函数进行了重写，再次调用 a 函数将会输出 `I'm b.`，如果还想执行原来 `a` 函数的内容，可以使用中间变量进行储存：

```
function a() {
  console.log("I'm a.");
}

var c = a;

a = function b() {
  console.log("I'm b.");
};

a()  // I'm b.
c()  // I'm a.

```

此时，调用 a 函数会输出 `I'm b.`，调用 c 函数会输出 `I'm a.`。

这种原函数直接覆盖的方法通常只用来进行临时调试，实用性不大，但是它能够帮助我们理解 Hook 的过程，在实际 JS 逆向过程中，我们会用到更加高级一点的方法，比如 `Object.defineProperty()`。

---


### Object.defineProperty()

基本语法：`Object.defineProperty(obj, prop, descriptor)`，它的作用就是直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，接收的三个参数含义如下：

`obj`：需要定义属性的当前对象；

`prop`：当前需要定义的属性名；

`descriptor`：属性描述符，可以取以下值：

<th align="left">属性名</th><th align="left">默认值</th><th align="left">含义</th>
|------
<td align="left">get</td><td align="left">undefined</td><td align="left">存取描述符，目标属性获取值的方法</td>
<td align="left">set</td><td align="left">undefined</td><td align="left">存取描述符，目标属性设置值的方法</td>
<td align="left">value</td><td align="left">undefined</td><td align="left">数据描述符，设置属性的值</td>
<td align="left">writable</td><td align="left">false</td><td align="left">数据描述符，目标属性的值是否可以被重写</td>
<td align="left">enumerable</td><td align="left">false</td><td align="left">目标属性是否可以被枚举</td>
<td align="left">configurable</td><td align="left">false</td><td align="left">目标属性是否可以被删除或是否可以再次修改特性</td>

通常情况下，对象的定义与赋值是这样的：

```
var people = {}
people.name = "Bob"
people["age"] = "18"

console.log(people)
// { name: 'Bob', age: '18' }

```

使用 `Object.defineProperty()` 方法：

```
var people = {}

Object.defineProperty(people, 'name', {
   value: 'Bob',
   writable: true  // 是否可以被重写
})

console.log(people.name)  // 'Bob'

people.name = "Tom"
console.log(people.name)  // 'Tom'

```

在 Hook 中，使用最多的是存取描述符，即 get 和 set。

get：属性的 getter 函数，如果没有 getter，则为 undefined，当访问该属性时，会调用此函数，执行时不传入任何参数，但是会传入 this 对象（由于继承关系，这里的 this 并不一定是定义该属性的对象），该函数的返回值会被用作属性的值。

set：属性的 setter 函数，如果没有 setter，则为 undefined，当属性值被修改时，会调用此函数，该方法接受一个参数，也就是被赋予的新值，会传入赋值时的 this 对象。

用一个例子来演示：

```
var people = {
  name: 'Bob',
};
var count = 18;

// 定义一个 age 获取值时返回定义好的变量 count
Object.defineProperty(people, 'age', {
  get: function () {
    console.log('获取值！');
    return count;
  },
  set: function (val) {
    console.log('设置值！');
    count = val + 1;
  },
});

console.log(people.age);
people.age = 20;
console.log(people.age);

```

输出：

```
获取值！
18
设置值！
获取值！
21

```

通过这样的方法，我们就可以在设置某个值的时候，添加一些代码，比如 `debugger;`，让其断下，然后利用调用栈进行调试，找到参数加密、或者参数生成的地方，需要注意的是，网站加载时首先要运行我们的 Hook 代码，再运行网站自己的代码，才能够成功断下，这个过程我们可以称之为 Hook 代码的注入，以下将介绍几种主流的注入方法。

---


### Hook 注入的几种方法

以下以某奇艺 cookie 中的 `__dfp` 值为例，来演示具体如何注入 Hook。

#### 1、Fiddler 插件注入

来到某奇艺首页，可以看到其 cookie 里面有个 `__dfp` 值：

如果直接搜索是搜不到的，我们想通过 Hook 的方式，让在生成 `__dfp` 值的地方断下，就可以编写如下自执行函数：

```
(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('__dfp') != -1) {
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

`if (val.indexOf('__dfp') != -1) {debugger;}` 的意思是检索 `__dfp` 在字符串中首次出现的位置，等于 -1 表示这个字符串值没有出现，反之则出现。如果出现了，那么就 debugger 断下，这里要注意的是不能写成 `if (val == '__dfp') {debugger}`，因为 val 传过来的值类似于 `__dfp=xxxxxxxxxx`，这样写是无法断下的。

有了代码该如何使用呢？也就是怎么注入 Hook 代码呢？这里推荐 Fiddler 抓包工具搭配编程猫的插件使用，插件可以在公众号输入关键字【**Fiddler插件**】获取，其原理可以理解为拦截 —&gt; 加工 —&gt; 放行的一个过程，利用 Fiddler 替换响应，在 Fiddler 拦截到数据后，在源码第一行插入 Hook 代码，由于 Hook 代码是一个自执行函数，那么网页一旦加载，就必然会先运行 Hook 代码。安装完成后如下图所示，打开抓包，点击开启注入 Hook：

浏览器清除 cookie 后重新进入某奇艺的页面，可以看到成功断下，在 console 控制台可以看到捕获的一些 cookie 值，此时的 `val` 就是 `__dfp` 的值，接下来在右侧的 Call Stack 调用栈里就可以看到一些函数的调用过程，依次向上跟进就能够找到最开始 `__dfp` 生成的地方。

#### 2、TamperMonkey 注入

TamperMonkey 俗称油猴插件，是一款免费的浏览器扩展和最为流行的用户脚本管理器，支持很多主流的浏览器， 包括 Chrome、Microsoft Edge、Safari、Opera、Firefox、UC 浏览器、360 浏览器、QQ 浏览器等等，基本上实现了脚本的一次编写，所有平台都能运行，可以说是基于浏览器的应用算是真正的跨平台了。用户可以在 GreasyFork、OpenUserJS 等平台直接获取别人发布的脚本，功能众多且强大，比如视频解析、去广告等。

我们依旧以某奇艺的 cookie 为例来演示如何编写 TamperMonkey 脚本，首先去应用商店安装 TamperMonkey，安装过程不再赘述，然后点击图标，添加新脚本，或者点击管理面板，再点击加号新建脚本，写入以下代码：

```
// ==UserScript==
// @name         Cookie Hook
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Cookie Hook 脚本示例
// @author       K哥爬虫
// @match        *
// @icon         https://www.kuaidaili.com/img/favicon.ico
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('__dfp') != -1) {
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

主体的 JavaScript 自执行函数和前面都是一样的，这里需要注意的是最前面的注释，每个选项都是有意义的，所有的选项参考 [TamperMonkey 官方文档](https://www.tampermonkey.net/documentation.php)，以下列出了比较常用、比较重要的部分选项（其中需要特别注意 `@match`、`@include` 和 `@run-at` 选项）：

|选项|含义
|------
|@name|脚本的名称
|@namespace|命名空间，用来区分相同名称的脚本，一般写作者名字或者网址就可以
|@version|脚本版本，油猴脚本的更新会读取这个版本号
|@description|描述这个脚本是干什么用的
|@author|编写这个脚本的作者的名字
|`@match`|从字符串的起始位置匹配正则表达式，只有匹配的网址才会执行对应的脚本，例如 `*` 匹配所有，`https://www.baidu.com/*` 匹配百度等，可以参考 Python re 模块里面的 `re.match()` 方法，允许多个实例
|`@include`|和 @match 类似，只有匹配的网址才会执行对应的脚本，但是 @include 不会从字符串起始位置匹配，例如 `*://*baidu.com/*` 匹配百度，具体区别可以参考 [TamperMonkey 官方文档](https://www.tampermonkey.net/documentation.php)
|@icon|脚本的 icon 图标
|@grant|指定脚本运行所需权限，如果脚本拥有相应的权限，就可以调用油猴扩展提供的 API 与浏览器进行交互。如果设置为 none 的话，则不使用沙箱环境，脚本会直接运行在网页的环境中，这时候无法使用大部分油猴扩展的 API。如果不指定的话，油猴会默认添加几个最常用的 API
|@require|如果脚本依赖其他 JS 库的话，可以使用 require 指令导入，在运行脚本之前先加载其它库
|`@run-at`|脚本注入时机，该选项是能不能 hook 到的关键，有五个值可选：`document-start`：网页开始时；`document-body`：body出现时；`document-end`：载入时或者之后执行；`document-idle`：载入完成后执行，默认选项；`context-menu`：在浏览器上下文菜单中单击该脚本时，一般将其设置为 `document-start`

清除 cookie，开启 TamperMonkey 插件，再次来到某奇艺首页，可以看到也成功被断下，同样的也可以跟进调用栈来进一步分析 `__dfp` 值的来源。

#### 3、浏览器插件注入

浏览器插件官方叫法应该是浏览器扩展（Extension），浏览器插件能够增强浏览器功能，同样也能够帮助我们 Hook，浏览器插件的编写并不复杂，以 Chrome 插件为例，只需要保证项目下有一个 manifest.json 文件即可，它用来设置所有和插件相关的配置，必须放在根目录。其中 `manifest_version`、`name`、`version` 3个参数是必不可少的，如果想要深入学习，可以参考[小茗同学](https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html)的博客和 [Google 官方文档](https://developer.chrome.com/docs/extensions/)。需要注意的是，火狐浏览器插件不一定能在其他浏览器上运行，而 Chrome 插件除了能运行在 Chrome 浏览器之外，还可以运行在所有 webkit 内核的国产浏览器，比如 360 极速浏览器、360 安全浏览器、搜狗浏览器、QQ 浏览器等等。我们还是以某奇艺的 cookie 来演示如何编写一个 Chrome 浏览器 Hook 插件。

新建 manifest.json 文件：

```
{
    "name": "Cookie Hook",          // 插件名称
    "version": "1.0",               // 插件版本
    "description": "Cookie Hook",   // 插件描述
    "manifest_version": 2,          // 清单版本，必须是2或者3
    "content_scripts": [{
        "matches": ["&lt;all_urls&gt;"],  // 匹配所有地址
        "js": ["cookie_hook.js"],   // 注入的代码文件名和路径，如果有多个，则依次注入
        "all_frames": true,         // 允许将内容脚本嵌入页面的所有框架中
        "permissions": ["tabs"],    // 权限申请，tabs 表示标签
        "run_at": "document_start"  // 代码注入的时间
    }]
}

```

新建 cookie_hook.js 文件：

```
var hook = function() {
    'use strict';
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function(val) {
            if (val.indexOf('__dfp') != -1) {
                debugger;
            }
            console.log('Hook捕获到cookie设置-&gt;', val);
            cookieTemp = val;
            return val;
        },
        get: function() {
            return cookieTemp;
        },
    });
}
var script = document.createElement('script');
script.textContent = '(' + hook + ')()';
(document.head || document.documentElement).appendChild(script);
script.parentNode.removeChild(script);

```

将这两个文件放到同一个文件夹，打开 chrome 的扩展程序, 打开开发者模式，加载已解压的扩展程序，选择创建的文件夹即可：

来到某奇艺页面，清除 cookie 后重新进入，可以看到同样也成功断下，跟踪调用栈就可以找到其值生成的地方：

---


### 常用 Hook 代码总汇

除了使用上述的 `Object.defineProperty()` 方法，还可以直接捕获相关接口，然后重写这个接口，以下列出了常见的 Hook 代码。注意：以下只是关键的 Hook 代码，具体注入的方式不同，要进行相关的修改。

#### Hook Cookie

Cookie Hook 用于定位 Cookie 中关键参数生成位置，以下代码演示了当 Cookie 中匹配到了 `__dfp` 关键字， 则插入断点：

```
(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('__dfp') != -1) {
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

```
(function () {
    'use strict';
    var org = document.cookie.__lookupSetter__('cookie');
    document.__defineSetter__('cookie', function (cookie) {
        if (cookie.indexOf('__dfp') != -1) {
            debugger;
        }
        org = cookie;
    });
    document.__defineGetter__('cookie', function () {
        return org;
    });
})();

```

#### Hook Header

Header Hook 用于定位 Header 中关键参数生成位置，以下代码演示了当 Header 中包含 `Authorization` 关键字时，则插入断点：

```
(function () {
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == 'Authorization') {
            debugger;
        }
        return org.apply(this, arguments);
    };
})();

```

#### Hook URL

URL Hook 用于定位请求 URL 中关键参数生成位置，以下代码演示了当请求的 URL 里包含 `login` 关键字时，则插入断点：

```
(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("login") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();

```

#### Hook JSON.stringify

`JSON.stringify()` 方法用于将 JavaScript 值转换为 JSON 字符串，在某些站点的加密过程中可能会遇到，以下代码演示了遇到 `JSON.stringify()` 时，则插入断点：

```
(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(params) {
        console.log("Hook JSON.stringify ——&gt; ", params);
        debugger;
        return stringify(params);
    }
})();

```

#### Hook JSON.parse

`JSON.parse()` 方法用于将一个 JSON 字符串转换为对象，在某些站点的加密过程中可能会遇到，以下代码演示了遇到 `JSON.parse()` 时，则插入断点：

```
(function() {
    var parse = JSON.parse;
    JSON.parse = function(params) {
        console.log("Hook JSON.parse ——&gt; ", params);
        debugger;
        return parse(params);
    }
})();

```

#### Hook eval

JavaScript `eval()` 函数的作用是计算 JavaScript 字符串，并把它作为脚本代码来执行。如果参数是一个表达式，`eval()` 函数将执行表达式。如果参数是 Javascript 语句，`eval()` 将执行 Javascript 语句，经常被用来动态执行 JS。以下代码执行后，之后所有的 `eval()` 操作都会在控制台打印输出将要执行的 JS 源码：

```
(function() {
    // 保存原始方法
    window.__cr_eval = window.eval;
    // 重写 eval
    var myeval = function(src) {
        console.log(src);
        console.log("=============== eval end ===============");
        debugger;
        return window.__cr_eval(src);
    }
    // 屏蔽 JS 中对原生函数 native 属性的检测
    var _myeval = myeval.bind(null);
    _myeval.toString = window.__cr_eval.toString;
    Object.defineProperty(window, 'eval', {
        value: _myeval
    });
})();

```

#### Hook Function

以下代码执行后，所有的函数操作都会在控制台打印输出将要执行的 JS 源码：

```
(function() {
    // 保存原始方法
    window.__cr_fun = window.Function;
    // 重写 function
    var myfun = function() {
        var args = Array.prototype.slice.call(arguments, 0, -1).join(","),
            src = arguments[arguments.length - 1];
        console.log(src);
        console.log("=============== Function end ===============");
        debugger;
        return window.__cr_fun.apply(this, arguments);
    }
    // 屏蔽js中对原生函数native属性的检测
    myfun.toString = function() {
        return window.__cr_fun + ""
    }
    Object.defineProperty(window, 'Function', {
        value: myfun
    });
})();

```
