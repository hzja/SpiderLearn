# 原创
：  【kali-信息收集】（1.4）识别活跃的主机/查看打开的端口：Nmap（网络映射器工具）

# 【kali-信息收集】（1.4）识别活跃的主机/查看打开的端口：Nmap（网络映射器工具）

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、工具](#%E4%BA%8C%E3%80%81%E5%B7%A5%E5%85%B7)

[2.1、Nmap（网络映射器工具）](#2.1%E3%80%81Nmap%EF%BC%88%E7%BD%91%E7%BB%9C%E6%98%A0%E5%B0%84%E5%99%A8%E5%B7%A5%E5%85%B7%EF%BC%89)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[2.2、Zenmap（图形化TCP端口扫描工具）](#2.2%E3%80%81Zenmap%EF%BC%88%E5%9B%BE%E5%BD%A2%E5%8C%96TCP%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F%E5%B7%A5%E5%85%B7%EF%BC%89)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
尝试渗透测试之前， 必须先识别在这个目标网络内活跃的主机。 在一个目标网络内，最简单的方法将是执行ping命令。


---


---


## 二、工具

### 2.1、Nmap（网络映射器工具）

> 
<h4>简介：</h4>
Nmap是一个网络扫描和嗅探工具包，也叫网络映射器(Network Mapper)
<hr/>
基本功能：一是探测一组主机是否在线；二是扫描主机端口， 嗅探所提供的 网络服务； 三是推断主机所用的橾作系统
<hr/>
用户利用Nmap来进行网络系统安全的评估， 而黑客则用于扫描网络。 例如， 通过向远程主机发送探测数据包， 获取主机的响应 ，并根据主机的端口开放悄况得到网络的安全状态。 从中寻找存在漏涧的目标主 机，从而实施下一步的攻击
<hr/>
Nmap使用TCP/IP协议栈指纹准确地判断目标主机的操作系统类型。 Nmap通 过对目标主机进行端口扫描， 找出有哪些端口正在目标主机上监听。（当侦测到目标主机上有多于一个开放的TCP端口、一个关闭的TCP端口和一个关闭的UDP端口时， Nmap的探测能力最优）


---


> 
<h4>原理：</h4>
Nmap工具的工作原理

 Nmap对目标主机进行一系列测试，利用得出的测试结果建立相应目标主机的Nmap指纹。最后， 将此Nmap指纹与指纹库中指纹进行查找匹配， 从而得出目标主机的操作系统类型。
<hr/>
Nmap主要扫描类型



> 
<h4>使用：</h4>
[【端口扫描工具】nmap核心使用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)[nmap“扫描基础”“端口扫描技术”“服务和版本探测”“操作系统探测”“时间和性能”“防火墙/IDS躲避和哄骗”相关参考指南<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)



> 
<h3>2.2、Zenmap（图形化TCP端口扫描工具）</h3>
<h4>简介：</h4>
Zemuap是Nmap官方推出的一款基千Nmap的安全扫描图形用户界面。它的设计目标是快速地扫描大型网络， 当然也可以使用它扫描单个主机。


#### 简介：
