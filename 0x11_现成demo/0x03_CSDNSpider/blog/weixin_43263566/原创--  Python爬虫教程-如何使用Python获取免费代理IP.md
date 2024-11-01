# 原创
：  Python爬虫教程：如何使用Python获取免费代理IP

# Python爬虫教程：如何使用Python获取免费代理IP

**部分数据来源：**ChatGPT

#### 引言

        在爬取数据时，为了避免被反爬机制封锁，我们需要使用代理IP来进行隐蔽访问。有些网站提供免费的代理IP，我们可以使用Python来自动化获取这些代理IP，并进行验证筛选出可用的代理IP。

#### 准备工作

        在开始之前，需要安装 `requests` 和 `beautifulsoup4` 两个 Python 模块，可以使用以下命令进行安装：

```
pip install requests
pip install beautifulsoup4

```

#### 获取代理 IP 地址

        在使用代理 IP 地址之前，需要先获取一些有效的代理 IP 地址。可以通过以下代码获取一个可用的代理 IP 地址列表：

```
import requests
from bs4 import BeautifulSoup

# 设置请求头部信息，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
}

# 获取代理IP列表并格式化代理IP地址
def get_proxy_list():
    url = "https://www.proxy-list.download/HTTP"
    try:
        resp = requests.get(url, headers=headers, timeout=10) #发送请求，并
```
