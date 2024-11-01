# 原创
：  安全技能从0到1 | windows抓包微信小程序

# 安全技能从0到1 | windows抓包微信小程序

### 话不多说，直接先上个效果图：

新的版本哈：<br/>  

<br/> 抓包效果如下：

### 然后直接说我如何配置的：

##### 准备好三个工具：bp、fiddler、proxifier【也可以用其他的进行代理】

<br/> bp、proxifier在正式课件有，fiddler直接去官网下载即可。

##### 第一步：证书安装

抓包前必须要把证书搞好，要不然中间折腾的你受不了<br/> 1、Fiddler证书安装：

<br/> options设置打开；<br/> 这样照着勾起来：

<br/> 连接的监听端口设置一个未占用的；

然后网关手动代理配置，这里的代理就是burp的代理，和burp中option的代理地址端口记得一致；<br/>  

<br/> 然后生成下载证书：

<br/> 或者用浏览器访问127.0.0.1:fiddler监听端口

<br/> 安装证书：

<br/> 这里注意要这样选择！为什么？对于这个问题，可以参考如下文章https://www.wanganke.com/web/article/show/4511

<br/> 点击完成即可成功导入；<br/>  

<br/> 2、burp证书安装：<br/> 保姆级教程，一步一步跟着点即可：

<br/> 和上面的方式一样导入即可；

##### 第二步：挂上proxifier代理【或者你可以全局代理】

将流量走向配置为：微信|小程序—&gt;Fiddler—&gt;burp<br/> 1、代理服务器：<br/> 与burp一致<br/>  

<br/> 2、代理规则：<br/> 微信开个小程序后用任务管理器找到进程：

<br/> 找到文件所属目录后，在代理规则的应用程序里浏览选择它，动作记得选上配置的代理服务器，名称任意，然后确认即可。

### 然后就可以开始自由自在的抓包测试啦~

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
