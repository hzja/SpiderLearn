# 原创
：  【kali-权限提升】（4.2.3）社会工程学工具包：二维码组合攻击

# 【kali-权限提升】（4.2.3）社会工程学工具包：二维码组合攻击

**目录**

[二维码攻击](#web%E7%AB%99%E7%82%B9%E5%85%8B%E9%9A%86%E9%92%93%E9%B1%BC)

[作用：](#%E4%BD%9C%E7%94%A8%EF%BC%9A)

[1.1、第一步：启动SET](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8SET)

[1.2、第二步：选择模块](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[1.3、第三步：payload选择](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9Apayload%E9%80%89%E6%8B%A9)

[1.4、第四步：payload设置](#1.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9Apayload%E8%AE%BE%E7%BD%AE)

[1.5、第五步：返回信息](#1.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%94%E5%9B%9E%E4%BF%A1%E6%81%AF)

---


## 二维码攻击

> 
<h3>作用：</h3>
二维码攻击需要与钓鱼网站等其他结合使用，以获取信息
其实也可以使用在线二维码生成平台
作用基本上是一样的


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
输入编号8，二维码攻击向量





> 
<h3>1.4、第四步：payload设置</h3>
（二维码攻击需要与钓鱼网站等其他结合使用，以获取信息）
我这里用的是爱奇艺
http://www.iqiyi.com/

然后下面就保存到给出的目录里面 


> 
<h3>1.5、第五步：返回信息</h3>
在/root/.set/reports/下找到了二维码

 用手机扫码试一下

和预期效果一样

