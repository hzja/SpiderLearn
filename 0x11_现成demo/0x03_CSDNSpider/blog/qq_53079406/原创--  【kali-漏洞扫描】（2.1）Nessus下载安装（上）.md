# 原创
：  【kali-漏洞扫描】（2.1）Nessus下载安装（上）

# 【kali-漏洞扫描】（2.1）Nessus下载安装（上）

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[ 1.2、下载（kali-Linux）：](#%C2%A01.2%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[1.3、安装：](#1.3%E3%80%81%E5%AE%89%E8%A3%85%EF%BC%9A)

[1.4、运行：](#1.4%E3%80%81%E8%BF%90%E8%A1%8C%EF%BC%9A)

[1.5、申请：](#1.5%E3%80%81%E7%94%B3%E8%AF%B7%EF%BC%9A)

[获取激活码：](#%E8%8E%B7%E5%8F%96%E6%BF%80%E6%B4%BB%E7%A0%81%EF%BC%9A)

[获取识别码](#%E8%8E%B7%E5%8F%96%E8%AF%86%E5%88%AB%E7%A0%81)

[到官网下载插件包](#%E5%88%B0%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BD%E6%8F%92%E4%BB%B6%E5%8C%85)

[安装插件包](#%E5%AE%89%E8%A3%85%E6%8F%92%E4%BB%B6%E5%8C%85)

[离线激活](#%E7%A6%BB%E7%BA%BF%E6%BF%80%E6%B4%BB)

[备份（建议）](#%E5%A4%87%E4%BB%BD%EF%BC%88%E5%BB%BA%E8%AE%AE%EF%BC%89)

[重启nessus](#%E9%87%8D%E5%90%AFnessus)

[再次访问](#%E5%86%8D%E6%AC%A1%E8%AE%BF%E9%97%AE)

[二、windows安装](#%E4%BA%8C%E3%80%81windows%E5%AE%89%E8%A3%85)

[2.1、下载](#2.1%E3%80%81%E4%B8%8B%E8%BD%BD)

[2.2、相同：](#2.2%E3%80%81%E7%9B%B8%E5%90%8C%EF%BC%9A)

[2.3、不同：](#2.3%E3%80%81%E4%B8%8D%E5%90%8C%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
Nessus号称是世界上最流行的漏洞扫描程序，全世界有超过75000个组织在使用它。  
该工具提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。  
Nessus不同于传统的漏洞扫描软件，Nessus可同时在本机或远端上遥控，进行系统的漏洞分析扫描。Nessus也是渗透测试重要工具之一


> 
<h3> 1.2、下载（kali-Linux）：</h3>
官网：
[Download Nessus | Tenable®<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://www.tenable.com/downloads/nessus?loginAttempted=true](https://www.tenable.com/downloads/nessus?loginAttempted=true)<img alt="" height="745" src="https://img-blog.csdnimg.cn/25fa1652aa22401e9bba9367def391f9.png" width="1077"/>





> 
<h3>1.3、安装：</h3>
可以直接在官网下载
可以找到合适的版本

 解压安装软件包
 sudo dpkg -i Nessus-8.15.5-debian6_amd64.deb 



> 
<h3>1.4、运行：</h3>
启动服务
sudo service nessusd start


初步登录nessus，浏览器访问 https://localhost:8834，初始化扫描器



选择 Managed Scanner-----&gt;Managed by Tenable.sc

 <img alt="" height="734" src="https://img-blog.csdnimg.cn/255039a5203a4fc4a4d568d731c0ed08.png" width="1078"/>
创建账号密码
用户名和密码
默认密码可以设置成nessus:nessus(主要是方便记)






> 
<h3>1.5、申请：</h3>
<h4>获取激活码：</h4>
nessus官方申请激活码，邮箱必须正确，用来接收激活码
（可以使用网上的临时邮箱）
[获取激活码|内瑟斯®|成立® (tenable.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://www.tenable.com/products/nessus/activation-code](https://www.tenable.com/products/nessus/activation-code)选择16个ip的（最右侧）


<hr/>
<h4>获取识别码</h4>
sudo /opt/nessus/sbin/nessuscli fetch --challenge


<hr/>
<h4>到官网下载插件包</h4>
输入申请的激活码，以及上一步得到的识别码
[Tenable Network Security (nessus.org)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://plugins.nessus.org/v2/offline.php](https://plugins.nessus.org/v2/offline.php)<img alt="" height="556" src="https://img-blog.csdnimg.cn/68e43dc5ad0347d0838e9d1806c51a33.png" width="1111"/>
 分别为插件下载地址、证书

证书下载地址


<hr/>
<h4>安装插件包</h4>
移到nessus文件夹下
在这个文件夹位置，右键打开终端输入
/opt/nessus/sbin/nessuscli update all-2.0.tar.gz



<hr/>
<h4>离线激活</h4>
/opt/nessus/sbin/nessuscli fetch --register-offline ./nessus.license

提示正确注册
<hr/>
<h4>备份（建议）</h4>
sudo cp -r /opt/nessus/lib/nessus/plugins/ ./

<hr/>
<h4>重启nessus</h4>
sudo service nessusd restart

<hr/>
<h4>再次访问</h4>
浏览器访问Nessus(https://localhost:8834)
会初编译插件,时间有点长，要个几十分钟


 


#### 获取识别码

---


#### 安装插件包

---


#### 备份（建议）

---


#### 再次访问

<br/>  

---


---


## 二、windows安装

> 
<h3>2.1、下载</h3>
我下的64位的msi安装程序




> 
<h3>2.2、相同：</h3>
初始登录，设置密码，申请激活码、创建plugin_feed_info.inc文件内容相同


> 
<h3>2.3、不同：</h3>
1、nessus需要安装在c盘下
默认是这个目录 

<hr/>
2、也是在文件目录下使用管理员身份获取识别码
cd C:\Program Files\Tenable\Nessus
nessuscli.exe fetch --challenge


<hr/>
3、因为自己的邮箱使用过一次
（然后使用的网上的临时邮箱）

 <img alt="" height="228" src="https://img-blog.csdnimg.cn/64a1be98c7024c55af490864abbd0687.png" width="840"/>
<img alt="" height="611" src="https://img-blog.csdnimg.cn/7aa6d2baa06e4329b6905010d4f2473e.png" width="1200"/> 基本上一样了

<hr/>
 4、更新插件


nessuscli.exe update ./all-2.0.tar.gz

<hr/>
 5、配置文件位置不同
plugin_feed_info.inc文件复制到以下目录中
C:\ProgramData\Tenable\Nessus\nessus
C:\ProgramData\Tenable\Nessus\nessus\plugins

<hr/>
5、服务重启
在windows的服务列表中找到 Tenable Nessus 服务重启




---


---

