# 原创
：  6-2 MySQL基本操作之记录增删改查

# 6-2 MySQL基本操作之记录增删改查

#### 前置条件：

创建库：[MySQL基本操作之创建数据库-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133951336)

创建表：[MySQL基本操作之创建数据表-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/133952800)

### 数据表增加数据/记录 

#### 1、向学生表（student）添加数据 

```
# 如果已经有 beizhu  字段这句代码就不要执行了
ALTER TABLE student ADD beizhu VARCHAR(250) COMMENT '备注';  # 在未尾添加一个字段

INSERT INTO student(name, age, gender, birth_date, email, address, phone , beizhu) 
VALUES('张三', 27, '男', '1996-1-1', '[[email protected]](/cdn-cgi/l/email-protection)', '上海', '139000022', '学渗透');

INSERT INTO student(name, age, gender, birth_date, email, address, phone , beizhu) 
VALUES('李四', 19, '男', '1999-1-1', '[[email protected]](/cdn-cgi/l/email-protection)', '杭州', '1393342422', '学开发');

INSERT INTO student(n
```
