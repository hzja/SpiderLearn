# 原创
：  【漏洞复现】jumpserver任意密码重置

# 【漏洞复现】jumpserver任意密码重置

#### jumpserver任意密码重置漏洞-CVE-2023-42820

##### jumpserver

```
jumpserver是FIT2CLOUD飞致云旗下的开源堡垒机。
```

#### 环境搭建

##### 这里用的是vulhub靶场

##### 进入 jumpserver 的目录

##### 修改配置文件 config.env 里面的 DOMAINS 参数为kali的地址

##### 运行环境，第一次运行的话会拉取文件，要耐心等待。

##### 命令：
1. `sudo compose up -d`
##### 查看docker容器

##### 命令：
1. `sudo docker-compose -ps`
##### 用浏览器访问 192.168.55.166:8080 (kali的ip地址)

#### 首先我们用它自带的poc(可以帮助我们理解漏洞原理)

##### 点击”忘记密码”

##### 输入用户名 admin 和验证码

**右键 =&gt; 在新建标签页打开图像 (获得图片种子值 seed )**

##### 复制 seed 值后进行下一步，输入邮箱(默认都是admin@mycomany),复制url上面的 token 值

##### 上poc算它的验证码(我的理解是根据种子值 seed 和 token 可以算出来它的验证码)

##### 命令：
1. `python3 poc.py -t 目标地址 --email admin&lt;span&gt;@mycomany&lt;/span&gt; --seed 种子值 --token 口令值`
##### 我这里报错了，经过一系列的修改都没运行成功。我在其他地方找到了一个自动化的exp。

#### 上自动化exp(在附件分享给你们)

##### 修改配置文件里面的ip地址

##### 全自动就是好，都不用自己去算验证码，直接把密码改好了，我们拿过去登录试一下

##### 登录成功，这次漏洞复现到此结束，感谢观看。

## **免费领取安全学习资料包！~**<img alt="" height="768" src="https://img-blog.csdnimg.cn/ff35aaf6215244529587612de637fd41.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/d441847801a54ed2b41bef21873ef32d.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/efaf4063a5cb40bc936303e54cd280f9.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/aa76d6ed016c4c4384bf39caaf62a164.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/11680e2ae491459f8ee0a5efde2dd71f.png" width="665"/>

应急响应笔记

学习路线

 
