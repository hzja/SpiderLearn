# 原创
：  【proxy_pool搭建问题】多版本python、依赖Redis启动失败、No module named ‘click‘、proxyPool启动报错

# 【proxy_pool搭建问题】多版本python、依赖Redis启动失败、No module named ‘click‘、proxyPool启动报错

**目录**

[一、提示：多版本python](#%E4%B8%80%E3%80%81%E6%8F%90%E7%A4%BA%EF%BC%9A%E5%A4%9A%E7%89%88%E6%9C%ACpython)

[二、问题一：Redis启动失败](#%E4%BA%8C%E3%80%81%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9ARedis%E5%90%AF%E5%8A%A8%E5%A4%B1%E8%B4%A5)

[2.1、错误重现：](#2.1%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[2.2、解决方法：](#2.2%E3%80%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%9A)

[三、问题二：No module named 'click'](#%E4%B8%89%E3%80%81%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9ANo%20module%20named%20'%20rel=)

[3.1、错误重现：](#3.1%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[3.2、解决方法：](#3.2%E3%80%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%9A)

[3.2.1、原因一：未安装click模块](#3.2.1%E3%80%81%E5%8E%9F%E5%9B%A0%E4%B8%80%EF%BC%9A%E6%9C%AA%E5%AE%89%E8%A3%85click%E6%A8%A1%E5%9D%97)

[3.2.2、原因二：安装了多个python](#3.2.2%E3%80%81%E5%8E%9F%E5%9B%A0%E4%BA%8C%EF%BC%9A%E5%AE%89%E8%A3%85%E4%BA%86%E5%A4%9A%E4%B8%AApython)

[四、问题三：proxyPool启动报错](#%E5%9B%9B%E3%80%81%E9%97%AE%E9%A2%98%E4%B8%89%EF%BC%9AproxyPool%E5%90%AF%E5%8A%A8%E6%8A%A5%E9%94%99)

[4.1、错误重现：](#4.1%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A%E6%97%A0DATABASE%20CONFIGURE)

[4.2、解决方法：](#4.2%E3%80%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.2.1、原因一：连接密码问题](#4.2.1%E3%80%81%E5%8E%9F%E5%9B%A0%E4%B8%80%EF%BC%9A)

[4.2.2、原因二：不兼容](#4.2.2%E3%80%81%E5%8E%9F%E5%9B%A0%E4%BA%8C%EF%BC%9A%E4%B8%8D%E5%85%BC%E5%AE%B9)

---


 （代码总是不能想我们所想，所以才显得我们专业）

---


## 一、提示：多版本python

> 
 如果直接使用py -3 安装相关的依赖，可能会不知道安装到哪一个模块上面了

使用python的时候，加上对应的版本号
eg：py -3.8


---


---


## 二、问题一：Redis启动失败

> 
<h3>2.1、错误重现：</h3>
点击exe文件闪退
在命令行运行
提示：Creating Server TCP listening socket *:6379: bind: Unknown error
创建服务器TCP侦听套接字 *：6379：绑定：未知错误




> 
<h3>2.2、解决方法：</h3>
进入到Windosw Powershell（或者命令提示符）
**依次输入：**
.\redis-cli.exe<br/> shutdown<br/> exit<br/>  .\redis-server.exe redis.windows.conf

 最后看到这图片就是启动成功了


---


---


## 三、问题二：No module named 'click'

> 
<h3>3.1、错误重现：</h3>
ModuleNotFoundError: No module named 'click'
ModulenotFoundError：没有名为“click”的模块




> 
<h3>3.2、解决方法： </h3>
<h4>3.2.1、原因一：未安装click模块</h4>
**联网安装：**
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple click


**更多开源镜像**
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
阿里云 http://mirrors.aliyun.com/pypi/simple/
豆瓣 http://pypi.douban.com/simple/
<hr/>
<h4>3.2.2、原因二：安装了多个python</h4>
因为存在多个版本的python3

输入py -3 会找不到对应的模块 
所以未找到对应的模块
加上对应的版本号就可以了




#### 3.2.2、原因二：安装了多个python

---


---


## 四、问题三：proxyPool启动报错

> 
<h3>4.1、错误重现：</h3>
没有连接到
DATABASE CONFIGURE（数据库配置）<img alt="" height="706" src="https://img-blog.csdnimg.cn/6b0203a085b34fc388349cd88ff812a5.png" width="1200"/>



> 
<h3>4.2、解决方法：</h3>
<h4>4.2.1、原因一：连接密码问题</h4>
在命令行设置的Redis密码，在重启后会恢复默认空
推荐直接将proxy_pools中的Redis的密码改为空
（即将密码删除） 


或者在每次启动客户端的时候
重设密码
config set requirepass 123456


<hr/>
<h4>4.2.2、原因二：不兼容</h4>
在 proxy_pool 目录中的 requirements.txt 中加上一行
最新版的itsdangerous与proxy_pool不兼容，默认安装后，启动项目的时候会出现错误
加上itsdangerous==2.0.0

  py -3.8 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt




#### 4.2.2、原因二：不兼容
