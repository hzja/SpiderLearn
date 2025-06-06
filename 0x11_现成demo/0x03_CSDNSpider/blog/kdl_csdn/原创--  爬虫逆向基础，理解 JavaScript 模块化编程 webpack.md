# 原创
：  爬虫逆向基础，理解 JavaScript 模块化编程 webpack

# 爬虫逆向基础，理解 JavaScript 模块化编程 webpack

> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


---


### 简介

在分析一些站点的 JavaScript 代码时，比较简单的代码，函数通常都是一个一个的，例如：

```
function a() {console.log("a")}
function b() {console.log("a")}
function c() {console.log("a")}

```

但是稍微复杂一点的站点，通常会遇到类似如下的代码结构：

```
!function(i) {
    function n(t) {
        return i[t].call(a, b, c, d)
    }
}([
    function(t, e) {}, 
    function(t, e, n) {}, 
    function(t, e, r) {}, 
    function(t, e, o) {}
]);

```

这种写法在 JavaScript 中很常见，对于熟悉 JavaScript 的人来说可能非常简单，但是爬虫工程师大多数都是用 Python 或者 Java 来写代码的，看到这种语法就有可能懵了，由于在剥离 JS 加密代码时会经常遇到，所以理解这种语法对于爬虫工程师来说是非常重要的。

这种写法貌似没有官方的名称，相当于进行了模块化编程，因此大多数人称其为 webpack，上面的示例看起来比较费劲，简单优化一下：

```
!function (allModule) {
    function useModule(whichModule) {
        allModule[whichModule].call(null, "hello world!");
    }
    useModule(0)
}([
    function module0(param) {console.log("module0: " + param)},
    function module1(param) {console.log("module1: " + param)},
    function module2(param) {console.log("module2: " + param)},
]);

```

运行以上代码，会输出 `module0: hello world!`，相信通过浅显易懂的变量名和函数名，应该就可以看懂大致含义了，调用 `useModule(0)`，从所有函数里选择第一个，将 `hello world!` 传递给 `module0` 并输出。

仔细观察以上代码，我们会发现主要用到了 `!function(){}()` 和 `function.call()` 语法，接下来就一一介绍一下。

---


### 函数声明与函数表达式

在 ECMAScript（JavaScript 的一个标准）中，有两个最常用的创建函数对象的方法，即使用函数声明或者函数表达式，ECMAScript 规范明确了一点，即函数声明必须始终带有一个标识符，也就是我们所说的函数名，而函数表达式则可以省略。

函数声明，会给函数指定一个名字，会在代码执行以前被加载到作用域中，所以**调用函数在函数声明之前或之后都是可以的**：

```
test("Hello World!")

function test(arg) {
    console.log(arg)
}

```

函数表达式，创建一个匿名函数，然后将这个匿名函数赋给一个变量，在代码执行到函数表达式的时候才会有定义，所以**调用函数在函数表达式之后才能正确运行**，否则是会报错的：

```
var test = function (arg) {
    console.log(arg)
}

test("Hello World!")

```

---


### IIFE 立即调用函数表达式

IIFE 全称 Immediately-invoked Function Expressions，译为立即调用函数表达式，也称为自执行函数、立即执行函数、自执行匿名函数等，IIFE 是一种语法，这种模式本质上就是函数表达式（命名的或者匿名的）在创建后立即执行。当函数变成立即执行的函数表达式时，表达式中的变量不能从外部访问。IIFE 主要用来隔离作用域，避免污染。

---


#### IIFE 基本语法

IIFE 的写法非常灵活，主要有以下几种格式：

1、匿名函数前面加上一元操作符，后面加上 `()`：

```
!function () {
    console.log("I AM IIFE")
}();

-function () {
    console.log("I AM IIFE")
}();

+function () {
    console.log("I AM IIFE")
}();

~function () {
    console.log("I AM IIFE")
}();

```

2、匿名函数后面加上 `()`，然后再用 `()` 将整个括起来：

```
(function () {
    console.log("I AM IIFE")
}());

```

3、先用 `()` 将匿名函数括起来，再在后面加上 `()`：

```
(function () {
    console.log("I AM IIFE")
})();

```

4、使用箭头函数表达式，先用 `()` 将箭头函数表达式括起来，再在后面加上 `()`：

```
(() =&gt; {
  console.log("I AM IIFE")
})()

```

5、匿名函数前面加上 `void` 关键字，后面加上 `()`， `void` 指定要计算或运行一个表达式，但是不返回值：

```
void function () {
    console.log("I AM IIFE")
}();

```

有的时候，我们还有可能见到立即执行函数前面后分号的情况，例如：

```
;(function () {
    console.log("I AM IIFE")
}())

;!function () {
    console.log("I AM IIFE")
}()

```

这是因为立即执行函数通常作为一个单独模块使用一般是没有问题的，但是还是建议在立即执行函数前面或者后面加上分号，这样可以有效地与前面或者后面的代码进行隔离，否则可能出现意想不到的错误。

---


#### IIFE 参数传递

将参数放在末尾的 `()` 里即可实现参数传递：

```
var text = "I AM IIFE";

(function (param) {
    console.log(param)
})(text);

// I AM IIFE

```

```
var dict = {name: "Bob", age: "20"};

(function () {
    console.log(dict.name);
})(dict);

// Bob

```

```
var list = [1, 2, 3, 4, 5];

(function () {
    var sum = 0;
    for (var i = 0; i &lt; list.length; i++) {
        sum += list[i];
    }
    console.log(sum);
})(list);

// 15

```

---


### Function.prototype.call() / apply() / bind()

`Function.prototype.call()`、`Function.prototype.apply()`、`Function.prototype.bind()` 都是比较常用的方法。它们的作用一模一样，即**改变函数中的 `this` 指向**，它们的区别如下：

---


#### call()

`call()` 方法接受多个参数，第一个参数 thisArg 指定了函数体内 this 对象的指向，如果这个函数处于非严格模式下，指定为 null 或 undefined 时会自动替换为指向全局对象（浏览器中就是 window 对象），在严格模式下，函数体内的 this 还是为 null。从第二个参数开始往后，每个参数被依次传入函数，基本语法如下：

```
function.call(thisArg, arg1, arg2, ...)

```

示例：

```
function test(a, b, c) {
    console.log(a + b + c)
}

test.call(null, 1, 2, 3)  // 6

```

```
function test() {
    console.log(this.firstName + " " + this.lastName)
}

var data = {firstName: "John", lastName: "Doe"}
test.call(data)  // John Doe

```

---


#### apply()

`apply()` 方法接受两个参数，第一个参数 thisArg 与 `call()` 方法一致，第二个参数为一个带下标的集合，从 ECMAScript 第5版开始，这个集合可以为数组，也可以为类数组，`apply()` 方法把这个集合中的元素作为参数传递给被调用的函数，基本语法如下：

```
function.apply(thisArg, [arg1, arg2, ...])

```

示例：

```
function test(a, b, c) {
    console.log(a + b + c)
}

test.apply(null, [1, 2, 3])  // 6

```

```
function test() {
    console.log(this.firstName + " " + this.lastName)
}

var data = {firstName: "John", lastName: "Doe"}
test.apply(data)  // John Doe

```

---


#### bind()

`bind()` 方法和 `call()` 接受的参数是相同的，只不过 `bind()` 返回的是一个函数，基本语法如下：

```
function.bind(thisArg, arg1, arg2, ...)

```

示例：

```
function test(a, b, c) {
    console.log(a + b + c)
}

test.bind(null, 1, 2, 3)()  // 6

```

```
function test() {
    console.log(this.firstName + " " + this.lastName)
}

var data = {firstName: "John", lastName: "Doe"}
test.bind(data)()  // John Doe

```

---


### 理解 webpack

有了以上知识后，我们再来理解一下模块化编程，也就是前面所说的 webpack 写法：

```
!function (allModule) {
    function useModule(whichModule) {
        allModule[whichModule].call(null, "hello world!");
    }
    useModule(0)
}([
    function module0(param) {console.log("module0: " + param)},
    function module1(param) {console.log("module1: " + param)},
    function module2(param) {console.log("module2: " + param)},
]);

```

首先，这整个代码是一个 IIFE 立即调用函数表达式，传递的参数是一个数组，里面包含三个方法，分别是 `module0`、`module1` 和 `module2`，可以将其视为三个模块，那么 IIFE 接受的参数 `allModule` 就包含这三个模块，IIFE 里面还包含一个函数 `useModule()`，可以将其视为模块加载器，即要使用哪个模块，示例中 `useModule(0)` 即表示调用第一个模块，函数里面使用 `call()` 方法改变函数中的 `this` 指向并传递参数，调用相应的模块进行输出。

---


### 改写 webpack

对于我们爬虫逆向当中经常遇到的 webpack 模块化的写法，可以很容易对其进行改写，以下以一段加密代码为例：

```
CryptoJS = require("crypto-js")

!function (func) {
    function acvs() {
        var kk = func[1].call(null, 1e3);
        var data = {
            r: "I LOVE PYTHON",
            e: kk,
            i: "62bs819idl00oac2",
            k: "0123456789abcdef"
        }
        return func[0].call(data);
    }

    console.log("加密文本：" + acvs())

    function odsc(account) {
        var cr = false;
        var regExp = /(^\d{7,8}$)|(^0\d{10,12}$)/;
        if (regExp.test(account)) {
            cr = true;
        }
        return cr;
    }

    function mkle(account) {
        var cr = false;
        var regExp = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (regExp.test(account)) {
            cr = true;
        }
        return cr;
    }

}([
    function () {
        for (var n = "", t = 0; t &lt; this.r.length; t++) {
            var o = this.e ^ this.r.charCodeAt(t);
            n += String.fromCharCode(o)
        }
        return encodeURIComponent(n)
    },
    function (x) {
        return Math.ceil(x * Math.random())
    },
    function (e) {
        var a = CryptoJS.MD5(this.k);
        var c = CryptoJS.enc.Utf8.parse(a);
        var d = CryptoJS.AES.encrypt(e, c, {
            iv: this.i
        });
        return d + ""
    },
    function (e) {
        var b = CryptoJS.MD5(this.k);
        var d = CryptoJS.enc.Utf8.parse(b);
        var a = CryptoJS.AES.decrypt(e, d, {
            iv: this.i
        }).toString(CryptoJS.enc.Utf8);
        return a
    }
]);

```

可以看到关键的加密入口函数是 `acvs()`，`acvs()` 里面又调用了 IIFE 参数列表里面的第一个和第二个函数，剩下的其他函数都是干扰项，而第一个函数中用到了 r 和 e 参数，将其直接传入即可，最终改写如下：

```
function a(r, e) {
    for (var n = "", t = 0; t &lt; r.length; t++) {
        var o = e ^ r.charCodeAt(t);
        n += String.fromCharCode(o)
    }
    return encodeURIComponent(n)
}

function b(x) {
    return Math.ceil(x * Math.random())
}

function acvs() {
    var kk = b(1e3);
    var r = "I LOVE PYTHON";
    return a(r, kk);
}

console.log("加密文本：" + acvs())

```

---


### 总结

看完本文后，你可能会觉得 webpack 也不过如此，看起来确实比较简单，但实际上我们在分析具体站点时往往不会像上述例子这么简单，本文旨在让大家简单理解一下模块化编程 webpack 的原理，后续 K 哥将会带领大家实战分析比较复杂的 webpack！敬请关注！
