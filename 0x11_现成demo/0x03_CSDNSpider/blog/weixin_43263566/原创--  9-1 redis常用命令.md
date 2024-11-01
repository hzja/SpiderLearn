# 原创
：  9-1 redis常用命令

# 9-1 redis常用命令

在 Redis 客户端中，以下是一些常用的 Redis 命令和对应的示例：

#### 1、退出客户端 (Quit):

```
redis-cli&gt; QUIT
```

#### 2、停止 Redis 服务 (Shutdown):

```
redis-cli&gt; SHUTDOWN
```

#### 3、测试服务是否运行 (Ping):

```
redis-cli&gt; PING
```

#### 4、打印字符串 (Echo):

```
redis-cli&gt; echo "Hello, World!"
```

#### 5、验证密码是否正确 (AUTH):

```
redis-cli&gt; AUTH password
```

#### 6、查看所有的键

```
keys *
```

#### 7、删除键 (DEL):

```
redis-cli&gt; DEL key
```

#### 8、检查 key 是否存在 (EXISTS):

```
redis-cli&gt; EXISTS key
```

#### 9、查看 Redis 信息 (INFO):
