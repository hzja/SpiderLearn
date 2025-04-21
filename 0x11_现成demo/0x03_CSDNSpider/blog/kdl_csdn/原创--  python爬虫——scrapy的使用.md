# 原创
：  python爬虫——scrapy的使用

# python爬虫——scrapy的使用

本文中的知识点：

---


### 安装scrapy

> 
由于小哥的系统是win7，所以以下的演示是基于windows系统。linux系统的话，其实命令都一样的，没啥差，windows与linux都可以用。


```
pip install scrapy

```

安装好后，先看下scrapy是否安装上了，确认下，我的是Scrapy 1.8.0

```
scrapy version

```

好了，安装很简单。用scrapy创建个新项目吧。命令行下输入，这里**注意**，命令会在当前目录下创建ts项目。

---


### 创建新项目

```
# 新建一个名为ts的scrapy的项目
scrapy startproject ts 

```

我是在桌面下创建的ts目录，创建成功后给的提示截图如下。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/ccc3e6045c0382004a1e774e32fd151c.png"/>

##### 分析目录文件

让我们去目录下看看都有些什么，有个scrapy.cfg配置文件，ts目录。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/2bd71f66f890743a45869662371a90ae.png"/><br/> 在进入ts目录，看下有些什么。嗯~~~ 主菜来了，这里就是我们要写的内容了。

先不用管这么细，我们先跑起来。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c1c116cf89acdd216ea23647713d1bd1.png"/>

---


### 代码样例

抓个百度首页试试吧。<br/> 进入spiders目录里，创建个baidu的爬虫，并且限制抓取域名的范围。**注意**要在spiders的目录下输入以下命令

```
scrapy genspider baidu "baidu.com"

```

<img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c538f243f8c3fbc58d94b238f0c67051.png"/><br/> 看到命令已经帮我们自动创建了爬虫代码，打开文件看下。<br/> 看下这里的代码，先导入scrapy，定义了一个BaiduSpider类，必须要继承scrapy.Spider。这里**注意**，里面有3个必须的属性(name，allowed_domains，start_urls)。

好的，既然都OK了，那我们去运行下，看看会发生什么。<br/> 命令行下输入，**注意**这里的baidu就是爬虫的name属性。

```
scrapy crawl baidu

```

嘎嘎嘎，，，一大堆信息，看的是不是有点懵，说实话，我也是。这是正常信息，已经跑起来了。这些参数，大家随意看一看吧，我先不解释了。。。手动滑稽~~~哈哈哈，其实先不用看，一会我们在讲。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/18f35441523491e0e2ca90aebeeb8468.png"/>

#### 代码改造下，按照我们的预期来

还记得刚才的parse函数么，不过命令创建的是啥事都没干。自己定义下，让它做点事，也好知道代码是按照我们的预期去跑的。

```
# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # 打印下response返回的状态码
        print(response.status)

```

在来运行下，还记得刚才的运行命令吗？不记得了？。。。行，我在说一遍，

```
scrapy crawl baidu

```

好的，让我们看看会给什么信息。嗯，，，有点问题，没有打印response的状态码，看下日志，这里说的是爬虫碰到了robots.txt，给Forbidden（禁止）了。MD，百度竟然不给我爬，百度自己的spider都在爬其他网站的，，，<br/> 这里得解释下为什么禁止了，这其实就是个爬虫的哲学问题了，盗亦有道的道理，相信大家都听说过，爬虫也是，爬亦有道。robots.txt也就是[robots协议](https://baike.baidu.com/item/robots%E5%8D%8F%E8%AE%AE/2483797?fromtitle=robots.txt&amp;fromid=9518761&amp;fr=aladdin)，这个文件会告诉爬虫，哪些能爬，哪些不能爬，爬虫要遵守这个规则。毕竟是别人的网站嘛，，，<br/> ****本文以教学为主，旨在教大家使用scrapy框架，合理使用爬虫，遵守互联网规则是每一位互联网人的责任。****<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/785eb949cbc6c4dfab0241588a6fdf80.png"/><br/> 好的，问题该怎么解决？其实robots.txt也是可以解决的。这个时候settings.py就派上用场了。到我们之前的目录下，找到settings.py文件。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/b7c90933e33801725b81fd19c6eab62d.png"/><br/> 打开看下，注意到ROBOTSTXT_OBEY = True ，这个就是遵守robots协议。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/9c45632f477f3d902968d4f43349fe3a.png"/>

**改成False，不遵守robots协议** ~~~嘿嘿嘿，别笑，，，我只是教大家学scrapy框架而已<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/10188ebf08939c94e6b9d7ff8b4e7c41.png"/><br/> 再来运行下。看到这里就已经打印出来了，返回200，成功抓取百度。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c4b021b40ff61ed4153b41789baa8481.png"/>

##### 再来改造下

改造下parse函数，把抓取的数据保存到一个文件里。毕竟之前的定义的parse动作是打印各种信息，都在看日志，脑袋都大了，这次直接点，看文件好吧。

```
# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # 定义文件名 baidu.html
        filename = 'baidu.html'
        with open(filename, 'wb') as f:
            f.write(response.body) #文件写入response的body信息

```

好的，运行下试试。（PS：命令没忘吧，忘了的往上翻翻），这里**注意我是在spiders目录下运行的**，baidu.html文件也会保存在当前目录下。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/e88c12192ee3c7a047dbf56aebd3d946.png"/><br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/4d66917ca02571b755714781bd70122f.png"/><br/> 看到了吧，文件出来了，直接双击打开看看，嗯，是百度首页。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c11dc008b8c4cb4a5d5dde9389ecf499.png"/>

### 使用代理

准备工作，找个可靠的代理IP，剩下的跟着我的步骤走。

##### 修改中间件配置

这里就需要用到中间件了，找到文件middleware.py，打开看看文件。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/40e785408502ffc66177d4debd1e8ba8.png"/><br/> 这就是项目的中间件配置了。参数挺多，不过设置代理，我们只需要关注几个参数即可。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/71d2e35dd952abad16301b0a08cee82b.png"/><br/> 找到TsDownloaderMiddleware，这个类就是我们的项目下载器的中间件，我们的代理配置主要写在process_request函数里。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/a53dd1efbb2fb8a6e95f20c4534c1651.png"/><br/> 改成

```
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 代理IP由快代理赞助
        proxy = '112.192.158.65:20823'
        # 做了个处理,http与https
        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://%s" % proxy
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://%s" % proxy
        return None

```

修改后如图<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/91c3ceb9399727484fcd3ed1d59e5b1a.png"/>

#### settings.py文件也需要修改，需要修改两处：

1、header参数，记住爬虫要模拟用户的真实请求。找到USER_AGENT参数，改成自己浏览器的ua，不知道怎么找ua的同学可以看我前面的一篇教程（[点击跳转](https://blog.csdn.net/kdl_csdn/article/details/103962098)）中有提到。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/4900dd8a87832e4415bdfec308b71f0f.png"/><br/> 修改后<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/23d07963a7d1556e349900565d23aebe.png"/><br/> 2、找到DOWNLOADER_MIDDLEWARES参数，Ctrl + f搜索，注释掉这个配置保存，启动配置<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/3d01172ad88a6f5fbe2e0bebf04325f8.png"/><br/> 注释后，修改后<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/bcd35207f72e4d5589834d2f36af6d82.png"/><br/> 好的，在改下我们的爬虫代码，spiders目录下的baidu.py文件。因为我们用了代理，所以去访问下查IP的网站，看看是否用上代理了。

```
# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?ie=UTF-8&amp;wd=ip']

    def parse(self, response):
        filename = 'baidu.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

```

<img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/b1cf6eab503fa4e91d697315501bac28.png"/><br/> 好的，现在在spiders目录下运行下，看看有没有文件出来。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/da7d847f1f7f2b09d5464c2ff5b504e0.png"/><br/> 有了，打开文件看下。对吧，这里查到的IP也是我们在代码样例中的IP。说明成功用上代理了。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c08f0e5759e5164453c82e9d3d1305dc.png"/><br/> scrapy使用代理总结下，需要修改及注意那些点。

嗯，主要注意这两个点。<br/> 其实还有一种设置代理的方法，我就先不写了，交给大家去研究吧。

### 进阶学习：
