# 原创
：  如何利用Python爬虫抓取某眼查网站中的q业信息？

# 如何利用Python爬虫抓取某眼查网站中的q业信息？

**部分数据来源：**ChatGPT 

#### 引言：

        最近在朋友圈看到了一个Python爬虫兼职的机会，但是由于一些原因我没有接到，于是我自己写了一个某眼查搜索结果爬取的Python脚本。下面将分享这个脚本的详细使用教程。

#### 背景

        某眼查是一家经营企业信用信息服务的公司，可以通过其网站查询公司信息、股权结构及主要人员信息。而该网站抵制爬虫行为，会经常进行反爬虫操作，对于一些比较敏感的信息需要登录后才能查看。所以我们需要通过编写爬虫程序来实现对企业信息的抓取。

#### 正文：

#### 一、准备工作

        在开始之前，你需要安装Python编程语言和一些Python库，如selenium、beautifulsoup等。如果你还没有安装这些库，可以通过以下命令安装：

```
pip install selenium
pip install beautifulsoup4
pip install urllib

```

另外，你还需要一个Chrome浏览器.

#### 二、获取Cookie信息

        在开始抓取之前，我们需要登录某眼查并获取Cookie信息。登录某眼查后，按下F12打开控制台，找到Network标签页，并刷新一下页面。然后在左侧菜单中选择任意一项请求，点击它，界面右侧会出现该请求的详细信息。
