# 原创
：  【快代理API】检测开放代理有效性

# 【快代理API】检测开放代理有效性

#### 接口描述

#### 返回结果

代理存活返回true，失效返回false<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/7f12ca5a31279cd053e5b6d90c5be402.png"/>

#### 参数说明

##### 必填参数
1. orderid 订单号1. proxy 要检测的开放代理1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

注意这里的orderid，api_key参数需要填自己订单的真实信息。

```
import requests


# API接口
api_url = "https://dps.kdlapi.com/api/checkopsvalid"

# 订单号跟API Key
orderid = 938452897319117
api_key = "8b0zeiofqrpq5ay594hu8vq7ojztmta6"

# 代理IP
proxy = "103.143.234.5:56269"

# 参数
params = {
        "proxy": proxy,
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，代理存活<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/4d37be3a608288af61c2ddb94d61f8ae.png"/>

#### 进阶学习
