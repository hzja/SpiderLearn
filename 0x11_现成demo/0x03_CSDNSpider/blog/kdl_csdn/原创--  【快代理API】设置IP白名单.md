# 原创
：  【快代理API】设置IP白名单

# 【快代理API】设置IP白名单


          摘要生成于
          [ C知道](https://ai.csdn.net?utm_source=cknow_pc_ai_abstract) 
          ，由 DeepSeek-R1 满血版支持，
          [ 前往体验 &gt;](https://ai.csdn.net?utm_source=cknow_pc_ai_abstract)

#### 接口描述

#### 返回结果

#### 参数说明

<img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/00d4bb7eb8d35419e060c8aab11fa32d.png"/><br/> 注意参数iplist，如果不带此参数代表设置您的当前IP作为白名单

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests


# API接口
api_url = "https://dev.kdlapi.com/api/setipwhitelist"

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

运行结果，设置成功<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/3d5a4087d143b64f8acb69b8a03068b0.png"/>

#### 进阶学习
