# 原创
：  Python爬虫初学者也能学会的最新电影榜单提取方法

# Python爬虫初学者也能学会的最新电影榜单提取方法

**部分数据来源：**ChatGPT

#### 引言

        如果你是一个电影迷，想要了解最新的电影资源，那么这篇文章就是为你准备的。我们将介绍如何用Python获取最新电影榜单，并列出其中的电影名称。

首先，让我们看看我们需要的库：requests和BeautifulSoup。

Requests是一个Python第三方库，它可以用于发送HTTP请求和获取响应。BeautifulSoup可以解析HTML和XML文档，可以提取出想要的信息，如标签和属性。

接下来，我们需要知道从哪个网站获取最新电影榜单。我们将使用“美剧天堂”网站提供的榜单，该网站是一个很受欢迎的电影资源共享网站。

#### 1、我们需要定位榜单的URL地址。

```
url = 'https://www.meijutt.tv/new100.html'

```

#### 2、发送请求并获取响应内容。

```
response = requests.get(url)
html = response.content.decode('gbk')

```

我们需要使用BeautifulSoup来解析HTML文档，并定位我们所需要的信息。在这种情况下，我们需要获取电影名称。我们将使用 ‘ul’ 和 ‘li’ 标签来获取电影列表，如下所示。

```
soup = BeautifulSoup(html, 'html.parser')
movies = soup.find('ul', attrs={"class": "top-list fn-clear
```
