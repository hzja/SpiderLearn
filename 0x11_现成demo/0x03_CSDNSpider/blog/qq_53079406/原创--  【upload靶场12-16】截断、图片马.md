# 原创
：  【upload靶场12-16】截断、图片马

# 【upload靶场12-16】截断、图片马

**目录**

[推荐](#%E6%8E%A8%E8%8D%90)

[Pass12（get 00截断，绕过白名单）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass13（post 00截断，绕过白名单）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass14（图片马，判断文件类型）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass15（图片马，检测是否为图片）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass16（图片马，检查字节、后缀）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>推荐</h2>
[【upload靶场1-11】基础关卡：特点、分析、利用<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125846616?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125846616?spm=1001.2014.3001.5501)


## Pass12（get 00截断，绕过白名单）

> 
<h3>特点：</h3>
%00截断
<hr/>
前提：
版本：php版本&lt;5.3.4
函数：magic_quotes_gpc为off
原理：move_uploaded_file（底层为C），遇到0x00会截断（16进制），%00（URL编码）


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单
流文件：是否能够利用::$DATA流文件进行绕过
逻辑漏洞：是否循环执行检测
特殊字符利用：%00（即0x00）截断


> 
<h3>利用：</h3>
1、使用%00来截断
<hr/>

上传图片马 （在bp里面加%00去截断）



在文件路径后加上shell.php%00


 <img alt="" height="742" src="https://img-blog.csdnimg.cn/26417c2e00c545a38c2e35d3023d4822.png" width="927"/>
将filename传入的文件名改为合法的

 <img alt="" height="738" src="https://img-blog.csdnimg.cn/dc0f964add7547b284ab51f023790828.png" width="792"/>



打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
（删除图片URL地址中shell.php后面多余部分）


粘贴shell地址，和自己设置的密码


---


---


## Pass13（post 00截断，绕过白名单）

> 
<h3>特点：</h3>
%00截断
<hr/>
前提：
版本：php版本&lt;5.3.4
函数：magic_quotes_gpc为off
原理：move_uploaded_file（底层为C），遇到0x00会截断（16进制），%00（URL编码）


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单
流文件：是否能够利用::$DATA流文件进行绕过
逻辑漏洞：是否循环执行检测
特殊字符利用：%00（即0x00）截断


> 
<h3>利用：</h3>
1、使用%00来截断
<hr/>

上传 （在bp里面加%00去截断）


<hr/>

1、在文件路径后加上shell.php+（+是为了给00留一个位置）
2、将filename传入的文件名改为合法的

 <img alt="" height="819" src="https://img-blog.csdnimg.cn/e54afbc111d1480a97fed94687125fcb.png" width="713"/>

在Hex中将+改为00 



<hr/>

打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
（删除图片URL地址中shell.php后面多余部分）


粘贴shell地址，和自己设置的密码


---


---


---


## Pass14（图片马，判断文件类型）

> 
<h3>特点：</h3>
通过判断文件的前两个字节，判断文件类型
<hr/>
1、Png：89 50 4E 47 0D 0A 1A 0A<br/> 2、Jpg：FF D8<br/> 3、Gif：47 49 46 38 39|37 61 <br/> 4、Bmp：42 4D


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
图片马：向图片中植入语句


> 
<h3>利用：</h3>
1、使用图片木马
php5.6以上的版本才能成功解析图片木马
<hr/>
制作图片马
1、可以直接使用Hex软件（如010 Editor、winhex等）在合适位置写入代码
2、在cmd命令中，将图片与php文件拼接

或者
（要先进入文件夹内，使用cd）
copy 文件名.png/b + 文件名.php 文件名.png 

 <img alt="" height="242" src="https://img-blog.csdnimg.cn/13bbf2cfebc242da9073bf7c85fd3613.png" width="276"/>
<hr/>

上传 图片马



<img alt="" height="781" src="https://img-blog.csdnimg.cn/01fd86ca8f9e426ea979269a0be17041.png" width="1038"/>



<hr/>

打开图片获得图片地址
利用文件包含漏洞upload-labs/include.php?file=upload/文件名
（图片显示为乱码则解析成功了）
复制图片马的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


---


## Pass15（图片马，检测是否为图片）

> 
<h3>特点：</h3>
通过getimagesize()函数检查是否为图片文件
<hr/>
1、Png：89 50 4E 47 0D 0A 1A 0A<br/> 2、Jpg：FF D8<br/> 3、Gif：47 49 46 38 39|37 61 <br/> 4、Bmp：42 4D


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
图片马：向图片中植入语句
和Pass14基本上一样


> 
<h3>利用：</h3>
1、使用图片木马
php5.6以上的版本才能成功解析图片木马
<hr/>
制作图片马
1、可以直接使用Hex软件（如010 Editor、winhex等）在合适位置写入代码
2、在cmd命令中，将图片与php文件拼接

或者
（要先进入文件夹内，使用cd）
copy 文件名.png/b + 文件名.php 文件名.png 

 <img alt="" height="241" src="https://img-blog.csdnimg.cn/b4ce683b83004b7e91077ce008de0f4f.png" width="314"/>
<hr/>


上传 图片马



<hr/>

打开图片获得图片地址
利用文件包含漏洞upload-labs/include.php?file=upload/文件名
（图片显示为乱码则解析成功了）
复制图片马的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


---


## Pass16（图片马，检查字节、后缀）

> 
<h3>特点：</h3>
通过exif_imagetype()函数，读取图像的第一个字节，并检查其后缀名
返回值与getimage()函数返回的索引2相同
<hr/>
1、Png：89 50 4E 47 0D 0A 1A 0A<br/> 2、Jpg：FF D8<br/> 3、Gif：47 49 46 38 39|37 61 <br/> 4、Bmp：42 4D


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
图片马：向图片中植入语句
和前几关基本上一样


> 
<h3>利用：</h3>
1、使用图片木马
php5.6以上的版本才能成功解析图片木马
需要开启`php_exif`模块

<hr/>

制作图片马
1、可以直接使用Hex软件（如010 Editor、winhex等）在合适位置写入代码
2、在cmd命令中，将图片与php文件拼接


或者
（要先进入文件夹内，使用cd）
copy 文件名.png/b + 文件名.php 文件名.png 

 <img alt="" height="173" src="https://img-blog.csdnimg.cn/246bd742af3944fb953455f9ecf8422b.png" width="641"/>

<hr/>
 上传 图片马




<hr/>
 打开图片获得图片地址
利用文件包含漏洞upload-labs/include.php?file=upload/文件名
（图片显示为乱码则解析成功了）
复制图片马的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---

