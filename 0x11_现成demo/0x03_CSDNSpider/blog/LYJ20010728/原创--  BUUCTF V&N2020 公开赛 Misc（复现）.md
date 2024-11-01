# 原创
：  BUUCTF V&N2020 公开赛 Misc（复现）

# BUUCTF V&amp;N2020 公开赛 Misc（复现）

#### BUUCTF V&amp;N2020 公开赛 Misc（复现）

## 真·签到

> 
CV大法题


> 
Flag：flag{welcome_to_vn}


## 拉胯的三条命令

> 
根据说明文档中的内容，可以发现流量包应该是和Nmap扫描有关


> 
参考文章：[https://www.hackingarticles.in/understanding-nmap-scan-wireshark/](https://www.hackingarticles.in/understanding-nmap-scan-wireshark/)<br/> 找到相关端口号：`3306、22、21、801、631`


> 
Flag：flag{21226318013306}


## ML 第一步

> 
nc连上后给70组数据，需要拟合成一个函数，然后解答给出的十组数据


> 
Payload


```
import re
import numpy as np 
from pwn import *

def process(data):
    x_data = []
    y_data = []
    for i in data:
        z = i.split(',')
        x = float(z[0][2:])
        x_data.append(x)
        y = float(z[1][2:-2])
        y_data.append(y)
    return (np.array(x_data),np.array(y_data))

if __name__ == '__main__':
    p = remote('node4.buuoj.cn',29773)

    print(p.recvline())
    p.sendline('H3rmesk1t')

    for i in range(4):
        print(p.recvline())
    p.sendline()

    data = []
    for i in range(70):
        data.append(p.recvline())

    (x,y) = process(data)
    W = np.poly1d(np.polyfit(x,y,10))
    print(W)

    p.recvline()
    p.sendline()

    for i in range(10):
        information = p.recvline()
        xi = float(re.compile(b'When x=([0-9\.]+),y=?').findall(information)[0])
        p.sendline(str(W(xi)))
        print(xi,W(xi))

    p.interactive()

```

## 内存取证

> 
使用`volatility`，进行镜像分析


```
./volatility_2.6_lin64_standalone -f ~/Desktop/mem.raw imageinfo

```

> 
发现了这个的系统是`Win7SP1x86_23418`，查看进程


```
./volatility_2.6_lin64_standalone -f ~/Desktop/mem.raw --profile=Win7SP1x86_23418 pslist

```

> 
发现可疑进程


```
TrueCrypt.exe  一个磁盘软件
notepad.exe    万能的记事本
iexplore.exe   浏览器
mspaint.exe    画图
DumpIt.exe     内存读取工具

```

> 
查看一下notepad.exe，HxD分析找到可疑链接（VOL文件下载，下载密码可以在iexplore历史记录中找到）


```
./volatility_2.6_lin64_standalone -f ~/Desktop/mem.raw --profile=Win7SP1x86_23418 memdump -p 3552 -D ./

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9e1eaf1811474e44af706718fb4f329a.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7056c9bcadbe4feca06f35289723059f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
查看一下mspaint.exe，将其dump下来，用位移软件GIMP进行分析，得到一个密码：`1YxfCQ6goYBD6Q`


```
./volatility_2.6_lin64_standalone -f ~/Desktop/mem.raw --profile=Win7SP1x86_23418 memdump -p 2648 -D ./

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e101a8805d67409c8da3d9c539b20481.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a6ad7004fcdb4aa9a33ee05276d9fcc0.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
查看TrueCrypt.exe


```
./volatility_2.6_lin64_standalone -f ~/Desktop/mem.raw --profile=Win7SP1x86_23418 memdump -p 3364 -D ./

```

> 
使用Elcomsoft Forensic Disk Decryptor，得到`uOjFdKu1jsbWI8N51jsbWI8N5`


> 
使用[VeraCrypt](https://www.veracrypt.fr/en/Downloads.html)对VOL进行挂载


> 
用前面得到的密码`1YxfCQ6goYBD6Q`解压压缩包


> 
Flag：RoarCTF{wm_D0uB1e_TC-cRypt}


## Final Game

> 
打开压缩包可以看到备注


```
Stupid mortal, you must enter the eighth circle of Hell to get the Tip of god。'=B;:?8\&lt;;:921Uv.3,1*No'&amp;J*)iF~%$#zy?w|{zsr8pun4rTji/PONMLKJIHGFEDCBA@?&gt;=&lt;;:987SRQ3IHMFKDCBf)('&amp;%$#"!~}|{zyxwvutsrqpon,+*)i'&amp;%${zy?}|{t:xwp6Wsrkj0QPONMLKJIHGFEDCBA@VUTYXWVUTSRKoON0LKDCgfS

```

> 
发现关键字`the eighth circle of Hell`，Google这个可以发现是和《神曲》有关，而且这个Malebolge和压缩包中的txt文件名也相同，同时Malebolge也是一种编程语言，[在线编译网站](http://malbolge.doleczek.pl/)


> 
将压缩包备注中的看似乱码的字符串复制进去，而且要删去每行最后的换行，将其变为一行后再Run program，即可得到压缩包密码：`%&amp;^&amp;#@()(*:";'/,,`


> 
解开压缩包得到hint


```
神说：要有ELF！！！
神说：要有WORD！！！
神说：要有NTFS！！！
神说：要有PDF！！！
神说：要有OSZ！！！

地狱 -- 炼狱 -- 天堂

```

> 
用7z打开vmdk文件，寻找后发现一些可疑文件


```
Windows7_by_Lamber.vmdk\Users\lenovo\Documents\Purgatory.zip
Windows7_by_Lamber.vmdk\Users\lenovo\Desktop\Door.png
Windows7_by_Lamber.vmdk\Users\lenovo\Music\paradise.zip
Windows7_by_Lamber.vmdk\Users\lenovo\Downloads\proverbs.pdf

```

> 
结合txt中hint的NTFS，执行`dir /r`，可以看到在Door.png这个文件后隐藏有exe文件


> 
用工具NtfsStreamsEditor将其提取出来，得到Purgatory.exe


> 
后续参考：[http://www.ga1axy.top/index.php/archives/33/](http://www.ga1axy.top/index.php/archives/33/)

