# 原创
：  记一次EDU证书站

# 记一次EDU证书站

> 
如果文章对你有帮助，欢迎关注、点赞、收藏一键三连支持以下哦！<br/> 想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


**目录**

**目录**

[1.前言：](#1.%E5%89%8D%E8%A8%80%EF%BC%9A)

[2.信息搜集](#2.%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86)

[3.漏洞挖掘](#3.%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)

---


### 1.前言：

挖了一段时间EDU老破小的站，也该拿证书站下手了。下手的第一个目标，那必然是漏洞排行榜第一的某交大！！！

### 2.信息搜集

想快速挖到漏洞，必须信息搜集全面。如果信息搜集不到位不全面，后面挖洞也很困难，除非0day在手，哈，那你就是大佬！

信息搜集三要素：子域名、目录、端口号

这里就先用子域名搜集一下，除了老掉牙的Oneforall，这里再推荐两个在线搜集的工具，也是特别不错的，大家可以尝试一下。
1.  https://securitytrails.com 国外网站需要注册但是比较全 
<br/> 2.http://z.zcjun.com/ 国内站无需注册

这里利用国外的网站搜集到的子域名保存好了，然后利用另外一个神器httpx去检测状态，还可以指定目录探测。

```
httpx 语句：httpx.exe -path （指定路径）-l ip地址.txt -title -tech-detect -status-code -threads 50 -web-server -mc 200 （状态码）
```

这里搜集到不少4级域名，3级域名感觉都被大佬们测烂了。所以还是去找找这种相对较少人找到的站去测测。

接下来就是查找目录了，这边用了js神器，jjjjjjjj 去查找目录，可以查看到未授权的接口直接访问即可。<br/> https://github.com/ttstormxx/jjjjjjjjjjjjjs

### 3.漏洞挖掘

通过之前的信息搜集，找到一个https://xxx.xxx.xxx.edu.cn/ums/user/index.html#/login<br/> 这里开始网站是校外登陆的点<br/>  

<br/> 然后点击注册，注册成功之后发现需要审核。无语！！！<br/>  

<br/> 不过这里有个改密码的点。有功能咱就测！这显然是个修改密码的接口，然后点击并尝试修改post传参，发现可以越权任意修改其他用户密码。

<br/> 只需要修改用户名称即可。可以注册两个用户，互相修改尝试。

不过之前找到一个未授权的接口，通过js神器jjjjj搜找到https://xxx.xxx.xxx.edu.cn/ums/ums/userlist （post传参）<br/> 通过未授权访问userlist得到其他真实用户名，然后修改回显修改成功，如果用户没有回显失败。

最后申请高危成功，证书到手！

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

**没看够~？欢迎关注！**

[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
