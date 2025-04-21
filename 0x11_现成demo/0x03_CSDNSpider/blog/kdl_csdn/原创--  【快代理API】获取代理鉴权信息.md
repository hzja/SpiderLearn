# 原创
：  【快代理API】获取代理鉴权信息

# 【快代理API】获取代理鉴权信息

#### 接口描述

鉴权信息在HTTP请求的Header中传递，格式为：

```
Proxy-Authorization: &lt;type&gt; &lt;credentials&gt;

```

#### 返回结果

#### 参数说明

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests


# API接口
api_url = "https://dev.kdlapi.com/api/getproxyauthorization"

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

运行结果，返回鉴权信息<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/2a2d137793fd3b884b77ff4e020d9bed.png"/>

#### 进阶学习
