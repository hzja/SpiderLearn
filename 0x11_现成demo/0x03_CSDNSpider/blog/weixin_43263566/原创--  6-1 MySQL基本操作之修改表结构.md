# 原创
：  6-1 MySQL基本操作之修改表结构

# 6-1 MySQL基本操作之修改表结构

#### 前置条件：

创建库：[MySQL基本操作之创建数据库-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133951336)

创建表：[MySQL基本操作之创建数据表-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133952800)

#### 1、末尾增加字段

在表结构末尾增加一个名为 beizhu 的字段，类型为 varchar(250)，并添加注释 'trie'：

```
ALTER TABLE student ADD beizhu VARCHAR(250) COMMENT 'trie';
```

#### 2、在表结构开头增加一个名为 xxx 的字段，类型为 varchar(20)：

```
ALTER TABLE student ADD xxx VARCHAR(20) FIRST;
```
