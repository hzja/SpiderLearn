# 原创
：  【kali-权限提升】（4.2.6）社会工程学工具包（中）：中间人攻击工具Ettercap

# 【kali-权限提升】（4.2.6）社会工程学工具包（中）：中间人攻击工具Ettercap

**目录**

[Ettercap工具](#Ettercap%E5%B7%A5%E5%85%B7)

[1.1、第一步：启动Ettercap工具](#1.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8Ettercap%E5%B7%A5%E5%85%B7)

[1.2、第二步：配置](#1.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%85%8D%E7%BD%AE)

[1.3、第三步：主机发现](#1.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E4%B8%BB%E6%9C%BA%E5%8F%91%E7%8E%B0)

[1.4、第四步：选择目标](#1.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E7%9B%AE%E6%A0%87)

[1.5、第五步：选择攻击类型](#1.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E9%80%89%E6%8B%A9%E6%94%BB%E5%87%BB%E7%B1%BB%E5%9E%8B)

[1.6、第六步：分析](#1.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90)

---


## Ettercap工具

> 
<h3>1.1、第一步：启动Ettercap工具</h3>
sudo ettercap -G


 Ettercap启动界面


> 
<h3>1.2、第二步：配置</h3>
选择要使用的网卡，点击"对号"



> 
<h3>1.3、第三步：主机发现</h3>
点击"搜索"按钮，进行主机发现

 点击Host List可以查看列表



> 
<h3>1.4、第四步：选择目标</h3>
将想要欺骗的**网关**添加到"add to target 1"


将想要欺骗**受害者**添加到"add to target 2"




> 
<h3>1.5、第五步：选择攻击类型</h3>
点击"圆圈"（MITM Menu）
选择"arp poisoning spoofing"（ARP中毒欺骗）



默认选择"sniff remote connections"（嗅探远程连接）
点击"OK"，ettercap会自动开始arp欺骗


查看默认网关的时候，发现我搞错了
（发现刚开始选择的网关地址是192.168.190.1    选错了  这里是192.168.190.2）

然后重新上面过程配置了一遍


> 
<h3>1.6、第六步：分析</h3>
查看网关地址
输入arp -a



