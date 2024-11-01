# 原创
：  19-1 burpsuite模块介绍之repeater

# 19-1 burpsuite模块介绍之repeater

#### 导语 

repeater是一个用于手动操作和发送个别HTTP请求的简单工具，它可以帮助您分析应用程序的响应。您可以使用repeater从Burp Suite的任何位置发送内部请求，然后修改请求并发送。通过这种方式，您可以测试和调试应用程序，并对请求和响应进行精细控制。

|repeater名称|Repeater
|------
|repeater作用|用于手动操作和发送个别HTTP请求，分析应用程序的响应
|update content-length|自动更新消息头中的Content-Length
|Unpack gzip /deflate|解压压缩文件
|Follow redirections|跳转控制，可以选择从不跳转、同一站点内跳转、Scope内跳转、始终跳转四种之一
|Process cookie in redirections|跳转的同时是否处理Cookie
|View|主要控制Repeater面板整个布局

#### <img alt="" height="439" src="https://img-blog.csdnimg.cn/direct/d8a4e815889d4a82b9e55b86376086e8.png" width="846"/>使用示例

这个模块没啥好说的操作都很简单，可以参考我之前的这篇文章：[tomcat PUT任意方法写文件-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/134768512)

重这里看起就行了（虽然这个模块的操作简单但是这个是最常用的模块）
