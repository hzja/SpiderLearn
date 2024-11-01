# 原创
：  12-2 Nginx配置文件详解

# 12-2 Nginx配置文件详解

Nginx是一个常用的高性能的Web服务器和反向代理服务器

#### 下面是Nginx常见的目录与配置文件：

1.  主配置文件：/etc/nginx/nginx.conf 这是Nginx的主要配置文件，用于配置全局的设置、HTTP块、事件处理、邮件等内容。 
1.  子配置文件目录：/etc/nginx/conf.d/ 在这个目录下可以放置一些额外的配置文件，这些配置文件可以包含不同的虚拟主机或者其他配置信息。需要注意的是，这里的配置文件需要以.conf为后缀，并且需要手动创建。 
1.  默认主页面路径：/usr/share/nginx/html 这是Nginx默认的网站根目录，通常情况下可以在这个目录下放置网站的静态文件或者动态文件。 
1.  访问日志存放路径：/var/log/nginx/access.log Nginx的访问日志会被记录到这个文件中，可以通过查看这个文件来了解用户的访问情况。 
1.  错误日志存放路径：/var/log/nginx/error.log Nginx的错误日志会被记录到这个文件中，可以通过查看这个文件来了解Nginx服务器的错误情况。 

更多信息请自行查看官方文档：[nginx 文档](https://nginx.org/en/docs/) 

#### Nginx的主配置文件（nginx.conf）讲解

```
vim /etc/nginx/nginx.conf
```

1.  全局块：
