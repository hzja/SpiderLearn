# 原创
：  VulnHub渗透测试实战靶场 - FRISTILEAKS: 1.3

# VulnHub渗透测试实战靶场 - FRISTILEAKS: 1.3

#### VulnHub渗透测试实战靶场 - FRISTILEAKS: 1.3

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/fristileaks/FristiLeaks_1.3.ova)


## TOPHATSEC: FRESHLY靶机搭建

> 
将下载好的靶机导入Vmware，网络连接设置为`NAT`模式，虚拟机的MAC地址为：`08:00:27:A5:A6:76`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6b407d583b2d476ba9bf2210af06df44.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> 获取到目标靶机的IP为：`192.168.246.132`

## 渗透测试

### 信息搜集

> 
用`Nmap`扫描一下目标靶机：`sudo nmap -sS -A 192.168.246.132`，发现仅开放了80端口


### 漏洞挖掘

> 
用`dirsearch`探测一下80端口web的目录：`python3 dirsearch.py -u 192.168.246.132 -e *.php`


> 
查看一下扫描到的信息：


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1264fbbc1f6b4ca9988c4b621965b85f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/19f97117734e44d5b16865e663bff03b.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/92b53a1a676844daa5a76cda62221e55.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
访问`http://192.168.246.132/robots.txt`中的路径，发现都是同一张图片`"THIS IS NOT THE RUL"`


> 
分析发现`http://192.168.246.132/images/keep-calm.png`中的图片提示了一个目录`fristi`，尝试访问一下


> 
再次用dirsearch扫描一下`http://192.168.246.132/fristi/`的目录


> 
进一步分析扫描得到的信息，发现在`http://192.168.246.132/fristi/main_login.php`的源码中存在一串base64字符串


> 
将内容复制出来写入文本，用base64解密发现是一张png格式的图片


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/95de79f07be14306addfa885ad08fd17.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5e44407569fd4636a40593cb82dab4b4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
在head部分同样发现可以字样


> 
尝试用`eezeepz:keKkeKKeKKeKkEkkEk`登录，成功进入，发现文件上传点


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b48fc3e33c2a41edbb2dc202c8d6d4c1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0f0c80c2e1f240db9eaee77db7e39dae.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
测试后发现此上传点未做任何过滤，可以直接上传shell文件


### getshell

> 
在shell文件的后缀名上加上`.png`或者`.jpg`或者`.gif`，上传上去<br/> 起一个监听，访问上传的图片，成功反弹shell


### 提权

#### 方法一

> 
查看`/etc/passwd`，发现有三个用户可以调用`/bin/bash`


> 
查看home目录中的eezeepz目录，发现一个值得注意的文件`notes.txt`


> 
根据notes.txt中的内容描述，在`/tmp/`目录下创建`runthis`的文件，过了一段时间后发现计划任务就执行成功了


```
echo "/usr/bin/../../bin/chmod -R 777 /home/admin" &gt;/tmp/runthis

```

> 
查看文件



```
#Enhanced with thanks to Dinesh Singh Sikawar @LinkedIn
import base64,codecs,sys

def encodeString(str):
    base64string= base64.b64encode(str)
    return codecs.encode(base64string[::-1], 'rot13')

cryptoResult=encodeString(sys.argv[1])
print cryptoResult

```

> 



```
=RFn0AKnlMHMPIzpyuTI0ITG

```

> 



```
mVGZ3O3omkJLmy2pcuTq

```

> 
对应写出解密脚本，并对两个txt文本文档进行解密<br/> 得到：`LetThereBeFristi!`和`thisisalsopw123`


```
import sys
import codecs
import base64
def decodeString(str):
    strs = codecs.decode(str[::-1],'rot13')
    return base64.b64decode(strs)

cryptoResult = decodeString(sys.argv[1])
print(cryptoResult)

```

> 
用得到的密码尝试登录另外两个账户，发现admin的密码是`thisisalsopw123`，fristigod的密码是`LetThereBeFristi!`<br/> 测试后发现admin用户无法直接提权至root，也无法访问fristigod用户的家目录


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/10be4e9dec6249799e7d7ac3d5cacb67.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/80868da94e15496288489ba632059934.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
在之前查看`/etc/passwd`时发现`fristigod`用户目录是位于`/var/fristigod`，发现文件`.bash_history`和目录`.secret_admin_stuff`，分别查看一下


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/38cfb08be1804140b6d64c86fcf94bb6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/529c012b5ca94d239eda3e1a83387ffe.png#pic_center"/>

> 
在`.bash_history`中，可以看到通过`sudo -u`来执行一些操作，在`.secret_admin_stuff`目录下存在doCom文件


> 
这里采用 `sudo` 提升权限，并创建一个shell



```
sudo -u fristi /var/fristigod/.secret_admin_stuff/doCom /bin/bash

```

#### 方法二

> 
使用命令`uname -a`查看linux内核信息，发现在脏牛漏洞范围内（Linux kernel &gt;= 2.6.22），可以进行测试


> 
在GitHub上下载exp：[exp链接](https://github.com/FireFart/dirtycow)，用前面已知的文件上传漏洞，结合蚁剑将exp上传上去


> 
利用命令 `gcc -pthread dirty.c -o dirty -lcrypt` 进行编译，生成dirty文件

