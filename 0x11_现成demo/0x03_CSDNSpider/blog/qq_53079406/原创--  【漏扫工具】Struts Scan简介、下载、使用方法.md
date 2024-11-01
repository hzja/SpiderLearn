# 原创
：  【漏扫工具】Struts Scan简介、下载、使用方法

# 【漏扫工具】Struts Scan简介、下载、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、系统](#%E4%BA%8C%E3%80%81%E7%B3%BB%E7%BB%9F)

[2.1、Windows](#2.1%E3%80%81Windows)

[2.2、Linux](#2.2%E3%80%81Linux)

[三、下载：](#%E4%B8%89%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、第一步：在文件夹中打开Windows powershell](#4.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%9C%A8%E6%96%87%E4%BB%B6%E5%A4%B9%E4%B8%AD%E6%89%93%E5%BC%80Windows%20powershell)

[4.2、第二步：终端运行struts-scan.exe URL](#4.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%BB%88%E7%AB%AF%E8%BF%90%E8%A1%8Cstruts-scan.exe%20URL)

[4.3、第三步：查看结果](#4.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E7%BB%93%E6%9E%9C)

---


## 一、简介：

> 
Struts是流行和成熟的基于MVC设计模式的一个非常优秀Web应用程序框架。
它先是Jakarta项目的一个子项目，后来转为Apache软件基金会的一个子项目。
<hr/>
Struts1采用Servlet的机制处理用户请求。
Struts2是Struts的下一代产品，它以WebWork为核心，采用拦截器的机制处理用户的请求，这样的设计也使得业务逻辑控制器能够与Servlet API完全脱离开，所以Struts2可以理解为WebWork的更新产品。


---


---


## 二、系统

> 
<h3>2.1、Windows</h3>
下载以后在终端直接运行这个加上命令


<hr/>
<h3>2.2、Linux</h3>
使用python运行这py脚本加上命令




### 2.2、Linux

---


---


## 三、下载：

> 
GitHub下载：
[Lucifer1993/struts-scan: Python2编写的struts2漏洞全版本检测和利用工具 (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/Lucifer1993/struts-scan](https://github.com/Lucifer1993/struts-scan)




---


---


## 四、使用方法：

​​本处介绍的是Windows的使用方法

如果是Linux的话，操作类似

只是在终端是使用（python struts-scan.py 目标URL）

> 
<h3>4.1、第一步：在文件夹中打开Windows powershell</h3>
（如果使用命令提示符，就要进入到目录里面）
空白处点击右键
（如果没有，尝试按住shift再右键空白处）




> 
<h3>4.2、第二步：终端运行struts-scan.exe URL</h3>
我输入的是：
.\struts-scan.exe http://baidu.com




> 
<h3>4.3、第三步：查看结果</h3>
在文件夹中会输出扫描结果的文件



