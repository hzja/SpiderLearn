# 原创
：  17track物流查询平台 last-event-id 参数逆向分析

# 17track物流查询平台 last-event-id 参数逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

目标：17xx 物流查询平台 last-event-id 参数逆向分析

网站：`aHR0cHM6Ly93d3cuMTd0cmFjay5uZXQvemgtY24=`

### 抓包分析

打开 `F12` ，映入眼帘的就是我们熟悉的 `debugger` , 我们直接看它触发 `debugger` 的 js 文件：

又是经典的 ob 混淆， 这里直接借用 v佬 的插件快速还原，工具地址如下：

> 
Github 仓库：https://github.com/cilame/v_jstools
在线分析工具：https://astexplorer.net


看了一下也不需要我们做另外的预处理操作了，只需要把代码 ob 混淆的部分放入工具内就可以还原了：

还原后，过 `debugger` 就容易多了，只需要将下面这几个关于代码检测的函数都删除掉，都是些无关的代码，检测代码格式化 、`debugger` 等：

然后再通过工具替换代码，这边选用 `ReRes` 工具进行替换，写好规则保存勾选就好了：

```
https://github.com/annnhan/ReRes

```

我们就可以正常抓包分析代码了，目标参数：

通过搜索 `last-event-id` 就可以定位到，其就在我们解完混淆的文件里：

解完混淆后代码就清晰可见，缺啥扣啥，一步步来就好了，代码也不多，可见 AST 解混淆的重要性。

注意点：

附上完整的 `JS` 代码：

```
var _0x199099 = [];
var _0x19d69d = "";
var _0x308754 = "17";
var _0x58ecad = 0;
var _0x269b49 = "";
var _0x288444 = 5;
function _0x5879b4(_0x56b807, _0x3603af) {
    var _0x2f5b4a = 1315423911 ^ _0x3603af &lt;&lt; 16;
    var _0x4844e9;
    var _0x4d42c4;
    for (_0x4844e9 = _0x56b807.length - 1; _0x4844e9 &gt;= 0; _0x4844e9--) {
        _0x4d42c4 = _0x56b807.charCodeAt(_0x4844e9);
        _0x2f5b4a ^= (_0x2f5b4a &lt;&lt; 5) + _0x4d42c4 + (_0x2f5b4a &gt;&gt; 2);
    }
    return _0x4243f2(4),
    Math.abs(_0x2f5b4a &amp; 2147483647);
};

function _0x4243f2(_0x8916b) {
    _0x199099[3] = _0x8916b;
}


function _0x1d212e(_0x3ffdba) {
    if (!_0x3ffdba)
        return 0;
    var _0x9920fa = 5381;
    var _0x55570f = _0x3ffdba.length;
    while (_0x55570f) {
        _0x9920fa = _0x9920fa * 33 ^ _0x3ffdba.charCodeAt(--_0x55570f);
    }
    return _0x9920fa &gt;&gt;&gt; 0;
};

function _0x39b7cc(_0x18dcad) {
    return _0x18dcad.split("").reverse().join("");
};


function _0x402770(_0x1e4f12) {
    var _0x3bcbe3 = "";
    for (var _0x5f5a6c = 0; _0x5f5a6c &lt; _0x1e4f12.length; _0x5f5a6c++) {
        if (_0x3bcbe3 == "")
            _0x3bcbe3 = _0x1e4f12.charCodeAt(_0x5f5a6c).toString(16);
        else
            _0x3bcbe3 += _0x1e4f12.charCodeAt(_0x5f5a6c).toString(16);
    }
    return _0x3bcbe3;
};

;function _0x4293c9(_0x5b936d) {
    function _0x44c5b9(_0x185712, _0x240a39, _0xc135ae, _0x4da978, _0x511583) {
        return _0x56f850(_0x185712 - 152, _0x240a39 - 498, _0xc135ae - 247, _0x4da978 - -820, _0x240a39);
    }
    var _0x147e74 = _0x5b936d;
    while (_0x147e74.length &lt; 8) {
        _0x147e74 = "0" + _0x147e74;
    }
    return _0x147e74;
}

;function _0x59789d(_0x20b526, _0x117056, _0x2c2317) {
    var _0x26536c = _0x5879b4(_0x20b526, _0x117056);
    if (_0x2c2317) {
        _0x199099[5] = _0x4293c9(_0x26536c.toString(16));
        return;
    }
    _0x199099[4] = _0x4293c9(_0x26536c.toString(16));
};

function _0x187331(_0xcae6a6) {
    var _0x59eb35 = _0xcae6a6;

    var _0x46a854 = Math.random();
    _0x59eb35 = Math.round(_0x46a854 * _0xcae6a6);
    _0x288444 = _0x288444 * _0x288444;
    
    _0x199099[1] = _0x59eb35.toString(16);
    _0x199099[2] = _0x59eb35.toString(16).length;
    return _0x59eb35;
};

function createGUID(e, t) {
    var o = (new Date).getTime();
    return (e || "G-xxxxxxxxxxxxxxxx").replace(t || /[xy]/g, function(e) {
        var t = (o + 16 * Math.random()) % 16 | 0;
        return ("x" == e ? t : 7 &amp; t | 8).toString(16).toUpperCase()
    })
}




function get_last_event_id(_0x19d69d, YQ_md5){
    _yq_bid = createGUID();
    _0x4566f3 = undefined;
    _0x59789d(_0x19d69d, _0x19d69d.length, !![])
    _0x6de72e = _0x187331(43)


    var _0x5d4d80 = "yq-";
    _0x58ecad = _0x6de72e;

    // 指纹信息 24: screen.colorDepth
    cancas_fp = '24\r\nzh-CN\r\n-480\r\n1067x1707\r\ndata:image/png;base64,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+nvXGm0L1ZPFO/6e271RWX1vkJZz3/SeYr3dMepg//0Tlim4B7Uuw3J9yH/jEWsd5OOBfOXt/pbQcnpY2wjobgO1nILe7efv5v3q6SmP+JRXnQiLnzbW0tr4s9eB5ej6bs7/bt/7II91t7FZvl9YYfGJ3Gzo+meh/K9//nbC4vPni/5As2oSDxdU95fuhc+DEhZPDXlVO/fF+h6rGWldCYuPYrrozX/BoZ723wuvByURdatEhJnJfRfWvSQHn3mwBO5EWA82ogdztLoU1oM5AxwFwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEMAwhImVQgUBEAAwkINgAAICEPg/wHI0p2WviCNVgAAAABJRU5ErkJggg=='

    var _0x2b62a6 = _0x1d212e(cancas_fp);
    var _0x5d74a6 = _0x1d212e(_0x4566f3);

    if (_0x6de72e == 0)
    _0x5d4d80 += "random";
    else {
    _0x5d4d80 = "dropdown-menu-footer yq-user-footer clearfix";   // 目测可以写死或者随机取
    }
    _0x269b49 = _yq_bid;


    _0x5d4d80 = _0x269b49;
    (_0x58ecad = _0x58ecad * 50,
    _0x5d4d80 += ":" + false + ":" + _0x2b62a6 + ":" + _0x6de72e + ":" + _0x58ecad);
    _0x5d4d80 += "/" + Date.now().toString(16) + "/11/" + true + "/" + new Date().getTimezoneOffset().toString() + "/" + _0x2b62a6 + "/" + YQ_md5 + "/" + _0x5d74a6;
    _0x59789d(_0x5d4d80, _0x6de72e);
    _0x5d4d80 = _0x402770(_0x39b7cc(_0x5d4d80));
    _0x199099[0] = _0x5d4d80;
    return [_0x199099.join(""), _yq_bid]

};

console.log(get_last_event_id('{"data":[{"num":"LZ025387152CN","fc":0,"sc":0}],"guid":"","timeZoneOffset":-480}', '22c342b'));

```

### 结果验证
