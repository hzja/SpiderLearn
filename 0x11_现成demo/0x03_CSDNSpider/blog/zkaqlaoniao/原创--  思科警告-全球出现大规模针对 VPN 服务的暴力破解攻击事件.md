# 原创
：  思科警告：全球出现大规模针对 VPN 服务的暴力破解攻击事件

# 思科警告：全球出现大规模针对 VPN 服务的暴力破解攻击事件

近日，全球范围内出现了大量针对思科、CheckPoint、Fortinet、SonicWall 和 Ubiquiti 设备的 VPN 和 SSH 服务的大规模凭据暴力破解活动。

原文地址：https://mp.weixin.qq.com/s/UoMgC8Bp6OMJiXgeU3XbyA

暴力攻击是指使用许多用户名和密码尝试登录帐户或设备，直到找到正确的组合。一旦获得正确的凭据，威胁者就可以利用它们劫持设备或访问内部网络。

但据 Cisco Talos 称，这种新的暴力攻击活动混合使用了与特定组织相关的有效和通用员工用户名。

研究人员称，他们最早于今年3月18日发现了此类攻击事件，所有攻击都源于 TOR 出口节点以及其他各种匿名工具和代理服务器，威胁者利用这些工具和代理服务器来躲避拦截。

思科塔洛斯报告警告称：根据目标环境的不同，此类攻击可能会导致未经授权的网络访问、账户锁定或拒绝服务状况。与这些攻击有关的流量随着时间的推移而增加，并可能继续上升。

用于实施攻击的一些服务包括 TOR、VPN Gate、IPIDEA Proxy、BigMama Proxy、Space Proxy、Nexus Proxy 和 Proxy Rack。

思科的研究人员报告称，以下八项服务是此次活动的主要目标：

该恶意活动没有具体针对特定行业或地区，表明其采取的是随机、机会性攻击的更广泛策略。

Talos 团队在 GitHub 上共享了该活动的完整入侵指标 (IoC) 列表，其中包括攻击者的 IP 地址（用于列入拦截列表）以及暴力攻击中使用的用户名和密码列表。

今年 3 月下旬，思科警告称，针对思科安全防火墙设备上配置的远程访问 VPN (RAVPN) 服务，出现了一波密码喷射攻击。

这种密码喷射攻击对薄弱的密码很有效，很多用户名使用的都是一小套常用密码，而不是使用大字典暴力破解。

安全研究员 Aaron Martin 根据观察到的攻击模式和目标范围，将这些攻击归因于一个名为「Brutus」的恶意软件僵尸网络。

思科此前针对该攻击提出的建议包括：

目前尚未核实此次攻击是否是之前攻击的延续，思科公司目前也并未对这两起事件的关联情况进行回应。

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
