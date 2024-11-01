# 原创
：  【kali-信息收集】（1.3）探测网络范围：DMitry（域名查询工具）、Scapy（跟踪路由工具）

# 【kali-信息收集】（1.3）探测网络范围：DMitry（域名查询工具）、Scapy（跟踪路由工具）

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、工具](#%E4%BA%8C%E3%80%81%E5%B7%A5%E5%85%B7)

[2.1、域名查询工具DMitry](#2.1%E3%80%81%E5%9F%9F%E5%90%8D%E6%9F%A5%E8%AF%A2%E5%B7%A5%E5%85%B7DMitry)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[2.2、跟踪路由工具Scapy](#%C2%A0%E8%B7%9F%E8%B8%AA%E8%B7%AF%E7%94%B1%E5%B7%A5%E5%85%B7Scapy)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[命令：](#%E5%91%BD%E4%BB%A4%EF%BC%9A)

[基础：](#%E5%9F%BA%E7%A1%80%EF%BC%9A)

[ ARP().display()](#%C2%A0ARP%28%29.display%28%29)

[IP().display()](#IP%28%29.display%28%29)

[ICMP().display()](#ICMP%28%29.display%28%29)

[TCP().display()](#TCP%28%29.display%28%29)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
网络范围内的IP地址或域名也是渗透测试的一个重要部分
<hr/>
通过测试网络范围内的IP地计或域名， 确定是否有人入侵自己的网络中并损害系统。不仅对局部IP基础架构进行渗透割试，从现在的安全形势来看，只有对整个IT基础架构进行测试才有意义。因为黑客只要在一个领域找到漏洞，就可以利用这个漏洞攻击另外一个领域。在Kali中提供了DMitry和Scapy工具。 其中，DMitry工具用来查询目标网络中JP地址或域名信息；Scapy工具用来扫描网络及嗅探数据包


---


---


## 二、工具

> 
<h3>2.1、域名查询工具DMitry</h3>
<h4>简介：</h4>
DMitry工具是用来查询IP或域名WHOIS信息的。 WHOIS是用来查询域名是否已经被注册及已经注册域名的详细信息的数据库（如域名所有人和域名注册商）。 使用该工具 可以查到域名的注册商和过期时间等。
<hr/>
<h4>命令：</h4>
dmitry -h
<pre><code>dmitry: invalid option -- 'h'
Usage: dmitry [-winsepfb] [-t 0-9] [-o %host.txt] host
  -o     Save output to %host.txt or to file specified by -o file
  -i     Perform a whois lookup on the IP address of a host
  -w     Perform a whois lookup on the domain name of a host
  -n     Retrieve Netcraft.com information on a host
  -s     Perform a search for possible subdomains
  -e     Perform a search for possible email addresses
  -p     Perform a TCP port scan on a host
* -f     Perform a TCP port scan on a host showing output reporting filtered ports
* -b     Read in the banner received from the scanned port
* -t 0-9 Set the TTL in seconds when scanning a TCP port ( Default 2 )
*Requires the -p flagged to be passed
</code></pre>
<hr/>
<h4>使用：</h4>
收集百度的域名信息
dmitry -wnpb baidu.com


<hr/>
<h4>分析：</h4>
使用DMitry工具可以查看到IP或域名信息,但还是不能判断出这个网络范围。因为一般的路由器和防火墙等并不支持IP地蚧范围的方式，所以工作中经常要把IP地址转换成子网掩码的格式CIDR格式和思科反向子网掩码格式等。
在Linux中，netmask工具可以在lP范围、 子网掩码、 CIDR和Cisco等格式中互相转换， 并且提供了lP地址的点分十进制、十六进制、八进制和二进制之间的互相转换。使用netmask工具将域名转换成标准的子网掩码格式。
<hr/>
<h4>命令：</h4>
netmask -s baidu.com
输出了域名的IP地址和子网掩码




#### 命令：

---


#### 分析：

---


> 
<h3>2.2、跟踪路由工具Scapy</h3>
<h4>简介：</h4>
Scapy是 款强大的交互式数据包处理工具 、 数据包生成器 、 网络扫描器、 网络发现 工具和包嗅探工具。 它提供多种类别的交互式生成数据包或数据包集合、 对数据包进行操作、 发送数据包、 包嗅探、 应答和反馈匹配等功能
<hr/>
<h4>命令：</h4>
<pre><code>Usage: scapy.py [-s sessionfile] [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]
Args:
        -H: header-less start
        -C: do not read startup file
        -P: do not read pre-startup file
</code></pre>
kali中直接使用scapy就可以进入，exit()退出（py环境自带）
<hr/>
<h4>基础：</h4>
每一个协议就是一个类，只需要实例化一个协议类eg：ip=IP()
IP数据包源地址和目的地址，这两个属性使用src和dst来设置
scapy [-s sessionfile] [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]<br/>  
<hr/>
<h4> ARP().display()</h4>

<pre><code>hwtype= 0x1 硬件类型
ptype= IPv4 协议类型
hwlen= 6 硬件地址长度（MAC）
plen= 4 协议地址长度（IP）
op= who-has who-has查询
hwsrc= 00:0c:29:89:54:97 源MAC地址
psrc= 192.168.190.131 源IP地址
hwdst= 00:00:00:00:00:00 目标硬件地址
pdst= 0.0.0.0 向谁发送查询请求</code></pre>
sr1(ARP(pdst="192.168.1.7"))
<hr/>
<h4>IP().display()</h4>

<pre><code>version= 4 版本：IPV4
ihl= None 首部长度
tos= 0x0 服务
len= None 总长度
id= 1 标识
flags=
frag= 0 标志
ttl= 64 生存时间
proto= hopopt 传输控制协议 IPV6逐跳选项
chksum= None 首部校验和
src= 127.0.0.1 源地址
dst= 127.0.0.1 目的地址</code></pre>
<hr/>
<h4>ICMP().display()</h4>

<pre><code>type= echo-request 类型，标识ICMP报文的类型
code= 0 编码
chksum= None 校验和
id= 0x0 标识
seq= 0x0</code></pre>
<hr/>
<h4>TCP().display()</h4>

<pre><code>sport= ftp_data TCP源端口
dport= http TCP目的端口
seq= 0 32位序号
ack= 0 32位确认序号
dataofs= None 4位首部长度
reserved= 0 保留0位
flags= S URG，ACK，PSH，RST，SYN，FIN
window= 8192 窗口大小
chksum= None 16位校验和
urgptr= 0 优先指针
options= [] 选项</code></pre>
<hr/>
<h4>使用：</h4>
使用Scapy实现多行并行跟踪路由功能
**第一步：启动Scapy工具**
看到》》》提示符 ， 表示scapy命令登录成功



**第二步：使用sr(）函数实现发送和接收数据包**
执行命令后 ， 会自动与xxx.com建立连接
使用Ctrl+C终止接收数据包

**第三步：以表的形式查看数据包发送情况**
**第四步：使用scapy查看TCP路由跟踪信息**




#### 命令：

---


####  ARP().display()

---


#### ICMP().display()

---


#### 使用：
