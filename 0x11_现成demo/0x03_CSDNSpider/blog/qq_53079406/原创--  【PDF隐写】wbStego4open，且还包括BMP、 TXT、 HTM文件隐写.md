# 原创
：  【PDF隐写】wbStego4open，且还包括BMP、 TXT、 HTM文件隐写

# 【PDF隐写】wbStego4open，且还包括BMP、 TXT、 HTM文件隐写

**目录**

[wbStego4open](#wbStego4open)

[下载地址：](#%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[首页：](#%E9%A6%96%E9%A1%B5%EF%BC%9A)

[Flowchart-Mode（流程图模式）](#Flowchart-Mode%EF%BC%88%E6%B5%81%E7%A8%8B%E5%9B%BE%E6%A8%A1%E5%BC%8F%EF%BC%89)

[ ​](#%C2%A0%E2%80%8B)

[使用过程：](#%E4%BD%BF%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[第一步：点击Continue，进入开始阶段](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%82%B9%E5%87%BBContinue%EF%BC%8C%E8%BF%9B%E5%85%A5%E5%BC%80%E5%A7%8B%E9%98%B6%E6%AE%B5)

[第二步：选择PDF文件](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9PDF%E6%96%87%E4%BB%B6)

[第三步：选择需要隐藏的载体文件，并进行隐藏](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E9%9C%80%E8%A6%81%E9%9A%90%E8%97%8F%E7%9A%84%E8%BD%BD%E4%BD%93%E6%96%87%E4%BB%B6%EF%BC%8C%E5%B9%B6%E8%BF%9B%E8%A1%8C%E9%9A%90%E8%97%8F)

---


（把所有类型隐写工具写完将进行分类总结归一）

## wbStego4open

### 下载地址：

> 
wbStego4open  (http://wbstego.wbailer.com)
我windows下的这个




### 简介：

> 
是一个隐写开源工具， 支持 Windows 和Linux 平台。
可以用 wbStego4open 可以把文件隐藏到 BMP、 TXT、 HTM 和 PDF 文件中， 且不会被看出破绽。 还可以用它来创建版权标识文件并嵌入到文件中将其隐藏。
能够允许用户把数据隐藏到 PDF 文件中的隐写程序非常少
这个程序利用 PDF 文件头添加额外信息， 这个区域的信息会被 Adobe Acrobat Reader 阅读器忽略。 此外， wbStego 在插入数据时， 充分利用了插入法和 LSB 修改法两种技术。
拥有数字证书的PDF文件内容其实是可以修改的， 但会提示接收者文件已经被修改过了， 不要相信其中的内容


### 原理：

> 
首先，wbStego4open会把插入数据中的每一个ASCII码转换为二进制形式
然后，把每一个二进制数字再替换为十六进制的20或09，20代表0，09代表1
最后，将这些被转换后的十六进制数据嵌入到PDF文件中
查看，用wbStego4open修改后的文件内容，会发现文件中已混入了很多由20和09组成的8位字节
还原，把这些 8 位字节取出来后， 再提取其最低有效位， 组合后即可获得其所代表的 ASCII 码的二进制形式， 然后再把二进制码转换成 ASCII 码就能得到原始消息了


### 首页：

> 
Settings（环境）、Flowchart-Mode（流程图模式）、Exit（退出）、Continue（继续）


<h3>Flowchart-Mode（流程图模式）</h3>
<h3> <img alt="" height="440" src="https://img-blog.csdnimg.cn/df239088283d4db6ac1134bcafd72496.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="662"/></h3>


###  <img alt="" height="440" src="https://img-blog.csdnimg.cn/df239088283d4db6ac1134bcafd72496.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="662"/>

### 使用过程：

#### 第一步：点击Continue，进入开始阶段

> 
 <img alt="" height="421" src="https://img-blog.csdnimg.cn/9392dc07b93a4d22802ebbbd989c02e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="671"/>

Encode（编码）
如果要在载体文件中隐藏数据。
Decode（解码）
如果要写隐藏的数据WBStego4再次进入一个文件。
 <img alt="" height="421" src="https://img-blog.csdnimg.cn/2267ca6705e64bda82a1e1fd771902bb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="671"/>


#### 第二步：选择PDF文件

> 
再点击Continue
然后选择要隐藏的数据，输入文件名或单击...按钮以选择文件或版权信息。
然后再点击Continue




#### 第三步：选择需要隐藏的载体文件，并进行隐藏

> 
要选择2次选择文件类型（在文件夹找文件时候，要选择文件类型后再找，因为他会先筛选一遍对应文件）

 再点Continue


应该PDF里面的东西太少了
 <img alt="" height="171" src="https://img-blog.csdnimg.cn/a83eb3a7903740fba779bcad8092c5c0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_8,color_FFFFFF,t_70,g_se,x_16" width="335"/>
按照流程，这一步一完，就算成功了
 <img alt="" height="440" src="https://img-blog.csdnimg.cn/eb509224c3ec41d9813bd2638db5ba10.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="662"/>


推荐：

[【数据隐藏】一起入门隐写吧，宝？word、图像、移动设备、文件压缩数据隐藏](https://blog.csdn.net/qq_53079406/article/details/123537834?spm=1001.2014.3001.5501)

 
