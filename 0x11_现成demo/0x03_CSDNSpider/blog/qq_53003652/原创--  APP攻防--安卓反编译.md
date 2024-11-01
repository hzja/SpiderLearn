# 原创
：  APP攻防--安卓反编译

# APP攻防--安卓反编译

### 前言：

在最近的工作中一直在接触APP测试，给大家分享下个人的一些经验，水平有限，大佬勿喷。<br/> 首先APP攻防是要学会反编译的，大概有如下几种方式。

### dex2jar

dex2jar是一个安卓反编译的工具，可以吧.dex文件转换成.jar文件，可以帮助我们分析具体的代码。<br/> 项目地址：<br/> [https://github.com/pxb1988/dex2jar/releases](https://github.com/pxb1988/dex2jar/releases)<br/> 使用：<br/> 把测试apk后缀改为zip解压，可以得到.dex文件<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c6b6166923f0f094f2c954b913022989.jpeg"/><br/> 把.dex文件单独解压出来<br/> 使用命令：<br/> `d2j-dex2jar &lt;.dex路径&gt; -o &lt;输出路径+名称.jar&gt;`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a19b90def186d45dc0086280b28002d4.jpeg"/><br/> 输出路径下就会有.jar文件<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/474bc1106caa517a82acf63d9a826a22.jpeg"/>

### jd-gui

得到.jar文件该怎么打开呢，就是jd-gui这个工具<br/> 项目地址：<br/> [https://github.com/java-decompiler/jd-gui/releases](https://github.com/java-decompiler/jd-gui/releases)<br/> jd-gui可以以图形化的界面让开发者测试.jar文件代码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/71da913e332020514f5fa03627f8de19.jpeg"/><br/> 此时可以测试代码是否做过混淆。混淆过的代码类文件和方法都是以a,b,c…之类命名的

### Android killer

一代神器Android killer，不多说直接上图<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9f82307750d63abe99c927a5a01238d8.jpeg"/><br/> Android killer是一款集成了adb，dex2jar等安卓测试工具为一体的图形化工具，对新人十分友好。<br/> 项目地址：<br/> [https://github.com/liaojack8/AndroidKiller](https://github.com/liaojack8/AndroidKiller)

### Apktool

apktool也可以进行反编译，并且还能进行回编译<br/> 项目地址：<br/> [https://ibotpeaches.github.io/Apktool/](https://ibotpeaches.github.io/Apktool/)<br/> 使用命令：<br/> `java -jar apktool.jar d xxx.apk`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9e85de4446472f9e6baae8881acca849.jpeg"/><br/> 反编译后的内容会在当前目录下生成。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ad8d8a84458e5103498849019499d8b4.jpeg"/><br/> 当然，除了这些还有其他方式，比如ApkBurster等，我日常使用的还是这些工具，祝师傅们早日成为APP攻防高手
