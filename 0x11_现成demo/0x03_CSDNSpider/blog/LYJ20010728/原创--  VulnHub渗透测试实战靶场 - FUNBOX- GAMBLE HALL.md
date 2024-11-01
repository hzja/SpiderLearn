# 原创
：  VulnHub渗透测试实战靶场 - FUNBOX: GAMBLE HALL

# VulnHub渗透测试实战靶场 - FUNBOX: GAMBLE HALL

#### VulnHub渗透测试实战靶场 - FUNBOX: GAMBLE HALL

## 题目描述

```
Not a reallife box !

It's a very easy box, that makes you crazy.

HINTS:
Don't forget to add: funbox6.box in your /etc/hosts !

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## FUNBOX: GAMBLE HALL靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.112`，发现开放了 `22、80` 端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.112`


### 漏洞挖掘

> 



> 



> 



### getshell

> 



> 



### 提权

> 


