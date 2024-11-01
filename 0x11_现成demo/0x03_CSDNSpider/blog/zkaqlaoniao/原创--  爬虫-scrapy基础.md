# 原创
：  爬虫/scrapy基础

# 爬虫/scrapy基础

> 
如果文章对你有帮助，欢迎关注、点赞、收藏一键三连支持以下哦！<br/> 想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步


**目录**

[0x01 安装和简介](#0x01%20%E5%AE%89%E8%A3%85%E5%92%8C%E7%AE%80%E4%BB%8B)

[0x02 文件作用](#0x02%20%E6%96%87%E4%BB%B6%E4%BD%9C%E7%94%A8)

[0x04 保存数据](#0x04%20%E4%BF%9D%E5%AD%98%E6%95%B0%E6%8D%AE)

---


## 0x01 安装和简介

---


<br/> Scrapy是适用于Python的一个快速、高层次的屏幕抓取和web抓取框架。<br/> 原理图：

<br/> 简单来说，先去spiders拿url，再转到引擎，再给其他的模块传来传去。

我自己是linux安装，windows安装很麻烦

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
pip install lxml
sudo apt-get install python-dev python-pip libxml2-dev zlib1g-dev libffi-dev libssl-dev
pip install Scrapy
apt-get install python3-scrapy
```

<br/> 这几条都可以试试，毕竟安装这个东西很玄学。<br/> 输入scrapy后出现这个就是下载好了:

```
└─# scrapy
Scrapy 2.7.1 - no active project
 
Usage:
scrapy &lt;command&gt; [options] [args]
 
Available commands:
bench Run quick benchmark test
commands
fetch Fetch a URL using the Scrapy downloader
genspider Generate new spider using pre-defined templates
runspider Run a self-contained spider (without creating a project)
settings Get settings values
shell Interactive scraping console
startproject Create new project
version Print Scrapy version
view Open URL in browser, as seen by Scrapy
 
[ more ] More commands available when run from project directory
 
Use "scrapy &lt;command&gt; -h" to see more info about a command
```

## 0x02 文件作用

<br/> 创建项目：

> 
scrapy startproject &lt;项目名字&gt;


<br/> 框架结构：

> 
tree &lt;项目名字&gt;
<br/> myspider<br/> ├── __init__.py<br/> ├── items.py<br/> ├── middlewares.py<br/> ├── pipelines.py --&gt;管道 保存数据<br/> ├── settings.py --&gt; 设置文件 ua 启动管道<br/> └── spiders --&gt;自定义<br/> └── __init__.py


<br/> 先来看看scrapy.cfg<br/> settings是详细设置<br/> deploy部署 应用于项目部署

items.py 模版类，定义数据存储模型

<br/> middlewsres 中间件模块，一般不用编写。<img alt="" height="504" src="https://img-blog.csdnimg.cn/img_convert/277fbde86c4db5a0ad5d84e09342532a.png" width="641"/>

<br/> pipelines 数据清洗或保存<img alt="" height="515" src="https://img-blog.csdnimg.cn/img_convert/a4d9fc04072f2fc597c146699cb10576.png" width="623"/>

0x03 创建爬虫<br/> 在项目目录下执行：

> 
cd example<br/> scrapy genspider example example.com


<br/> 新的框架结构

<img alt="" height="507" src="https://img-blog.csdnimg.cn/img_convert/a43d077c4efb2c15e2a2f344e2157130.png" width="653"/><br/> 首先继承了一个类，name是爬虫的名字，allowed_domain是允许的域名，意思是只爬取这个域名的信息，start_urs起始url是bbs.zkaq.cn。

parse方法中response是请求bbs对应的响应。<br/> 运行爬虫：

> 
scrapy crawl zkaq --nolog


<br/> —nolog:去除日志，只得到结果。<br/> 我之前有一篇爬取所有帖子名字的文章，这里直接把当时的xpath放到parse方法里。<img alt="" height="504" src="https://img-blog.csdnimg.cn/img_convert/a7aa033a3c6fa7bd05ac2f5384712f6d.png" width="656"/>

<br/> 这里用的是response的xpath方法，返回一个列表，操作和列表一样，但是有两个别的方法：

> 
extarct(): 返回一个带有字符串的列表<br/> extarct_first()：返回列表的第一个字符串，没有时返回none。


<br/> 用上面的指令运行：<img alt="" height="248" src="https://img-blog.csdnimg.cn/img_convert/d511fba44f9adac3b3bbe1031a0a04ad.png" width="629"/>

<br/> 一点vim知识（我不太会linux）：

> 
i 进入编辑模式<br/> ESC 退出模式<br/> :wq 保存并退出


## <br/> 0x04 保存数据

---


<br/> 利用管道(pipelines)对数据进行处理和保存。
1. 定义一个管道类1. 重写process_item方法1. process_item处理完后返回给引擎 实际上是，spiders给引擎，引擎给pipeline1.   4.在settings.py中，把管道注释删除,这一步叫做启动管道。
管道执行顺序： 

> 
ITEM_PIPELINES = {<br/> 'myspider.pipelines.MySpiderPipeline': 299,<br/> 'myspider.pipelines.MySpiderPipeline': 300,
<br/> }


<br/> 则299先执行。<br/> 在zkaq.py中，使用yield把node_list返回给引擎<img alt="" height="477" src="https://img-blog.csdnimg.cn/img_convert/dbd011858e3f304f8a5c0e9de5276136.png" width="630"/>

<br/> 最后运行爬虫<img alt="" height="503" src="https://img-blog.csdnimg.cn/img_convert/9d65959fe181c04d1c85aae7628c1756.png" width="655"/>

还没看够？下篇继续<br/> https://docs.qq.com/doc/DYlBlQ2xhaFBmamtq
