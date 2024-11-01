# 原创
：  37-1 Python 的 requests 库发送 GET 请求

# 37-1 Python 的 requests 库发送 GET 请求

靶场环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187) 

#### **一、requests库介绍：**

        requests库是用 Python 语言编写的第三方库，用于访问网络资源。它基于 urllib，但相比 urllib 更加简单、方便和易于使用。通过 requests 库，可以实现自动爬取 HTML 网页页面，并模拟人类访问服务器以自动提交网络请求。

#### **二、Requests库的安装：**

1.  使用以下命令查看已安装的 Python 包列表： <pre>`pip list`</pre> 
1.  若要卸载已安装的 requests 库，可以执行以下命令： <pre>`pip uninstall requests`</pre> 
1.  使用以下命令安装 requests 库： <pre>`pip install requests`</pre> 
1.  如果需要通过豆瓣镜像安装，可以使用以下命令： <pre>`pip install requests -i https://pypi.douban.com/simple`</pre> 

 
