# 原创
：  【快代理API】获取隧道代理IP

# 【快代理API】获取隧道代理IP

#### 接口描述

#### 返回结果

代理IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/18bae836d067df22371c7bfe0a676a3f.png"/>

#### 参数说明

##### 必填参数
1. orderid 订单号1. num 数量
#### 代码样例

```
import requests

# API接口
api_url = "http://tps.kdlapi.com/api/gettps"

# 订单号跟API Key
orderid = 918538132507097
num = 1

# 参数
params = {
        "orderid": orderid,
        "num": num,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

返回结果，隧道代理<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/ab2964ac9038e940524ef74d81481b8c.png"/>

#### 进阶学习
