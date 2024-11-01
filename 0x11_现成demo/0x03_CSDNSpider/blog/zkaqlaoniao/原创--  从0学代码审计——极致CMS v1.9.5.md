# 原创
：  从0学代码审计——极致CMS v1.9.5

# 从0学代码审计——极致CMS v1.9.5

### 0x01 框架基础

环境搭建这块还是比较容易的，github可以下载任意版本的极致CMS，下载源码有注册脚本，本地只需要新建一个数据库即可安装成功。下载链接：https://github.com/Cherry-toto/jizhicms<br/> 下载后的目录结构如下：<br/>  

<br/> 这块代码的底层使用Frphp框架，该框架目录结构如下：<br/>  

<br/> 白盒审计框架首先要弄懂该框架是怎么路由调度的，以及相关业务代码是怎么在游览器通过url访问的。做个测试，通过后台登录的功能调试代码，分析实现登录的业务逻辑是怎么实现的。以上的框架目录中有两个入口文件，分别为index.php和admin.php，前者是前台管理的入口，后者是后台管理的入口。<br/>  

<br/> 接下来就分析为什么url是这种格式，在admin.php文件里下断点<br/>  

<br/> 实例化核心类，run方法启动程序<br/>  

<br/> 跟进 route 方法开始获取路由<br/>  

<br/> 从 $_SERVER 获取url，读取webconfig配置文件，检测该url是否允许访问<br/>  

<br/> 该框架内置有三种url格式，首先会将这三种url格式与当前url进行匹配，如果匹配不成功，就解析当前的url<br/>  

<br/> 清除url的入口文件字符串，也就是admin.php<br/>  

<br/> 去除 url 的 html 后缀，注释也说了，非常清楚，然后将剩下的 /Login/index 以斜杠分割成数组<br/>  

<br/> 获取控制器名和方法名，随后对控制器名进行拼接与判断<br/>  

<br/>  

<br/> 调用 LoginController 的 index 方法<br/>  

<br/> 该方法就是一个处理登录逻辑的方法，到此路由调度完成。

### 0x02 漏洞审计

##### 任意文件下载RCE

前台没有什么功能点，全是静态的，而且前台登录也没有具体代码实现。那么重点分析后台管理，用已知的账号密码登录，漏洞点在插件的下载<br/>  

<br/> 抓包看一下<br/>  

<br/> url是可控的，按理来说可以任意文件下载，找到插件下载的相关实现代码<br/>  

<br/> 从前端获取相关参数信息，创建一个临时文件目录，也就是 tmp_path，Cache_Path就是缓存文件目录。文件名是经过拼接的，所以任意文件下载的只能是zip<br/>  

<br/> 创建 tmp_path 这个临时文件，将下载的文件写进这个临时文件里，也可以认为是重命名。<br/> 既然下载的插件是zip，那么肯定会有解压的操作，当 action=file-upzip 时，有具体实现代码<br/>  

<br/> 首先判断该临时文件是否存在，然后将压缩包解压到 A/exts目录下，get_zip_originalsize 函数实现解压功能，写一个执行phpinfo的php文件，压缩成zip，然后在当前目录下开启web服务<br/>  

<br/> 抓包修改url，下载构造好的1.zip<br/>  

<br/> 下载完成，此时cache目录下多了一个我们下载的zip<br/>  

<br/> 然后解压<br/>  

<br/> 此时我们构造的1.php已经解压到 A/exts 目录下<br/>  

<br/> 该目录下的文件可以直接通过文件访问<br/>  

<br/> 已经成功getshell了

##### sql注入漏洞

漏洞点在插件的配置这里<br/>  

<br/> 找到关键代码<br/>  

<br/> 通过url获取id，find查询当前id的信息，此处不存在sql注入漏洞，因为该id的意思是已经安装的插件id，参数id并不完全可控，url上的id只能匹配数字，无法写入sql语句。下面处理POST数据的代码块，使用 setconfigdata 方法可以执行更新的sql语句<br/>  

<br/> 存在字符串拼接，单引号闭合，可以执行sql语句<br/>  

<br/> 执行报错语句<br/>`id=1' and updatexml(1, concat(0x7e, version()),1)#`<br/>  

<br/> 成功执行我们添加的报错语句，但是报错日志不会回显到页面上。理论上可以通过页面回显不同来盲注，漏洞审计存在即可，就不往下分析利用过程了。

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
