# 原创
：  【MSFconsole进阶】Encoders（编码器模块）：编码器、使用方法

# 【MSFconsole进阶】Encoders（编码器模块）：编码器、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、使用方法：](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[2.1、查看编码器](#2.1%E3%80%81%E6%9F%A5%E7%9C%8B%E7%BC%96%E7%A0%81%E5%99%A8)

[2.2、编码器：](#2.2%E3%80%81%E7%BC%96%E7%A0%81%E5%99%A8%EF%BC%9A)

[2.3、格式：](#2.3%E3%80%81%E6%A0%BC%E5%BC%8F%EF%BC%9A)

[2.4、示例：](#2.4%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 一、简介：

> 
作用一：避免出现的“坏字符”
作用二：对攻击载荷进行“免杀”处理


---


---


## 二、使用方法：

> 
<h3>2.1、查看编码器</h3>
#查看当前系统支持的编码器
show encoders



> 
<h3>2.2、编码器：</h3>
0   encoder/cmd/brace
Bash Brace扩展命令编码器
<hr/>
1   encoder/cmd/echo
回声命令编码器
<hr/>
2   encoder/cmd/generic_sh
通用外壳可变替换命令编码器
<hr/>
3   encoder/cmd/ifs
bourne $ {ifs}替换命令编码器
<hr/>
4   encoder/cmd/perl
perl命令编码器
<hr/>
5   encoder/cmd/powershell_base64
powershell base64命令编码器
<hr/>
6   encoder/cmd/printf_php_mq
printf（1）通过php magic_quotes实用命令编码器
<hr/>
 7   encoder/generic/eicar
EICAR 编码器
<hr/>
8   encoder/generic/none
"none" 编码器
<hr/>
9   encoder/mipsbe/byte_xori
Byte XORi 编码器
<hr/>
10  encoder/mipsbe/longxor
XOR 编码器
<hr/>
11  encoder/mipsle/byte_xori
Byte XORi 编码器
<hr/>
12  encoder/mipsle/longxor
XOR 编码器
<hr/>
13  encoder/php/base64
PHP Base64 编码器
<hr/>
14  encoder/ppc/longxor
PPC LongXOR编码器
<hr/>
15  encoder/ppc/longxor_tag
PPC LongXOR 编码器
<hr/>
16  encoder/ruby/base64
Ruby Base64编码器
<hr/>
17  encoder/sparc/longxor_tag
sparc dword xor编码器
<hr/>
18  encoder/x64/xor
XOR 编码器
<hr/>
19  encoder/x64/xor_context
基于主机名的上下文钥匙有效载荷编码器
<hr/>
20  encoder/x64/xor_dynamic
动态密钥XOR编码器
<hr/>
 21  encoder/x64/zutto_dekiru
Zutto Dekiru
<hr/>
22  encoder/x86/add_sub
添加/子编码器
<hr/>
23  encoder/x86/alpha_mixed
alpha2字母数字混合箱编码器
<hr/>
24  encoder/x86/alpha_upper
alpha2字母数字大写编码器
<hr/>
25  encoder/x86/avoid_underscore_tolower
避免下划线/倾角
<hr/>
26  encoder/x86/avoid_utf8_tolower
避免使用UTF8/tolower
<hr/>
27  encoder/x86/bloxor
Bloxor-基于变质块的XOR编码器
<hr/>
28  encoder/x86/bmp_polyglot
BMP多语言
<hr/>
29  encoder/x86/call4_dword_xor
Call+4 Dword XOR编码器
<hr/>
30  encoder/x86/context_cpuid
基于CPUID的上下文键合有效载荷编码器
<hr/>
31  encoder/x86/context_stat
基于Stat（2）的上下文键合有效载荷编码器
<hr/>
32  encoder/x86/context_time
时间（2）基于上下文键控有效载荷编码器
<hr/>
33  encoder/x86/countdown
单字节XOR倒计时编码器
<hr/>
34  encoder/x86/fnstenv_mov
可变长度FNSTENV/MOV DWORD XOR编码器
<hr/>
35  encoder/x86/jmp_call_additive
跳/调用XOR添加反馈编码器
<hr/>
36  encoder/x86/nonalpha
非-Alpha 编码器
<hr/>
37  encoder/x86/nonupper
x86/非upper编码器
<hr/>
38  encoder/x86/opt_sub
子编码器（优化）
<hr/>
39  encoder/x86/service
注册服务
<hr/>
40  encoder/x86/shikata_ga_nai
多态性XOR添加反馈编码器
<hr/>
41  encoder/x86/single_static_bit
单个静态位
<hr/>
42  encoder/x86/unicode_mixed
alpha2字母数字Unicode混合箱编码器
<hr/>
43  encoder/x86/unicode_upper
alpha2字母数字Unicode大写编码器
<hr/>
44  encoder/x86/xor_dynamic
动态密钥XOR编码器


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


---


> 
<h3>2.3、格式：</h3>
在输入命令的时候加上
-e （编码器）


> 
<h3>2.4、示例：</h3>
generate -b '\x00\xff' -f exe -e x86/shikata_ga_nai -i 5 -k -x /usr/share/windows-binaries/radmin.exe -o /root/1.exe



