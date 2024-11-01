# 原创
：  26-2 SQL注入攻击 - 堆叠注入（Stacked Injection）

# 26-2 SQL注入攻击 - 堆叠注入（Stacked Injection）

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、堆叠注入定义

        堆叠注入（Stacked Injection）是指一次性执行多条 SQL 语句的注入技术。在实际应用中，堆叠注入通常指在MySQL等数据库中，通过在命令行中以分号（;）分隔每条语句来实现同时执行多条语句的注入攻击。因此，堆叠注入即为一堆（多条）SQL语句一起执行的注入攻击方式。

####  二、堆叠注入的原理

堆叠注入（Stacked Injection）的原理是利用 SQL 语句中的分号（;）作为语句结束的标志，通过在输入中插入分号并继续构造新的 SQL 语句来实现执行多条 SQL 语句的目的。当数据库执行时，会按顺序执行这些语句，从而导致恶意操作的执行。与联合注入（Union Injection）不同的是，联合注入主要用于执行查询语句，并且只能合并特定类型的语句，而堆叠注入可以执行任意类型的 SQL 语句。

举例来说，如果用户输入 `1; DELETE FROM products`，服务器端生成的 SQL 语句可能会变成：

```
select * from users where productid=1; DELETE FROM users
```

这样，在执行查询时，第一条语句
