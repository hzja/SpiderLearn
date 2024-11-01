# 原创
：  【WebGoat安装错误合集】WebGoat8.2.2每一步出现的错误整理，最后附带正确的安装教程

# 【WebGoat安装错误合集】WebGoat8.2.2每一步出现的错误整理，最后附带正确的安装教程

**目录**

[一、错误重现：](#%E4%B8%80%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[1.1、错误一：](#1.1%E3%80%81%E9%94%99%E8%AF%AF%E4%B8%80%EF%BC%9A)

[1.2、错误二：](#1.2%E3%80%81%E9%94%99%E8%AF%AF%E4%BA%8C%EF%BC%9A)

[1.3、错误三：端口被占用](#1.3%E3%80%81%E9%94%99%E8%AF%AF%E4%B8%89%EF%BC%9A%E7%AB%AF%E5%8F%A3%E8%A2%AB%E5%8D%A0%E7%94%A8)

[二、问题解决：](#%E4%BA%8C%E3%80%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[2.1、解决一：](#2.1%E3%80%81%E8%A7%A3%E5%86%B3%E4%B8%80%EF%BC%9A)

[ JDK准备：](#%C2%A0JDK%E5%87%86%E5%A4%87%EF%BC%9A)

[2.1.1、方法一：手工配置](#2.1.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E6%89%8B%E5%B7%A5%E9%85%8D%E7%BD%AE)

[2.1.2、方法二：工具配置](#2.1.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%B7%A5%E5%85%B7%E9%85%8D%E7%BD%AE)

[2.1.3、JDK的配置：](#2.1.3%E3%80%81JDK%E7%9A%84%E9%85%8D%E7%BD%AE%EF%BC%9A)

[2.1.4、JRE的生成：](#2.1.4%E3%80%81JRE%E7%9A%84%E7%94%9F%E6%88%90%EF%BC%9A)

[2.2、解决二：](#2.2%E3%80%81%E8%A7%A3%E5%86%B3%E4%BA%8C%EF%BC%9A)

[2.3、解决三：](#2.3%E3%80%81%E8%A7%A3%E5%86%B3%E4%B8%89%EF%BC%9A)

[三、安装+启动：](#%E4%B8%89%E3%80%81%E5%AE%89%E8%A3%85%2B%E5%90%AF%E5%8A%A8%EF%BC%9A)

[3.1、第一步：下载源文件](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%B8%8B%E8%BD%BD%E6%BA%90%E6%96%87%E4%BB%B6)

[3.2、第二步：准备配置文件](#3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%87%86%E5%A4%87%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)

[3.3、第三步：启动](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8)

[四、owaspbwa集成了WebGoat](#%E5%9B%9B%E3%80%81owaspbwa%E9%9B%86%E6%88%90%E4%BA%86WebGoat)

[五、Linux](#%E4%BA%94%E3%80%81Linux)

---


（你走过的路，是我填过的坑） 

---


## 一、错误重现：

### 1.1、错误一：

> 
 #提示版本不够
#Exception in thread "main" java.lang.UnsupportedClassVersionError: org/owasp/webgoat/StartWebGoat has been compiled by a more recent version of the Java Runtime (class file version 59.0), this version of the Java Runtime only recognizes class file versions up to 52.0



### 1.2、错误二：

> 
现在常见的WebGoat安装，在搬来搬去的过程中，就给搞漏了一些步骤
下图是我在找到的存在错误的步骤（误人子弟）
错哪请看后面



### 1.3、错误三：端口被占用

> 
这个好解决



---


<img alt="" src="https://img-blog.csdnimg.cn/242ed2d3ced14495bd2f9e6edc5c9157.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_12,color_FFFFFF,t_70,g_se,x_16"/> 

## 二、问题解决：

### 2.1、解决一：

错误二也会产生错误一的提示

> 
<h4> JDK准备：</h4>
V8需要jdk11及以上
（图方便就直接软件管家下载吧）

 <img alt="" height="478" src="https://img-blog.csdnimg.cn/b67e97031b92445bbb00b4d836a57938.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_15,color_FFFFFF,t_70,g_se,x_16" width="629"/>


> 
<h4>2.1.1、方法一：手工配置</h4>
[3分钟复制粘贴配置java环境变量，验证配置是否成功，java文件运行方法<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/123482726?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165028109016780261979271%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165028109016780261979271&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123482726.nonecase&amp;utm_term=jdk&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123482726?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165028109016780261979271%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165028109016780261979271&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123482726.nonecase&amp;utm_term=jdk&amp;spm=1018.2226.3001.4450)
<h4>2.1.2、方法二：工具配置</h4>
[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501)

<h4>2.1.3、JDK的配置：</h4>
[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501)
<h4>2.1.4、JRE的生成：</h4>
[【高版本JRE生成】JRE版本不够，生成JRE失败，高版本JDK生成JRE过程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124262183?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124262183?spm=1001.2014.3001.5501)


#### 2.1.2、方法二：工具配置

#### 2.1.4、JRE的生成：

### 2.2、解决二：

> 
 需要的环境有：jdk、Webgoat和Webwolf
所以要下载这2个
（不然也会报错误一）
[Releases · WebGoat/WebGoat (github.com)<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://github.com/WebGoat/WebGoat/releases](https://github.com/WebGoat/WebGoat/releases)（顺路带一个链接吧）



### 2.3、解决三：

> 
 关闭自己占用8080端口的进程



 或者直接关掉自己的Apache



---


 

## 三、安装+启动：

### 3.1、第一步：下载源文件

> 
在解决二中，下载2个jar文件（还有2个另外文件是源代码，看自己情况下）


### 3.2、第二步：准备配置文件

> 
在解决一中，jdk11及以上


### 3.3、第三步：启动

> 
进入到目录下（根据自己文件的目录而定）



启动
java -jar webgoat-server-8.2.2.jar


浏览器输入
[http://127.0.0.1:8080/WebGoat](http://127.0.0.1:8080/WebGoat)

 
去注册新用户

 
随便注册<img alt="" height="836" src="https://img-blog.csdnimg.cn/5ba12d2fd0914f1fb496a97c42d6efd8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

登录进去了

 



---


## 四、owaspbwa集成了WebGoat

> 
 下载owaspbwa
 里面集成了WebGoat


这里有WebGoat



 不过这个版本有一点低（最新版已经V8了）<img alt="" height="710" src="https://img-blog.csdnimg.cn/5e1264b6496c423ab9838cdb2a05fd9e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1136"/>


---


## 五、Linux

> 
 
 发现最新的Linux自带的就是jdk11（nice）
使用Linux就不需要再配置jdk了

这个就差不多了

