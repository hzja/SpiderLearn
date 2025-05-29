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
const {
   VM,VMScript} = require("vm2");
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
   
        set_native(func,myFunction_toString_symbol,`function ${
     myFunction_toString_symbol,func.name || ''}() { [native code] }`)
    }
}).call(this);

window = this
```
