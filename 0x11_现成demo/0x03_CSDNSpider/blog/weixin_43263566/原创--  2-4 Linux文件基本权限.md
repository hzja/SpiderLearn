# 原创
：  2-4 Linux文件基本权限

# 2-4 Linux文件基本权限

### 一、Linux权限

#### 简介

#### 文件权限

**只有root用户和文件拥有者才可以修改文件访问权限**

**每个文件针对三类访问者（文件所有者 u、同组用户 g、其他用户 o****）定义了三种主要权限：**

|权限位|权限值|描述
|------
|r|4|可读取
|w|2|可写入
|x|1|可执行

#### 目录权限

|权限|描述
|------
|读权限 - r|用户可以列出目录中的所有文件和子目录。
|写权限 - w|用户可以在目录中创建、删除和重命名文件和子目录。
|执行权限 - x|用户可以进入该目录（即切换到该目录作为当
