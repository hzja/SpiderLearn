# 原创
：  【快代理API】更换隧道代理IP

# 【快代理API】更换隧道代理IP

#### 接口描述

#### 返回结果

#### 参数说明

##### 必填参数
1. orderid 订单号1. signature API Key
[获取订单号和API Key教程](https://blog.csdn.net/kdl_csdn/article/details/105160723)

#### 代码样例

```
import requests

# 使用隧道代理
# 隧道服务器
tunnel_host = "tps176.kdlapi.com"
tunnel_port = 15818

# 隧道id和密码
tid = "t18538132507140"
password = "4zdldwy7"

proxies = {
    "http": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port),
    "https": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port)
}

r = requests.get("https://dev.kdlapi.com/testproxy", proxies=proxies)

# API接口
api_url = "https://tps.kdlapi.com/api/changetpsip"

# 订单号跟API Key
orderid = 918538132507097
api_key = "azx0jv2f1r9ytsmzuxskvrf9rp01vcea"

# 参数
params = {
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

```

运行结果，返回新的IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/c660199ec677151b3bcba2011246d608.png"/>

#### 进阶学习
