# 原创
：  【代码审计-PHP】审计方法、敏感函数、功能点

# 【代码审计-PHP】审计方法、敏感函数、功能点

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
（1）软件分析（√）
（2）手动分析（√）
（3）工具（√）


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

[一、软件分析](#%E4%B8%80%E3%80%81%E8%BD%AF%E4%BB%B6%E5%88%86%E6%9E%90)

[二、手动分析](#%E4%BA%8C%E3%80%81%E6%89%8B%E5%8A%A8%E5%88%86%E6%9E%90)

[方法一：静态分析](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E9%9D%99%E6%80%81%E5%88%86%E6%9E%90)

[方法二：动态分析](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%8A%A8%E6%80%81%E5%88%86%E6%9E%90)

[三、工具](#%E4%B8%89%E3%80%81%E5%B7%A5%E5%85%B7)

---


> 
<h2>一、软件分析</h2>
seay自动代码审计
数据库监控脚本


## 二、手动分析

> 
<h3>方法一：静态分析</h3>
第一步：危险函数
第二步：函数的判断语句分析
第三步：函数值的传递过程
第四步：传递过程中是否有判断缺陷地方
第五步：传递过程中是否有函数值可控的地方

<table border="1" cellpadding="1" cellspacing="1"><tbody>|类型|危险函数
|SQL|select、insert、update、POST、$REQUEST、mysql_query、mysqli
|文件上传|$_FILES、move_uploaded_file、!file_exists、type="file"
|文件读写|file_get_contents()、file_put_contents()、move_uploaded_file()、highlight_file()、fopen()、readfile()、fread()、fgetss()、fgets()、parse_ini_file()、show_source()、file()、rename()
|文件删除|unlink &amp; delete()、rmdir()
|文件包含|include、include_once、require、require_once
|命令执行|system()、exec()、shell_exec()、passthru()、pcntl_exec()、popen()、proc_open()
|代码执行|eval()、assert()、preg_replace()、call_user_func()、call_user_func_array()、array_map()
|xss|print、print_r、echo、printf、sprintf、die、var_dump、var_export
|变量覆盖关|$$、parse_str()、extract()、importrequestvariables()
|反序列化|serialize()、unserialize()、__construct__
|……|……
</tbody></table>


> 
<h3>方法二：动态分析</h3>
第一步：可能出现问题的功能点
第二步：phpStudy + PhpStorm + XDebug动态调试
第三步：发现漏洞
<table border="1" cellpadding="1" cellspacing="1"><tbody>|功能
|文件上传|解析执行
|查询|SQL注入
|密码找回|逻辑漏洞、重置任意用户账号密码、短信验证码劫持、用户邮箱劫持篡改
|登录|暴力破解、SQL注入、逻辑、越权
|评论、资料|XSS
|个人中心|越权、遍历
|注册|任意账号注册、存储型xss
|后台管理|密码泄露、目录遍历
|……|……
</tbody></table>


> 
<h2>三、工具</h2>

Seay 


RIPS 


CheckMarx 


Fortify 


VCG 


Kunlun-M



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

