# 原创
：  APP攻防--ADB基础

# APP攻防--ADB基础

### 进入app包

先使用 `adb devices`查看链接状态<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2c3ef5223ce004e12316cc20491b1736.jpeg"/><br/> 手机连接成功的<br/> `adb shell`<br/> 获取到手机的一个shell<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/23053dc7893e7f96eb9ad20b1e84a977.jpeg"/><br/> 此时想进入app包时没有权限的，APP包一般在data/data/下。没有执行权限，如图<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4c38200df19055bdd10fef84f4f69279.jpeg"/><br/> Permission denied 权限被拒绝<br/> 此时需要手机root，root后输入·<br/> `su root`<br/> 然后命令就能执行了<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fd53d41408972f0c869025ca246a8c46.jpeg"/><br/> 找到要测试的APP包,cd进去<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b559bdcf7400b00c2ce43b6c56084689.jpeg"/><br/> 查看文件下的权限，如果有x权限那么久是危险的。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6af007ff11b9d21a4001986b1bf3f0c0.jpeg"/>

### 常见的adb命令

连接设备或模拟器：

`adb connect &lt;设备IP地址&gt;:&lt;端口号&gt;`<br/> `adb devices`<br/> 安装应用程序：

`adb install &lt;应用程序.apk&gt;`<br/> 卸载应用程序：

`adb uninstall &lt;应用程序包名&gt;`<br/> 启动应用程序：

`adb shell am start -n &lt;应用程序包名&gt;/&lt;Activity名称&gt;`

停止应用程序：

`adb shell am force-stop &lt;应用程序包名&gt;`<br/> 查看设备日志：

`adb logcat`<br/> 拉取文件从设备到计算机：

`adb pull &lt;设备路径&gt; &lt;本地路径&gt;`<br/> 推送文件从计算机到设备：

`adb push &lt;本地文件路径&gt; &lt;设备路径&gt;`<br/> 获取应用程序包名和Activity名称：

`adb shell dumpsys package &lt;应用程序.apk&gt;`<br/> 查看设备信息：

`adb shell getprop`<br/> 列出设备上的所有应用程序包名：

`adb shell pm list packages`<br/> 查看设备上的所有应用程序的权限信息：

`adb shell pm list permissions -d -g`
