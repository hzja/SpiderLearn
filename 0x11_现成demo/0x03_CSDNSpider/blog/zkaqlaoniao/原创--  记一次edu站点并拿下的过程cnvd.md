# 原创
：  记一次edu站点并拿下的过程cnvd

# 记一次edu站点并拿下的过程cnvd

## **0x01 jeecg-boot介绍**

<br/> JeecgBoot是一款基于代码生成器的低代码开发平台，零代码开发！采用前后端分离架构：SpringBoot2.x，Ant Design&amp;Vue，Mybatis-plus，Shiro，JWT。强大的代码生成器让前后端代码一键生成，无需写任何代码！ JeecgBoot引领新的开发模式 (Online Coding模式-&gt; 代码生成器模式-&gt; 手工MERGE智能开发)，帮助解决Java项目70%的重复工作，让开发更多关注业务逻辑。

## <br/>**0x02 发现过程**

<br/> 一开始想着去复现一下CVE-2023-1454(jeecg-boot)的SQL注入的，结果意外打野发现了edu站点。来到目标站点时，进行目录的拼接访问

```
/jeecg-boot/jmreport/qurestSql

```

发现直接404了<br/>  

<br/> 不慌，直接拼接jeecg-boot，发现未授权。<br/>  

<br/> (小声说：edu站点提交cnvd是收的)<br/>  

<br/> 大家也可以去fofa上找类似网站，祝大家尽快拿到属于自己的一份编号

```
app="JeecgBoot-企业级低代码平台"
```

**没看够~？欢迎关注！**

 【腾讯文档】免费领取安全学习资料包！<br/> https://docs.qq.com/doc/DYlBlQ2xhaFBmamtq
