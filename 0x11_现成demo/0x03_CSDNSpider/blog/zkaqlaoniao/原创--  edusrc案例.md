# 原创
：  edusrc案例

# edusrc案例

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


### 一、序

---


1、许久没有发文章了，就随便发发文章水一水，因为是实战文章，使用码打得厚一点，希望理解。由于本文章技术含量较低，大佬们手下留情。

2、刚开始挖edu的站，我也是感觉挖不出东西，但是后来挖着挖着就感觉其实也没那么难挖，所以挖洞不能至于理论，还得实践总结出自己的经验。

### 二、案例1

---


1、这个站是一个OA系统，当时真的是js审计，测注入，测目录，测端口，修改返回包，最后一个admin和123456就给我进去了，最后人傻了。<img alt="" height="614" src="https://img-blog.csdnimg.cn/4b18800d61e544b7a36353d3ccd9f2c4.png" width="1080"/><img alt="" height="570" src="https://img-blog.csdnimg.cn/43d08c7d697d48668b2a5d9ac286ffa6.png" width="1080"/>

2、所以不要以为弱口令很少，在edu里弱口令还是很常见的，毕竟弱口令就是0day嘛。

### 三、案例2

---


1、这个站之前挖了一个批量弱口令，真的是想不到的漏洞，当时测试了很久，最后是直接去找了他们学校领导的名字，密码123456直接就进去了，直接导致，全校领导信息泄露<img alt="" height="544" src="https://img-blog.csdnimg.cn/b67007f4b6194791825fe80da02e2581.png" width="1080"/><img alt="" height="626" src="https://img-blog.csdnimg.cn/e63bb68c7144427eaf16651f8f50b596.png" width="1080"/><img alt="" height="1061" src="https://img-blog.csdnimg.cn/f99e5a3c9f3e4cd789494b776c17f844.png" width="1080"/>

### 四、案例3

1、edu的证书站，证书刚上没多久，一堆人跑过去挖，我这种菜鸡就也去看看能不能混两个洞<br/> （1）找他们学校的学号，工号，身份证（挖edu最重要的是有账户，能进系统）<img alt="" height="250" src="https://img-blog.csdnimg.cn/854e8fc7627f4189981d4a22da7640ad.jpeg" width="666"/><img alt="" height="519" src="https://img-blog.csdnimg.cn/605b2a843bd948398b763cfb5b549c55.png" width="477"/>

（2）收集子域名、端口服务、旁站、c段等等，此处略，相信大家都会。<br/> 我一般是云服务器挂个灯塔，搭配oneforall，nmap，然后自己开bp，一个站一个站看过去

（3）之后是拿他们的学生账户和身份证进了几个系统，然后就是在系统里面测（毕竟有功能点才有可能存在漏洞）<br/> 这里有个小知识点，我们用账户登录的时候，可以扩展思维，比如用户名是学生的中文名字（例如：张三）；或者是拼音（例如：ZhangSan）；或者是名字每个字的首字母大小写（例如：ZS、zs）；又可能是拼音加学号（ZhangSan+学号）；身份证后六、八位；组合（学校缩写、学院缩写、专业编号等等）加身份证后六、八位<img alt="" height="459" src="https://img-blog.csdnimg.cn/39a03600ae80435594a093e4f8a8280e.png" width="1080"/><img alt="" height="711" src="https://img-blog.csdnimg.cn/8c5b68d8b9ba40efa19983d89fb945e9.png" width="1080"/><img alt="" height="487" src="https://img-blog.csdnimg.cn/3dea4861c018466887bc6f4f9fbb5343.png" width="1080"/>

2、之后因为考试就没有挖这个站了，后来去看的时候，发现外网基本上没啥点可打了，当然0day除外哈<br/> 于是乎就开始找账户进入统一认证系统（下面仅供参考），拿账户（vpn）的方法挺多的：（1）信息收集，拿到学号，身份证去爆破 （2）去淘宝等平台购买，有买vpn的，不过一般比较贵 （3）社工，这个我就不多说了

之后我是搞了一个统一认证账户登录（怎么来的，懂的都懂）<img alt="" height="615" src="https://img-blog.csdnimg.cn/8e8fa21e646c45fdafac26b79d790c89.png" width="1080"/>3、存储xss<br/> payload如图<img alt="" height="736" src="https://img-blog.csdnimg.cn/85f295bdc66345e98f98a75219282e32.png" width="1080"/>弹窗了<img alt="" height="648" src="https://img-blog.csdnimg.cn/079d5cf38c404bbba33b2a775079c305.png" width="1080"/>可以看到标签已经插进去了

因为这个站其实也没啥功能，随便测了下就不了了之，（当然还是自己太菜了，没0day，不像大佬出手就是0day）<br/> 之后漏洞也是提交给edusrc了

4、有VPN之后，我们也可以连接sslVPN，开fscan或者是goby进行内网的资产收集和渗透，毕竟外坚内脆嘛，网上也有很多文章，可以参考参考。

**没看够~？欢迎关注！**

**  **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

###  渗透工具

### 技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

### 面试题

### 帮助你在面试中脱颖而出

### 视频

### 基础到进阶

### 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
