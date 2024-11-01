# 原创
：  【MSFconsole进阶】Nops（空指令模块）：作用、使用方法

# 【MSFconsole进阶】Nops（空指令模块）：作用、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、作用：](#%E4%BA%8C%E3%80%81%E4%BD%9C%E7%94%A8%EF%BC%9A)

[三、使用方法：](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[ 3.1、第一步：查看可用的模块](#%C2%A03.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E5%8F%AF%E7%94%A8%E7%9A%84%E6%A8%A1%E5%9D%97)

[ 3.2、第二步：直接使用](#%C2%A03.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%9B%B4%E6%8E%A5%E4%BD%BF%E7%94%A8)

---


## 一、简介：

> 
空指令不会对程序运行状态造成任何实质影响的空操作或者无关操作指令
eg：x86 CPU----&gt;0x90


---


---


## 二、作用：

> 
（1）填充：（nop指令一个字节），使指令按字对齐，减少取指令时的内存访问次数
eg：偶数对齐，若一条指令占3字节，使用nop指令，cpu 就可从第四个字节处读取指令了
（2）延迟：nop指令会产生一定的延迟（效果取决于CPU性能），使用rep前缀，多占用几个时钟脉冲
（3）等待：使用 nop，等待缓冲区清空，总线恢复（i/o传输）
（4）清除：清除上一个算术逻辑指令设置的flag位
（5）破解：将程序验证部分用nop填充，致使验证失效


---


---


## 三、使用方法：

> 
<h3> 3.1、第一步：查看可用的模块</h3>
#查看支持的空指令
show nops

NOP Generators<br/> ==============
   #  Name                 Disclosure Date  Rank    Check  Description<br/>    -  ----                 ---------------  ----    -----  -----------<br/>    0  nop/aarch64/simple                    normal  No     Simple<br/>    1  nop/armle/simple                      normal  No     Simple<br/>    2  nop/mipsbe/better                     normal  No     Better<br/>    3  nop/php/generic                       normal  No     PHP Nop Generator<br/>    4  nop/ppc/simple                        normal  No     Simple<br/>    5  nop/sparc/random                      normal  No     SPARC NOP Generator<br/>    6  nop/tty/generic                       normal  No     TTY Nop Generator<br/>    7  nop/x64/simple                        normal  No     Simple<br/>    8  nop/x86/opty2                         normal  No     Opty2<br/>    9  nop/x86/single_byte                   normal  No     Single Byte


> 
<h3> 3.2、第二步：直接使用</h3>
use nop/aarch64/simple 



