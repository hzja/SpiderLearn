# 原创
：  OSPF配置

# OSPF配置

**1、设备配置**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210115202645303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、总公司路由器配置**

```
&lt;Huawei&gt;system
[Huawei]sysname R1
[R1]interface g0/0/1
[R1-GigabitEthernet0/0/1]ip address 11.1.1.1 24
[R1-GigabitEthernet0/0/1]interface g0/0/0
[R1-GigabitEthernet0/0/0]ip address 12.1.1.1 24
[R1-GigabitEthernet0/0/0]interface g0/0/2
[R1-GigabitEthernet0/0/2]ip address 13.1.1.1 24
[R1-GigabitEthernet0/0/2]quit
[R1]ospf
[R1-ospf-1]area 0
[R1-ospf-1-area-0.0.0.0]network 12.1.1.0 0.0.0.255
[R1-ospf-1-area-0.0.0.0]network 13.1.1.0 0.0.0.255
[R1-ospf-1-area-0.0.0.0]


```

**3、南昌分公司路由配置**

```
&lt;Huawei&gt;system
[Huawei]sysname R2
[R2]interface g0/0/0
[R2-GigabitEthernet0/0/0]ip address 12.1.1.2 24
[R2-GigabitEthernet0/0/0]interface g0/0/1
[R2-GigabitEthernet0/0/1]ip address 22.1.1.1 24
[R2-GigabitEthernet0/0/1]quit
[R2]ospf
[R2-ospf-1]area 0
[R2-ospf-1-area-0.0.0.0]network 22.1.1.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]network 12.1.1.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]

```

**4、拉萨分公司路由配置**

```
&lt;Huawei&gt;system
[Huawei]sysname R3
[R3]interface g0/0/2
[R3-GigabitEthernet0/0/2]ip address 13.1.1.3 24
[R3-GigabitEthernet0/0/2]interface g0/0/1
[R3-GigabitEthernet0/0/1]ip address 33.1.1.1 24
[R3-GigabitEthernet0/0/1]quit
[R3]ospf
[R3-ospf-1]area 0
[R3-ospf-1-area-0.0.0.0]network 13.1.1.0 0.0.0.255
[R3-ospf-1-area-0.0.0.0]network 33.1.1.0 0.0.0.255
[R3-ospf-1-area-0.0.0.0]

```

**5、设置主机IP**<br/> **6、测试连通性**

```
PC&gt;ping 33.1.1.2

Ping 33.1.1.2: 32 data bytes, Press Ctrl_C to break
From 33.1.1.2: bytes=32 seq=1 ttl=125 time=15 ms
From 33.1.1.2: bytes=32 seq=2 ttl=125 time=32 ms
From 33.1.1.2: bytes=32 seq=3 ttl=125 time=31 ms
From 33.1.1.2: bytes=32 seq=4 ttl=125 time=31 ms
From 33.1.1.2: bytes=32 seq=5 ttl=125 time=31 ms

--- 33.1.1.2 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 15/28/32 ms

PC&gt;ping 22.1.1.2

Ping 22.1.1.2: 32 data bytes, Press Ctrl_C to break
From 22.1.1.2: bytes=32 seq=1 ttl=125 time=16 ms
From 22.1.1.2: bytes=32 seq=2 ttl=125 time=31 ms
From 22.1.1.2: bytes=32 seq=3 ttl=125 time=16 ms
From 22.1.1.2: bytes=32 seq=4 ttl=125 time=16 ms
From 22.1.1.2: bytes=32 seq=5 ttl=125 time=31 ms

--- 22.1.1.2 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 16/22/31 ms

```
