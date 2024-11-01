# 原创
：  get基于报错的sql注入利用-读敏感文件和写入一句话木马

# get基于报错的sql注入利用-读敏感文件和写入一句话木马

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187) 

基础：[GET基于报错的sql注入利用-脱库-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/135795755) 

#### 1、select into outfile或`dumpfile` 写入一句话马

这里用Sqli-labs靶场的第一关做演示，之前演示过改关卡的闭合符是单引号，靶场地址：[http://127.0.0.1/sqlilabs/less-1/?id=1](http://127.0.0.1/sqlilabs/less-1/?id=1)

判断MysQL的存储路径方便我们写入一句话马

```
# MySQL的@@datadir变量的值（表示数据目录的路径）
-1 union select 1,@@datadir,3 -- -
```

&lt;
