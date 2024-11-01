# 原创
：  VulnHub渗透测试实战靶场 - POTATO (SUNCSR): 1

# VulnHub渗透测试实战靶场 - POTATO (SUNCSR): 1

#### VulnHub渗透测试实战靶场 - POTATO（SUNCSR）: 1

## 环境下载

> 



## POTATO (SUNCSR): 1靶机搭建

> 



## 渗透测试

### 信息搜集

> 



> 



> 



### 漏洞挖掘

> 



```
hydra -l potato -P top500.txt -V ssh://192.168.246.139:7120 

```

### getshell

> 



### 提权

> 



> 



```
gcc 37292.c -o CVE-2015-1328

```

> 


