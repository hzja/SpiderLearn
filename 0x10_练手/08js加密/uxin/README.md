# 优信二手车JS逆向破解
***
#### 文件列表:
##### uxin.js 破解JS
##### handle_uxin.py 使用pyexecjs读取破解JS，实现破解
***
#### 逆向方法:
##### 1、解除无限debug,根据chrome开发者工具右侧调用顺序，将无限debug函数置空
```javascript
_0x355d23 =function(){};
_0x4db1c = function(){};
```
##### 2、置空后下断点到arg2和arg1位置
```javascript
var _0x23a392 = arg1[_0x55f3('0x19', '\x50\x67\x35\x34')]();
arg2 = _0x23a392[_0x55f3('0x1b', '\x7a\x35\x4f\x26')](_0x5e8b26);
``` 
##### 3、逐步调试最终定位到只需要如下代码即可得出_0x23a392
```javascript
String['\x70\x72\x6f\x74\x6f\x74\x79\x70\x65'][_0x55f3('0x14', '\x5a\x2a\x44\x4d')] = function() {
    var _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd, 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c, 0x22, 0x25, 0xc, 0x24];
    var _0x4da0dc = [];
    var _0x12605e = '';
    for (var _0x20a7bf = 0x0; _0x20a7bf < this['\x6c\x65\x6e\x67\x74\x68']; _0x20a7bf++) {
        var _0x385ee3 = this[_0x20a7bf];
        for (var _0x217721 = 0x0; _0x217721 < _0x4b082b[_0x55f3('0x16', '\x61\x48\x2a\x4e')]; _0x217721++) {
            if (_0x4b082b[_0x217721] == _0x20a7bf + 0x1) {
                _0x4da0dc[_0x217721] = _0x385ee3;
            }
        }
    }
    _0x12605e = _0x4da0dc['\x6a\x6f\x69\x6e']('');
    return _0x12605e;
};
```
##### 4、经过多次调试发现，_0x5e8b26值固定，接着调试arg2 = _0x23a392\[_0x55f3\('0x1b', '\x7a\x35\x4f\x26'\)\]\(_0x5e8b26\);找到如下代码
```javascript
String[_0x55f3('0x5', '\x6e\x5d\x66\x52')][_0x55f3('0x6', '\x50\x67\x35\x34')] = function(_0x4e08d8) {
    var _0x5a5d3b = '';
    for (var _0xe89588 = 0x0; _0xe89588 < this[_0x55f3('0x8', '\x29\x68\x52\x63')] && _0xe89588 < _0x4e08d8[_0x55f3('0xa', '\x6a\x45\x26\x5e')]; _0xe89588 += 0x2) {
        var _0x401af1 = parseInt(this[_0x55f3('0xb', '\x56\x32\x4b\x45')](_0xe89588, _0xe89588 + 0x2), 0x10);
        var _0x105f59 = parseInt(_0x4e08d8[_0x55f3('0xd', '\x58\x4d\x57\x5e')](_0xe89588, _0xe89588 + 0x2), 0x10);
        var _0x189e2c = (_0x401af1 ^ _0x105f59)[_0x55f3('0xf', '\x57\x31\x46\x45')](0x10);
        if (_0x189e2c[_0x55f3('0x11', '\x4d\x47\x72\x76')] == 0x1) {
            _0x189e2c = '\x30' + _0x189e2c;
        }
        _0x5a5d3b += _0x189e2c;
    }
    return _0x5a5d3b;
};
```
##### 5、逐步调试，最终得出arg2值
##### 6、uxin逆向JS方法和努比亚逆向方法相同,可以改为python代码

***
#### 我在慕课网上主讲课程[Python爬虫工程师必学——App数据抓取实战](https://coding.imooc.com/class/283.html),还请各位大神多多支持.
#### bug:dazhuang_python@sina.com
