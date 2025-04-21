# 原创
：  【快代理API】获取开放代理

# 【快代理API】获取开放代理

#### 使用快代理提供的生成API链接

我的订单生成API链接<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/682240a0c7fb8188f035ab8c270cd5bd.png"/>

点生成链接<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/f27d639717844329e84e0b59bf0d7627.png"/>

#### 代码样例

```
import requests


# API接口
api_url = "http://dev.kdlapi.com/api/getproxy/?orderid=948538324516226&amp;num=100&amp;protocol=1&amp;method=2&amp;an_an=1&amp;an_ha=1&amp;sep=1"

res = requests.get(api_url)
print(res.content)

```

运行结果，返回开放代理的IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/375b049cc1ea5259ec402ce2177fc2b5.png"/>

#### 进阶学习
