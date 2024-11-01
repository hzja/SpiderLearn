# 原创
：  HDLC协议的配置

# HDLC协议的配置

**1、基本配置**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021012423310371.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

```
&lt;Huawei&gt;system
[Huawei]sysname AR1
[AR1]interface g0/0/1
[AR1-GigabitEthernet0/0/1]ip address 11.1.1.1 24
[AR1-GigabitEthernet0/0/1]quit 
[AR1]interface s0/0/0
[AR1-Serial0/0/0]ip address 12.1.1.1 24
[AR1-Serial0/0/0]quit
[AR1]


```

```
&lt;Huawei&gt;system
[Huawei]sysname AR2
[AR2]interface g0/0/1
[AR2-GigabitEthernet0/0/1]ip address 22.1.1.2 24	
[AR2-GigabitEthernet0/0/1]quit
[AR2]interface s0/0/0
[AR2-Serial0/0/0]ip address 12.1.1.2 24
[AR2-Serial0/0/0]quit 
[AR2]	

```

**2、配置静态路由**<br/> 在AR2上配置默认路由指向出口网关AR1，并在AR1上配置目的网段PC1所在网络的路由器——下一跳路由器AR2。

```
[AR2]ip route-static 0.0.0.0 0.0.0.0 12.1.1.1
[AR1]ip route-static 22.1.1.0 255.255.255.0 12.1.1.2

```

在PC1上测试与PC2的通信。

```
PC&gt;ping 22.1.1.22

Ping 22.1.1.22: 32 data bytes, Press Ctrl_C to break
From 22.1.1.22: bytes=32 seq=1 ttl=126 time=94 ms
From 22.1.1.22: bytes=32 seq=2 ttl=126 time=62 ms
From 22.1.1.22: bytes=32 seq=3 ttl=126 time=47 ms
From 22.1.1.22: bytes=32 seq=4 ttl=126 time=31 ms
From 22.1.1.22: bytes=32 seq=5 ttl=126 time=63 ms

--- 22.1.1.22 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 31/59/94 ms

```

**3、配置HDLC**<br/> 默认情况下，串行接口封装的链路层协议即为PPP，查看。

```
[AR1]display interface s0/0/0
Serial0/0/0 current state : UP
Line protocol current state : UP
Last line protocol up time : 2021-01-24 23:21:05 UTC-08:00
Description:
Route Port,The Maximum Transmit Unit is 1500, Hold timer is 10(sec)
Internet Address is 12.1.1.1/24
Link layer protocol is PPP
LCP opened, IPCP opened
Last physical up time   : 2021-01-24 23:17:12 UTC-08:00
Last physical down time : 2021-01-24 23:17:11 UTC-08:00
Current system time: 2021-01-24 23:25:00-08:00Interface is V35
    Last 300 seconds input rate 2 bytes/sec, 0 packets/sec
    Last 300 seconds output rate 2 bytes/sec, 0 packets/sec
    Input: 1508 bytes, 103 Packets
    Ouput: 1534 bytes, 104 Packets
    Input bandwidth utilization  : 0.02%
    Output bandwidth utilization : 0.02%

```

在AR1和AR2的串口上分别使用LINK-PROTOCOL命令配置链路层协议为HDLC。

```
[AR1-Serial0/0/0]link-protocol hdlc
Warning: The encapsulation protocol of the link will be changed. 
Continue? [Y/N]:y

[AR2-Serial0/0/0]link-protocol hdlc
Warning: The encapsulation protocol of the link will be changed. 
Continue? [Y/N]:y

```

再一次查看。

```
[AR1]display interface s0/0/0
Serial0/0/0 current state : UP
Line protocol current state : UP
Last line protocol up time : 2021-01-24 23:27:17 UTC-08:00
Description:
Route Port,The Maximum Transmit Unit is 1500, Hold timer is 10(sec)
Internet Address is 12.1.1.1/24
Link layer protocol is nonstandard HDLC
Last physical up time   : 2021-01-24 23:27:17 UTC-08:00
Last physical down time : 2021-01-24 23:27:17 UTC-08:00
Current system time: 2021-01-24 23:27:58-08:00Interface is V35
    Last 300 seconds input rate 3 bytes/sec, 0 packets/sec
    Last 300 seconds output rate 3 bytes/sec, 0 packets/sec
    Input: 1910 bytes, 136 Packets
    Ouput: 1958 bytes, 136 Packets
    Input bandwidth utilization  : 0.03%
    Output bandwidth utilization : 0.03%


```

**4、验证配置效果**<br/> 测试PC1和PC2的连通性。

```
PC&gt;ping 22.1.1.22

Ping 22.1.1.22: 32 data bytes, Press Ctrl_C to break
From 22.1.1.22: bytes=32 seq=1 ttl=126 time=47 ms
From 22.1.1.22: bytes=32 seq=2 ttl=126 time=46 ms
From 22.1.1.22: bytes=32 seq=3 ttl=126 time=47 ms
From 22.1.1.22: bytes=32 seq=4 ttl=126 time=47 ms
From 22.1.1.22: bytes=32 seq=5 ttl=126 time=63 ms

--- 22.1.1.22 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 46/50/63 ms

```

可以正常通信。
