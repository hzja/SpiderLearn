# 原创
：  37-2 Python 的 requests 库发送 POST 请求

# 37-2 Python 的 requests 库发送 POST 请求

准备 sqlilabs 靶场： [构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、发送 POST 请求

首先使用bp对 sqlilabs 靶场的第12关抓个包，了解这个关卡是如何发包的

打开靶场：本地ip+ /sqli-labs-master/Less-12/

先随便输入个账号登录如：23523 / 3tw4t

再输入个正确的账号登录：admin/admin

**使用bp抓包登录的包了解请求格式**

<img alt="" height="667" src="https://img-blog.csdnimg.cn/direct/4f8aeb893041405fb23d4edbfe3c0738.png" width="967"/> 

**构造请求脚本**

 

```
# -*- coding:utf-8 -*-
import r
```
