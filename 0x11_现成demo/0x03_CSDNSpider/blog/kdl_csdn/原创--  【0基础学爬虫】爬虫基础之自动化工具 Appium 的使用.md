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
1. appium server 开启 4723 端口，监听客户端的连接，首先我们要开启 appium 服务，即 appium server，默认监听 4723 端口。4723 端口专门和脚本打交道，基于 WebDriver 协议。接下来脚本与 appium server 的通信实际上是一个 HTTP request 请求给 appium server，在请求的 body 中，会以 WebDriver Wire 协议规定的 JSON 格式的字符串来告诉 appium 服务我们希望设备接下来做什么事情；1. appium 客户端（测试脚本）基于 Json wire protocol 发送设备信息给 appium server，请求创建 session。其中设备信息放在 desired capabilities 中，包括系统平台，版本，应用等信息（详细介绍参考 App 控件定位）。session 用于保存设备配置信息；1. appium server 创建 session id 并返回给 client，作为客户端请求的唯一标识，那么，将测试设备信息告知之后，是不是就可以开始进行测试了呢？答案是：NO。这里又要引入一个名词：session。session 就是一个会话，在 webdriver/appium，你的所有工作永远都是在 session start 后才可以进行的。client 请求创建 1 个 session，在该 session 中通过 http 向 appium server 发送请求，appium server 解析请求，完成相应操作并返回 response；1. 开启 bootstrap socket 服务器：appium 在初始化时将中间件 Bootstrap.jar 推送到设备，bootstrap 是 uiautomator 的测试脚本，继承于 UiautomatorTestCase。手机端通过该脚本监听端口 4724，appium server 作为 socket-client 端通过 4724 端口将请求发送给 socket 服务器（bootstrap.jar），然后 bootstrap 将 appium 命令转换成 uiautomator 命令。
#### 安装

##### jdk 安装

Appium 需要 Java8 以上的开发环境：

> 
官网下载：https://www.oracle.com/java/technologies/downloads/?er=221886#java8


Java downloads。有 3 种系统，Linux，macOS，Windows 自行选择即可，按照默认路径安装即可：

配置环境变量（“我的电脑”右键菜单 —-&gt; 属性 —-&gt; 高级 —-&gt; 环境变量 —-&gt; 系统变量 —&gt; 新建）：

path 变量，编辑添加：

cmd输入 java -version 如果有版本号输出，那么证明安装成功。

##### 安装 Android SDK

Android SDK 是谷歌提供的 Android 开发工具包，在进行安卓开发的时候，往往需要通过引入工具包来调用安卓原生的 API ，安装方式有俩种，第一种可以通过安装 android studio 开发工具：

> 
https://developer.android.com/


其内部集成了 android-sdk ，或者直接下载 Android SDK：

> 
https://dl.google.com/android/android-sdk_r24.4.1-windows.zip


下载完成后，解压出来：

然后双击 SDK Manager.exe 安装 sdk tools、sdk plaform-tools、sdk build-tools：

配置环境变量（“我的电脑”右键菜单 —-&gt; 属性 —-&gt; 高级 —-&gt; 环境变量 —-&gt; 系统变量 —&gt; 新建）：

path 变量，编辑添加：

验证 Android SDK 是否安装成功，输入 :adb version /adb 能成功输出内容，即为成功。

##### 安装 Appium

> 
下载地址：https://bitbucket.org/appium/appium.app/downloads/?tab=downloads


下载完毕，将 Appium\node_modules.bin 的路径添加到系统变量 path 中 。以上工作全部做完以后，cmd 运行 appium-doctor 进行环境检测，看看 appium 运行所需的环境是不是全部安装完毕，运行结果如下，证明我们安装成功：

##### Appium-windows 可视化平台安装

Appium-windows 是 windows 桌面应用的自动化测试方案的必要组成部分，是 win 桌面应用 UI 自动化的最佳选择：

> 
下载地址：https://github.com/appium/appium-desktop/releases/tag/v1.15.1


根据不同的操作系统来选择适合自己的进行下载：

打开我们安装好的软件，选择 Edit Config：

进去以后看我们俩个选择是否有内容，如果默认有内容那么证明我们的环境变量已经配好：

##### Appium-Python-Client 安装
<li> 通过源文件安装，解压到指定目录， 运行 `python setup.py install` 进行安装：
<blockquote>
下载地址：https://pypi.org/project/Appium-Python-Client/
</blockquote> </li>1.  直接通过 `pip install Appium-Python-Client` 或 `pip3 install Appium-Python-Client` 进行安装。 
安装完成后，我们即可通过编写 Python 代码来实现自动化的测试。

### Appium 实战测试

经过上面的操作，我们已经将所有必须的的环境都已经装好，我们使用官方提供的测试 app 来进行测试：

> 
下载地址：https://github.com/appium/android-apidemos/releases/tag/v3.1.0


下载以后我们将 app 安装到手机或者真机，命令为：

```
adb install ApiDemos-debug.apk

```

#### 启动 Appium

在安装完毕以后，我们启动 Appium ， host 和 port 默认的即可，单击 start 启动：

出现下图以上提示，即为启动成功，端口默认为 4723，在此窗口将会一直显示 appium serve 的运行日志：

#### 移动设备/模拟器连接电脑

将真机/模拟器通过 USB 设线连接电脑，命令行输入 `adb devices`，如果输出以下提示，则我们的移动设备连接成功：

```
$ adb devices
List of devices attached
FA77D0303724          device

```

这里我们的设备就与电脑连接成功了。

### 测试脚本编写

启动成功以后，我们可以看见可以通过左侧快速定位：

同时还可以通过设置点击等事件生成多种语言的测试代码：

app 测试代码如下：

```
from appium import webdriver

class TestApidemos:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'emulator-5554',
            'appPackage': 'io.appium.android.apis',
            'appActivity': '.ApiDemos',
            'automationName': 'Uiautomator2',
            'newCommandTimeout': 3000
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_appium(self):
        elem = self.driver.find_element_by_xpath('//*[@text="App"]')
        elem.click()
        Alarm_exist = self.driver.find_element_by_xpath('//*[@text="Alarm"]').is_displayed()
        assert Alarm_exist == True

if __name__ == "__main__":
    test = TestApidemos()
    try:
        test.setup()
        test.test_appium()
        print("测试通过")
    except AssertionError:
        print("测试失败")
    finally:
        test.teardown()

```

#### desired_caps 参数获取

appPackage 与 appActivity 获取方法：

```
adb shell dumpsys activity activities | find "mFocusedActivity"

```

deviceName 获取方法：

```
adb devices

```

platformVersion 获取方法：

```
adb shell getprop ro.build.version.release

```

也可以使用 pytest 来测试：

```
pytest test_apidemos.py::TestApidemos::test_appium

```

### **总结**

Appium 是一个开源的跨平台移动应用自动化测试工具，用于测试原生、混合和移动 Web 应用程序。 APP上面的测试逐渐的流行起来。而作为 APP 自动化测试中最常用的框架就是 Appium。Appium 是一个开源、跨平台的测试框架。可以用来测试原生及混合的移动端应用！
