# 转载
：  Weblogic CVE 2023-21839漏洞复现

# Weblogic CVE 2023-21839漏洞复现

WebLogic 存在远程代码执行漏洞（CVE-2023-21839/CNVD-2023-04389），由于Weblogic IIOP/T3协议存在缺陷，当IIOP/T3协议开启时，允许未经身份验证的攻击者通过IIOP/T3协议网络访问攻击存在安全风险的WebLogic Server，漏洞利用成功WebLogic Server可能被攻击者接管执行任意命令导致服务器沦陷或者造成严重的敏感数据泄露。

### 危害级别：高

### 影响版本

本次漏洞影响范围如下：

12.2.1.2.0<br/> 12.2.1.1.0<br/> 12.2.1.3.0<br/> 12.2.1.0.0<br/> 12.2.1.4.0<br/> 14.1.1.0.0<br/> 12.1.2.0.0<br/> 12.1.3.0.0<br/> 10.3.6.0

### FOFA Query：
| app="BEA-WebLogic-Server" || app="Weblogic_interface_7001" 

Vulfocus 已经集成该漏洞环境可通过以下环境使用：
| docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.2.1.2.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.2.1.1.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.2.1.3.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.2.1.4.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.2.1.0.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:14.1.1.0.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.1.2.0.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:12.1.3.0.0-jdk-release<br/> docker pull vulfocus/vcpe-1.0-a-oracle-weblogic:10.3.6.0-jdk-release 

### 漏洞复现

本次使用安装环境-docker部署Vulhub

1、 安装最新版的docker

注：部分linux系统不适配docker最新版本，解决办法：升级linux内核或者降低docker版本，更换docker具体操作如下:

curl -s https://get.docker.com/ | sh

（1）指定版本：sudo apt-get install docker-ce=17.12.1~ce-0~ubuntu

（2）卸载docker-ce<br/> sudo apt-get autoremove docker-ce<br/> （3）显示稳定可使用版本<br/> sudo apt-cache madison docker-ce

2、启动docker服务

service docker start

3、安装pip

apt-get install python-pip

4、安装compose

pip install docker-compose (网速太慢的话，本机下载上传到虚拟机)

5、配置docker加速

curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io

6、下载或克隆Vulhub

git clone https://github.com/vulhub/vulhub.git(网速太慢的话，本机下载上传到虚拟机)

7、进入Vulhub

cd vulhub-master/

8、进入某一个漏洞/环境的目录

cd /home/vulhub1/桌面/vulhub-master/weblogic/CVE-2023-21839

9、编译漏洞环境

sudo docker-compose build(有的需要编译，有的不需要，这个漏洞不需要)

10、启动漏洞环境

docker-compose up -d

11、查看漏洞环境

docker ps

12、访问漏洞环境

VPS公网IP+映射端口 ，可以查看每个漏洞目录下的remade.md文件，cat查看

13、结束漏洞环境（下次无需编译，须在当前目录执行命令）

docker-compose down

14、访问http://127.0.0.1:7001/console/login/LoginForm.jsp，漏洞环境已经起来

注：本次目的就是反弹漏洞靶场服务器A的shell

### 利用方式

#### DNSLOG探测

<br/> EXP链接：https://github.com/DXask88MA/Weblogic-CVE-2023-21839（jar包形式）

源码poc：

```
来源：https://www.freebuf.com/vuls/364212.html
```

> 
声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！


@**学习更多渗透技能！体验靶场实战练习**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/33f96f7dd9784526b56a03d704e96a66.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/bab4efbad2404331ae5c06a29f2b2ba7.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/51a79a0f7119401bb3a97cd78c711d4b.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/3d346e7a5a054ef196f0c63e39dd5553.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/5630b8aabe7b4258a05a27933c1053ce.png" width="665"/>

应急响应笔记

学习路线
