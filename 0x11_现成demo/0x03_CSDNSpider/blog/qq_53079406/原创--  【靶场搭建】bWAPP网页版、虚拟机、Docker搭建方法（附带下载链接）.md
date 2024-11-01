# 原创
：  【靶场搭建】bWAPP网页版、虚拟机、Docker搭建方法（附带下载链接）

# 【靶场搭建】bWAPP网页版、虚拟机、Docker搭建方法（附带下载链接）

**目录**

[一、前言](#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[ 2.1、网页版下载](#%C2%A02.1%E3%80%81%E7%BD%91%E9%A1%B5%E7%89%88%E4%B8%8B%E8%BD%BD)

[2.1.1、网盘：](#2.1.1%E3%80%81%E7%BD%91%E7%9B%98%EF%BC%9A)

[2.1.2、GitHub：](#2.1.2%E3%80%81GitHub%EF%BC%9A)

[2.1.3、官网：](#2.1.3%E3%80%81%E5%AE%98%E7%BD%91%EF%BC%9A)

[2.2、虚拟机下载](#2.2%E3%80%81%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD)

[2.3、Docker 下载](#2.3%E3%80%81Docker%20%E4%B8%8B%E8%BD%BD)

[三、安装](#%E4%B8%89%E3%80%81%E5%AE%89%E8%A3%85)

[3.1、配置数据库、安装](#3.1%E3%80%81%E9%85%8D%E7%BD%AE%E6%95%B0%E6%8D%AE%E5%BA%93%E3%80%81%E5%AE%89%E8%A3%85)

[3.1.1、第一步：填写数据库信息](#3.1.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%A1%AB%E5%86%99%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BF%A1%E6%81%AF)

[3.1.2、第二步：进行安装](#3.1.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%BF%9B%E8%A1%8C%E5%AE%89%E8%A3%85)

[3.2、登录使用](#3.2%E3%80%81%E7%99%BB%E5%BD%95%E4%BD%BF%E7%94%A8)

[3.2.1、第三步：登录页面](#3.2.1%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2)

[3.2.2、第四步：登录](#3.2.2%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%99%BB%E5%BD%95)

---


 

## 一、前言

> 
<h3>1.1、简介：</h3>
bWAPP 是一款非常好的漏洞演示平台，其包含有 100 多个漏洞。
<hr/>
安装方法：
①下载网页版，在 Apache+MySQL+PHP 环境下配置
②下载虚拟机（有1G多一点）
③使用 Docker 安装


---


## 二、下载：

> 
<h3> 2.1、网页版下载</h3>
推荐网盘、GitHub下载
<h4>2.1.1、网盘：</h4>
（现在那个官网好像没工作了，我用c币为大家下好）
链接：https://pan.baidu.com/s/10GZHgDo1Kb87F-l_vxO7RQ?pwd=a9ty <br/> 提取码：a9ty

<h4>2.1.2、GitHub：</h4>
（突然找到GitHub里面也有，花冤枉钱了）：
[raesene/bWAPP (github.com)<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://github.com/raesene/bWAPP](https://github.com/raesene/bWAPP)

<h4>2.1.3、官网：</h4>
[bWAPP - Browse /bWAPP at SourceForge.net<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://sourceforge.net/projects/bwapp/files/bWAPP/](https://sourceforge.net/projects/bwapp/files/bWAPP/)
点击下载最新的

 （官网可能已经下不了了，上面有网盘链接）
（下载完以后，往后翻到安装）


#### 2.1.2、GitHub：

> 
<h3>2.2、虚拟机下载</h3>
下载之后解压，用 VMware 打开即可<br/> 默认账号密码为：bee/bug
官网下载连接：
[bWAPP - Browse /bee-box at SourceForge.net<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://sourceforge.net/projects/bwapp/files/bee-box/](https://sourceforge.net/projects/bwapp/files/bee-box/)





> 
<h3>2.3、Docker 下载</h3>
下载项目到服务器上
1.、创建镜像
docker build -t bwapp
<hr/>
2.、创建容器
docker run -it --name bwapp_vul -p 0.0.0.0:8080:80 bwapp /bin/bash 
docker run -d --name bwapp_vul -p 0.0.0.0:8080:80 bwapp 
<hr/>
3、拉取项目 bwapp.git
docker run -d -p 8080:80 raesene/bwapp
访问 localhost:8080/bWAPP/ 
访问 localhost:8080/install.php（或者是127.0.0.1）


---


---


## 三、安装

> 
<h3>3.1、配置数据库、安装</h3>
<h4>3.1.1、第一步：填写数据库信息</h4>
bWAPP\admin下的settings.php


修改数据库连接
改为自己的数据库root的用户名，密码
（为减低风险，可以在安装好后，新建一个当前数据库的高级权限，再修改配置）

<hr/>

<h4>3.1.2、第二步：进行安装</h4>
然后访问 bWAPP 进行安装：localhost:8080/bwapp/install
（有的是127.0.0.1，根据自己设置的来，有时候不带端口号会报错）
将www后面的输入到losthost:8080/后面
下面是我的文件的位置


我在URL输入的是
localhost:8080/bWAPP/bWAPP/install.php
然后点击


安装成功，现在再去看数据库，其实已经有了bwapp了<img alt="" height="650" src="https://img-blog.csdnimg.cn/80d6b748ce454e089b238f11457d75e3.png" width="1072"/>



#### 3.1.2、第二步：进行安装

> 
<h3>3.2、登录使用</h3>
<h4>3.2.1、第三步：登录页面</h4>
localhost:8080/bWAPP/bWAPP/login.php
（就是把后面的改为login.php）


<hr/>
<h4>3.2.2、第四步：登录</h4>
默认密码
bee/bug
（settings.php中默认设置的）






#### 3.2.2、第四步：登录
