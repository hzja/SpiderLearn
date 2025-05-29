# 原创
：  通杀无限 debugger，目前只有 1% 的人知道！

# 通杀无限 debugger，目前只有 1% 的人知道！


          摘要生成于
          [ C知道](https://ai.csdn.net?utm_source=cknow_pc_ai_abstract) 
          ，由 DeepSeek-R1 满血版支持，
          [ 前往体验 &gt;](https://ai.csdn.net?utm_source=cknow_pc_ai_abstract)

### 前言

相信很多小伙伴在进行 web 逆向的时候，都遇到过无限 debugger。最简单的方法，在 debugger 位置，点击行号，右键 Never pause here，永远不在此处断下即可。但是这种方法就妄想通杀，显然是不大可能的，不然这种防护岂不是弄出来骗自己的。

现在很多网站，这样处理是无法绕过的。例如常规的，可能存在格式化检测，内存爆破，禁用右键，要么就会接着进入到下一个 debugger 中，甚至出现网页卡死的情况等等。这些可能就会挡住一部分爬虫 er。当然，对于大部分人来说，这些都不是问题，八仙过海，祭出各种法宝，检测点改写、删除，文件替换，Hook 掉 constructor 或 setTimeout 等等，K哥之前也写过相关文章：

但终究是提升了咱采集数据的成本，那有什么方法能够一劳永逸的解决掉这个痛点，直接舒舒服服的开始调试呢？

### 分析

最近吾爱破解上有两篇好文，讲解了无限 debugger 的通杀解决方案：

简单来说，一个是从浏览器方面解决，一个是浏览器直接帮你解决。

Firefox 于 2023 年 12 月 19 日更新的 121.0 版本，使得小小无限 debugger，隔壁阿姨来了，都能上手一把梭！

我们来看看 Firefox 新版本到底更新了啥，为广大爬虫 er 带来了福音，[Firefox 更新日志](https://www.mozilla.org/en-US/firefox/121.0/releasenotes/?utm_source=firefox-browser&amp;utm_medium=firefox-desktop&amp;utm_campaign=whatsnew)，新功能很多，通过阅览，我们注意到了这个：

> 
https://www.mozilla.org/en-US/firefox/121.0/releasenotes/?utm_source=firefox-browser&amp;utm_medium=firefox-desktop&amp;utm_campaign=whatsnew


> 
The Firefox Debugger now includes a new feature: an option to disable the keyword on the current page. This feature is accessible via a new checkbox in the Breakpoints side panel labeled , located next to the existing checkbox. By default, this option is enabled, meaning that the debugger statements are active unless manually disabled.
`debugger;``Pause on debugger statement``Pause on exceptions`
翻译：
Firefox Debugger 现在有一个新功能：一个选项可以禁用当前页面的关键字。这个功能可以通过断点侧面板中一个新的复选框来访问， 它位于现有复选框的旁边。默认情况下， 这个选项是启用的， 这意味着除非手动禁用， 否则调试器语句是活动的。


以前在开发者人员工具 Source（调试器）侧边栏的 Breakpoints（断点）中只有一个 Pause on exceptions（异常处暂停）选项，Firefox 更新到 121.0 之后，多了一个 Pause on debugger statement（在调试器语句上暂停）选项，这个新选项是默认勾选的，即不禁用，理论上，取消勾选之后，就能绕过无限 debugger，真的假的？我们来测试一下。

### 实践

首先下载个浏览器：[Firefox 火狐浏览器官方最新下载](https://www.firefox.com.cn/)，下载下来的版本为 116.0，并非最新版，需要去设置中更新到 121.0 版本：

接下来，我们找几个网站测试一下。

##### 1. 瑞数 4 代

正常情况：

取消勾选 Pause on debugger statement：

##### 2. 瑞数 vmp

正常情况：

取消勾选 Pause on debugger statement：

##### 3. 17track

正常情况：

取消勾选 Pause on debugger statement：

### 总结

根据实际测试，取消勾选 Pause on debugger statement 确实能直接绕过无限 debugger！大伙可以去多找些网站试试。当然，如果碰上 2、3 这种有格式化检测的网站，会有些卡顿，不过这也极大的降低了复杂度！希望 Chrome、Edge 等浏览器也尽快实现这种好用的功能，甚至更为完善~
