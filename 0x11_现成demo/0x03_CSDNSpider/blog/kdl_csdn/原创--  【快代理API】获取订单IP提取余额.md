# 原创
：  【快代理API】获取订单IP提取余额

# 【快代理API】获取订单IP提取余额

#### 接口描述

#### 返回结果

balance 余额<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/df825ac6c1cfd098cec11c30e7258111.png"/>

#### 参数说明

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests


# API接口
api_url = "https://dps.kdlapi.com/api/getipbalance"

# 订单号跟API Key
orderid = 948538010667581
api_key = "ll1jibev8bohcplm1p20jy8ksx4my2od"

# 参数
params = {
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，此订单今日还剩990个IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/11eca7845493267566f86ad61b39f33a.png"/>

#### 进阶学习
