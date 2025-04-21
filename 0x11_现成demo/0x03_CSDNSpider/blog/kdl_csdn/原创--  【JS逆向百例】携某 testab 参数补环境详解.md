# 原创
：  【JS逆向百例】携某 testab 参数补环境详解

# 【JS逆向百例】携某 testab 参数补环境详解

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近很多粉丝咨询补环境相关的问题，确实，相较于硬刚算法，补环境相对通用、易于实现。不过现在网上很多文章，对于如何补浏览器环境，都说的很模糊，或者直接表示”缺啥补啥“。诚然，补环境的文章确实不好写，但这对于部分人来说，看完还是很蒙圈，如果是小白的话，那就更不友好了。JSVMP 插桩跟算法，公众号和知识星球中都有不少文章，本文将采用补环境的方式解决 JSVMP，并详细分析处理过程。

### 逆向目标

### 参数分析

直接全局搜索 testab 定位：

可以发现是 e 函数生成的，我们向下跟栈，发现是一段 vmp 代码：

接着向前跟栈，点击 `_callee2$`，发现 vmp 是通过 eval 函数执行的：

那也说明，testab 的值就是在 vmp 中生成的，我们把 vmp 代码拿下来放到代码段里面跑：

这段 vmp 代码是动态变化的，由 getHotelScript 接口返回的，我们为了方便调试，这里进行固定：

直接把这个 vmp 代码放到代码段里面跑，会报错 `func.apply is not a function`，我们需要通过 window[‘callback’] 来进行调用，这里面 window[‘callback’] 就是下面这段：

这里给出两种调用方法（推荐第二种）：

```
// 第一种
var code = `放入 vmp 代码`
function decode(callback) {
    window[callback] = function(e) {
        delete window[callback];
        var e = e()
        testab = e;
        return e;
    }
    window.eval(code);
    return testab
}
decode("KLBNxcMKmI")

// 第二种
function decode(callback) {
    window[callback] = function(e) {
        delete window[callback];
        var e = e()
        testab = e;
        return e;
    }
    // 这里直接放入 vmp 代码
    
    return testab
}
decode("KLBNxcMKmI")

```

代码段创建好后，打印输出，结果为：

```
'be727422b2c51e6f62fe934f20e023bd39667628c0c4a143fc24c9a9564db142'

```

我们只需要在 node 中也成功打印出这个结果就 OK 了，话不多说，开始补环境。

### jsvmp 插桩辅助补环境

对于补 jsvmp，不要一上来就挂代理补环境，我们应该先大致看看 vmp 代码怎样操作的浏览器环境。

相关 vmp 知识就不介绍了，网上有很多，自行查阅。因为我们是辅助补环境，我们可以在指令为函数调用的地方下断点：

我这里输出代码写的很随便，小伙伴们可以根据自己的需求修改，打印部分结果如下。

navigator 自有属性和 external 的 toString() 检测：

document.documentElement 的 getAttribute 检测：

Object.keys 对 document 原型检测：

navigator 属性描述符检测以及 ua 检测：

node process 检测：

Window toString() 检测：

document 检测：

createElement 检测：

appendChild 及报错检测：

vm 以及其它检测：

想输出更多的日志，也可以在加法那里打日志断点，这里就不做分析了：

大致看一下日志后，就可以开始补环境了。

#### testab 补环境

感觉市面上的补环境教程很多都是说缺啥补啥，很难找到一个非常详细的，很多人前面环境没补好，导致走到了错误的分支，一些浏览器对象或者函数被跳过执行了，以至于最后的环境没有补对。

因此这里最开始写的详细一点。

补环境的话，这个网站用 node 或者 vm2 补都可以，都是能得出这个一模一样的结果，这里选择用 vm2 进行补环境方便一点。

第一步，创建好文件，可以创建 3 个文件，分别放入 js 代码，补环境代码和主程序运行代码：

main.js

```
const {VM,VMScript} = require("vm2");
const fs = require('fs');
const vm =new VM()

var code = fs.readFileSync('./env.js')
code += fs.readFileSync('./code.js')
function decode(){
    var res = vm.run(code)
    console.log(res)
    return res
}
decode()

```

env.js

```
//放入环境, 可以先把 toString() 保护代码给拿过来
!(function(){
    "use strict";
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('',')_',(Math.random()+'').toString(36)));
    const mytoString = function(){
        return typeof this == 'function' &amp;&amp; this[myFunction_toString_symbol] || $toString.call(this);
    };
    function set_native(func,key,value){
        Object.defineProperty(func,key,{
            "enumerable" : false,
            "configurable" : true,
            "writable" : true,
            "value" : value
        })
    };
    delete Function.prototype['toString'];
    set_native(Function.prototype,"toString",mytoString);
    set_native(Function.prototype.toString,myFunction_toString_symbol,"function toString() { [native code] }");
    this.func_set_native = function (func)  {
        set_native(func,myFunction_toString_symbol,`function ${myFunction_toString_symbol,func.name || ''}() { [native code] }`)
    }
}).call(this);

window = this;


```

code.js

```
function decode(callback) {
window[callback] = function(e) {
            delete window[callback];
            var e = e()
            testab = e;
            return e;
        };
        // 这里放入自执行函数
}
decode("KLBNxcMKmI")

```

直接运行 main.py 文件，报错：

这个是检测了 self 的属性，另外说一下，很多操作也在 self 里面进行，我们在 env 文件增加如下代码：

```
self = window;
self.window = window;

```

运行，发现没有报错了，得到下面的结果：

但是和我们浏览器的值不一样，这时候挂上代理（这里有坑，下面讲）：

```
function proxy(obj,name){
    return new Proxy(obj,{
        get:function (target, p, receiver) {
            console.table([{'method':'get',target:name,p:p,receiver:receiver,value:Reflect.get(target, p, receiver)}])
            return Reflect.get(target, p, receiver)
        },
        set:function (target, p, value,receiver){
            console.table([{'method':'set',target:name, p:p, value:value, receiver:receiver}])
            return Reflect.set(target, p, value, receiver)
        },
    })
};

window = proxy(window,"window");
self = proxy(self,"self");

```

继续运行（点调式按钮，不要点运行按钮），捕获到了很多，但是不方便看，这时候我们借助浏览器调试：

在配置里面加上 `--inspect-brk`：

然后运行，把下面这些常见的对象都补好：

这里给出补好的代码：

```
Window = function Window(){};
Location = function Location(){};
Navigator = function Navigator(){};
Image = function Image(){
    console.log("Image", arguments)
};
document = {};
navigator = {};
location = {};

```

再次运行，这里可以先不给 document 这几个对象挂代理，我们可以看看 window 还有哪些没补，补好了之后在进行挂代理。

发现多了这些对象：

对比浏览器，我们只需要再补 external 就行了：

发现是对象，我们需要挂上代理，这里可以补上他的 toString()，因为我们上面的日志已经输出了：

（这里顺带一提，只要是函数，可以都加上 toString 保护，以免被检测）

```
external = {};
Object.defineProperty(external,Symbol.toStringTag,{
    value:'External'
})
External = function External(){
    console.log("External",arguments)
};
func_set_native(External)
external.__proto__ = External.prototype;
external = proxy(external,"external")；

```

同时对 document、navigator、location 挂上代理，self 和 window 就不需要挂了，继续运行：

补完这些基本的环境后：

```
Object.setPrototypeOf(navigator,Navigator.prototype);
Navigator.prototype.webdriver = false;
Navigator.prototype.platform = 'Win32'
Navigator.prototype.appCodeName = 'Mozilla'
Navigator.prototype.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

HTMLHtmlElement = function HTMLHtmlElement(){};
document.documentElement = new HTMLHtmlElement();
document.documentElement = proxy(document.documentElement,"documentElement")
HTMLBodyElement = function HTMLBodyElement(){};
document.body = new HTMLBodyElement();
document.body = proxy(document.body,"body");
document.createElement = function createElement(){
    console.log("createElement创建了", arguments);
}

```

注意后面的补环境需要打开浏览器异常断点捕获来辅助补环境：

这里调用了 getAttribute 属性，根据我们上面的 vmp 日志，这里判断了自动化的一些属性，这里我们直接返回 null 就行：

```
HTMLHtmlElement = function HTMLHtmlElement(){
    this.getAttribute = function (){
        return null
    }
};
document.documentElement = new HTMLHtmlElement();
document.documentElement =  proxy(document.documentElement,"documentElement")

```

继续运行，报错，这个不用管，浏览器也会报错：

继续报错 `process is not defined`，这里在检测 node 环境：

一直按 F8 可以看到报错了，`Cannot read properties of undefined (reading 'style')`，同时我们下面捕获到了。

createElement 创建了 div 标签，那就可以推断出创建了 div 标签，然后调用了 style 属性：

代码如下：

```
HTMLDivElement = function HTMLDivElement(){
    this.style = {};
    this.style = proxy(this.style,"this.style");
};
document.createElement = function createElement(){
    console.log("createElement创建了",arguments);
    let tagName = arguments[0]
    if (tagName == "div"){
        var div = new HTMLDivElement();  // 只要是对象，我们就需要挂上代理
        div = proxy(div,"div");
        return div
    }
}

```

继续运行：

补好代码，继续运行：

```
this.style = {
        height:""
    };
this.offsetHeight = 0

```

注意这里是对 offsetHeight 进行检测，至于为什么，我们可以先测试一些。我们可以先把 body 的 appendChild 方法补成空函数，运行：

浏览器模拟实现为：

因此我们要在调用 appendChild 时，offsetHeight 设置为 20：

```
HTMLBodyElement = function HTMLBodyElement(){
    this.appendChild = function (child){
        if (child.tagName=="DIV"){
            child.offsetHeight = 20
        }
    }
};
document.body = new HTMLBodyElement();
document.body = proxy(document.body,"body");
HTMLDivElement = function HTMLDivElement(){
    this.tagName = "DIV"
    this.style = {
        height:""
    };
    this.offsetHeight = 0
    this.style = proxy(this.style,"this.style");
    this.remove = function (){
        this.offsetHeight = 0
    }
};

```

然后中途又创建了 a 标签、p 标签等等，还有检测了 body 下面的 children 的 length 属性这里直接跳到下面这部分：

还是先把 appendChild 补空，测试是否检测了 appendChild，运行代码：

补环境有经验的小伙伴，一看就知道，这里是在进行报错检测，举个例子：

简单模拟一下：

```
this.children = [];
this.parentNode = null;
this.appendChild = function (child){
let ancestor = this;
while (ancestor){
if (ancestor === child){
throw new Error("Failed to execute 'appendChild' on 'Node': The new child element contains the parent.");
}
ancestor = ancestor.parentNode;
}
child.parentNode = this;
this.children.push(child);
    }

```

后面的环境都可以通过这样操作，下面只说重点了。

#### Object 检测相关

Object 代码部分就靠大家自己补了，对照着 vmp 日志肯定能补出来的。

##### freeze

首先是 document 和 navigator 对象设置值，在浏览器中，这些对象是不能重新赋值的，因此需要冻结这些对象：

```
Object.freeze(document)
Object.freeze(navigator)

```

##### getOwnPropertyDescriptor

检测了 navigator 的 webdriver 属性，hook 代码如下：

```
_getOwnPropertyDescriptor = Object.getOwnPropertyDescriptor;
Object.getOwnPropertyDescriptor = function (obj,p){
    // 自己对照浏览器补
    debugger;
    // console.log(arguments)
    return _getOwnPropertyDescriptor.apply(this,arguments)
};

```

##### keys

检测了 document 原型 和 HTMLImageElement：

```
_keys = Object.keys;
Object.keys = function (obj){
    debugger;
    // 自己对照浏览器补
    // console.log(arguments);
    return _keys.apply(this,arguments)
};

```

##### getOwnPropertyNames

检测了 navigator 属性：

```
Object.getOwnPropertyNames = function (obj){
    
    debugger;
    // console.log(arguments);
    return _getOwnPropertyNames.apply(this,arguments)
};

```

#### 正则检测

检测了 vm node：

```
RegExp = new Proxy(RegExp,{

    construct(target, argArray) {
        if (argArray[0] &amp;&amp; argArray[0].indexOf('vm') !== -1)
        {
            // debugger;
            return new target(...['bootstrapNodeJSCoretryModuleLoadevalmachinerunInContext','g'])
        }
        return new target(...argArray)
    }
});

```

把上面补好之后，发现结果还是不对：

#### 代理检测

原因是因为检测了代理，这里有两种解决方法。

##### 第一种

将所有挂的代理都去掉，如果补的不全，可能会导致结果还是不一致。

##### 第二种

选择一个完善的代理，这里是一个开源框架里面的代理：

```
dtavm = {}
dtavm.log = console.log
function proxy(obj, objname, type) {
    function getMethodHandler(WatchName, target_obj) {
        let methodhandler = {
            apply(target, thisArg, argArray) {
                if (this.target_obj) {
                    thisArg = this.target_obj
                }
                let result = Reflect.apply(target, thisArg, argArray)
                if (target.name !== "toString") {
                    if (target.name === "addEventListener") {
                        dtavm.log(`调用者 =&gt; [${WatchName}] 函数名 =&gt; [${target.name}], 传参 =&gt; [${argArray[0]}], 结果 =&gt; [${result}].`)
                    } else if (WatchName === "window.console") {
                    } else {
                        dtavm.log(`调用者 =&gt; [${WatchName}] 函数名 =&gt; [${target.name}], 传参 =&gt; [${argArray}], 结果 =&gt; [${result}].`)
                    }
                } else {
                    dtavm.log(`调用者 =&gt; [${WatchName}] 函数名 =&gt; [${target.name}], 传参 =&gt; [${argArray}], 结果 =&gt; [${result}].`)
                }
                return result
            },
            construct(target, argArray, newTarget) {
                var result = Reflect.construct(target, argArray, newTarget)
                dtavm.log(`调用者 =&gt; [${WatchName}] 构造函数名 =&gt; [${target.name}], 传参 =&gt; [${argArray}], 结果 =&gt; [${(result)}].`)
                return result;
            }
        }
        methodhandler.target_obj = target_obj
        return methodhandler
    }

    function getObjhandler(WatchName) {
        let handler = {
            get(target, propKey, receiver) {
                let result = target[propKey]
                if (result instanceof Object) {
                    if (typeof result === "function") {
                        dtavm.log(`调用者 =&gt; [${WatchName}] 获取属性名 =&gt; [${propKey}] , 是个函数`)
                        return new Proxy(result, getMethodHandler(WatchName, target))
                    } else {
                        dtavm.log(`调用者 =&gt; [${WatchName}] 获取属性名 =&gt; [${propKey}], 结果 =&gt; [${(result)}]`);
                    }
                    return new Proxy(result, getObjhandler(`${WatchName}.${propKey}`))
                }
                if (typeof (propKey) !== "symbol") {
                    dtavm.log(`调用者 =&gt; [${WatchName}] 获取属性名 =&gt; [${propKey?.description ?? propKey}], 结果 =&gt; [${result}]`);
                }
                return result;
            },
            set(target, propKey, value, receiver) {
                if (value instanceof Object) {
                    dtavm.log(`调用者 =&gt; [${WatchName}] 设置属性名 =&gt; [${propKey}], 值为 =&gt; [${(value)}]`);
                } else {
                    dtavm.log(`调用者 =&gt; [${WatchName}] 设置属性名 =&gt; [${propKey}], 值为 =&gt; [${value}]`);
                }
                return Reflect.set(target, propKey, value, receiver);
            },
            has(target, propKey) {
                var result = Reflect.has(target, propKey);
                dtavm.log(`针对in操作符的代理has=&gt; [${WatchName}] 有无属性名 =&gt; [${propKey}], 结果 =&gt; [${result}]`)
                return result;
            },
            deleteProperty(target, propKey) {
                var result = Reflect.deleteProperty(target, propKey);
                dtavm.log(`拦截属性delete =&gt; [${WatchName}] 删除属性名 =&gt; [${propKey}], 结果 =&gt; [${result}]`)
                return result;
            },
            defineProperty(target, propKey, attributes) {
                var result = Reflect.defineProperty(target, propKey, attributes);
                dtavm.log(`拦截对象define操作 =&gt; [${WatchName}] 待检索属性名 =&gt; [${propKey.toString()}] 属性描述 =&gt; [${(attributes)}], 结果 =&gt; [${result}]`)
                // debugger
                return result
            },
            getPrototypeOf(target) {
                var result = Reflect.getPrototypeOf(target)
                dtavm.log(`被代理的目标对象 =&gt; [${WatchName}] 代理结果 =&gt; [${(result)}]`)
                return result;
            },
            setPrototypeOf(target, proto) {
                dtavm.log(`被拦截的目标对象 =&gt; [${WatchName}] 对象新原型==&gt; [${(proto)}]`)
                return Reflect.setPrototypeOf(target, proto);
            },
            preventExtensions(target) {
                dtavm.log(`方法用于设置preventExtensions =&gt; [${WatchName}] 防止扩展`)
                return Reflect.preventExtensions(target);
            },
            isExtensible(target) {
                var result = Reflect.isExtensible(target)
                dtavm.log(`拦截对对象的isExtensible() =&gt; [${WatchName}] isExtensible, 返回值==&gt; [${result}]`)
                return result;
            },
        }
        return handler;
    }

    if (type === "method") {
        return new Proxy(obj, getMethodHandler(objname, obj));
    }
    return new Proxy(obj, getObjhandler(objname));
}

```

直接用上面的这个代理替换掉自己的代理，结果就正确了：

自此，testab 参数补环境模拟完成。

### 结果展示

#### 浏览器

#### vm2

#### node
