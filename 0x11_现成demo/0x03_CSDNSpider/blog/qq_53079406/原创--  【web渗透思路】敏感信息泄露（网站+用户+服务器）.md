# 原创
：  【web渗透思路】敏感信息泄露（网站+用户+服务器）

# 【web渗透思路】敏感信息泄露（网站+用户+服务器）

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
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（学者自查）： 
（1）信息泄露示例（√）
（2）泄露方式（√）
（3）泄露危害（√）
（4）泄露挖掘（√）
（5）用户信息泄露（√）
（6）服务器信息泄露（√）


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

[一、信息泄露示例](#%E4%B8%80%E3%80%81%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E7%A4%BA%E4%BE%8B)

[1、示例：](#1.1%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[二、泄露方式](#%E4%BA%8C%E3%80%81%E6%B3%84%E9%9C%B2%E6%96%B9%E5%BC%8F)

[1、原理：](#2.1%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[三、泄露危害](#%E4%B8%89%E3%80%81%E6%B3%84%E9%9C%B2%E5%8D%B1%E5%AE%B3)

[1、危害：](#3.1%E3%80%81%E5%8D%B1%E5%AE%B3%EF%BC%9A)

[ 四、泄露挖掘](#%C2%A0%E5%9B%9B%E3%80%81%E6%B3%84%E9%9C%B2%E6%8C%96%E6%8E%98)

[1、爬虫文件](#1%E3%80%81%E7%88%AC%E8%99%AB%E6%96%87%E4%BB%B6)

[2、目录信息](#2%E3%80%81%E7%9B%AE%E5%BD%95%E4%BF%A1%E6%81%AF)

[3、越权访问](#3%E3%80%81%E8%B6%8A%E6%9D%83%E8%AE%BF%E9%97%AE)

[4、开发注释、js文件](#4%E3%80%81%E5%BC%80%E5%8F%91%E6%B3%A8%E9%87%8A%E3%80%81js%E6%96%87%E4%BB%B6)

[5、错误提示](#5%E3%80%81%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA)

[6、调试信息](#6%E3%80%81%E8%B0%83%E8%AF%95%E4%BF%A1%E6%81%AF)

[7、备份等目录文件](#7%E3%80%81%E5%A4%87%E4%BB%BD%E7%AD%89%E7%9B%AE%E5%BD%95%E6%96%87%E4%BB%B6)

[8、配置不安全](#8%E3%80%81%E9%85%8D%E7%BD%AE%E4%B8%8D%E5%AE%89%E5%85%A8)

[9、版本控制历史](#9%E3%80%81%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E5%8E%86%E5%8F%B2)

[五、用户信息泄露](#%E4%BA%94%E3%80%81%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)

[1、评论处](#1%E3%80%81%E8%AF%84%E8%AE%BA%E5%A4%84)

[2、转账处](#2%E3%80%81%E8%BD%AC%E8%B4%A6%E5%A4%84)

[3、搜索处](#3%E3%80%81%E6%90%9C%E7%B4%A2%E5%A4%84)

[4、个人页面处](#4%E3%80%81%E4%B8%AA%E4%BA%BA%E9%A1%B5%E9%9D%A2%E5%A4%84)

[5、客服处](#5%E3%80%81%E5%AE%A2%E6%9C%8D%E5%A4%84)

[6、上传、数据更新处](#6%E3%80%81%E4%B8%8A%E4%BC%A0%E3%80%81%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0%E5%A4%84)

[7、任意账号重置](#7%E3%80%81%E4%BB%BB%E6%84%8F%E8%B4%A6%E5%8F%B7%E9%87%8D%E7%BD%AE)

[8、接口参数处](#8%E3%80%81%E6%8E%A5%E5%8F%A3%E5%8F%82%E6%95%B0%E5%A4%84)

[9、弱口令](#9%E3%80%81%E5%BC%B1%E5%8F%A3%E4%BB%A4)

[10、第三方平台（如GitHub）](#10%E3%80%81%E7%AC%AC%E4%B8%89%E6%96%B9%E5%B9%B3%E5%8F%B0%EF%BC%88%E5%A6%82GitHub%EF%BC%89)

[11、未删除的敏感文件](#11%E3%80%81%E6%9C%AA%E5%88%A0%E9%99%A4%E7%9A%84%E6%95%8F%E6%84%9F%E6%96%87%E4%BB%B6)

[六、服务器信息泄露](#%E5%85%AD%E3%80%81%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)

[1、XML文件](#1%E3%80%81XML%E6%96%87%E4%BB%B6)

[2、上传文件](#2%E3%80%81%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)

[3、中间件](#3%E3%80%81%E4%B8%AD%E9%97%B4%E4%BB%B6)

[4、报错信息](#4%E3%80%81%E6%8A%A5%E9%94%99%E4%BF%A1%E6%81%AF)

---


> 
<h2> <img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>助你一臂之力  </h2>
<h3>📋问题1：有没有完整信息泄露相关的靶场进行练习？</h3>
🎯[【BP靶场portswigger-服务端6】信息泄露漏洞-5个实验（全）<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=MBR7"/>https://blog.csdn.net/qq_53079406/article/details/128544645?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/128544645?spm=1001.2014.3001.5501)


> 
<h2>一、信息泄露示例</h2>
<h3>1、示例：</h3>
查看其他用户私密数据、个人身份信息等敏感数据
有关网站技术细节/架构(如源代码等)
robots.txt泄露网站隐藏目录,文件
站点的备份文件未删除导致的泄露
在错误消息中泄露数据库表,字段等敏感数据
泄露在源代码中泄露数据库账号密码等
(GitHub)网站某些程序的细微差别提示是否存在某些资源、相似的程序的套用
……


> 
<h2>二、泄露方式</h2>
<h3>1、原理：</h3>
1、敏感数据不慎泄露给浏览该网站信息用户
2、攻击者通过恶意的交互从网站获得数据
3、第三方存储机构
4、历史信息
5、社工


> 
<h2>三、泄露危害</h2>

<h3>1、危害：</h3>
1、利于攻击者进行下一步的攻击
2、数据被非法处理
3、……


> 
<h2>四、泄露挖掘</h2>
<h3>1、爬虫文件</h3>
1、如/robots.txt, /sitemap.xml
会列出特定目录不让爬虫爬取（在bp的sitemap里可能找不到，需手动测试）
2、Sitemap 使用XML格式来记录整个网站的信息并供Google读取（哪些网页最重要，以及更改频率），是对原来robots.txt的扩展，使搜索引擎能更快更全面的收录网站的内容
<hr/>
<hr/>
<h3>2、目录信息</h3>
1、由于网站存在配置缺陷，存在目录可浏览，致使网站很多隐私文件与目录泄露（如备份文件、配置文件等），攻击者可对此进一步的利用
2、自动目录列表/索引是一个Web 服务器功能，如果正常的基本文件（index.html/home.html/​默认）列出请求目录中的所有文件。Web服务器隐藏默认情况下文件夹的内容。如果没有index.html或 index.php文件，则会显示“403 Forbidden”错误
3、证明存在此漏洞方法：①访问Web应用存在的一些目录，如果返回文件列表信息②web扫描器③body:index of


<hr/>
<hr/>

<h3>3、越权访问</h3>
1、个人中心、个人资料、我的帐户等页面会包含敏感信息（如email，电话号码等）
当存在逻辑缺陷时，可能使攻击者可以越权访问其他用户的数据
2、如：GET /user/personal-info?user=
修改user参数，越权访问
<hr/>
<hr/>
<h3>4、开发注释、js文件</h3>
F12：测试阶段，可能在HTML中写有关敏感信息的注释（如测试账号），部署到生成文件前，通常会删除
JS文件：可能包含目录文件、接口文件、秘钥、加密算法等
<hr/>
<hr/>

<h3>5、错误提示</h3>
1、错误消息，有的会有提示，有的关闭了提示，靠自己分析不同测试时候页面差别（如明显差别就是字节）
2、当有提醒时，可能会提示应该输入什么消息、或数据类型，利于攻击者更加准确进行测试
3、详细的错误消息，可以提供有关网站使用的技术信息（如数据库类型、模板类型、服务器版本号、开源框架信息等），进一步针对相关信息，查找常见配置错误或危险的默认设置
<hr/>
<hr/>
<h3>6、调试信息</h3>
调试时，许多网站会生成自定义错误消息和日志，包含应用程序行为的大量信息（可能包含用于发起攻击的重要信息，如可控变量的值、中间件的主机名和登录凭据、服务器文件和目录、加密密钥等）
<hr/>
<hr/>
<h3>7、备份等目录文件</h3>
1、源代码访问权限（源代码中可能有敏感数据，如账号密码、GitHub的开源项目等）
2、使用vim编辑的时候，vim会在被编辑文件同一目录下，创建一个名为filename.swp的文件，记录我们的动作
3、index.phps、.bak、/tz.php等形式
4、/.git（GitHack）
5、/.svn（Seay-SVN）
6、域名解析记录
7、访问/editor
8、数字的临界值
9、查看/db/db.mdb将文件后缀改为txt打开（mdb文件是早期的asp+access架构的数据库文件）
10、备份的sql文件会泄露敏感信息，还提示了backup.sql
<hr/>
<hr/>
<h3>8、配置不安全</h3>
网站扩展的第三方技术（关注使用的第三方相关的配置权限）
<hr/>
<hr/>
<h3>9、版本控制历史</h3>
1、简述：
开发一般都是使用某种形式的版本控制系统（如Git、SVN）
一般通过目录扫描发现，或者手动在URL后测试
若配置不当，可能会将.git、.svn文件直接部署上线，从而导致泄露
<hr/>
2、git版本控制
利用工具：GitHack
默认Git项目将其所有版本控制数据存储在.git文件夹中，虽无法获得完整的源代码， 但可以阅读更改的代码段，这仍然可能存在敏感数据
若可直接访问/.git，并下载到本地用Git打开，以访问网站的版本控制历史记录
<hr/>
3、svn版本控制
利用工具：Seay-SVN、dvcs-ripper工具中的rip-svn.pl脚本进行clone


---


### 2、目录信息

---


---


### 4、开发注释、js文件

---


---


### 6、调试信息

---


---


### 8、配置不安全

---


---


> 
<h2>五、用户信息泄露</h2>
<h3>1、评论处</h3>
1、如显示用户手机号或邮箱等，中间的一段数字会被加密（1999********999）
若加密不当，抓包查看返回包，可能直接显示明文，或意外找到其他参数
2、评论区互动交流（如追加评论，商家回复，@功能，搜索引擎的爬虫，及秒杀成功等阶段）
通过抓包进行分析
<hr/>
<h3>2、转账处</h3>
1、如建行转账时，需要输入对方的姓名，然后在数据库中进行验证
类似的验证地方通过抓包，看是否会泄露用户的其他信息（如电话等）
2、历史转账记录等地方
抓包分析，看是否会泄露
<hr/>
<h3>3、搜索处</h3>
1、看搜索是否会意外搜索到用户信息
<hr/>
<h3>4、个人页面处</h3>
1、若存在可以返回敏感的信息，则对参数进行修改，尝试越权访问
<hr/>
<h3>5、客服处</h3>
1、社工
<hr/>
<h3>6、上传、数据更新处</h3>
1、常见的有头像上传，查看头像链接，会有一个URL地址（还有上传证件等）
若没有进过特别复制的处理，还是有可能进行任意查看（服务器URL地址泄露）
2、修改资料，如地址等
尝试越权，当权限未处理好，可能有任意用户查看
在最后一步，修改用户名，尝试越权修改
3、子账号等下级处
通过对下级账号处修改ID等参数，可能有任意账户查看
4、如下单处
抓包修改账号参数，可能就可能使用别人账号下单，可能就可以查看别人的用户信息
5、……
<hr/>
<h3>7、任意账号重置</h3>
明显了，都能任意密码重置了，岂不是可以泄露任意用户信息
<hr/>
<h3>8、接口参数处</h3>
最容易想到的就是修改ID参数
<hr/>
<h3>9、弱口令</h3>
都弱口令，还有数据安全可言？
<hr/>
<h3>10、第三方平台（如GitHub）</h3>
存放着用户的信息等
<hr/>
<h3>11、未删除的敏感文件</h3>
存放有敏感信息的文件，未被删除就上线了（如.xml、.git、.svn、.txt、.doc、.sql等）


### 2、转账处

---


### 4、个人页面处

---


### 6、上传、数据更新处

---


### 8、接口参数处

---


### 10、第三方平台（如GitHub）

---


> 
<h2>六、服务器信息泄露</h2>
<h3>1、XML文件</h3>
一些XML文件可能未完全删除，可能泄露很多敏感信息
<hr/>
<h3>2、上传文件</h3>
服务器URL地址信息泄露
<hr/>
<h3>3、中间件</h3>
Apache Tomcat、Struts2、CMS、zabbix、Nginx等存在的配置等问题
<hr/>
<h3>4、报错信息</h3>
泄露敏感路径


### 2、上传文件

---


### 4、报错信息

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

