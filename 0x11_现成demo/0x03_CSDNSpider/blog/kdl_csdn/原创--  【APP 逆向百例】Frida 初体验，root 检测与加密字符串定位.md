# 原创
：  【APP 逆向百例】Frida 初体验，root 检测与加密字符串定位

# 【APP 逆向百例】Frida 初体验，root 检测与加密字符串定位

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

### 安装 ADB

adb（Android Debug Bridge）即安卓调试桥，安装后可以在电脑上与手机进行交互，Android Studio 等工具里面会自带 adb，有时候我们并不想下载这么大的工具，所以这里介绍一下 Android SDK Platform-Tools，它是 Android SDK 的一个组件，它包括与 Android 平台交互的工具，主要是 adb 和 fastboot，官方下载地址：https://developer.android.com/studio/releases/platform-tools ，下载完成后将该目录添加到环境变量，USB 连接手机，手机上设置允许 USB 调试，使用命令 `adb version` 可查看版本信息，`adb devices` 可以查看当前连接的设备，如下图所示：

### 安装 Frida

Frida 是一款基于 Python + JavaScript 的 Hook 与调试框架，首先电脑端使用命令 `pip install frida-tools` 安装 frida 模块（此命令默认会安装最新版的 frida 和 frida-tools，如），然后下载 frida-server，下载地址：https://github.com/frida/frida/releases

frida-server 要根据你电脑端安装的 frida 版本和手机的 CPU 架构来选择对应的，使用命令 `frida --version` 可以查看 frida 版本，使用命令 `adb shell` 进入手机，输入 `getprop ro.product.cpu.abi` 查看 CPU 架构，如下图所示，我这里 frida 是 15.2.2 版本，手机 CPU 为 arm64，所以我下载的是 `frida-server-15.2.2-android-arm64.xz`。

某些 Android 低版本使用高版本 frida 可能有问题，遇到问题可尝试降低 frida 版本来解决。

将下载好的 frida-server 使用 `adb push` 命令传到手机的 `/data/local/tmp/` 目录下，并给予 777 读、写、执行的权限，然后直接运行 frida-server，正常不会有任何输出，当然也可以使用 &amp; 等方式让其在后台运行。

然后另开一个 cmd 使用命令 `frida-ps -U ` 可查看手机进程，有输出则正常。

### 逆向分析

使用 `adb install` 命令安装 UnCrackable-Level1.apk，打开该 APP，会检测到 root，出现 `Root detected!` 的提示，如下图所示：

使用 JEB、JADX、GDA 等工具反编译 apk，直接搜索关键字 `Root detected!` 即可定位到检测的地方：

可以看到图中有三个检测方法 `c.a()`、`c.b()`、`c.c()`，其中一个返回为真，则弹出 `Root detected!`，然后前面还有一个 `onClick` 方法，如果点击 OK 按钮，则触发 `System.exit(0);`，即退出 APP，先点进三个检测方法看看：

`a()` 方法通过检测 Android 系统环境变量中是否有 su 文件来判断是否被 root；

`b()` 方法通过检测 `Build.TAGS` 中是否包含字符串 `test-keys` 来判断是否被 root；

`c()` 方法通过检测指定路径下是否包含指定的文件来判断是否被 root。

所以我们这里就有多种过掉检测的方法：

方法一：Hook 三个检测方法，让它们都返回 false，不再执行后续的 a 方法，就不会退出 APP 了：

```
Java.perform(
    function(){
        console.log("[*] Hook begin")
        var vantagePoint = Java.use("sg.vantagepoint.a.c")
        vantagePoint.a.implementation = function(){
            console.log("[*] Hook vantagepoint.a.c.a")
            this.a();
            return false;
        }
        vantagePoint.b.implementation = function(){
            console.log("[*] Hook vantagepoint.a.c.b")
            this.b();
            return false;
        }
        vantagePoint.c.implementation = function(){
            console.log("[*] Hook vantagepoint.a.c.c")
            this.c();
            return false;
        }
    }
)

```

方法二：Hook `a()` 方法，置空，什么都不做，不弹出对话框，也不退出 APP：

```
Java.perform(
    function(){
        console.log("[*] Hook begin")
        var mainActivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");
        mainActivity.a.implementation = function(){
            console.log("[*] Hook mainActivity.a")
        }
    }
)

```

方法三：Hook `onClick()` 方法，点击 OK 后不让其退出 APP，注意这里是内部类的 Hook 写法：

```
Java.perform(
    function(){
        console.log("[*] Hook begin")
        var mainActivity$1 = Java.use("sg.vantagepoint.uncrackable1.MainActivity$1");
        mainActivity$1.onClick.implementation = function(){
            console.log("[*] Hook mainActivity$1.onClick")
        }
    }
)

```

方法四：Hook `System.exit()` 方法，点击 OK 后不让其退出 APP：

```
Java.perform(
    function(){
        console.log("[*] Hook begin")
        var javaSystem = Java.use("java.lang.System");
        javaSystem.exit.implementation = function(){
            console.log("[*] Hook system.exit")
        }
    }
)

```

root 检测过掉之后，APP 还要输入一个字符串，输入错误会提示 `That's not it. Try again.`，如下图所示：

分析 Java 代码，有一个 `if-else` 判断，obj 为输入的字符串，`a.a(obj)` 判断为真，就表示输入正确。

跟到 `a.a()` 方法，可以看到 `bArr` 是内置的字符串，通过 `equals()` 方法比较输入的 `str` 是否和 `bArr` 相等：

`bArr` 的值，主要经过 `sg.vantagepoint.a.a.a()` 方法处理后得到，继续跟进去可以发现是 AES 加密算法：

这里就可以直接 Hook `sg.vantagepoint.a.a.a()`，直接拿到加密后的值，也就是我们要的正确字符串，由于这里返回的是 ASCII 码，所以我们还需要在 JavaScript 代码中使用 `String.fromCharCode()` 将其转换成正常字符，Hook 代码如下：

```
Java.perform(
    function(){
        var cryptoAES = Java.use("sg.vantagepoint.a.a");
        cryptoAES.a.implementation = function(bArr, bArr2){
            console.log("[*] Hook cryptoAES")
            var secret = "";
            var decryptValue = this.a(bArr, bArr2);
            console.log("[*] DecryptValue:", decryptValue)
            for (var i=0; i &lt; decryptValue.length; i++){
              secret += String.fromCharCode(decryptValue[i]);
            }
            console.log("[*] Secret:", secret)
            return decryptValue;
        }
    }
)

```

运行 Hook 脚本有两种方式，一是结合 Python 使用，二是直接通过 frida 命令使用脚本，注入 Hook 代码也有个时机问题，有时候需要在 APP 启动就开始 Hook，有时候可以等 APP 启动加载完毕了再 Hook，本例中，过 root 检测的时候，如果采用第一、二种方法，即 Hook 三个检测方法或者 a 方法，那就需要在 APP 启动的时候就 Hook，如果采用第三、四种方法，即 Hook `onClick()` 或者 `System.exit()` 方法，那么等 APP 启动了再 Hook 也可以。

#### 结合 Python 使用

首先来看一下结合 Python 怎么使用，JavaScript 代码如下（frida-hook.js）：

```
/* ==================================
# @Time    : 2022-08-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: frida-hook.js
# @Software: PyCharm
# ================================== */


Java.perform(
    function(){
        console.log("[*] Hook begin")

        // 方法一：Hook 三个检测方法，让它们都返回 false，不再执行后续的 a 方法，就不会退出 APP 了
        // var vantagePoint = Java.use("sg.vantagepoint.a.c")
        // vantagePoint.a.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.a")
        //     this.a();
        //     return false;
        // }
        // vantagePoint.b.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.b")
        //     this.b();
        //     return false;
        // }
        // vantagePoint.c.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.c")
        //     this.c();
        //     return false;
        // }

        // 方法二：Hook a() 方法，置空，什么都不做，不弹出对话框，也不退出 APP
        // var mainActivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");
        // mainActivity.a.implementation = function(){
        //    console.log("[*] Hook mainActivity.a")
        // }

        // 方法三：Hook onClick() 方法，点击 OK 后不让其退出 APP
        // var mainActivity$1 = Java.use("sg.vantagepoint.uncrackable1.MainActivity$1");
        // mainActivity$1.onClick.implementation = function(){
        //     console.log("[*] Hook mainActivity$1.onClick")
        // }

        // 方法四：Hook System.exit 方法，点击 OK 后不让其退出 APP
        var javaSystem = Java.use("java.lang.System");
        javaSystem.exit.implementation = function(){
            console.log("[*] Hook system.exit")
        }

        var cryptoAES = Java.use("sg.vantagepoint.a.a");
        cryptoAES.a.implementation = function(bArr, bArr2){
            console.log("[*] Hook cryptoAES")
            var secret = "";
            var decryptValue = this.a(bArr, bArr2);
            console.log("[*] DecryptValue:", decryptValue)
            for (var i=0; i &lt; decryptValue.length; i++){
              secret += String.fromCharCode(decryptValue[i]);
            }
            console.log("[*] Secret:", secret)
            return decryptValue;
        }
    }
)

```

Python 代码如下（frida-hook.py）：

```
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2022-08-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: frida-hook.py
# @Software: PyCharm
# ==================================


import sys
import frida


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


with open("./frida-hook.js", "r", encoding="utf-8") as fp:
    hook_string = fp.read()

# 方式一：attach 模式，已经启动的 APP
process = frida.get_usb_device(-1).attach("Uncrackable1")
script = process.create_script(hook_string)
script.on("message", on_message)
script.load()
sys.stdin.read()

# 方式二，spawn 模式，重启 APP
# device = frida.get_usb_device(-1)
# pid = device.spawn(["owasp.mstg.uncrackable1"])
# process = device.attach(pid)
# script = process.create_script(hook_string)
# script.on("message", on_message)
# script.load()
# device.resume(pid)
# sys.stdin.read()

```

Python 代码中，attach 模式 Hook 已经存在的进程，spawn 模式会重启 APP，启动一个新的进程并挂起，在启动的同时注入 frida 代码，适用于在进程启动前的一些 Hook，attach 模式传入的是 APP 名称，spawn 模式传入的是 APP 包名，查看 APP 名称和包名的方法有很多，这里介绍两个 frida 命令，`frida-ps -Uai`：列出安装的程序，`frida-ps -Ua`：列出正在运行中的程序，如下图所示，本例中 `Uncrackable1` 就是 APP 名称，`owasp.mstg.uncrackable1` 就是包名：

运行 Python 代码，注意手机端也要启动 frida-server，过掉 root 检测后，先随便输入字符串，点击 VERIFY 就会 Hook 到正确的字符串为 `I want to believe`，再次输入正确的字符串，即可验证成功。

#### frida 命令

不使用 Python，也可以直接使用 frida 命令来实现，和前面 Python 一样也有两种模式，同样的一个是 APP 名一个是包名：

`frida -U Uncrackable1 -l .\frida-hook.js`：attach 模式，APP 启动后注入 frida 代码；

`frida -U -f owasp.mstg.uncrackable1 -l .\frida-hook.js --no-pause`：spawn 模式，重启 APP，启动的同时注入 frida 代码。

至此，我们完美绕过了 root 检测，并成功找到了正确的字符串。
