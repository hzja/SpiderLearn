# 原创
：  38-3 Web应用防火墙 - 安装配置WAF

# 38-3 Web应用防火墙 - 安装配置WAF

首先需要安装Centos 7 虚拟机：[Centos7超详细安装教程_centos7安装教程-CSDN博客](https://blog.csdn.net/weixin_61587867/article/details/129392663)

#### 安装配置WAF

在桌面环境中，右键点击打开终端，首先执行以下步骤：

##### 1）安装必要的工具： 输入命令：

```
sudo su
yum install -y wget epel-release
```

##### 2）第二步，安装依赖工具，输入以下命令：

```
yum install -y httpd httpd-devel pcre pcre-devel libxml2-devel gcs lua-devel yajl-devel ssdeep-devel curl-devel
```
