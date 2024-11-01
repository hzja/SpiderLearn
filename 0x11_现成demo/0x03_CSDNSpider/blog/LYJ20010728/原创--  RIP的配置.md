# 原创
：  RIP的配置

# RIP的配置

**1、设备配置**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210115133403402.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> **2、总公司路由器配置**

```
&lt;Huawei&gt;system.
[Huawei]sysname R1
[R1]interface g0/0/0
[R1-GigabitEthernet0/0/0]ip address 11.1.1.1 24
[R1-GigabitEthernet0/0/0]interface g0/0/1
[R1-GigabitEthernet0/0/1]ip address 12.1.1.1 24
[R1-GigabitEthernet0/0/1]interface g0/0/2
[R1-GigabitEthernet0/0/2]ip address 13.1.1.1 24
[R1-GigabitEthernet0/0/2]quit
[R1]rip
[R1-rip-1]version 2
[R1-rip-1]undo summary 
[R1-rip-1]network 11.0.0.0
[R1-rip-1]network 12.0.0.0
[R1-rip-1]network 13.0.0.0
[R1-rip-1]quit
[R1]


```

**3、成华区分中心路由器配置**

```
&lt;Huawei&gt;system
[Huawei]sysname R2
[R2]interface g0/0/1
[R2-GigabitEthernet0/0/1]ip address 12.1.1.2 24
[R2-GigabitEthernet0/0/1]interface g0/0/0
[R2-GigabitEthernet0/0/0]ip address 22.1.1.1 24
[R2-GigabitEthernet0/0/0]quit
[R2]rip
[R2-rip-1]version 2
[R2-rip-1]undo summary 
[R2-rip-1]network 12.0.0.0
[R2-rip-1]network 22.0.0.0
[R2-rip-1]quit
[R2]


```

**4、金牛区分中心路由器配置**

```
&lt;Huawei&gt;system
[Huawei]sysname R3
[R3]interface g0/0/2
[R3-GigabitEthernet0/0/2]ip address 13.1.1.3 24
[R3-GigabitEthernet0/0/2]interface g0/0/0
[R3-GigabitEthernet0/0/0]ip address 33.1.1.1 24
[R3-GigabitEthernet0/0/0]quit
[R3]rip
[R3-rip-1]version 2
[R3-rip-1]undo summary 
[R3-rip-1]network 13.0.0.0
[R3-rip-1]network 33.0.0.0
[R3-rip-1]quit
[R3]


```

**5、设置主机IP**<br/> **6、查看RIP配置**

```
[R1]display ip routing-table protocol rip
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Public routing table : RIP
         Destinations : 2        Routes : 2        

RIP routing table status : &lt;Active&gt;
         Destinations : 2        Routes : 2

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

       22.1.1.0/24  RIP     100  1           D   12.1.1.2        GigabitEthernet
0/0/1
       33.1.1.0/24  RIP     100  1           D   13.1.1.3        GigabitEthernet
0/0/2

RIP routing table status : &lt;Inactive&gt;
         Destinations : 0        Routes : 0

[R1]display current-configuration configuration rip
[V200R003C00]
#
rip 1
 undo summary
 version 2
 network 11.0.0.0
 network 12.0.0.0
 network 13.0.0.0
#
return

```

```
[R2]display ip routing-table protocol rip
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Public routing table : RIP
         Destinations : 3        Routes : 3        

RIP routing table status : &lt;Active&gt;
         Destinations : 3        Routes : 3

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

       11.1.1.0/24  RIP     100  1           D   12.1.1.1        GigabitEthernet
0/0/1
       13.1.1.0/24  RIP     100  1           D   12.1.1.1        GigabitEthernet
0/0/1
       33.1.1.0/24  RIP     100  2           D   12.1.1.1        GigabitEthernet
0/0/1

RIP routing table status : &lt;Inactive&gt;
         Destinations : 0        Routes : 0

[R2]display current-configuration configuration rip
[V200R003C00]
#
rip 1
 undo summary
 version 2
 network 12.0.0.0
 network 22.0.0.0
#
return

```

```
[R3]display ip routing-table protocol rip
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Public routing table : RIP
         Destinations : 3        Routes : 3        

RIP routing table status : &lt;Active&gt;
         Destinations : 3        Routes : 3

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

       11.1.1.0/24  RIP     100  1           D   13.1.1.1        GigabitEthernet
0/0/2
       12.1.1.0/24  RIP     100  1           D   13.1.1.1        GigabitEthernet
0/0/2
       22.1.1.0/24  RIP     100  2           D   13.1.1.1        GigabitEthernet
0/0/2

RIP routing table status : &lt;Inactive&gt;
         Destinations : 0        Routes : 0
	
[R3]display current-configuration configuration rip
[V200R003C00]
#
rip 1
 undo summary
 version 2
 network 13.0.0.0
 network 33.0.0.0
#
return

```

**7、测试连通性**

```
PC&gt;ping 22.1.1.2

Ping 22.1.1.2: 32 data bytes, Press Ctrl_C to break
From 22.1.1.2: bytes=32 seq=1 ttl=126 time=16 ms
From 22.1.1.2: bytes=32 seq=2 ttl=126 time=31 ms
From 22.1.1.2: bytes=32 seq=3 ttl=126 time=16 ms
From 22.1.1.2: bytes=32 seq=4 ttl=126 time=16 ms
From 22.1.1.2: bytes=32 seq=5 ttl=126 time=15 ms

--- 22.1.1.2 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 15/18/31 ms

PC&gt;ping 33.1.1.2

Ping 33.1.1.2: 32 data bytes, Press Ctrl_C to break
From 33.1.1.2: bytes=32 seq=1 ttl=126 time=31 ms
From 33.1.1.2: bytes=32 seq=2 ttl=126 time=16 ms
From 33.1.1.2: bytes=32 seq=3 ttl=126 time=31 ms
From 33.1.1.2: bytes=32 seq=4 ttl=126 time=15 ms
From 33.1.1.2: bytes=32 seq=5 ttl=126 time=32 ms

--- 33.1.1.2 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 15/25/32 ms

```
