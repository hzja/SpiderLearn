# 转载
：  python爬虫0基础教程：关于爬取网页图片

# python爬虫0基础教程：关于爬取网页图片

在现在这个信息爆炸的时代，要想高效的获取数据，爬虫是非常好用的。而用python做爬虫也十分简单方便，下面通过一个简单的小爬虫程序来看一看写爬虫的基本过程：

## 准备工作

## <br/> 语言：python

IDE：pycharm

首先是要用到的库，因为是刚入门最简单的程序，我们主要就用到下面这两：

```
import requests //用于请求网页
import re  //正则表达式，用于解析筛选网页中的信息
```

<br/> 其中re是python自带的，requests库需要我们自己安装，在命令行中输入pip install requests即可。

然后随便找一个网站，注意不要尝试爬取隐私敏感信息，这里找了个表情包网站：

注：此处表情包网站中的内容本来就可以免费下载，所以爬虫只是简化了我们一个个点的流程，注意不能去爬取付费资源。<img alt="" height="863" src="https://img-blog.csdnimg.cn/956eb60179ec4c18aaab89536abd2e41.png" width="1200"/>

我们要做的就是通过爬虫把这些表情包下载到我们电脑里。

## 编写爬虫程序

<br/> 首先肯定要通过python访问这个网站，代码如下：

```
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
response = requests.get('https://qq.yh31.com/zjbq/',headers=headers)  //请求网页
```

<br/> 其中之所以要加headers这一段是因为有些网页会识别到你是通过python请求的然后把你拒绝，所以我们要换个正常的请求头。可以随便找一个或者f12从网络信息里复制一个。<img alt="" height="606" src="https://img-blog.csdnimg.cn/8990cfbec2734f5dba0b15da3494a9c0.png" width="1200"/>

然后我们要找到我们要爬取的图片在网页代码里的位置，f12查看源代码，找到表情包如下：

 然后建立匹配规则，用正则表达式把中间那串替换掉，最简单的就是.*?

```
t = '&lt;img src="(.*?)" alt="(.*?)" width="160" height="120"&gt;'
```

<br/>  像这样。

然后就可以调用re库里的findall方法把相关内容爬下来了：

```
result = re.findall(t, response.text)
```

<br/> 返回的内容是由字符串组成的列表，最后我们经由爬到的地址通过python语句把图片下下来保存到文件夹里就行了。

程序代码

```
import requests
import re
import os
 
image = '表情包'
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
response = requests.get('https://qq.yh31.com/zjbq/',headers=headers)
response.encoding = 'GBK'
response.encoding = 'utf-8'
print(response.request.headers)
print(response.status_code)
t = '&lt;img src="(.*?)" alt="(.*?)" width="160" height="120"&gt;'
result = re.findall(t, response.text)
for img in result:
    print(img)
    res = requests.get(img[0])
    print(res.status_code)
    s = img[0].split('.')[-1]  #截取图片后缀，得到表情包格式，如jpg ，gif
    with open(image + '/' + img[1] + '.' + s, mode='wb') as file:
        file.write(res.content)
```

<br/> 最后结果就是这个样子：

> 
<br/> 原文链接：https://blog.csdn.net/qq_46145027/article/details/123969044


---


 

还没看够？下篇继续

** **<img alt="" height="768" src="https://img-blog.csdnimg.cn/5be9cac530424c06ab153b63ed2ce91d.png" width="1024"/>

 

#### 渗透工具

#### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

#### 视频

#### 基础到进阶

#### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
