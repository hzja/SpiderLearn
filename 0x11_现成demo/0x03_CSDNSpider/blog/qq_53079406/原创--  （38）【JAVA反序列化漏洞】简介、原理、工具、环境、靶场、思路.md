# 原创
：  （38）【JAVA反序列化漏洞】简介、原理、工具、环境、靶场、思路

# （38）【JAVA反序列化漏洞】简介、原理、工具、环境、靶场、思路

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、原理：](#%E4%BA%8C%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[2.1、Java对象：](#2.1%E3%80%81Java%E5%AF%B9%E8%B1%A1%EF%BC%9A)

[2.2、Java 序列化：](#2.2%E3%80%81Java%20%E5%BA%8F%E5%88%97%E5%8C%96%EF%BC%9A)

[2.3、Java 反序列化：](#2.3%E3%80%81Java%20%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%EF%BC%9A)

[三、函数：](#%E4%B8%89%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[四、工具：](#%E5%9B%9B%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[4.1、ysoserial 0.0.4版](#4.1%E3%80%81ysoserial%200.0.4%E7%89%88)

[4.2、 payload生成器](#4.2%E3%80%81%20payload%E7%94%9F%E6%88%90%E5%99%A8)

[4.2.1、介绍： ](#4.2.1%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A%C2%A0)

[4.3、提示：](#4.3%E3%80%81%E6%8F%90%E7%A4%BA%EF%BC%9A)

[五、准备：](#%E4%BA%94%E3%80%81%E5%87%86%E5%A4%87%EF%BC%9A)

[5.1、WebGoat](#5.1%E3%80%81WebGoat)

[5.2、 环境变量的配置：](#5.2%E3%80%81%20%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E7%9A%84%E9%85%8D%E7%BD%AE%EF%BC%9A)

[5.2.1、方法一：手工配置](#5.2.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E6%89%8B%E5%B7%A5%E9%85%8D%E7%BD%AE)

[5.2.2、方法二：工具配置](#5.2.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%B7%A5%E5%85%B7%E9%85%8D%E7%BD%AE)

[5.2.3、JDK的配置：](#5.2.3%E3%80%81JDK%E7%9A%84%E9%85%8D%E7%BD%AE%EF%BC%9A)

[5.2.4、JRE的生成：](#5.2.4%E3%80%81JRE%E7%9A%84%E7%94%9F%E6%88%90%EF%BC%9A)

[5.3、错误+安装](#5.3%E3%80%81%E9%94%99%E8%AF%AF%2B%E5%AE%89%E8%A3%85)

[六、WebGoat](#%E5%85%AD%E3%80%81WebGoat)

[6.1、分析：](#6.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[6.2、插件](#6.2%E3%80%81%E6%8F%92%E4%BB%B6)

[ 6.2.1、Java Deserialization Scanner](#%C2%A06.2.1%E3%80%81Java%20Deserialization%20Scanner)

[6.3、漏洞利用：](#6.3%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%9A)

[6.3.1、大体思路：](#6.3.1%E3%80%81%E5%A4%A7%E4%BD%93%E6%80%9D%E8%B7%AF%EF%BC%9A)

[6.3.2、具体思路](#6.3.2%E3%80%81%E5%85%B7%E4%BD%93%E6%80%9D%E8%B7%AF)

---


        <img alt="" src="https://img-blog.csdnimg.cn/ff017706a9f44356949fae661a35e15e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_12,color_FFFFFF,t_70,g_se,x_16"/>

（大家都在学习） 

---


## 一、简介：

> 
序列化也就是将数据拆成一小块小块保存到文件中（每块设置编号），反序列化就是重现组合起来


> 
（1）序列化就是将数据转化成一种可逆的字符串（利于存储或者传输），字符串还原原来结构的过程叫做反序列化
（2）序列化后，方便保存和传输（保留成员变量，不保留函数方法）

（3）数据（对象）--------序列化----------&gt;字符串-----------反序列化--------&gt;数据（对象）


---


## 二、原理：

> 
<h3>2.1、Java对象：</h3>
①多种方式来创建对象，没被回收都可复用此对象（存在于JVM中的堆heap内存中），当JVM处于运行状态，对象就存在；反之，对象就不存在。
②在真实的环境中，通过序列化，实现在JVM中的对象和字节数组流之间转换，实现将这些对象持久化保存下来，在需要的时候再使用。


> 
<h3>2.2、Java 序列化：</h3>
完整性+可传递性
①将对象转换为字符串等字节数组流过程（保存属性状态，不保存对象中的方法），从而实现对象持久化，以便传输（可移植性）或保存在本地文件中，将序列化对象写入文件之后，可从文件中读取，并且进行反序列化。


> 
<h3>2.3、Java 反序列化：</h3>
将一个对象的字节序列（字符串）中保存的对象状态及描述信息，通过反序列化，恢复成 Java 对象的过程（重建）


---


## 三、函数：

> 
序列化：ObjectOutputStream类–&gt; writeObject()（写入）
反序列化：ObjectInputStream类 --&gt;readObject() （读取）


> 
Serializable（接口） ：（序列化与反序列化的类必须使用）一个标志性接口，标识在 JVM 中进行序列化，为该类自动生成一个序列化版本号。
serialVersionUID（类属性）：序列化版本号（默认提供），给 JVM 区别同名类。
transient（关键字）：不希望特定属性参与序列化，使用这个关键字标注该属性。


---


 

## 四、工具：

> 
<h3>4.1、ysoserial 0.0.4版</h3>
（现在最新的是0.0.6）
链接：https://pan.baidu.com/s/18q2ruwCFGI1vMvl9j7lT3w?pwd=hj12 <br/> 提取码：hj12


> 
<h3>4.2、 payload生成器</h3>
[angelwhu/ysoserial: A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. (github.com)<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://github.com/angelwhu/ysoserial](https://github.com/angelwhu/ysoserial)

[frohoff/ysoserial: A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. (github.com)<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://github.com/frohoff/ysoserial](https://github.com/frohoff/ysoserial)
<h4>4.2.1、介绍： </h4>
ysoserial payload是创建了一个URLStreamHandler的子类：SilentURLStreamHandler
SilentURLStreamHandler重写了getHostAddress(URL u)，屏蔽了返回值，因此在生成payload的时候、也就是序列化的时候，不会触发dns查询。



> 
<h3>4.3、提示：</h3>
 上上述文件需要经过Maven编译，或者Gradle编译（Gradle更简单，以后应该会超过Maven）成.jar文件，后才能使用
[【Maven使用】IDEA使用Maven进行文件打包+命令含义+错误分析<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124322125?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124322125?spm=1001.2014.3001.5501)
[【Gradle】问题解析+下载安装+环境配置+验证安装<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124312186?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_53079406/article/details/124312186?spm=1001.2014.3001.5502)
IntelliJ IDEA中也包含Maven、Gradle
（里面也可以配置自己的maven、Gradle）
官网：
[IntelliJ IDEA：JetBrains 功能强大、符合人体工程学的 Java IDE<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://www.jetbrains.com/zh-cn/idea/](https://www.jetbrains.com/zh-cn/idea/)<img alt="" height="514" src="https://img-blog.csdnimg.cn/9f5a545a6b6d4bdabeac9f320318a0a4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

激活： 
网上有很多激活脚本（容易找到）


---


## 五、准备：

> 
<h3>5.1、WebGoat</h3>
 链接：[https://github.com/WebGoat/WebGoat/releases](https://github.com/WebGoat/WebGoat/releases)


> 
<h3>5.2、 环境变量的配置：</h3>
<h4>5.2.1、方法一：手工配置</h4>
[3分钟复制粘贴配置java环境变量，验证配置是否成功，java文件运行方法<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/123482726?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165028109016780261979271%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165028109016780261979271&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123482726.nonecase&amp;utm_term=jdk&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123482726?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165028109016780261979271%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165028109016780261979271&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123482726.nonecase&amp;utm_term=jdk&amp;spm=1018.2226.3001.4450)
<h4>5.2.2、方法二：工具配置</h4>
[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501)

<h4>5.2.3、JDK的配置：</h4>
[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501)
<h4>5.2.4、JRE的生成：</h4>
[【高版本JRE生成】JRE版本不够，生成JRE失败，高版本JDK生成JRE过程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124262183?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124262183?spm=1001.2014.3001.5501)


#### 5.2.2、方法二：工具配置

#### 5.2.4、JRE的生成：

> 
<h3>5.3、错误+安装</h3>

全面的错误解决
[【WebGoat安装错误合集】WebGoat8.2.2每一步出现的错误整理，最后附带正确的安装教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124297362?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124297362?spm=1001.2014.3001.5501)


---


 

## 六、WebGoat

> 
<h3>6.1、分析：</h3>
下面的输入框存在反序列化的漏洞，我们要生成含有可执行代码的序列化字符串，在输入框提交，进行反序列化，从而执行我们构造的代码，让页面延迟5s就完成题目了
以 rO0AB 开头， JAVA 序列化 base64 加密的。
以 aced 开头， java 序列化的 16 进制。



解码看看
无任何有用信息



> 
<h3>6.2、插件</h3>
<h4> 6.2.1、Java Deserialization Scanner</h4>
是一个Burp套件插件，用于检测和利用Java Deserialization（java反序列化）漏洞
[【JAVA反序列扫描工具】简介、下载、安装、使用<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124336323?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124336323?spm=1001.2014.3001.5501)这个工具的扫描，也得依靠我们对他进行配置文件ysoserial.jar


> 
<h3>6.3、漏洞利用：</h3>
（由于僵持了好多天，我要去补充亿多点知识点去了，先把思路放这里）
<h4>6.3.1、大体思路：</h4>
构造恶意语句-----&gt;序列化------&gt;进行编码------&gt;最终的payload------&gt;提交进去执行


> 
<h4>6.3.2、具体思路</h4>
（前提：知道源码）
**第一步：**
提交，抓包，找到数据包中包含的目录（可能是发往反序列化函数的地方）
**第二步：**
在源码里搜索，找到反序列化的位置
**第三步：**
分析解码函数（即它的编码方法）及其接口
**第四步：**
查看ysoserial支持的插件，对应查找WebGoat是否安装了对应的.jar包（名含有core，与ysoserial支持的版本一致），并复制到ysoserial目录下
**第五步：**
根据这个.jar包，利用ysoserial生成反序列化漏洞的payload，执行calc.exe，将payload保存在token.bin文件中
**第六步：**
采用python脚本对payload进行base64编码（根据所使用的序列化编码方法）
**第七步：**
在反序列化框提交构造的序列化字符串（触发反序列化）


（前提：不知道源码）
可以就要通过其他方法去分析到编码方式、含有的.jar包
接口测试、回显数据分析……

