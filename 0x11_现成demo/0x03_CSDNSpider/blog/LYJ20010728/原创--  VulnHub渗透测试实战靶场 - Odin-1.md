# 原创
：  VulnHub渗透测试实战靶场 - Odin：1

# VulnHub渗透测试实战靶场 - Odin：1

#### VulnHub渗透测试实战靶场 - Odin：1

## 题目描述

```
Odin ventured to the Well of Mimir, near Jötunheim, the land of the giants in the guise of a walker named Vegtam. Mímir, who guarded the well, to allow him to drink from it, asked him to sacrifice his left eye, this being a symbol of his will to obtain knowledge

Pls, add /etc/hosts -&gt; ip vm + odin

example: 192.168.1.1 odin

Twitter: @ArmBjorn

Work in Virtualbox.

Get root permissions

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
用 Nmap 扫描一下目标靶机的端口信息：`sudo nmap -sS -A -Pn 192.168.56.110`，发现开放了 `80` 端口


> 
用 dirb 扫描一下 80 端口 web 目录：`dirb http://192.168.56.110`


### 漏洞挖掘

> 



> 



```
++++++++++[&gt;+&gt;+++&gt;+++++++&gt;++++++++++&lt;&lt;&lt;&lt;-]&gt;&gt;&gt;&gt;++++++++++.+.+++++.————.+.+++++.——-.
nottuzy

SWYgeW91IGxvb2sgY2xvc2VseSwgeW91IHdvbid0IG5lZWQgaXQgaGVyZQo=
If you look closely, you won't need it here

```

> 



> 



### getshell

> 



> 



### 提权

> 



> 



> 


