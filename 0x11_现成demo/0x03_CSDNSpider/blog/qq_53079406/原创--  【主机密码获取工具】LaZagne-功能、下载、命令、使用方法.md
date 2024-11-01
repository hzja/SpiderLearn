# 原创
：  【主机密码获取工具】LaZagne：功能、下载、命令、使用方法

# 【主机密码获取工具】LaZagne：功能、下载、命令、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、功能：](#1.1%E3%80%81%E5%8A%9F%E8%83%BD%EF%BC%9A)

[1.2、局限性：](#1.2%E3%80%81%E5%B1%80%E9%99%90%E6%80%A7%EF%BC%9A)

[支持的软件：](#%E6%94%AF%E6%8C%81%E7%9A%84%E8%BD%AF%E4%BB%B6%EF%BC%9A)

[权限问题：](#%E6%9D%83%E9%99%90%E9%97%AE%E9%A2%98%EF%BC%9A)

[1.3、跨平台性：](#1.3%E3%80%81%E8%B7%A8%E5%B9%B3%E5%8F%B0%E6%80%A7%EF%BC%9A)

[1.4、免杀：](#1.4%E3%80%81%E5%85%8D%E6%9D%80%EF%BC%9A)

[现状：](#%E7%8E%B0%E7%8A%B6%EF%BC%9A)

[措施：](#%E6%8E%AA%E6%96%BD%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.1、GitHub：](#2.1%E3%80%81GitHub%EF%BC%9A)

[2.2、版本：](#2.2%E3%80%81%E7%89%88%E6%9C%AC%EF%BC%9A)

[三、环境：](#%E4%B8%89%E3%80%81%E7%8E%AF%E5%A2%83%EF%BC%9A)

[3.1、安装依赖： ](#3.1%E3%80%81%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96%EF%BC%9A%C2%A0)

[3.2、使用exe文件](#3.2%E3%80%81%E4%BD%BF%E7%94%A8exe%E6%96%87%E4%BB%B6)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、支持模块](#4.1%E3%80%81%E6%94%AF%E6%8C%81%E6%A8%A1%E5%9D%97)

[4.2、输出格式：](#4.2%E3%80%81%E8%BE%93%E5%87%BA%E6%A0%BC%E5%BC%8F%EF%BC%9A)

[4.3、示例：](#4.3%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[获取所有密码：](#%E8%8E%B7%E5%8F%96%E6%89%80%E6%9C%89%E5%AF%86%E7%A0%81%EF%BC%9A)

[获取一类软件的密码：](#%E6%8A%93%E5%8F%96%E7%89%B9%E5%AE%9A%E4%B8%80%E7%B1%BB%E8%BD%AF%E4%BB%B6%E7%9A%84%E5%AF%86%E7%A0%81%EF%BC%9A)

[获取指定软件的密码：](#%E6%8A%93%E5%8F%96%E7%89%B9%E5%AE%9A%E4%B8%80%E4%B8%AA%E8%BD%AF%E4%BB%B6%E7%9A%84%E5%AF%86%E7%A0%81%EF%BC%9A)

[获取所有密码并输出](#%E8%8E%B7%E5%8F%96%E6%89%80%E6%9C%89%E5%AF%86%E7%A0%81%E5%B9%B6%E8%BE%93%E5%87%BA)

[五、权限：](#%E4%BA%94%E3%80%81%E6%9D%83%E9%99%90%EF%BC%9A)

[5.1、windows](#5.1%E3%80%81windows)

[5.2、Linux](#5.2%E3%80%81Linux)

---


## 一、简介：

> 
<h3>1.1、功能：</h3>
一个开源应用程序，用于获取存储在本地计算机上（最常用的软件）的‎**‎**大量密码‎‎。每个软件使用不同的技术（纯文本、明文，API，自定义算法，数据库等）存储其密码。


> 
<h3>1.2、局限性：</h3>
<h4>支持的软件：</h4>
找到最常用的软件的密码（支持市面上大部分常用工具）
eg：浏览器、Git、SVN、Wifi、Databases 等，但是对聊天软件的支持不够本土化，主要支持一些国外的聊天软件
<hr/>
<h4>权限问题：</h4>
在提权后的root或system（高权限管理员账号）下运行
否则可能抓不到


#### 权限问题：

> 
<h3>1.3、跨平台性：</h3>
基于py开发的，跨平台性相对较好
如果目标机上没有 py 环境，将py转换成 exe再放到目标机上


> 
<h3>1.4、免杀：</h3>
<h4>现状：</h4>
LaZagne的Releases里面的exe已经被各种杀软记录了md5
<hr/>
<h4>措施：</h4>
自己打包如果将LaZagne转为exe，会产生新的md5，在md5检测层面有一定免杀效果，但是还是要经过行为的检测
可以用全新的环境打包（只装需要的包，减小体积，XP环境下打包也可以减少一点体积）



#### 措施：

---


---


## 二、下载：

> 
<h3>2.1、GitHub：</h3>
[AlessandroZ/LaZagne: Credentials recovery project (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne)
<hr/>
<h3>2.2、版本：</h3>
Windows 版本、Linux 版本、Mac版本



### 2.2、版本：

---


---


## 三、环境：

> 
（谈到环境，那真的是各种软件需求不同的版本，换来换去，干脆下一个吧）

 <img alt="" height="333" src="https://img-blog.csdnimg.cn/41cae4885cea4d3da81e0eaeb2212fe4.png" width="1006"/>
<hr/>
<h3>3.1、安装依赖： </h3>
python -m pip install -r requirements.txt
（我的没有找到合适的依赖）

<hr/>
<h3>3.2、使用exe文件</h3>
（直接使用打包好的exe文件）
链接：https://pan.baidu.com/s/19w6fbeS5_epOQmXdpSVmow?pwd=6zr7 <br/> 提取码：6zr7




---


### 3.2、使用exe文件

## 四、使用方法：

> 
<h3>4.1、支持模块</h3>
位置论点（选择主命令）：<br/>   {chats,mails,all,git,svn,windows,wifi,maven,sysadmin,browsers,games,multimedia,memory,databases,php}             
    chats（聊天）        
#Run chats module<br/>     mails（邮件）        
#Run mails module<br/>     all（所有）       
#Run all modules<br/>     git
#Run git module<br/>     svn
#Run svn module<br/>     windows
#Run windows module<br/>     wifi
#Run wifi module<br/>     maven
#Run maven module<br/>     sysadmin
#Run sysadmin module<br/>     browsers（浏览器）
#Run browsers module<br/>     games（游戏）
#Run games module<br/>     multimedia（多媒体）
#Run multimedia module<br/>     memory              
#Run memory module<br/>     databases(数据库)           
#Run databases module<br/>     php                
#Run php module
<hr/>
<h3>4.2、输出格式：</h3>

加上输出文件的位置 -output D:\……
**eg：**
laZagne.exe all -oN -output C:\……


### 4.2、输出格式：

> 
<h3>4.3、示例：</h3>
<h4>获取所有密码：</h4>
.\laZagne.exe all
（下图是普通用户）
还能发现2个



<hr/>


<h4>获取一类软件的密码：</h4>
eg：抓取浏览器
.\laZagne.exe browsers
（下图是普通用户）


<hr/>

<h4>获取指定软件的密码：</h4>
eg：获取火狐
.\laZagne.exe browsers -firefox
（下图是普通用户） 


<hr/>


<h4>获取所有密码并输出</h4>
.\laZagne.exe all -oN -output D:\BaiduNetdiskDownload\LaZagne-master\LaZagne-master

 <img alt="" height="482" src="https://img-blog.csdnimg.cn/8ec1af56cf8a45499920609c53745e69.png" width="1200"/>
 


 


#### 获取一类软件的密码：

---


#### 获取所有密码并输出

 

## 五、权限：

> 
<h3>5.1、windows</h3>
使用管理员身份
<hr/>
<h3>5.2、Linux</h3>
su root
sudo


### 5.2、Linux
