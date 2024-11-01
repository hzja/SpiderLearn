# 原创
：  【端口扫描工具】nmap核心使用方法

# 【端口扫描工具】nmap核心使用方法

**目录**

[nmap的基础使用：](#nmap%E7%9A%84%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%EF%BC%9A)

[1.1、常用命令参数：](#1.1%E3%80%81%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%E5%8F%82%E6%95%B0%EF%BC%9A)

[命令格式：](#%E5%91%BD%E4%BB%A4%E6%A0%BC%E5%BC%8F%EF%BC%9A)

[主机发现：](#%E4%B8%BB%E6%9C%BA%E5%8F%91%E7%8E%B0%EF%BC%9A)

[扫描](#%E6%89%AB%E6%8F%8F)

[ 扫描速度](#%C2%A0%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6)

[扫描端口](#%E6%89%AB%E6%8F%8F%E7%AB%AF%E5%8F%A3)

[1.2、基本扫描](#1.2%E3%80%81%E5%9F%BA%E6%9C%AC%E6%89%AB%E6%8F%8F)

[1.3、自定义端口扫描](#1.3%E3%80%81%E8%87%AA%E5%AE%9A%E4%B9%89%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[1.4、Ping扫描](#1.4%E3%80%81Ping%E6%89%AB%E6%8F%8F)

[1.5、路由追踪](#1.5%E3%80%81%E8%B7%AF%E7%94%B1%E8%BF%BD%E8%B8%AA)

[1.6、扫描网段,C段](#1.6%E3%80%81%E6%89%AB%E6%8F%8F%E7%BD%91%E6%AE%B5%2CC%E6%AE%B5)

[1.7、操作系统类型的探测](#1.7%E3%80%81%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E7%B1%BB%E5%9E%8B%E7%9A%84%E6%8E%A2%E6%B5%8B)

[1.8、nmap万能开关](#1.8%E3%80%81nmap%E4%B8%87%E8%83%BD%E5%BC%80%E5%85%B3)

[1.9、扫描服务与版本](#1.9%E3%80%81%E6%89%AB%E6%8F%8F%E6%9C%8D%E5%8A%A1%E4%B8%8E%E7%89%88%E6%9C%AC)

[1.10、其他命令：](#1.10%E3%80%81%E5%85%B6%E4%BB%96%E5%91%BD%E4%BB%A4%EF%BC%9A)

---


## nmap的基础使用：

> 
<h3>1.1、常用命令参数：</h3>
<h4>命令格式：</h4>
nmap [扫描类型][选项]{目标或目标集合}
<hr/>
<h4>主机发现：</h4>

<hr/>
<h4>扫描</h4>

<hr/>
<h4> 扫描速度</h4>

<hr/>
<h4>扫描端口</h4>




#### 主机发现：

---


####  扫描速度

---


> 
<h3>1.2、基本扫描</h3>
默认先检测目标是否开机，如是则进一步探测目标主机最常用的1000个端口
例  nmap 39.106.226.142




> 
<h3>1.3、自定义端口扫描</h3>
例   nmap -p80  39.106.226.142




> 
<h3>1.4、Ping扫描</h3>
例  nmap -sP 39.106.226.142
 <img alt="" height="112" src="https://img-blog.csdnimg.cn/c9322a4acf7d4f8ba6927cffcc6b493e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_15,color_FFFFFF,t_70,g_se,x_16" width="635"/>



> 
<h3>1.5、路由追踪</h3>
查我们电脑所在地到目的地之间所经过的网络节点
例  sudo nmap --traceroute 39.106.226.142




> 
<h3>1.6、扫描网段,C段</h3>
例  nmap -sP 39.106.226.142/24




> 
<h3>1.7、操作系统类型的探测</h3>
例  nmap -o 39.106.226.142




> 
<h3>1.8、nmap万能开关</h3>
包含了端口ping扫描，操作系统扫描，脚本扫描，路由跟踪，服<br/> 务探测
例  nmap -A 39.106.226.142




> 
<h3>1.9、扫描服务与版本</h3>
例  nmap -sV 204.74.211.183
我扫了几个都没扫出来，尴尬了



### 1.10、其他命令：

```
-sT	         TCP connect()扫描，在目标主机的日志中记录大批连接请求和错误信息。
-sS	         半开扫描，很少有系统能把它记入系统日志。
-sF  -sN	 秘密FIN数据包扫描、Xmas Tree、Null扫描模式
-sP	         ping扫描，Nmap默认都会使用ping扫描，只有主机存活，才会继续扫描。
-sU	         UDP扫描，是不可靠的
-sA	         通常用来穿过防火墙的规则集
-sV	         探测端口服务版本
-Pn	         扫描之前不需要用ping命令，有些防火墙禁止ping命令。可以使用此选项进行扫描
-v	         显示扫描过程，推荐使用
-h	         帮助选项，是最清楚的帮助文档
-p	         指定端口，如“1-65535、1433、135、22、80”等
-O	         启用远程操作系统检测，存在误报
-A	         全面系统检测、启用脚本检测、扫描等
-oN/-oX/-oG	 将报告写入文件，分别是正常、XML、grepable 三种格式
-T4	         针对TCP端口禁止动态扫描延迟超过10ms
-iL	         读取主机列表，例如，“-iL C  \ip.txt”
-iflist      查看本地主机的接口信息和路由信息
-A           选项用于使用进攻性方式扫描
-T4          指定扫描过程使用的时序，总有6个级别（0-5），级别越高，扫描速度越快，但也容易被防火墙或IDS检测并屏蔽掉，推荐使用T4
-oX test.xml 将扫描结果生成 test.xml 文件，如果中断，则结果打不开
-oA test.xml 将扫描结果生成 test.xml 文件，中断后，结果也可保存
-oG test.txt 将扫描结果生成 test.txt 文件
-sn         只进行主机发现，不进行端口扫描
-O          指定Nmap进行系统版本扫描
-sV         指定让Nmap进行服务版本扫描
-p &lt;port ranges&gt;   扫描指定的端口
-sS/sT/sA/sW/sM  指定使用 TCP SYN/Connect()/ACK/Window/Maimon scans的方式来对目标主机进行扫描
-sU         指定使用UDP扫描方式确定目标主机的UDP端口状况
-script &lt;script name&gt;    指定扫描脚本
-Pn         不进行ping扫描
-sP         用ping扫描判断主机是否存活，只有主机存活，nmap才会继续扫描，一般最好不加，因为有的主机会禁止ping
-PI         设置这个选项，让nmap使用真正的ping(ICMP echo请求)来扫描目标主机是否正在运行。
-iL 1.txt    批量扫描1.txt中的目标地址
-sL          List Scan 列表扫描，仅将指定的目标的IP列举出来，不进行主机发现
-sY/sZ       使用SCTP INIT/COOKIE-ECHO来扫描SCTP协议端口的开放的情况
-sO         使用IP protocol 扫描确定目标机支持的协议类型
-PO         使用IP协议包探测对方主机是否开启 
-PE/PP/PM    使用ICMP echo、 ICMP timestamp、ICMP netmask 请求包发现主机
-PS/PA/PU/PY    使用TCP SYN/TCP ACK或SCTP INIT/ECHO方式进行发现
-sN/sF/sX   指定使用TCP Null, FIN, and Xmas scans秘密扫描方式来协助探测对方的TCP端口状态
-e eth0           指定使用eth0网卡进行探测
-f    --mtu &lt;val&gt;   指定使用分片、指定数据包的 MTU.
-b &lt;FTP relay host&gt;   使用FTP bounce scan扫描方式
-g            指定发送的端口号
-r          不进行端口随机打乱的操作（如无该参数，nmap会将要扫描的端口以随机顺序方式扫描，以让nmap的扫描不易被对方防火墙检测到）
-v 表示显示冗余信息，在扫描过程中显示扫描的细节，从而让用户了解当前的扫描状态
-n          表示不进行DNS解析；
-D  &lt;decoy1,decoy2[,ME],...&gt;   用一组 IP 地址掩盖真实地址，其中 ME 填入自己的 IP 地址
-R          表示总是进行DNS解析。 
-F          快速模式，仅扫描TOP 100的端口 
-S &lt;IP_Address&gt;   伪装成其他 IP 地址
--ttl &lt;val&gt;   设置 time-to-live 时间
--badsum   使用错误的 checksum 来发送数据包（正常情况下，该类数据包被抛弃，如果收到回复，说明回复来自防火墙或 IDS/IPS）
--dns-servers     指定DNS服务器
--system-dns    指定使用系统的DNS服务器   
--traceroute    追踪每个路由节点 
--scanflags &lt;flags&gt;   定制TCP包的flags
--top-ports &lt;number&gt;   扫描开放概率最高的number个端口
--port-ratio &lt;ratio&gt;   扫描指定频率以上的端口。与上述--top-ports类似，这里以概率作为参数
--version-trace   显示出详细的版本侦测过程信息
--osscan-limit   限制Nmap只对确定的主机的进行OS探测（至少需确知该主机分别有一个open和closed的端口）
--osscan-guess   大胆猜测对方的主机的系统类型。由此准确性会下降不少，但会尽可能多为用户提供潜在的操作系统
--data-length &lt;num&gt;   填充随机数据让数据包长度达到 Num
--ip-options &lt;options&gt;   使用指定的 IP 选项来发送数据包
--spoof-mac &lt;mac address/prefix/vendor name&gt;    伪装 MAC 地址
--version-intensity &lt;level&gt;   指定版本侦测强度（0-9），默认为7。数值越高，探测出的服务越准确，但是运行时间会比较长。
--version-light   指定使用轻量侦测方式 (intensity 2)
--version-all   尝试使用所有的probes进行侦测 (intensity 9)
--version-trace   显示出详细的版本侦测过程信息
```
