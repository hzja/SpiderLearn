# 原创
：  VulnHub渗透测试实战靶场 - Funbox: Lunchbreaker

# VulnHub渗透测试实战靶场 - Funbox: Lunchbreaker

#### VulnHub渗透测试实战靶场 - Funbox: Lunchbreaker

## 题目描述

```
It's a box for beginners and can be pwned in the lunch break.

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
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.116`，发现开放了 `22、80、110、143` 四个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.116`


### 漏洞挖掘

> 



```
DISALLOW: dirb, gobuster, etc.
ALLOW: WYSIWYG

```

> 



> 



> 



```
If the radiance of a thousand suns / were to burst at once into the sky / that would be like / the splendor of the Mighty One and I am become Death, the shatterer of worlds

Look deep into nature and then you will understand everything better."

```

> 



### getshell

> 



```
hydra -l jane -P rockyou.txt -V funbox8.ctf ftp

```

> 



```
kJGgh-kiu65-zghku-76zzt-hgf56
llij8-fgzZ-rTzU1-ddfgz-i876S

```

> 



> 



### 提权

> 



> 



> 


