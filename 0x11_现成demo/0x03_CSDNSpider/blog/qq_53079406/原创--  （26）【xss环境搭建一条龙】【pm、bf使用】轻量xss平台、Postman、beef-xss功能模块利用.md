# 原创
：  （26）【xss环境搭建一条龙】【pm、bf使用】轻量xss平台、Postman、beef-xss功能模块利用

# （26）【xss环境搭建一条龙】【pm、bf使用】轻量xss平台、Postman、beef-xss功能模块利用

**目录**

<img alt="" height="23" src="https://img-blog.csdnimg.cn/faadebb69d53406e9ceb6a24697a91c7.png" width="23"/>[​XSS平台搭建：](#%E2%80%8BXSS%E5%B9%B3%E5%8F%B0%E6%90%AD%E5%BB%BA%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​第一步：先下载源文件](#%E2%80%8B%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%85%88%E4%B8%8B%E8%BD%BD%E6%BA%90%E6%96%87%E4%BB%B6)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​第一个（来源：清华大学蓝莲花战队）：](#%E2%80%8B%E7%AC%AC%E4%B8%80%E4%B8%AA%EF%BC%88%E6%9D%A5%E6%BA%90%EF%BC%9A%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E8%93%9D%E8%8E%B2%E8%8A%B1%E6%88%98%E9%98%9F%EF%BC%89%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​第二个（网上发布的，在真实机上搭建失败，打算虚拟机终端搭建）：](#%E2%80%8B%E7%AC%AC%E4%BA%8C%E4%B8%AA%EF%BC%88%E7%BD%91%E4%B8%8A%E5%8F%91%E5%B8%83%E7%9A%84%EF%BC%8C%E5%9C%A8%E7%9C%9F%E5%AE%9E%E6%9C%BA%E4%B8%8A%E6%90%AD%E5%BB%BA%E5%A4%B1%E8%B4%A5%EF%BC%8C%E6%89%93%E7%AE%97%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%BB%88%E7%AB%AF%E6%90%AD%E5%BB%BA%EF%BC%89%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/faadebb69d53406e9ceb6a24697a91c7.png" width="23"/>[​XSS工具使用：](#%E2%80%8BXSS%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/faadebb69d53406e9ceb6a24697a91c7.png" width="23"/>[​postman：](#%E2%80%8Bpostman%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​下载：](#%E2%80%8B%E4%B8%8B%E8%BD%BD%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​使用教程：](#%E2%80%8B%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/29ab151801ad4fb9bcc4fafbd42b993b.png" width="23"/>[​对比老版：](#%E2%80%8B%E5%AF%B9%E6%AF%94%E8%80%81%E7%89%88%EF%BC%9A) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​基本功能介绍：](#%E2%80%8B%E5%9F%BA%E6%9C%AC%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/1b9e66b6093a463aae623851c9df7baa.png" width="23"/>[​界面导航理解](#%E2%80%8B%E7%95%8C%E9%9D%A2%E5%AF%BC%E8%88%AA%E7%90%86%E8%A7%A3) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/9adac1f12d3b44deb37634c081affde6.png" width="23"/>[​Environments配置环境变量](#%E2%80%8BEnvironments%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/a58b74d89a1d47379182a0064a81d102.png" width="23"/>[​将请求中不变的数据参数化](#%E2%80%8B%E5%B0%86%E8%AF%B7%E6%B1%82%E4%B8%AD%E4%B8%8D%E5%8F%98%E7%9A%84%E6%95%B0%E6%8D%AE%E5%8F%82%E6%95%B0%E5%8C%96) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/7a4a2722858f48c18874c90f51f3bacd.png" width="23"/>[​Postman Tests](#%E2%80%8BPostman%20Tests) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/59749aa0555244968ec9558c447f44be.png" width="23"/>[​集合测试](#%E2%80%8B%E9%9B%86%E5%90%88%E6%B5%8B%E8%AF%95) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/faadebb69d53406e9ceb6a24697a91c7.png" width="23"/>[​beef-xss：](#%E2%80%8Bbeef-xss%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​可能会用到：](#%E2%80%8B%E5%8F%AF%E8%83%BD%E4%BC%9A%E7%94%A8%E5%88%B0%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​使用方法：](#%E2%80%8B%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/f8364589ee3b409484488cd811b6460d.png" width="23"/>[​第一步：启动beef](#%E2%80%8B%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8beef) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1ede973e74748bfb5d16d31593a8714.png" width="23"/>[​第二步： 放Hook（钩子）](#%E2%80%8B%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%C2%A0%E6%94%BEHook%EF%BC%88%E9%92%A9%E5%AD%90%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/192ea318b8164b389a9e42a2e82b041d.png" width="23"/>[​第三步：开始摆起来](#%E2%80%8B%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%BC%80%E5%A7%8B%E6%91%86%E8%B5%B7%E6%9D%A5) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​Commands（命令）](#%E2%80%8BCommands%EF%BC%88%E5%91%BD%E4%BB%A4%EF%BC%89)

<img alt="" height="23" src="https://img-blog.csdnimg.cn/b379ea39ea3e45df9c62ab19e33c9723.png" width="23"/>[​颜色的含义：](#%E2%80%8B%E9%A2%9C%E8%89%B2%E7%9A%84%E5%90%AB%E4%B9%89%EF%BC%9A) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/8f21f2395f7044e990419937ddc606a6.png" width="23"/>[​Details(细节,这就是上钩主机的相关信息)](#%E2%80%8BDetails%28%E7%BB%86%E8%8A%82%2C%E8%BF%99%E5%B0%B1%E6%98%AF%E4%B8%8A%E9%92%A9%E4%B8%BB%E6%9C%BA%E7%9A%84%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF%29) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/83f7d4ddcef0474e8dd11b5951e2bb26.png" width="23"/>[​Browser（浏览器，就是检测浏览器相关特性）](#%E2%80%8BBrowser%EF%BC%88%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%8C%E5%B0%B1%E6%98%AF%E6%A3%80%E6%B5%8B%E6%B5%8F%E8%A7%88%E5%99%A8%E7%9B%B8%E5%85%B3%E7%89%B9%E6%80%A7%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/44f9ed7a448b433abcb3869ece9599b9.png" width="23"/>[​Chrom Extensions（Chrom延伸）](#%E2%80%8BChrom%20Extensions%EF%BC%88Chrom%E5%BB%B6%E4%BC%B8%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/6a296bf9384c44f5a2248d1032ddccb4.png" width="23"/>[​Debug（调试）](#%E2%80%8BDebug%EF%BC%88%E8%B0%83%E8%AF%95%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/4ff99664207f430f8b8b31151df35c26.png" width="23"/>[​Exploits（漏洞利用，虽然还没认真看，听见名字就觉得挺不错）](#%E2%80%8BExploits%EF%BC%88%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%8C%E8%99%BD%E7%84%B6%E8%BF%98%E6%B2%A1%E8%AE%A4%E7%9C%9F%E7%9C%8B%EF%BC%8C%E5%90%AC%E8%A7%81%E5%90%8D%E5%AD%97%E5%B0%B1%E8%A7%89%E5%BE%97%E6%8C%BA%E4%B8%8D%E9%94%99%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/ac72f84e77a744dfa13fd9bc6f84b6d0.png" width="23"/>[​Host（主机）](#%E2%80%8BHost%EF%BC%88%E4%B8%BB%E6%9C%BA%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/e3ccf8ec1cc0411dbc4eba10edcedd33.png" width="23"/>[​IPEC（通信）](#%E2%80%8BIPEC%EF%BC%88%E9%80%9A%E4%BF%A1%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/3e6c8b4ba2c340a091bcbe556cac6dfd.png" width="23"/>[​Metasploit（一个框架，获取、开发并对计算机软件漏洞实施攻击，内置在MSF中）](#%E2%80%8BMetasploit%EF%BC%88%E4%B8%80%E4%B8%AA%E6%A1%86%E6%9E%B6%EF%BC%8C%E8%8E%B7%E5%8F%96%E3%80%81%E5%BC%80%E5%8F%91%E5%B9%B6%E5%AF%B9%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%BD%AF%E4%BB%B6%E6%BC%8F%E6%B4%9E%E5%AE%9E%E6%96%BD%E6%94%BB%E5%87%BB%EF%BC%8C%E5%86%85%E7%BD%AE%E5%9C%A8MSF%E4%B8%AD%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/d6533f852ae74060b1feee0db6555141.png" width="23"/>[​Misc（杂项）](#%E2%80%8BMisc%EF%BC%88%E6%9D%82%E9%A1%B9%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/058454e4c1d247d4831505a69aa6f850.png" width="23"/>[​Network（网络）](#%E2%80%8BNetwork%EF%BC%88%E7%BD%91%E7%BB%9C%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/895418517572447cbb50b87fb1efb597.png" width="23"/>[​Persistence（就是为了持续性Hook住目标）](#%E2%80%8BPersistence%EF%BC%88%E5%B0%B1%E6%98%AF%E4%B8%BA%E4%BA%86%E6%8C%81%E7%BB%AD%E6%80%A7Hook%E4%BD%8F%E7%9B%AE%E6%A0%87%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/94071ccfd63f412a86f2ade5a8228f84.png" width="23"/>[​Phonegap(开源的开发框架，让开发者使用 HTML 、 Javascript 、CSS等Web APIs开发跨平台的移动应用程序)](#%E2%80%8BPhonegap%28%E5%BC%80%E6%BA%90%E7%9A%84%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6%EF%BC%8C%E8%AE%A9%E5%BC%80%E5%8F%91%E8%80%85%E4%BD%BF%E7%94%A8%20HTML%20%E3%80%81%20Javascript%20%E3%80%81CSS%E7%AD%89Web%20APIs%E5%BC%80%E5%8F%91%E8%B7%A8%E5%B9%B3%E5%8F%B0%E7%9A%84%E7%A7%BB%E5%8A%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%29) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/db9e7a26b4a34d8ead5767896dea1d45.png" width="23"/>[​Social Engineerin（社会工程学，永远的经典）](#%E2%80%8BSocial%20Engineerin%EF%BC%88%E7%A4%BE%E4%BC%9A%E5%B7%A5%E7%A8%8B%E5%AD%A6%EF%BC%8C%E6%B0%B8%E8%BF%9C%E7%9A%84%E7%BB%8F%E5%85%B8%EF%BC%89) 

<img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>[​ offline（离线的）](#%E2%80%8B%C2%A0offline%EF%BC%88%E7%A6%BB%E7%BA%BF%E7%9A%84%EF%BC%89)

---


## <img alt="" height="23" src="https://img-blog.csdnimg.cn/faadebb69d53406e9ceb6a24697a91c7.png" width="23"/>XSS平台搭建：

 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/0c0cf407d78e47f08d5103c20976d716.png" width="23"/>第一步：先下载源文件

 

> 
第一个（来源：清华大学蓝莲花战队）：
 XSS平台项目名称：BlueLotus_XSSReceiver
作者：firesun（来源：清华大学蓝莲花战队）
GITHub（更全，轻量级无需数据库）：[asw3asw/BlueLotus_XSSReceiver (github.com)](https://github.com/asw3asw/BlueLotus_XSSReceiver)
 gitee下载地址（gitee需要注册，貌似很正规）：[BlueLotus_XSSReceiver: XSS平台 CTF工具 Web安全工具 (gitee.com)](https://gitee.com/evlon/BlueLotus_XSSReceiver#%E5%B9%B3%E5%8F%B0%E8%AF%B4%E6%98%8E)



> 
 第二个（网上别人发布的）：
（不推荐，因为不全面，而且我试了一遍，可能比第一个更繁琐一点）
GitHub（需要数据库）：[https://github.com/78778443/xssplatform](https://github.com/78778443/xssplatform)


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/53705c315e194c02bbe4b4dd9e1b596d.png" width="23"/>第一个（来源：清华大学蓝莲花战队）：

 

> 
在地址栏中输入本地搭建的网站，目录下的BlueLotus_XSSReceiver-master


提示信息：
（我安装环境：phpstudy下的MySQL，直接解压到WWW下的）
手动安装方法：
将config-sample.php改名为config.php
删除install.php即可（这个删除其实可以不删除，往后看）。


修改config-sample.php改名为config.php（这步没错）





 install.php（删了以后就没有这个安装页面，就没地方点登录了）


 然后点击登录
如果删除了话，其实下次多打一点，把登录页面URL也打出来
localhost:8080/BlueLotus_XSSReceiver-master/**login.php**


默认密码在修改了的config.php文件里，打开看一看


输入后台密码后然后就登录进去了



 （比需要配置数据库连接的快很多，可能出现的错误也能很快解决）

 

 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/9795e5ec14e24d4f9f25eacf26e44104.png" width="23"/>第二个（网上发布的，在真实机上搭建失败，打算虚拟机终端搭建）：

 

> 
（我是在真实机上搭建的，出现了404错误，且尝试各方方法，检测各种配置文件）
（我打算在虚拟机的终端上进行搭建，终端才是真的可靠）
（走过的每一步都是有用的，下面的过程可以当坑，来吸取我失败经验）


> 
第二步：将XSS源码放在网站目录下

也就是将下载解压后的文件，放在WWW下（我用的是phpstudy集成环境）









第三步：提前下好一个MySQL管理工具（主要是方便操作一点）
点击管理，跳转到登录页面


 <img alt="" height="628" src="https://img-blog.csdnimg.cn/1290a64f38c942cd83bbc66228ee38da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="861"/>

密码为数据库密码 （忘记了就再修改一下，修改密码不需要知道原密码）


新建一个数据库,我取名为xssplatform（数据库平台）

现在里面是什么都还没有的





第四步：连接到数据库
更改config.php配置文件



根据自己的实际情况更改用户密码，数据库名 



第五步：导入到数据库


















检查config.php配置都没问题（炒你鱿鱼算了）
准备使用其他的数据库软件，最后如果不行就尝试命令行导入（希望不到最后一步）
官方软件：MySQL Workbench
工具：Navicat for MySQL

MySQL Workbench

<img alt="" height="837" src="https://img-blog.csdnimg.cn/a60424eeb15a447b8ee23c59093a3522.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/> 


UPDATE oc_module SET<br/> code=REPLACE(code,'http://xsser.me','http://localhost:8080/xssplatform-master')
<img alt="" height="610" src="https://img-blog.csdnimg.cn/799fc51e16a04f098b145f88b3484dc1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="731"/> 

 

 
 注册帐号，将config.php中的invite改为normal，即为开放注册<img alt="" height="515" src="https://img-blog.csdnimg.cn/2b018441aabf41d1a4736cedae9bcb2c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="739"/>
 <img alt="" height="286" src="https://img-blog.csdnimg.cn/f8f111ae0e4b4ab4808cc28a7faf4a88.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="661"/>
 <img alt="" height="472" src="https://img-blog.csdnimg.cn/1bac9a8db8874079893e526fc431a06d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1013"/>



 


 
 


 

尝试在终端导入（成功导入了）
<img alt="" height="535" src="https://img-blog.csdnimg.cn/65752bab860e413b81a78563fe1475f3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="738"/> <img alt="" height="371" src="https://img-blog.csdnimg.cn/a0c84ce97ddf409c8706adddca963f21.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_12,color_FFFFFF,t_70,g_se,x_16" width="492"/>
 <img alt="" height="534" src="https://img-blog.csdnimg.cn/0e2146e06aa6433491266d8eba983359.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="746"/>
 <img alt="" height="399" src="https://img-blog.csdnimg.cn/30f8747051244c6189f30555a70bf4cf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_15,color_FFFFFF,t_70,g_se,x_16" width="623"/>
 
 <img alt="" height="65" src="https://img-blog.csdnimg.cn/3efbd7979dc142e1890d5593058c5028.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_13,color_FFFFFF,t_70,g_se,x_16" width="546"/>


 
 


<img alt="" height="381" src="https://img-blog.csdnimg.cn/b2e05b37ec0347368efafe7d7fa7d354.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_10,color_FFFFFF,t_70,g_se,x_16" width="441"/> 

<img alt="" height="713" src="https://img-blog.csdnimg.cn/35cd866f829a40d6827e96715517a991.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/> 

 
 


 

 

## <img alt="" height="23" src="https://img-blog.csdnimg.cn/81e28aecb26a46118e4ee13a7598606e.png" width="23"/>XSS工具使用：

 

## <img alt="" height="23" src="https://img-blog.csdnimg.cn/b528d2fe3e894b5eb2ab8558be1e9afd.png" width="23"/>postman：

 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/6691ec806d63416dab61bf9d9af03443.png" width="23"/>下载：

 

> 
下载地址（官网）：[Postman API Platform | Sign Up for Free](https://www.postman.com/)

 <img alt="" height="932" src="https://img-blog.csdnimg.cn/87ca4add1ce7466ab86bd63bf3bc8453.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

postman是免安装的，双击程序，既可以运行了



若个人使用，选择下面的跳过（skip）即可，这时会进入到postman主界面，至此postman安装成功。
若团队使用，可以进行注册，注册后使用账号可以加入团队工作区



### <img alt="" height="23" src="https://img-blog.csdnimg.cn/931c1f8ba86b4e5a8cb716982570f281.png" width="23"/>使用教程：

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/66b2b444be4b4f82a99e6a3a010f771a.png" width="23"/>对比老版：

 

> 
 新建一个后，页面差不多是这样了（最新版的）

 （版本怎么变，万变不离其宗，核心东西都差不多）
老版的这个左边是横着的，但是不影响聪明的我（先参考参考老版的）



### <img alt="" height="23" src="https://img-blog.csdnimg.cn/147d7aee6b374251917c01a332ff303f.png" width="23"/>基本功能介绍：

> 
Collections(这个一般是主要使用的)、APIs、Environments（环境）、Mock Services（模拟服务）、Monitors（监视）、History（历史记录）
老版的左边没有这3个



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/587f1fa0d09c475a8bf0d604cfe5043c.png" width="23"/>界面导航理解

 

> 
NEW新建请求----请求方法----URL地址-----发送
Authorization：访问API，需要相应的授权，如Username、Password、Token等<br/> Headers：请求头信息<br/> Body：请求体信息<br/> Pre-request Script：请求之前 先执行脚本，使用设置环境的预请求脚本来确保在正确的环境中运行测试<br/> Tests：测试，它设置检查点来验证响应状态是否正常、检索的数据是否符合预期



设置请求方法（post那里）-----设置请求体类型（body下面）

<img alt="" height="178" src="https://img-blog.csdnimg.cn/1f17716f0a2743689d20b2d0f2bfce7c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="865"/> <img alt="" height="265" src="https://img-blog.csdnimg.cn/fd5e25ab7b514216b1ba7ee43199e684.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="906"/>



接口响应数据解析

Pretty（格式后展示）、Raw（原始数据）、Preview（预览）、visualize（可视化）<img alt="" height="714" src="https://img-blog.csdnimg.cn/b02dd0a1916e42c3884e6df5fd129e15.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1110"/>


 

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/f1a86aaaead74c61bc4d48a040d30249.png" width="23"/>Environments配置环境变量

 

> 
在测试过程中，都是使用一个测试地址，就可以把被测地址设置为环境变量
值可以设置多个，最后点save


 可以选择环境变量<img alt="" height="394" src="https://img-blog.csdnimg.cn/7489f5471efd413cb6aa612d89b1feec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1115"/>
 <img alt="" height="241" src="https://img-blog.csdnimg.cn/2d8f73e27e8040709b2fb367c30568da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_8,color_FFFFFF,t_70,g_se,x_16" width="357"/>

Globals（全局的）可以添加到全局变量



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/dd768add5d6f456f8ff42d8912a4e59a.png" width="23"/>将请求中不变的数据参数化

 

> 
 将数据参数化，能够避免测试的时候的重复，可以进行自动化迭代测试
并使用{{TEST}}来包裹参数
例：
**第一步：**现将变量配置为全局环境



将要变量参数和对应的值输入进去，再点击save
 <img alt="" height="396" src="https://img-blog.csdnimg.cn/4ccb36d0ac5c40cb9253ffc903382f5b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1126"/>

**第二步：**将全局变量用{{}}包裹起来，如：{{URL}}
 能找到配置的环境，就能显示蓝色<img alt="" height="494" src="https://img-blog.csdnimg.cn/e70faa979c954747a6d9276434f2bb08.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1111"/>

 如果没有的话就是红色的

第三步：就能Send了 


#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/275540e154d2485ea67eb910033116e6.png" width="23"/>Postman Tests

 

> 
 为了协助验证结果，点击Tests能够在请求中添加自己选的JavaScript代码（对比成功或失败状态、预期结果）
**第一步：**
点击Test-----在右侧的js代码中选择一个预期的测试结果（左侧就会自动写入测试代码）
点击一个200状态码试试，点击Send

 （我忘记把URL改回来了，哈哈哈）



**第二步：**
点击Test Results（测试结果）
然后看见和预期是一样的200状态码 

（也可以添加多个js测试代码同时测试）


#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/2aa9bc9d30d34cdca48b5700d41a6bbc.png" width="23"/>集合测试

 

> 
（上一个测试的升级版）
集合测试（能被导入和导出）所以测试的结果能够更好的分享或保存（不过注册了这个软件的，好像有团队协作模式）

**第一步：**点到Collections然后点击加号，新建一个Collection


命名要命好，最好是写上描述，方便日后的管理 

 <img alt="" height="624" src="https://img-blog.csdnimg.cn/3ed0173bb76b47759f3f3db6119ed8ab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_13,color_FFFFFF,t_70,g_se,x_16" width="555"/>


**第二步：**首先，先新建测试项

 <img alt="" height="437" src="https://img-blog.csdnimg.cn/86f2919e976047af9db5d1627ca7bd24.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

再点击右键，类似方法，再添加多个request


可以对每一个request进行命名，可以方便区分
（然后可以看到Test Collection下面已经添加了多个不同的test了）



**第三步：**
将这些集合进行测试



二次的测试结果都出来了 


 点view summary（可以查看概况）



 

## <img alt="" height="23" src="https://img-blog.csdnimg.cn/81bdb03f097b4d56a495f18821bc870c.png" width="23"/>beef-xss：

 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/7dde3bd183ab412ea047e7b32eb86149.png" width="23"/>可能会用到：

 

> 
 安装：
[Linux中安装beef以及启动](https://blog.csdn.net/qq_53079406/article/details/122736178?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164828230416782092923056%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164828230416782092923056&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-122736178.nonecase&amp;utm_term=beef&amp;spm=1018.2226.3001.4450)
查看密码/hook：
[“忘记BeEF账号密码（权限不足问题）”之查看账号密码，BeEF的基本启动和使用，Hook使用方法及相关机器信息查看和命令使用](https://blog.csdn.net/qq_53079406/article/details/122740966?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164829178316780265438994%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164829178316780265438994&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-122740966.nonecase&amp;utm_term=beef&amp;spm=1018.2226.3001.4450)


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/18c7b1f0484647a4a2fd12b25b9da9dd.png" width="23"/>使用方法：

 

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/6b2d3db508ab4b39ac19e15f199cd547.png" width="23"/>第一步：启动beef

 

> 
第一次启动后需要手动设置密码
方法一：在终端输入beef-xss

 <img alt="" height="760" src="https://img-blog.csdnimg.cn/c6c42d4dbe734266aadf1841c5685f60.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


方法二：
如果安装成功，直接搜beef，会出现beef的启动终端，然后会出现界面
（按道理说还多了一步，但是总感觉简单了）





#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/9814b7babc5341aeab2438f99d6d06b6.png" width="23"/>第二步： 放Hook（钩子）

 

> 
 这个钩子其实在启动beef的时候里面包含了示例（就好像没有一个动作是多余的，哈哈哈）
让我重新打开终端进行查看（每一步重复都是一次进步）
看到没有，宝
Web UI（就是beef登录的网页）
Hook（钩子）
Example（多贴心，还给出了例子）



拿钩子到XSS存储型靶场里去试一下，把钩子上传进去（因为是测试，把安全等级调为low）
没有下载DVWA的可以用pikachu的XSS
（里面的ip放的自己的ip）



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/b7d80acbceca4e8eba34e0101071914e.png" width="23"/>第三步：开始摆起来

 

> 
 然后在beff的控制端可以看见一个上线的主机（这个就是……，哈哈哈）



 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/0099565aea2a46f1a1bfee18af5835b4.png" width="23"/>Commands（命令）

 

> 
 点击相应的主机后，点击commands（命令），执行相关模块对目标主机进行入侵

<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/4b3384210b2f4efcacebf520c4a071af.png" width="23"/>颜色的含义：</h4>
 
绿色模块：适用当前用户，并且执行结果对用户不可见
红色模块：不适用当前用户，有些红色模块也可以执行
橙色模块：模块可用，但结果对用户可见
灰色模块：模块为在目标浏览器上测试过


<h4><img alt="" height="23" src="https://img-blog.csdnimg.cn/521ba47decbc44a0bfe2105b114571bd.png" width="23"/>Details(细节,这就是上钩主机的相关信息)</h4>
 



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/521ba47decbc44a0bfe2105b114571bd.png" width="23"/>Details(细节,这就是上钩主机的相关信息)

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/54d4e261b2014255bfc7040c4ded56fb.png" width="23"/>Browser（浏览器，就是检测浏览器相关特性）

 

> 
 eg：
此模块将检查浏览器是否有Foxit Reader插件。


 点击右下角Execute（执行）后，历史记录中双击一个历史记录，就可以查看到命令执行的结果
（下面都是这样了，我就不一一重复这么多了）



 

 

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/eb70e879ca8f4dbfb7bf22c4111e674b.png" width="23"/>Chrom Extensions（Chrom延伸）

 

> 
eg：（打开第一个看看是什么究竟是何种妖魔鬼怪）
打开一个新选项卡，然后执行javascript代码。 Chrome扩展需要具有“标签”权限，以及访问域。


双击command[num]查看结果



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/917a1c4797b64c3bbb3c43e3e507611b.png" width="23"/>Debug（调试）

 

> 
 eg：（老规矩，打开一个个功能试试）
此模块将通过DNS，客户端发送到服务器的数据。牛肉的DNS服务器用于重建通过DNS挤出的数据的块。<br/> 确保：<br/>  - 启用DNS扩展，<br/>  -  DNS服务器正在侦听端口53，<br/>  - 挂钩的浏览器正在解析通过牛肉的DNS服务器指定的域。
默认情况下，用于挤出数据的所有DNS请求返回NXDOMAIN响应。


 双击----查看结果



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/d76e03d3c9cd492184a09c8ac36028e5.png" width="23"/>Exploits（漏洞利用，虽然还没认真看，听见名字就觉得挺不错）

 

> 
eg：（第一个）
此模块利用CVE-2012-0053以便阅读受害者的cookie，即使使用HttpOnly属性发出。如果目标服务器正在运行Apache HTTP Server 2.2.0至2.21，则漏洞仅适用。


 没结果，说明没这漏洞<img alt="" height="296" src="https://img-blog.csdnimg.cn/2d590356087d423092bdfee56adb69e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_19,color_FFFFFF,t_70,g_se,x_16" width="775"/>


#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/692ec532828149ccad59a140b78e7f4f.png" width="23"/>Host（主机）

 

> 
eg： 
他的模块通过某些AVS自动检测到JavaScript代码（目前支持Kaspersky，Avira，Avast（ASW），Bitdefender，Norton，Web博士的检测


结果是没有检测到



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/adc79942b9fd48c5a997af4bc9201f7c.png" width="23"/>IPEC（通信）

 

> 
 eg：（有点坑）
使用协议间的开发/通信（IPEC）挂钩的浏览器将在“目标地址”输入字段中指定的目标上向ActiveFAX RAW Server套接字（默认为3000）发送消息。该模块可以通过ActiveFAX服务器向（Premium）Faxnumber发送传真。
目标地址可以位于挂钩的浏览器的子网上，这些子网可能无法直接从Internet访问。


显示发送了（感觉靶机bbq了）


此时靶机好像瓦特了
提示信息是：
您的浏览器发送了此服务器无法理解的请求。<br/> 请求标头字段的大小超过服务器限制。
 <img alt="" height="376" src="https://img-blog.csdnimg.cn/d86cc9a071644a5199a9a49e90538c05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_16,color_FFFFFF,t_70,g_se,x_16" width="657"/>


 

（接下来就不把每个commands都试一遍了）

#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/0ea5d33df69c43efabc5046109c92134.png" width="23"/>Metasploit（一个框架，获取、开发并对计算机软件漏洞实施攻击，内置在MSF中）

 

> 
eg：
此模块将用户将用户重定向到Metasproit侦听器上的Autopwn端口，然后依靠Metasploit来处理生成的shell。如果加载Metasploit扩展，则此模块将将URL预先填充到预启动的侦听器。否则，请输入您希望将用户重定向到的URL。



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/3c30b3d6c9044b468330344fd1480812.png" width="23"/>Misc（杂项）

 

> 
eg：
创建一个不可见的iframe。



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/586b8d7a5eae439e812d4cd643c82628.png" width="23"/>Network（网络）

 

> 
eg：
扫描Web服务器的IP范围，允许使用CORS的交叉源请求。 HTTP响应返回牛肉。
注意：将IP地址范围设置为“常见”以扫描公共LAN地址列表。



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/eca3a082ff044b2497a694bd77ccbf86.png" width="23"/>Persistence（就是为了持续性Hook住目标）

 

> 
eg：
此模块将使用一个浏览器攻击，以确保牛肉钩将留在用户离开域（手动将其更改为URL栏中）



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/d1dffb7447e14ce38865f2165dd45fd1.png" width="23"/>Phonegap(开源的开发框架，让开发者使用 HTML 、 Javascript 、CSS等Web APIs开发跨平台的移动应用程序)

 

> 
 eg：
显示用户警报



#### <img alt="" height="23" src="https://img-blog.csdnimg.cn/b164a4c735d141d8a742ce98ec5df834.png" width="23"/>Social Engineerin（社会工程学，永远的经典）

 

> 
eg：
将文本转换为MP3并在挂钩的浏览器上播放。注意：此模块需要安装跛脚和截止圈。



 

 

### <img alt="" height="23" src="https://img-blog.csdnimg.cn/c84970c44f434db4a4ebb7dd7d502764.png" width="23"/> offline（离线的）

 

> 
 当用户离线以后，你啥操作都执行不了了（且行且珍惜吧）



<img alt="" src="https://img-blog.csdnimg.cn/4e512308431a40528352fdc378e515e3.png"/> 
