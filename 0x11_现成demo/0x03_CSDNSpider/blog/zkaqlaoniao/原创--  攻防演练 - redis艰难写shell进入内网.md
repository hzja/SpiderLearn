# 原创
：  攻防演练 | redis艰难写shell进入内网

# 攻防演练 | redis艰难写shell进入内网

### 背景

某地市级攻防演练

### 要求

拿到指定单位的靶标系统（必须是web后台管理权限+数据库+服务器）

### 正式开始

#### redis未授权

首先通过信息收集获取到了一些IP，且发现一个IP中存在redis未授权。

<br/> 此时兴冲冲的去尝试写入定时任务反弹shell，主从复制，写入私钥，结果都以失败告终。。。<br/> 小tips：一般fscan会检测是否可以写入定时任务，如果有就直接定时任务弹shell，百试百灵！（下图这种就是能写计划任务的）

#### 获取绝对路径

以上手段尝试无果后，尝试在该IP开放的web服务中扫描目录，结果扫到了一个`phpinfo`页面！且phpinfo中泄漏了站点的绝对路径！这不就柳暗花明又一村了吗！决定直接在redis里写webshell咯！嘿嘿！

<br/> 就在我一脸兴奋的<br/>`config set dir E:/WSPHP/PHPWS/`<br/>`config set dbfilename redis.php`<br/>`set webshell "&lt;?php eval($_POST['zkaq']);?&gt;"`<br/>`save`<br/> 之时，数据库给我返回一个<br/>  

<br/> 瞬间头大了！！！

#### 更改只读权限

秉持着遇事不决，便问百度的原则，我查到了两个办法

<br/> 方法一需要服务器权限，且需要重启服务，很显然咱们不具备这个条件，也没这个胆量，怕重启起不来人就傻了，只能用方法二尝试一下了，结果还真的可以了！

#### 写入webshell

更改好权限，又有绝对路径后，终于可以愉快的写shell了，结果在连上的一瞬间，看见站点的根目录下已经存在很多webshell文件了，果然在每一个你所向往的林荫小路中，其实早已车水马龙，不过幸好目标单位还没下线，还可以再吃点分！

#### 获取服务器权限

拿到webshell可以执行命令后，自然就是风哥教我的搭建隧道，创建用户一条龙了！<br/> 成功登录RDP后，就获取到了服务器权限，成功了三分之一了！加油！

#### 获取数据库权限

获取到服务器权限后，扔进去一个searchall跑了一下，获取到了数据库凭证！并成功获取了数据库权限！成功了三分之二了！<br/> （searchall还是很好用的，项目地址在这里  https://github.com/Naturehi666/searchall )

#### web权限

随后在服务器中装了一个绿色版everthing成功找到了靶标系统的源码，且在数据库中找到其登录凭证后，以为马上就要吃到靶标分时，结果在外网死活找不到他的资产了！最终在服务器中源码的js文件中找到一个唯一值，并在资产测绘中搜索该唯一值，好消息是找到了！坏消息是关站了！！没得办法，只能在内网中截了一张图，去跟裁判battle了。

### 至此，对要求的靶标系统的服务器、数据库、后台已经完全获取到！有什么不足的地方，欢迎大家互相指出！

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
