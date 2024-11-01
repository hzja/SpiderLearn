# 原创
：  验证码识别插件-captcha-killer

# 验证码识别插件-captcha-killer

## 前言

想必大家都会使用burp进行爆破,当遇到带验证码的登录表单进行爆破时,基本尝试抓包后观察验证码是否主动更新,或者进行验证码绕过(我是十八期萌新,听风风说的有这个方法,但我还没学到),机缘巧合下我接触到了captcha-killer这个插件,可以提供给大家第三种爆破思路（插件可以从GitHub下载)<br/> (https://github.com/c0ny1/captcha-killer)

### 什么是captcha-killer?

总的来说,它是个用Java写的插件,可以无缝衔接于burp.但是他只是一个调用接口,并不进行识别的操作,真正进行验证码识别处理的是两个个用Python脚本(codereg.py)调用的两个接口(ddddocr和aiohttp), 稍后我会进行简明的介绍<br/> captcha-killer设计理念是只专注做好对各种验证码识别技术接口的调用, 说具体点就是burp通过这一个插件，就可以适配各种验证码识别接口，无需重复编写调用代码.<br/> 今天不谈编码层面如何实现(主要是我也不会)，感兴趣的同学可以去github看源码. 此篇文章只通过使用步骤来说明使用方法

### 简要介绍codereg.py

个人理解,这个脚本的整体识别流程是通过python在本地开启一个验证码识别的web接口来接收captcha-killer传来的验证码图片内容，然后调用识别服务(利用机器学习)来识别，最后返回结果给captcha-killer.

---


---


## 正题

**ok废话不多说,这里是正题!!!!!!!!!!!!**

### 1.安装插件

首先打开burp,选择Extender——&gt;Add（默认Java类型插件）————&gt;Select File——&gt;选择下载的captcha-killer-modified-jdk14.jar文件

发现任务栏里多出一个captcha-killer,就说明安装成功,如下图↓

---


---


### 2.获取目标网站验证码

#### (1)找到要爆破的网站并打开burp,我找到了一个网站作为案例(并未进行爆破)

#### (2)开始抓包,点击验证码刷新,拦截此次请求

#### (3)鼠标右键,将这个包发送到captcha-killer模组里

[‘extensions’—-&gt;’captcha-killer’—&gt;’send to captcha panel’]

#### (4)点击任务栏里的插件模组,可以看到数据包已经自动填入,点击获取按钮,可以获取数据包内的图片验证码,此时获取验证码的流程已经走完,接下来的任务是进行识别

### 3.开启本地验证码识别服务

本文实验的python版本环境：Python 3.9.4

#### (1)python中安装ddddocr和aiohttp包

和其他第三方包的安装方式一样,在dos命令中写入以下命令
1.  `pip install ddddocr aiohttp -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com` 
这样就是安装成功了

#### (2)用python运行codereg.py脚本

打开命令控制台(建议在当前文件夹下打开cmd,不用填路径也不用配环境变量)<br/> 运行以下脚本
1.  `python codereg.py` 
<br/> 显示ddddocr(本地验证码识别的web接口)已经运行成功,此时的接收端口为8888.<br/> 注意,这个dos面板不能关掉,否则ddddocr不会继续运行,也就不能进行识别了

#### (3)在burp的captcha页面配置接口URL和请求模板（Request template）
1.  `POST /reg HTTP/1.1` 1.  `Host: 127.0.0.1:8888` 1.  `Authorization:Basic f0ngauth` 1.  `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0` 1.  `Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8` 1.  `Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2` 1.  `Accept-Encoding: gzip, deflate` 1.  `Connection: keep-alive` 1.  `Upgrade-Insecure-Requests: 1` 1.  `Content-Type: application/x-www-form-urlencoded` 1.  `Content-Length: 8332` 1.   1.  `&lt;@BASE64&gt;&lt;@IMG_RAW&gt;&lt;/@IMG_RAW&gt;&lt;/@BASE64&gt;` 
将以上代码直接复制进插件页面的左下角的请求模板中,填写url为http://127.0.0.1:8888

点击识别之后通过ddddocr进行了机器学习的识别,可以看到dos面板开始进行了一系列操作

此时可在右边的结果栏看到识别成功(这个第一张示例验证码比较复杂,所以识别失误了),但问题不大,识别简单的验证码成功率为百分之99.9%,复杂的验证码就别用这个插件了

以上就是配置识别验证码的接口配置完成,接下来进行批量化处理的教学

### 4.最终步骤:将验证码识别与爆破结合

#### (1)按正常步骤进行账号密码验证的抓包

打开拦截开关,抓取登录操作的数据包

#### (2)发送到intruder模块

和正常的爆破一样,发送到入侵者模块

#### (3)对密码和验证码添加攻击字段标记并选择pitchfork模式

#### (4)字段1对应密码,选择字典

payload页面字段1选一个爆破密码的字典

#### (5)字段2对应captcha-killer模块

第二个payload是验证码的值<br/> 线程2选择继承插件模式<br/> 继承插件选择captcha-killer

#### (6)一定注意选择单线程

线程池为单线程，否则验证码识别会交叉出现错误,很好理解,因为页面的验证码会一次一换,如果不是一一对应的关系就会出现验证码错误.

#### (7)最终开始攻击,就会实现密码和验证码一一对应的爆破了

<br/> ↑此图为本机测试,并未进行未授权攻击

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
