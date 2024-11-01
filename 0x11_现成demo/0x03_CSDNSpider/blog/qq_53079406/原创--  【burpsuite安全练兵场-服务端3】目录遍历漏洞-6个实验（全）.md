# 原创
：  【burpsuite安全练兵场-服务端3】目录遍历漏洞-6个实验（全）

# 【burpsuite安全练兵场-服务端3】目录遍历漏洞-6个实验（全）

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
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点： 
（1）通过目录遍历阅读任意文件（√）
（2）利用文件路径遍历漏洞的常见障碍（√）
（3）如何防止目录遍历攻击（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|服务端专项|所需基础知识|学习目标|状态
|[【0X01】SQL注入-17个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128434815?spm=1001.2014.3001.5501)|1、数据库基本语法| 1、掌握SQL注入方法 2、掌握不同注入的区别 3、掌握注入的意义，即可以发现的信息 |已发布
|[【0X02】身份认证漏洞-16个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128454196?spm=1001.2014.3001.5501)| 1、基本信收集 2、爆破工具的使用（如BP） 3、需要一点的逻辑分析能力 | 1、掌握身份验证的方法 2、掌握对数据包差别的细微分析 3、掌握身份认证的基本逻辑 |已发布
|[【0X03】目录遍历漏洞-6个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128487462?spm=1001.2014.3001.5501)|1、对于路径的敏感度| 1、掌握路径模糊查询（爆破） 2、掌握基本的绕过方法 |已发布
|[【0X04】操作系统命令注入-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128495612?spm=1001.2014.3001.5501)| 1、基本操作系统命令（可慢慢接触后学） 2、带外的平台（可慢慢发现） 3、带外的服务器（实验可使用BP提供的） | 1、掌握基本命令 2、掌握BP提供的服务器 3、掌握拼拼接命令 |已发布
|[【0X05】业务逻辑漏洞-11个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128509488?spm=1001.2014.3001.5501)| 1、需要会基本的BP使用能力（后期可不断提高）  2、基础的数据包分析能力（可不断提升） | 1、掌握如何分析业务逻辑 2、掌握业务逻辑的可能缺陷 3、掌握业务逻辑的第三方功能 |已发布
|[【0X06】信息泄露漏洞-5个实验（全）](https://blog.csdn.net/qq_53079406/article/details/128544645?spm=1001.2014.3001.5501)| 1、需要会一些发现的工具（后期可不断使用新工具） 2、需要会一点Linux基本工具命令 | 1、掌握BP信息收集的工具的使用方法 2、掌握常见的信息泄露及其获取方法 |已发布
|【0X07】访问控制|即将发布，敬请期待|——|——
|【0X08】文件上传|即将发布，敬请期待|——|——
|【0X09】服务端请求伪造SSRF|即将发布，敬请期待|——|——
|【0X10】XEE注射|即将发布，敬请期待|——|——
</tbody></table>


---


**目录**

[一、目录遍历](#%E4%B8%80%E3%80%81%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86)

[1、意义](#1%E3%80%81%E6%84%8F%E4%B9%89)

[二、通过目录遍历阅读任意文件](#%E4%BA%8C%E3%80%81%E9%80%9A%E8%BF%87%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E9%98%85%E8%AF%BB%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6)

[1、示例](#1%E3%80%81%E7%A4%BA%E4%BE%8B)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%AE%80%E5%8D%95%EF%BC%89)[实验1：文件路径遍历（简单）](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%AE%80%E5%8D%95%EF%BC%89)

[三、利用文件路径遍历漏洞的常见障碍](#%E4%B8%89%E3%80%81%E5%88%A9%E7%94%A8%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E%E7%9A%84%E5%B8%B8%E8%A7%81%E9%9A%9C%E7%A2%8D)

[1、对于../等的限制](#1%E3%80%81%E5%AF%B9%E4%BA%8E..%2F%E7%AD%89%E7%9A%84%E9%99%90%E5%88%B6)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%94%A8%E7%BB%9D%E5%AF%B9%E8%B7%AF%E5%BE%84%E6%97%81%E8%B7%AF%E9%98%BB%E6%AD%A2%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)[实验2：文件路径遍历（用绝对路径旁路阻止遍历序列）](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%94%A8%E7%BB%9D%E5%AF%B9%E8%B7%AF%E5%BE%84%E6%97%81%E8%B7%AF%E9%98%BB%E6%AD%A2%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)

[2、嵌套遍历序列](#2%E3%80%81%E5%B5%8C%E5%A5%97%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E9%9D%9E%E9%80%92%E5%BD%92%E5%9C%B0%E5%89%A5%E7%A6%BB%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)[实验3：文件路径遍历（非递归地剥离遍历序列）](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E9%9D%9E%E9%80%92%E5%BD%92%E5%9C%B0%E5%89%A5%E7%A6%BB%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)

[3、编码绕过](#3%E3%80%81%E7%BC%96%E7%A0%81%E7%BB%95%E8%BF%87)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%94%A8%E5%A4%9A%E4%BD%99%E7%9A%84URL%E8%A7%A3%E7%A0%81%E5%89%A5%E7%A6%BB%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)[实验4：文件路径遍历（用多余的URL解码剥离遍历序列）](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%94%A8%E5%A4%9A%E4%BD%99%E7%9A%84URL%E8%A7%A3%E7%A0%81%E5%89%A5%E7%A6%BB%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%EF%BC%89)

[4、基文件夹开头](#4%E3%80%81%E5%9F%BA%E6%96%87%E4%BB%B6%E5%A4%B9%E5%BC%80%E5%A4%B4)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E9%AA%8C%E8%AF%81%E8%B7%AF%E5%BE%84%E8%B5%B7%E5%A7%8B%EF%BC%89)[实验5：文件路径遍历（验证路径起始）](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E9%AA%8C%E8%AF%81%E8%B7%AF%E5%BE%84%E8%B5%B7%E5%A7%8B%EF%BC%89)

[5、文件扩展名固定](#5%E3%80%81%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D%E5%9B%BA%E5%AE%9A)

[        ](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%A9%BA%E5%AD%97%E8%8A%82%E6%97%81%E8%B7%AF%E9%AA%8C%E8%AF%81%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D%EF%BC%89)[实验6：文件路径遍历（空字节旁路验证文件扩展名）](#%E5%AE%9E%E9%AA%8C6%EF%BC%9A%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%EF%BC%88%E7%A9%BA%E5%AD%97%E8%8A%82%E6%97%81%E8%B7%AF%E9%AA%8C%E8%AF%81%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D%EF%BC%89)

[四、如何防止目录遍历攻击](#%E5%9B%9B%E3%80%81%E5%A6%82%E4%BD%95%E9%98%B2%E6%AD%A2%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%94%BB%E5%87%BB)

---


> 
<h2> <img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>助你一臂之力</h2>
<h3>📋问题1：如何快速发现漏洞点的？</h3>
🎯编写自动化脚本跑，BP跑
🎯如发现特定框架等，使用特定的目录字典进行跑
🎯特殊字符字典搜集
<hr/>
<h2>📋问题2：使用的工具有哪些？</h2>
🎯BP必备（爆破跑的时候，HTTP历史记录收集收集）
🎯dirsearch.py、御剑等


## 📋问题2：使用的工具有哪些？

> 
<h2>一、目录遍历</h2>
<h3>1、意义</h3>
1、目录遍历（也称为文件路径遍历）是一个Web安全漏洞，使得攻击者能够读取运行应用程序的服务器上的任意文件（包括应用程序代码和数据、后端系统的凭据以及敏感的操作系统文件）
<hr/>
2、在某些情况下，攻击者可能能够写入服务器上的任意文件，从而允许他们修改应用程序数据或行为，并最终完全控制服务器


---


---


> 
<h2>二、通过目录遍历阅读任意文件</h2>
<h3>1、示例</h3>
<pre><code>1、销售商品图像的购物应用程序：
图像通过HTML加载，如
&lt;img src="/loadImage?filename=218.png"&gt;


该loadImage图像URL采用filename参数并返回指定文件的内容

映像文件本身存储在磁盘上的位置/var/www/images/。为返回映像，应用程序将请求的文件名附加到此基目录，并使用文件系统API读取文件的内容。

文件路径：/var/www/images/218.png
</code></pre>
<br/>  
<pre><code>2、攻击者：

如果应用程序未对目录遍历进行防御，请求以下URL，从服务器的文件系统中检索任意文件： 
https://insecure-website.com/loadImage?filename=../../../etc/passwd

这将导致应用程序从以下文件路径读取：
/var/www/images/../../../etc/passwd
（../表示向上一级目录）

Unix的操作系统上：  ../
Windows：         ../ and ..\ 都是有效的目录遍历序列

系统文件：
https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini</code></pre>
<hr/>
涉及实验：
实验1：文件路径遍历（简单）



> 
<h3>实验1：文件路径遍历（简单）</h3>
信息：
需要我们检索/etc/passwd的内容
<hr/>
part1:
随便点开一个博客
（同时抓包）
第三个数据包就带有filename参数进行检索内容，修改filename参数


<hr/>
part2:
发送到repeater进行分析
../../../etc/passwd
检索出了密码

在拦截的数据包中修改后取消拦截




---


---


---


## 三、利用文件路径遍历漏洞的常见障碍

> 
<h3>1、对于../等的限制</h3>
1、将用户输入放置到文件路径中的应用程序实现了某种类型的防御路径遍历攻击，而这些攻击通常可以被绕过
————
2、如果应用程序从用户提供的文件名中剥离或阻止目录遍历序列，那么就有可能使用各种技术绕过防御
如，使用文件系统根目录的绝对路径（filename=/etc/passwd）直接引用文件，而不使用任何遍历序列。
————
涉及实验：
实验2：文件路径遍历（用绝对路径旁路阻止遍历序列）


> 
<h3>实验2：文件路径遍历（用绝对路径旁路阻止遍历序列）</h3>
信息：
绝对路径/etc/passwd
<hr/>
part1：
点击一个博客

 第三个数据包的filename参数

<hr/>
part2：
发到repeater
题目提示的绝对路径/etc/passwd
账号密码回显

 修改数据包，并关闭拦截

 <img alt="" height="704" src="https://img-blog.csdnimg.cn/df1c7fc840b447bba87c5e53417918ae.png" width="1200"/>



---


---


> 
<h3>2、嵌套遍历序列</h3>
如....// or ....\/ ，当内部序列被剥离时（过滤一遍），它将恢复为简单的遍历序列
————
涉及实验：
实验3：文件路径遍历（非递归地剥离遍历序列）


> 
<h3>实验3：文件路径遍历（非递归地剥离遍历序列）</h3>
信息：
还是告诉了/etc/passwd
<hr/>
part1：
拦截到第三个数据包


<hr/>
part2：
发送到repeater
使用嵌套遍历....//....//....//etc/passwd


数据包修改，并关闭拦截

 <img alt="" height="695" src="https://img-blog.csdnimg.cn/6d1a9d1a3ed749af95dada8a7c5163a5.png" width="1200"/>



---


---


> 
<h3>3、编码绕过</h3>
1、除去遍历序列：在某些上下文中，如在URL路径或filename的参数multipart/form-data请求时，Web服务器可能会在将输入传递到应用程序之前去除任何目录遍历序列。
2、编码绕过：有时可以通过URL编码或甚至双URL编码来绕过这种清理，../ 字符，一次编码%2e%2e%2f、二次编码%252e%252e%252f。各种非标准编码，如..%c0%af或..%ef%bc%8f，也可能起到作用
3、工具：BP Intruder提供了一个预定义的负载列表（将GitHub或自己收集的特殊编码导入，观察哪些可以使用），其中包含各种可供尝试的编码路径遍历序列。 
<hr/>
涉及实验：
实验4：文件路径遍历（用多余的URL解码剥离遍历序列）


> 
<h3>实验4：文件路径遍历（用多余的URL解码剥离遍历序列）</h3>
信息：
还是告诉了/etc/passwd
<hr/>
part1：
拦截到第三个数据包


<hr/>

part2：
发送到repeater

URL编码一次

URL编码二次
<img alt="" height="426" src="https://img-blog.csdnimg.cn/abe4c514019d4511834ef64b54145162.png" width="1200"/> 使用编码绕过..%252f..%252f..%252fetc/passwd



数据包修改，并关闭拦截

 <img alt="" height="600" src="https://img-blog.csdnimg.cn/7df0afdc8d5a44dfb14006e93cf503d6.png" width="1200"/>



---


---


> 
<h3>4、基文件夹开头</h3>
要求用户提供的文件名必须以预期的基文件夹开头
如，/var/www/images
需要包括基本文件夹，加上遍历序列：
filename=/var/www/images/../../../etc/passwd
<hr/>
涉及实验：
实验5：文件路径遍历（验证路径起始）


> 
<h3>实验5：文件路径遍历（验证路径起始）</h3>
信息：
还是告诉了/etc/passwd
<hr/>
part1：
拦截到第四个数据包



<hr/>
part2：
发送到repeater
带基路径的遍历/var/www/images/../../../etc/passwd



数据包修改，并关闭拦截




---


---


> 
<h3>5、文件扩展名固定</h3>
应用程序要求用户提供的文件名必须以预期的文件扩展名（如.png）结尾，则可以使用空字节在所需扩展名之前有效地终止文件路径，如
filename=../../../etc/passwd%00.png（实战中可能得考虑更多办法，如在hex中改为%0a换行截断等方法）
<hr/>
涉及实验：
实验6：文件路径遍历（空字节旁路验证文件扩展名）


> 
<h3>实验6：文件路径遍历（空字节旁路验证文件扩展名）</h3>
信息：
还是告诉了/etc/passwd
<hr/>
part1：
拦截到第三个数据包




<hr/>
part2：
发送到repeater
直接上路径，可能没什么有用报错信息
就得结合场景自己尝试了（原文件为图片，就可能会检测后缀，如果是上传，就可能还会检测文件类型了）


带上图片的后缀，并空字节截断后缀
../../../etc/passwd%00.png




数据包修改，并关闭拦截




---


---


---


> 
<h2>四、如何防止目录遍历攻击</h2>
1、防止文件路径遍历漏洞的最有效方法是完全避免将用户提供的输入传递给文件系统API。许多执行此操作的应用程序函数可以重写，以便以更安全的方式提供相同的行为。
<hr/>
2、如果认为将用户提供的输入传递给文件系统API是不可避免的，那么应该同时使用两层防御来防止攻击：
————
（2）白名单（输入前）：应用程序应该在处理用户输入之前对其进行验证。理想情况下，验证应该与允许值的白名单进行比较。如果对于所需的功能来说这是不可能的，那么验证应该验证输入是否只包含允许的内容，比如纯字母数字字符。
————
（2）符合路径规范（输入后）：验证提供的输入后，应用程序应将输入附加到基目录，并使用平台文件系统API规范化路径。应用程序应验证规范化路径是否从预期的基目录开始。


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
|看雪众测（物联网）|[看雪渗透测试服务](https://ce.kanxue.com/)
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

