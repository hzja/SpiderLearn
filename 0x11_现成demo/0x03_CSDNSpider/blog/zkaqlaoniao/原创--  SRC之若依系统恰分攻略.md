# 原创
：  SRC之若依系统恰分攻略

# SRC之若依系统恰分攻略

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[​编辑Druid弱口令上分](#%E2%80%8B%E7%BC%96%E8%BE%91Druid%E5%BC%B1%E5%8F%A3%E4%BB%A4%E4%B8%8A%E5%88%86)

[信息收集](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[druid目录探测](#druid%E7%9B%AE%E5%BD%95%E6%8E%A2%E6%B5%8B)

[druid弱口令爆破](#druid%E5%BC%B1%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4)

[总结](#%E6%80%BB%E7%BB%93)

---


## 前言

---


> 
`1.若依系统存在较多魔改版本，具有前后端分离的情况，内置了druid`


通过这个拿下了交大证书

## <img alt="3dfb00db42344a0aa27405fb17ecda1d.png" src="https://img-blog.csdnimg.cn/3dfb00db42344a0aa27405fb17ecda1d.png"/>**Druid弱口令上分**

---


### 信息收集

---


首先，我们要做的是收集基于若依CMS的系统

#### 图标收集方法

最简单的就是利用图标的方法进行收集(以下只是举例)

> 
`1.(icon_hash="-1231872293" || icon_hash="706913071")`


**内容收集**

另外可以收集的就是内容

下面是以主体中的关键字进行匹配(大部分存在二改的情况)<img alt="6afa0cb0e7984aa8a0af837eeaf4971d.png" src="https://img-blog.csdnimg.cn/6afa0cb0e7984aa8a0af837eeaf4971d.png"/>

#### 标题收集

收集类似的标题

#### 前后端分离之后端收集1

发现下述内容，是ruoyi后端，也需要进行收集

由于存在很多魔改版本,大致会修改ruoyi那一段

<img alt="c53d41593b564203b8a9e09610f27a78.png" src="https://img-blog.csdnimg.cn/c53d41593b564203b8a9e09610f27a78.png"/>收集的思路大致为内容匹配(以下是思路之一)

<img alt="52fc0445694d418b8671bea4ff232bda.png" src="https://img-blog.csdnimg.cn/52fc0445694d418b8671bea4ff232bda.png"/>**前后端分离之后端收集2**

除了存在后台欢迎的情况，也可能做了弱权限校验，会出现以下情况

因此此类也需要收集

#### 最重要

如果是为了教育上分的话，需要加上一点小小的黑魔法<br/> 加上下面这句话就会筛选出来的内容为教育网段内容

> 
`1.org="China Education and Research Network Center"`


### druid目录探测

---


#### 默认路径探测0-未授权

如果配置不当可能不需要druid密码即可直接访问druid

> 
`1./druid/index.html`


#### 默认路径探测1-druid

若依默认的druid路径是

> 
`1.``/druid/login.html`


收集的网址直接拼接，如果成功，就说明存在druid后台

#### 默认路径探测2-默认api

若依存在默认的api，druid的路径可能在api下

> 
`1./prod-api/druid/login.html`
`2./dev-api/druid/login.html`


收集的网址直接拼接，如果成功，就说明存在druid后台

#### 默认路径探测3-开发自定义

在这个情况下，直接扫描是没有任何用处的，通常的思路是首先浅浅登录错误一次，查看数据包的目录

示例如下

发现存在一个地址

抓包查看地址后发现如下目录

那么拼接地址为

> 
`1./{发现的api}/druid/login.html`


#### 默认路径探测总结

常见路径地址如下

> 
`1./druid/index.html`
`2./druid/login.html`
`3./prod-api/druid/login.html`
`4./prod-api/druid/index.html`
`5./dev-api/druid/login.html`
`6./dev-api/druid/index.html`
`7./api/druid/login.html`
`8./api/druid/index.html`
`9./admin/druid/login.html`
`10./admin-api/druid/login.html`


甚于内容请在实战中进行尝试

### druid弱口令爆破

---


通常druid不需要验证码就可以进行爆破（请自行收集字典)

#### 常见用户名

> 
`1.admin`
`2.druid`
`3.ruoyi`
`4....`


#### 常见密码

> 
`1.123456`
`2.admin`
`3.druid`
`4....`


### 总结

相对来说爆破还是需要一本好的字典的，重点在于收集面

以下是在edu-src中使用druid弱口令上分的部分

**没看够~？欢迎关注！**
