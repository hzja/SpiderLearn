# 原创
：  APP攻防--签名&&组件&&权限

# APP攻防--签名&amp;&amp;组件&amp;&amp;权限

### 前言

上文说到了反编译的方式，这期就深入到APP内部，即客户端安全。

### 安装包签名

在Android操作系统中，每个应用程序（APP）安装包（APK）都必须经过数字签名，以确保应用的完整性和来源验证。

#### apksigner

apksigner是Android-SDK里面的一个工具，SDK的安装方式大家可自行搜索。apksigner可以检测安装包的签名。<br/> 命令：<br/> `.\apksigner.bat verify -v --print-certs .\test.apk`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ae6664e6283f8025dae781743e5fc029.jpeg"/><br/> 可以看到这个APP只进行了v1签名，这是不安全的。如果只使用v1签名方案，那么它就容易受到安卓5.0-8.0上的Janus漏洞（CVE-2017-13156）的攻击。在安卓5.0-7.0上运行的使用了v1签名方案的应用程序，以及同时使用了v2/v3签名方案的应用程序也同样存在漏洞。

#### apk-info

这个工具是图形化的，不仅仅能看到签名，还有组件等详细信息<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3c6dac96655d937c1b59d3f81500d0ba.jpeg"/><br/> 工具地址：<br/> [https://pan.baidu.com/s/1soEX-D_k54k9b07hu1UWlw?pwd=cy7t](https://pan.baidu.com/s/1soEX-D_k54k9b07hu1UWlw?pwd=cy7t)<br/> 提取码：cy7t

### 组件

#### 四大组件

Android应用程序的四大组件是构成Android应用的核心元素，它们允许应用程序执行不同的任务和功能。这四大组件包括：

**Activity（活动）**：Activity是Android应用的用户界面组件，通常代表应用的一个屏幕或一个用户与应用程序进行交互的界面。每个Activity都是一个独立的UI界面，可以包括用户界面元素，如按钮、文本框和图像。应用程序通常由多个Activity组成，它们通过Activity之间的切换来实现不同的用户交互。

**Service（服务）**：Service是一种在后台运行的组件，它执行长时间运行的操作，而不需要与用户界面进行交互。服务通常用于执行一些后台任务，如音乐播放、文件下载、数据同步等，以便不会阻塞用户界面。服务可以在后台运行，即使用户切换到其他应用或锁定屏幕。

**Broadcast Receiver（广播接收器）**：广播接收器是一种用于监听和响应系统广播消息或应用内自定义广播的组件。它可以在应用内或跨应用之间传递消息，以触发相应的操作。例如，应用可以注册广播接收器来监听手机电池电量变化、网络连接状态、来电通知等事件。

**Content Provider（内容提供者）**：内容提供者是用于管理应用内数据共享的组件。它允许不同应用程序之间共享数据，并提供了标准的接口来访问和操作数据。内容提供者通常用于访问应用的数据库或共享数据，以确保数据的安全和一致性。

这四大组件共同构成了Android应用的基础架构，使应用能够实现各种不同的功能和交互。开发者可以根据应用的需求组合和使用这些组件，以创建丰富的Android应用程序。<br/> 大家可以看一下前辈们的文章<br/> [安卓四大组件知识点总结](https://www.cnblogs.com/hwb04160011/p/13960517.html)

#### ADB

##### **ADB是什么**

ADB项目下载地址：[https://adbshell.com/downloads](https://adbshell.com/downloads)<br/> ADB（Android Debug Bridge）是Android开发工具中的一个命令行工具，用于与Android设备通信和管理。顾名思义，安卓调试桥，它提供了一种方式，开发者可以在开发、调试和测试Android应用程序时与设备或模拟器进行交互。

ADB的主要功能包括：

安装和卸载应用程序：ADB允许开发者将应用程序安装到设备或模拟器上，也可以卸载已安装的应用程序。

文件传输：通过ADB，可以在设备和计算机之间传输文件，包括复制文件到设备或从设备中获取文件。

调试和日志记录：开发者可以使用ADB来启用和管理应用程序的调试模式，以便进行调试。还可以使用ADB来捕获设备上的日志信息，有助于排查问题。

Shell访问：通过ADB，开发者可以访问设备的Unix shell，执行命令和查看设备的状态。

端口转发：ADB允许将本地计算机上的端口与设备上的端口进行转发，从而实现本地和设备之间的通信。

屏幕截图和录屏：ADB可以用来获取设备屏幕的截图，也可以用于录制设备屏幕的视频。

设备信息和状态查询：通过ADB，可以获取设备的信息，如设备型号、操作系统版本和唯一标识符等。

ADB是Android开发的重要工具之一，它使开发者能够更轻松地进行应用程序开发、测试和调试，以确保应用在不同设备上正常运行。ADB通常与Android SDK一起提供，安装Android Studio时会自动包括ADB。

##### 常用命令

```
adb connect 127.0.0.1:62001 链接夜神模拟器
adb devices 查看连接
adb logcat  打印
logcatadb install  安装，覆盖安装是-r
adb uninstall卸载
adb push   推送本地文件至 Android 设备
adb pull    推送Android文件至本地
adb shell mount -o remount rw / 修改系统读写权限
adb root  获得root权限
adb kill-server  重启

```

也可以将手机通过数据线连接电脑，直接adb连接手机。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f3a47a240d0fa36ef5a1936b49b9fdf4.jpeg"/>

#### drozer

##### drozer是什么

Drozer是一种用于Android应用渗透测试和安全评估的开源工具。它提供了一组功能，使安全研究人员和渗透测试人员能够分析、评估和测试Android应用程序的安全性。Drozer旨在帮助识别和利用应用程序中的漏洞，并提供有关潜在威胁的信息。

Drozer的一些主要功能和用途包括：

应用安全分析：Drozer允许安全专家对应用程序进行深入的安全分析，包括查找应用程序中的漏洞、弱点和潜在的安全问题。

应用权限检查：它可以检查应用程序的权限请求，并提供关于应用程序可能过度请求权限或滥用权限的信息。

漏洞利用：Drozer包括一些模块，用于利用已知的Android漏洞，以测试应用程序的弱点。

数据泄漏测试：它可以帮助识别应用程序中的数据泄漏问题，包括敏感数据泄露。

反编译和逆向工程：Drozer允许用户分析应用程序的代码，进行逆向工程，并查看应用程序的内部结构。

交互式漏洞利用：它提供了一个交互式Shell，允许用户执行命令和进行漏洞测试。

Drozer是一个功能强大的工具，但需要谨慎使用，因为在未经授权的环境中使用它可能会违反法律。通常，Drozer被用于合法的安全评估和渗透测试，以帮助开发者和组织识别和解决Android应用程序中的安全问题。安全专家通常会在受控环境中使用它，以测试应用程序的安全性。

##### 使用准备

drozer分为两部分，手机上要安装drozer Agent为服务端，电脑端安装console是控制台。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/33fd32eba1f56e4a1b8ac6a9bac0073c.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/017aba8327b36ab8813059cdc286c4c3.jpeg"/><br/> drozer使用必须是python2.7环境。<br/> adb连接手机：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b00f29b45b8fa9976af1694f6a6a1cf3.jpeg"/><br/> 然后进行端口转发：<br/> `adb forward tcp:31415 tcp:31415`<br/> `drozer console connect`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7746783a94e9316f429f457d190dd85b.jpeg"/><br/> 出现这个页面就代表连接成功。<br/> 在手机上打开drozer Agent，打开这个开关<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4800342f48a15080e83eca66a0aae77c.jpeg"/>

#### drozer基本命令

列出所有APP安装包<br/> `run app.package.list`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/84f072869e39f8b7e1911ee064653b85.jpeg"/><br/> 查看包详情<br/> `run app.package.info -a com.xxxxxx.sieve`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8a0a81fadd5ad13b9dc1fa77c3081292.jpeg"/><br/> 列出组件攻击面<br/> `run app.package.attacksurface com.xxxxxx.sieve`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1401bebc6f188e4b06617d7acd6480ca.jpeg"/><br/> 查看activity组件信息<br/> `run app.activity.info -a com.xxxxxx.sieve`<br/> 查看broadcast组件信息<br/> `run app.broadcast.info -a com.xxxxxx.sieve`<br/> 查看service组件信息<br/> `run app.service.info -a com.xxxxxx.sieve`<br/> 查看Content Provider组件信息<br/> `run app.provider.info -a com.xxxxxx.sieve`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b4ad8678ecb40fb5f5d864ddc4390460.jpeg"/><br/> 对应每种组件下有各种漏洞检测方式，大家如果感兴趣可以参考这位大佬的文章。<br/> [drozer漏洞检测](https://blog.csdn.net/qq_42067124/article/details/129803628)

### 权限

#### AllowBackup

android:allowBackup 是一个在 Android 应用的 AndroidManifest.xml 文件中的权限设置，用于控制应用数据是否可以被备份。这个权限通常设置在 元素内，其值可以是 true 或 false。

如果 android:allowBackup=“true”：这意味着应用的数据可以被系统备份工具（如Android的云备份服务）备份。这通常适用于用户应用，以便他们可以在设备之间或在重新安装应用时还原数据。

如果 android:allowBackup=“false”：这表示应用的数据不应该被备份。这通常适用于包含敏感信息的应用，如金融应用或安全敏感的应用，以确保用户数据不会被泄露。

在渗透测试中，android:allowBackup 的设置可能具有安全风险。如果一个应用允许备份，攻击者可以尝试访问和还原备份数据，这可能导致敏感数据泄露。因此，渗透测试人员可能会检查应用程序的 android:allowBackup 设置，以确保它们符合安全最佳实践。

如果发现应用的 android:allowBackup 设置不正确，可能需要提出安全建议或漏洞报告，以帮助应用开发者改进安全性。此外，测试人员还可以检查应用的其他数据存储和加密方法，以确保数据在备份和存储期间的安全性。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/233b158433301929adcb5e4621da618e.jpeg"/><br/> 如果被设置成了true，可以用 adb backup 将应用数据导出<br/> 然后用abe 工具将导出的数据解密为 tar 压缩包文件，这样可以得到一些敏感数据。

#### Debuggable

android:debuggable 是一个用于 Android 应用的 AndroidManifest.xml 文件中的权限设置，用于指示应用是否可以进行调试。这个权限通常设置在 元素内，其值可以是 true 或 false。

如果 android:debuggable=“true”：这表示应用是可调试的，允许开发者使用调试工具来分析应用的运行时行为。这对于开发和调试应用程序非常有用。

如果 android:debuggable=“false”：这表示应用不应该被调试。在正式发布的应用中，通常应将 android:debuggable 设置为 false 以防止未经授权的调试操作。

在渗透测试中，android:debuggable 的设置可能具有重要的安全风险。如果应用被设置为可调试，那么攻击者可能会利用这个权限来获取敏感信息，如应用内部的数据、逻辑和密钥。因此，渗透测试人员通常会检查应用程序的 android:debuggable 设置，以确保在正式发布的应用中它被设置为 false。

如果发现应用的 android:debuggable 设置为 true，这可能是一个潜在的安全漏洞，需要向应用开发者报告，以确保在发布时设置为 false，以增强安全性。确保应用不容易被未经授权的调试是一项重要的安全措施，以防止敏感数据泄露和应用的滥用。
