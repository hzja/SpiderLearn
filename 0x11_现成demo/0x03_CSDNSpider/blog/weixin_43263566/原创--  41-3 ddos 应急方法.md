# 原创
：  41-3 ddos 应急方法

# 41-3 ddos 应急方法

#### 一、常规DDoS应急办法

1.  定期扫描和清查安全漏洞：定期对网络主节点进行扫描，及时清理可能存在的安全漏洞，以及新出现的漏洞。 
1.  检查访问者来源：通过反向路由器查询的方法检查访问者的IP地址是否真实，如果不真实，则予以屏蔽，以防黑客攻击使用假IP地址方式迷惑用户。 
1.  在骨干节点配置防火墙：防火墙本身具有一定的防护能力，可以抵御DDoS攻击和其他一些攻击。在发现受到攻击的时候，可以将攻击导向一些牺牲主机，保护真正的主机不被攻击。 
1.  采用分布式集群防御：分布式集群防御是目前网络安全界防御大规模DDoS攻击最有效的方法。该方法拥有多个节点，当一个节点受攻击无法提供服务时，系统自动切换另一个节点，并将攻击者的数据包全部返回发送点，使攻击源成为瘫痪状态，从更为深度的安全防护角度影响企业的安全执行决策。 

####  二、云防御体系

1.  设置黑名单：建立一个黑名单，将已知的恶意IP地址或攻击源加入其中，以屏蔽来自这些源的流量，减少潜在攻击的影响。 
1.  畸形报文检测：实施对网络传输中的报文进行监测和分析，检测是否存在畸形报文，即不符合协议规范的报文，以此防止攻击者利用畸形报文进行攻击。 
1.  扫描窥探报文：对网络传输中的数据包进行扫描，识别并拦截可能的窥探报文，防止攻击者通过窥探获取敏感信息或发现系统漏洞。 
1.  虚假源流量检测：通过分析网络流量的源地址，识别虚假源流量，防止攻击者伪造源地址进行攻击和欺骗。 
1.  异常连接威胁检测：监测
