# 原创
：  【kali-信息收集】（1.9）Metasploit+搜索引擎工具Shodan

# 【kali-信息收集】（1.9）Metasploit+搜索引擎工具Shodan

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、使用](#%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8)

[2.1、过滤语法](#2.1%E3%80%81%E8%BF%87%E6%BB%A4%E8%AF%AD%E6%B3%95)

[City、Country命令](#City%E3%80%81Country%E5%91%BD%E4%BB%A4)

[HOSTNAME命令](#HOSTNAME%E5%91%BD%E4%BB%A4)

[NET命令](#NET%E5%91%BD%E4%BB%A4)

[Title命令](#Title%E5%91%BD%E4%BB%A4)

[关键字搜索](#%E5%85%B3%E9%94%AE%E5%AD%97%E6%90%9C%E7%B4%A2)

[组合搜索](#%E7%BB%84%E5%90%88%E6%90%9C%E7%B4%A2)

[其他搜索术语](#%E5%85%B6%E4%BB%96%E6%90%9C%E7%B4%A2%E6%9C%AF%E8%AF%AD)

[2.2、Metasploit实现Shodan搜索](#2.2%E3%80%81Metasploit%E5%AE%9E%E7%8E%B0Shodan%E6%90%9C%E7%B4%A2)

[(1)注册](#%281%29%E6%B3%A8%E5%86%8C)

[(2)获取API](#%282%29%E8%8E%B7%E5%8F%96API)

[(3)启动PostgreSQL服务](#%283%29%E5%90%AF%E5%8A%A8PostgreSQL%E6%9C%8D%E5%8A%A1)

[(4)启动Metasploit服务](#%284%29%E5%90%AF%E5%8A%A8Metasploit%E6%9C%8D%E5%8A%A1)

[(5)启动MSF终端](#%285%29%E5%90%AF%E5%8A%A8MSF%E7%BB%88%E7%AB%AF)

[(6)选择模块](#%286%29%E9%80%89%E6%8B%A9%E6%A8%A1%E5%9D%97)

[(7)配置参数](#%287%29%E9%85%8D%E7%BD%AE%E5%8F%82%E6%95%B0)

[(8) 启动搜索引擎](#%288%29%20%E5%90%AF%E5%8A%A8%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
Shodan是互联网上最强人的一个搜索引学工具。该工具不是在网上搜索网址， 而是直接搜索服务器。Shodan可以说是一款＂ 黑暗＂ 谷歌，一直不停的在寻找心所有和互联网连接的服务器、摄像头、打印机和路由器等。每个月都会在大约5亿个服务器上日夜不停的搜集信息
www.shodanhq.com


---


---


## 二、使用

> 
<h3>2.1、过滤语法</h3>
<h4>City、Country命令</h4>
使用City和Country命令可以缩小搜索的地理位置
1、country:china表示从中国进行搜索
2、city:beijing表示从北京城市搜索。
City和Countly命令也可以结合使用
3、country:china city:beijing
<hr/>
<h4>HOSTNAME命令</h4>
HOSTNAME命令通过指定主机名来扫描整个域名
hostname:google表示搜索google主机
<hr/>
<h4>NET命令</h4>
使用NET命令扫描单个IP 或一个网络范围<br/> net:192.168.190.131：扫描主机192.168.190.131<br/> net:192.168. 190.0/24:：扫描192.168.190.0/24网络内所有主机
<hr/>
<h4>Title命令</h4>
使用Title命令可以搜索项目
title: "Server Room"：表示搜索服务器机房信息
<hr/>
<h4>关键字搜索</h4>
Shodan使用一个关键字搜索是最受欢迎的方式。如果知道目标系统使用的服务器类型或嵌入式服务器名， 来搜索一个Web页面是很容易的
apache/2.2.8 200 ok：表示搜索所有Apache服务正在运行的2.2.8版本， 并且仅搜索打开的站点
apache/2.2.8 -401 -302：表示跳过显示401的非法页或302删除页
<hr/>
<h4>组合搜索</h4>
IIS/7.0 hostname:YourCompany.com city:Boston表示搜索在波士顿所有正在运行IIS/7.0的Microsoft服务器
llS/5.0 hostname:YourCompany.com country:FR表示搜索在法国所有运行llS/5.0的系统
Title:camera hostname: YourCompany.com表示在某台主机中标题为camera的信息
geo:33.5,36.3 os:Linux表示使用坐标轴（经度33.S, 纬度36.3)的形式搜索Linux操作系统
<hr/>
<h4>其他搜索术语</h4>
Port：通过端口号搜索
OS：通过操作系统搜索
After或Before：使用时间搜索服务


#### HOSTNAME命令

---


#### Title命令

---


#### 组合搜索

---


> 
<h3>2.2、Metasploit实现Shodan搜索</h3>
<h4>(1)注册</h4>
在Shodanhq.com网站注册一个免费的账户

<hr/>
 
<h4>(2)获取API</h4>
从http://www.shodanhq.com/api_doc网站获取API key

<hr/>
 
<h4>(3)启动PostgreSQL服务</h4>
service postgresql start

或者
sudo service postgresql start
<hr/>
<h4>(4)启动Metasploit服务</h4>
service metasploit start
或者
sudo service metasploit start
（注：这一步可能不需要了，metasploit已经被废弃替代了）
<hr/>
 
<h4>(5)启动MSF终端</h4>
msfconsole

<hr/>
<h4>(6)选择模块</h4>
选择auxiliary/gather/shodan_ search模块， 并查看该模块下可配控的选项参数
输出信息中，有四个必须配置选项参数，其中有两个已经配置， QUERY和SHODAN_APIKEY还没有配置 
use auxiliary/gather/shodan_search

show options

<hr/>
<h4>(7)配置参数</h4>
配置QUERY和SHODAN_APIKEY选项参数
1、set SHODAN_APIKEY （+API值）
2、set QUERY （+要搜索的关键字）

<hr/>
 
<h4>(8) 启动搜索引擎</h4>
run



#### (2)获取API

---


#### (4)启动Metasploit服务

---


#### (6)选择模块

---


#### (8) 启动搜索引擎
