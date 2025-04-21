# 原创
：  【快代理API】获取独享代理

# 【快代理API】获取独享代理

#### 使用快代理提供的生成API链接

<img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/9978ae7ce8357bf93c57904deb160a9f.png"/><br/> 点生成链接<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/f18063fe69dc03127b56f4be499cee17.png"/>

#### 代码样例

```
import requests


# API接口
api_url = "http://kps.kdlapi.com/api/getkps/?orderid=968538292172353&amp;num=1&amp;pt=1&amp;sep=1"

res = requests.get(api_url)
print(res.content)

```

运行结果，返回独享代理的IP<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/8c937b70a42c1455e08bd9f709adc83e.png"/>

#### 进阶学习
