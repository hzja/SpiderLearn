# 原创
：  VirtualBox(Host only)和VMware共用同一虚拟网卡

# VirtualBox(Host only)和VMware共用同一虚拟网卡

#### VirtualBox和VMware共用同一虚拟网卡

## 背景描述

> 
最近学渗透的时候需要从VulnHub下载靶机到本地玩，而且VulnHub的靶机大多数只能在VirtualBox或者VMware这两种虚拟机软件下的一种运行，有时候需要利用到VirtualBox和VMware共用同一虚拟网卡来搭建渗透环境


## 配置步骤

### 配置VirtualBox上的靶机

> 
VirtualBox设置为`Host-Only`模式


### 配置VMware软件

> 
设置桥接模式的网卡为`VirtualBox Host-Only Ethernet Adapter`，让VirtualBox和VMware共用VirtualBox的`VirtualBox Host-Only Ethernet Adapter`网卡


### 配置VMware上的Kali

> 
配置Kali默认的网络适配器为桥接模式，对应到Kali里面的网口为`eth0`<br/> 给Kali增加一个网络适配器，并设置它的网络为`NAT`模式


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/91d64d2e69db44c29622fa19e9a76280.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/194e923e47714b85abbae2f5d2082ec1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
进入Kali系统，测试一下是否可用，发现靶机和攻击机成功在同一个网段内


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9bb3a462c26846cdad62af452f90beda.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8ed31d56d32c4c998ed5d1c2e2b43e9b.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
