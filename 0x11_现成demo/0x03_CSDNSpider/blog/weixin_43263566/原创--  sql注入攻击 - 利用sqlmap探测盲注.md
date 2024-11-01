# 原创
：  sql注入攻击 - 利用sqlmap探测盲注

# sql注入攻击 - 利用sqlmap探测盲注

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187) 

<img alt="" height="555" src="https://img-blog.csdnimg.cn/direct/7d1f22bcc1bf43d9b4c3a545b1e07f1d.png" width="1200"/> 

#### 一、利用 sqlmap 探测 get 盲注

```
sqlmap -h
```

<img alt="" height="513" src="https://img-blog.csdnimg.cn/direct/f239a27ba6ae47c19fc3eaf49af7027f.png" width="650"/> 

**`--technique=TECH`：指定要使用的 SQL 注入技术，默认为 "BEUSTQ"。**

BEUSTQ 是一个缩写，其中每个字母代表一个不同的 SQL 注入技术：
