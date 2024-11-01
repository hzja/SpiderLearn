# 原创
：  【kali-信息收集】（1.5）系统指纹识别：Nmap、p0f

# 【kali-信息收集】（1.5）系统指纹识别：Nmap、p0f

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、工具](#%E4%BA%8C%E3%80%81%E5%B7%A5%E5%85%B7)

[2.1、Nmap（识别系统指纹信息）](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[2.2、p0f（指纹识别工具）](#2.2%E3%80%81p0f%EF%BC%88%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB%E5%B7%A5%E5%85%B7%EF%BC%89)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[安装：](#%E5%AE%89%E8%A3%85%EF%BC%9A)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
一些便携式计算机操作系统使用指纹识别来验证密码进行登录。 指纹识别是识别系统的一个典型模式， 包括指纹图像获取、 处理 、 特征提取和对等模块


---


---


## 二、工具

> 
<h3>2.1、Nmap（识别系统指纹信息）</h3>
<h4>使用：</h4>
[【端口扫描工具】nmap核心使用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)[nmap“扫描基础”“端口扫描技术”“服务和版本探测”“操作系统探测”“时间和性能”“防火墙/IDS躲避和哄骗”相关参考指南<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)
<hr/>
<h4>示例：</h4>

sudo nmap -O 219.140.194.134  




#### 示例：

### 2.2、p0f（指纹识别工具）

> 
<h4>简介：</h4>
pOf 是一款百分之百的被动指纹识别工具。它在不干涉双方通信的情况下，通过分析目标主机发出的数据包，对主机上的操作系统进行鉴别， 即使是在系统上装有性能良好的防火墙也没有问题
<hr/>
识别信息有：操作系统类型、端口、是否运行于防火墙之后、是否运行千NAT模式、是否运行于负载均衡膜式、远程系统已启动时间、远程系统的DSL 和ISP 信息等


> 
<h4>安装：</h4>
在kali中输入p0f，然后输入y确认安装



> 
<h4>命令：</h4>


<pre><code>用法: p0f [ …选项… ] ['过滤规则']

网络接口选项:
-i iface - 指定监听的网络接口
-r file - 读取由抓包工具抓到的网络数据包文件
-p - 设置 -i参数 指定的网卡 为混杂模式
-L - 列出所有可用接口


操作模式和输出设置:
-f file - 指定指纹数据库 (p0f.fp) 路径，不指定则使用默认数据库。(默认：/etc/p0f/p0f.fp)
-o file - 将信息写入指定的日志文件中。只有同一网卡的log文件才可以附加合并到本次监听中来。
-s name - 回答 unix socket 的查询 API
-u user - 以指定用户身份运行程序，工作目录会切换到到当前用户根目录下；
-d - 以后台进程方式运行p0f ,需要配合-0或者-s选项


性能相关的选项:
-S limit - 设置API并发数，默认为20，上限为100；
-t c,h - 设置连接超时时间 (30s,120m)
-m c,h - 设置最大网络连接数(connect)和同时追踪的主机数(host)(默认值: c = 1,000, h = 10,000)</code></pre>


> 
<h4>使用：</h4>
1、嗅探流经eth0的流量识别连接双方的指纹信息
<pre><code>sudo ./p0f -i eth0 'port 443'
</code></pre>
2、从文件中来识别系统
使用p0f 分析Wireshark 捕获的一个文件
<pre>`p0f -r /tmp/targethost.pcap -o p0f-result.log`</pre>


