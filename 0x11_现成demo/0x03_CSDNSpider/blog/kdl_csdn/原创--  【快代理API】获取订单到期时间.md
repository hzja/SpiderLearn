# 原创
：  【快代理API】获取订单到期时间

# 【快代理API】获取订单到期时间

#### 接口描述

#### 返回结果

#### 参数说明

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

这里需要拿到自己的订单号和订单号的API key，

```
import requests


# API接口
api_url = "https://dev.kdlapi.com/api/getorderexpiretime"

# 订单号跟API Key
orderid = 938452897319117
api_key = "8b0zeiofqrpq5ay594hu8vq7ojztmta6"

# 参数
params = {
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，到期时间<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/5686bf5be4c5c53031e263b3f57ffaf4.png"/>

#### 进阶学习
