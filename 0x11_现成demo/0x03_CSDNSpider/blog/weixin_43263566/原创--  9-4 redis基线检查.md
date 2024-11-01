# 原创
：  9-4 redis基线检查

# 9-4 redis基线检查

#### 1、禁止使用 root 用户启动 | 访问控制

##### 描述：

使用root权限来运行网络服务存在较大的风险。Nginx和Apache都有独立的work用户，而Redis没有。例如，Redis的Crackit漏洞就是利用root用户权限替换或增加authorize_keys，从而获取root登录权限。

##### 加固建议：

使用root切换到redis用户启动服务，步骤如下：

```
# 创建reds用户，并指定其登录后所使用的shell，并禁止其创建登录目录
useradd -s /sbin/nolog -M redis
```

接下来，可以使用sudo命令以redis用户身份启动Redis服务器，具体命令如下：

```
# 这里要改成你自己的安装目录
cd ./redis-6.0.8/src
 
sudo -u redis ./redis-server ../redis.conf
```

#### 2、禁止监听在公网 | 访问控制 

##### **描述：**

Redis监听在0.0.0.0地址上，可能会导致服务对外或内网产生横向移动渗透的风险，黑客可以利用此漏洞进行入侵。

##### **加固建议&amp;#**
