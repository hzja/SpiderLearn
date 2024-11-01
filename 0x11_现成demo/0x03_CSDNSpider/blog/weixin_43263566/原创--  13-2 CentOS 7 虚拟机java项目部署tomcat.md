# 原创
：  13-2 CentOS 7 虚拟机java项目部署tomcat

# 13-2 CentOS 7 虚拟机java项目部署tomcat

#### 首先安装java环境

下载安装包：[jdk-19_linux-x64_bin.tar.gz_免费高速下载|百度网盘-分享无限制 (baidu.com)](https://pan.baidu.com/s/1fyrn2eo-MBw9Lmwg74IT1A?pwd=ax12)

将安装包上传到虚拟机

 解压

```
tar zxvf jdk-19_linux-x64_bin.tar.gz
```

移动文件到

```
mv jdk-19.0.1 /usr/jdk-19.0.1
```

编辑配置文件

```
vim /etc/profile
```

```
export JAVA_HOME=/usr/jdk-19.0.1
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

让配置生效

```
source /etc/profile
```

验证安装
