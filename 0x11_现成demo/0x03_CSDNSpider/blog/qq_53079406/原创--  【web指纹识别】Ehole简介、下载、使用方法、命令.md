# 原创
：  【web指纹识别】Ehole简介、下载、使用方法、命令

# 【web指纹识别】Ehole简介、下载、使用方法、命令

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.1、GitHub下载：](#2.1%E3%80%81GitHub%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.2、win版：](#2.2%E3%80%81win%E7%89%88%EF%BC%9A)

[2.3、Linux版：](#2.3%E3%80%81Linux%E7%89%88%EF%BC%9A)

[三、win版使用方法：](#%E4%B8%89%E3%80%81win%E7%89%88%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[3.1、第一步：文件夹中打开windows powershell（或者cmd后进入）](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%96%87%E4%BB%B6%E5%A4%B9%E4%B8%AD%E6%89%93%E5%BC%80windows%20powershell%EF%BC%88%E6%88%96%E8%80%85cmd%E5%90%8E%E8%BF%9B%E5%85%A5%EF%BC%89)

[3.2、第二步：终端运行+命令](#3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%BB%88%E7%AB%AF%E8%BF%90%E8%A1%8C%2B%E5%91%BD%E4%BB%A4)

[3.3、使用示例](#3.3%E3%80%81%E4%BD%BF%E7%94%A8%E7%A4%BA%E4%BE%8B)

[3.3.1、识别单一的URL](#3.3.1%E3%80%81%E8%AF%86%E5%88%AB%E5%8D%95%E4%B8%80%E7%9A%84URL)

[3.3.2、识别本地文件里的URL](#3.3.2%E3%80%81%E8%AF%86%E5%88%AB%E6%9C%AC%E5%9C%B0%E6%96%87%E4%BB%B6%E9%87%8C%E7%9A%84URL)

[3.4、命令选项：](#3.3%E3%80%81%E5%91%BD%E4%BB%A4%E9%80%89%E9%A1%B9%EF%BC%9A)

[四、日志文件](#%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6)

---


## 一、简介：

> 
EHole是一款对资产中重点系统指纹识别的工具，在红队作战中，信息收集是必不可少的环节，如何才能从大量的资产中提取有用的系统(如OA、VPN、Weblogic...)。EHole旨在帮助红队人员在信息收集期间能够快速从C段、大量杂乱的资产中精准定位到易被攻击的系统，从而实施进一步攻击。


---


---


## 二、下载：

> 
<h3>2.1、GitHub下载：</h3>
[Releases · EdgeSecurityTeam/EHole (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/EdgeSecurityTeam/Ehole/releases](https://github.com/EdgeSecurityTeam/Ehole/releases)下载对应的系统的版本


<h3>2.2、win版：</h3>
 在终端调用（很简单）
<h3>2.3、Linux版：</h3>
下载解压后，直接运行


### 2.2、win版：

---


---


## 三、win版使用方法：

> 
<h3>3.1、第一步：文件夹中打开windows powershell（或者cmd后进入）</h3>
空白处右键
（或者按住shift+右键）




<hr/>
<h3>3.2、第二步：终端运行+命令</h3>
用法:
Ehole [-f|-l] [parameter]
Ehole [-f|-l] [范围]



### 3.2、第二步：终端运行+命令

> 
<h3>3.3、使用示例</h3>
<h4>3.3.1、识别单一的URL</h4>
 我在fofa上随便找的一个URL试的

<hr/>
<h4>3.3.2、识别本地文件里的URL</h4>
新建一个文件（同一目录下）

 里面包含很多URL

 执行命令（-l是本地文件的意思）
.\Ehole3.0-Win.exe -l URL.txt




#### 3.3.2、识别本地文件里的URL

> 
<h3>3.4、命令选项：</h3>
-f string<br/>         FOFA搜索资产，支持IP和IP段。（192.168.1.1 | 192.168.1.0/24）
<hr/>
-fall string<br/>         FOFA批处理搜索IP
<hr/>
-fofa string<br/>        FOFA搜索资产，支持所有FOFA搜索语法。<br/> ps：“”“”必须先于“ \”。(ip=\"192.168.1.0/24\" | domain=\"test.com\")
<hr/>
-ftime string<br/>         FOFA超时（默认为“ 10”）
<hr/>
-h    帮助
<hr/>
-json string<br/>         输出 json
<hr/>
-l string<br/>        基于本地文件探测
<hr/>
-log string<br/>         日志文件名（默认“ server.log”）
<hr/>
-t string<br/>         线程（默认为“ 100”）
<hr/>
-u string<br/>         目标网址


---


---


---


---


---


---


## 四、日志文件

> 
运行以后会产生一个服务器日志文件





