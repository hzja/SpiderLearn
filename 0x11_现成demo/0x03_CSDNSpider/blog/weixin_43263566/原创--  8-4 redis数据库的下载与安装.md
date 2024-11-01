# 原创
：  8-4 redis数据库的下载与安装

# 8-4 redis数据库的下载与安装

### 一、使用Docker方式部署redis

#### 1）搜索Redis镜像：

在Docker Hub或其他镜像仓库中搜索Redis镜像，可以使用下面的命令查找可用的镜像

```
docker search redis
```

#### 2）拉取镜像：

```
docker pull 镜像名字
```

请注意，拉取镜像可能需要一些时间，因为服务器在国外而且镜像文件比较大。

#### 3）运行容器：

使用命令`docker run -d -p 6379:6379 -v $PWD/cont/redis.conf:/usr/local/etc/redis/redis.conf -v $PWD/data:/data --name docker-redis 镜像名字 redis-server /usr/local/etc/redis/redis.conf --appendonly yes`来运行Redis容器。
