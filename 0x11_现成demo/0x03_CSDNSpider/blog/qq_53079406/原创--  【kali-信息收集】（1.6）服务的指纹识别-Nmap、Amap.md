# 原创
：  【kali-信息收集】（1.6）服务的指纹识别：Nmap、Amap

# 【kali-信息收集】（1.6）服务的指纹识别：Nmap、Amap

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、工具](#%E4%BA%8C%E3%80%81%E5%B7%A5%E5%85%B7)

[2.1、Nmap（识别服务指纹信息）](#2.1%E3%80%81Nmap%EF%BC%88%E8%AF%86%E5%88%AB%E6%9C%8D%E5%8A%A1%E6%8C%87%E7%BA%B9%E4%BF%A1%E6%81%AF%EF%BC%89)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[测试：](#%E6%B5%8B%E8%AF%95%EF%BC%9A)

[2.2、Amap（服务枚举工具）](#2.2%E3%80%81Amap%EF%BC%88%E6%9C%8D%E5%8A%A1%E6%9E%9A%E4%B8%BE%E5%B7%A5%E5%85%B7%EF%BC%89)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[安装：](#%E5%AE%89%E8%A3%85%EF%BC%9A)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
为了确保有一个成功的渗透测试 ， 必须需要知道目标系统中服务的指纹信息。 服务指 纹信息包括服务端口 、 服务名和版本等


---


---


## 二、工具

> 
<h3>2.1、Nmap（识别服务指纹信息）</h3>
<h4>使用：</h4>
[【端口扫描工具】nmap核心使用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125263917?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125263917-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)[nmap“扫描基础”“端口扫描技术”“服务和版本探测”“操作系统探测”“时间和性能”“防火墙/IDS躲避和哄骗”相关参考指南<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/122759253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165932934416781432923359%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165932934416781432923359&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-122759253-null-null.nonecase&amp;utm_term=nmap&amp;spm=1018.2226.3001.4450)
<hr/>
<h4>测试：</h4>
用Nmap工具查看39.106.226.142服务上正在运行的端口
nmap -sV 39.106.226.142 


可以查看到目标服务器上运行的端口号、各个端口对应的服务及版本信息


#### 测试：

> 
<h3>2.2、Amap（服务枚举工具）</h3>
<h4>简介：</h4>
Amap是一个服务枚举工具。 使用该工具能识别正运行在 一 ·个指定端口或一个范围端<br/> 口上的应用程序
<hr/>
<h4>安装：</h4>
sudo apt install amap 


<hr/>
<h4>命令：</h4>
<pre><code>Syntax: amap [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o &lt;file&gt;] [-D &lt;file&gt;] [-t/-T sec] [-c cons] [-C retries] [-p proto] [-i &lt;file&gt;] [target port [port] ...]
Modes:
  -A         Map applications: send triggers and analyse responses (default)
  -B         Just grab banners, do not send triggers
  -P         No banner or application stuff - be a (full connect) port scanner
Options:
  -1         Only send triggers to a port until 1st identification. Speeeeed!
  -6         Use IPv6 instead of IPv4
  -b         Print ascii banner of responses
  -i FILE    Nmap machine readable outputfile to read ports from
  -u         Ports specified on commandline are UDP (default is TCP)
  -R         Do NOT identify RPC service
  -H         Do NOT send application triggers marked as potentially harmful
  -U         Do NOT dump unrecognised responses (better for scripting)
  -d         Dump all responses
  -v         Verbose mode, use twice (or more!) for debug (not recommended :-)
  -q         Do not report closed ports, and do not print them as unidentified
  -o FILE [-m] Write output to file FILE, -m creates machine readable output
  -c CONS    Amount of parallel connections to make (default 32, max 256)
  -C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)
  -T SEC     Connect timeout on connection attempts in seconds (default 5)
  -t SEC     Response wait timeout in seconds (default 5)
  -p PROTO   Only send triggers for this protocol (e.g. ftp)
  TARGET PORT   The target address and port(s) to scan (additional to -i)
amap is a tool to identify application protocols on target ports.
Note: this version was NOT compiled with SSL support!
Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.
</code></pre>

<hr/>
<h4>使用：</h4>
用Amap 工具在指定的端口（或一段范围）， 测试目标主机39.106.226.142上正在运行的应用程序
amap -bqv 39.106.226.142 80




#### 安装：

---


#### 使用：
