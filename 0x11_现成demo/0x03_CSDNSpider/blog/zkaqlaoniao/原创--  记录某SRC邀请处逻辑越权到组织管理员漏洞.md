# 原创
：  记录某SRC邀请处逻辑越权到组织管理员漏洞

# 记录某SRC邀请处逻辑越权到组织管理员漏洞

1.在挖掘某src漏洞时候信息收集的时候收集到某小程序 该小程序的主要功能是帮助购买此服务的公司管理项目和销售员工的<br/> 这里我们准备两个测试账号(A和B)<br/> 2.我们登录进去该小程序，按照正常步骤流程注册个公司账户对该小程序进行试用，新建个公司项目后登录进去，点击公司管理，得先去客户项目选项处新建个项目才能进行后续操作<br/>  

<br/> 3.新建完项目后 我们返回主页 点击我们 点击邀请成员操作<br/>  

<br/> 4.我们选择随意一个低于公司管理员的权限，例如这里

5.邀请一个招聘专员的权限 然后将邀请链接发送到测试账号B<br/>  

<br/> 6.然后切换到另外的测试账号B，点击邀请连接进去，然后点击加入组织的时候进行抓包<br/> 重点来啦！！！这里我们可以看到包中有个role_id参数 这里是对邀请成员进组织时的权限的，因为role_id可控，所有我们是否可以将其改成组织管理员的role_id将其由招聘专员提升成组织管理员权限呢<br/>  

<br/> 发包过去 返回success<br/>  

<br/> 返回A账号 进入该项目 可以看到成功通过邀请链接将低权限的邀请更改为项目管理员权限<br/>  

<br/> 且通过上面的报文可以看到公司id是可以进行爆破遍历操作的，我们也可以对id进行爆破加入其他人的公司

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
