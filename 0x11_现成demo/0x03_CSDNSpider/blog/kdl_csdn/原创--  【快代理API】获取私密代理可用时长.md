# 原创
：  【快代理API】获取私密代理可用时长

# 【快代理API】获取私密代理可用时长

#### 接口描述

#### 返回结果

#### 参数说明

##### 必填参数
1. orderid 订单号1. proxy 要查询的代理1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests


# API接口
api_url = "https://dps.kdlapi.com/api/getdpsvalidtime"

# 订单号跟API Key
orderid = 938452897319117
api_key = "8b0zeiofqrpq5ay594hu8vq7ojztmta6"

# 代理IP
proxy = "117.26.41.138:23745"

# 参数
params = {
        "proxy": proxy,
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，代理可用时长226秒<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/b03a276ef5eeb7a49e649e8f9e26ec16.png"/>

#### 进阶学习
