# 原创
：  【kali-权限提升】（4.2.1）社会工程学工具包（上）：web钓鱼模块

# 【kali-权限提升】（4.2.1）社会工程学工具包（上）：web钓鱼模块

**目录**

[一、社会工程学工具包（SET）](#%E4%B8%80%E3%80%81%E7%A4%BE%E4%BC%9A%E5%B7%A5%E7%A8%8B%E5%AD%A6%E5%B7%A5%E5%85%B7%E5%8C%85%EF%BC%88SET%EF%BC%89)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、使用](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8)

[2.1、第一步：启动SET](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8SET)

[2.2、第二步：选择模块](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[2.3、第三步：payload选择](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9Apayload%E9%80%89%E6%8B%A9)

[2.4、第四步：payload设置](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AEpayload)

[ 2.5、第五步：返回数据](#%C2%A02.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE)

---


## 一、社会工程学工具包（SET）

> 
<h3>1.1、概述：</h3>
SET利用人们的好奇心、信任、贪婪及一些愚猛的错误， 攻击人们自身存在的弱点。使用SET可以传递攻击载荷到目标系统， 收集目标系统数据， 创建待久后门， 进行中间人攻击等


---


---


## 二、使用

（payload选择自己合适的）

> 
<h3>2.1、第一步：启动SET</h3>
输入sudo setoolkit
（或者在工具菜单中找到后打开）

输出的信息详细的介绍了SET。该信息在第一次运行时， 才会显示
接受这部分信息后， 才可进行其他操作。
<hr/>
输入y

 显示了社会工程学工具包的创建者、版本、代号及菜单信息
选择相应的编号进行操作


<pre><code>   1) Social-Engineering Attacks
社会工程攻击
   2) Penetration Testing (Fast-Track)
渗透测试（快速轨道）
   3) Third Party Modules
第三方模块
   4) Update the Social-Engineer Toolkit
更新社交工程工具包
   5) Update SET configuration
更新设置配置
   6) Help, Credits, and About
帮助，学分等
</code></pre>



> 
<h3>2.2、第二步：选择模块</h3>
选择攻击社会工程学，在菜单中的编号为1
输入1
显示了攻击社会工程学的菜单选项， 这时就可以选择攻击工程学的类型， 然后进行攻击
<img alt="" height="597" src="https://img-blog.csdnimg.cn/b4b2f6f7a78b49d4a13ec4b72bb83639.png" width="873"/> <img alt="" height="257" src="https://img-blog.csdnimg.cn/afab3c9ee3244c4687032a02b751c9d1.png" width="870"/>
<pre><code>   1) Spear-Phishing Attack Vectors
鱼叉式钓鱼攻击向量
   2) Website Attack Vectors
网站攻击向量
   3) Infectious Media Generator
感染性媒体生成器
   4) Create a Payload and Listener
创建有效载荷和侦听器
   5) Mass Mailer Attack
大众邮件攻击
   6) Arduino-Based Attack Vector
基于Arduino的攻击向量
   7) Wireless Access Point Attack Vector
无线访问点攻击矢量
   8) QRCode Generator Attack Vector
QRCode Generator攻击向量
   9) Powershell Attack Vectors
Powershell攻击向量
  10) Third Party Modules
第三方模块
</code></pre>



> 
<h3>2.3、第三步：payload选择</h3>
输入编号2，网站攻击向量
输出的信息显示了可生成的所有攻击载荷

<pre><code>   1) Java Applet Attack Method
Java小程序攻击方法
   2) Metasploit Browser Exploit Method
metasploit浏览器利用方法
   3) Credential Harvester Attack Method
凭证收集攻击法
   4) Tabnabbing Attack Method
Tabnabbing攻击方法
   5) Web Jacking Attack Method
网络升压攻击方法
   6) Multi-Attack Web Method
多攻击Web方法
   7) HTA Attack Method
HTA攻击方法</code></pre>



> 
<h3>2.4、第四步：payload设置</h3>
我输入的3
凭证收集攻击


<pre><code>   1) Web Templates
网络模板
   2) Site Cloner
网站克隆
   3) Custom Import
自定义导入</code></pre>
选择第一项web模板
输入1

设置用于钓鱼的IP地址(此处默认Kali本机IP，同时会默认设定80端口，故需要提前执行命令`sudo systemctl stop apache2`关闭Apache服务，避免80端口占用)，然后选择钓鱼的网站 
选择谷歌登录

 开始了





> 
<h3> 2.5、第五步：返回数据</h3>
前提：攻击机未关闭防火墙可能就别人访问不了
sudo systemctl stop firewalld 
（我就遇到了访问超时，可惜被我发现了）



我在虚拟机Win上面访问 Kali 的IP地址
进去是谷歌登录页面
输入账号和密码(登录后会进行跳转到谷歌官网)

此时账号密码会在攻击机中显示



