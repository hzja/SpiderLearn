# 原创
：  【kali-信息收集】（1.2）SNMP枚举：Snmpwalk、Snmpcheck；SMTP枚举：smtp-user-enum

# 【kali-信息收集】（1.2）SNMP枚举：Snmpwalk、Snmpcheck；SMTP枚举：smtp-user-enum

**目录**

[一、SNMP枚举](#%E4%B8%80%E3%80%81SNMP%E6%9E%9A%E4%B8%BE)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、SNMP枚举工具](#%E4%BA%8C%E3%80%81SNMP%E6%9E%9A%E4%B8%BE%E5%B7%A5%E5%85%B7)

[2.1、Snmpwalk](#2.1%E3%80%81Snmpwalk)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[测试](#%E6%B5%8B%E8%AF%95)

[2.2、Snmpcheck](#2.2%E3%80%81Snmpcheck)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[测试：](#%E6%B5%8B%E8%AF%95%EF%BC%9A)

[三、SMTP枚举工具](#%E4%B8%89%E3%80%81SMTP%E6%9E%9A%E4%B8%BE%E5%B7%A5%E5%85%B7)

[3.1、smtp-user-enum](#3.1%E3%80%81smtp-user-enum)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[测试：](#%E6%B5%8B%E8%AF%95%EF%BC%9A)

---


## 一、SNMP枚举

> 
<h3>1.1、简介：</h3>
简单网络管理协议SNMP用于网络设备的管理。网络设备种类多种多样，不同设备厂商提供的管理接口各不相同，这使得网络管理变得愈发复杂
<hr/>
为解决这一问题，SNMP应运而生。SNMP作为广泛应用于TCP/IP网络的网络管理标准协议，提供了统一的接口，从而实现了不同种类和厂商的网络设备之间的统一管理
SNMP协议：SNMPv1、SNMPv2c、SNMPv3


---


---


## 二、SNMP枚举工具

> 
<h3>2.1、Snmpwalk</h3>
<h4>简介：</h4>
Snmpwalk 是一个 SNMP 应用程序 。 它使用 SNMP 的 GETNEXT 请求， 查询指定的所有 OID (SNMP 协议中的对象标识）树信息， 并显示给用户
<hr/>
<h4>测试</h4>
使用 Snmpwalk 命令测试 Windows 主机
snmpwalk -c public 192.168.190.131 -v 2c
<hr/>
使用 snmpwalk 命令枚举安装的软件
 snmpwalk -c public 192.168.41.138 -v 1 I gr ep ftp 
<hr/>
使用 Snmpwalk 工具也可以枚举目标主机上打开的 TCP 端口
snmpwalk -c public 192.168.41.138 -v 1 I grep tcpConnState I cut -d "." -f6 I sort-nu


#### 测试

---


> 
<h3>2.2、Snmpcheck</h3>
<h4>简介：</h4>
Snmpcheck 工具允许用户枚举 SNMP 设备的同时将结果以可读的方式输出。
<hr/>
<h4>测试：</h4>
snmpcheck -t 192.168.190.131
输出的是枚举运行信息
系统信息， 如主机名、 操作系统类型及架构
设备信息， 如设备 ID 号 、 类型和状态等
存储信息， 如设备 id 、 设备类型和文件系统类型等
用户账户信息
进程信息， 如进程ID、 进程名和进程类型等
网络信息， 如TTL值、 TCP段和数据元
网络接口信息， 如接口状态、 速率 、 IP地址和子网掩码等
路由信息， 如目标地址、 下一跳地址、 子网掩码和路径长度值
网络服务信息，如分布式组件对象模型服务、 DHCP 客户端和 DNS 客户端等
监听的 TCP 端口， 如监听的 TCP 端口号有 135 、139 等
监听 UDP 端口信息， 如监听的 UDP 端口有 123、 161 、 4500、 500 和 5355 等
软件组件信息， 如 Visual C++ 2008
Web 服务信息， 如发送的字节数、 文件数和当前匿名用户等


#### 测试：

---


---


## 三、SMTP枚举工具

> 
<h3>3.1、smtp-user-enum</h3>
<h4>简介：</h4>
smlp-user-enum是针对SMTP服务器的25端口，进行用户名枚举的工具，用以探测服务器已存在的邮箱账户。 在SMTP服务上启动用户的SMTP枚举
<hr/>
<h4>安装：</h4>
sudo apt install smtp-user-enum 

 
<hr/>
<h4>命令：</h4>
<pre><code>Usage: smtp-user-enum [options] ( -u username | -U file-of-usernames ) ( -t host | -T file-of-targets )

options are:
        -m n     Maximum number of processes (default: 5)
        -M mode  Method to use for username guessing EXPN, VRFY or RCPT (default: VRFY)
        -u user  Check if user exists on remote system
        -f addr  MAIL FROM email address.  Used only in "RCPT TO" mode (default: user@example.com)
        -D dom   Domain to append to supplied user list to make email addresses (Default: none)
                 Use this option when you want to guess valid email addresses instead of just usernames
                 e.g. "-D example.com" would guess foo@example.com, bar@example.com, etc.  Instead of 
                      simply the usernames foo and bar.
        -U file  File of usernames to check via smtp service
        -t host  Server host running smtp service
        -T file  File of hostnames running the smtp service
        -p port  TCP port on which smtp service runs (default: 25)
        -d       Debugging output
        -w n     Wait a maximum of n seconds for reply (default: 5)
        -v       Verbose
        -h       This help message

Also see smtp-user-enum-user-docs.pdf from the smtp-user-enum tar ball.

Examples:

$ smtp-user-enum -M VRFY -U users.txt -t 10.0.0.1
$ smtp-user-enum -M EXPN -u admin1 -t 10.0.0.1
$ smtp-user-enum -M RCPT -U users.txt -T mail-server-ips.txt
$ smtp-user-enum -M EXPN -D example.com -U users.txt -t 10.0.0.1
</code></pre>
<hr/>
<h4>测试：</h4>
smtp-user-enum -M VRFY -U /tmp/users.txt -t 192.168.190.131 



#### 安装：

---


#### 测试：
