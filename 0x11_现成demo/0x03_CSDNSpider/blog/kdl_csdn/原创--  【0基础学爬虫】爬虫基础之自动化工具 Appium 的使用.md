# 原创
：  【0基础学爬虫】爬虫基础之自动化工具 Appium 的使用

# 【0基础学爬虫】爬虫基础之自动化工具 Appium 的使用

大数据时代，各行各业对数据采集的需求日益增多，网络爬虫的运用也更为广泛，越来越多的人开始学习网络爬虫这项技术，K哥爬虫此前已经推出不少爬虫进阶、逆向相关文章，为实现从易到难全方位覆盖，特设【0基础学爬虫】专栏，帮助小白快速入门爬虫，本期为自动化工具 Appium 的使用。

### 概述

自动化测试在测试过程中节约了时间，还能避免包括人为因素造成的测试错误和遗漏。可供选择的自动化测试工具有很多，一些是开源的，而有些则较贵。但是自动化工具无论新旧，都有各自的特点。关于 Android 自动化测试，工具有很多，比如 Robotium、MonkeyRunner、Ronaorex、Appium、Robotium、uiautomator2 等等，本文将对 Appium 做详细讲解。

### Appium 的使用

#### 介绍

Appium 是一个开源测试自动化框架，用于原生、 混合和移动 Web 应用程序。它使用 WebDriver 协议驱动 iOS、Android 和 Windows 应用程序。 支持多种语言：支持多种语言，java、python、php、Ruby等等 ， Appium 与 Selenium 类似，是一个跨语言的自动化框架，可与任何测试框架结合使用。使开发者能够使用其熟悉的语言编写测试脚本，架构如下:

#### 工作流程

1. appium server 开启 4723 端口，监听客户端的连接，首先我们要开启 appium 服务，即 appium server，默认监听 4723 端口。4723 端口专门和脚本打交道，基于 WebDriver 协议。接下来脚本与 appium server 的通信实际上是一个 HTTP request 请求给 appium server，在请求的 body 中，会以 WebDriver Wire 协议规定的 JSON 格式的字符串来告诉 appium 服务我们希望设备接下来做什么事情；
1. appium 客户端（测试脚本）基于 Json wire protocol 发送设备信息给 appium server，请求创建 session。其中设备信息放在 desired capabilities 中，包括系统平台，版本，应用等信息（详细介绍参考 App 控件定位）。session 用于保存设备配置信息；
1. appium server 创建 session id 并返回给 client，作为客户端请求的唯一标识，那么，将测试设备信息告知之后，是不是就可以开始进行测试了呢？答案是：NO。这里又要引入一个名词：session。session 就是一个会话，在 webdriver/appium，你的所有工作永远都是在 session start 后才可以进行的。client 请求创建 1 个 session，在该 session 中通过 http 向 appium server 发送请求，appium server 解析请求，完成相应操作并返回 response；
1. 开启 bootstrap socket 服务器：appium 在初始化时将中间件 Bootstrap.jar 推送到设备，bootstrap 是 uiautomator 的测试脚本，继承于 UiautomatorTestCase。手机端通过该脚本监听端口 4724，appium server 作为 socket-client 端通过 4724 端口将请求发送给 socket 服务器（bootstrap.jar），然后 bootstrap 将 appium 命令转换成 uiautomator 命令。

#### 安装

##### jdk 安装

Appium 需要 Java8 以上的开发环境：

> 
官网下载：https://www.oracle.com/java/technologies/downloads/?er=221886#java8


Java downloads。有 3 种系统，Linux，macOS，Windows 自行选择即可，按照默认路径安装即可：

配置环境变量（“我的电脑”右键菜单 —-&gt; 属性 —-&gt; 高级 —-&gt; 环境变量 —-&gt; 系统变量 —&gt; 新建）：
