# 原创
：  Python爬虫 | 使用Selenium和BeautifulSoup爬取xxx余票信息并保存到Excel文件、表格、图表

# Python爬虫 | 使用Selenium和BeautifulSoup爬取xxx余票信息并保存到Excel文件、表格、图表

## 前言

        12306是中国铁路客运唯一官方网站，是购买火车票的重要网上平台。本文主要介绍如何使用Python爬虫模块Selenium和BeautifulSoup，从12306上爬取火车票信息并保存到Excel文档中，方便大家查看和比较不同车次和座位类型的价格和余票情况。

### 准备工作

在开始之前，我们需要进行一些准备工作。

安装以下组件：

可以使用以下命令来安装上述组件：

```
pip install beautifulsoup4
pip install selenium

```

注意：由于需要使用Selenium模拟浏览器访问网站，因此需要下载前端驱动程序，根据浏览器版本选择相应的驱动程序。本文使用的是Chrome浏览器，驱动程序下载链接为：[http://npm.taobao.org/mirrors/chromedriver/。](http://npm.taobao.org/mirrors/chromedriver/%E3%80%82)

安装完成后，将下载好的驱动程序解压到任意位置，并将驱动程序所在文件夹添加到系统的PATH环境变量中。

### 爬取火车票信息

#### 设置请求参数

首先需要设置请求参数，包括出发城市、到达城市、出发日期等信息。在代码中，使用以下参数：
