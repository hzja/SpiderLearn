# 原创
：  sqli-labs-master靶场搭建详细过程（附下载链接）

# sqli-labs-master靶场搭建详细过程（附下载链接）
1. 首先进行搭建准备，分别点击下载SQLi-LABS以及phpstudy，下载网址如下。
```
# SQLi-LABS
https://github.com/Audi-1/sqli-labs
```

```
# phpstudy
https://www.xp.cn/download.html
```
1. 将下载好的”sqli-labs-master.zip”进行解压。1. 将解压缩好的“sqli-labs-master”文件夹移动到“WWW”目录下。1. 在“WWW\sqli-labs\sql-connections”路径下找到“db-creds.inc”文件。1. 打开后找到“$dbpass =”，在后面输入数据库的密码，默认是“root”。
```
&lt;?php

//give your mysql connection username n password
$dbuser ='root';
$dbpass ='root';               #此位置需要根据自己数据库的密码进行修改！！！
$dbname ="security";
$host = 'localhost';
$dbname1 = "challenges";



?&gt;
```
1. 在安装好的phostudy中点击“软件管理”，下滑找到“php5.5.9nts”后点击“安装”，安装完成后如下图所示。1. 之后点击“网站”--&gt;“管理”--&gt;php版本，选择刚刚安装的“php5.5.9nts”。1. 点击“启动”。1. 通过浏览器访问“[http://localhost/sqli-labs-master/](http://localhost/sqli-labs-master/)“后会进入如下页面。1. 点击”Setup/reset Database for labs“ 来创建数据库、创建表和填充数据。1. 得到以下页面SQLi-LABS靶场即搭建完成。