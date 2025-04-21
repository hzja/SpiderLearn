# 原创
：  【MySQL】在CentOS环境下安装MySQL

# 【MySQL】在CentOS环境下安装MySQL

**目录**

[一、卸载残留环境](#%E4%B8%80%E3%80%81%E5%8D%B8%E8%BD%BD%E6%AE%8B%E7%95%99%E7%8E%AF%E5%A2%83)

[二、获取官方yum源](#%E4%BA%8C%E3%80%81%E8%8E%B7%E5%8F%96%E5%AE%98%E6%96%B9yum%E6%BA%90)

[三、安装yum源](#%E4%B8%89%E3%80%81%E5%AE%89%E8%A3%85yum%E6%BA%90)

[四、安装MySQL](#%E5%9B%9B%E3%80%81%E5%AE%89%E8%A3%85MySQL)

[五、启动MySQL](#%E4%BA%94%E3%80%81%E5%90%AF%E5%8A%A8MySQL)

---


## 一、卸载残留环境

输入 ps axj | grep mysql 查看是否存在正在运行的MySQL服务

如果有，则先输入 systemctl stop mysqld 来关闭服务

然后输入 rpm -qa | grep mysql 查看是否已经存在相关安装包

像这样，如果存在，则需要全部卸载，输入 rpm -qa | grep mysql | xargs yum -y remove即可全部卸载。

此时再输入 rpm -qa | grep mysql，原先的安装包已经卸载了

要确认是否已经将MySQL服务卸载干净，可以输入ls /etc/my.cnf 查看是否存在该文件，如果卸载干净了是不会有这个文件的

---


## 二、获取官方yum源

首先通过下面这段命令查看CentOS版本

```
cat /etc/redhat-release
```

然后在官方yum源网站中下载yum源，尽量寻找和自己环境版本匹配的源

网址：[Index of /232905 (mysql.com)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://repo.mysql.com/](https://repo.mysql.com/)

进入网页后如果看不全细节，可以在页面源代码中查看

推荐选择前缀为mysql57的rpm安装包，按照自己的版本对应el后面的数字，有对应的小版本则优先选择，否则选择大版本匹配的。

点击下载到本地后，将对应rpm安装包上传到Linux中。

---


## 三、安装yum源

首先保证与rpm安装包位于同一目录下

输入 rpm -ivh + 安装包名 即可安装，类似这个效果

然后输入 ls /etc/yum.repos.d/ -l 查看yum源列表中是否已经有了MySQL的yum源

然后输入 yum list | grep mysql 查看是否存在相关MySQL的资源

至此，yum源安装成功，之前的rpm安装包可以卸载了

---


## 四、安装MySQL

输入 yum install -y mysql-community-server 开始安装，如果安装成功最后会提示Complete，这里已经安装好了所以会提示Nothing to do

如果安装到最后提示如下：

> 
Failing package is: mysql-community-client-5.7.39-1.el7.x86_64
GPG Keys are configured as: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql


则说明遇到了密钥过期的问题

输入 rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022 即可解决

要验证是否安装成功，输入 ls /etc/my.cnf 确保该文件存在，然后输入which mysqld和which mysql看下是否存在MySQL的服务端和客户端

---


## 五、启动MySQL

输入 systemctl start mysqld 启动MySQL服务

然后输入 ps axj | grep mysql 看看有没有跑起来

至此完成MySQL在CentOS环境下的安装

如有错误和缺漏欢迎在评论区指出.
