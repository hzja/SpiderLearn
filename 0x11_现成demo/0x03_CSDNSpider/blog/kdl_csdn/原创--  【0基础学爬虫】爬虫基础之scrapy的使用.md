# 原创
：  【0基础学爬虫】爬虫基础之scrapy的使用

# 【0基础学爬虫】爬虫基础之scrapy的使用

## 【0基础学爬虫】爬虫基础之scrapy的使用

大数据时代，各行各业对数据采集的需求日益增多，网络爬虫的运用也更为广泛，越来越多的人开始学习网络爬虫这项技术，K哥爬虫此前已经推出不少爬虫进阶、逆向相关文章，为实现从易到难全方位覆盖，特设【0基础学爬虫】专栏，帮助小白快速入门爬虫，本期为自动化工具 Selenium 的使用。

### scrapy简介

Scrapy 是一个用于爬取网站并提取结构化数据的强大且灵活的开源框架。它提供了简单易用的工具和组件，使开发者能够定义爬虫、调度请求、处理响应并存储提取的数据。Scrapy 具有高效的异步处理能力，支持分布式爬取，通过其中间件和扩展机制可以方便地定制和扩展功能，广泛应用于数据挖掘、信息聚合和自动化测试等领域。

### scrapy 工作流程

```
1、启动爬虫：Scrapy 启动并激活爬虫，从初始URL开始爬取。
2、调度请求：爬虫生成初始请求，并将其发送给调度器。
3、下载页面：调度器将请求发送给下载器，下载器从互联网获取页面。
4、处理响应：下载器将响应返回给引擎，传递给爬虫。
5、提取数据：爬虫从响应中提取数据（items）和更多的URL（新的请求）。
6、处理数据：提取的数据通过项目管道进行处理，清洗并存储。
7、继续爬取：新的请求被调度器处理，继续下载和提取数据，直到所有请求处理完毕。

```

### scrapy 每个模块的具体作用

### 安装scrapy

```
pip install scrapy

```

安装成功后，直接在命令终端输入 scrapy ，输出内容如下：

### 新建scrapy项目

使用 scrapy startproject + 项目名 创建新项目。

这里我们使用 `scrapy startproject scrapy_demo` 创建项目示例:

然后通过下面命令创建我们的爬虫模板，这里就按照scrapy 给出的实例创建:

```
cd scrapy_demo
scrapy genspider example example.com

```

使用pycharm 打开我们的项目，项目格式如下：

各个文件夹的含义：

```
spiders：存放爬虫文件
items：定义爬取的数据结构
middlewares：定义下载中间件和爬虫中间件。中间件是处理请求和响应的钩子，可以修改请求、响应、异常等
pipelines：定义管道，用于处理爬虫提取的数据，例如数据清洗、验证和存储等操作。
settings：定义了项目的基本配置

```

### 使用scrapy

这里以我们熟悉的某瓣为例来说明 `scrapy` 的用法。

修改 example.py 文件：

```
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    # allowed_domains = ["example.com"]   # 允许爬取的网站范围，可以不要
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)

```

在终端输入 `scrapy crawl example` 运行结果如下：

输出了很多信息，包含版本号、插件、启用的中间件等信息。

```
Versions:版本信息,包括scrapy和其它库的版本信息
Overridden settings： 重写的相关配置
Enabled downloader middlewares：开启的下载器中间件
Enabled spider middlewares：开启的爬虫中间件
Enabled item pipelines：开启的管道
Telnet Password：Telnet 平台密码（Scrapy附带一个内置的telnet控制台，用于检查和控制Scrapy运行过程）
Enabled extensions ：开启的拓展功能
Dumping Scrapy stats：所以的信息汇总

```

我们重点看这里：

可以发现，我们返回了403状态码，原因是因为我们少了请求头和有robots协议。

在 setting.py 增加请求头、修改 robots 协议：

```
# Obey robots.txt rules
ROBOTSTXT_OBEY = False   # 这里改成False，表示不遵守robots协议

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}  # 然后把这个放开，这个表示该项目的默认请求头

```

运行之后，可以发现能正常返回 html 页面数据。

#### scrapy 运行项目的两种方式

上面我们是通过终端运行的，下面我们使用 python 运行。

修改 example.py 文件代码：

```
import scrapy
from scrapy import cmdline


class ExampleSpider(scrapy.Spider):
    name = "example"
    # allowed_domains = ["example.com"]   # 允许爬取的网站范围，可以不要
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl example".split())
    # cmdline.execute("scrapy crawl example --nolog".split()) 不输出提示信息


```

如果不想输出与爬虫无关的信息，可以在后面加上 --nolog 命令，这样就不会打印提示信息了。

#### 数据翻页抓取

scrapy实现翻页请求

我们可以直接利用scrapy 内置的数据解析方法对数据进行抓取：

代码如下：

```
import scrapy
from scrapy import cmdline


class ExampleSpider(scrapy.Spider):
    name = "example"
    # allowed_domains = ["example.com"]   # 允许爬取的网站范围，可以不要
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)
        ol_list = response.xpath('//ol[@class="grid_view"]/li')
        for ol in ol_list:
            item = {
   }
            # 利用scrapy封装好的xpath选择器定位元素，并通过extract()或extract_first()来获取结果
            item['title'] = ol.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['rating'] = ol.xpath('.//div[@class="bd"]/div/span[2]/text()').extract_first(&lt;/
```
