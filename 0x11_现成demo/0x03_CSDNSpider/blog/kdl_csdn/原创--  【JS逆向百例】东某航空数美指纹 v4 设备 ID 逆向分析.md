# 原创
：  【JS逆向百例】东某航空数美指纹 v4 设备 ID 逆向分析

# 【JS逆向百例】东某航空数美指纹 v4 设备 ID 逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

目标：东某航空某数指纹 v4 设备 ID 逆向分析

网站：`aHR0cHM6Ly93d3cuZG9uZ2hhaWFpci5jb20v`

### 抓包分析

打开网站，找到返回机票信息的机票查询接口 `flightSearch`，分析发现两个加密参数需要分析：

搜索后发现，“B” 后面的内容，是由 `v4` 接口返回的，然后拼接上 “B” 得到的 `deviceId`：

点开调用堆栈，都是由 `fp.min.js` 文件加载出来的，进入后，发现经过 ob 混淆了，不过通过搜索也能轻松定位到。我们直接搜索 `compress ` 或者 `encode`，注意找与后面数字一致的地方，打下断点，有两处地方，重新刷新，最终定位到的位置如下：

#### ep

该参数由 `_0x5223ab` 大对象取值生成，搜索发现 `_0x5223ab` 对象是经过 `_0x484fb9` 函数进行赋值操作的：

我们搜索 `_0x484fb9` 函数的赋值操作，即可定位到 `ep` 参数生成的位置：

#### data

由 `_0x1d1d7a ` 生成，定位就在上面，通过 `_0x99c3c2 ` 函数生成，跟进去，返回的 `_0x1498fb`：

两次赋值 `tn`，不过赋值在两个不同的对象中，只用分析下面的就行，下面的后面会用到，跟进 `_0x28c88b`：

扣下来即可，里面的 `md5` 摘要算法，经过测试也是标准的，继续往下走，跟进到 `_0x8b10c3['default']` 函数中，传入了两个对象：

通过一些条件进行筛选，满足条件的，取一个对象的值与第二个对象的 key，进行 DES 加密，然后添加到新的对象，不满足条件的直接添加到新的对象中去：

然后进行 `gzip` 压缩，提示得相当清楚，我们可以直接引库：

```
// 导入pako库
const pako = require('pako');

function gzip_decrypt(compressedBase64String){
    // 将Base64字符串解码为二进制数据
    compressedData = Buffer.from(compressedBase64String, 'base64');

    // 使用pako库解压缩二进制数据
    decompressedData = pako.ungzip(compressedData, { to: 'string' });

    // 输出解压缩后的字符串
    return decompressedData;
}

function gzip_encrypt(dataToCompress){
    // 将数据转换为Uint8Array
    dataUint8Array = new TextEncoder().encode(dataToCompress);

    // 使用pako库进行gzip压缩
    compressedDataUint8Array = pako.gzip(dataUint8Array);

    // 将压缩后的数据以Base64编码
    compressedBase64String = Buffer.from(compressedDataUint8Array).toString('base64');
    return compressedBase64String;
};

_0x1498fb = gzip_encrypt(JSON.stringify(_0x1498fb));

```

继续往下走，来到我们返回最后一个 `_0x1498fb` 值的生成位置，通过 `aesEncrypt` 函数将上面的压缩数据 `_0x1498fb` 与 `priId` 加密后生成，进入到这个函数中观察一下：

是标准的 AES，CBC 加密，加密内容为 `gzip` 压缩数据 `_0x1498fb`，key 是 `priId`，iv 值固定为 `0102030405060708`。目前 `priId` 的生成方式还不知道，发现也是在 `_0x5223ab` 大对象中，跟我们获取 `ep` 的逻辑一样，发现就在生成 `ep` 的位置的上面：

将我们生成 `ep` 传入的 uuid 类型的参数 `_0x1dbb2a` 进行截取然后进行标准的 `MD5` 加密，就得到了 `priId` 参数值。

最后就是对明文的分析了，由一些浏览器环境、加密参数等信息构成，通过 `sent` 接收 ，由 `_0xa0ac38(_0x4c1ea4['Protocol'])` 返回，分析几个加密参数：

扣下来即可，`MD5_Encrypt ` 是标准加密：

```
function _0xf7f244() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'['replace'](/[xy]/g, function(_0x33e3b5) {
        var _0x49279a = 0x10 * Math['random']() | 0x0;
        return ('x' == _0x33e3b5 ? _0x49279a : 0x3 &amp; _0x49279a | 0x8)['toString'](0x10);
    });
};


function getLocalsmid() {
    var _0xa5b93 = (_0x1ccff8 = new Date(),
    _0x5a4c0d = _0x1ccff8['getFullYear']()['toString'](),
    _0x5b0ca1 = (_0x1ccff8['getMonth']() + 0x1)['toString'](),
    _0x229546 = _0x1ccff8['getDate']()['toString'](),
    _0x539a5b = _0x1ccff8['getHours']()['toString'](),
    _0x29336d = _0x1ccff8['getMinutes']()['toString'](),
    _0x548117 = _0x1ccff8['getSeconds']()['toString'](),
    _0x317aff = _0x5a4c0d + (_0x5b0ca1 = _0x5b0ca1 &lt;= 0x9 ? '0' + _0x5b0ca1 : _0x5b0ca1) + (_0x229546 = _0x229546 &lt;= 0x9 ? '0' + _0x229546 : _0x229546) + (_0x539a5b = _0x539a5b &lt;= 0x9 ? '0' + _0x539a5b : _0x539a5b) + (_0x29336d = _0x29336d &lt;= 0x9 ? '0' + _0x29336d : _0x29336d) + (_0x548117 = _0x548117 &lt;= 0x9 ? '0' + _0x548117 : _0x548117),
    _0x163575 = _0xf7f244(),
    _0x4fa2e9 = _0x317aff + MD5_Encrypt(_0x163575) + '00',
    _0xd556d6 = MD5_Encrypt('smsk_web_' + _0x4fa2e9)['substr'](0x0, 0xe),
    _0x4fa2e9 + _0xd556d6 + 0x0), _0x317aff, _0x163575, _0x4fa2e9, _0xd556d6, _0x1ccff8, _0x5a4c0d, _0x5b0ca1, _0x229546, _0x539a5b, _0x29336d, _0x548117;
    return _0xa5b93;
};

```

最后，风控部分就需要自己去探索了，跑多了，如果遇到 `'status': '-2'`，就是触发了数某的验证码，携带验证成功的 `rid` 就可以正常采集到数据了。

### 结果验证
