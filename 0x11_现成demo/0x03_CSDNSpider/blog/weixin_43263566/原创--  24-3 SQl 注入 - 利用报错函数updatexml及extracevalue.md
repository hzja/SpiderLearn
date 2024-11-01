# 原创
：  24-3 SQl 注入 - 利用报错函数updatexml及extracevalue

# 24-3 SQl 注入 - 利用报错函数updatexml及extracevalue

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、updatexml() 函数

##### 1. 使用前提:

在 MySQL 高版本中（大于5.1版本）添加了对 XML 文档进行查询和修改的函数，包括 `updatexml()` 和 `extractvalue()`。

##### 2. 显示错误处理：

在开发程序中应采用 `print_r(mysql_error())` 函数，将 MySQL 错误信息输出。

##### 3. updatexml函数介绍：

##### 4. Payload内容：
