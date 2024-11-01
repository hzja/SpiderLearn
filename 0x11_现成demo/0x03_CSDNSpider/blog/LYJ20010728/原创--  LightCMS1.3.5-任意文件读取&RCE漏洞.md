# 原创
：  LightCMS1.3.5-任意文件读取&RCE漏洞

# LightCMS1.3.5-任意文件读取&amp;RCE漏洞

#### LightCMS1.3.5-任意文件读取&amp;RCE漏洞

## 环境搭建(Kali)

> 
个人环境配置：php7.4.15 + mysql8.0.25


> 
- 首先确保系统已安装好composer，可以参考我之前写的文章：[文章链接](https://editor.csdn.net/md/?articleId=117754283)- 下载文件源码


```
cd /var/www/html
git clone https://hub.fastgit.org/eddy8/LightCMS.git
cd lightCMS
composer install

```

> 
- 设置目录权限：storage/和bootstrap/cache/目录需要写入权限。


```
sudo chmod 777 -R storage/ bootstrap/cache/

```

> 
- 新建一份环境配置，并配置好数据库等相关配置


```
cp .env.example .env

数据库配置：
CREATE DATABASE homestead;
CREATE USER 'homestead'@'localhost' IDENTIFIED BY 'secret';
GRANT ALL PRIVILEGES ON *.* TO 'homestead'@'localhost';
FLUSH PRIVILEGES;

```

> 
初始化系统


```
php artisan migrate --seed

PS:这里可能会遇到一些问题，我备注一下自己遇到的问题及其解决方案
1、安装组件时如果无法生成vendor目录可以运行composer install --ignore-platform-reqs命令
2、启动服务时Illuminate\Database\QueryException报错可能是因为没有安装php-mysql依赖
step1:php -v
step2: Install php mysql extension
php 7.x sudo apt-get install php7.x-mysql
step3: service apache2 restart
step4: php artisan migrate

```

> 
- 后台访问地址：/admin/login


```
默认用户（此用户为超级用户，不受权限管理限制）：admin/admin
这里可能会遇到图形验证码无法显示，终端输入：apt-get install php7.x-gd

```

## 漏洞复现

### 利用点一

> 
使用admin/admin登录管理员<br/> 访问http://ip/admin/neditor/serve/catchimage，POST传file=file:///etc/passwd，此时会返回


```
{"list":[{"url":"http://light.com/upload/image/202106/0f1726ba83325848d47e216b29d5ab99.jpg","source":"file:///etc/passwd","state":"SUCCESS"}]}

```

> 
根据返回值，直接访问链接地址即可


### 利用点二

> 
直接传php文件RCE，构造一个php脚本放置vps下，访问读取该文件


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610002741842.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610002747715.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 漏洞分析

> 
这个漏洞出在`app/Http/Controllers/Admin/NEditorController.php`中的远程下载图片的功能


> 
这里简单使用了`file_get_contents`来获取并保存文件内容，所以我们可以使用file协议实现任意文件读取等ssrf操作，更危险的是这里的逻辑是取到的文件名后缀是什么，保存的就是什么后缀，所以我们可以放一个php一句话在服务器上，然后来请求该一句话文件来达到getshell的目的

