# 原创
：  DinodasRAT 恶意软件以Linux服务器为目标对多国进行攻击

# DinodasRAT 恶意软件以Linux服务器为目标对多国进行攻击

近日，有安全研究人员发现 Red Hat 和 Ubuntu 系统也受到了 Linux 版 DinodasRAT恶意软件的攻击，并且该恶意软件可能从 2022 年就开始运行了。

此前网络安全公司 ESET 还在一次名为 "Jacana 行动 "的间谍活动中发现 DinodasRAT 入侵了 Windows 系统，当时该恶意软件的攻击目标是政府。

### **DinodasRAT 的详细信息**

在本周早些时候的一份报告中，卡巴斯基的研究人员表示，DinodasRAT 的 Linux 变体在执行时会在其二进制文件所在的目录中创建一个隐藏文件，该文件充当互斥器，以防止多个实例在受感染的设备上运行。

然后，恶意软件使用 SystemV 或 SystemD 启动脚本在计算机上设置持久性。为了使检测变得复杂，恶意软件会在父进程等待时再次执行。

恶意软件的执行逻辑 **（图片来源：卡巴斯基）**

使用感染、硬件和系统详细信息对受感染的计算机进行标记，并将报告发送到命令和控制 (C2) 服务器以管理受害主机。

为受害者创建唯一 ID **（<em>图片来源：**卡巴斯基）</em>

该恶意软件与 C2 服务器的通信通过 TCP 或 UDP 进行，在 CBC 模式下利用微型加密算法 (TEA)以确保安全的数据交换。

Dinodas网络数据包结构 **（<em><em>图片来源：**</em>卡巴斯基）</em>

DinodasRAT 具有旨在监视、控制和从受感染系统中窃取数据的功能。其主要特点包括：

研究人员表示，DinodasRAT 使攻击者能够完全控制受感染的系统。攻击者主要使用恶意软件来通过 Linux 服务器获取和维护对目标的访问。

卡巴斯基表示，后门功能齐全，使攻击者能够完全控制受感染的机器，从而实现数据泄露和间谍活动。 

卡巴斯基没有提供有关初始感染方法的详细信息，但指出自 2023 年 10 月以来，该恶意软件影响了中国、台湾、土耳其和乌兹别克斯坦的受害者。

原文地址：https://www.bleepingcomputer.com/news/security/dinodasrat-malware-targets-linux-servers-in-espionage-campaign/?traffic_source=Connatix#google_vignette

图片来源：https://www.bleepingcomputer.com/news/security/dinodasrat-malware-targets-linux-servers-in-espionage-campaign/?traffic_source=Connatix#google_vignette

  申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
