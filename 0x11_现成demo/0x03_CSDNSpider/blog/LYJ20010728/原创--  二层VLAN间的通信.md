# 原创
：  二层VLAN间的通信

# 二层VLAN间的通信

### 案例一、基于非对称VLAN模型的端口隔离技术的实现

**1、配置用户设备**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111163341114.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置Switch1**

```
&lt;Huawei&gt;sys
[Huawei]sysname Switch1
[Switch1]vlan batch 10 20 30
[Switch1]interface g0/0/1
[Switch1-GigabitEthernet0/0/1]port link-type hybrid 
[Switch1-GigabitEthernet0/0/1]port hybrid tagged vlan all
[Switch1-GigabitEthernet0/0/1]q
[Huawei]interface g0/0/2
[Huawei-GigabitEthernet0/0/2]port link-type hybrid
[Huawei-GigabitEthernet0/0/2]port hybrid pvid vlan 10
[Huawei-GigabitEthernet0/0/2]port hybrid untagged vlan 10 30
[Huawei-GigabitEthernet0/0/2]q
[Huawei]interface g0/0/3
[Huawei-GigabitEthernet0/0/3]port link-type hybrid
[Huawei-GigabitEthernet0/0/3]port hybrid pvid vlan 20
[Huawei-GigabitEthernet0/0/3]port hybrid untagged vlan 20 30
[Huawei-GigabitEthernet0/0/3]q

```

**3、配置Switch2**

```
&lt;Huawei&gt;sys
[Huawei]sysname Switch2
[Switch2]vlan batch 10 20 30
[Switch2]interface g0/0/1
[Switch2-GigabitEthernet0/0/1]port link-type hybrid
[Switch2-GigabitEthernet0/0/1]port hybrid tagged vlan 10 20 30
[Switch2-GigabitEthernet0/0/1]q
[Switch2]interface g0/0/2
[Switch2-GigabitEthernet0/0/2]port link-type hybrid 
[Switch2-GigabitEthernet0/0/2]port hybrid pvid vlan 30
[Switch2-GigabitEthernet0/0/2]port hybrid untagged vlan 10 20 30
[Switch2-GigabitEthernet0/0/2]q

```

**4、验证**

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fed9:57ff
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.100.10
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-D9-57-FF
DNS server........................:

PC&gt;ping 192.168.100.30

Ping 192.168.100.30: 32 data bytes, Press Ctrl_C to break
From 192.168.100.30: bytes=32 seq=1 ttl=255 time=47 ms
From 192.168.100.30: bytes=32 seq=2 ttl=255 time=62 ms
From 192.168.100.30: bytes=32 seq=3 ttl=255 time=32 ms
From 192.168.100.30: bytes=32 seq=4 ttl=255 time=47 ms
From 192.168.100.30: bytes=32 seq=5 ttl=255 time=46 ms

--- 192.168.100.30 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 32/46/62 ms

PC&gt;ping 192.168.100.20

Ping 192.168.100.20: 32 data bytes, Press Ctrl_C to break
From 192.168.100.10: Destination host unreachable
From 192.168.100.10: Destination host unreachable
From 192.168.100.10: Destination host unreachable
From 192.168.100.10: Destination host unreachable
From 192.168.100.10: Destination host unreachable

--- 192.168.100.20 ping statistics ---
  5 packet(s) transmitted
  0 packet(s) received
  100.00% packet loss

```

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fefa:1a1d
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.100.20
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-FA-1A-1D
DNS server........................:

PC&gt;ping 192.168.100.30

Ping 192.168.100.30: 32 data bytes, Press Ctrl_C to break
From 192.168.100.30: bytes=32 seq=1 ttl=255 time=110 ms
From 192.168.100.30: bytes=32 seq=2 ttl=255 time=47 ms
From 192.168.100.30: bytes=32 seq=3 ttl=255 time=31 ms
From 192.168.100.30: bytes=32 seq=4 ttl=255 time=32 ms
From 192.168.100.30: bytes=32 seq=5 ttl=255 time=31 ms

--- 192.168.100.30 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 31/50/110 ms

PC&gt;ping 192.168.100.10

Ping 192.168.100.10: 32 data bytes, Press Ctrl_C to break
From 192.168.100.20: Destination host unreachable
From 192.168.100.20: Destination host unreachable
From 192.168.100.20: Destination host unreachable
From 192.168.100.20: Destination host unreachable
From 192.168.100.20: Destination host unreachable

--- 192.168.100.10 ping statistics ---
  5 packet(s) transmitted
  0 packet(s) received
  100.00% packet loss

```

### 案例二、基于 MUX VLAN 端口隔离与通信

**1、配置用户设备**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111172810174.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置交换机Ha1**

```
（1）配置 MUX VLAN
&lt;Huawei&gt;system
[Huawei]sysname Ha_1
[Ha_1]vlan batch 10 20 30
[Ha_1]vlan 30
[Ha_1-vlan30]mux-vlan						//配置主VLAN
[Ha_1-vlan30]subordinate group 10			//配置VLAN 10为互通型从VLAN
[Ha_1-vlan30]subordinate separate 20		//配置VLAN 20位隔离型从VLAN

（2）配置交换机的VLAN
[Ha_1]interface g0/0/1
[Ha_1-GigabitEthernet0/0/1]port link-type access
[Ha_1-GigabitEthernet0/0/1]port default vlan 10
[Ha_1-GigabitEthernet0/0/1]port mux-vlan enable 
[Ha_1-GigabitEthernet0/0/1]q
[Ha_1]interface g0/0/2
[Ha_1-GigabitEthernet0/0/2]port link-type access
[Ha_1-GigabitEthernet0/0/2]port default vlan 10
[Ha_1-GigabitEthernet0/0/2]port mux-vlan enable
[Ha_1-GigabitEthernet0/0/2]q
[Ha_1]interface g0/0/3
[Ha_1-GigabitEthernet0/0/3]port link-type access
[Ha_1-GigabitEthernet0/0/3]port default vlan 20
[Ha_1-GigabitEthernet0/0/3]port mux-vlan enable
[Ha_1-GigabitEthernet0/0/3]q
[Ha_1]interface g0/0/4
[Ha_1-GigabitEthernet0/0/4]port link-type access
[Ha_1-GigabitEthernet0/0/4]port default vlan 20
[Ha_1-GigabitEthernet0/0/4]port mux-vlan enable
[Ha_1-GigabitEthernet0/0/4]q
[Ha_1]interface g0/0/11
[Ha_1-GigabitEthernet0/0/11]port link-type access
[Ha_1-GigabitEthernet0/0/11]port default vlan 30
[Ha_1-GigabitEthernet0/0/11]port mux-vlan enable
[Ha_1-GigabitEthernet0/0/11]q

```

**3、验证**<br/> PC1分别验证PC2、PC3、Server的连通性

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fe72:67bd
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.200.10
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-72-67-BD
DNS server........................:

PC&gt;ping 192.168.200.20	//PC3

Ping 192.168.200.20: 32 data bytes, Press Ctrl_C to break
From 192.168.200.10: Destination host unreachable
From 192.168.200.10: Destination host unreachable
From 192.168.200.10: Destination host unreachable
From 192.168.200.10: Destination host unreachable
From 192.168.200.10: Destination host unreachable

--- 192.168.200.20 ping statistics ---
  5 packet(s) transmitted
  0 packet(s) received
  100.00% packet loss

PC&gt;ping 192.168.200.11	//PC2

Ping 192.168.200.11: 32 data bytes, Press Ctrl_C to break
From 192.168.200.11: bytes=32 seq=1 ttl=128 time=47 ms
From 192.168.200.11: bytes=32 seq=2 ttl=128 time=31 ms
From 192.168.200.11: bytes=32 seq=3 ttl=128 time=32 ms
From 192.168.200.11: bytes=32 seq=4 ttl=128 time=31 ms
From 192.168.200.11: bytes=32 seq=5 ttl=128 time=31 ms

--- 192.168.200.11 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 31/34/47 ms

PC&gt;ping 192.168.200.30	//Server

Ping 192.168.200.30: 32 data bytes, Press Ctrl_C to break
From 192.168.200.30: bytes=32 seq=1 ttl=255 time=62 ms
From 192.168.200.30: bytes=32 seq=2 ttl=255 time=16 ms
From 192.168.200.30: bytes=32 seq=3 ttl=255 time=16 ms
From 192.168.200.30: bytes=32 seq=4 ttl=255 time=15 ms
From 192.168.200.30: bytes=32 seq=5 ttl=255 time&lt;1 ms

--- 192.168.200.30 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 0/21/62 ms

```

通过测试操作，网吧一区使用了互通型从VLAN技术，PC1和PC2、Server可以相互通信，PC1和PC3不能通信。

PC3上分别验证PC4和Server的连通性

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:febb:c87
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.200.20
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-BB-0C-87
DNS server........................:

PC&gt;ping 192.168.200.21	//PC4

Ping 192.168.200.21: 32 data bytes, Press Ctrl_C to break
From 192.168.200.20: Destination host unreachable
From 192.168.200.20: Destination host unreachable
From 192.168.200.20: Destination host unreachable
From 192.168.200.20: Destination host unreachable
From 192.168.200.20: Destination host unreachable

--- 192.168.200.21 ping statistics ---
  5 packet(s) transmitted
  0 packet(s) received
  100.00% packet loss

PC&gt;ping 192.168.200.30	//Server

Ping 192.168.200.30: 32 data bytes, Press Ctrl_C to break
From 192.168.200.30: bytes=32 seq=1 ttl=255 time=16 ms
From 192.168.200.30: bytes=32 seq=2 ttl=255 time=15 ms
From 192.168.200.30: bytes=32 seq=3 ttl=255 time=32 ms
From 192.168.200.30: bytes=32 seq=4 ttl=255 time=15 ms
From 192.168.200.30: bytes=32 seq=5 ttl=255 time=16 ms

--- 192.168.200.30 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 15/18/32 ms

```

通过测试操作，由于网吧二区使用了隔离型从VLAN技术，PC3和PC4不能通信，PC3和Server可以相互通信。
