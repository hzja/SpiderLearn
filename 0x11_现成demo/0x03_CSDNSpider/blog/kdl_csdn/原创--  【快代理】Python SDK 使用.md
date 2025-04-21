# 原创
：  【快代理】Python SDK 使用

# 【快代理】Python SDK 使用

#### 本文知识点

#### 安装kdl包

```
pip install kdl

```

#### 功能展示

#### 如何获取订单号与API key

登录[快代理官网](https://www.kuaidaili.com/?utm_source=csdn&amp;utm_campaign=b1a20&amp;utm_medium=b1)，打开会员中心，可以看到我的订单与API key<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/275fe1130df64d814e29864b7d3c53c0.png"/>

#### 使用样例

##### 获取订单到期时间

```
import kdl

# 938452897319117是要查询的订单号
# 8b0zeiofqrpq5ay594hu8vq7ojztmta6是此订单号的API key
auth = kdl.Auth("938452897319117", "8b0zeiofqrpq5ay594hu8vq7ojztmta6")
client = kdl.Client(auth)

# 获取订单到期时间, 返回时间字符串
expire_time = client.get_order_expire_time()
print("expire time", expire_time)

```

运行结果<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/4b7eb19e5bdbd172b2b8f1ed9b0f33f9.png"/>

##### 获取订单的白名单

```
import kdl

# 938452897319117是要查询的订单号
# 8b0zeiofqrpq5ay594hu8vq7ojztmta6是此订单号的API key
auth = kdl.Auth("938452897319117", "8b0zeiofqrpq5ay594hu8vq7ojztmta6")
client = kdl.Client(auth)

# 获取ip白名单, 返回ip列表
ip_whitelist = client.get_ip_whitelist()
print("ip whitelist", ip_whitelist)

```

##### 设置订单的白名单

```
import kdl

# 938452897319117是要查询的订单号
# 8b0zeiofqrpq5ay594hu8vq7ojztmta6是此订单号的API key
auth = kdl.Auth("938452897319117", "8b0zeiofqrpq5ay594hu8vq7ojztmta6")
client = kdl.Client(auth)

# 设置ip白名单，参数类型为字符串或列表或元组
# 成功则返回True, 否则抛出异常
client.set_ip_whitelist([])
client.set_ip_whitelist("183.221.150.77")
print(client.get_ip_whitelist())


```

##### 提取IP

这里注意我的订单是个私密代理的订单，提取的参数要参考私密代理的[获取IP接口](https://www.kuaidaili.com/doc/api/getdps/)

```
import kdl

# 938452897319117是要查询的订单号
# 8b0zeiofqrpq5ay594hu8vq7ojztmta6是此订单号的API key
auth = kdl.Auth("938452897319117", "8b0zeiofqrpq5ay594hu8vq7ojztmta6")
client = kdl.Client(auth)

# 提取私密代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://www.kuaidaili.com/doc/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'
ips = client.get_dps(num=5, sign_type='hmacsha1', format='json', pt=1, area='北京,上海,广东')
print("dps proxy: ", ips)

```

##### 检测IP有效性

这里的IP有效性并不是指IP对实际业务的可用性，而是当前IP是否还存活。有效的为true，无效的为false

```
import kdl

# 938452897319117是要查询的订单号
# 8b0zeiofqrpq5ay594hu8vq7ojztmta6是此订单号的API key
auth = kdl.Auth("938452897319117", "8b0zeiofqrpq5ay594hu8vq7ojztmta6")
client = kdl.Client(auth)

# 检测私密代理有效性： 返回 ip: true/false 组成的dict
ips = client.get_dps(num=5, sign_type='simple', format='json')
valids = client.check_dps_vali

```

##### 获取IP余额

此方法只对私密代理集中提取与私密代理按量付费的订单有效

```
import kdl

# 978454633327237 是要查询的订单号
# 619anlef8rt7fsbv0mo7vsm56g62aq1o 是此订单号的API key
auth = kdl.Auth("978454633327237", "619anlef8rt7fsbv0mo7vsm56g62aq1o")
client = kdl.Client(auth)

# 获取计数版ip余额（按量付费订单和包年包月的集中提取型订单有效）
balance = client.get_ip_balance(sign_type='hmacsha1')
print("balance: ", balance)

```

#### 进阶学习
