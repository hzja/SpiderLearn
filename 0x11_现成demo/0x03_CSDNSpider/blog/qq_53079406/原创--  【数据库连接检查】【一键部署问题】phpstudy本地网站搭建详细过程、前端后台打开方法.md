# 原创
：  【数据库连接检查】【一键部署问题】phpstudy本地网站搭建详细过程、前端后台打开方法

# 【数据库连接检查】【一键部署问题】phpstudy本地网站搭建详细过程、前端后台打开方法

**目录**

<img alt="" height="23" src="https://img-blog.csdnimg.cn/c660db5e99424c2bb303b7ad1c10473b.png" width="23"/>[​搭建本地网站](#%E6%90%AD%E5%BB%BA%E6%9C%AC%E5%9C%B0%E7%BD%91%E7%AB%99)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​搭建基础： ](#%E6%90%AD%E5%BB%BA%E5%9F%BA%E7%A1%80%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​准备简阶段：](#%E5%87%86%E5%A4%87%E7%AE%80%E9%98%B6%E6%AE%B5%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​其他管理软件](#%E5%85%B6%E4%BB%96%E7%AE%A1%E7%90%86%E8%BD%AF%E4%BB%B6)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​开始搭建](#%E5%BC%80%E5%A7%8B%E6%90%AD%E5%BB%BA)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​网站和数据库配置阶段](#%E7%BD%91%E7%AB%99%E5%92%8C%E6%95%B0%E6%8D%AE%E5%BA%93%E9%85%8D%E7%BD%AE%E9%98%B6%E6%AE%B5)

[​](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%BC%80%E5%90%AF%E6%9C%8D%E5%8A%A1Apache%E5%92%8CMySQL)<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[ 第一步：开启服务Apache和MySQL](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%BC%80%E5%90%AF%E6%9C%8D%E5%8A%A1Apache%E5%92%8CMySQL)

[​](#%E2%80%8B)<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第二步：创建网站](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%9B%E5%BB%BA%E7%BD%91%E7%AB%99)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​安装网站程序](#%E5%AE%89%E8%A3%85%E7%BD%91%E7%AB%99%E7%A8%8B%E5%BA%8F)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第三步：选择建站系统](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E5%BB%BA%E7%AB%99%E7%B3%BB%E7%BB%9F)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​简介：](#%E2%80%8B%E7%AE%80%E4%BB%8B%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第四步：对建站系统的配置](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%AF%B9%E5%BB%BA%E7%AB%99%E7%B3%BB%E7%BB%9F%E7%9A%84%E9%85%8D%E7%BD%AE)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​检查数据库连接](#%E6%A3%80%E6%9F%A5%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BF%9E%E6%8E%A5)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第一步：进行登录](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%BF%9B%E8%A1%8C%E7%99%BB%E5%BD%95)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第二步：查看那个创建数据库的情况，并重新配置好 ](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E9%82%A3%E4%B8%AA%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E6%83%85%E5%86%B5%EF%BC%8C%E5%B9%B6%E9%87%8D%E6%96%B0%E9%85%8D%E7%BD%AE%E5%A5%BD)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​继续安装](#%E7%BB%A7%E7%BB%AD%E5%AE%89%E8%A3%85)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[​第一步：浏览器重新进入，连接数据库](#%E2%80%8B%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%B5%8F%E8%A7%88%E5%99%A8%E9%87%8D%E6%96%B0%E8%BF%9B%E5%85%A5%EF%BC%8C%E8%BF%9E%E6%8E%A5%E6%95%B0%E6%8D%AE%E5%BA%93)

[​](#%E2%80%8B%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%A0%B9%E6%8D%AE%E6%8F%90%E7%A4%BA%E5%AE%89%E8%A3%85)<img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>[第二步：根据提示安装](#%E2%80%8B%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%A0%B9%E6%8D%AE%E6%8F%90%E7%A4%BA%E5%AE%89%E8%A3%85)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​一键部署](#%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​Apache【AH00526】问题](#Apache%E3%80%90AH00526%E3%80%91%E9%97%AE%E9%A2%98)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>[​打开网站前端](#%E2%80%8B%E6%89%93%E5%BC%80%E7%BD%91%E7%AB%99%E5%89%8D%E7%AB%AF)

---


## <img alt="" height="23" src="https://img-blog.csdnimg.cn/c660db5e99424c2bb303b7ad1c10473b.png" width="23"/>搭建本地网站

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>搭建基础： 

> 
 推荐下载phpstudy这种集成环境，就可以避免一个一个下载apache、MySQL等
（我相信在看的各位都有phpstudy，俗称小皮面板）
如果没有的就安装一个把（官方下一个，都是免费的）

下载完后，首页就是一个已经有的套件



### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>准备简阶段：

> 
搭建网站，一般需要Apache/Nginx、FTP、Mysql
Apache/Nginx：都是web服务器，都能执行网站文件。Apache稳定性不错，拓展多，而Nginx并发能力强，运行效率高，各有千秋。
FTP：（本地搭建不需要）通过FTP软件连接上服务器，进行文件管理（服务器支持FTP协议）
MySQL：这个应该就都知道了，存储和管理数据文件
PHP.nts：php运行支持程序


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>其他管理软件

> 
 phpMyadmin
 可以对数据库进行管理，而且可以很方便找到后面数据库连接的错误（推荐）


可以直接在phpstudy中的软件管理里面下载



### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>开始搭建

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>网站和数据库配置阶段

> 
<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/> 第一步：开启服务Apache和MySQL</h4>


<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第二步：创建网站</h4>


我门这次搭建的是本地的
域名可以随便写（前提，勾选同步hosts，它就会先从本地解析）
勾选创建数据库、同步Hosts
选择php版本（不选，会导致严重错误，这个情况在一键部署的时候会出现）






点击创建数据库的时候，会弹出数据库的创建（这个要记住，后面网站连接数据库的时候需要）




点击确认







#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第二步：创建网站

 <img alt="" src="https://img-blog.csdnimg.cn/7c1c4c15940b41edaf275fa8b82cbc4b.png"/>

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>安装网站程序

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第三步：选择建站系统

> 
安装网站程序（可在官网下载，也可在phpstudy中一键部署）
[下载 | WordPress.org China 简体中文](https://cn.wordpress.org/download/)
这个根据搭建什么类型的网站就下载相应的建站系统
 <img alt="" height="787" src="https://img-blog.csdnimg.cn/a3d7acc58f2949ce9b7d9aba7d317b7e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1000"/>


（用WordPress做示范）
<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>简介：</h4>
WordPress是使用PHP语言开发的博客平台，用户可以在支持PHP和MySQL数据库的服务器上架设属于自己的网站。也可以把 WordPress当作一个内容管理系统（CMS）来使用。




#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第四步：对建站系统的配置

> 
 <img alt="" height="787" src="https://img-blog.csdnimg.cn/28f9ad8fb8594987a8b018b19187f999.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1000"/>



然后把下载的wordpress文件解压到这个根目录下面



修改wp-confi-sample.php




修改为自己创建数据库时候的账号密码等，localhost（根据自己主机的情况看需不需要改为127.0.0.1）







在浏览器上输入本地网站的域名，会首先访问hosts，中的对应网站
点击现在就开始





错误时就会连接失败，在上述配置没问题的前提下，开始下面的检查过程，若成功直接安装即可



 <img alt="" src="https://img-blog.csdnimg.cn/47b7e4a24c924cd4ab9d8d55ca193e10.png"/>

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>检查数据库连接

此时phpMyAdmin就能发挥作用了

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第一步：进行登录

> 
其实发现用创建的数据库是登不进去的（因为我们登错号了）


应该用这个号登录



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第二步：查看那个创建数据库的情况，并重新配置好 

> 
可以看出，其实在phpstudy中没有成功创建数据库的


现在就创建成功了


然后在这个新建的数据库中，添加有所有权限的用户


创建成功



### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>继续安装

> 
<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第一步：浏览器重新进入，连接数据库</h4>
再去浏览器输入域名，并连接数据库就成功了


<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第二步：根据提示安装</h4>
接下的安装程序就是非常简单了











#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/cf2716dd5c854fac85ed68be87ab3024.png" width="23"/>第二步：根据提示安装

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>一键部署

> 
过程有异曲同工之妙，只是更简单了一点点




 该配置的连接还是要配置的，就不再一 一开始了



 <img alt="" src="https://img-blog.csdnimg.cn/2094f305f7a74d58afc897465af28956.png"/>

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>Apache【AH00526】问题

> 
 <img alt="" height="405" src="https://img-blog.csdnimg.cn/4121dc9adf484aa391cf3a4e43fb9f6f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_15,color_FFFFFF,t_70,g_se,x_16" width="646"/>
这个问题是因为对应网站没有选择一个php支持程序，导致的空白
（检查半天才发现，:)  ） 


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/a411ac12792d47dfb2d078f84c6c9e8b.png" width="23"/>打开网站前端

> 

 <img alt="" height="787" src="https://img-blog.csdnimg.cn/99f6a522149644209ab1abc17c4e2ff6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1000"/>


