# 原创
：  三层VLAN间的通信

# 三层VLAN间的通信

### VLAN间通信实现方案一

**1、配置用户设备**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111222843460.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置二层交换机**

```
创建VLAN 10 端口划分
&lt;Huawei&gt;sys
[Huawei]sysname SW2
[SW2]vlan 10
[SW2-vlan10]q
[SW2]interface g0/0/1
[SW2-GigabitEthernet0/0/1]port link-type access
[SW2-GigabitEthernet0/0/1]port default vlan 10
[SW2-GigabitEthernet0/0/1]q

创建VLAN 20 端口划分
[SW2]vlan 20
[SW2-vlan20]q
[SW2]interface g0/0/2
[SW2-GigabitEthernet0/0/2]port link-type access
[SW2-GigabitEthernet0/0/2]port default vlan 20
[SW2-GigabitEthernet0/0/2]q

配置验证
[SW2]display vlan
The total number of vlans is : 3
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
--------------------------------------------------------------------------------

VID  Type    Ports                                                          
--------------------------------------------------------------------------------
1    common  UT:GE0/0/3(U)      GE0/0/4(D)      GE0/0/5(D)      GE0/0/6(D)      
                GE0/0/7(D)      GE0/0/8(D)      GE0/0/9(D)      GE0/0/10(D)     
                GE0/0/11(D)     GE0/0/12(D)     GE0/0/13(D)     GE0/0/14(D)     
                GE0/0/15(D)     GE0/0/16(D)     GE0/0/17(D)     GE0/0/18(D)     
                GE0/0/19(D)     GE0/0/20(D)     GE0/0/21(D)     GE0/0/22(D)     
                GE0/0/23(D)     GE0/0/24(D)                                     

10   common  UT:GE0/0/1(U)                                                      

20   common  UT:GE0/0/2(U)                                                      


VID  Status  Property      MAC-LRN Statistics Description      
--------------------------------------------------------------------------------

1    enable  default       enable  disable    VLAN 0001                         
10   enable  default       enable  disable    VLAN 0010                         
20   enable  default       enable  disable    VLAN 0020         

配置二层交换机的VLAN的汇聚链接                
[SW2]interface g0/0/3
[SW2-GigabitEthernet0/0/3]port link-type trunk
[SW2-GigabitEthernet0/0/3]port trunk allow-pass vlan 10 20
[SW2-GigabitEthernet0/0/3]q


```

**3、配置三层交换机**

```
&lt;Huawei&gt;sys
[Huawei]sysname SW3
[SW3]vlan batch 10 20
[SW3]interface g0/0/3
[SW3-GigabitEthernet0/0/3]port link-type trunk
[SW3-GigabitEthernet0/0/3]port trunk allow-pass vlan 10 20
[SW3-GigabitEthernet0/0/3]q
[SW3]interface Vlanif 10
[SW3-Vlanif10]
Jan 11 2021 22:20:40-08:00 SW3 %%01IFNET/4/IF_STATE(l)[0]:Interface Vlanif10 has
 turned into UP state.	
[SW3-Vlanif10]ip address 192.168.10.254 24
[SW3]interface Vlanif 20
[SW3-Vlanif20]
Jan 11 2021 22:21:11-08:00 SW3 %%01IFNET/4/IF_STATE(l)[2]:Interface Vlanif20 has
 turned into UP state.	
[SW3-Vlanif20]ip address 192.168.20.254 24


```

**4、验证**

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fe5f:3184
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.10.1
Subnet mask.......................: 255.255.255.0
Gateway...........................: 192.168.10.254
Physical address..................: 54-89-98-5F-31-84
DNS server........................:

PC&gt;ping 192.168.20.1

Ping 192.168.20.1: 32 data bytes, Press Ctrl_C to break
From 192.168.20.1: bytes=32 seq=1 ttl=127 time=78 ms
From 192.168.20.1: bytes=32 seq=2 ttl=127 time=78 ms
From 192.168.20.1: bytes=32 seq=3 ttl=127 time=78 ms
From 192.168.20.1: bytes=32 seq=4 ttl=127 time=78 ms
From 192.168.20.1: bytes=32 seq=5 ttl=127 time=78 ms

--- 192.168.20.1 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 78/78/78 ms

```

### VLAN间通信实现方案二

**1、配置用户设备**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111224233444.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置交换机SA的VLAN**

```
&lt;Huawei&gt;sys
[Huawei]sysname SA
[SA]vlan batch 10 20
[SA]interface g0/0/1
[SA-GigabitEthernet0/0/1]port link-type access
[SA-GigabitEthernet0/0/1]port default vlan 10
[SA-GigabitEthernet0/0/1]q
[SA]interface g0/0/2
[SA-GigabitEthernet0/0/2]port link-type access
[SA-GigabitEthernet0/0/2]port default vlan 20
[SA-GigabitEthernet0/0/2]q
[SA]interface g0/0/3
[SA-GigabitEthernet0/0/3]port link-type trunk 
[SA-GigabitEthernet0/0/3]port trunk allow-pass vlan 10 20
[SA-GigabitEthernet0/0/3]q

```

**3、配置交换机SB的VLAN**

```
&lt;Huawei&gt;sys
[Huawei]sysname SB
[SB]vlan batch 10 20
[SB]interface g0/0/1
[SB-GigabitEthernet0/0/1]port link-type access
[SB-GigabitEthernet0/0/1]port default vlan 20
[SB-GigabitEthernet0/0/1]q
[SB]interface g0/0/2
[SB-GigabitEthernet0/0/2]port link-type access
[SB-GigabitEthernet0/0/2]port default vlan 10
[SB-GigabitEthernet0/0/2]q
[SB]interface g0/0/3
[SB-GigabitEthernet0/0/3]port link-type trunk
[SB-GigabitEthernet0/0/3]port trunk allow-pass vlan 10 20
[SB-GigabitEthernet0/0/3]q

```

**4、验证**

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fea2:5ccc
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.10.1
Subnet mask.......................: 255.255.255.0
Gateway...........................: 192.168.10.254
Physical address..................: 54-89-98-A2-5C-CC
DNS server........................:

PC&gt;ping 192.168.20.1

Ping 192.168.20.1: 32 data bytes, Press Ctrl_C to break
From 192.168.10.1: Destination host unreachable
From 192.168.10.1: Destination host unreachable
From 192.168.10.1: Destination host unreachable
From 192.168.10.1: Destination host unreachable
From 192.168.10.1: Destination host unreachable

--- 192.168.10.254 ping statistics ---
  5 packet(s) transmitted
  0 packet(s) received
  100.00% packet loss

PC&gt;ping 192.168.10.10

Ping 192.168.10.10: 32 data bytes, Press Ctrl_C to break
From 192.168.10.10: bytes=32 seq=1 ttl=128 time=62 ms
From 192.168.10.10: bytes=32 seq=2 ttl=128 time=63 ms
From 192.168.10.10: bytes=32 seq=3 ttl=128 time=62 ms
From 192.168.10.10: bytes=32 seq=4 ttl=128 time=63 ms
From 192.168.10.10: bytes=32 seq=5 ttl=128 time=78 ms

--- 192.168.10.10 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 62/65/78 ms

```

由上面的操作我们可以知道，相同的VLAN之间可以通信，不同的VLAN之间无法通信。<br/> **5、创建VLANIF接口**

```
[SA]interface vlanif 10
[SA-Vlanif10]ip address 192.168.10.254 24
[SA]interface vlanif 20
[SA-Vlanif20]ip address 192.168.20.254 24

```

**6、设置网关地址**<br/> 根据创建的VLANIF接口分别给PC1、PC2、PC3、PC4配置网关。<br/> **7、验证**

```
PC&gt;ping 192.168.20.10

Ping 192.168.20.10: 32 data bytes, Press Ctrl_C to break
From 192.168.20.10: bytes=32 seq=1 ttl=127 time=109 ms
From 192.168.20.10: bytes=32 seq=2 ttl=127 time=63 ms
From 192.168.20.10: bytes=32 seq=3 ttl=127 time=47 ms
From 192.168.20.10: bytes=32 seq=4 ttl=127 time=62 ms
From 192.168.20.10: bytes=32 seq=5 ttl=127 time=63 ms

--- 192.168.20.10 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 47/68/109 ms

PC&gt;ping 192.168.20.1

Ping 192.168.20.1: 32 data bytes, Press Ctrl_C to break
From 192.168.20.1: bytes=32 seq=1 ttl=127 time=47 ms
From 192.168.20.1: bytes=32 seq=2 ttl=127 time=31 ms
From 192.168.20.1: bytes=32 seq=3 ttl=127 time=31 ms
From 192.168.20.1: bytes=32 seq=4 ttl=127 time=47 ms
From 192.168.20.1: bytes=32 seq=5 ttl=127 time=31 ms

--- 192.168.20.1 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 31/37/47 ms

```

再次测试发现两端均能ping通了，结果表明不同的VLAN之间可以相互通信。
