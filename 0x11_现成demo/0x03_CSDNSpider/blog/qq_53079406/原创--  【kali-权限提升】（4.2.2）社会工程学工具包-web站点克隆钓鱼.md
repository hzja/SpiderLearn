# 原创
：  【kali-权限提升】（4.2.2）社会工程学工具包：web站点克隆钓鱼

# 【kali-权限提升】（4.2.2）社会工程学工具包：web站点克隆钓鱼

**目录**

[web站点克隆钓鱼](#web%E7%AB%99%E7%82%B9%E5%85%8B%E9%9A%86%E9%92%93%E9%B1%BC)

[ 1.1、第一步：启动SET](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8SET)

[1.2、第二步：选择模块](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[1.3、第三步：payload选择](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9Apayload%E9%80%89%E6%8B%A9)

[1.4、第四步：payload设置](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AEpayload)

[1.5、第五步：返回数据](#1.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE)

---


## web站点克隆钓鱼

> 
<h3> 1.1、第一步：启动SET</h3>
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
<h3>1.2、第二步：选择模块</h3>
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
<h3>1.3、第三步：payload选择</h3>
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
<h3>1.4、第四步：payload设置</h3>
我输入的3
凭证收集攻击


<pre><code>   1) Web Templates
网络模板
   2) Site Cloner
网站克隆
   3) Custom Import
自定义导入</code></pre>
选择第一项web模板
输入2


输入本机（攻击机）IP，和克隆的URL（我使用的QQ邮箱的登录页面）




> 
<h3>1.5、第五步：返回数据</h3>
我使用win11输入设定的ip
到了qq邮箱登录页面

密码输入登录。肯定会能在kali上收到账号密码
现在尝试快捷登录试一下（登录进正常页面了）

 现在看一下kali中收集到了什么信息
没有任何收获（所以不要找可以快捷登录的）



