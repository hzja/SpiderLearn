# 原创
：  SRC实战 | edu某学院-存储型xss漏洞小思路

# SRC实战 | edu某学院-存储型xss漏洞小思路

前话：XSS漏洞并不多见，而且反射型基本都不会收【危害太低】，所以要找到存储型xss，见框就插的方法没有用了【除非运气特别好】<br/> 这时候就得改变一下思路，找一些隐秘的传参有回显的点；

### 漏洞复现：

<br/> 注册登录后，一个平平无奇的提交工单接口，所有提交信息已经见框就插，毫无作用QAQ，于是在放弃测试xss后，对上传图片进行测试：

<br/> 然后测了半天发现是个白名单，准备放弃的时候：

<br/> 突然发现提交的数据包有一条是对图片路径的传参<br/> 加上我在测试的时候有尝试修改相应包上传php文件：

<br/> 发现虽然可以提交，但是文件会被删除<br/> 但是文件路径依然回显：

<br/> 所以我马上感觉这个文件路径的传参点可能xss有戏，闭合src=” ＋弹窗1：<br/>  

<br/> 效果如下：

<br/> 一个存储xss漏洞就找到惹

##### 漏洞修复建议：

对图片路径得传参进行实体化编码和多一些判断

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
