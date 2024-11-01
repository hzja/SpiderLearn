# 原创
：  BurpSuite保姆级教程

# BurpSuite保姆级教程

## Burp Suite下载,破解,代理web,代理模拟器

#### (一)为Burp Sutie下载运行执行脚本环境(Java)

1.Java官网下载地址：https://www.oracle.com/java/technologies/<br/> 下载Java SE 17.0.8(LTS)<br/> 备注：1.2023版Burp Suite 完美的运行脚本的环境是Java17<br/> 2.Java8不支持<br/> 3.Java17以下版本存在 我已知问题：鼠标编辑数据包时字体出现不协调问题

2.选择：<br/> windows系统<br/> x64 insaller (.exe程序安装的意思)

3.安装程序一直下一步<br/> 如果需要更改程序安装地址：注意存储程序路径都应该是英文目录下<br/> (中文目录/路径:会报错无法安装)

4.cmd命令行,查看是否安装Java17脚本环境成功<br/> java -version //查看java版本

### (二)下载Burp Suite

Burp Suite官方下载地址：https://portswigger.net/burp/releases#professional<br/>  

<br/> 因为是Burp Suite官网下载地址：可以一直持续追最新版本、当然喜欢什么版本也可以下什么版本、觉得什么版本牛逼就下载什么版本(不需要再靠他人要,自己动手丰衣足食)<br/> (这就是我为什么要出这个文章的原因：我看的太多次,很多人向别人要Burp Suite各种版本)(官网下载,无毒,绿色)

版本问题：<br/> Stable：稳定版本<br/> Early Adopter：实验版本

Professional：专业版本<br/> Community Edition：社区版本

建议选择：Stable(稳定版本) + Burp Suite Professional(专业版本) + JAR(文件格式)

#### (三)下载Burp Suite 注册机破解脚本

Burp Suite注册机破解脚本地址：https://github.com/h3110w0r1d-y/BurpLoaderKeygen

##### (四)破解Burp Suite流程

1.下载的Burp Suite的jar文件 和 Burp Suite注册机破解脚本的jar文件 (放在同一目录(文件夹)下)

2.点击 BurpLoaderKeygen.jar 自动生成.config.ini文件(配置文件)

###### 这里也可以自定义一个名字(不影响破解,无关紧要)

3.点击Run -&gt; 自动打开Burp Suite Professional

4.点击 I Accept(我同意)

5.复制 -&gt; 粘贴 -&gt; (Next)下一步

6.点击 Manual activation(手动激活)

7.BurpLoaderKeygen.jar(破解机的密码) 对应 Burp Suite Professional(激活的密码) 输入 -&gt; 点击Next(下一步)

8.页面提示：Success(成功) -&gt; 点击Finish(完成)关闭激活注册页面

#### (五)为Burp Suite下载证书

(抓取web服务器https协议 需要安装证书才能抓取数据包)

1.点击：第一步Settings(设置) -&gt; 点击：第二步Proxy(代理) -&gt; 点击：第三步import / export CA certificate(导出CA证书)

2.点击Certificate in DER format(DER格式的证书) -&gt; Next(下一步)

3.保存的目录(文件夹)最好是和Burp Suite其他所有文件在一起(方便查找和修改)

4.点击Next(保存指定目录(文件夹)里)

5.页面提示：The certificate was successfully exported(证书已成功导出) -&gt; 点击close(关闭)<br/>  

##### (6)浏览器安装Burp Suite证书

(Burp Suite抓取浏览器https协议需要安装Burp Suite的证书)<br/> 1.浏览器设置 -&gt; 搜索：证书 -&gt; 点击：安全

2.点击：管理设备的证书

##### 3.为受信任的根证书颁布机构(安装证书)

##### 为中间证书颁发机构(安装证书)

#### 注意：为什么要给两个都安装证书,是因为有的web服务器,需要奇奇怪怪的机构,才能抓取https协议,一次性给它搞定。

##### (六)为Burp Suite下载浏览器代理插件

1.浏览器代理插件名：SwitchyOmega

2.设置代理规则

3.设置代理端口：8080 设置代理ip：127.0.0.1(本地地址)

##### (七)模拟器安装Burp Suite证书

抓取安卓应用(使用协议为http/https的数据包)

1.下载模拟器<br/> 下载逍遥模拟器地址：https://www.xyaz.cn/

###### 2.注意：安装程序一直下一步 注意：目录(文件夹)不要出现中文(防止出现错误,无法正常安装成功)！！！

3.windows+R -&gt; cmd -&gt; config //查看本机ip地址

###### 3.为模拟器下载Burp Suite证书

3.1 Settings设置 -&gt; Proxy(代理) -&gt; Proxy listeners(代理监听) -&gt; ADD(添加)

4.端口：8888(自定义设置) ip：与本机ip地址一致

5.调整状态:Running(状态打勾为开启)

6.模拟器打开浏览器

7.1 设置-开启：Burp Suite代理拦截功能：Proxy(代理) -&gt; Intercept(拦截) -&gt; (intercept is on)正在进行拦截<br/> 7.2 设置-开启：模拟器浏览器应用：输入地址：自己的ip + 设置的端口 -&gt; 回车确认 -&gt; 点击下载CA Certificate(CA证书)

###### 注意：模拟器下载默认保存的路径为：下载共享路径

8.查看下载完成后的模拟器里的浏览器里的Burp Suite证书<br/> 第一步：点击：共享 -&gt; 第二步：点击：安卓图标 -&gt; 第三步：查看是否存在下载完成的Burp Suite证书

9.给.der 更改为 .cer (为给模拟器里的浏览器安装证书做准备)

10.安装证书-1.打开设置

10.安装证书-2.安全性和位置信息

10.安装证书-3.加密与凭据

10.安装证书-4.从SD卡安装

10.安装证书-4.1 继续操作

10.安装证书-4.2 继续操作

10.安装证书-4.3 点击Download(下载共享路径)

10.安装证书-4.4 点击.cer后缀名文件

10.安装证书-4.5 输入密码(模拟器的锁屏密码) -&gt; 回车确定

10.安装证书-4.6 输入证书名称(自定义昵称) -&gt; 点击确定

10.安装证书-4.7 页面提示：已安装Burp Suite

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
