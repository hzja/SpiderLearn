# 原创
：  【后端检测-绕过】突破getmagesize()、exif_imagetype()绕过

# 【后端检测-绕过】突破getmagesize()、exif_imagetype()绕过

**目录**

[一、突破getmagesize():](#%E7%AA%81%E7%A0%B4getmagesize%28%29%3A)

[1.1、原理：](#1.1%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[1.2、利用过程：](#1.2%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.3、文件拼接](#%E6%96%87%E4%BB%B6%E6%8B%BC%E6%8E%A5)

[1.4、LSB图片隐写](#LSB%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[二、突破exif_imagetype()：](#%E7%AA%81%E7%A0%B4exif_imagetype%28%29%EF%BC%9A)

[2.1、原理：](#2.1%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[2.2、利用过程：](#2.2%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 一、突破getmagesize():

> 
<h3>1.1、原理：</h3>
隐写术的使用，将Shellcode隐写到一张BMP图片中，把字符串拆成字节，写入每个像素的alpha通道中，然后上传到可信任的网站下偏移拼接shellcode进行远程动态加载，能有效地增加了免杀性和隐匿性。

getimagesize()用于获取图像大小及相关信息，该函数参数为字符串表示的图像资源。
可以是服务器图片等可以获取的资源，也可以是用户表单上传的图像



隐写技术（一般和加解密一起使用）
隐写的利用过程有很多
（我最近在看**数据隐藏技术揭秘**）




> 
<h3>1.2、利用过程：</h3>
第一步：准备一张图片，要上传的shellcode文件
第二步：利用隐写术，将shellcode写进图片中
第三步：上传经过隐写后生成的图片


> 
<h3>1.3、文件拼接</h3>
在上文GIF绕过的时候提到
使用命令将2文件内容合并（可以将zip等其他类型文件伪装成图片等，copy/b 1.gif/b+1.rar/b 2.gif）
就是隐写的一直，但是容易使用010Editor等工具观察发现问题，或者使用Linux下的binwalk这个工具。
binwalk可以自动化的分析图片中附加的其他的文件，其原理就是检索匹配文件头，常用的一些文件头都可以被发现，然后利用偏移可以配合winhex或者是dd分割出隐藏的部分。


> 
<h3>1.4、LSB图片隐写</h3>
是一种常见的方式，LSB也就是最低有效位 (Least Significant Bit)。
<h4>原理：</h4>
图片中的像数一般是由三种颜色组成，即三原色，由这三种原色可以组成其他各种颜色，例如在PNG图片的储存中，每个颜色会有 8bit，LSB隐写就是修改了像数中的最低的1bit，把信息隐藏进去，但是人眼看不出来。

Stegsolve可以辅助寻找这种LSB隐藏痕迹
下载地址：
[http://www.caesum.com/handbook/Stegsolve.jar<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>http://www.caesum.com/handbook/Stegsolve.jar](http://www.caesum.com/handbook/Stegsolve.jar)
（使用方法：需要使用java环境打开）
需要配置java环境：
[3分钟复制粘贴配置java环境变量，验证配置是否成功，java文件运行方法怎么快怎么来，并确保能正常运行<img alt="" src="https://g.csdnimg.cn/static/logo/favicon32.ico"/>https://blog.csdn.net/qq_53079406/article/details/123482726?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/123482726?spm=1001.2014.3001.5501)
独特的打开方法：（不见不知道）
[Stegsolve.jar工具包准备，避坑指南，教你正确启动Stegsolve让我承担所有把，为你们避开所有的坑<img alt="" src="https://g.csdnimg.cn/static/logo/favicon32.ico"/>https://blog.csdn.net/qq_53079406/article/details/123484448?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/123484448?spm=1001.2014.3001.5501)



先打开文件
再Stegsolve----Analyse----Frame Browser
可以浏览三个颜色通道中的每一位，可以在红色通道的最低位



可以使用在线http://tool.chinaz.com/qrcode/，解qrcode得到了flag{}
隐写使用了ascii，可以使用Stegsolve-----Analyse-----Data Extract来查看ascii码






---


---


## 二、突破exif_imagetype()：

> 
<h3>2.1、原理：</h3>
exif_imagetype() 读取一个图像的第一个字节并检查其签名。如果发现了恰当的签名则返回一个对应的常量，否则返回 FALSE

exif_imagetype ( string $filename ) : int
 $filename是文件位置和名称，如果检查是图片文件则返回一个跟图像类型对应的数字，否则返回 FALSE。
<hr/>
<h3>2.2、利用过程：</h3>
利用包含文件包含漏洞




### 2.2、利用过程：
