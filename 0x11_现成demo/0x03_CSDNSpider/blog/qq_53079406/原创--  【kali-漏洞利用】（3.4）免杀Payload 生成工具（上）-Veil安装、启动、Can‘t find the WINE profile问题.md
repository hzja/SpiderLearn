# 原创
：  【kali-漏洞利用】（3.4）免杀Payload 生成工具（上）：Veil安装、启动、Can‘t find the WINE profile问题

# 【kali-漏洞利用】（3.4）免杀Payload 生成工具（上）：Veil安装、启动、Can‘t find the WINE profile问题

**目录**

[一、veil](#%E4%B8%80%E3%80%81veil)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、安装：](#1.2%E3%80%81%E5%AE%89%E8%A3%85%EF%BC%9A)

[1.3、更新：](#1.3%E3%80%81%E6%9B%B4%E6%96%B0%EF%BC%9A)

[1.4、安装依赖](#1.4%E3%80%81%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96)

[python安装](#python%E5%AE%89%E8%A3%85)

[pywin32-218 模块安装](#pywin32-218%20%E6%A8%A1%E5%9D%97%E5%AE%89%E8%A3%85)

[pycrypto-2.6 模块安装](#pycrypto-2.6%20%E6%A8%A1%E5%9D%97%E5%AE%89%E8%A3%85)

[1.5、最后的补装](#1.5%E3%80%81%E6%9C%80%E5%90%8E%E7%9A%84%E8%A1%A5%E8%A3%85)

[select setup language](#select%20setup%20language)

[Autolt](#Autolt)

[1.6、问题解决：Can't find the WINE profile](#1.6%E3%80%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9ACan'%20rel=)

[问题重现：](#%E9%97%AE%E9%A2%98%E9%87%8D%E7%8E%B0%EF%BC%9A)

[解决方法：](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%9A)

[1.7、启动：](#1.7%E3%80%81%E5%90%AF%E5%8A%A8%EF%BC%9A)

---


## 一、veil

> 
<h3>1.1、概述：</h3>
Veil是一款利用Metasploit框架生成相兼容的Payload工具
能绕过常见的杀毒软件


> 
<h3>1.2、安装：</h3>
sudo apt-get install veil
安装过程没有提示错误， 则表示Veil安装成功（依赖较多， 安装时间长点）
（我是装系统时候，就安装了kali的所有软件）

<hr/>
（下图是我重装系统后又安装的一遍）

 <img alt="" height="511" src="https://img-blog.csdnimg.cn/5d6a192b60484de982be70e92fe479a4.png" width="640"/>
<img alt="" height="510" src="https://img-blog.csdnimg.cn/ce85bec23da4446ba5d8275f2170224a.png" width="644"/> 
 


> 
<h3>1.3、更新：</h3>
输入的是veil
（然后克隆-更新配置）
输入y
（等待下载解压完成，时间有点长）




> 
<h3>1.4、安装依赖</h3>
会依次弹出的对话框，以图形界面的形式依次安装Python 及它的两个模块pywin32-218 和pycrypto-2.6
<h4>python安装</h4>
Python初始安装的界面

选择Python安装位置

自定义Python（都已经被选好了）

 安装完成，点击finish



 

> 
<h4>pywin32-218 模块安装</h4>
全部都是点击下一步按钮（后面界面都是一样）

 <img alt="" height="466" src="https://img-blog.csdnimg.cn/7dfd7e12e2c14206a6668b8e3a7592cb.png" width="1173"/>



 

> 
<h4>pycrypto-2.6 模块安装</h4>
（全部都点击下一步即可）

<img alt="" height="628" src="https://img-blog.csdnimg.cn/e722cfd2c63e46f2a049726ee1d5c63f.png" width="1200"/> <img alt="" height="651" src="https://img-blog.csdnimg.cn/1918346cafbc4db9878a29f1c92142ea.png" width="1200"/>


 

> 
<h3>1.5、最后的补装</h3>
（我的kali还差一些依赖，经常安装软件的人，都不需要看字，就能安装）


应该差依赖，需要手动安装

<hr/>
<h4>select setup language</h4>
选择第一个按钮
 <img alt="" height="168" src="https://img-blog.csdnimg.cn/07c9dfa72d4e413081418f2359bb11c6.png" width="545"/>
选中第一个，选择第一个按钮

选择中间那个按钮

 这是存在了，应该是替换，点是<img alt="" height="414" src="https://img-blog.csdnimg.cn/7a063fbe60f2465fb646fe0a7c268089.png" width="902"/>
 <img alt="" height="414" src="https://img-blog.csdnimg.cn/ebb92a5192164efcaf23b27518ed87d8.png" width="909"/>
这就是finish了

<hr/>
<h4>Autolt</h4>
选择第一个

 选择中间那个

 选中第一个，再选择中间那个

选择中间那个<img alt="" height="415" src="https://img-blog.csdnimg.cn/aaf4b6080d16469bbdf63e91aa98d2ba.png" width="913"/>
 选择中间那个

 选择中间那个



 选择中间那个




---


#### Autolt

> 
<h3>1.6、问题解决：Can't find the WINE profile </h3>
<h4>问题重现：</h4>
<img alt="" height="89" src="https://img-blog.csdnimg.cn/9fa58843df2446329f5f6264a6d74a83.png" width="685"/>[!] ERROR #2-3: Can't find the WINE profile for AuotIT v3 (/var/lib/veil/wine//drive_c/Program Files/AutoIt3/Aut2Exe/Aut2exe.exe).   Run: /usr/share/veil/config/setup.sh --force --silent<br/>  
<hr/>
<h4>解决方法：</h4>
/usr/share/veil/config/setup.sh --force --silent
（中间可能会有红色的报错，但是还是可以安装成功的）



#### 解决方法：

> 
<h3>1.7、启动：</h3>
输入veil



