# 原创
：  【JS 逆向百例】DOM事件断点调试，某商盟登录逆向

# 【JS 逆向百例】DOM事件断点调试，某商盟登录逆向

<img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/036543ced85592ace659a1a6ca26a084.png#pic_center"/><br/> 

#### 文章目录

---


> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 声明

**本文章中所有内容仅供学习交流，抓包内容、敏感网址、数据接口均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！**

### 逆向目标

### DOM 简介

在以前的案列中，我们都是通过直接搜索来定位加密参数的位置的，直接搜索出来的定位通常是比较准确的，但是有个弊端就是搜索的结果可能会非常多，需要人工去过滤，需要一定的经验去判断准确的加密位置，而且对于一些反爬力度较大的站点来说，可能做了很多混淆，根本就搜索不到，那么今天的案列中，我们将介绍另一种方法，即 DOM 事件断点，需要注意的是，DOM 事件断点也是有弊端的，**通过这种方法找到的位置通常在加密处理之前**，也就是说想要找到准确的加密位置，还需要进一步分析上下文才能确定。

DOM 全称 Document Object Model，即文档对象模型，是 HTML 和 XML 文档的编程接口，定义了访问和操作 HTML 文档的标准方法。

一个网页其实就是一个 HTML 文件，经过浏览器的解析，最终呈现在用户面前，一个简单的 HTML 页面代码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;

&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;title&gt;我的第一个HTML页面&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;h1&gt;我的第一个标题&lt;/h1&gt;
    &lt;p&gt;我的第一个段落&lt;/p&gt;
&lt;/body&gt;

&lt;/html&gt;

```

在 HTML 页面代码中，head、body 等标签不是随意排列的，它们有自己的规则。首先，它们是嵌套的，一层套一层，比如 html 套 body，body 又套 h1，其次， 每一层可以同时存在很多标签，比如 head 和 body 属于同一层，它们被外面的 html 套着，这样的结构很像计算机里的文件夹，例如，我的电脑是最外层，里面套着 C、D、E、F 盘，每个盘里又有很多文件夹，文件夹里又有文件夹，逐个打开后才能看到具体的文件。

为什么要按照这种结构来组织呢？目的其实是方便解析和查询，解析的时候，从外向里循序渐进，好比按照图纸盖房子，先盖围墙，再盖走廊，最后才盖卧室。查询的时候，会遵循一条明确的路线，一层一层地缩小范围，查找效率会非常高。

所以，浏览器在解析 HTML 文档时，会把每个标签抽象成代码里的对象，按照这种层次分明的结构组织，这就是 DOM，HTML DOM 结构如下图所示：

### 逆向过程

本次逆向的目标是某商盟的登录密码，本案例的加密参数为 `j_mcmm`，加密比较简单，直接全局搜索也很容易找到加密的地方，但是本次我们不使用全局搜索，改用 DOM 事件断点来定位加密位置。

打开开发者工具，点击左上角箭头按钮，再点击登陆按钮，即可定位到该按钮元素的位置，在 Elements 面板，右边选择 Event Listeners，即事件监听列表，可以看到一些鼠标点击、鼠标移动、提交、加载等事件：

我们将这些事件展开具体看一下，submit 提交事件，定位到 div 标签，div 标签下有一个 form 表单，form 的作用就是为用户输入创建 HTML 表单，向服务器传输数据，跟进这个 submit 用到的 JS 文件，大概率就能够找到加密的地方，这里还有个小技巧，如果事件太多，不太好判断哪个是提交数据的，或者哪个是登录事件的，可以选择性的点击 Remove，移除一些事件，再登录，如果登录不能点击，或者 Network 里没有提交请求，就说明 Remove 的这个事件刚好就是目标事件。

跟进 submit 事件用到的 JS，会定位到 `function e()` 的位置，往下看，就可以找到疑似加密的地方，这里出现了两个 `j_mcmm`，分别是 `g.j_mcmm` 和 `P.j_mcmm`，埋下断点进行调试，经过对比可以发现 `g.j_mcmm` 是最终需要的值：

在 `g.j_mcmm = b` 语句中，b 的值就是最终加密后的值，往上找，第 1125 和 1126 行 `var e = b;` `b = F(F(b) + c);`，把明文密码赋值给 b，c 为验证码，经过 F 这个函数的处理后得到加密值，继续跟进 F 函数：

可以看到其实就是经过以下函数的处理：

```
function d(a) {
    return n(e(o(m(a + "{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}")), 32))
}

```

这个函数中，又包含 n, e, o, m 函数，这里不再每个函数去剥离，直接将这个函数往下所有单个字母的函数 copy 下来本地调试即可。

### 完整代码

GitHub 关注 K 哥爬虫，持续分享爬虫相关代码！欢迎 star ！https://github.com/kgepachong/

**以下只演示部分关键代码，不能直接运行！**完整代码仓库地址：https://github.com/kgepachong/crawler/

#### JavaScript 加密关键代码架构

```
function getEncryptedPassword(a, b, c) {
    // a: 用户名, b: 密码, c: 验证码
    function d(a) {
        return n(e(o(m(a + "{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}")), 32))
    }

    function e(a, b) {}

    function f(a, b, c, d, e, f) {}

    function g(a, b, c, d, e, g, h) {}

    function h(a, b, c, d, e, g, h) {}

    function i(a, b, c, d, e, g, h) {}

    function j(a, b, c, d, e, g, h) {}

    function k(a, b)  {}

    function l(a, b)  {}

    function m(a)  {}

    function n(a)  {}

    function o(a)  {}

    c.hex_md5 = d
    b = d(d(b) + c);
    return b
}

// 测试样例
// console.log(getEncryptedPassword('123123', '1231234', '6798'))

```

#### Python 登录关键代码

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import random

import execjs
import requests
from PIL import Image


index_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
login_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
ver_code_url = '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler'
headers = {
    'Referer': '脱敏处理，完整代码关注 GitHub：https://github.com/kgepachong/crawler',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
session = requests.session()


def get_verification_code():
    response = session.get(url=ver_code_url, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image.show()
    code = input('请输入验证码: ')
    return code


def get_encrypted_password(username, password, code):
    with open('encrypt.js', 'r', encoding='utf-8') as f:
        js = f.read()
    encrypted_password = execjs.compile(js).call('getEncryptedPassword', username, password, code)
    return encrypted_password


def login(username, encrypted_password, code):
    timestamp = str(round(time.time() * 1000))
    jsonp = ''
    for _ in range(20):
        jsonp += str(random.randint(0, 9))
    jsonp = 'jQuery' + jsonp + '_' + timestamp
    params = {
        'jsonp': jsonp,
        'protocol': ' http:',
        'loginIndex': index_url,
        'j_mmrm': username,
        'j_mcmm': encrypted_password,
        'j_valcode': code,
        '_': timestamp
    }
    response = session.get(url=login_url, params=params, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    code = get_verification_code()
    encrypted_pwd = get_encrypted_password(username, password, code)
    login(username, encrypted_pwd, code)


if __name__ == '__main__':
    main()

```
