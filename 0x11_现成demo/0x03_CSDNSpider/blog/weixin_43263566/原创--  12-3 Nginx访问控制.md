# 原创
：  12-3 Nginx访问控制

# 12-3 Nginx访问控制

Nginx的`location`块用于基于接收到的请求字符串（例如：www.test.com/uri-string）对虚拟主机之外的部分进行匹配，并对特定的请求进行处理。它可以用于地址重定向、数据缓存、应答控制等功能，并且还可以配置许多第三方模块。

#### `location`块的基本格式：

```
location [= | ~ | ~*] uri {
    指令1;
    指令2;
    ...
}
```

##### 使用精确匹配的`location`块的配置

###### 准备

1.  首先进入命令行或者终端，进入需要创建目录的文件夹。 <pre>`cd /usr/share/nginx/html`</pre> 
1.  然后输入以下命令来创建test目录： <pre>`mkdir test`</pre> 
