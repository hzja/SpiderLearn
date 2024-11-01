# 原创
：  【代码审计-PHP】基于Thinkphp框架开发的

# 【代码审计-PHP】基于Thinkphp框架开发的

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
（1）Thinkphp基本结构（√）
（2）基本函数（√）
（3）危险函数（√）
（4）已有漏洞（√）
（5）漏洞检测工具（√）


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

[ 一、Thinkphp基本结构](#%C2%A0%E4%B8%80%E3%80%81Thinkphp%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84)

[1、框架目录](#1%E3%80%81%E6%A1%86%E6%9E%B6%E7%9B%AE%E5%BD%95)

[2、判断框架、版本](#2%E3%80%81%E5%88%A4%E6%96%AD%E6%A1%86%E6%9E%B6%E3%80%81%E7%89%88%E6%9C%AC)

[3、入口文件](#3%E3%80%81%E5%85%A5%E5%8F%A3%E6%96%87%E4%BB%B6)

[4、资源文件](#4%E3%80%81%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6)

[5、调试开关](#5%E3%80%81%E8%B0%83%E8%AF%95%E5%BC%80%E5%85%B3)

[6、URL路由](#6%E3%80%81URL%E8%B7%AF%E7%94%B1)

[二、基本函数](#%E4%BA%8C%E3%80%81%E5%9F%BA%E6%9C%AC%E5%87%BD%E6%95%B0)

[1、请求](#1%E3%80%81%E8%AF%B7%E6%B1%82)

[2、交互：](#2%E3%80%81%E4%BA%A4%E4%BA%92%EF%BC%9A)

[3、响应：](#3%E3%80%81%E5%93%8D%E5%BA%94%EF%BC%9A)

[三、危险函数](#%E4%B8%89%E3%80%81%E5%8D%B1%E9%99%A9%E5%87%BD%E6%95%B0)

[四、已有漏洞](#%E5%9B%9B%E3%80%81%E5%B7%B2%E6%9C%89%E6%BC%8F%E6%B4%9E)

[五、漏洞检测工具](#%E4%BA%94%E3%80%81%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B%E5%B7%A5%E5%85%B7)

[六、工具](#%E5%85%AD%E3%80%81%E5%B7%A5%E5%85%B7)

---


> 
<h2> 一、Thinkphp基本结构</h2>
<h3>1、框架目录</h3>

<pre><code>www  WEB部署目录（或者子目录）
├─application           应用目录
│  ├─common             公共模块目录（可以更改）
│  ├─module_name        模块目录
│  │  ├─common.php      模块函数文件
│  │  ├─controller      控制器目录
│  │  ├─model           模型目录
│  │  ├─view            视图目录
│  │  ├─config          配置目录
│  │  └─ ...            更多类库目录
│  │
│  ├─command.php        命令行定义文件
│  ├─common.php         公共函数文件
│  └─tags.php           应用行为扩展定义文件
│
├─config                应用配置目录
│  ├─module_name        模块配置目录
│  │  ├─database.php    数据库配置
│  │  ├─cache           缓存配置
│  │  └─ ...            
│  │
│  ├─app.php            应用配置
│  ├─cache.php          缓存配置
│  ├─cookie.php         Cookie配置
│  ├─database.php       数据库配置
│  ├─log.php            日志配置
│  ├─session.php        Session配置
│  ├─template.php       模板引擎配置
│  └─trace.php          Trace配置
│
├─route                 路由定义目录
│  ├─route.php          路由定义
│  └─...                更多
│
├─public                WEB目录（对外访问目录）
│  ├─index.php          入口文件
│  ├─router.php         快速测试文件
│  └─.htaccess          用于apache的重写
│
├─thinkphp              框架系统目录
│  ├─lang               语言文件目录
│  ├─library            框架类库目录
│  │  ├─think           Think类库包目录
│  │  └─traits          系统Trait目录
│  │
│  ├─tpl                系统模板目录
│  ├─base.php           基础定义文件
│  ├─convention.php     框架惯例配置文件
│  ├─helper.php         助手函数文件
│  └─logo.png           框架LOGO文件
│
├─extend                扩展类库目录
├─runtime               应用的运行时目录（可写，可定制）
├─vendor                第三方类库目录（Composer依赖库）
├─build.php             自动生成定义文件（参考）
├─composer.json         composer 定义文件
├─LICENSE.txt           授权说明文件
├─README.md             README 文件
├─think                 命令行入口文件</code></pre>

<hr/>
<h3>2、判断框架、版本</h3>
在源码中搜Thinkphp，如果有就是Thinkphp框架
搜THINK_VERSION可以看到相应的版本信息
<img alt="" height="860" src="https://img-blog.csdnimg.cn/ec14bf288fe54ac3882154a9a24365d8.png" width="891"/>​
<hr/>
<h3>3、入口文件</h3>
关键词APP_PATH
定义应用目录、框架入口文件
<img alt="" height="845" src="https://img-blog.csdnimg.cn/89b4525472c24df792769c16d3f29ae3.png" width="1200"/>​

<img alt="" height="847" src="https://img-blog.csdnimg.cn/25c44795490946f6aaff2e58053c62c5.png" width="1200"/>​
 <img alt="" height="452" src="https://img-blog.csdnimg.cn/18d0134605a44a7c8f5d68b3f3ea31e8.png" width="1030"/>​

按住Ctrl再点击这个目录，就会在左边目录栏跳转到这个目录位置<img alt="" height="777" src="https://img-blog.csdnimg.cn/e8644c56e2d14f2883a68fd7aad0ec63.png" width="1018"/>​
<hr/>
<h3>4、资源文件</h3>
均放在public的目录下,找不到的话会爆路径错误情况

<pre><code>public
├─index.php       应用入口文件
├─static		  静态资源目录   
│  ├─css            样式目录
│  ├─js             脚本目录
│  └─img            图像目录
│─router.php      快速测试文件
└─.htaccess       用于apache的重写</code></pre>

<hr/>
<h3>5、调试开关</h3>
审计的时候，需要将false改为true
如果直接搜debug的话，可能会搜到convention.php上的debug

<pre><code>  默认情况下：
    // 应用调试模式
    'app_debug'              =&gt; false,
    // 应用Trace
    'app_trace'              =&gt; false,
</code></pre>

<img alt="" height="426" src="https://img-blog.csdnimg.cn/248d13cb748f400d977dc1a4e945e68f.png" width="1126"/>​
<hr/>
<h3>6、URL路由</h3>

<pre><code>①方法/变量值进行传参
http://domainName/index.php/模块/控制器/操作/方法/变量值

eg:访问www.xxx.com/index.php/index/index/index
为application目录下的index模块下的从contraller目录下的index文件下的index函数

②变量传参
http://tp5.com/index.php?s=/index/Index/index
</code></pre>




### 2、判断框架、版本

---


### 4、资源文件

---


### 6、URL路由

---


---


## 二、基本函数

> 
<h3>1、请求</h3>
Request对象进行调用
获取请求变量
利用：寻找用户可控的变量（且传入给有一定功能的函数）
<hr/>
1、param()
获取所有请求变量
param('指定的函数对象','未获取到时的默认值','对于获取到的值的处理函数')
$request-&gt;param()：用于获取所有的变量（优先级：路由变量 &gt; 当前请求变量($_POST) &gt; $_GET变量
<hr/>
2、get()
获取$_GET变量
$request-&gt;get('指定的函数对象')<br/> echo input('get.函数对象') 
<hr/>
3、<br/> post()获取$_POST
file()获取$_FILE
ip()获取请求IP
method()获取请求方法
pathInfo()获取控制器和方法名的路径
rootInfo()获取路由


---


> 
<h3>2、交互：</h3>
配置：
1、代码过滤
2、过滤器过滤
3、模块过滤
4、预编译，使用占位符
……
<hr/>
利用：
1、判断代码绕过条件
2、过滤器漏洞
3、寻找未使用过滤模块的地方
4、不安全的过滤
……


> 
<h3>3、响应：</h3>
1、配置自动输出
配置：在config.ph中设置default_return_type更改默认返回类型
利用：寻找模板存在的漏洞、寻找未引用模板的目录
<hr/>
2、函数输出
配置：
return 格式类型json($data,201,['set_cookie'=&gt;'xxxx'])
利用：寻找用户可控值
<hr/>
3、重定向
eg:
if($userid&gt;=0){$this-&gt;success("提示语","user跳转页面")}<br/> else{ $this-&gt;error("错误提示语")}
利用：看是否能利用重定向漏洞，跳转到其他不安全地方


---


---


---


> 
<h2>三、危险函数</h2>
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


---


---


> 
<h2>四、已有漏洞</h2>
针对未公开的漏洞
根据描述寻找到未公开的漏洞点
<img alt="" height="896" src="https://img-blog.csdnimg.cn/2e3652eab81f4f38bed8d8c15de1c155.png" width="837"/>​



---


---


> 
<h2>五、漏洞检测工具</h2>
针对已公开的漏洞
大佬集成了一个工具箱，可以关注公众号以后免费下载
<img alt="" height="991" src="https://img-blog.csdnimg.cn/1d5bffeb72214edea81eb6e248e9b9e8.png" width="1200"/>​
 <img alt="" height="739" src="https://img-blog.csdnimg.cn/9424cdf48daa48ad984486710808037a.png" width="982"/>​



---


---


> 
<h2>六、工具</h2>
Seay
RIPS
CheckMarx
Fortify
VCG
Kunlun-M


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

