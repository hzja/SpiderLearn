# 原创
：  【proxy_pool搭建】Windows版搭建、Redis依赖环境安装、proxy_pool依赖安装、proxy_pool搭建

# 【proxy_pool搭建】Windows版搭建、Redis依赖环境安装、proxy_pool依赖安装、proxy_pool搭建

**目录**

[一、问题：](#%E4%B8%80%E3%80%81%E9%97%AE%E9%A2%98%EF%BC%9A)

[二、Redis依赖安装](#%E4%BA%8C%E3%80%81Redis%E4%BE%9D%E8%B5%96%E5%AE%89%E8%A3%85)

[2.1、Redis下载](#2.1%E3%80%81Redis%E4%B8%8B%E8%BD%BD)

[2.2、Redis安装](#2.2%E3%80%81Redis%E5%AE%89%E8%A3%85)

[2.3、启动](#2.3%E3%80%81%E5%90%AF%E5%8A%A8)

[2.4、命令行设置Redis密码](#2.4%E3%80%81%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%AE%BE%E7%BD%AERedis%E5%AF%86%E7%A0%81)

[2.4.1、打开Redis客户端](#2.4.1%E3%80%81%E6%89%93%E5%BC%80Redis%E5%AE%A2%E6%88%B7%E7%AB%AF)

[2.4.2、查看密码](#2.4.2%E3%80%81%E6%9F%A5%E7%9C%8B%E5%AF%86%E7%A0%81)

[2.4.3、设置密码](#2.4.3%E3%80%81%E8%AE%BE%E7%BD%AE%E5%AF%86%E7%A0%81)

[2.4.4、提示：](#2.4.4%E3%80%81%E6%8F%90%E7%A4%BA%EF%BC%9A)

[2.4.5、验证密码：](#2.4.5%E3%80%81%E9%AA%8C%E8%AF%81%E5%AF%86%E7%A0%81%EF%BC%9A)

[三、proxy_pool依赖安装](#%E4%B8%89%E3%80%81proxy_pool%E4%BE%9D%E8%B5%96%E5%AE%89%E8%A3%85)

[四、proxy_pool搭建](#%E5%9B%9B%E3%80%81proxy_pool%E6%90%AD%E5%BB%BA)

[4.1、下载：](#4.1%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[4.2、更改配置：](#4.2%E3%80%81%E6%9B%B4%E6%94%B9%E9%85%8D%E7%BD%AE%EF%BC%9A)

[4.3、启动](#4.3%E3%80%81%E5%90%AF%E5%8A%A8)

[4.4、检验：](#4.4%E3%80%81%E6%A3%80%E9%AA%8C%EF%BC%9A)

---


 

---


## 一、问题：

> 
 （搭建可能遇见的问题）
[【proxy_pool搭建问题】多版本python、依赖Redis启动失败、No module named ‘click‘、proxyPool启动报错<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124771045?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124771045?spm=1001.2014.3001.5501)


## 二、Redis依赖安装

> 
<h3>2.1、Redis下载</h3>
[Releases · microsoftarchive/redis (github.com)https://github.com/microsoftarchive/redis/releases<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases)

<hr/>

<h3>2.2、Redis安装</h3>


修改文件位置，然后基本上都是下一步了






### 2.2、Redis安装

> 
<h3>2.3、启动</h3>
进入安装目录
双击运行redis服务端文件redis-server.exe
然后再运行启动redis客户端，双击redis-cli.exe

服务端文件redis-server.exe

再打开客户端redis-cli.exe




> 
<h3>2.4、命令行设置Redis密码</h3>
<h4>2.4.1、打开Redis客户端</h4>

<hr/>
<h4>2.4.2、查看密码</h4>
输入config get requirepass
默认密码是空

<hr/>
<h4>2.4.3、设置密码</h4>
config set requirepass 123456
（123456是设置的密码）
返回ok就是设置成功了

<hr/>
<h4>2.4.4、提示：</h4>
设置密码成功后所有操作都要验证密码，否则会报错
<hr/>

<h4>2.4.5、验证密码：</h4>
输入auth 123456
（auth 后接的 password）





#### 2.4.2、查看密码

---


#### 2.4.4、提示：

---


---


---


 

## 三、proxy_pool依赖安装

> 
打开Windows powershell（或者cmd后进入）
pip3 install -r requirements.txt
或者
  py -3.8 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

最让人难搞的是这个click（python自带的模块）
我安装的是python3.8和python3.10







---


---


## 四、proxy_pool搭建

> 
<h3>4.1、下载：</h3>
[jhao104/proxy_pool: Python爬虫代理IP池(proxy pool) (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/jhao104/proxy_pool](https://github.com/jhao104/proxy_pool)


> 
<h3>4.2、更改配置：</h3>
更改配置文件setting.py中的内容


将要改的地方


更改HOST和Redis的密码
我改后是下面这样


保存后退出


> 
<h3>4.3、启动</h3>
进入到目录里面
打开Windows powershell（或者使用cmd）
 py -3.8 proxyPool.py schedule
(python后面接的版本根据自己具体的python版本)




> 
<h3>4.4、检验：</h3>
 浏览器输入
[http://127.0.0.1:5010/](http://127.0.0.1:5010/)
 配置成功就会返回页面，失败则会连接失败


