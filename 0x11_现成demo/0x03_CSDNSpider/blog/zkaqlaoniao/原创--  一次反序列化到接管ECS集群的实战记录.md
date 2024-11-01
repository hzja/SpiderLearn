# 原创
：  一次反序列化到接管ECS集群的实战记录

# 一次反序列化到接管ECS集群的实战记录

##### 1.shiro反序列化

在某次测试的时候发现了一个后台管理系统，目测站点是若依管理系统(根据图标、站点背景图等)<br/>  

<br/> 若依管理系统版本 &lt; v4.6.2存在默认shiro key的问题(从4.6.2版本开始默认采用随机key)，因此容易导致shiro反序列化的发生，所以看到若依管理系统可以直接拿工具去测一下是否存在密钥泄露的问题<br/> 工具参考链接：https://github.com/j1anFen/shiro_attack

<br/> 如上图，此站点存在shiro反序列化漏洞，权限为root，看看有没有其他有用的东西

<br/> 查看arp表，发现还有几个ip的解析记录，应该还有的搞

##### 2.获取AK，接管ECS集群

在当前目录下有个config目录，config目录中有一个application.yml文件，猜测是若依的配置文件，打开发现了阿里云的Access-Key

<br/> 既然有了AK，那么何不尝试一下能不能直接接管云服务呢(笑)，说干就干<br/> 工具参考链接：https://github.com/teamssix/cf

<br/> 如图，根据拿到的AK成功接管了该OSS和ECS资源，至此测试结束

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
