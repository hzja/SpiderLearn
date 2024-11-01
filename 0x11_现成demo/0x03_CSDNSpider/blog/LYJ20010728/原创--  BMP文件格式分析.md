# 原创
：  BMP文件格式分析

# BMP文件格式分析

#### BMP文件格式分析

## 位图定义

> 
计算机能以位图和矢量图格式显示图像


### Bitmap（位图）

> 



### Vector（矢量图）

> 



## BMP位图文件

> 
常见的图像文件格式有：BMP、JPG(JPEG)、GIF等


> 
BMP图像文件(Bitmap-File)格式是Windows采用的图像文件存储格式，在Windows环境下运行的所有图像处理软件都支持这种格式，Windows 3.0以后的BMP文件都是指设备无关位图(DIB，device-independent bitmap)，BMP位图文件默认的文件扩展名是`.BMP`，有时也会以`.DIB`或`.RLE`作扩展名


> 
例图，512 x 512


### BMP文件结构

> 
- 位图文件头(bitmap-file header)- 位图信息头(bitmap-informationheader)- 颜色表(color table)- 颜色点阵数据(bits data)


> 
需要注意的是，24位真彩色位图没有颜色表只有位图文件头、位图信息头和颜色点阵数据这三部分


> 
如果位深度是24的话，就说明图片是24位真彩色


> 
通过`010 editor`可以看到这个文件的全部数据


#### BITMAPFILEHEADER（位图文件头）

> 
位图文件头分4部分，共14字节


> 
在Windows中数据是反的，如果一段数据为`50 1A 25 3C`，则为`0x3C251A50`，因此bfSize的数据为`36 00 0C 00`，其实是`0x000C0036`，也就是`0xC0036`


#### BITMAPINFOHEADER（2位图信息头）

> 
位图信息头共40字节


> 
真彩色位图主要关心的是`biWidth`和`biHeight`这两个数值，两个数值体现的是图像的尺寸，`biSize、biPlanes、biBitCount`这几个数值是固定的


#### 4颜色点阵数据

> 



## Photoshop和Windows的BMP文件比较

> 
Windows的BMP文件最后少了两个0字节，没有整体补位，bfSize(文件大小)，biSizeImage(全部像素大小)也相应地减去2


> 
行补位的公式为：widthBytes = (width**biBitCount+31)/32**4<br/> 参数说明：


