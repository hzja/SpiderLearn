# 原创
：  百度指数 Cipher-Text、百度翻译 Acs-Token 逆向分析

# 百度指数 Cipher-Text、百度翻译 Acs-Token 逆向分析

> 
K 哥之前写过一篇关于百度翻译逆向的文章，也在 bilibili 上出过相应的视频，最近在 K 哥爬虫交流群中有群友提出，百度翻译新增了一个请求头参数 Acs-Token，如果不携带该参数，直接按照以前的方法进行处理，会出现 1022 报错，并且如果直接将 Acs-Token 写成定值，前几次可能能成功，多查询几次也会报同样的错误，现对其进行逆向分析，对往期代码进行重构。与此同时，K哥发现百度指数的某些接口有个 Cipher-Text 参数，与百度翻译的 Acs-Token 加密方式差不多，所以就一起分析一波。


### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请联系作者立即删除！**

### 逆向目标

### 逆向过程

#### 抓包分析

先以百度翻译为例，随便输入文字，可以看到没有刷新页面，翻译结果就出来了，由此可以推断是 Ajax 加载的，打开开发者工具，选择 XHR 过滤 Ajax 请求，找到接口位置，详细分析推荐阅读 K 哥往期百度翻译逆向的文章，如下图可以看到在请求头中新增了一个 Acs-Token 参数，前面两串数字看起来像时间戳，具体加密方式需要我们来进一步分析：

这里使用 Fiddler 插件 hook 定位 Acs-Token 参数，相关 hook 操作方式可阅读 K 哥往期文章，本文不再赘述：

```
(function () {
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        console.log(key, ':', value)
        if (key == 'Acs-Token') {
            debugger;
        }
        return org.apply(this, arguments);
    };
})();

```

清除缓存，点击翻译，可以看到成功 hook 到 Acs-Token 参数，往下跟栈即可找到其值生成的位置：

#### 逆向分析

向下跟栈分析，Acs-Token 参数的值在 `translate.js` 文件的第 187 行生成，由 sign 参数传递，sign 参数定义在第 180 行，在第 195 行打下断点调试，点击翻译后成功在断点处断下：

跟进 `getAcsSign()` 函数，整体选中，点击进入到 `paris.js` 文件中，可以看到函数体中创建了一个异步 Promise 对象进行异步操作：

Promise 的构造函数接收一个函数参数，并且这个函数需要传入两个参数：

所以异步操作执行成功即返回 sign 参数的值：

到这里已经拿到 sign 了，我们再向上跟栈，可以发现 Acs-Token 参数的值在 `acs-2060.js` 文件的第 805 行生成，很明显是拼接而成的：

上图是几天前分析的时候断下的情况，今天再次分析的时候发现结构变了，如下图所示：

这个 `acs-2060.js` 是咋来的呢？在 `paris.js` 里其实可以看到 init 初始化了了一些配置文件，其中的 acsUrl 就是 `acs-2060.js` 的地址，2060 是渠道号，由管理员分配，根据注释可以看到这个东西叫做“玉门关”。

继续前面的步骤，分析一下 `acs-2060.js`，在第 805 行打断点调试，分析 `a8()` 中各拼接部分含义，可得到如下结果：

a0，a1 为定值，分析 a2 字典中各参数值含义：

选中 eg，跟进到 eg 函数定义的位置，在 `acs-2060.js` 文件的第 537 行：

具体内容如下：

```
function eg(a2, a8, a9) {
    return a2 = b('0x4d') == typeof a2 ? JSON[b('0xc')](a2) : void 0x0 === a2 ? '' : '' + a2,
        dD[b('0x37')](a2, ad[b('0x29')](a8), {
        '\x69\x76': ad[b('0x29')](a9),
        '\x6d\x6f\x64\x65': cc,
        '\x70\x61\x64\x64\x69\x6e\x67': cz
    })[b('0x27')][b('0xa')](ag);
}

```

可以在第 538 行打断点进行调试，亦可从控制台直接打印混淆部分内容，会发现三个经典加密参数：

并且在第 548 行将 eg 赋值给了 `window.aes_encrypt`，很明显 AES 加密了，可以选择直接引库，也可以直接扣代码，这里不做继续研究:

#### 百度指数 Cipher-Text

百度指数的 Cipher-Text 和百度翻译的 Acs-Token 在结构上是一样的，根据百度翻译的经验，我们知道核心加密代码应该在“玉门关”里面，不同的站分配的渠道号不一样，我们直接全局搜索 acsUrl，或者直接找 acs 开头的 JS，会发现有一个 `acs-2057.js`：

老样子，在 `a8()` 处下断，刷新接口，即可断下：

百度指数与百度翻译不一样的地方在于开头的那个时间戳不一样，变量 `a0` 不一样，其他的逻辑都是一样的，我们注意到开头的时间戳隔一段时间就会改变，如果在项目代码中应用，人工定时去改肯定是不合理的，这里的处理思路可以是先在本地固定一套算法，然后每次请求先去拿 acs 开头的那个 JS，拿到内容后，通过正则匹配去拿到那个时间戳，再传到本地的算法里生成最终值，灵活处理即可。

至此，Cipher-Text 和 Acs-Token 就分析结束了，本次逆向的加密算法其实并不难，但是想要找到加密位置需要一定的技巧，另外在写这篇文章时，发现百度翻译不加 Acs-Token 请求又可以了，目前的状况是有时候不加可以请求，有时候不加又不能请求，如果你请求发现报错 `{"errno":1022,"errmsg":"访问出现异常，请刷新后重试！","error":1022,"errShowMsg":"访问出现异常，请刷新后重试！"}`，那就可以尝试加上这个参数。

### 完整代码

bilibili 关注 K 哥爬虫，小助理手把手视频教学：https://space.bilibili.com/1622879192

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

以下只演示部分关键代码，不能直接运行！

#### baidufanyi_encrypt.js

```
var window =  global;

// 以下部分内容过长，此处省略
// 完整代码关注 GitHub：https://github.com/kgepachong/crawler
(function(){...
})()
function ascToken(translate_url){
    // 部分参数直接写死了，不同网站参数值不同，如果在项目中使用，请灵活处理
    var a0 = 'uyaqcsmsseqyosiy';
    var a1 = '1234567887654321';
    var ae = (new Date).getTime();
    var a2 = '{"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36","url":' + translate_url + '","platform":"Win32","clientTs":' + ae + ',"version":"2.2.0"}';
    // 这里开头的时间戳写死了，如果请求失败请更新这个值
    return '1660546809505_' + ae + '_' + window.aes_encrypt(a2, a0, a1);
}

// console.log(ascToken("https://fanyi.baidu.com/#zh/en/%E6%B5%8B%E8%AF%95"))

```

#### baidufanyi.py

```
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-12
# @Author  : 微信公众号：K哥爬虫
# @FileName: baidufanyi.py
# @Software: PyCharm
# ==================================


import re
import execjs
import requests
from urllib import parse


session = requests.session()
index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# cookies = {
#     "BAIDUID": "624363427DBD2BFCDF0C3D6E129F5C65:FG=1"
# }


def get_params(query):
    # 获取 token 和 gtk
    session.get(url=index_url, headers=headers)
    # print(session.cookies.get_dict())
    response_index = session.get(url=index_url, headers=headers)
    token = re.findall(r"token: '([0-9a-z]+)'", response_index.text)[0]
    gtk = re.findall(r'gtk = "(.*?)"', response_index.text)[0]
    # 自动检测语言
    response_lang = session.post(url=lang_url, headers=headers, data={'query': query})
    lang = response_lang.json()['lan']
    return token, gtk, lang


def get_sign_and_token(query, gtk, lang):
    with open('baidufanyi_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('e', query, gtk)
    translate_url = 'https://fanyi.baidu.com/#%s/en/%s' % (lang, parse.quote(query))
    acs_token = execjs.compile(baidu_js).call('ascToken', translate_url)
    return sign, acs_token


def get_result(query, lang, sign, token, acs_token):
    data = {
        'from': lang,
        'to': 'en',
        'query': query,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    headers["Acs-Token"] = acs_token
    response = session.post(url=translate_api, headers=headers, data=data)
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字：')
    token, gtk, lang = get_params(query)
    sign, acs_token = get_sign_and_token(query, gtk, lang)
    result = get_result(query, lang, sign, token, acs_token)
    print('翻译成英文的结果为：', result)


if __name__ == '__main__':
    main()

```

<img alt="17" src="https://i-blog.csdnimg.cn/blog_migrate/4be9221784a4e04565c67d567f02819d.png"/><br/> <img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/3db9ba46b4c35a3b32dc4c371607683c.png"/>
