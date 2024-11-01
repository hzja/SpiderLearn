# 原创
：  39-2 Web应用防火墙 - WAF数据库层绕过

# 39-2 Web应用防火墙 - WAF数据库层绕过

如果你本地没有安装mysql就先安装一下：[4-2 MySQL 的下载与安装_mysql5.7.9.1下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133841689) 

#### 一、数据库层绕过简介

        绕过数据库层通常用于规避Web应用防火墙（WAF）的SQL注入防护规则。攻击者需要利用数据库特性，寻找规避常规安全策略的方法。这里涉及到不同数据库的特性、SQL语法和安全策略的深入理解。

#### 二、MySQL 数据库中的绕过策略

MySQL是最常用的数据库之一，因此针对MySQL的研究非常深入。绕过WAF的SQL注入防护规则需要了解常见过滤点和数据库特性。

##### 1）常见过滤点

**(1) \Nunion 形式**

```
# 先进入mysql数据库（这个是默认数据，mysql都有的）
use mysql

SELECT Host FROM user where Host=\Nunion SELECT schema_name FROM information_schema.schemata;
```

这个SQL语句的作用是尝试从两个不同的数据源中获取信息并合并结果集。让我解释一下：
