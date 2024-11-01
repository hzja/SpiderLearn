# 原创
：  【kali-漏洞利用】（3.2）Metasploit基础（上）：基础知识

# 【kali-漏洞利用】（3.2）Metasploit基础（上）：基础知识

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、Armitage（图形管理工具）](#%E4%BA%8C%E3%80%81Armitage%EF%BC%88%E5%9B%BE%E5%BD%A2%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%EF%BC%89)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、使用：](#2.2%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

[第一步：启动Metasploit 服务](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8Metasploit%20%E6%9C%8D%E5%8A%A1)

[第二步：启动Armitage工具](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8Armitage%E5%B7%A5%E5%85%B7)

[第三步：显示基本信息](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%98%BE%E7%A4%BA%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)

[第四步：启动Metasploit的RPC服务](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8Metasploit%E7%9A%84RPC%E6%9C%8D%E5%8A%A1)

[第五步：连接到Metasploit服务+模块分析](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%9E%E6%8E%A5%E5%88%B0Metasploit%E6%9C%8D%E5%8A%A1%2B%E6%A8%A1%E5%9D%97%E5%88%86%E6%9E%90)

[第六步：选中poor（推荐）](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E9%80%89%E4%B8%ADpoor%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%89)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
Metasploit是一款开源的安全漏洞检测工具，可以帮助安全和IT专业人士识别安全性问题，验证漏洞的缓解措施，并管理专家驱动的安全性进行评估，提供真正的安全风险情报。这些功能包括智能开发，代码审计，Web应用程序扫描，社会工程。团队合作，在Metasploit和综合报告提出了他们的发现


---


---


## 二、Armitage（图形管理工具）

> 
<h3>2.1、简介：</h3>
Armitage 组件是Metasploit 框架中一个完全交互式的图形化用户接口， Armitage 工具包含Metasploit 控制台， 通过使用其标签特性， 用户可以看到多个Metasploil 控制台或多个Meterpreter 会话


> 
<h3>2.2、使用：</h3>
<h4>第一步：启动Metasploit 服务</h4>
Metasploit默认使用PostgreSQL存储渗透测试所需的数据表，所以在启动Armitage之前需要首先启动 PostgreSQL服务和Metasploit服务
<hr/>
启动 PostgreSQL服务
**sudo service postgresql start**
<hr/>

启动Metasploit 服务


<hr/>
或者直接在终端输入
sudo msfconsole

<hr/>
<h4>第二步：启动Armitage工具</h4>
终端输入sudo armitage
（或者在kali中找这个程序）

<hr/>
<h4>第三步：显示基本信息</h4>
界面显示了连接Metasploit服务的基本信息

<hr/>
<h4>第四步：启动Metasploit的RPC服务</h4>
点击是即可


<hr/>

<h4>第五步：连接到Metasploit服务+模块分析</h4>




1、左上：预配置模块，用户可以在模块列表中使用空格键搜索提供的模块
2、右上：目标系统， 用户能执行利用涌洞攻击
3、下：Metasploit标签，运行多个Meterpreter命令或控制台会话，并且同时显示
<hr/>
<h4>第六步：选中poor（推荐）</h4>




#### 第一步：启动Metasploit 服务

---


---


#### 第三步：显示基本信息

---


#### 第五步：连接到Metasploit服务+模块分析

---

