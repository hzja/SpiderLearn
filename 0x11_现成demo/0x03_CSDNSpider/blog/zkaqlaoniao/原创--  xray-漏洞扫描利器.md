# 原创
：  xray：漏洞扫描利器

# xray：漏洞扫描利器

> 
<h3>公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习</h3>


### 简介

长亭科技旗下的一款网络安全漏洞扫描工具，用于检测和评估web应用程序的安全性。具有一下特点：检测速读快、检查范围广、代码质量高、高级可定制以及安全无危害。属于不开源的项目，用户直接下载xray的可执行文件，即可运行该工具

xray使用了与burpsuit一样的盈利模式：社区版、高级版和企业版

xray目前支持检测的漏洞：

```
XSS漏洞检测 (key: xss)
SQL 注入检测 (key: sqldet)
命令/代码注入检测 (key: cmd-injection)
目录枚举 (key: dirscan)
路径穿越检测 (key: path-traversal)
XML 实体注入检测 (key: xxe)
文件上传检测 (key: upload)
弱口令检测 (key: brute-force)
jsonp 检测 (key: jsonp)
ssrf 检测 (key: ssrf)
基线检查 (key: baseline)
任意跳转检测 (key: redirect)
CRLF 注入 (key: crlf-injection)
Struts2 系列漏洞检测 (高级版，key: struts)
Thinkphp系列漏洞检测 (高级版，key: thinkphp)
XStream 系列漏洞检测 (key: xstream)
POC 框架 (key: phantasm)

```

### 下载和安装

XRAY是一款不开源的漏扫工具，

提供两种下载渠道：
1. 官方下载：[GitHub - chaitin/xray: 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc | 使用之前务必先阅读文档](https://github.com/chaitin/xray)1. 非官方渠道(高级版，版本相对落后与官方版本)：[https://www.iculture.cc/software/pig=30388](https://www.iculture.cc/software/pig=30388)
大家根据自己的求进行下载

### 基本使用

#### 初始化

xray属于命令行执行的工具，并未提供图形化界面。所以，在我们下载好程序之后，将其解压到一个目录，然后通过cmd或者powershell进入这个目录

<br/> 不过在正式运行之前，我们需要执行一次命令，用于初始化配置文件：

<br/> 执行完成之后，回到目录就能发现先他有了最初的配置文件

<br/> 在修改配置文件的情况下，我们就已经能够简单的使用xray来扫描一部分的网站了。

xray存在两种运行方式：
1. 主动扫描1. 被动扫描
#### 主动扫描

主动扫描类似于SQLmap工具，用户通过指令设置需要扫描的功能、提供需要扫描的目标、设定结果保存的格式即可完成一次攻击

```
xray_windows_amd64.exe ws --url "http://testphp.vulnweb.com" --html-output 1.html

```

这个是一个简单的示例，当我们在cmd中执行命令之后，xray就会列出可攻击的poc和会测试的点：

<br/> 当探测到漏洞之后，会在终端以红色内容来输出漏洞信息：

<br/> 比如上面就发现了目标站点存在 .idea配置文件信息泄露漏洞，此时我们就可以通过它同的poc去验证这个漏洞是否真实存在：

<br/> 通过在终端里面看，并不是非常的方便，当xray扫描完成之后，xray会根据用户设定的保存格式，将所有检测到的漏洞都输出到对应的文件里面，比如我们在最开始使用的 —html-output 指令，就是让xray将结果以html形式输出：

<br/> 这样我们就可以通过访问这个文件来获取漏洞的详细信息

<br/> 然后我们就可以通过这样在网页上查看到它具体的漏洞信息。在xray的返回结果里面，有两个比较重要的字段：target和 pluginname/vulntype<br/> target : 保存了存在漏洞的url地址<br/> pluginname/vulntype： 则记录了url中存在的漏洞。<br/> 当然，这个知识记录了简单的信息。当我们想要看某个漏洞的具体细节时：可以通过点击 ID 列前面的加号，来展开这个漏洞：

<br/> 然后就可以查看到对应漏洞的细节：URL、payload和请求包。

通过这个演示之后，我想大家应该都掌握了xray的基本用法，接下来就是去查看他的一些具体的功能和使用参数了。<br/>`xray_windows_amd64.exe -h` 查看xray的帮助信息：

<br/> 在我当前使用的这个xray工具，能够实现一下攻击：

```
webscan      ws    web扫描任务
servicescan  ss    服务扫描
subdomain    sd    子域名扫描
poclint      pl，lint  检测poc的规范情况
burp-gamma   btg   将bp的poc转换成xray的poc格式
transform          将其他与语言的脚本转化成gamma脚本
reverse            运行独立的反向连接服务器
convert            扫描结果之间的转换（html -&amp;gt; json, json -&amp;gt; html）
genca              初始化ca证书
upgrade            更新xray
version            版本信息
x                  查看说有poc的可用性

```

对于安全测试人员来说，主要使用的是webscan、servicescan和subdomain

##### webscan

`xray_windows_amd64.exe ws -h` 通过这条命令，就可以查看到当前webscan的帮助信息：

```
--list    -l                           列出所有的plugin
--plugins value, --plugin value        检测指定的plugin
--poc value, -p value                  检测指定的poc
--level value                          指定poc的危害等级，只使用某个级别的poc（low,medium,high,critical），需要要使用多个级别时，用逗号分隔
--tags value                           指定运行某个标签的poc
--listen value                         监听一个地址，进行被动扫描
--basic-crawler value, --basic value   爬虫模式扫描，自动探测网站的所有url连接，并且进行扫描
--url-file value, -uf value            从文件中读取url，并对这些url进行测试
--burp-file value, --bf value          读取bp的请求包，进行测试
--url value, -u value                  指定单条url进行测试
--data value, -d value                 指定测试post传参点（username=admin）
--raw-request file, --rr file          加载原生http请求
--force-ssl, --fs                      配置访问https网站
--json-output file, --jo file          以json格式保存扫描结果
--html-output file, --ho file          以html格式保存扫描结果
--webhook-output value, --wo value     根据xray的格式保存结果

```

接下来进行演示：

###### 列出所有可用的plugin

`xray_windows_amd64.exe ws -l` 列出所有的可用plugin

###### 指定plugin模块

`xray_windows_amd64.exe ws --plugins xss,dirscan -u "http://testphp.vulnweb.com" --ho 2.html`指定扫描模块进行扫描

###### 指定poc进行扫描

`xray_windows_amd64.exe ws --poc poc-yaml-manageengine-servicedesk-cve-2017-11512-lfi -u "http://testphp.vulnweb.com" --ho 5.html` 指定poc进行扫描，需要将poc写在xray的可执行目录下

###### 使用网页爬虫进行漏洞测试

`xray_windows_amd64.exe ws --basic-crawler "http://testphp.vulnweb.com" --ho 6.html` 使用网页爬虫，爬取网站上所有的链接，并将链接加入到测试队列中

<br/>**在使用爬虫模式时，只能对单个url链接进行爬虫模式扫描**

###### 批量网站扫描

`xray_windows_amd64.exe ws --uf target.txt --ho 5.html` 将目标站点放入文件中，实现批量目标扫描

在实际工作中，可以通过选择一种扫描方式，然后利用 —poc和—plugins的组合，来控制扫描使用的poc。

##### servicescan

xray 中最常见的是 web 扫描，但是 xray 将会逐渐开放服务扫描的相关能力，目前主要是服务扫描相关的 poc。同样的，通过一个案例来进行演示：

<br/> 很显然，内置的 servicescan的poc相对来说量还是有点少的，不过也有肯能是我的操作不对，那就查看一手帮助信息：<br/>`xray_windows_amd64.exe ss -h` 查看帮助信息

<br/> 从帮助信息中不难看出，新的功能就3个：

```
--target value, -t value            指定目标
--module value, -m value            指定目标服务器的中间件，目前只支持 tomcat和weblogic
--target-file value, --tf file      指定扫描使用的poc的路径

```

从这里就能看出，有点点的鸡肋了。

##### subdomain

xray也推出了子域名查询的功能，不过它属于高级版和企业版才有的功能，所以换个非官方的xray，试一手，尝尝鲜：<br/>`xray.exe subdomain --target "zkaq.cn" --html-output 5.html` 扫描目标站点的子域名

<br/> 当成功扫到域名之后，会在终端以绿色字体显示

<br/> 感觉他的实现方式有点在暴力破解，又好像有在调用dns进行查询，每太看懂。<br/> 简单演示完了之后，接下就试去查看帮助信息:<br/>`xray.exe subdomain -h` 查看子域名暴破的帮助信息

<br/> ok,不难看出，和 serverscan 大差不差。

##### 被动扫描

代理模式下的基本架构为，扫描器作为中间人，首先原样转发流量，并返回服务器响应给浏览器等客户端，通讯两端都认为自己直接与对方对话，同时记录该流量，然后修改参数并重新发送请求进行扫描。<br/> 主动扫描已经能够帮助我们完成一些内容漏洞发现了，但是，在我看来xray更更核心的功能是他的被动扫描模块。<br/> 在使用被动扫描模式之前，我们需要先初始化一份ca证书，并且将证书导入到浏览器中：

###### 生成证书

`xray.exe genca`初始化证书

###### 初始化监听

`xray.exe ws --listen 127.0.0.1:8082 --ho 6.html` 初始化xray的监听地址

<br/> 通过这样的方式，xray就已经开始进行监听了。之后只需要将浏览器的代理只想xray的代理地址，xray的被动扫描功能就能体现出来的

<br/> 当我将浏览导入好证书、设置好代理之后，访问bbs.zkaq.cn,然后我的xray就开始去扫描站点了

<br/> 这样，xray就能有效的对一些需要登录的功能点进行测试，并且，他的测试是你访问了这个站点url之后，它检测到数据包了，才会去进行检测。不过在使用xray被动模式时，需要进行一些设置，不然可能会误伤其他站点。就比如我现在，并没有去设置xray的配置文件，然后它对一外站也进行测试

#### 配置文件修改

再上面的测试中，我们一直使用的都是默认配置，xray再默认情况下是对政府网站和校园网站禁止访问的，如果你再用xray去测试一些校园src的时候，可能就会因为配置的原因而无法进行扫描。<br/> 所以在工作和使用中，大家需要及时去修改和调整xray的配置文件。<br/> 默认情况下，第一此运行xray，xray就会在目录下生成配置文件

<br/> 这些.yaml后缀的文件就是xray的配置文件，其中config.ymal中包含了最基础的xray配置：

```
http           基础的http请求配置
plugins        扫描时使用的插件和poc
reverse        反连平台，有一部分poc时需要通过反连平台来确定漏洞是否存在。
mitm           被动扫描
basic-crawler  主动扫描中的爬虫设置

```

在这些配置中，最基础的配置是http、mitm和basic-crawler三个项目

###### http

在http中，我们需要修改的内容就包括一下三个点

proxy: 能帮助用户吟唱自己的真实IP，同时对于一些网站的防护（基于IP尽心的防护）<br/> max_qps: 设置发包速率，防止发包过快，导致一些站点崩溃<br/> headers: 设置请求头，可以往里面插入一些请求头的内容

###### mitm

在mitm中，我们需要修改的东西不多，就也就三个点：

<br/> 一个设置允许和禁止xray访问的域名，一个设置上层代理。配置方式，大同小异，知识这里的配置只影响被动扫描功能

```
hostname_allowed:   # 设置允许访问域名，*通配符
- "*.ncu.edu.cn"
- "*.jxnu.edu.cn"
hostname_disallowed:  # 设置不允许访问的域名
- "*google*"
- "*firefox*"
- "*bing.com"
- "*.gov.cn"
- "*.edu.cn"

upstream_proxy: 'http://127.0.0.1:8080'  # 设置上游代理，隐藏个人IP

```

###### basic-crawler

爬虫需要设置的内容可能稍微偏多一些

<br/> 爬虫没有单独设置代理，它的代理使用的http配置项中的代理来实现隐藏IP或者防护的。

```
max_depth: 1
max_count_of_links: 10

hostname_allowed:   # 设置允许访问域名，*通配符
- "*.ncu.edu.cn"
- "*.jxnu.edu.cn"
hostname_disallowed:  # 设置不允许访问的域名
- "*google*"
- "*firefox*"
- "*bing.com"
- "*.gov.cn"
- "*.edu.cn"

```

完成这些基础配置后，绝大部分的工作场景都能使用了

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/39079d4d36204925ab978b80ed7b30a0.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/6186edf0339b4b07bb58a0ba95ca9456.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/25e195b75ee24e1bbb523088a4469ff8.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/814e76ab67954483934746e65a6c7fdf.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/ed96ae97d85c4757abff07d6e31cc0a2.png" width="665"/>

应急响应笔记

学习路线
