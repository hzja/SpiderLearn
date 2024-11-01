# 原创
：  【web渗透思路】任意账号的注册、登录、重置、查看

# 【web渗透思路】任意账号的注册、登录、重置、查看

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
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： <br/> （1）任意用户注册（√）
（2）任意用户登陆（√）
（3）任意账号重置（√）
（4）任意用户查看（√）


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

[一、任意用户注册](#%E4%B8%80%E3%80%81%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E6%B3%A8%E5%86%8C)

[1.未验证邮箱/手机号](#1.%E6%9C%AA%E9%AA%8C%E8%AF%81%E9%82%AE%E7%AE%B1%2F%E6%89%8B%E6%9C%BA%E5%8F%B7)

[2、不安全验证邮箱/手机号](#2%E3%80%81%E4%B8%8D%E5%AE%89%E5%85%A8%E9%AA%8C%E8%AF%81%E9%82%AE%E7%AE%B1%2F%E6%89%8B%E6%9C%BA%E5%8F%B7)

[3.批量注册](#3.%E6%89%B9%E9%87%8F%E6%B3%A8%E5%86%8C)

[4.个人信息伪造](#4.%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%E4%BC%AA%E9%80%A0)

[5.前端验证审核绕过](#5.%E5%89%8D%E7%AB%AF%E9%AA%8C%E8%AF%81%E5%AE%A1%E6%A0%B8%E7%BB%95%E8%BF%87)

[6.用户名覆盖](#6.%E7%94%A8%E6%88%B7%E5%90%8D%E8%A6%86%E7%9B%96)

[二、任意用户登录](#%E4%BA%8C%E3%80%81%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95)

[1、万能密码](#1%E3%80%81%E4%B8%87%E8%83%BD%E5%AF%86%E7%A0%81)

[2、验证码、密码回显](#2%E3%80%81%E9%AA%8C%E8%AF%81%E7%A0%81%E3%80%81%E5%AF%86%E7%A0%81%E5%9B%9E%E6%98%BE)

[3、登录检测不安全](#3%E3%80%81%E7%99%BB%E5%BD%95%E6%A3%80%E6%B5%8B%E4%B8%8D%E5%AE%89%E5%85%A8)

[三、任意账号重置](#%E4%B8%89%E3%80%81%E4%BB%BB%E6%84%8F%E8%B4%A6%E5%8F%B7%E9%87%8D%E7%BD%AE)

[1、重置账号名](#1%E3%80%81%E9%87%8D%E7%BD%AE%E8%B4%A6%E5%8F%B7%E5%90%8D)

[2、验证码](#2%E3%80%81%E9%AA%8C%E8%AF%81%E7%A0%81)

[3、MVC数据对象自动绑定](#3%E3%80%81MVC%E6%95%B0%E6%8D%AE%E5%AF%B9%E8%B1%A1%E8%87%AA%E5%8A%A8%E7%BB%91%E5%AE%9A)

[4、Unicode字符处理](#4%E3%80%81Unicode%E5%AD%97%E7%AC%A6%E5%A4%84%E7%90%86)

[四、任意用户查看](#%E5%9B%9B%E3%80%81%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E6%9F%A5%E7%9C%8B)

[1、cookie未鉴权](#1%E3%80%81%E5%8F%82%E6%95%B0%E4%BF%AE%E6%94%B9)

[2、cookie鉴权](#2%E3%80%81cookie%E9%89%B4%E6%9D%83)

[2、接口中参数](#2%E3%80%81%E6%8E%A5%E5%8F%A3%E4%B8%AD%E5%8F%82%E6%95%B0)

---


> 
<h2>一、任意用户注册</h2>
<h3>1.未验证邮箱/手机号</h3>
情景：应用为了方便用户记录用户名，使用邮箱和手机号作为用户名（因此很多应用在注册的时候就要求用户填写，多数时候都会给用户发送激活信息，激活后才能登录）
缺陷：
1、未审核邮箱/手机号是否有效（及未发送验证信息），从而实现任意注册账号
2、未验证数据库中是否已经存在相同的用户名（导致同一账号，有2个密码，且用户数据产生读取问题）
<hr/>
<h3>2、不安全验证邮箱/手机号</h3>
用户注册邮箱/手机号提交后，会通过发验证码等方法对其真实性进行验证
缺陷：
1、返回的验证码：验证码信息会隐藏在返回包中，或hidden属性隐藏，或者是可以伪zao该信息，劫chi到验证信息
2、分布验证/多步填写等情况：第一步填写的时候验证完成以后，后面并未对账号进行再次验证，通过修改数据包中已验证的邮箱/手机
3、验证未绑定：使用自己邮箱/手机获取验证码后，在其他账号上使用
<hr/>

<h3>3.批量注册</h3>
（提示：危害不足）
通常由于无验证码或者验证码不安全，再对用户名进行爆破即可
<hr/>

<h3>4.个人信息伪造</h3>
（提示：有的行业会危害不足，防沉迷可能不一样）
需填写身份证等信息，可任意构造绕过身份证与姓名（一般网站危害不足）
如果是防沉迷系统存在此类问题（危害应该足了）

<hr/>
<h3>5.前端验证审核绕过</h3>
1、任意填写注册信息，服务器会对信息进行审核，并通过返回状态给前端判断（如检测是否存在恶意标签等，对返回的状态可修改绕过）
2、步骤
使用正常账号或合规操作执行，拦截返回信息（判断信息）
使用需要绕过检测的操作，并将服务器返回判断信息替换为正确时的
<hr/>

<h3>6.用户名覆盖</h3>
未对数据库中的账号进行核对是否已经存在
利用地方：注册账号、修改个人信息


### 2、不安全验证邮箱/手机号

---


### 4.个人信息伪造

---


### 6.用户名覆盖

> 
<h2>二、任意用户登录</h2>
<h3>1、万能密码</h3>
对万能密码需要有一定的了解，并不是真的万能
有时候也得考虑
字符型 or 数值型
单引号 or 双引号
<pre><code>asp aspx万能密码

1：  "or "a"="a
2：  '.).or.('.a.'='.a 
3：  or 1=1--
4：  'or 1=1--
5：  a'or' 1=1--
6：  "or 1=1--
7：  'or.'a.'='a
8：  "or"="a'='a
9：  'or''='
10： 'or'='or'
11： admin'or 1=1#

</code></pre>
<pre><code>PHP万能密码

admin'/*
密码*/'

'or 1=1/*
"or "a"="a
"or 1=1--
"or"="
"or"="a'='a
"or1=1--
"or=or"
''or'='or'
') or ('a'='a
'.).or.('.a.'='.a
'or 1=1
'or 1=1--
'or 1=1/*
'or"="a'='a
'or' '1'='1'
'or''='
'or''=''or''='
'or'='1'
'or'='or'
'or.'a.'='a
'or1=1--
1'or'1'='1
a'or' 1=1--
a'or'1=1--
or 'a'='a'
or 1=1--
or1=1--</code></pre>
<pre><code>jsp 万能密码

1'or'1'='1
admin' or 1=1/*</code></pre>
<hr/>
<h3>2、验证码、密码回显</h3>
1、可以拦截到验证码（或者验证固定）
2、通过修改user_id，密码会返回在数据包中（至少是加密的）
<hr/>
<h3>3、登录检测不安全</h3>
1、如下传入参数后登录成功（具体参数可能需要代码审计，或通过已有账号抓包分析）
http://127.0.0.1/vlcms/index.php?s=/member/res_login/
POST:uid=60
2、再访问如下主页，判断是否真的登录成功
http://127.0.0.1/vlcms/index.php?s=/member/


### 2、验证码、密码回显

---


> 
<h2>三、任意账号重置</h2>
<h3>1、重置账号名</h3>
登录状态下，点击修改密码，用户名一般不可修改
1、如果可以通过修改前端的代码，让用户名变为可以修改的状态
2、或者在数据包传输过程中修改用户名
3、如果设置新密完全是由前端 js，基于应答状态码决定（即校验通过时服务端并未向客户端 set - cookie），那么可以修改状态码
<hr/>
<h3>2、验证码</h3>
1、验证码在返回包中回显
2、验证码未绑定、无效
3、验证码在本地进行验证
<hr/>
<h3>3、MVC数据对象自动绑定</h3>
邮箱重置密码/手机号码重置密码
如果请求中没有明显的身份标识，可增加参数值来测试是否存在MVC数据对应自动绑定漏洞（如增加email参数，并用自己邮箱作为参数值，看是否能收到密码重置链接）


<hr/>
<h3>4、Unicode字符处理</h3>
（一个大佬的方法）
1、情景：通过URL如/forget-password?email=发送邮件的方法重置密码
2、缺陷：输入邮箱xxxx@gmáil.com会被规范化为xxxx@gmail.com
3、原理：gmáil.com的punnycode是xn--gmil-6na.com，所以目标站点就会把xxxx@gmail.com用户的重置密码链接发送到邮箱xxxx@xn--gmil-6na.com中。并不需要注册gmáil.com域名，并搭建邮件服务器才能完成攻击，bp插件collabrator everwhere的collobrator client就可以实现
4、工具：bp提供了一个在公网能够访问到的域名burpcollaborator.net，并且在使用collabrator的时候会随机生成一个二级域名供我们使用，比如xxxxxx.burpcollaborator.net
5、验证漏洞：重置密码接口处输入含有Unicode字符的邮箱地址：xxxx@gmáil.com.xxxxxx.burpcollaborator.net，如果目标存在漏洞，就可以在collobrator client上看到目标站点发送给我们的xxxx@gmail.com用户的重置密码链接了



### 2、验证码

---


### 4、Unicode字符处理

> 
<h2>四、任意用户查看</h2>
<h3>1、cookie未鉴权</h3>
修改参数，如User _id等与账号一一对应的编号
<hr/>
<h3>2、cookie鉴权</h3>
钓yu等其他方法获取到其他用户cookie，替换cookie
<hr/>
<h3>2、接口中参数</h3>
情景：&amp;parameters ={"User _Id":"加密后的值"}接口，返回了User _Id所对应用户的数据
利用：解密 加密值（一般不可能），所以需要在大量数据包中找到在前端带入后，服务器返回数据中被加密后的值（这就要一眼看出加密值的特点，不然就算在面前也……）


### 2、cookie鉴权

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

