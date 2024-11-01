# 原创
：  9-3 redis配置文件详解

# 9-3 redis配置文件详解

### 一、配置文件位置

以配置文件启动

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf ( Windows名为redis.windows. conf)

例：

```
# 这里要改成你自己的安装目录
cd ./redis-6.0.8
vim redis.conf
```

redis对配置文件对大小写不敏感

### 二、配置文件

#### 1、获取当前服务的配置内容

```
# 返回Redis数据目录的位置
config get dir

# 返回当前日志级别的设置
config get loglevel
```

#### 2、可以通过修改 Redis 配置文件 redis.conf 或者使用 CONFIG SET 命令来修改配置

直接修改配置文件用vim命令来就行了：
