# 原创
：  7-2 数据库扫描工具scuba

# 7-2 数据库扫描工具scuba

### 目录:

#### 一、什么是Scuba？

Scuba是一款网络安全扫描工具，而非数据库扫描软件。Scuba支持对Web应用程序、操作系统、网络协议等进行扫描，以发现潜在的安全漏洞和风险，并提供详细的扫描结果报告。Scuba的主要特点是支持多种扫描技术和功能，可以根据用户的需求进行定制化扫描，以提高扫描效率和准确性。 

这个工具其实就是扫描mysql的配置文件，减少我们手动检查的时间：[MySQL安全基线检查-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/134043432)

#### 二、Scuba的安装（[下载](https://tool.4xseo.com/a/19792.html)）

##### Windows安装

###### 1）将mysql-connector-java-5.1.44文件夹下的mysql-connector-java-5.1.44-bin.jar，复制到Scuba-Windows\ODBC\Production\MYSQL目录下

好像是说本机还有安装java的jdk,但是我主机之前就有安装过，我也不知道需不需要，如果你
