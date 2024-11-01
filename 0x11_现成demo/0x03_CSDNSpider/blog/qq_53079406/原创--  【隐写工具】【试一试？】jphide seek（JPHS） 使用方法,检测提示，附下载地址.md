# 原创
：  【隐写工具】【试一试？】jphide seek（JPHS） 使用方法,检测提示，附下载地址

# 【隐写工具】【试一试？】jphide seek（JPHS） 使用方法,检测提示，附下载地址

**目录**

[准备阶段：](#%E5%87%86%E5%A4%87%E9%98%B6%E6%AE%B5%EF%BC%9A)

[windows可视化界面的下载地址：](#windows%E5%8F%AF%E8%A7%86%E5%8C%96%E7%95%8C%E9%9D%A2%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

[GitHub下载地址：](#GitHub%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

[使用对象：](#%E4%BD%BF%E7%94%A8%E5%AF%B9%E8%B1%A1%EF%BC%9A)

[JPHS介绍：](#JPHS%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[隐藏文件：](#%E9%9A%90%E8%97%8F%E6%96%87%E4%BB%B6%EF%BC%9A)

[第一步：准备文件](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%87%86%E5%A4%87%E6%96%87%E4%BB%B6)

[第二步：（windows版本） 打开软件，点击“Open jpeg”](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%EF%BC%88windows%E7%89%88%E6%9C%AC%EF%BC%89%20%E6%89%93%E5%BC%80%E8%BD%AF%E4%BB%B6%EF%BC%8C%E7%82%B9%E5%87%BB%E2%80%9COpen%20jpeg%E2%80%9D)

[第三步：点击“Hide”，并输入密码](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%82%B9%E5%87%BB%E2%80%9CHide%E2%80%9D%EF%BC%8C%E5%B9%B6%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81)

[第三步：将他们合并，并另存为](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%B0%86%E4%BB%96%E4%BB%AC%E5%90%88%E5%B9%B6%EF%BC%8C%E5%B9%B6%E5%8F%A6%E5%AD%98%E4%B8%BA)

[提取隐藏文件：](#%E6%8F%90%E5%8F%96%E9%9A%90%E8%97%8F%E6%96%87%E4%BB%B6%EF%BC%9A)

---


## 准备阶段：

> 
 有windows和Linux版本的，windows版有可视化界面
<h4>windows可视化界面的下载地址：</h4>
[Download for Free JPHS for Windows 0.5 (scanwith.com)](https://www.scanwith.com/JPHS_for_Windows_download.htm#google_vignette)
<h4>GitHub下载地址：</h4>
[h3xx/jphs: jphide &amp; seek steganography tools (github.com)](https://github.com/h3xx/jphs)


#### GitHub下载地址：

## 使用对象：

> 
从名字不难看出使用对象是JPEG文件（就是常见的.jpg文件）
简介：JPEG是联合图象专家组(Joint Picture Expert Group)的英文缩写，是国际标准化组织(ISO)和CCITT联合制定的静态图象的压缩编码标准，比相同图象质量的其它文件格式（静态图象）相比压缩比最高的（高压缩比）


## JPHS介绍：

> 
对有损压缩JPEG文件进行信息的加密隐藏、探测提取的工具

JPHS包含2个功能（靠2个程序实现）：
JPHIDE：能够将信息文件加密隐藏到JPEG图像
JPSEEK：从用JPHIDE程序加密隐藏得到的JPEG图像中探测并提取到信息文件


## 隐藏文件：

> 
<h4> 第一步：准备文件</h4>
(test.jpg文件)+（test.txt文本）



<h4>第二步：（windows版本） 打开软件，点击“Open jpeg”</h4>
使用图形化操作界面的Jphs（Windows版本）-------&gt;点击“Open jpeg”打开JPEG格式图片
（我这里打开的test.jpg）


打开之后有按钮就不是灰色的了
并且还会显示JPEG文件的相关信息
(注：如果打开的不是JPEG文件会自动退出)





<h4>第三步：点击“Hide”，并输入密码</h4>
点击“Hide”后输入2次相同的密码，并点击ok


然后选择要隐藏进去的文件<img alt="" height="560" src="https://img-blog.csdnimg.cn/7fb475d2001f44f78625e6f5da97bd81.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="694"/>


 选择之后会在第二个Hidden中显示相关信息<img alt="" height="556" src="https://img-blog.csdnimg.cn/4c0fd50ca4dc4798935cb0d70215f975.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="690"/>




<h4>第三步：将他们合并，并另存为</h4>
点击“Save jpeg as”将图片另存为jpeg格式然后输入自己想输入的名字.jpg

 <img alt="" height="555" src="https://img-blog.csdnimg.cn/80c1346517f240d1928b23f72661f7e5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="691"/>
 the file you hid in this jpeg has caused statistically significant change and may be detectable
您在此JPEG中隐藏的文件导致统计上显着的变化，可能是可检测的


#### 第二步：（windows版本） 打开软件，点击“Open jpeg”

#### 第三步：将他们合并，并另存为

## 提取隐藏文件：

> 
 （注：对图片的隐写方式和密码都一无所知的时候，使用Stegdetect进行探测和破解）
我们这里知道，就可以直接提取吧


显示出信息就是打开成功了


点击seek，再输入密码进行提取




<img alt="" height="555" src="https://img-blog.csdnimg.cn/36480dec786d408e9c015c9a11fd68e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="688"/> 已经提取到了（和隐藏进去的进行对比，是一样的）




推荐：

[【数据隐藏】一起入门隐写吧，宝？word、图像、移动设备、文件压缩数据隐藏](https://blog.csdn.net/qq_53079406/article/details/123537834?spm=1001.2014.3001.5501)

 

 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/290915296ff2be121fe5fa70df15914b.gif"/>
