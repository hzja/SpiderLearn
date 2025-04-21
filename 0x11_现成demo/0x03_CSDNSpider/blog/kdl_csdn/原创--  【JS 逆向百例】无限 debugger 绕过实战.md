# 原创
：  【JS 逆向百例】无限 debugger 绕过实战

# 【JS 逆向百例】无限 debugger 绕过实战

<img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/7d4a1d625bf858b90a223fe60c15b735.png#pic_center"/><br/> 

#### 文章目录

---


> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### 逆向过程

#### 绕过无限 debugger

我们尝试抓包，打开开发者工具，刷新一下页面，会发现此时页面被断到 debugger 的位置，点击下一步，又会被断到另一个 debugger 的位置，这种情况就是无限 debugger，无限 debugger 存在的意义就是防止一部分人进行调试，但事实上绕过无限 debugger 的方法非常简单，方法也非常多，以下介绍常用的几种绕过方法。

##### 1.Never pause here

在 debugger 位置，点击行号，右键 Never pause here，永远不在此处断下即可：

##### 2. Add conditional breakpoint

同样右键选择 Add conditional breakpoint，输入 false 即可跳过无限 debugger，其原理是添加条件断点，不管前面代码的逻辑是什么，运行到 debugger 的时候必定是 true 才能执行，只需要将其改为 false，那么它就不执行了：

##### 3.中间人拦截替换无限 debug 函数

所谓中间人拦截替换，就是狸猫换太子，将原来的含有无限 debugger 的函数给替换掉，这种方法适用于知道无限 debugger 函数所在的具体 JS 文件，重写 JS 文件，使其不含有无限 debugger 的函数，利用第三方工具将原来的 JS 文件替换成重写过后的文件，这类工具有很多，例如浏览器插件 ReRes，它通过指定规则，可以把请求映射到其他的 URL，也可以映射到本机的文件或者目录，抓包软件 Fidder 的 Auto responder 功能，也可以实现替换。

##### 4.方法置空

直接在 Console 中将无限 debugger 的函数重写置空也可以破解无限 debugger，缺点是刷新后失效，基本上不太常用。

#### 抓包分析

绕过无限 debugger 后，点击下一页进行抓包分析，数据接口类似于：`http://zwfw.xxxxxx.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=d455731630315957615&amp;t=2491_d51515_1630315979000`，Cookie、Query String Parameters 和 Request Payload 的参数需要我们解决。

#### 参数逆向

首先是 Cookie，直接搜索，可以发现在首页的请求中，Set-Cookie 里设置了 cookie 值，那么使用 get 方法请求主页，在 response 里面直接取 Cookie 即可：

Request Payload 的参数经过观察可以发现 start 每一页 +7，其他参数不变

Query String Parameters 的两个参数 s 和 t，是经过 JS 加密后得到的。

全局搜索 s 这个参数，由于 s 太多，可以尝试搜索 `var s`，可以找到一个 `var sig` 的地方，这段函数后面有两个比较明显的语句：`curUrl += "?s=" + sig;` `curUrl += "&amp;t=" + t;`，不难看出是 URL 拼接语句，s 参数就是 sig，埋下断点，可以看到正是我们要找的参数：

将这段函数 copy 下来进行本地调试，会发现提示 LEx 未定义，直接跟进 `LEx.isNotNull` 这个函数，将原函数 copy 下来即可：

再次调试，会提示 `__signature` 参数未定义，全局搜索发现这个值在主页的 HTML 里面可以找到，直接正则表达式提取出来即可。

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码，不能直接运行！**完整代码仓库地址：https://github.com/kgepachong/crawler/

#### JS 加密代码

```
isNotNull = function (obj) {
    if (obj === undefined || obj === null || obj == "null" || obj === "" || obj == "undefined")
        return false;
    return true;
};

function getDecryptedParameters(__signature) {
    var sig = "";
    var chars = "0123456789abcdef";
    if (!isNotNull(__signature)) {
        var curTime = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "" + Date.parse(new Date());
        sig = chars.charAt(parseInt(Math.random() * (15 - 15 + 1) + 10)) + chars.charAt(curTime.length) + "" + curTime;
    } else {
        sig = __signature;
    }

    var key = "";
    var keyIndex = -1;
    for (var i = 0; i &lt; 6; i++) {
        var c = sig.charAt(keyIndex + 1);
        key += c;
        keyIndex = chars.indexOf(c);
        if (keyIndex &lt; 0 || keyIndex &gt;= sig.length) {
            keyIndex = i;
        }
    }

    var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
    var t = timestamp;
    //LEx.azdg.encrypt(timestamp,key);
    t = t.replace(/\+/g, "_");
    return {"s": sig, "t": t};
}

// 测试样例
// console.log(getDecryptedParameters("c988121626057020055"))

```

#### Python 代码

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import execjs
import requests


index_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
data_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
session = requests.session()


def get_encrypted_parameters(signature):
    with open('encrypt.js', 'r', encoding='utf-8') as f:
        js = f.read()
    encrypted_parameters = execjs.compile(js).call('getDecryptedParameters', signature)
    return encrypted_parameters


def get_signature_and_cookies():
    response = session.get(url=index_url, headers=headers)
    cookies = response.cookies.get_dict()
    cookie = cookies['ICITYSession']
    signature = re.findall(r'signature = "(.*)"', response.text)[0]
    return cookie, signature


def get_data(cookie, parameters, page):
    payload_data = {'start': page*7, 'limit': 7, 'TYPE@=': '2', 'OPEN@=': '1'}
    params = {'s': parameters['s'], 't': parameters['t']}
    cookies = {'ICITYSession': cookie}
    response = session.post(url=data_url, headers=headers, json=payload_data, params=params, cookies=cookies).json()
    print(payload_data, response)


def main():
    ck, sig = get_signature_and_cookies()
    for page in range(10):
        # 采集10页数据
        param = get_encrypted_parameters(sig)
        get_data(ck, param, page)


if __name__ == '__main__':
    main()

```
