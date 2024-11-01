# 原创
：  【kali-权限提升】（4.2.4）社会工程学工具包：远控木马使用、设置、利用

# 【kali-权限提升】（4.2.4）社会工程学工具包：远控木马使用、设置、利用

**目录**

[远控木马](#%E8%BF%9C%E6%8E%A7%E6%9C%A8%E9%A9%AC)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、第一步：启动SET](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8SET)

[1.2、第二步：选择模块](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[1.3、第三步：payload选择](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9Apayload%E9%80%89%E6%8B%A9)

[1.4、第四步：payload设置](#1.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9Apayload%E8%AE%BE%E7%BD%AE)

[1.5、第五步：返回信息](#1.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%94%E5%9B%9E%E4%BF%A1%E6%81%AF)

[1.6、第六步：建立会话](#1.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E5%BB%BA%E7%AB%8B%E4%BC%9A%E8%AF%9D)

[1.7、第七步：利用](#1.7%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

---


## 远控木马

> 
<h3>简介：</h3>
SET 同时集成了木马生成工具，可以生成木马并调用MSF框架对远程主机进行控制


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
输入编号4，创建有效载荷和侦听器


<pre><code>1) Windows Shell Reverse_TCP               在受害者身上产生指挥外壳，然后寄回攻击者
2) Windows Reverse_TCP Meterpreter         在受害者身上产生仪表壳，然后寄回攻击者
3) Windows Reverse_TCP VNC DLL             在受害者上产生VNC服务器并将其发送回攻击者
4) Windows Shell Reverse_TCP X64           Windows X64命令外壳，反向TCP内联
5) Windows Meterpreter Reverse_TCP X64     连接回攻击者（Windows X64），MeterPreter
6) Windows Meterpreter Egress Buster       产生仪表式外壳，并通过多个端口找到港口房屋
7) Windows Meterpreter Reverse HTTPS       使用SSL通过HTTP通过隧道通信并使用MeterPreter
8) Windows Meterpreter Reverse DNS         使用主机名代替IP地址，并使用反向计量表
9) Download/Run your Own Executable        下载可执行文件并运行它
</code></pre>


> 
<h3>1.4、第四步：payload设置</h3>
选择Windows Reverse_TCP Meterpreter，在受害者身上产生仪表壳，然后寄回攻击者

输入2
设置监听的主机IP(攻击机IP地址)和端口
下面是在本地生成的木马程序payload.exe

 <img alt="" height="777" src="https://img-blog.csdnimg.cn/c5616c3f06ac4d6e9c4a6089c48c4f2d.png" width="884"/>

 /root/.set/
（需要使用root权限打开）<img alt="" height="511" src="https://img-blog.csdnimg.cn/f6ab55fc52de4aa99ac6e8a501dd09d7.png" width="644"/>



> 
<h3>1.5、第五步：返回信息</h3>
放到目标主机中（我直接拖过去失败了）

 是exe后缀，但是打开以后
好像是个文件夹

 就要考虑使用其他方式上传/下载到目标主机
<hr/>
为了测试我在虚拟机上下载了wmtool

（原文件路径（可能）和共享文件路径都需要root权限）



在win11里面就能看见了


<hr/>
为了安全起见我移动到了win7中（虚拟机）
点击运行

观察kali变化
（我点击运行了2次）
在这千万别和我一样傻等
按回车键（哈哈哈）

 


---


> 
<h3>1.6、第六步：建立会话</h3>
查看会话
输入sessions -i


激活第二条会话
输入sessions -i 2
（获得 Shell 后即可操控 Win 7 靶机）




> 
<h3>1.7、第七步：利用</h3>
执行命令，截图，提权……
sysinfo<br/> ls

 <img alt="" height="63" src="https://img-blog.csdnimg.cn/95324038b6f94505a2b65fa0dfddec2b.png" width="801"/>

