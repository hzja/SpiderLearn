# 原创
：  【mysql环境】mysql的多种安装方法、环境配置总结

# 【mysql环境】mysql的多种安装方法、环境配置总结

**目录**

[第一步：mysql安装方法](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9Amysql%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95)

[方法一：](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[方法二：](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[方法三：](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A)

[第二步：配置环境变量](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

[第三步：验证是否配置成功](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E9%AA%8C%E8%AF%81%E6%98%AF%E5%90%A6%E9%85%8D%E7%BD%AE%E6%88%90%E5%8A%9F)

---


## 第一步：mysql安装方法

### 方法一：

下载MSI安装程序，进行mysql的安装

下载MySQL（官网下载地址https://downloads.mysql.com/archives/installer/）

（教程比较多）

如：

[https://blog.csdn.net/SoloVersion/article/details/123760428](https://blog.csdn.net/SoloVersion/article/details/123760428)

---


### 方法二：

下载压缩包解压安装

（教程比较多）

如：

[https://blog.csdn.net/weixin_43605266/article/details/110477391](https://blog.csdn.net/weixin_43605266/article/details/110477391)

---


### 方法三：

在docker中安装mysql容器

**<strong>1、Docker官网**</strong>：

https://hub.docker.com/_/mysql
| 命令 | 描述 

描述
| docker pull mysql | 下载最新版Mysql镜像 (=== docker pull mysql:latest ) 

下载最新版Mysql镜像 (=== docker pull mysql:latest )
| docker pull mysql:版本号 | 下载指定版本的Mysql镜像 

下载指定版本的Mysql镜像

点击Tags，可以查看所有的版本，以及对应的命令就在后面

——————

**<strong>2、下载mysql镜像**</strong>

docker pull mysql

——————

3、查看已经下载的镜像

sudo docker images

 ——————

4、创建Mysql容器并运行
| 命令 | 描述 

描述
| docker run | 创建一个新的容器 , 同时运行这个容器 

创建一个新的容器 , 同时运行这个容器
| -name mysql | 要启动的容器的名称（这里是mysql） 

要启动的容器的名称（这里是mysql）
| -d | 后台运行 

后台运行
| -p 3306:3306 | 将容器的 3306 (后) 端口映射到主机的 3306 (前) 端口 

将容器的 3306 (后) 端口映射到主机的 3306 (前) 端口
| -restart unless-stopped | 容器重启策略 

容器重启策略
| -v /mydata/mysql/log:/var/log/mysql | 将日志文件夹挂载到主机 

将日志文件夹挂载到主机
| -v /mydata/mysql/data:/var/lib/mysql | 将mysql储存文件夹挂载到主机 

将mysql储存文件夹挂载到主机
| -v /mydata/mysql/conf:/etc/mysql | 将配置文件夹挂载到主机 

将配置文件夹挂载到主机
| -e MYSQL_ROOT_PASSWORD=root | 设置root的密码（需要记住） 

设置root的密码（需要记住）
| mysql:版本号 | 启动对应的mysql的版本  

启动对应的mysql的版本 
| \ | shell 命令换行符 

shell 命令换行符

（注：使用-v将文件挂载到主机上的前，需要保证文件夹已经存在）

不挂载：

docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql

挂载（使用不挂载命令后，此处不用再输入）：

```
docker run \
--name mysql \
-d \
-p 3306:3306 \
--restart unless-stopped \
-v /mydata/mysql/log:/var/log/mysql \
-v /mydata/mysql/data:/var/lib/mysql \
-v /mydata/mysql/conf:/etc/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
mysql:版本号
```

注：如果未挂载，后续想要继续挂载的话，再使用加了挂载参数-v 文件地址参数（即上述挂载命令）

没有文件夹，我们可以手动进行创建

mkdir -p /mydata/mysql/log

——————

5、查看运行中的容器

docker ps

——————

6、进入mysql容器（mysql是容器名）

docker exec -it mysql bash

进入mysql

mysql -uroot -p

（输入的密码的地方，是隐藏式的，输入了但是不会显示而已。成功进入到mysql命令行）

---


---


## 第二步：配置环境变量

1、进入环境变量编辑

<img alt="" height="497" src="https://img-blog.csdnimg.cn/0383df958fae4ad190e2cbf4ed601a8a.png" width="943"/><br/> 2. “系统变量”---&gt;“Path”---&gt;“编辑”---&gt;“新建”---&gt;将MySQL的安装路径添加上去---&gt;“确定”

把mysql的bin目录加上去<br/><img alt="" height="652" src="https://img-blog.csdnimg.cn/665006f192d6498c8320a0ca54d414da.png" width="667"/>

## 第三步：验证是否配置成功

1、window+R---&gt;cmd

<br/> 2. 输入mysql -u root -p回车（直接在命令行打开前提是配置了全局环境）

输入密码，按下回车键，出现mysql命令行即成功

---


---


##  实战中心：

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
