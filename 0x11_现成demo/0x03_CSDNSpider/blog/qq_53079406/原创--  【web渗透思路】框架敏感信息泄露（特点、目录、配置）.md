# 原创
：  【web渗透思路】框架敏感信息泄露（特点、目录、配置）

# 【web渗透思路】框架敏感信息泄露（特点、目录、配置）

 <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）框架信息泄露（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|渗透思维博文|目标|状态
|[【web渗透思路】敏感信息泄露（网站+用户+服务器）](https://blog.csdn.net/qq_53079406/article/details/127974676)| 信息泄露示例、泄露方式、泄露危害、泄露挖掘、用户信息泄露、服务器信息泄露 |已发布
|[【web渗透思路】框架敏感信息泄露（特点、目录、配置）](https://blog.csdn.net/qq_53079406/article/details/127992005)|框架信息泄露|已发布
|[【web渗透思路】任意账号的注册、登录、重置、查看](https://blog.csdn.net/qq_53079406/article/details/127999030)|任意用户注册、登陆、重置、查看|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、挖掘思路](#%E4%B8%80%E3%80%81%E6%8C%96%E6%8E%98%E6%80%9D%E8%B7%AF)

[1、方法：](#1%E3%80%81%E6%96%B9%E6%B3%95%EF%BC%9A)

[二、框架之信息泄露](#%E4%BA%8C%E3%80%81%E6%A1%86%E6%9E%B6%E4%B9%8B%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)

[ 1、Webpack](#%C2%A01%E3%80%81Webpack)

[1.1、简述](#1.1%E3%80%81%E7%AE%80%E8%BF%B0)

[1.2、.js.map文件泄露](#1.2%E3%80%81.js.map%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2)

[1.3、源码审计](#1.3%E3%80%81%E6%BA%90%E7%A0%81%E5%AE%A1%E8%AE%A1)

[2、Spring boot](#2%E3%80%81Spring%20boot)

[1.1、简述](#1%E3%80%81%E7%AE%80%E8%BF%B0)

[1.2、利用](#1.2%E3%80%81%E5%88%A9%E7%94%A8)

[1.3、框架识别](#1.3%E3%80%81%E6%A1%86%E6%9E%B6%E8%AF%86%E5%88%AB)

---


（基本分析方法都是一样，这里就举2个框架关于信息泄露方面的）

## 一、挖掘思路

> 
<h3>1、方法：</h3>
摸清楚是何种框架后，直接搜对应框架存在的漏洞问题
框架存在的路径，进行遍历访问
框架所具有的特点
框架的组件等


---


---


## 二、框架之信息泄露

> 
<h3> 1、Webpack</h3>
<h4>1.1、简述</h4>
是一个JavaScript应用程序的静态资源打包器，它会递归构建一个依赖关系图，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个bundle。
大部分Vue等项目应用会使用webpack进行打包，如果没有正确配置，就会导致项目源码泄露，可能泄露的各种信息如API、加密算法、管理员邮箱、内部功能等。
<pre><code>project_name
|—— src
|    |—— index.js
|    |—— App.vue 
|—— index.html
|—— package.json 
|—— webpack.config.js
|—— babel.config.js
</code></pre>

<hr/>
<h4>1.2、.js.map文件泄露</h4>
1、方法一：如果配置好npm环境，并安装了reverse-sourcemap，在js最后会有注释：//#sourceMappingURL=xxxxxxx.js.map
2、方法二：在开发者工具中搜索.js.map，找到MarketSearch.js.map所在的js，找到对应的链URL，一般静态文件会挂载在当前域名下（但不排除其他站点挂载的情况，所以需要找到对应的URL），并对其进行下载

<img alt="" height="227" src="https://img-blog.csdnimg.cn/ce5a95a9acd94bf286b1519257553604.png" width="337"/>  
3、方法三：可以在浏览器控制台中的Sources------&gt; Page------&gt; webpack://中查看源代码（js同目录下会生成 js.map文件）
4、方法四：插件的使用
<hr/>
<hr/>
<h4>1.3、源码审计</h4>
获得源码后，开始正常的挖掘操作
1、找前端接口（如登录接口api、user、login等）
2、找路径（寻找未授权访问）
3、找有请求传入的地方（GET、POST寻找可控变量）
4、找高权限接口（如一些管理员接口中可能的关键词admin,superadmin,manage等）
5、拼接的动态接口（接口又很多参数拼接而成）
……
<hr/>
1.2、框架识别
1、使用浏览器插件识别


2、看图标

3、最基本识别web框架的方式是查看HTTP响应报头中的X-Powered-By字段


#### 1.2、.js.map文件泄露

---


---


> 
<h3>2、Spring boot</h3>
<h4>1.1、简述</h4>
1、Spring boot：是 Spring 的一套快速配置脚手架，可基于Spring boot 快速开发单个微服务（其特点决定了功能模块分布式部署，在不同的机器上相互通过服务调用进行交互，业务流会经过多个微服务的处理和传递）
2、微服务的监控：Actuator组件为Spring Boot提供对应用系统的监控和管理的集成功能，可以查看应用配置的详细信息（如自动化配置信息、创建的Spring beans信息、系统环境变量的配置信以及Web请求的详细信息等）
3、安全隐患：Actuator配置不当或存在缺陷，可造成信息泄露等（如/heapdump作为Actuator组件最为危险的Web接口，如果Actuator配置不当，攻击者可无鉴权获取heapdump堆转储文件）
4、分类：
​ 1.原生端点
​ 2.用户自定义扩展端点


<hr/>
<h4>1.2、利用</h4>
获取相应数据后，再使用工具进行分析
<hr/>
<h4>1.3、框架识别</h4>
1、使用浏览器插件识别
2、看图标

3、报错页面




#### 1.2、利用

---


---


---


> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>目标：众测平台、企业src应急响应中心 
<table border="1" cellpadding="1" cellspacing="1"><tbody>|众测平台|URL
|漏洞盒子|[漏洞盒子 | 互联网安全测试众测平台](https://www.vulbox.com/)
|火线安全平台|[火线安全平台](https://www.huoxian.cn/)
|漏洞银行|[BUGBANK 官方网站 | 领先的网络安全漏洞发现品牌 | 开放安全的提出者与倡导者 | 创新的漏洞发现平台](https://www.bugbank.cn/)
|360漏洞众包响应平台|[360漏洞云漏洞众包响应平台](https://src.360.net/)
|补天平台（奇安信）|[补天 - 企业和白帽子共赢的漏洞响应平台，帮助企业建立SRC](https://www.butian.net/)
|春秋云测|[首页](https://zhongce.ichunqiu.com/)
|雷神众测（可信众测，安恒）|[雷神众测 - BountyTeam](https://www.bountyteam.com/)
|云众可信（启明星辰）|[云众可信 - 互联网安全服务引领者](https://www.cloudcrowd.com.cn/)
|ALLSEC|[ALLSEC](https://i.allsec.cn/#/)
|360众测|[360众测平台](https://zhongce.360.cn/)
|看雪众测（物联网）|[https://ce.kanxue.com/](https://ce.kanxue.com/)
|CNVD众测平台|[网络安全众测平台](https://zc.cnvd.org.cn/)
|工控互联网安全测试平台|[CNCERT工业互联网安全测试平台](https://test.ics-cert.org.cn/)
|慢雾（区块链）|[Submit Bug Bounty - SlowMist Zone - Blockchain Ecosystem Security Zone](https://slowmist.io/bug-bounty.html)
|平安汇聚|[http://isrc.pingan.com/homePage/index](http://isrc.pingan.com/homePage/index)
</tbody></table>


<table border="1" cellpadding="1" cellspacing="1"><tbody>|互联网大厂|URL
|阿里|https://asrc.alibaba.com/#/
|腾讯|https://security.tencent.com/
|百度|https://bsrc.baidu.com/v2/#/home
|美团|https://security.meituan.com/#/home
|360|https://security.360.cn/
|网易|https://aq.163.com/
|字节跳动|https://security.bytedance.com/
|京东|https://security.jd.com/#/
|新浪|http://sec.sina.com.cn/
|微博|https://wsrc.weibo.com/
|搜狗|http://sec.sogou.com/
|金山办公|https://security.wps.cn/
|有赞|https://src.youzan.com/
</tbody></table>

<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

