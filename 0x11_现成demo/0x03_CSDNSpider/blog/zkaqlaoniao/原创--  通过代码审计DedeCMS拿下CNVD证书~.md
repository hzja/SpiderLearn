# 原创
：  通过代码审计DedeCMS拿下CNVD证书~

# 通过代码审计DedeCMS拿下CNVD证书~

### DedeCMS V5.7.104存在任意文件删除

漏洞位置: /dede/album_add.php<br/> 第 237 行 - 第 250 行

<br/> 代码分析:
1.  $albumUploadFiles 数据不为空进入 if循环 1.  Stripslashes 删除反斜杠 并且将albumUploadFiles的内容json格式 1.  循环files数组内容 1.  DEDEDATA是一个常量为当前绝对路径/data/uploadtmp 这里是会移动到这个目录当中 1.  $tmpfile = $uploadtmp./我们的文件名称 1.  第244 - 249 并没有对$tmpfile做任何操作 1.  第249行将$tmpfile = $uploadtmp./我们的文件名称移动到我们244-249的所创建的文件当中 1.  250将$tmpFile的文件删除 没有任何限制<br/> 漏洞复现: 
<br/> 1.将内容填写完毕并且选择手工上传的位置上传我们的png图片往下面翻有直接点击确定

<br/> 2.点击确定后会显示这样的页面

<br/> 3.利用burp工具进行抓包修改数据 抓取当前页面默认会有数据传输<br/> 抓取后往下面翻

<br/> 这里是得到的json格式数据 我们可以通过手动的方式修改我们的1-21442Y3V.png 那么这里是上面上传的临时文件名 这里会进行删除 我们通过手动方式修改<br/> 4.我在我的源码当中的根目录创建了一个文件 先做演示

<br/> 5.我们通过上面的审计得到data/文件名称 为我们的临时位置<br/> Payload<br/> 修改为../../lynn.txt

<br/> 提交数据<br/> 数据已被删除

<br/> 利用任意文件删除<br/> 我们去删除连接数据库文件<br/> 利用文件式管理器

<br/> 我们是删除不了的会提示

<br/> 利用我们的任意删除<br/> Payload<br/> ../common.inc.php | 即可删除我们的连接数据库文件

<br/> 我们正常访问页面

<br/> 页面显示空白

### 附上证书

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
