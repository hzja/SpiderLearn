# 原创
：  VLAN的划分及跨交换机VLAN内的通信

# VLAN的划分及跨交换机VLAN内的通信

**1、配置用户设置**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111162009996.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置交换机LSW1**

```
&lt;Huawei&gt;sys
[Huawei]vlan batch 10 20
[Huawei]interface g0/0/1
[Huawei-GigabitEthernet0/0/1]port link-type access
[Huawei-GigabitEthernet0/0/1]port default vlan 10
[Huawei-GigabitEthernet0/0/1]q
[Huawei]interface g0/0/2
[Huawei-GigabitEthernet0/0/2]port link-type access
[Huawei-GigabitEthernet0/0/2]port default vlan 20
[Huawei-GigabitEthernet0/0/2]q
[Huawei]interface g0/0/6
[Huawei-GigabitEthernet0/0/6]port link-type trunk
[Huawei-GigabitEthernet0/0/6]port trunk allow-pass vlan all
[Huawei-GigabitEthernet0/0/6]q
[Huawei]display vlan
The total number of vlans is : 3
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
--------------------------------------------------------------------------------

VID  Type    Ports                                                          
--------------------------------------------------------------------------------
1    common  UT:GE0/0/3(D)      GE0/0/4(D)      GE0/0/5(D)      GE0/0/6(U)      
                GE0/0/7(D)      GE0/0/8(D)      GE0/0/9(D)      GE0/0/10(D)     
                GE0/0/11(D)     GE0/0/12(D)     GE0/0/13(D)     GE0/0/14(D)     
                GE0/0/15(D)     GE0/0/16(D)     GE0/0/17(D)     GE0/0/18(D)     
                GE0/0/19(D)     GE0/0/20(D)     GE0/0/21(D)     GE0/0/22(D)     
                GE0/0/23(D)     GE0/0/24(D)                                     

10   common  UT:GE0/0/1(U)                                                      

             TG:GE0/0/6(U)                                                      

20   common  UT:GE0/0/2(U)                                                      

             TG:GE0/0/6(U)                                                      


VID  Status  Property      MAC-LRN Statistics Description      
--------------------------------------------------------------------------------

1    enable  default       enable  disable    VLAN 0001                         
10   enable  default       enable  disable    VLAN 0010                         
20   enable  default       enable  disable    VLAN 0020  

```

**3、配置交换机LSW2**

```
&lt;Huawei&gt;sys
[Huawei]vlan batch 10 20
[Huawei]interface g0/0/1
[Huawei-GigabitEthernet0/0/1]port link-type access
[Huawei-GigabitEthernet0/0/1]port default vlan 10
[Huawei-GigabitEthernet0/0/1]q
[Huawei]interface g0/0/2
[Huawei-GigabitEthernet0/0/2]port link-type access
[Huawei-GigabitEthernet0/0/2]port default vlan 20
[Huawei-GigabitEthernet0/0/2]q
[Huawei]interface g0/0/6
[Huawei-GigabitEthernet0/0/6]port link-type trunk
[Huawei-GigabitEthernet0/0/6]port trunk allow-pass vlan all
[Huawei-GigabitEthernet0/0/6]q
[Huawei]display vlan
The total number of vlans is : 3
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
--------------------------------------------------------------------------------

VID  Type    Ports                                                          
--------------------------------------------------------------------------------
1    common  UT:GE0/0/3(D)      GE0/0/4(D)      GE0/0/5(D)      GE0/0/6(U)      
                GE0/0/7(D)      GE0/0/8(D)      GE0/0/9(D)      GE0/0/10(D)     
                GE0/0/11(D)     GE0/0/12(D)     GE0/0/13(D)     GE0/0/14(D)     
                GE0/0/15(D)     GE0/0/16(D)     GE0/0/17(D)     GE0/0/18(D)     
                GE0/0/19(D)     GE0/0/20(D)     GE0/0/21(D)     GE0/0/22(D)     
                GE0/0/23(D)     GE0/0/24(D)                                     

10   common  UT:GE0/0/1(U)                                                      

             TG:GE0/0/6(U)                                                      

20   common  UT:GE0/0/2(U)                                                      

             TG:GE0/0/6(U)                                                      


VID  Status  Property      MAC-LRN Statistics Description      
--------------------------------------------------------------------------------

1    enable  default       enable  disable    VLAN 0001                         
10   enable  default       enable  disable    VLAN 0010                         
20   enable  default       enable  disable    VLAN 0020     

```

**4、验证**

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fe99:6c95
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.100.1
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-99-6C-95
DNS server........................:

PC&gt;ping 192.168.100.10

Ping 192.168.100.10: 32 data bytes, Press Ctrl_C to break
From 192.168.100.10: bytes=32 seq=1 ttl=128 time=63 ms
From 192.168.100.10: bytes=32 seq=2 ttl=128 time=62 ms
From 192.168.100.10: bytes=32 seq=3 ttl=128 time=47 ms
From 192.168.100.10: bytes=32 seq=4 ttl=128 time=62 ms
From 192.168.100.10: bytes=32 seq=5 ttl=128 time=63 ms

--- 192.168.100.10 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 47/59/63 ms

```

```
PC&gt;ipconfig

Link local IPv6 address...........: fe80::5689:98ff:fe51:7b6e
IPv6 address......................: :: / 128
IPv6 gateway......................: ::
IPv4 address......................: 192.168.200.1
Subnet mask.......................: 255.255.255.0
Gateway...........................: 0.0.0.0
Physical address..................: 54-89-98-51-7B-6E
DNS server........................:

PC&gt;ping 192.168.200.10

Ping 192.168.200.10: 32 data bytes, Press Ctrl_C to break
From 192.168.200.10: bytes=32 seq=1 ttl=128 time=62 ms
From 192.168.200.10: bytes=32 seq=2 ttl=128 time=63 ms
From 192.168.200.10: bytes=32 seq=3 ttl=128 time=62 ms
From 192.168.200.10: bytes=32 seq=4 ttl=128 time=47 ms
From 192.168.200.10: bytes=32 seq=5 ttl=128 time=46 ms

--- 192.168.200.10 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 46/56/63 ms

```
