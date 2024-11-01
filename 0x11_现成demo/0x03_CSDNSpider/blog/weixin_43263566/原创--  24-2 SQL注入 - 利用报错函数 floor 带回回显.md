# 原创
：  24-2 SQL注入 - 利用报错函数 floor 带回回显

# 24-2 SQL注入 - 利用报错函数 floor 带回回显

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、原理

利用`COUNT()`, `FLOOR()`, `RAND()`, 和 `GROUP BY`来生成主键重复错误

**函数解释**

#### 二、注入示例

以靶场的第五关做演示：[http://127.0.0.1/sqlilabs/less-5/?id=1](http://127.0.0.1/sqlilabs/less-5/?id=1)
