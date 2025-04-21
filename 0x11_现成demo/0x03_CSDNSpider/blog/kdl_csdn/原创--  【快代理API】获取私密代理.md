# 原创
：  【快代理API】获取私密代理

# 【快代理API】获取私密代理

#### 使用快代理提供的生成API链接

我的订单生成API链接<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/bd586b2a01ef1f18ee457aa51f4a8fac.png"/><br/> 点生成链接<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/dfe5f8f5bd1a344359f77da1fe8dec68.png"/>

#### 代码样例

```
import requests


# API接口
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=938452897319117&amp;num=10&amp;pt=1&amp;sep=1"

res = requests.get(api_url)
print(res.content)

```

运行结果，返回私密代理的IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/07ca84f9e73320e639a81e26f5874bae.png"/>

#### 进阶学习
