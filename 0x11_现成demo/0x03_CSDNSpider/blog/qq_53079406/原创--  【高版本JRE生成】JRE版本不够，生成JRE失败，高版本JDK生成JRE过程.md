# 原创
：  【高版本JRE生成】JRE版本不够，生成JRE失败，高版本JDK生成JRE过程

# 【高版本JRE生成】JRE版本不够，生成JRE失败，高版本JDK生成JRE过程

**目录**

[错误重现：](#%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[ 错误一：Java Runtime版本不够](#%C2%A0%E9%94%99%E8%AF%AF%E4%B8%80%EF%BC%9AJava%20Runtime%E7%89%88%E6%9C%AC%E4%B8%8D%E5%A4%9F)

[ 错误二：生成JRE失败](#%C2%A0%E9%94%99%E8%AF%AF%E4%BA%8C%EF%BC%9A%E7%94%9F%E6%88%90JRE%E5%A4%B1%E8%B4%A5)

[原因分析：](#%E5%8E%9F%E5%9B%A0%E5%88%86%E6%9E%90%EF%BC%9A)

[ 分析一：](#%C2%A0%E5%88%86%E6%9E%90%E4%B8%80%EF%BC%9A)

[ 分析二：](#%C2%A0%E5%88%86%E6%9E%90%E4%BA%8C%EF%BC%9A)

[问题解决：](#%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[第一步：管理员终端](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%AE%A1%E7%90%86%E5%91%98%E7%BB%88%E7%AB%AF)

[第二步：进入文件](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%BF%9B%E5%85%A5%E6%96%87%E4%BB%B6)

[ 第三步：生成](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90)

[推荐：](#%E6%8E%A8%E8%8D%90%EF%BC%9A)

---


（问题定点突破，终将有所获） 

---


## 错误重现：

> 
<h3> 错误一：Java Runtime版本不够</h3>
#但是我使用jdk11，jdk16，都提示jre不满足（要升级版本）：
#Exception in thread "main" java.lang.UnsupportedClassVersionError: org/owasp/webgoat/StartWebGoat has been compiled by a more recent version of the Java Runtime (class file version 59.0), this version of the Java Runtime only recognizes class file versions up to 52.0



> 
<h3> 错误二：生成JRE失败</h3>
#在JDK11以后的版本中生成JRE失败

 #错误: C:\Program Files\Java\jdk-11.0.2\jre
#并且从报错中无法得到很有效的信息


---


## 原因分析：

> 
<h3> 分析一：</h3>
#结合我自己的经验和百度发现
#在之前的 jdk1.8 版本乃至以下压缩包下载解压后直接运行会生成 jdk、jre 两个目录文件
#Java11 之后，只有 jdk 目录文件生成，没有 jre 目录文件，这时我们可以通过命令行方式手动生成 jre。



 #jdk11的目录里，可以看到目录里也没有生成 jre 目录


#查看版本java -version

 Java(TM) SE Runtime Environment 18.9 (build 11.0.2+9-LTS)<br/> Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.2+9-LTS, mixed mode)
Java（TM）SE运行时环境18.9（构建11.0.2 + 9-LTS）<br/> Java Hotspot（TM）64位服务器VM 18.9（构建11.0.2 + 9-LT，混合模式）


> 
<h3> 分析二：</h3>
#错误: C:\Program Files\Java\jdk-11.0.2\jre
#其实这是因为打开的cmd并以管理员身份打开

#其实是权限不够的问题
#cmd！=管理员命令提示符 
#（虽然有时候叫错）


 

---


## 问题解决：

> 
<h3>第一步：管理员终端</h3>
#打开命令提示符（管理员身份）



<h3>第二步：进入文件</h3>
#进入到C:\Program Files\Java\jdk-11.0.2目录里面
cd C:\Program Files\Java\jdk-11.0.2



<h3> 第三步：生成</h3>
#开始生成JRE
bin\jlink.exe --module-path jmods --add-modules java.desktop --output jre



#可以看见已经生成了JRE了




### 第二步：进入文件

## 推荐：

[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="icon-default.png?t=M3C8" src="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8"/>https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124252949?spm=1001.2014.3001.5501)
