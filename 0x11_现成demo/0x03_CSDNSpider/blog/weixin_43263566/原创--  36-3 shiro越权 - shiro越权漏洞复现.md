# 原创
：  36-3 shiro越权 - shiro越权漏洞复现

# 36-3 shiro越权 - shiro越权漏洞复现

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、vulhub搭建shiro漏洞环境

```
# 切换到漏洞目录下，vulhub要改成自己的存放路径
cd ./vulhub/vulhub/shiro/CVE-2020-1957

# 使用 Docker Compose 来拉取并启动 Shiro 靶场
docker-compose up -d

# 关闭防火墙（如果有的话）
systemctl stop firewalld
```

IP + 8080 端口访问

#### 二、漏洞复现

我们现在访问网站的admin页面，网站会先对我们当前的用户权限进行验证，没有通过就会跳转到登录页面，让我们的登录一个有对应权限的账号

注意：因为靶场会进行权限验证所以访问会比较慢
