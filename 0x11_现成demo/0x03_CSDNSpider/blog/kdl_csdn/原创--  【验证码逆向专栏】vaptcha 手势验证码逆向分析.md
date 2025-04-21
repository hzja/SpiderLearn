# 原创
：  【验证码逆向专栏】vaptcha 手势验证码逆向分析

# 【验证码逆向专栏】vaptcha 手势验证码逆向分析

### 逆向目标

目标：vaptcha 手势验证码

网站：`aHR0cHM6Ly93d3cudmFwdGNoYS5jb20vI2RlbW8=`

### 抓包分析

抓包分析，首先是 vaptcha-demo 接口：

这个接口返回了验证码类型，其中 embed 的值就是嵌入式点击验证码，其他三个分别对应三种类型。

再看下面这个接口：

目前猜测是请求或配置某些静态资源。

再往下看会看到几个 config 接口：

然后是图片接口 get：

返回的数据包含图片链接等信息：

返回的图片是乱码的，还原步骤后文分析：

接下来是验证接口 validate，参数加密方式大差不大：

返回下面内容，代表验证通过：

### 逆向分析

#### 图片还原

直接下 canvas 断点，我们在下面的这个地方向上跟栈：

跟到这里，会发现加载了几次图像，当我们刷新图片的时候，会看到图片不断地切换。其实就是通过固定数组不断对图像进行操作，然后覆盖：

但是我们最终还原的图像结果不在这，因为最后一次循环执行时，没有获取 `_0x3af163` 数组的最后一个值，而是跳到了其他地方。我们下断点调试，可以找到最终生成地方：

这个解密函数 Decrypt 和参数的生成也很简单，算法如下：

```
function _0x5845e4(_0x33bc25, _0xcc5af2) {
        var _0x1b7e7e = '';
        _0x1b7e7e = (parseInt(_0x33bc25) - _0xcc5af2)['toString']();
        if (_0x1b7e7e['length'] &lt; 0xa) {
            _0x1b7e7e = '0' + _0x1b7e7e;
        }
        return _0x1b7e7e;
    }

```

参数是由 canvas 指纹 + hashComponents + 固定字符串 + work2 接口值返回：

```
_0x3ac810 = _0x3b0a39 + _0x53e0aa + parseInt(_0x327a80['secretC']) + _0x33539f;

```

`_0x3b0a39`：

`_0x53e0aa`：

`_0x33539f`：

传入图片 url 和这个顺序即可还原图片：

还原代码可以 GPT 一下，下面给出的还原代码，仅供参考，感兴趣的小伙伴可以自行修改：

```
// 用于处理图像的函数
const {createCanvas, loadImage} = require('canvas'); // 导入 canvas 模块
const fetch = require('node-fetch');  // 安装2版本

// 用于处理图像的函数
function huany(order,src) {
    // 创建一个 canvas
    const wid = 290;
    const hei = 167;
    const canvas = createCanvas(wid, hei); // 使用 canvas 库创建 canvas 对象
    const ctx = canvas.getContext('2d');  // 获取绘图上下文

    const can_width = Math.round(wid / 5);
    const can_height = Math.round(hei / 2);

    // 使用 node-fetch 下载图像
    const imageUrl = src;

    // 加载图像
    fetch(imageUrl)
        .then(response =&gt; response.buffer()) // 将响应转换为二进制数据
        .then(imageBuffer =&gt; loadImage(imageBuffer)) // 使用 canvas 的 loadImage 函数加载图像
        .then(image =&gt; {
            console.log("图片加载成功！");

            const width = Math.round(400 / 5);
            const height = Math.round(230 / 2);

            // 确保 order 是一个有效的字符串
            if (order.length !== 10) return;

            // 按照顺序处理图像
            for (let i = 0; i &lt; 10; i++) {  // 假设 shunxu[0] 中只有 10 个字符
                const j = i &lt; 5 ? i : i - 5;
                let cha_value = parseInt(order.charAt(i));

                if (cha_value &lt; 5) {
                    // 处理第一部分的图像绘制
                    ctx.drawImage(image, j * width, i &lt; 5 ? 0 : height, width, height, cha_value * can_width, 0, can_width, can_height);
                } else {
                    cha_value = cha_value - 5;
                    // 处理第二部分的图像绘制
                    ctx.drawImage(image, j * width, i &lt; 5 ? 0 : height, width, height, cha_value * can_width, can_height, can_width, can_height);
                }
            }

            // 将生成的图像保存为 PNG 文件
            const fs = require('fs');
            const out = fs.createWriteStream('image.png');
            const stream = canvas.createPNGStream();
            stream.pipe(out);
            out.on('finish', () =&gt; console.log('图像已保存为 image.png'));
        })
        .catch(error =&gt; {
            console.error("图片加载失败！", error);
        });
}

// 执行函数，使用指定的顺序
huany("1523906784","https://img-cn.vaptcha.net/vaptcha/9d64bb2c0c2b494c9881f40250caf252.jpg");

```

#### k 参数

直接搜索这个值，在第二个 config 接口：

#### en 参数

因为获取图片和验证的加密内容基本一致，且都在 vm 文件里面，这里就一同分析。搜索 en 值或者 xhr 断点都可以找到，这里直接搜索即可：

val 的 en 值：

可以看到是一个控制流语句，en 的值都是由 encryFunc 加密生成，接受两个参数，`_0x3583f5['selectFrom'](0x3, 0xf) ` 和

`_0x5d0500`，而 `_0x5d0500` 的值由很多值相加生成，这里我们逐一分析，这里以 get 接口为例：

```
_0x5d0500 = _0x42d77b + _0x34957f + _0x30ee8c + _0x184fa6 + _0x1cbeb7 + _0x38e801 + _0xe67885 + _0x30b74a + _0x183d7b + _0x3c7b59 + _0x28aaca['globalMd5']['slice'](0x0, 0x5);

```

`_0x42d77b` 是 `_0x40ed1f['GenerateFP']()` 生成，进入这个函数，可以看到，经过了canvas 指纹和 crc32 校验：

`_0x34957f` 是上一个异步生成的值返回，我们进入 GenerateFP 这个函数：

可以看到是一段 promise 代码，遇到这种，可以直接到所有返回值和成功回调的地方下断点：

慢慢分析，会发现最后返回的值是 `_0x22dd67 `。`_0x22dd67` 又是通过 hashComponents 方法对 `_0x26e045` 进行加密生成：

可以看到 `_0x26e045` 里面全是环境，这里先把环境写死，再把 `_0x42bf43['hashComponents']` 函数扣下来即可。

当 `_0x22dd67` 值为 true 时，会直接返回该值，反之切割 8 位后返回。

knock 参数的值都是第二个 config 接口返回的，下面就不多强调了：

```
// canvas 指纹
_0x30ee8c = _0x40ed1f['GenerateFP'](_0x1f1e69['knock']['substr'](-0x5, 0x5))  

```

这里的 md5 都是标准的加密算法，直接引库或者扣都行：

```
const crypto = require('crypto');
crypto.createHash('md5').update("值").digest('hex')

```

```
// 异步函数
_0x184fa6 =  _0x16d82b['GenerateFP'](_0x1f1e69['knock']['substr'](-0x5, 0x5))
_0x59bba5 = 'adszzSECRETB'  // 固定值
_0x1cbeb7 = _0x36a17d['hex_md5'](_0x30ee8c + _0x184fa6 + _0x59bba5)['slice'](0x0, 0x5);

```

此处在 get 接口时，ha 的值为空，走第一个逻辑；在 val 接口时，ha 有值，走第二个逻辑：

```
_0x38e801 = _0x28aaca['ha'] === '' ? '0123456789qwe' : _0x28aaca['ha'] + _0x40ed1f['GenerateFP'](_0x28aaca['ha']);  

```

这个地方 get 接口是固定的，val 接口赋值不同：

```
_0xe67885 = _0x376c54 =  '0123456789qwe';

```

从 localStorage 里面取值，经过测试，这里的值可以写死：

```
_0x21a42e = _0x1f1e69['dfu']
_0x4fbf9b = _0x14e656 ? localStorage['getItem']('vaptchanu') ? localStorage['getItem']('vaptchanu')['split'](',')[0x0] : _0x28aaca['staticDfu'] : _0x28aaca['staticDfu'];
_0x30b74a = _0x1cb1c6['compareDfu'](_0x21a42e, _0x4fbf9b);

```

```
_0x183d7b =  _0x14e656 ? localStorage['getItem']('vaptchaut') ? localStorage['getItem']('vaptchaut') : _0x28aaca['staticDfuTrust'] ? _0x28aaca['staticDfuTrust'] : '0123456789qwertyuiopasdf87654321' : _0x28aaca['staticDfuTrust'] ? _0x28aaca['staticDfuTrust'] : '0123456789qwertyuiopasdf87654321';

```

通过对 ua、location 的 host 以及一段固定值，进行 md5 算法进行加密。另外还有个 globalMd5 值，get 接口生成的地方在这里：

```
 _0x36a17d['hex_md5'](_0x280f74)['slice'](0x0, 0x5);

```

参数是由第二个 config 接口的返回值，进行 md5 加密后得到的：

validate 接口值生成的位置，如下图所示：

其中 data 的值是由 get 接口返回的：

另外上面的 globalMd5 中的 splicingObj 函数也不一样，扣的时候注意点就行。

最后验证 val 接口 en 加密多了以下这些参数：

轨迹转化代码：

```
var _0x319301 = {
    '_sample': 'abcdefgh234lmntuwxyz',
    '_convertScale': function (_0x1acba4) {
        _0x1acba4 = Math['floor'](_0x1acba4);
        var _0x395d5e = this['_sample'][_0x1acba4 % 0x14];
        _0x1acba4 = Math['floor'](_0x1acba4 / 0x14);
        var _0x2de1a1 = this['_sample'][_0x1acba4 % 0x14];
        var _0x5461c6 = Math['floor'](_0x1acba4 / 0x14);
        _0x5461c6 = _0x5461c6 ? this['_sample'][_0x5461c6] : '_';
        return ''['concat'](_0x5461c6 || '_')['concat'](_0x2de1a1 || '_')['concat'](_0x395d5e || '_');
    },
    'assemblyCoordData': function (_0x4ae77e) {
        var _0x2e15c5 = [];
        var _0x31480a = [];
        var _0x457f77 = [];
        for (var _0x72bd9d = 0x0, _0x5abd1e = _0x4ae77e; _0x72bd9d &lt; _0x5abd1e['length']; _0x72bd9d++) {
            var _0x171511 = _0x5abd1e[_0x72bd9d];
            _0x2e15c5['push'](this['_convertScale'](_0x171511['x']));
            _0x31480a['push'](this['_convertScale'](_0x171511['y']));
            _0x457f77['push'](this['_convertScale'](_0x171511['time']));
        }
        return _0x2e15c5['join']('') + _0x31480a['join']('') + _0x457f77['join']('');
    }
};
var _0x47570b = [{x: 188, y: 87, time: 14.899999976158142}];
var _0x390710 = _0x319301['assemblyCoordData'](_0x47570b);
console.log(_0x390710);

```

轨迹处理可以自己训练或者对接平台，手势验证码的训练方法可以参考 K 哥往期的文章：

> 
https://mp.weixin.qq.com/s/RJ-oab76HETV2aZBMpleOg (手势验证码模型训练)


### 注意点

en 、knock 值错误，验证接口返回：

```
{"code":"0101","msg":""}

```

验证时间过长：

```
{"code":"0109","msg":""}

```

轨迹值不对，或同一张图片失败过多：

```
{"code":"0104","msg":""}

```

`_0x40ed1f['GenerateFP']() ` 有个坑，当用了 node 的 canvas 库生成这个值，就会报错：

```
{"code": "0103","data": {"u":"","ut":"","token":"000000000000000000000","rate":0},"msg":""}

```

访问频率过快：

```
{"code":"0105","msg":""}

```

另外，调试多了就会被风控，图片也会变灰，遇到这种情况，换个浏览器就行：

相关算法源码会放到星球里面，仅供学习交流，有需要的小伙伴自取~

### 结果验证
