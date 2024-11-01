# 原创
：  22-3 利用sqlmap探测get类型注入

# 22-3 利用sqlmap探测get类型注入

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187) 

基础：[GET基于报错的sql注入利用-脱库-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/135795755) 

sqlmap 工具是kali自带的

例子我都用sql靶场的第一关做演示

#### 1、探测数据库名

```
sqlmap -u "http://192.168.0.103/sqlilabs/less-1/?id=1" --dbs --batch
```

这是一个使用 sqlmap 工具进行 SQL 注入测试的命令。具体来说，该命令将使用 sqlmap 工具对 `http://192.168.0.103/sqlilabs/less-1/?id=1` 进行测试，其中：
