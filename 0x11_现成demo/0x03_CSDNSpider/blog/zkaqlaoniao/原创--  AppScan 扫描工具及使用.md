# 原创
：  AppScan 扫描工具及使用

# AppScan 扫描工具及使用

#### 一、简介

原名 watchire Appscan ,2007年被IBM收购，成为IBM Appscan。**IBM AppScan是一款非常好用且功能强大的Web 应用安全测试工具**

曾以 Watchfire AppScan 的名称享誉业界，Rational AppScan **可自动化 Web 应用的安全漏洞评估工作，能扫描和检测所有常见的 Web 应用安全漏洞**

例如 SQL 注入（SQL-injection）、跨站点脚本攻击（cross-site scripting）、缓冲区溢出（buffer overflow）及最新的 Flash/Flex 应用及 Web 2.0 应用曝露等方面安全漏洞的扫描。

#### 二、优缺点

###### **1.优点**
1.  知名度高，历史悠久，一款只针对于Web Application的扫描工具 1.  扫描过程：探索阶段 -&gt; 测试阶段。不同于主流的拥有截断代理功能扫描器，Appscan将浏览器集成到内部中进行手动爬网等，非常方便。 1.  第一个扫描过程如果发现新的URL地址，那么第一个扫描结束后，下一个对于新URL地址的扫描自动开始。  
###### **2.缺点**
1.  更新慢 1.  appscan扫描太慢，不如AWVS扫描快 
#### 三、安装

1.首先双击“AppScan_Setup_10.0.0.exe”开始安装，选择简体中文；

2.勾选“我接受许可协议中的全部条款”，然后继续安装；

3.选择软件安装路径，默认即可；

4.安装完成后先不要运行软件，点击完成退出引导；

**5.将破解补丁文件夹中rcl_rational.dll复制到软件安装目录下替换；**

6.然后运行AppScan10，点击”帮助-许可证-切换到IBM许可证“；

<br/> 7.选择打开Appscan License Manager

在”许可证配置-节点锁定许可证文件“中AppScanStandard.txt作为许可证；

<br/>  

8.至此，appscan10中文破解版成功激活，所有功能全部免费使用。

#### 四、主要模块介绍

###### 1.常规式扫描

> 
文件 —&gt; 新建 —&gt; 扫描Web应用程序 。ps：扫描Web应用程序之后，一直按照向导操作即可完成扫描。


> 
配置扫描向导


> 
网站的身份认证


> 
配置扫描策略


> 
策略优化，直接点击下一步即可


> 
一般来说，选择第三个，因为扫描的过程是：手动爬网+自动爬网+主动扫描


> 
手动探索结束后，添加所有


> 
有了爬网和初步检测的结果


> 
进行扫描，选择第二个，先让appscan做一个自动爬网


> 
当手动爬网，自动爬网结束之后，接下来就是扫描


> 
当第一次扫描结束后，appscan会发现新的URL，建议再做一次扫描，我就不演示了，步骤和上面一样。<br/> 分析扫描结果：


> 
手动测试验证扫描结果，类似于burp里面Repeater


###### 2.配置式扫描

###### 3.报告模块

###### 4.PowerTools辅助工具

#### 五、参考文章

> 
https://blog.csdn.net/qq_38317509/article/details/80981430 # 渗透测试之AppScan篇<br/> https://blog.csdn.net/qq_38317509/article/details/81347219 # Appscan工具的使用
  申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。
<h6>**免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/></h6>
渗透工具

技术文档、书籍
<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题
帮助你在面试中脱颖而出

视频
基础到进阶
环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等
<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线


