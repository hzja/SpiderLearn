# 原创
：  从接口发现到文件上传getshell

# 从接口发现到文件上传getshell

0x01 信息收集<br/> 通过fofa，子域名收集等相关工具搜索域名<br/> 定位到站点：htps://xx..edu.cn/x/xx/

0x02 寻找接口<br/> 通过f12寻找相关的js，发现有其他的页面

0x03 拼接路径<br/> https://xx.xx.edu.cn/xx/xx/repairResgister<br/> 之后未授权获取到注册用户的页面中，发现有一个上传图片进行上传

由于站点已修复，简单阐述一下<br/> html，jpg，txt，png等相关后缀可以进行上传，但进行jsp等相关的后缀并不能成功。如果是白名单，返回的页面只会显示：只能上传jpg，png等相关图片的后缀，但他并没有显示，所以初步判断这里是黑名单，之后进行上传图片马，还有通过空格，.，%00截断，来进行绕过。

0x04 权限<br/> 成功getshell

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
