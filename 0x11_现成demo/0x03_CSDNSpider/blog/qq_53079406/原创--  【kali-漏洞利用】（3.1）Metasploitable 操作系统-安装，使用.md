# 原创
：  【kali-漏洞利用】（3.1）Metasploitable 操作系统：安装，使用

# 【kali-漏洞利用】（3.1）Metasploitable 操作系统：安装，使用

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、下载：](#1.2%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[二、搭建](#%E4%BA%8C%E3%80%81%E6%90%AD%E5%BB%BA)

[2.1、解压：](#2.1%E3%80%81%E8%A7%A3%E5%8E%8B%EF%BC%9A)

[2.2、安装：](#2.2%E3%80%81%E5%AE%89%E8%A3%85%EF%BC%9A)

[2.3、开启虚拟机](#2.3%E3%80%81%E5%BC%80%E5%90%AF%E8%99%9A%E6%8B%9F%E6%9C%BA)

[可能出现的问题](#%E5%8F%AF%E8%83%BD%E5%87%BA%E7%8E%B0%E7%9A%84%E9%97%AE%E9%A2%98)

[再次启动虚拟机](#%E5%86%8D%E6%AC%A1%E5%90%AF%E5%8A%A8%E8%99%9A%E6%8B%9F%E6%9C%BA)

[2.4、使用：](#2.4%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
Metasploitable 是一款基于Ubuntu Linux 的操作系统。该系统是一个虚拟机文件， 从网站下载解压之后可以直接使用，无需安装。由于基于Ubuntu, 所以Metasploitable 使用起来十分得心应手
<hr/>
Metasploitable 就是用来作为攻击用的靶机， 所以它存在大量未打补丁漏洞， 并且开放了无数高危端口

 Metasploitable是一个故意易受攻击的Linux虚拟机。VM 可用于执行安全培训、测试安全工具以及练习常见的渗透测试技术。‎<br/> ‎ ‎<br/> ‎默认登录名和密码是 msfadmin：msfadmin


> 
<h3>1.2、下载：</h3>
地址1（要注册）：
[Download Metasploitable - Intentionally Vulnerable Machine | Rapid7<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://information.rapid7.com/download-metasploitable-2017.html](https://information.rapid7.com/download-metasploitable-2017.html)
地址2（推荐）：
[Metasploitable download | SourceForge.net<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://sourceforge.net/projects/metasploitable/](https://sourceforge.net/projects/metasploitable/)
<hr/>
我下的地址2


3.9M/s+1.4/s的加速=5.3M/s
其实还得看家里网速怎么样


 



---


---


## 二、搭建

> 
<h3>2.1、解压：</h3>
解压安装包





> 
<h3>2.2、安装：</h3>
虚拟机安装
使用vm直接打开 vmx后缀的
左上角----文件-----打开


找到刚刚解压的位置，选中，并打开

 <img alt="" height="1000" src="https://img-blog.csdnimg.cn/5d3aa2833d6a435681108b3f96456800.png" width="1200"/>



> 
<h3>2.3、开启虚拟机</h3>
启动Metasploitable2靶场
<h4>可能出现的问题</h4>
（我使用的是vm12）


在文件夹中找到vmx

使用记事本打开
将7改为10
然后保存


<hr/>
<h4>再次启动虚拟机</h4>




#### 再次启动虚拟机

> 
<h3>2.4、使用：</h3>
默认账号密码： 账号：msfadmin 密码：msfadmin
登录进去了


<hr/>

可以修改管理员密码
输入sudo passwd root
<hr/>
查看ip
可以输入ip add




---

