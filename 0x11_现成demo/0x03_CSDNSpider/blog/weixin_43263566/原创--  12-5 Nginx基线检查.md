# 原创
：  12-5 Nginx基线检查

# 12-5 Nginx基线检查

#### 扩展知识：

Nginx主配置文件：/etc/nginx/nginx.conf 这是Nginx的主要配置文件，用于配置全局的设置、HTTP块、事件处理、邮件等内容。

**打开并编辑配置文件**

```
vim /etc/nginx/nginx.conf
```

#### 一、关于禁止显示服务器版本号和操作系统版本信息：

**简介：**

在错误页面和响应头中显示Nginx版本号和操作系统信息可能会暴露服务器的安全漏洞。

默认是显示这些服务器信息的

```
curl -I 127.0.0.1
```

curl 工具，它用于在命令行下传输数据。在这个命令中，选项 -I 指示 curl 仅获取 HTTP 头信息而不下载页面内容 

**操作方法：**

在Nginx配置文件中，将`server_tokens`设置为`off`，即：

```
server_tokens off;
```

```
# 重启nginx 服务
nginx -s reload

# 再次查看
curl -I 127.0.0.1
```
