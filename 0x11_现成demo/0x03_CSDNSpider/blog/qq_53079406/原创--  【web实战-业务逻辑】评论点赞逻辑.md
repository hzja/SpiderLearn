# 原创
：  【web实战-业务逻辑】评论点赞逻辑

# 【web实战-业务逻辑】评论点赞逻辑

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
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点： 
（1）重放数据包（√）
（1）可能会验证cookie中的身份参数（√）
（1）可能会有特殊的逻辑，如再次点击会取消点赞（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|业务逻辑漏洞|博文|目标|状态
|评论、点赞|[【web实战-业务逻辑】评论点赞逻辑](https://blog.csdn.net/qq_53079406/article/details/128095877)|1、学习各种验证评论点赞成功的逻辑|已发布
|短信轰炸|[【web实战-业务逻辑】短信轰炸逻辑](https://blog.csdn.net/qq_53079406/article/details/128103256)|2、对于短信轰炸的防护机制的绕过|已发布
|并发|2023将公开实战笔记，敬请期待|——|——
|爆破|2023将公开实战笔记，敬请期待|——|——
|csrf|2023将公开实战笔记，敬请期待|——|——
|xss|2023将公开实战笔记，敬请期待|——|——
|越权操作|2023将公开实战笔记，敬请期待|——|——
|信息泄露|2023将公开实战笔记，敬请期待|——|——
|组合漏洞|2023将公开实战笔记，敬请期待|——|——
</tbody></table>


---


**目录** 

[点赞逻辑一：](#%E7%82%B9%E8%B5%9E%E9%80%BB%E8%BE%91%E4%B8%80%EF%BC%9A)

[第一步：找关键](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%89%BE%E5%85%B3%E9%94%AE)

[第二步：猜测逻辑](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%B5%8B%E9%80%BB%E8%BE%91)

[第三步：结论](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%BB%93%E8%AE%BA)

[第四步：归类](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%BD%92%E7%B1%BB)

[点赞逻辑二：](#%C2%A0%E7%82%B9%E8%B5%9E%E9%80%BB%E8%BE%91%E4%BA%8C%EF%BC%9A)

[第一步：找关键](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%89%BE%E5%85%B3%E9%94%AE)

[第二步：猜测逻辑](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%B5%8B%E9%80%BB%E8%BE%91)

[第三步：结论](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%BB%93%E8%AE%BA)

[第四步：归纳](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%BD%92%E7%BA%B3)

[点赞逻辑三：](#%C2%A0%E7%82%B9%E8%B5%9E%E9%80%BB%E8%BE%91%E4%BA%8C%EF%BC%9A)

[第一步：找关键](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%89%BE%E5%85%B3%E9%94%AE)

[第二步：猜测逻辑](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%8C%9C%E6%B5%8B%E9%80%BB%E8%BE%91)

[第三步：结论](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%BB%93%E8%AE%BA)

---


## 点赞逻辑一：

> 
<h3>第一步：找关键</h3>
先把关键函数最终推测出的结果放出来：
comment_id=为帖子id（且有指定位数）
status=推测为业务相关的
callback=__jp8推测为指定返回服务器的ip
（其余不影响业务的无用关键函数已被删除）
serviceToken=鉴别身份的

再次点赞，就为-1，即取消点赞




> 
<h3>第二步：猜测逻辑</h3>
（此处的基本逻辑：可以点赞，也可以取消点赞，听说你想取消别人带赞？）
假设：comment_id=为用户id，尝试批量单一账号点赞
确实全部成功

回到点赞页面查看（就加一）
直接可以推断出comment_id=为帖子的id
点赞不同的帖子，抓到的id不同，验证了猜想
（找关键字时候发现ID不同就应该引起注意的）
##所有帖子点赞一遍？搞笑了一波，请见谅




> 
<h3>第三步：结论</h3>
记录点赞次数的
是通过鉴别serviceToken=值
一个serviceToken=只能点赞一个，且其值也不好继续整下去了
整不了了，跑了


> 
<h3>第四步：归类</h3>
（此系统中与此类似的逻辑）
踩一脚功能
这里不能针对一个一直踩，所以无危害了
一时不知道说什么，那就遍历id把所有帖子都踩一脚




---


---


## 点赞逻辑二：

> 
<h3>第一步：找关键</h3>
先把关键函数最终推测出的结果放出来：
postId=为发帖人的id
commentId=为帖子id（且有指定位数，这里被加密了，难搞）
miui_vip_serviceToken=鉴别身份的
cUserId=鉴定用户的






> 
<h3>第二步：猜测逻辑</h3>
（此处的基本逻辑：只能点赞一次，再点赞将被识别为重复点赞）


假设：修改id值，绕过检测？（难搞，看见直接放弃，cookie了里面有身份鉴别，还有id鉴别）
改postId=提示评论与id不匹配
所以为发帖人id
现在唯一可以利用的就是cookie里面的id，能否替换了
能知道别人的id，但是不知道加密方法，或破解加密算法




> 
<h3>第三步：结论</h3>
记录点赞次数的
是通过cookie中的
miui_vip_serviceToken、cUserId
整不了了，再跑了


> 
<h3>第四步：归纳</h3>
（此系统中与此类似的逻辑）
投票




---


---


## 点赞逻辑三：

> 
<h3>第一步：找关键</h3>
测试了一下，没啥可以操作的关键参数








> 
<h3>第二步：猜测逻辑</h3>
尝试对其进行重放
发现可以一直重放


 一段时间后出现提示操作频繁（但10s左右又可以继续重放）
（经测试一分钟可以刷赞70次）








> 
<h3>第三步：结论</h3>
同一账号可以通过重放进行点赞
为鉴别点赞的用户身份，并进行限制



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

