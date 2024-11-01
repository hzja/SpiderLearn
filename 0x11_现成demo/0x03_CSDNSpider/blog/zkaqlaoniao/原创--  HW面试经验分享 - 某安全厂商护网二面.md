# 原创
：  HW面试经验分享 | 某安全厂商护网二面

# HW面试经验分享 | 某安全厂商护网二面

#### 某厂商蓝队初级二面分享

所面试的公司：某安全厂商

薪资待遇：待定

所在城市：上海

面试职位：蓝队初级

面试过程：感觉良好，就是有个别的小问题，没有说好。

面试官的问题：

---


##### 第1个问题(自我介绍)

```
hr：先自我介绍一下
I：面试官你好，我叫xxx，来自xxxxxx是一名大二在校生，学的专业是计算机网络技术，在校期间我参加过python程序设计实验室，编写过简单python爬虫脚本(如爬取豆瓣数据之类的)。专业技能的话，我熟悉常见的web漏洞和渗透测试工具的使用，然后我利用所学的专业技能，在漏洞盒子上提交过一些漏洞。我个人比较认真负责，喜欢和志同道合的人研究技术，每天都会锻炼，去预防职业疾病。最后，综上，我认为我的校园学习，我所掌握的能力，以及我做过的项目。我能够胜任这个渗透测试工程师(xxx)的岗位。
我的自我介绍完毕。
```

---


##### 第2个问题(安全设备)

```
hr：你有没有接触过哪些安全设备
I：入侵防御系统IPS，
        入侵检测系统IDS
        防火墙
        数据库审计系统
        日志审计系统
        堡垒机
        漏洞扫描系统
        数据安全态势感知平台
        终端安全管理系统
        WAF
        蜜罐
```

---


##### 第3个问题(误报)

```
hr：基于IDS的告警，怎么判断哪些是误报，哪些是确实攻击的
I：(1)设备误报：
来自外网的误报说明安全设备需要进行策略升级，不需要处置。
如果是来自内网的误报可以和负责人协商一下看能不能解决，
有必要的话添加白名单处理。

  (2)如果像SQL注入的误报：
先看ip，如果ip是公司内部的再看内部人员有没有相关操作，如果不是公司人员业务的操作那就是攻击了，然后分析payload,分析它写的payload安全设备能否它进行过滤拦截，如果它确实能绕过，那就应该攻击成功了，成功的话赶紧上报，做应急响应，做出相应处理，添加过滤规则，修改数据库中能修改的数据比如管理员账号密码啥的
```

---


##### 第3.1个问题(Shiro反序列化漏洞利用的告警，怎么判断它攻击成功)

```
hr：如果看到一条告警是Shiro反序列化漏洞利用的一条告警，那么怎么确定是真实的，而不是数据交互产生的误报
I：xxx（这我不知道，下面是问AI的）

1.确认告警来源：确认该告警来源，是通过安全设备观察和检测到的还是通过其他方式发现的。确认告警来源可以规避数据交互产生的误报问题。

```

`2.了解Shiro反序列化漏洞利用的原理：了解Shiro反序列化漏洞利用的原理可以帮助我们判断告警的真实性。`

`Shiro是一款Java安全框架，其中的Session序列化过程中存在反序列化漏洞。攻击者可以利用该漏洞，构造恶意Session序列化数据，通过反序列化来执行远程代码或对Session数据进行篡改。因此，如果确认该系统中存在Shiro反序列化漏洞，那么该告警可能是真实的。`

`3.检查攻击来源和目标系统：`

`如果检查发现攻击来源与目标系统都在同一内部网络中，并且该内部网络中已知存在Shiro反序列化漏洞，那么该告警的真实性更高。<br/><br/> 4.检查攻击行为：如果检查发现攻击行为与已知的Shiro反序列化漏洞利用方法相同，例如尝试构造恶意Session序列化数据进行反序列化，或者在Session中存储恶意数据，那么该告警的真实性也更高。<br/><br/> 总之，要确定该告警是否真实，需要通过多个方面进行确认，同时需要加强安全审计和监控，通过对系统漏洞进行及时修补和更新以及强化数据安全以防止安全漏洞的利用。`

---


##### 第3.2个问题(SQL注入，延时注入的告警，怎么判断它攻击成功)

```
hr：如果看到SQL注入，延时注入的告警，你怎么判断它攻击成功
I：
```

`xxx(面试的时候，我说和上面的误报差不多一样的，然后问了下AI，就感觉说的不是很好`)

要判断SQL注入，延时注入是否攻击成功，可以参考以下几个方面来进行判断：

<br/>`1.审查目标数据库记录：如果攻击成功，攻击者通常能够从数据库中检索，修改或删除敏感数据。通过审查数据库记录可以判断攻击是否成功。如果发现敏感数据被修改、增加或删除等异常行为，那么有可能是攻击成功了。<br/><br/> 2.检查数据库日志：数据库常常会记录访问和执行查询的日志，攻击者在利用SQL注入攻击时也会生成一些异常SQL查询语句。可以通过检查SQL查询语句的日志来判断是否存在异常查询语句，这些查询语句可能是攻击者用来执行恶意操作的。<br/><br/> 3.分析网络流量：可以通过分析网络流量来判断SQL注入或延时注入攻击是否成功。如果攻击成功，数据通常会被发送到攻击者的服务器，可以根据网络流量的情况来判断是否攻击成功。可以使用网络监控工具实时查看网络流量，对异常流量进行分析和跟踪。<br/><br/> 4.使用SQL注入漏洞测试工具：可以使用SQL注入漏洞测试工具来进行测试，确认漏洞是否真的存在以及攻击是否成功。<br/><br/> 需要注意的是，判断SQL注入或延时注入攻击是否成功并不是一件容易的事情，需要进行逐个的审计和验证。同时，要注意在处理SQL注入攻击时，不要随便删除或修改数据库中的数据，需要先备份数据库再进行操作，以免误操作影响业务运行。`

---


##### 第4个问题(应急响应)

```
hr：你之前有没有进行过，应急响应的工作
I：应急响应基本思路流程：
收集信息：收集客户信息和中毒主机信息，包括样本
判断类型：判断是否是安全事件，何种安全事件，勒索、挖矿、断网、DoS 等等
抑制范围：隔离使受害⾯不继续扩⼤
深入分析：日志分析、进程分析、启动项分析、样本分析方便后期溯源
清理处置：杀掉进程，删除文件，打补丁，删除异常系统服务，清除后门账号防止事件扩大，处理完毕后恢复生产
产出报告：整理并输出完整的安全事件报告
```

---


##### 第5个问题(溯源)

```
hr：你有没有对溯源，进行过了解
I：基本步骤：
1.攻击源捕获
    安全设备报警，如扫描IP、威胁阻断、病毒木马、入侵事件等
    日志与流量分析，异常的通讯流量、攻击源与攻击目标等
    服务器资源异常，异常的文件、账号、进程、端口，启动项、计划任务和服务等
    邮件钓鱼，获取恶意文件样本、钓鱼网站 URL 等
    蜜罐系统，获取攻击者 ID、电脑信息、浏览器指纹、行为、意图的相关信息
2.溯源反制手段
    IP 定位技术
    根据IP定位物理地址–代理 IP
     溯源案例：通过 IP 端口扫描，反向渗透服务器进行分析，最终定位到攻击者相关信息
    ID 追踪术
    ID 追踪术，搜索引擎、社交平台、技术论坛、社工库匹配
     溯源案例：利用 ID 从技术论坛追溯邮箱，继续通过邮箱反追踪真实姓名，通过姓名找到相关简历信息
    网站 url
    域名 Whois 查询–注册人姓名、地址、电话和邮箱 --域名隐私保护
    溯源案例：通过攻击 IP 历史解析记录/域名，对域名注册信息进行溯源分析
恶意样本分析
    提取样本特征、用户名、ID、邮箱、C2 服务器等信息–同源分析
    溯源案例：样本分析过程中，发现攻击者的个人 ID 和 QQ，成功定位到攻击者
社交账号
    基于 JSONP 跨域，获取攻击者的主机信息、浏览器信息、真实 IP 及社交信息等
    利用条件：可以找到相关社交网站的 jsonp 接口泄露敏感信息，相关网站登录未注销
3.攻击者画像
    攻击路径
    攻击目的：拿到权限、窃取数据、获取利益、DDOS 等
    网络代理：代理 IP、跳板机、C2 服务器等
    攻击手法：鱼叉式邮件钓鱼、Web渗透、水坑攻击、近源渗透、社会工程等

攻击者身份画像
    虚拟身份：ID、昵称、网名
    真实身份：姓名、物理位置
    联系方式：手机号、qq/微信、邮箱
    组织情况：单位名称、职位信息

```

`技巧`

`    域名、ip 反查目标个人信息<br/>     支付宝转账，确定目标姓氏<br/>     淘宝找回密码，确定目标名字<br/>     企业微信手机号查公司名称<br/>     REG007 查注册应用、网站<br/>     程序 PDB 信息泄露`

---


##### 第6个问题(内网渗透：票据伪造的原理)

```
hr：票据伪造的原理
I：xxx(说的不是很清楚，就不写了，学过内网的话，也知道是怎么回事，下面是问AI的)
    在内网渗透中，票据伪造是攻击者获取内部系统访问权限的一种重要手段。在内网渗透中，攻击者常常使用以下方式进行票据伪造：

1.Kerberos票据伪造：Kerberos是内部网络中常用的身份验证协议，攻击者可以在各种方式下获取了Kerberos票据，或者直接访问被保护资源后通过Kerberos票据离线生成票据。攻击者可以使用这些票据来进行Kerberos票据伪造，并将伪造的票据发送给目标系统，从而获得对目标系统的访问权限。此外，攻击者还可以针对Kerberos协议中的安全漏洞进行攻击，从而获取Kerberos票据并进行伪造。

2.NTLM票据伪造：NTLM票据也是内部网络中常用的身份验证方式。攻击者可以利用各种方式来获取NTLM票据，然后使用NTLM票据伪造技术来发送伪造的NTLM票据，从而获取对目标系统的访问权限。

3.Web应用程序漏洞：许多内部网络中的Web应用程序存在漏洞，攻击者可以利用这些漏洞来获取目标用户的票据，并使用票据伪造技术来修改票据内容或伪造票据，以获得访问目标系统的权限。

4.会话劫持：攻击者可以利用会话劫持技术，伪造目标用户的会话，从而获取访问目标系统的权限。

总之，在内网渗透中，攻击者通过大量的内部信息收集和渗透测试，获得相应系统的权限和票据，然后使用票据伪造技术来实现身份欺骗，进而深入渗透系统。因此，防范票据伪造攻击的关键在于加强身份验证、限制用户权限、审查安全漏洞和及时修补和更新系统补丁，以及集中管理票据等措施。
```

---


面试结果：待通知(要等国护发通知，然后厂商根据客户的需求，再结合我的水平，才能确定，是否能够发我offer)

面试难度：我感觉简单(可能是我面的多的原因吧)

面试感受：在学的扎实的情况下，除了一些其他问题，剩下的都能说出来。

如果，面试的时候，面试官问的问题，你知道，你也做过，但是有点模糊，你就和面试官说一下，给我想一分钟或者想30秒。

像我票据的问题，我知道怎么说，但是没有和面试官说让我想一下，不然我觉得我可以说的更清楚，说的更好

给大家的建议：多面试，就知道问什么了

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
