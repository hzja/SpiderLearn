# 原创
：  25-4 SQL注入攻击 - update注入

# 25-4 SQL注入攻击 - update注入

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、MySQL UPDATE语句复习：

**Update语句练习：**

要修改security数据库中users表的admin字段的值为000000，可以使用以下UPDATE语句：

```
UPDATE users SET admin='000000' WHERE &lt;更新条件&gt;;
```

请确保将`&lt;更新条件&gt;`替换为适合您情况的实际条件，以确保只有符合条件的行会被更新。如果要更新整个表中的所有行，可以省略WHERE子句

#### 二、update 注入代码分析

**靶场的17关（Less-17）**
