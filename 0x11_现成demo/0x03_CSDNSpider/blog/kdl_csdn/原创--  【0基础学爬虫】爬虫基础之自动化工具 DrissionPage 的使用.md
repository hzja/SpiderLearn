# 原创
：  【0基础学爬虫】爬虫基础之自动化工具 DrissionPage 的使用

# 【0基础学爬虫】爬虫基础之自动化工具 DrissionPage 的使用

### 概述

前三期文章中已经介绍到了 Selenium 与 Playwright 、Pyppeteer 的使用方法，它们的功能都非常强大。而本期要讲的 DrissionPage 更为独特，强大，而且使用更为方便，目前检测少，强烈推荐！！！

这里推荐观看十一姐 B 站 DrissionPage 系列视频，很详细：

> 
合集·爬虫自动化 DrissionPage 实战案例：<br/> https://space.bilibili.com/308704191/channel/collectiondetail?sid=1947582


DrissionPage 相关资料：

> 
官方文档：https://www.drissionpage.cn<br/> Drissionpage “姊妹库”：https://gitee.com/haiyang0726/SaossionPage


### DrissionPage 的使用

#### 介绍

DrissionPage 是一个基于 python 的网页自动化工具。它既能控制浏览器，也能收发数据包，还能把两者合而为一。可兼顾浏览器自动化的便利性和 requests 的高效率。它功能强大，内置无数人性化设计和便捷功能。它的语法简洁而优雅，代码量少，对新手友好。

#### 特性

##### 强大的自研内核

本库采用全自研的内核，内置了无数实用功能，对常用功能作了整合和优化，对比 selenium，有以下优点：

##### 亮点功能

除了以上优点，本库还内置了无数人性化设计。

#### 安装升级

```
# 安装
pip install DrissionPage
 
# 升级最新稳定版
pip install DrissionPage --upgrade
 
# 指定版本升级
pip install DrissionPage==4.0.0b17

```

CentOS 请参考这篇文章：

> 
linux 部署说明：https://blog.csdn.net/sinat_39327967/article/details/132181129


Ubuntu 请参考这篇文章：

> 
DrissionPage 在 Ubuntu Linux 的使用：https://zhuanlan.zhihu.com/p/674687748


#### 使用

##### 访问网页

```
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().set_paths(browser_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
# 1、设置无头模式：co.headless(True)
# 2、设置无痕模式：co.incognito(True)
# 3、设置访客模式：co.set_argument('--guest')
# 4、设置请求头user-agent：co.set_user_agent()
# 5、设置指定端口号：co.set_local_port(7890)
# 6、设置代理：co.set_proxy('http://localhost:1080')
page = ChromiumPage(co)

page.get('https://gitee.com/login', retry=3, timeout=15, interval=2)

# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')
# 输入对文本框输入账号
ele.input('您的账号')
# 定位到密码文本框并输入密码
page.ele('#user_password').input('您的密码')
# 点击登录按钮
page.ele('@value=登 录').click()

```

**获取浏览器路径的方法**:

该方法用于跳转到一个网址。当连接失败时，程序会进行重试：

##### 获取查找元素

本库提供一套简洁易用的语法，用于快速定位元素，并且内置等待功能、支持链式查找，减少了代码的复杂性。

同时也兼容 css selector、xpath、selenium 原生的 loc 元组。

定位元素大致分为三种方法：

```
# 输入
page.ele('xpath://input[@id="bindMobileFree"]').input("123456789")
# 点击
page.ele('x://span[@class="getYZM_btn"]').click()

```

```
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://gitee.com/explore')

# 获取包含“全部推荐项目”文本的 ul 元素
ul_ele = page.ele('tag:ul@@text():全部推荐项目')  

# 获取该 ul 元素下所有 a 元素
titles = ul_ele.eles('tag:a')  

# 遍历列表，打印每个 a 元素的文本
for i in titles:  
    print(i.text)

```

```
foot = page.ele('#footer-left')  # 用 id 查找元素
first_col = foot.ele('css:&gt;div')  # 使用 css selector 在元素的下级中查找元素（第一个）
lnk = first_col.ele('text:命令学')  # 使用文本内容查找元素
text = lnk.text  # 获取元素文本
href = lnk.attr('href')  # 获取元素属性值

print(text, href, '\n')

# 简洁模式串联查找
text = page('@id:footer-left')('css:&gt;div')('text:命令学').text
print(text)

```

##### 等待

##### 监听网络数据

```
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听

page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包(部分url)
for _ in range(5):
    page('@rel=next').click()  # 点击下一页
    res = page.listen.wait()  # 等待并获取一个数据包
    print(res.url)  # 输出数据包url
    print(res.response.headers)  # 输出响应头
    print(res.response.statusText)  # 输出响应状态码
    print(res.response.body)  # 输出响应内容

```

```
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
page.get('https://gitee.com/explore/all')  # 访问网址

i = 0
for packet in page.listen.steps():
    print(packet.url)  # 打印数据包url
    page('@rel=next').click()  # 点击下一页
    i += 1
    if i == 5:
        break

```

##### 动作链

```
```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.actions.move_to('#kw').click().type('DrissionPage')
page.actions.move_to('#su').click()
```

*   📌 使用新对象

```python
from DrissionPage import ChromiumPage
from DrissionPage.common import Actions

page = ChromiumPage()
ac = Actions(page)
page.get('https://www.baidu.com')
ac.move_to('#kw').click().type('DrissionPage')
ac.move_to('#su').click()
```

*   📌 操作方式

```python
ac.move_to(ele).click().type('some text')
```

```

```
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.actions.move_to((300, 500)).hold().move(300).release()

```

##### 标签页操作

[📌](https://www.drissionpage.cn/ChromiumPage/tab#-tabs_count) **注意**：可以对多标签页操作, 即可实现并发自动化。

##### 截图和录像

✅️️ 页面截图

```
# 对整页截图并保存
page.get_screenshot(path='tmp', name='pic.jpg', full_page=True)

```

✅️️ 元素截图

```
img = page('tag:img')
img.get_screenshot()
bytes_str = img.get_screenshot(as_bytes='png')  # 返回截图二进制文本

```

✅️️ 页面录像

```
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.screencast.set_save_path('video')  # 设置视频存放路径
page.screencast.set_mode.video_mode()  # 设置录制
page.screencast.start()  # 开始录制
page.wait(3)
page.screencast.stop()  # 停止录制

```

##### 执行 JS 语句

```
page.run_js(f'localStorage.setItem("__user_token.v3",`{token}`)')

page.run_js(f'localStorage.setItem("__user_info",`{token}`)')

cookies_set = ""
cookies_set += f'document.cookie=`__user_token.v3={token}; path=/;domain=i.shengcaiyoushu.com;`;'

page.run_js(cookies_set)

```

##### 反检测

在 Selenium、Playwright 、Playwright 的使用中，我们讲到了自动化工具容易被网站检测，也提供了一些绕过检测的方案。这里我们介绍一下 DrissionPage 的反检测方案。

以 https://bot.sannysoft.com 为例，我们分别测试正常模式与无头模式下的检测结果：

可以发现，我们没有做任何反检测的操作，都不会被检测到，就连使用无头模式也只有 userAgent 有问题，不过我们 co.set_user_agent() 设置一下就可以了，虽然这些只是最基本的检测机制，但也够用了。

### 总结

DrissionPage 语法简洁，使用方便，底层基于 CDP 协议，拥有较强的反检测机制，目前不需要做任何反检测的操作就可以绕过国内外绝大多数的网站自动化检测，包含但不限于 (xx 验证码、某数、5s)。 还有很多强大的功能这里没法一一展示，强烈推荐！
