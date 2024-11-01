# 原创
：  4-5 MySQL需要了解的常用命令

# 4-5 MySQL需要了解的常用命令

### 目录

####  1、MySQL 相关的 shell 命令

##### 1）启动MySQL：

```
systemctl start mysqld
```

该命令用于启动MySQL服务器

##### 2）关闭MySQL：

```
systemctl stop mysqld
```

该命令用于关闭MySQL服务器

##### 3）检查MySQL是否启动：

```
ps -ef | grep mysqld

或

systemctl status mysqld
```

ps -ef | grep mysqld  该命令用于查看当前系统中是否有mysqld进程在运行

#### 2、MySQL中的常用命令

要使用下面的命令首先你要先登录进MySQL

```
# 其中-u root表示使用root用户登录
```
