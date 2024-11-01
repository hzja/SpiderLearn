# 原创
：  【代码审计-JAVA】基于javaweb框架开发的

# 【代码审计-JAVA】基于javaweb框架开发的

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
（1）javaweb三大框架（√）
（2）特征（√）
（3）重要文件（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|审计博文|类型|状态
|[【代码审计-PHP】phpStudy（新版） + PhpStorm + XDebug动态调试](https://blog.csdn.net/qq_53079406/article/details/127728220)|PHP|已发布
|[【代码审计-PHP】审计方法、敏感函数、功能点](https://blog.csdn.net/qq_53079406/article/details/127819601)|PHP|已发布
|[【代码审计-PHP】基于Thinkphp框架开发的](https://blog.csdn.net/qq_53079406/article/details/127826862)|PHP|已发布
|[【代码审计-.NET】基于.NET框架开发的基本特征](https://blog.csdn.net/qq_53079406/article/details/128257403)| .NET |已发布
|[【代码审计-.NET】基于.NET框架开发的代码审计](https://blog.csdn.net/qq_53079406/article/details/128262502)|.NET|已发布
|[【代码审计-JAVA】基于javaweb框架开发的](https://blog.csdn.net/qq_53079406/article/details/128267950)|JAVA|已发布
|[【代码审计-JAVA】javaweb代码审计思路](https://blog.csdn.net/qq_53079406/article/details/128270053)|JAVA|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、javaweb三大框架](#%E4%B8%80%E3%80%81javaweb%E4%B8%89%E5%A4%A7%E6%A1%86%E6%9E%B6)

[1、Spring（开源分层的框架）](#1%E3%80%81Spring%EF%BC%88%E5%BC%80%E6%BA%90%E5%88%86%E5%B1%82%E7%9A%84%E6%A1%86%E6%9E%B6%EF%BC%89)

[2、Struts（MVC设计模式）](#2%E3%80%81Struts%EF%BC%88MVC%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%89)

[3、Hibernate（开源的对象关系映射框架）](#3%E3%80%81Hibernate%EF%BC%88%E5%BC%80%E6%BA%90%E7%9A%84%E5%AF%B9%E8%B1%A1%E5%85%B3%E7%B3%BB%E6%98%A0%E5%B0%84%E6%A1%86%E6%9E%B6%EF%BC%89)

[ 二、特征](#%C2%A0%E4%BA%8C%E3%80%81%E7%89%B9%E5%BE%81)

[1、结构](#1%E3%80%81%E7%BB%93%E6%9E%84)

[2、Servlet](#2%E3%80%81Servlet)

[3、程序入口](#3%E3%80%81%E7%A8%8B%E5%BA%8F%E5%85%A5%E5%8F%A3)

[三、重要文件](#%C2%A0%E4%BA%8C%E3%80%81%E9%87%8D%E8%A6%81%E6%96%87%E4%BB%B6)

[1、web.xml](#1%E3%80%81web.xml)

[2、pom.xml](#2%E3%80%81pom.xml)

[3、web.xml与pom.xml区别](#3%E3%80%81web.xml%E4%B8%8Epom.xml%E5%8C%BA%E5%88%AB)

[4、Filter（过滤器）](#4%E3%80%81Filter%EF%BC%88%E8%BF%87%E6%BB%A4%E5%99%A8%EF%BC%89)

[5、框架+组件](#5%E3%80%81%E6%A1%86%E6%9E%B6%2B%E7%BB%84%E4%BB%B6)

---


> 
<h2>一、javaweb三大框架</h2>
java web常用的三大框架：Spring、Struts、Hibernate（SSH）
（注：介绍来自百度百科）
<h3>1、Spring（开源分层的框架）</h3>
它是为了解决企业应用开发的复杂性而创建的。框架的主要优势之一就是其分层架构，分层架构允许使用者选择使用哪一个组件，同时为 J2EE 应用程序开发提供集成的框架。Spring的用途不仅限于服务器端的开发。从简单性、可测试性和松耦合的角度而言，任何Java应用都可以从Spring中受益。Spring的核心是控制反转(IoC)和面向切面(AOP)。简单来说，Spring是一个分层的JavaSE/EE full-stack(一站式) 轻量级开源框架。Spring的优点有，方便解耦，简化开发 (高内聚低耦合)；AOP编程的支持；声明式事务的支持；方便程序的测试；方便集成各种优秀框架；降低JavaEE API的使用难度。<img alt="" height="607" src="https://img-blog.csdnimg.cn/7a6fb56cd2514d088a332dcd4659c4bc.png" width="867"/>
<pre><code>.
|  mvnw
|  mvnw.cmd
|  pom.xml
|  README.md
|  .gitignore
└─ src
│   ├─main
│   │  ├─java
│   │  │  ├─com.example.demo
│   │  │  │  gApplication.java
│   │  │  │  
│   │  │  │  ├─controller
│   │  │  │  │  ├─UserController.java
│   │  │  │  │
│   │  │  │  ├─domain
│   │  │  │  │  ├─User.java
│   │  │  │  │
│   │  │  │  ├─service
│   │  │  │  │  ├─UserService.java
│   │  │  │  │  │
│   │  │  │  │  ├─impl
│   │  │  │  │  │  ├─UserServiceImpl.java
│   │  │  │  │
│   │  │  │  ├─repository
│   │  │  │  │  ├─UserRepository
│   │  │  │  │
│   │  │  │  ├─dto
│   │  │  │  │  ├─UserDTO.java
│   │  │  │  │
│   │  │  │  ├─vo
│   │  │  │  │  ├─UserVO.java
│   │  │  │  │
│   │  │  │  ├─utils
│   │  │  │  │  ├─EncryptUtil.java
│   │  │  │  │
│   │  │  │  ├─config
│   │  │  │  │  ├─QuartzJob.java
│   │  │  │  │
│   │  ├─resources
│   │  │  ├─static
│   │  │  │  ├─css
│   │  │  │  ├─js
│   │  │  ├─templates
│   │  │  ├─application.properties
│   │
│   ├─test
│   │  ├─java
│   │  │  ├─com.example.demo
│   │  │  │  ├─controller
│   │  │  │  │  ├─UserControllerTests.java</code></pre>
<hr/>

<h3>2、Struts（MVC设计模式）</h3>
Struts定义了通用的Controller，通过配置文件(通常是Struts -config.xml)隔离Model和View，以Action的概念以对用户请求进行了封装，使代码更加清晰易读。Struts还提供了自动将请求的数据填充到对象中以及页面标签等简化编码的工具。Struts能够开发大型Java Web项目。<img alt="" height="564" src="https://img-blog.csdnimg.cn/8b9825f3dbd049cfb9e04772acc654c8.png" width="730"/>
<pre><code>apps    用于存放官方提供的 Struts2 示例程序，这些程序可以作为学习者的参考资料。各示例均为 war 文件，可以通过 zip 方式进行解压。
docs    用于存放官方提供的 Struts2 文档，包括 Struts2 的快速入门、Struts2 的文档，以及 API 文档等内容。
lib     用于存放 Struts2 的核心类库，以及 Struts2 的第三方插件类库。
src     用于存放该版本 Struts2 框架对应的源代码。</code></pre>
<hr/>
<h3>3、Hibernate（开源的对象关系映射框架）</h3>
它对JDBC进行了非常轻量级的对象封装，它将POJO与数据库表建立映射关系，是一个全自动的orm框架，hibernate可以自动生成SQL语句，自动执行，使得Java程序员可以随心所欲的使用对象编程思维来操纵数据库。Hibernate可以应用在任何使用JDBC的场合，既可以在Java的客户端程序使用，也可以在Servlet/JSP的Web应用中使用，最具革命意义的是，Hibernate可以在应用EJB的JaveEE架构中取代CMP，完成数据持久化的重任。Hibernate的API有:Session、SessionFactory、Transaction、Query、Criteria和Configuration。通过这些接口，可以对持久化对象进行存取、事务控制。

<pre><code>documentation          存放了 Hibernate 的相关文档，包括 Hibernate 的参考文档和 API 文档等。
lib                    该路径下存放了 Hibernate 3 的核心类库，以及编译和运行所依赖的第三方类库。其中 lib 路径下的 required子目录中包含了运行 Hibernate 3 所必须的 JAR 包。
project                存放了 Hibernate 各种相关项目的源代码。
changelog.txt          升级日志
hibernate_logo.gif     hibernate logo
lgpl.txt               开源许可证内容</code></pre>



### 2、Struts（MVC设计模式）

---


> 
<h2> 二、特征</h2>
<h3>1、结构</h3>
<pre><code>1、分层架构：

视图层（View 视图)
控制层（Controller、Action 控制层）
服务层（Service）
业务逻辑层BO(business object)  
实体层（entity 实体对象、VO(value object) 值对象 、模型层（bean）
持久层（dao- Data Access Object 数据访问层、PO(persistant object) 持久对象）</code></pre>



<pre>`2、模块化开发`</pre>

<hr/>

<h3>2、Servlet</h3>
Java Web容器上运行的程序，处理服务器端的业务逻辑
Servlet3.0之前：在web.xml中配置
Servlet3.0之后(Tomcat7+)：可以使用注解方式配置Servlet

<h3>3、程序入口</h3>
（路由、接收处理参数的方法）
<pre><code>servlet    全局搜doGet()、doPost()
spring     匹配注解@RequestParam(value=”参数名”,required=true/false,defaultValue=””)
struts2    根据web.xml匹配路径与类名，寻找action</code></pre>



### 2、Servlet

> 
<h2>三、重要文件</h2>
<h3>1、web.xml</h3>
web.xml是web项目的配置文件，主要配置Filter，Listener，Servlet等（但是web.xml并不是必须的）
<pre><code>1、schema（模式文件）
使用的模式文件都必须标明在根元素&lt;web-app&gt;中，其他元素在&lt;web-app&gt;&lt;/web-app&gt;中
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;web-app version="3.4" 
    xmlns="http://……" 
    xmlns:xsi="http://……"
    xsi:schemaLocation="http://……
        http://……"&gt;
&lt;/web-app&gt;


2、&lt;display-name&gt;Web应用名称&lt;/display-name&gt;

3、&lt;discription&gt;Web应用描述&lt;/disciption&gt;

4、&lt;context-param&gt;上下文参数&lt;/context-param&gt;

5、&lt;filter&gt;过滤器&lt;/filter&gt;

6、&lt;listerner&gt;监听器&lt;/listener&gt;

7、&lt;servlet&gt;servlet是运行在服务器端的小程序&lt;/servlet&gt;

8、&lt;session-config&gt;会话超时配置&lt;/session-config&gt;

9、&lt;welcome-file-list&gt;欢迎文件页&lt;/welcome-file-list&gt;

10、&lt;jsp-config&gt;设置jsp&lt;/jsp-config&gt;


</code></pre>
<hr/>
<h3>2、pom.xml</h3>
全称：Project Object Model，是Maven项目中的文件，使用XML表示，项目的maven坐标，依赖关系，项目授权、项目的url，开发者需要遵循的规则，缺陷管理系统，组织和licenses，配置文件、开发者的信息和角色，以及其他所有的项目相关因素（project必须包含pom.xml文件）
<hr/>
<h3>3、web.xml与pom.xml区别</h3>
pom.xml（必须）：根目录里面（作用于整个项目的一些信息）
web.xml（非必须）：隐藏的（如：webapp里的WEB-INF文件内，写注册的功能，像servlet despatcher filter 等，并都加一个mapping与之对应）
<hr/>
<h3>4、Filter（过滤器）</h3>
通过对过滤器分析，可以知道过滤规则，以及可以最终筛选出未使用过滤器的URL
<pre><code>web.xml中
&lt;filter&gt;
    &lt;filter-name&gt;xsscheck&lt;/filter-name&gt;//名字
    &lt;filter-class&gt;com.anbai.sec.XssFilter&lt;/filter-class&gt;//class
&lt;/filter&gt;
&lt;filter-mapping&gt;
    &lt;filter-name&gt;xsscheck&lt;/filter-name&gt;//名字
    &lt;url-pattern&gt;*.jsp&lt;/url-pattern&gt;//路由
&lt;/filter-mapping&gt;
</code></pre>
<hr/>
<h3>5、框架+组件</h3>
通过了解了开发的框架以及组件以后，可以扩大攻击面
查看配置文件web.xml和外部引用库，确定当前引用框架名称和版本
<pre><code>框架确定：
1、maven（查看pom.xml关键字）
spring-core/ springframework.core    spring框架
struts2-core                         struts2框架
springframework.boot                 srping-boot框架
servlet-api                          原生servlet

2、lib（查看jar包名称）
spring-core/springframework.core    spring框架
struts2-core                        struts2框架
spring-boot                         srping-boot框架
servlet-api                         原生servlet</code></pre>
<pre><code>配置文件：
Struts2     struts.xml
Spring      applicationContext.xml
Spring MVC  spring-mvc.xml
Hibernate   Hibernate.cfg.xml
Mybaits     mybatis-config.xml</code></pre>



### 2、pom.xml

---


### 4、Filter（过滤器）

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

