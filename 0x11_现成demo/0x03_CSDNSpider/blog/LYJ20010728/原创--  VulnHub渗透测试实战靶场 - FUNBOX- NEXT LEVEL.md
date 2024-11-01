# 原创
：  VulnHub渗透测试实战靶场 - FUNBOX: NEXT LEVEL

# VulnHub渗透测试实战靶场 - FUNBOX: NEXT LEVEL

#### VulnHub渗透测试实战靶场 - FUNBOX: NEXT LEVEL

## 题目描述

```
Lets separate the script-kids from script-teenies.

Hint: The first impression is not always the right one!

If you need hints, call me on twitter: @0815R2d2 Have fun...

This works better with VirtualBox rather than VMware

This works better with VirtualBox rather than VMware.

```

## 环境下载

> 



## FUNBOX: NEXT LEVEL靶机搭建

> 

- 将下载好的靶机环境，导入 VritualBox，设置为 Host-Only 模式- 将 VMware 中桥接模式网卡设置为 VritualBox 的 Host-only


> 



## 渗透测试

### 信息搜集

> 
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.113`，发现开放了 `22、80` 端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.113`


### 漏洞挖掘

> 



> 



```
wpscan --url http://192.168.56.113/drupal/index.php --wp-content-dir=http://192.168.56.113/drupal/wp-content --enumerate u,p

```

> 



```
hydra -l ben -P rockyou.txt -V 192.168.56.113 ssh

```

### getshell

> 



### 提权

> 



> 



> 



> 

- 先使用 dd 命令将 `/etc/passwd` 复制到当前目录下


> 
- 由于 `adam` 用户没有修改权限，所以将其下载到本地


> 
- 生成一个以 root 为密码的密文，然后使用 root 身份进行修改


> 
- 将修改好的内容上传回去


> 
- 再利用 dd 命令将 `/etc/passwd` 的内容替换成修改过后的内容


> 


