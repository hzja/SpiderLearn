# 原创
：  实战 | 某证书站Bypass sql

# 实战 | 某证书站Bypass sql

## **信息收集**

```
edu证书站这么多年已经被各种大佬轮了不下几十遍了，所以各种思路也是被玩烂了。现在无非这几种方法:</code>`    找账号进统一系统-----&amp;gt;找各种洞``    子域名，ip旁站``    搞vpn账号打内网`<code>    公众号小程序（也是本人目前搞的最多的方法）.
```

## **定位目标**

1、搜索证书站的名字，然后找去一个一个寻找公众号和小程序，这种方法只能慢慢来。之后就定位到了某个公众号（目前已修），公众号也是另一种的web形式，所以这里公众号的选项可能是参数点

2、进行抓包处理（打个厚码），这里就是能看到各种参数值

3、对于这种参数值，按照我的习惯，**不管什么参数都试一试，试一试**。单引号两个单引号进行测试，看看闭合不闭合。这里也是有一个报错页面,直接放payload。

4、对于上面的我解释一下，首先respond包里面有一个.net，那么就可以证明这是一个aspx站点，那么根据经验判断，aspx站点配mssql数据库或者access数据库。判断语言和数据库，这里的order是一个排序注入点，这里的asc可控，所以可以进行注入，这里成功报错除了数据库名，一枚SQL注入到手~

```
数据库语句类似：select * from user order by asc
```

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/0b4ee047fe734a689773c7b3ed66a399.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/c5510ebd22b1433aac726b8c8eedbd85.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4cb6b9305b8f473fb0744911d49927ed.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/62f53ed1f8a947be9a446700e628d553.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/508d8b17fe5d4881a59304faa338d394.png" width="665"/>

应急响应笔记

学习路线
