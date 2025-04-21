# 原创
：  【JS逆向百例】音乐 wasm 逆向

# 【JS逆向百例】音乐 wasm 逆向

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近在看知识星球群聊的时候，发现有小伙伴在讨论酷某音乐的相关问题，之前也有星球成员私信询问这个案例。K哥一向是尽力满足粉丝需求的，本文就对该站进行逆向研究，该案例较为新奇，既能满足粉丝需求，也是对 wasm 逆向案例的补充与完善：

### 逆向目标

### 抓包分析

进入首页，随机输入手机号，点击发送验证码，弹出验证码弹窗，进行抓包，有很多响应。经过分析，有用的接口为 `send_mobile`与`get_verfy_info`：

<img alt="7GZzbe.jpg" src="https://i-blog.csdnimg.cn/blog_migrate/ed407f75a5ed1ad52759cfe2b78b757c.jpeg"/><br/> 经过首次 send_mobile 接口后会在响应协议头里返回 ssa-code：

同时在 `get_verfy_info` 接口将会携带这个参数：

最终，通过该接口返回一个 `sessionid`，代表会话创建完毕，是全局唯一的标识符：

然后，通过易盾点选/滑块验证码，发现会经过 `v4/verify_user_info` 进行验证：

该接口参数很多，同时还观察到了有 wasm 相关的字样：

最终，再次调用 `send_mobile ` 接口，`status:1` 则代表发送成功：

经过抓包分析，我们需要逆向的参数为：`mid`、`uuid`、`signature`、`params`、`pk`、`sid`、`edt` 。

### 逆向分析

#### mid、uuid 参数

点击发送按钮，然后我们查看 send 的堆栈，从第一个进入：

然后搜索 `mid:` 发现有几处地方可疑，在这几处分别下断，最终在如下的地方成功断下来：

我们进入 `getKgMid` 方法，发现他取了 cookie 中的 kg_mid，且这个值与我们刚刚看到的值相同，如果 cookie 中不存在该参数，那么将会调用下面的方法取浏览器的指纹信息，通过 md5 算法生成该值：

所以我们直接利用 v_jstools 去 hook 一下该 cookie 参数是如何生成的，Hook 脚本如下：

```
(function () {
  'use strict';
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('kg_mid') != -1) {
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

清空浏览器缓存，刷新发现成功断下，向上跟栈，找到该参数生成的位置如下：

分析可知，该参数是通过生成 uuid 然后利用 md5 算法生成的，跟进 uuid 的生成函数中，其生成逻辑如下：

```
Guid: function() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }
        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }

```

至此 mid、uuid 参数就分析完毕了。

#### signature 参数

signature 参数同上也是全局搜索 signature 最终在该地方成功断下，其生成逻辑如下：

将 url 中的 parm 参数与 data 参数进行拼接，然后分别调用 `K.unshift(y) ` 与 `K.push(y)` 在数组开头和结尾分别插入一个固定字符串，最终通过 `join` 将数组拼接成字符串进行 md5 加密生成 signature 参数。

#### params、pk 参数

params 参数就生成在 mid 参数下面，逻辑如下：

通过将待加密的 obj 对象传入 AES 函数中，最后返回 key 与 encryptedStr 参数。我们进入 AES 函数查看其生成逻辑：

经过分析可知，通过随机生成 t ，然后将 t 经过指定的处理逻辑将其处理为 key 和 iv ，最后将加密参数与 t 一起返回，复现如下：

```
function AES_Encrypt(data) {
    // 将输入数据转换为JSON字符串
    const jsonString = JSON.stringify(data);

    // 生成随机密钥（Key）
    const generateRandomKey = (length) =&gt; {
        const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        let randomKey = '';
        for (let i = 0; i &lt; length; i++) {
            randomKey += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return randomKey;
    };

    // 如果未提供密钥，则生成一个16字符的随机密钥
    key = generateRandomKey(16);

    // 使用MD5对密钥进行编码，并截取前32字符作为实际密钥
    const md5Key = md5_encode(key).substring(0, 32);

    // 如果未提供向量（IV），则使用密钥的最后16字符
    iv = md5Key.substring(md5Key.length - 16);

    // 将密钥和向量转换为CryptoJS的Utf8对象
    const cryptoKey = CryptoJS.enc.Utf8.parse(md5Key);
    const cryptoIv = CryptoJS.enc.Utf8.parse(iv);

    // 使用AES算法进行加密
    const encrypted = CryptoJS.AES.encrypt(jsonString, cryptoKey, {
        iv: cryptoIv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    // 将加密结果转换为Hex字符串
    const encryptedHexStr = CryptoJS.enc.Hex.stringify(CryptoJS.enc.Base64.parse(encrypted.toString()));

    return {
        key: key,
        encryptedStr: encryptedHexStr
    };
}

```

接着继续往下，发现 pk 是由 rsa 生成的，主要是对 key 进行了加密：

进入 RSA.encrypt 函数，发现是一个公钥指数为 10001 类型为 NoPadding 的 RSA 加密：

每次加密的结果都有且只有一个唯一值，经过引库或者 wt-js 进行复现，发现最终生成的加密值与其不同，最终我们将代码全部拿下，放到 nodepad 中：

发现其在一个大模块当中，我们将他改写为一个自执行函数，并且以模块的形式将他导入：

```
const RSA = require('./rsa'); // 引入保存的rsa.js文件

function rsa_encode(word){
    word = JSON.stringify(word)
    // 使用的公钥
    const publicKey = "B1B1EC76A1BBDBF0D18E8CD9A87E53FA3881E2F004C67C9DDA2CA677DBEFA3D61DF8463FE12D84FF4B4699E02C9D41CAB917F5A8FB9E35580C4BDF97763A0420A476295D763EE10174E6F9EBF7DF8A77BA5B20CDA4EE705DEF5BBA3C88567B9656E52C9CD5CD95CA735FF2D25F762B133273EEEB7B4F3EA8B6DA29040F3B67CD";
    
    // 使用 encrypt 函数进行加密
    const encryptedMessage = RSA.encrypt(word);
    return encryptedMessage
    
    }

```

最后与网页对照结果一致：

### sid、edt 参数

解决完上面的参数以后，最终来到 sid 与 edt 参数这边，同样利用堆栈和搜索，快速定位到如下位置：

发现其生成逻辑如下：

```
var t = new wasm_bindgen.EData;
e.sid = t.get_sid(),
e.edt = c

```

发现是先 new 了一个 `wasm_bindgen` 下的 EData 对象，我们进入 EData 里面查看，其逻辑为：

我们全局搜索 `wasm_bindgen` 在该变量赋值的地方下一个断点，清除缓存，点击发送在初始化的位置成功断下：

随后单步跟进，发现在该方法初始化完毕以后，在如下位置开始加载 wasm 文件：

紧接着就准备与 WebAssembly (Wasm) 模块交互，具体来说，开始为 WebAssembly 实例配置导入对象 `imports`。当然这也是本文最最最恶心的部分，在交互部分进行了大量的检测。

原型链的检测：

DOM 层相关检测：

WebGL 原型链检测：

WebGL 相关 API 操作检测：

如果我们还是像以往那样，在 node 中使用 WebAssembly 去加载 wasm 必然会出错，因为我们缺少对应的环境，所以我们需要将 `verifycode.js` 全部拉下来到本地，如下：

然后我们还是使用往期蜜雪的代理框架：[最新雪王 type__1286 参数逆向分析，K哥带你免费喝一杯~](https://mp.weixin.qq.com/s/Tvnp6557s25uvSJ_gXYZJg)。

将我们的老生常谈的 document、window、navigator、canvas、location 等等全部挂上代理。

**_instanceof 解析**

原始代码如下：

```
function _instanceof(left, right) {
  if (right != null &amp;&amp; typeof Symbol !== "undefined" &amp;&amp; right[Symbol.hasInstance]) {
    return !!right[Symbol.hasInstance](left);
  } else {
    return left instanceof right;
  }
}

```

所以在补的时候就需要注意原型链的继承关系，比如 window 以及 navigator、canvas 等，这里举几个例子说明：

```
HTMLCanvasElement = function HTMLCanvasElement (){
}
canvas.__proto__=HTMLCanvasElement.prototype

function WebGLRenderingContext() {}

// 为 WebGLRenderingContext 添加 Symbol.hasInstance
 Object.defineProperty(WebGLRenderingContext, Symbol.hasInstance, {
  value: function (obj) {
    return obj &amp;&amp; typeof obj === 'object' &amp;&amp; obj.drawingBufferWidth !== undefined &amp;&amp; obj.drawingBufferHeight !== undefined;
  }
}); 

```

在补的时候，可以去检测的地方插桩打印输出相关信息，或者可以直接修改 ret =true（前提你是得知道检测点在哪里）：

又或者可以大胆尝试修改 `_instanceof` 函数，在不影响 wasm 加载的情况下，使其部分检测返回 true 也不为一种办法（当然前提你也得知道检测什么），无脑返回 true 可能会导致假值或者不能用的情况。

在整体代码全部补完以后，我们运行用网页上的方式去调用：

```
var t = new wasm_bindgen.EData;
console.log(t.get_sid())
console.log(t.get_edt())

```

发现提示如下错误：

提示，我们的 wasm 下不存在该模块，但是当我们打印 wasm 的时候却发现 wasm 确确实实存在，且加载完成。进一步分析后得知，wasm 是 fetch 加载，而 fetch 又是异步的形式，所以当我们直接去调用的时候，肯定是调用不到的，同样需要写一个异步去调用：

```
setTimeout(() =&gt; {
			 var t = new wasm_bindgen.EData;
        	console.log(t.get_sid())
		    console.log(t.get_edt())
   			 setTimeout = function(){}
}, 1000);

```

最终，我们用 node 起接口，将异步结果导出：

```
const express = require('express');
const app = express();
const port = 3000;
// 定义一个接口来获取get_sid和get_edt的值
app.get('/getValues', async (req, res) =&gt; {
    // 模拟延时并获取值
    setTimeout(() =&gt; {
        try {
            var t = new wasm_bindgen.EData(); 
            const get_sid = t.get_sid();
            const get_edt = t.get_edt();
        res.json({ get_sid, get_edt });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}, 1000);
});

app.listen(port, () =&gt; {
    console.log(`Server is running on http://localhost:${port}`);
});

```

关于易盾的相关讲解，可以参考往期文章：[【验证码识别专栏】通杀空间推理验证码训练与识别](https://mp.weixin.qq.com/s/UhYgCbiFtyxdkXTEfjljkg)。

### 结果验证

最终的实现流程如下：
