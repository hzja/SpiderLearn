# 原创
：  6-4 MySQL身份验证绕过漏洞

# 6-4 MySQL身份验证绕过漏洞

 搭建 vmihub靶场：[vulhub靶场搭建与使用_剁椒鱼头没剁椒的博客-CSDN博客](https://blog.csdn.net/weixin_44268918/article/details/128055553)

#### 运行漏洞：

```
# 这里要改成自己的 /vulhub-master 存放目录
cd /etc/docker/vulhub-master/mysql/CVE-2012-2122


# 关闭防火墙，不然就要放行3306端口
systemctl stop firewalld

# 重启 Docker 服务
service docker restart

# 创建链接，这样才能直接使用docker-compose命令
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# 启动环境 
docker-compose up -d

```

####  查看漏洞详情

```
# 查看README.md文件
cat README.md
```

##### Mysql 身份认证绕过漏洞（CVE-2012-2122）介绍：

当连接MariaDB/MySQL时，输入的密码会与期望的正确密码比较，由于不正确的处理，会导致即便是memcmp()返回一个非零值，也会使MySQL认为两个密码是相同的。也就是说只要知道用户名&amp;
