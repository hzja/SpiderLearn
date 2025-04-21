# 原创
：  【快代理API】检测私密代理有效性

# 【快代理API】检测私密代理有效性

#### 接口描述

#### 返回结果

代理存活返回true，失效返回false<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/ea9eb27880c1c2d930376415ddf33125.png"/>

#### 参数说明

##### 必填参数
1. orderid 订单号1. proxy 要检测的私密代理1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

注意这里的orderid，api_key参数需要填自己订单的真实信息。

```
import requests


# API接口
api_url = "https://dps.kdlapi.com/api/checkdpsvalid"

# 订单号跟API Key
orderid = 938452897319117
api_key = "8b0zeiofqrpq5ay594hu8vq7ojztmta6"

# 代理IP
proxy = "121.17.171.7:17757"

# 参数
params = {
        "proxy": proxy,
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，代理存活<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/fb5cc00605cdf93f8a89d6b447d74e6e.png"/>

#### 进阶学习
