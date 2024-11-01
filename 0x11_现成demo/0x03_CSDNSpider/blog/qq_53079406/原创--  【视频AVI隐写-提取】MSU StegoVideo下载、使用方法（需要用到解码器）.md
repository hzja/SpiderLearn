# 原创
：  【视频AVI隐写/提取】MSU StegoVideo下载、使用方法（需要用到解码器）

# 【视频AVI隐写/提取】MSU StegoVideo下载、使用方法（需要用到解码器）

**目录**

[一、背景：](#%E4%B8%80%E3%80%81%E8%83%8C%E6%99%AF%EF%BC%9A)

[1.1、简介](#1.1%E3%80%81%E7%AE%80%E4%BB%8B)

[1.2、主要特性](#1.2%E3%80%81%E4%B8%BB%E8%A6%81%E7%89%B9%E6%80%A7)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[三、需要安装的环境](#%E4%B8%89%E3%80%81%E9%9C%80%E8%A6%81%E5%AE%89%E8%A3%85%E7%9A%84%E7%8E%AF%E5%A2%83)

[3.1、DIVX（国产）](#3.1%E3%80%81DIVX%EF%BC%88%E5%9B%BD%E4%BA%A7%EF%BC%89)

[3.2、Xvid](#3.2%E3%80%81Xvid)

[3.2.1、简介：](#3.2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.2.2、下载地址：](#3.2.2%E3%80%81%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、第一步：确认目的](#4.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%A1%AE%E8%AE%A4%E7%9B%AE%E7%9A%84)

[4.2、第二步：准备文件](#4.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%87%86%E5%A4%87%E6%96%87%E4%BB%B6)

[4.3、第三步：设置噪音级别和数据冗余度](#4.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AE%E5%99%AA%E9%9F%B3%E7%BA%A7%E5%88%AB%E5%92%8C%E6%95%B0%E6%8D%AE%E5%86%97%E4%BD%99%E5%BA%A6)

[ 4.4、第四步： 生成新的 AVI文件](#%C2%A04.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%20%E7%94%9F%E6%88%90%E6%96%B0%E7%9A%84%20AVI%E6%96%87%E4%BB%B6)

---


---


 

## 一、背景：

> 
<h3>1.1、简介</h3>
MSU Stego Video是一个免费、 非开源的隐写工具， 可以从俄国的莫斯科州立大学获取。


> 
<h3>1.2、主要特性</h3>
（1）能够在全动态视频中隐藏信息。
（2）能够在视频帧中冗余地嵌入数据， 使生成的AVI (Audio Video Interleave)，文件在丢帧（如 视频流传输过程中的丢包）的情况下仍能还原隐藏数据。
（3）在标清和高清模式下， MSU Stego对视频所做的更改在视觉上都无法感知。
（4）MSU Stego的数据嵌入对视频帧的修改甚微， 这样可以尽量保证隐秘性或者规避数据检测。


---


## 二、下载：

> 
链接：https://pan.baidu.com/s/12-jaBy_8LB-jdn4BV635pg?pwd=ptqi <br/> 提取码：ptqi


---


## 三、需要安装的环境

> 
 其实是2个解码器，根据自己电脑实际情况，可以选择安装合适的解码器
（解码器这块可能需要自己多试试）
最后一步的成功输出会用到解码器
<hr/>
<h3>3.1、DIVX（国产）</h3>
下载地址：
[Free DivX Video Software - Play, convert and cast video. Play DivX files.<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://www.divx.com/en/software/divx/](https://www.divx.com/en/software/divx/)
<hr/>
<h3>3.2、Xvid</h3>
<h4>3.2.1、简介：</h4>
Xvid Video Codec最新版是款针对视频文件所打造的视频编辑软件。Xvid Video Codec支持视频解码缓存，可用于对视频进行播放解码缓存下载播放。Xvid Video Codec中还适用于多种主流平台，包括windows、Linux、mac等。

<h4>3.2.2、下载地址：</h4>
在下载软件的网站可以下载到（就不多说了，找好评高的就可）


---


### 3.2、Xvid

#### 3.2.2、下载地址：

---


## 四、使用方法：

> 
<h3>4.1、第一步：确认目的</h3>
首先决定操作目的， 是嵌入数据还是提取数据。



> 
<h3>4.2、第二步：准备文件</h3>
然后确认MSU Stego所需的3个文件：
（路径最好别包含中文，可能会出错）
<hr/>
输入文件：即原始视频， 必须是 AVI格式的。
输出文件：用于存储处理过的视频（即重建）。
待隐藏信息：目前MSU Stego只支持使用 ASCII码的．txt文本文件



 <img alt="" height="376" src="https://img-blog.csdnimg.cn/7f6967e77e2b4e7eadd3ac1a09650db2.png" width="1012"/>
 <img alt="" height="364" src="https://img-blog.csdnimg.cn/9e181eafaa854246a0c8dc4f34a3e914.png" width="506"/>



> 
<h3>4.3、第三步：设置噪音级别和数据冗余度</h3>
数据冗余度决定了数据可以重复嵌人的次数， 这些重复的数据可用于当发生帧丢失或损坏时的数据恢复。


 noise level(噪音水平)、data redundancy（数据冗余）、Generate option parameters（生成选项参数）、planned compression bitrate（计划的压缩比特率）、File size（文件大小）、Video stream capacity（视频流容量）




> 
<h3> 4.4、第四步： 生成新的 AVI文件</h3>
会自动生成加密密码，也可自己修改
passcode（密码）


最后一步，会用到解码器（如果下的用不了，就再换其他的试试）
最后自动执行隐写，并输出文件

