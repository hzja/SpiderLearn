# 原创
：  Sqlmap进行http头注入及流量分析

# Sqlmap进行http头注入及流量分析

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

利用 SQLMap 进行 HTTP 头注入的方式对于 Less-19 注入点的注入

SQLMap 工具我使用kali中自带的

#### 注入准备

先使用bp将Less-19靶场的包抓下来保存到 txt 文件中，输入账号 admin/admin 进行抓包

复制数据包保存为 test.txt 文件

 然后在数据包的 Referer: 字段尾部加上 *

#### 注入实现

```
# 格式：
sqlmap -r 文件名称 -p 参数名 --dbs --batch
 
# 示例：（我的数据包文件是存放在kali的桌面所以这里就是 /home/
```
