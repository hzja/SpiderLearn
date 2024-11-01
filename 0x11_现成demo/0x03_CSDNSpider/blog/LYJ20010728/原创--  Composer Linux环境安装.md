# 原创
：  Composer Linux环境安装

# Composer Linux环境安装

> 
- Linux 平台可以使用以下命令来安装：


```
php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');"
php composer-setup.php

```

> 
- 移动 composer.phar，这样 composer 就可以进行全局调用：


```
mv composer.phar /usr/local/bin/composer

```

> 
- 切换为国内镜像：


```
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

```

> 
- 更新 composer：


```
composer selfupdate

```
