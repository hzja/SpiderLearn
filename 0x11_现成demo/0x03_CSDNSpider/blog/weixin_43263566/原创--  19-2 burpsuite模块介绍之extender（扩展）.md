# 原创
：  19-2 burpsuite模块介绍之extender（扩展）

# 19-2 burpsuite模块介绍之extender（扩展）

#### extender 

        Burp提供了对第三方拓展插件的支持，使用户能够编写自定义插件或从插件商店中安装拓展插件。这些Burp扩展程序可以以多种方式定制Burp的行为，包括修改HTTP请求和响应、自定义UI、添加自定义扫描程序检查以及访问关键的运行时信息，如代理历史记录、目标站点地图和扫描程序问题。

**扩展商店**

**也可以在其他地方下载插件到本地后在加载**

这里以伪造IP的插件burpFakeIP为例** **（插件作者与原文：[GitHub - TheKingOfDuck/burpFakeIP: 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件](https://github.com/TheKingOfDuck/burpFakeIP)）

**插件下载：**[https://github.com/TheKingOfDuck/burpFakeIP/releases/download/1.0/fakeIP.jar](https://github.com/TheKingOfDuck/burpFakeIP/releases/download/1.0/fakeIP.jar)

因为github是外国的网站在国内访问速度有
