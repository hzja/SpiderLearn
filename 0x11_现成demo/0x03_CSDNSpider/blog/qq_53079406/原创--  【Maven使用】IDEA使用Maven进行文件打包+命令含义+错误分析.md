# 原创
：  【Maven使用】IDEA使用Maven进行文件打包+命令含义+错误分析

# 【Maven使用】IDEA使用Maven进行文件打包+命令含义+错误分析

**目录**

[一、Maven](#%E4%B8%80%E3%80%81Maven)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1.1、clean（清除）](#1.1.1%E3%80%81clean%EF%BC%88%E6%B8%85%E9%99%A4%EF%BC%89)

[1.1.2、validate（验证）](#1.1.2%E3%80%81validate%EF%BC%88%E9%AA%8C%E8%AF%81%EF%BC%89)

[1.1.3、compile（编译）](#1.1.3%E3%80%81compile%EF%BC%88%E7%BC%96%E8%AF%91%EF%BC%89)

[1.1.4、test（测试）](#1.1.4%E3%80%81test%EF%BC%88%E6%B5%8B%E8%AF%95%EF%BC%89)

[1.1.5、package（打包）](#1.1.5%E3%80%81package%EF%BC%88%E6%89%93%E5%8C%85%EF%BC%89)

[1.1.6、vertify（验证）](#1.1.6%E3%80%81vertify%EF%BC%88%E9%AA%8C%E8%AF%81%EF%BC%89)

[1.1.7、install（安装）](#1.1.7%E3%80%81install%EF%BC%88%E5%AE%89%E8%A3%85%EF%BC%89)

[1.1.8、site（站点）](#1.1.8%E3%80%81site%EF%BC%88%E7%AB%99%E7%82%B9%EF%BC%89)

[1.1.9、deploy（配置部署）](#1.1.9%E3%80%81deploy%EF%BC%88%E9%85%8D%E7%BD%AE%E9%83%A8%E7%BD%B2%EF%BC%89)

[1.2、打包：](#1.2%E3%80%81%E6%89%93%E5%8C%85%EF%BC%9A)

[二、使用步骤：](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[2.1、第一步：加载文件](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%8A%A0%E8%BD%BD%E6%96%87%E4%BB%B6)

[2.1.1、错误提示：](#2.1.1%E3%80%81%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA%EF%BC%9A)

[ 2.2、第二步：Maven窗口](#%C2%A02.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9AMaven%E7%AA%97%E5%8F%A3)

[2.2.1、错误提示：](#2.2.1%E3%80%81%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA%EF%BC%9A)

[2.3、第三步：开始打包](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%BC%80%E5%A7%8B%E6%89%93%E5%8C%85)

[2.3.1、问题提示：](#2.3.1%E3%80%81%E9%97%AE%E9%A2%98%E6%8F%90%E7%A4%BA%EF%BC%9A)

---


（你相信光嘛！）

---


## 一、Maven

> 
<h3>1.1、简介：</h3>



> 
<h4>1.1.1、clean（清除）</h4>
清除之前（install）构建生成的所有文件，清除该项目路径下Target目录
但是不会删除本地的maven仓库已经生成的jar文件。
<h4>1.1.2、validate（验证）</h4>
验证项目正确性
验证信息完整可用
<h4>1.1.3、compile（编译）</h4>
编译选定项目的源代码，成.class文件（JAVA识别.class）
一般是编译src/main/java和src/test/java下面的文件
生成target目录，把配置文件和.class文件放到classes文件夹里
可重复生成
<h4>1.1.4、test（测试）</h4>
用合适的框架进行测试，测试compile编译出来的代码
测试文件一般不加包和部署
<h4>1.1.5、package（打包）</h4>
获取compile中编译好的文件，并将其打包为指定格式，打包方式有jar，pom，war
注：若项目A依赖项目于B，需要使用install安装到本地仓库。因为打包B时，只打包到B的target下，因此A找不到它所依赖的B项目，编译A就会报错
<h4>1.1.6、vertify（验证）</h4>
验证test结果
是否有效、满足标准
<h4>1.1.7、install（安装）</h4>
将软件包安装都本地仓库
让本地其他项目可以用到它（让其它项目依赖）
在项目路径下生成class文件和jar包，同时在本地maven仓库生成jar文件
<h4>1.1.8、site（站点）</h4>
生成项目的站点文档
在项目的“target/site”文件夹中
<h4>1.1.9、deploy（配置部署）</h4>
复制到远程仓库（最终文件）
与他人共享项目


#### 1.1.2、validate（验证）

#### 1.1.4、test（测试）

#### 1.1.6、vertify（验证）

#### 1.1.8、site（站点）

### 1.2、打包：

> 
常见的打包方法：
执行clean后
要么再点击 package
要么再点击 install


---


 

## 二、使用步骤：

> 
<h3>2.1、第一步：加载文件</h3>
Help-----Find Action------输入Maven Projects--------**+ Add Maven Projects**





选择自己的项目（或者是GitHub上的需要）


第一次使用，右下角，会提示下载什么
点击总是下载
然后自己会下载需要的环境等





<h4>2.1.1、错误提示：</h4>
如果你的项目不是Maven
就无法识别的，会提示错误
eg：



> 
<h3> 2.2、第二步：Maven窗口</h3>
打开Maven视窗
View - Tool Windows - Maven



<h4>2.2.1、错误提示：</h4>
如果不是Maven文件，就不可能识别，不会有Maven窗口（切莫跳过第一步）
但是如果把它放在和Maven文件一起就又有了（题外话）


> 
<h3>2.3、第三步：开始打包</h3>
文件----Lifecycle------clean


也需要下载相关环境<img alt="" height="952" src="https://img-blog.csdnimg.cn/bdba24b319f94f638c25c8b6295f12a1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

BUILD SUCCESS
 相关环境下载成功了，并执行了<img alt="" height="894" src="https://img-blog.csdnimg.cn/a622a6e0d9a7400186b73c59b58e1542.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>




install--------Run Maven Build
（进行项目打包）


开始自动下载相关依赖
 （下的时间可能有亿丢丢长）


下载完成后，当出现了BUILD SUCCESS就打包成功了




<h4>2.3.1、问题提示：</h4>

Maven的镜像也可能需要换一换，自带的可能会有问题
随着依赖包的更新，有的依赖包会过时
需要对pom.xml里的代码进行添加、修改等操作




建议：找时间学一学相关知识

直接使用前人打包好的（最后还是要学一下）

 
