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
const {
   createCanvas, loadImage} = require('canvas'); // 导入 canvas 模块
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
        .then(response =
```
