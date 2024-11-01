# 原创
：  SRC之若依系统恰分攻略-2

# SRC之若依系统恰分攻略-2

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[若依系统的信息收集](#%E8%8B%A5%E4%BE%9D%E7%B3%BB%E7%BB%9F%E7%9A%84%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[任意用户注册(较少见)](#%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E6%B3%A8%E5%86%8C%28%E8%BE%83%E5%B0%91%E8%A7%81%29)

[Druid登录后利用](#Druid%E7%99%BB%E5%BD%95%E5%90%8E%E5%88%A9%E7%94%A8)

[Swagger-ui泄露](#Swagger-ui%E6%B3%84%E9%9C%B2)

---


## 前言

---


```
之前介绍了若依系统的druid弱口令，接下来介绍若依系统的其他上分攻略
```

如果单纯的druid弱口令，那么只是低危，配合其他的可以升级危害。 

## 若依系统的信息收集

---


具体内容，请看前文，这里不做过多介绍

https://bbs.zkaq.cn/t/31119.html

## 任意用户注册(较少见)

---


通常我们遇到的ruoyi系统如下

 <img alt="" height="358" src="https://img-blog.csdnimg.cn/617f54100adf4deb86036a309e8ce5cd.png" width="1021"/>

注意URL为

```
https://xxxxx.edu.cn/login?redirect=%2Findex

```

也可能遇到其他二改系统的路径为

```
https://xxxxx.edu.cn/{任意内容}/login?redirect=%2Findex
```

大部分使用ruoyi框架的人都会忽略掉前端的注册界面(后端可能删了)<br/> 因此我们拼接/register<img alt="" height="440" src="https://img-blog.csdnimg.cn/5fba815b48af47d1ad5613ebc75c7a88.png" width="1080"/>

 这个时候我们注册账户，如果后端未关闭的话，可以注册成功

注册失败大致如下

下面是某交的成功案例

## Druid登录后利用

---


在我们无法登录若依的时候，如果我们获取到了druid连接池，我们可以尝试扩大危害

首先如何发现druid请看前文

https://bbs.zkaq.cn/t/31119.html

进入druid后我们重点关注的是`/druid/weburi.html`与`/druid/websession.html`

### Druid到获取未授权路由

---


在这我们可以获得创建了连接池的URI <img alt="" height="244" src="https://img-blog.csdnimg.cn/d0a67a09103f409bbf4ce9d45b483c46.png" width="1080"/>

在这里面如果开发在开发的时候没做权限校验，我们可以获得未授权的API接口

在这里就放个案例，进去之后发现了一个接口

通过拼接发现了未授权接口

### Druid到敏感信息泄露

---


有时候可能会在路径中翻到上传的文件(如PDF后缀)

访问的话，会发现泄露了大量的敏感信息

### Druid到登录系统

---


在`/druid/websession.html`路径下，我们有时候可以看到已经连接的`SESSIONID`

我们切到登录处在登录的同时替换掉`SESSIONID`有可能可以登录系统

这里不进行赘述

## Swagger-ui泄露

---


除了Druid之外，其实和Swagger组件是一起的

同理也存在自定义路径的可能性需要收集，如果Swagger组件没修改的话，查看的效果和druid泄露的效果类似

这边提供部分路径(建议确定是否是自定义路径之后进行dirsearche扫描)

```
/swagger-ui/index.html
/prod-api/swagger-ui/index.html
/api/swagger-ui/index.html
```

## 总结

利用起来不难，难的是信息收集，如何收集到更多的资产

---


**没看够~？欢迎关注！**

---


 <img alt="" height="768" src="https://img-blog.csdnimg.cn/17f505d73aff477ea464db514369ed6d.png" width="1024"/>
