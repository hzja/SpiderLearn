# 原创
：  征战EDU证书站

# 征战EDU证书站

### 1.前言：

挖了一段时间EDU老破小的站，也该拿证书站下手了。下手的第一个目标，那必然是漏洞排行榜第一的某交大！！！

### 2.信息搜集

想快速挖到漏洞，必须信息搜集全面。如果信息搜集不到位不全面，后面挖洞也很困难，除非0day在手，哈，那你就是大佬！

信息搜集三要素：子域名、目录、端口号

这里就先用子域名搜集一下，除了老掉牙的Oneforall，这里再推荐两个在线搜集的工具，也是特别不错的，大家可以尝试一下。
1.  https://securitytrails.com 国外网站需要注册但是比较全 
<br/> 2.http://z.zcjun.com/ 国内站无需注册

这里利用国外的网站搜集到的子域名保存好了，然后利用另外一个神器httpx去检测状态，还可以指定目录探测。<br/>`httpx 语句：httpx.exe -path （指定路径）-l ip地址.txt -title -tech-detect -status-code -threads 50 -web-server -mc 200 （状态码）`

这里搜集到不少4级域名，3级域名感觉都被大佬们测烂了。所以还是去找找这种相对较少人找到的站去测测。

接下来就是查找目录了，这边用了js神器，jjjjjjjj 去查找目录，可以查看到未授权的接口直接访问即可。<br/> https://github.com/ttstormxx/jjjjjjjjjjjjjs

### 3.漏洞挖掘

通过之前的信息搜集，找到一个https://xxx.xxx.xxx.edu.cn/ums/user/index.html#/login<br/> 这里开始网站是校外登陆的点<br/>  

<br/> 然后点击注册，注册成功之后发现需要审核。无语！！！<br/>  

<br/> 不过这里有个改密码的点。有功能咱就测！这显然是个修改密码的接口，然后点击并尝试修改post传参，发现可以越权任意修改其他用户密码。

<br/> 只需要修改用户名称即可。可以注册两个用户，互相修改尝试。

不过之前找到一个未授权的接口，通过js神器jjjjj搜找到https://xxx.xxx.xxx.edu.cn/ums/ums/userlist （post传参）<br/> 通过未授权访问userlist得到其他真实用户名，然后修改回显修改成功，如果用户没有回显失败。

最后申请高危成功，证书到手！

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
