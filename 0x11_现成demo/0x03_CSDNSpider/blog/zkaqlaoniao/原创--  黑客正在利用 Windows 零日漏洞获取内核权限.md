# 原创
：  黑客正在利用 Windows 零日漏洞获取内核权限

# 黑客正在利用 Windows 零日漏洞获取内核权限

名为 Lazarus Group 的朝鲜威胁攻击者正利用 Windows AppLocker 驱动程序 (appid.sys) 中的一个缺陷作为零日漏洞来获取内核级访问权限并关闭安全工具，从而允许他们绕过嘈杂的 BYOVD（自带漏洞）驾驶员）技术。

安全研究人员Avast 检测到了这一活动，并立即向 Microsoft 报告了该活动，导致该缺陷得到修复，该缺陷现在被追踪为 CVE-2024-21338，作为 2024 年 2 月 补丁的一部分。然而，微软并未将该漏洞标记为零日漏洞。

Avast 报告 称，Lazarus 组织利用 CVE-2024-21338 在其 FudModule rootkit 的更新版本中创建读/写内核原语，并且该rootkit曾滥用 戴尔驱动程序 进行 BYOVD 攻击，ESET 于 2022 年末首次记录该 rootkit。

新版本的 FudModule 在隐秘性和功能方面显着增强，包括用于逃避检测和关闭 Microsoft Defender 和 CrowdStrike Falcon 等安全保护的新技术和更新技术。此外，通过检索大部分攻击链，Avast 发现了 Lazarus 使用的一个先前未记录的远程访问木马 (RAT)，该安全公司承诺在 4 月份的BlackHat Asia上公布关于该木马的更多细节  。

### Lazarus 组织对0day 漏洞利用详情

该恶意软件利用了 Microsoft 的“appid.sys”驱动程序中的漏洞，该驱动程序是一个提供应用程序白名单功能的 Windows AppLocker 组件。

Lazarus 通过操纵 appid.sys 驱动程序中的输入和输出控制 (IOCTL) 调度程序来调用任意指针来利用它，欺骗内核执行不安全代码，从而绕过安全检查。

FudModule rootkit 与漏洞利用程序构建在同一模块内，执行直接内核对象操作 (DKOM) 操作以关闭安全产品、隐藏恶意活动并保持受破坏系统的持久性。（安全产品包括 AhnLab V3 Endpoint Security、Windows Defender、CrowdStrike Falcon 和 HitmanPro 反恶意软件解决方案）

Avast 在新的 rootkit 版本中观察到了新的隐秘功能和扩展功能，例如通过操纵句柄表条目来怀疑受 Protected Process Light (PPL) 保护的进程的能力、通过 DKOM 进行选择性和有针对性的中断、篡改驱动程序签名强制和安全方面的增强启动等等。

Avast 指出，这种新的利用策略标志着威胁攻击者的内核访问能力的重大演变，使他们能够发起更隐蔽的攻击，并在受感染的系统上持续更长时间。

安全研究人员表名，针对该漏洞的唯一有效的安全措施是尽快应用 2024 年 2 月补丁进行更新，因为 Lazarus 对 Windows 内置驱动程序的利用使得检测和阻止攻击变得特别困难。

参考链接：https://www.freebuf.com/news/392838.html

图片来源：https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-gain-kernel-privileges/

原文链接：https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-gain-kernel-privileges/

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
