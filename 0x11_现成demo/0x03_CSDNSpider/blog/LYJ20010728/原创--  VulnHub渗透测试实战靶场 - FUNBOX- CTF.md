# 原创
：  VulnHub渗透测试实战靶场 - FUNBOX: CTF

# VulnHub渗透测试实战靶场 - FUNBOX: CTF

#### VulnHub渗透测试实战靶场 - FUNBOX: CTF

## 题目描述

```
Groundhog Day: Boot2Root !

Initial footstep is a bit flowed, but really not difficult.

After getting access to Funbox: CTF, its nessesarry to find, read and understand the (2 and easy to find) hints.

Be smart and combine...

Hints: Nikto scans "case sensitive" and you need a minimum of 15 mins to get user !

If you need hints, call me on twitter: @0815R2d2

Have fun...

This works better with VirtualBox rather than VMware

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## FUNBOX: CTF靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.114`，发现开放了 `22、80、110、143` 四个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.114`


### 漏洞挖掘

> 



```
Disallow: upload/
Disallow: igmseklhgmrjmtherij2145236

```

> 



### getshell

> 



### 提权

> 



> 



> 



> 



> 


