# 原创
：  Scrapy使用隧道代理403问题解决方案

# Scrapy使用隧道代理403问题解决方案

### scrapy使用隧道代理不换IP

**客户现象**<br/> [快代理](https://www.kuaidaili.com/)隧道代理客户反馈使用隧道代理没有换IP，原因是使用了隧道代理但是目标网站还是403，跳验证码屏蔽等等，用户推断隧道没有更换代理IP

**反爬研究**<br/> 询问用户访问的网站是https://book.douban.com/，豆瓣读书<br/> https://book.douban.com/subject/35313246/?icn=index-latestbook-subject，35313246应该为book的id，需要访问那本书直接更换id即可

自己编写一个scrapy项目，不使用代理访问200个图书页面，发现前期响应状态为200，即可以爬取到页面，不一会就会出现大量的403状态码，即被防爬了

此时点开任意一个book页面，跳转https://sec.douban.com/b?r=https%3A%2F%2Fbook.douban.com%2Fsubject%2F35315077%2F%3Ficn%3Dindex-latestbook-subject，显示IP被封，需要登陆豆瓣，可以推断出豆瓣是以IP做爬虫监控的

同时我在用户的请求记录中发现了大量sec.douban.com访问记录，可以推断出用户在使用代理的过程中，大量请求会被ban掉<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/21be810d8ef1e1f8c83d09f6f47611e2.png#pic_center"/><br/> 于是在scrapy中使用隧道代理，发现前期同样的请求都是200，可以拉下来页面，在爬取了一会后就会出现大量的302，403状态码，基本复现了用户场景<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/16f7d608bf47af7a6c244865a3800dfe.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c4c94bab3dd41e04fe4e23d351d13f8f.png#pic_center"/><br/> 点开跳转的页面https://www.douban.com/misc/sorry?original-url=https%3A%2F%2Fbook.douban.com%2Fsubject%2F35313579%2F%3Ficn%3Dindex-latestbook-subject<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/905a39191aeab363c20e27b731ee81be.png#pic_center"/><br/> 发现同样是反爬的页面，所以问题就来了，为什么使用的隧道代理依然会被反爬？

隧道代理自身问题研究<br/> 首先根据用户的猜测，我怀疑有可能是IP重复率问题，即某一段时间集中转发在一个IP上，导致重复率很大，这一点测试得出

对于基础规格1s5次的隧道而言，1分钟内访问隧道的次数为300次，查询一分钟内访问次数在300次的隧道访问记录查看得出规格为1s5次，动态版的隧道在一分钟内访问了298次，其中275次都为不重复的代理IP，及重复率为7%-8%左右，可以说在一分钟内都会分配给不重复的IP

这时有人可能会说五分钟呢？，10分钟内呢？不过我写的scrapy项目中200个请求在一分钟内早已经跑完了，所以采用1分钟是有参考意义的

既然隧道代理每次都是更换了代理IP的，并且重复率完全达不到目标网站触发防爬跳转验证的程度，所以排除隧道本身问题

**请求客户端框架研究**<br/> 首先解析出隧道域名的IP地址

利用wireshark进行抓包 ip.addr 的数据包

继续挂上隧道代理运行请求200次，查看数据包，查看所有的http数据包<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/e7cb159886288afef14ee8ed8ff10a4a.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/831892d160cf63c705acd43a73da45dc.png#pic_center"/>

发现发送了起码200个，建立的连接只有是十个左右，200多个请求都只走了十几个连接，导致运行过程中会有403 302跳转登陆等等

之前已经知道了加上**Connection: close**头就就可以，实际测试确实是每个请求都会建立连接，为什么加close就可以了呢？

Scrapy 是一套基于基于Twisted的异步处理框架，通过查看Twisted源码可以看到

/twisted/web/_newclient.py中

实现的http1.1协议

class HTTP11ClientProtocol中的 _finishResponse_WAITING方法<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/49e975fbec2b36f9a0287cc92d80e541.png#pic_center"/>

如果在connection 显示的指定为close，在结束response后会giveup，当不添加Connection: close这个header是，则默认为keep-alive,走resumeProducing()会将连接给请求的生产者<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/0a8c1a84182f287bbf319cd7400930c3.png#pic_center"/>

通过debug也认证了之前的猜想<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/8031a80d49516e3c60d806c6a41beb5c.png#pic_center"/>

CSDN上有一篇博客记录了这个问题 https://blog.csdn.net/bf96163/article/details/111571803

```
request.headers['Proxy-Connection'] = "close" request.headers["Connection"] = "close"

```

博客中提到需要加这两个header，其实不然，通过看源码发现只需要**request.headers[‘Connection’] = “close”** 就可以了

**总结**<br/> 使用隧道代理要添加header Connection: close （[代码样例](https://www.kuaidaili.com/doc/dev/sdk_tps_http/#proxy_python-scrapy)已经发布）<br/> 反爬的可能的原因有很多，需要具体问题具体分析!

获取更多好文章，可以关注~<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/85046f254b1df775516198a12d339931.jpeg#pic_center"/>
