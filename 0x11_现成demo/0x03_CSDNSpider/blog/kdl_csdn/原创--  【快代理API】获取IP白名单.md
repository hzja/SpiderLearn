# 原创
：  【快代理API】获取IP白名单

# 【快代理API】获取IP白名单

#### 接口描述

#### 返回结果

返回白名单内的IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/e124eae61e58ddf494b697dad325a371.png"/>

#### 参数说明

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests


# API接口
api_url = "https://dev.kdlapi.com/api/getipwhitelist"

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

运行结果，返回当前设置的白名单IP与可设置的白名单额度<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/2511f2113355f555aad71319391b54b6.png"/>

#### 进阶学习
