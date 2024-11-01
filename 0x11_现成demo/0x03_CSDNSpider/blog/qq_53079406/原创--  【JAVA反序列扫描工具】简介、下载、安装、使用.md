# 原创
：  【JAVA反序列扫描工具】简介、下载、安装、使用

# 【JAVA反序列扫描工具】简介、下载、安装、使用

**目录**

[一、Java Deserialization Scanner](#%E4%B8%80%E3%80%81Java%20Deserialization%20Scanner)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、组成：](#1.2%E3%80%81%E7%BB%84%E6%88%90%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.1、方法一：BAPP store](#2.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9ABAPP%20store)

[2.2、 方法二：GitHub](#2.2%E3%80%81%20%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9AGitHub)

[三、配置](#%E4%B8%89%E3%80%81%E9%85%8D%E7%BD%AE)

[3.1、 插件的配置](#3.1%E3%80%81%20%E6%8F%92%E4%BB%B6%E7%9A%84%E9%85%8D%E7%BD%AE)

[3.2、ysoserial准备](#3.2%E3%80%81ysoserial%E5%87%86%E5%A4%87)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、截取发送到插件](#4.1%E3%80%81%E6%88%AA%E5%8F%96%E5%8F%91%E9%80%81%E5%88%B0%E6%8F%92%E4%BB%B6)

[4.2、 配置扫描](#4.2%E3%80%81%20%E9%85%8D%E7%BD%AE%E6%89%AB%E6%8F%8F)

[4.3、分析结果](#4.3%E3%80%81%E5%88%86%E6%9E%90%E7%BB%93%E6%9E%9C)

---


 （scan！）

---


## 一、Java Deserialization Scanner

> 
<h3>1.1、简介：</h3>
Java Deserialization Scanner是一个Burp套件插件，用于检测和利用Java Deserialization漏洞。
<h3>1.2、组成：</h3>
与Burp Suite Active and Massive Scanner集成
手动测试仪，用于检测自定义插入点上的Java Deserialization漏洞
利用，允许积极利用Frohoff Ysoserial积极利用Java Deserialization vullnerabilies


### 1.2、组成：

---


## 二、下载：

> 
<h3>2.1、方法一：BAPP store</h3>
BAPP store里面直接下载Java Deserialization Scanner
找到后，点击右边的安装



> 
<h3>2.2、 方法二：GitHub</h3>
GitHub下载：
[federicodotta/Java-Deserialization-Scanner: All-in-one plugin for Burp Suite for the detection and the exploitation of Java deserialization vulnerabilities (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://github.com/federicodotta/Java-Deserialization-Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner)<img alt="" height="709" src="https://img-blog.csdnimg.cn/2be47c2c5ee74fe68e8dc61c90d0ff11.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


---


## 三、配置

> 
<h3>3.1、 插件的配置</h3>
最后添加进去即可




 安装好后需要配置 ysoserial(是java反序列化漏洞payload生成器) 的路径
（可以直接填上文件名，我试了可以）




> 
<h3>3.2、ysoserial准备</h3>
源码下载地址（GitHub）

[angelwhu/ysoserial: A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. (github.com)<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://github.com/angelwhu/ysoserial](https://github.com/angelwhu/ysoserial)

[frohoff/ysoserial: A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://github.com/frohoff/ysoserial](https://github.com/frohoff/ysoserial)

ysoserial需要编译打包成.jar文件（Maven，Gradle都可打包）
可以自己从github上下载最新源码，编译打包（也可编制IDEA，直接在终端操作）
[【Maven使用】IDEA使用Maven进行文件打包+命令含义+错误分析<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://blog.csdn.net/qq_53079406/article/details/124322125?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124322125?spm=1001.2014.3001.5501)[【Gradle】问题解析+下载安装+环境配置+验证安装<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://blog.csdn.net/qq_53079406/article/details/124312186?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124312186?spm=1001.2014.3001.5501)
或者使用老版的ysoserial.jar
链接：https://pan.baidu.com/s/18q2ruwCFGI1vMvl9j7lT3w?pwd=hj12 <br/> 提取码：hj12




---


 

## 四、使用方法：

> 
<h3>4.1、截取发送到插件</h3>
send request to DS-Manual testing
发送到插件中


点击插件查看数据包



> 
<h3>4.2、 配置扫描</h3>
选择被序列化的部分，
并Set insertion port（设置插入部分）
还可以选择sleep等测试的方式

最下面方框是选择，选中的数据是什么编码 


> 
<h3>4.3、分析结果</h3>
在右边会出现测试的结果
我这右边都是NOT vulnerable（不脆弱）


如果扫描到有漏洞的话，
后面接的就会是：**Potentially VULNERABLE！！！**




根据在Manual testing结果中检出出有漏洞使用对应的命令
或者修改添加计算器等其他工具



