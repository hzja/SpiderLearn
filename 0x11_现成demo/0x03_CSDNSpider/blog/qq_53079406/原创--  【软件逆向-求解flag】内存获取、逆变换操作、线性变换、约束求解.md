# 原创
：  【软件逆向-求解flag】内存获取、逆变换操作、线性变换、约束求解

# 【软件逆向-求解flag】内存获取、逆变换操作、线性变换、约束求解

**目录**

[一、直接内存获取](#%E4%B8%80%E3%80%81%E7%9B%B4%E6%8E%A5%E5%86%85%E5%AD%98%E8%8E%B7%E5%8F%96)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、示例：](#1.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.3、分析：](#1.3%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[二、对算法进行逆变换操作](#%E4%BA%8C%E3%80%81%E5%AF%B9%E7%AE%97%E6%B3%95%E8%BF%9B%E8%A1%8C%E9%80%86%E5%8F%98%E6%8D%A2%E6%93%8D%E4%BD%9C)

[2.1、示例：](#2.1%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[三、线性变换的求解](#%E4%B8%89%E3%80%81%E7%BA%BF%E6%80%A7%E5%8F%98%E6%8D%A2%E7%9A%84%E6%B1%82%E8%A7%A3)

[3.1、简介：](#3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.2、示例：](#3.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[四、约束求解](#%E5%9B%9B%E3%80%81%E7%BA%A6%E6%9D%9F%E6%B1%82%E8%A7%A3)

[4.1、简介：](#4.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[4.2、示例：](#4.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 一、直接内存获取

> 
<h3>1.1、简介：</h3>
简单的情况，直接查看内存的方式获取flag
即只需要在比较的地方下个断点，然后通过查看内存即可得到flag

伪代码：
input = get_input()<br/> if(input == calc_flag())<br/> {<br/>         puts(flag is input)<br/> }


> 
<h3>1.2、示例：</h3>
main函数（反编译代码）：



> 
<h3>1.3、分析：</h3>
循环计算出了一个dest，然后与输入的参数argv[1]比较，如果相等，则argv[1]就是flag
选择在调用memcmp的地方下断点，然后运行程序。在断点断下之后，RDI寄存器指向的内容<br/> 即为flag，在GDB中读取flag


---


---


## 二、对算法进行逆变换操作

> 
<h3>2.1、示例：</h3>
一个判断过程的代码：
要分析convert的算法，然后分析结果编写出对应的逆算法，通过reverse_convert(stardard)方式求得flag
input = get_input()<br/> if(standard == convert(input))<br/> {<br/>         puts(flag is input)<br/> }

<hr/>
定位程序比较的地方：


是base64编码的程序
先分析main函数，其中change函数根据输入input得到一个output字符串，然后将output字符串与“ms4otszPhcr7tMmz GMkHyFn=”进行比较---&gt;需要分析change函数

<hr/>
change函数（反编译代码）：

变种的base64：
建立了一个to_string(i)与v22[i]的map，然后，将input转化为二进制的字符串，每次取6字节，转化为一个整数，接着查询map，得到对应的输出字节
<hr/>

base64逆变换：
import base64<br/> s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'<br/> s2 = 'ELF8n0BKxOCbj/WU9mwle4cG6hytqD+P3kZ7AzYsag2NufopRSIVQHMXJri51Tdv'<br/> dict = {}<br/> for i in range(len(s1)):<br/>         dict[s2[i]] = s1[i]<br/> dict['='] = '='<br/> output = 'ms4otszPhcr7tMmzGMkHyFn='<br/> s3 = ' '<br/> for i in range(len(output)):<br/>         s3 += dict[output[i]]<br/> flag = base64.b64decode(s3)<br/> print flag



---


---


---


## 三、线性变换的求解

> 
<h3>3.1、简介：</h3>
如果convert是一个线性变换，那么在output=convert(input)中，output的第i位只能由input的第i位决定。通过获取input[i]的所有可能输入对应的输出output[i]，即可求出input[i]。
对于这种变换，可以进行单字符爆破


> 
<h3>3.2、示例：</h3>
提供了一个cipher可执行程序和ciphertext密文数据。运行cipher，会要求输入明文，并将加密后的结果保存到out文件中
cipher程序运行结果


<hr/>
尝试发现当输入只有第1字节不同时，输出也只有第1字节不同
多次尝试，可以确定其为线性变换



<hr/>
采用单字节爆破
代码：
from zio import *<br/> with open('./ciphertext') as f:<br/> d = f.read()<br/> flag = ' '<br/> for i in range(len(d)):<br/>         for c in range(0x21, 0x80):<br/>                 try_input = flag + chr(c)<br/>                 io = zio('./cipher')<br/>                 io.writeline(try_input)<br/>                 io.close()<br/>                 f = open('./out', 'rb')<br/>                 d2 = f.read()<br/>                 if d2[i] == d[i]:<br/>                         flag += chr(c)<br/>                         break<br/> print flag



---


---


---


## 四、约束求解

> 
<h3>4.1、简介：</h3>
如果output=convert(input)之后，需要output满足多个约束条件
通常会选择约束求解，通常会用到的约束求解器为z3。


> 
<h3>4.2、示例：</h3>
运行程序，弹出错误对话框
用OD加载，下断点GetWindowsTextA，按下check键，程序成功断下来
调用堆栈，可以知道函数返回地址为0x40bd7b。


在IDA中查看0x40bd7b地址，发现该函数被识别为CWnd::GetWindowTextA，所以还要再回溯一层，最终到达地址0x4017AD。
<hr/>
0x4017AD函数的反编译代码
（除了对长度进行判断，要求小于40字节之外，还调用了3个子函数，对输入进行变换）
定位到程序的主要判断逻辑：


第一个函数sub_401380（反编译代码）
熟悉的base64字符串---&gt;该函数为base64加密


第二个函数sub_401000（反编译代码）
对每个字符做了一个减3的操作


第三个函数sub_401040（反编译代码）

<hr/>
 需要满足条件：
a2[i]+a2[i+1] == v5[i]<br/> a2[9]-a2[20]==22<br/> a2[40]==0

条件较难直接计算，故采用约束求解的方式进行求解
代码：
from z3 import *<br/> import base64<br/> s2 = [151, 130, 175, 190, 163, 189, 149, 132, 192, 188, 159, 162, 131, 99, 168, 197, 151, 151, 164, 164, 152, 166, 205, 188, 1
s1 = [BitVec('s1_%d' % i, 8) for i in range(41)]<br/> s = Solver()<br/> for i in range(39):<br/>         s.add(s1[i]+s1[i+1] == s2[i])<br/> s.add(s1[9] - s1[20] == 22)<br/> s.add(s1[40] == 0)<br/> s3 = ' '<br/> if s.check() == z3.sat:<br/>         m = s.model()<br/>         for i in range(40):<br/>                 s3 += chr(m[s1[i]].as_long())<br/> s4 = ' '.join([chr(ord(s3[i])+3) for i in range(len(s3))])<br/> flag = base64.b64decode(s4)<br/> print flag



---

