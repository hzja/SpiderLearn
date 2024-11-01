# 原创
：  6-3 MySQL数据库查询实战操作

# 6-3 MySQL数据库查询实战操作

#### 前置条件：

创建库：[MySQL基本操作之创建数据库-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133951336)

创建表：[MySQL基本操作之创建数据表-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133952800)

#### 目录

## 一、常规查询

### 普通的查询方式

####  1、查询所有姓名以 "张" 开头的学生：

```
SELECT * FROM student WHERE name LIKE '张%';
```

这条语句使用 `LIKE` 运算符来匹配以 "张" 开头的姓名。

 <img alt="" height="577" src="https://img-blog.csdnimg.cn/8ac8a29a6aab48688872b66f7d8ebb91.png" width="996"/> 

####  2、查询年龄在25岁以上的学生：

```
SELECT * FROM student WHERE age &gt; 25;
```

这条语句通过使用大于符号（&gt;）来筛选出年龄大于25岁的学生。

 
