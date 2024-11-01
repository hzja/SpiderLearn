# 原创
：  【检测隐藏信息】StegSpy介绍、下载、使用方法、以及组件COMDLG32.OCX问题

# 【检测隐藏信息】StegSpy介绍、下载、使用方法、以及组件COMDLG32.OCX问题

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、介绍：](#1.1%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[1.2、识别程序的特定版本](#1.2%E3%80%81%E8%AF%86%E5%88%AB%E7%A8%8B%E5%BA%8F%E7%9A%84%E7%89%B9%E5%AE%9A%E7%89%88%E6%9C%AC)

[1.3、支持格式：](#1.3%E3%80%81%E6%94%AF%E6%8C%81%E6%A0%BC%E5%BC%8F%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[ 2.1官网：](#%C2%A02.1%E5%AE%98%E7%BD%91%EF%BC%9A)

[2.2、下载位置](#2.2%E3%80%81%E4%B8%8B%E8%BD%BD%E4%BD%8D%E7%BD%AE)

[三、使用方法：](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[3.1、第一步：运行exe文件](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%BF%90%E8%A1%8Cexe%E6%96%87%E4%BB%B6)

[ 3.2、第二步：选择文件](#%C2%A03.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%96%87%E4%BB%B6)

[3.3、第三个：查看检测结果](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E4%B8%AA%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%A3%80%E6%B5%8B%E7%BB%93%E6%9E%9C)

[四、问题解决：](#%E5%9B%9B%E3%80%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[4.1、组件COMDLG32.OCX及依赖问题](#4.1%E3%80%81%E7%BB%84%E4%BB%B6COMDLG32.OCX%E5%8F%8A%E4%BE%9D%E8%B5%96%E9%97%AE%E9%A2%98)

[4.2、第一步：获取组件](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96%E7%BB%84%E4%BB%B6)

[4.3、第二步：放到system里面](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%94%BE%E5%88%B0system%E9%87%8C%E9%9D%A2)

[4.4、第三步：执行组件解决依赖问题](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%89%A7%E8%A1%8C%E7%BB%84%E4%BB%B6%E8%A7%A3%E5%86%B3%E4%BE%9D%E8%B5%96%E9%97%AE%E9%A2%98)

[4.4.1、提示：](#%E6%8F%90%E7%A4%BA%EF%BC%9A)

[4.4.2、输入：](#%E8%BE%93%E5%85%A5%EF%BC%9A)

[4.4.3、结果：](#4.4.3%E3%80%81%E7%BB%93%E6%9E%9C%EF%BC%9A)

---


 （是你吗，老六！）

---


## 一、简介：

> 
<h3>1.1、介绍：</h3>
StegSpy是一个用于检测隐藏信息的签名分析软件。
StegSpy是一个一直在进行中的程序。最新版本包括允许识别“隐蔽”文件。StegSpy将检测隐写术和用于隐藏消息的程序。最新版本还标识隐藏内容的位置。
<h3>1.2、识别程序的特定版本</h3>


<h3>1.3、支持格式：</h3>



### 1.2、识别程序的特定版本

---


## 二、下载：

> 
<h3> 2.1官网：</h3>
[spyhunter - StegSpy (spy-hunter.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>http://www.spy-hunter.com/stegspy](http://www.spy-hunter.com/stegspy)
<h3>2.2、下载位置</h3>
是免安装的软件






### 2.2、下载位置

---


## 三、使用方法：

> 
<h3>3.1、第一步：运行exe文件</h3>
直接点击运行exe文件
可能会报错“component comdlg32.ocx or one of its dependencies not correctly registered :a file is missing or invalid”
查看最后的问题解决方法



> 
<h3> 3.2、第二步：选择文件</h3>
点击run，然后选择要检查的文件





> 
<h3>3.3、第三个：查看检测结果</h3>
对不起，找不到Steg。



---


## 四、问题解决：

> 
<h3>4.1、组件COMDLG32.OCX及依赖问题</h3>
component comdlg32.ocx or one of its dependencies not correctly registered :a file is missing or invalid
组件COMDLG32.OCX或其依赖项之一未正确注册：文件丢失或无效



> 
<h3>4.2、第一步：获取组件</h3>
从网上找一个大型的网站下载 COMDLG32.OCX 下载


> 
<h3>4.3、第二步：放到system里面</h3>
一般现在电脑都是64位
32位系统将其复制到 C:\windows\system32\ 目录下

64位系统将其复制到 C:\Windows\SysWOW64\ 目录下



> 
<h3>4.4、第三步：执行组件解决依赖问题</h3>
用“管理员身份”运行命令提示符（直接搜）
不推荐使用win+R再CMD（并不是以管理员身份运行的）


<h4>4.4.1、提示：</h4>
命令提示符中system32并不表示你的操作系统是32位
不信，自己可以在system32，和SysWOW64都尝试一下


<h4>4.4.2、输入：</h4>
32位系统输入 regsvr32 c:\Windows\system32\comdlg32.ocx 回车


64位系统输入 regsvr32 c:\Windows\SysWOW64\comdlg32.ocx 回车


<h4>4.4.3、结果：</h4>




#### 4.4.1、提示：

#### 4.4.3、结果：
