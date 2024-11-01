# 原创
：  使用 Python 简单地实现一个网站视频播放地址查询工具

# 使用 Python 简单地实现一个网站视频播放地址查询工具

#### ** 部分数据来源：**ChatGPT

#### 一、编程思路

1. 明确需求：编写一个Python脚本，能够在目标网站上搜索指定的视频，并从中选择一个分类，列出该分类下的所有视频播放地址，并通过Selenium库抓取视频播放地址。
1. 获取目标网站信息：我们需要了解目标网站的网站结构，包括搜索页面和视频页面的HTML结构、搜索结果和视频分类的命名规则、视频播放地址的获取方式等。
1. 确定实现方式：我们可以使用requests库发起HTTP请求，通过beautifulsoup库解析HTML响应，获取到搜索结果和视频分类，再通过Selenium库模拟浏览器行为，打开目标视频的播放页面，并抓取视频播放地址。

#### 二、脚本使用教程

1. 安装必要的依赖库：requests、beautifulsoup、Selenium、urllib
1. 运行脚本：打开Python环境，执行脚本，输入指定的搜索关键词。
1. 选择分类：根据列出分类的列表，输入您选择查看的视频类别。
1. 获取播放地址：根据列出的视频播放地址列表，输入您要查看的视频播放地址的序号。
1. 获得视频播放地址：输出视频播放地址。

**完整代码： **

plyy_spider.py

```
# 导入所需的库
import requests  # 发送 HTTP 请求
from bs4 import BeautifulSoup  # 对 HTML 页面进行解析
from selenium import webdriver  # 使用 Selenium 自动化浏览器
imp
```
