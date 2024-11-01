# 原创
：  对HW 钓鱼简单样本分析以及制作

# 对HW 钓鱼简单样本分析以及制作

记录某个对某个钓鱼事件中获取的钓鱼样本进行分析，以及简单的制作学习<br/> 样本行为分析<br/> 首先看到是 qq 邮箱发来的某个压缩包大概本身是带密码的，反手就丢到虚拟机先看下大概文件，解压后是这样的一个快捷方式<br/>  

<br/> 然后打开属性查看快捷方式，看到他运行了一个 rundll32.exe 的文件，应该很多人已经知道这是为了调恶意的 dll，但一看就一个 rundll32.exe 后面全被空格隐藏了后面的命令执行<br/>  

<br/> 但解压开确只有一个 lnk，小问题，我们打开 cmd 命令执行 dir /a<br/>  

<br/> 我们只需通过该命令<br/> attrib -s -a -h -r C:\Users\14022\Desktop\北京交通大学-xxxx\北京交通大学-xxxx.pdf<br/> 就可以将该恶意脚本显示，不然无论查看如何设置都是不行的<br/>  

<br/> 显示出来后，看到 rundll32.exe 驱动的就是这个 dll(这个pdf后缀的文件就是将dll文件改成pdf后缀然后用rundll32来进行运行)，显然这就是那个可恶的马仔了，立即拿出我的 ida pro 丢进去分析一手<br/> 好小子，居然是 apc 注入将 shellcode 注入进 rundll32 进程最后远控会连

继续往下摸索看到了该远控指向的地址www.microsoftdnsserver.xyz:2087，这个丢微步的云沙箱也可以解析分析到，全局搜索

确实是为恶意域名<br/> 样本简易制作方式解析<br/> 首先是对快捷方式的参数的隐藏，这里笔者做了一个简单的 python 脚本作为例子，具体展示在参数这块

因为快捷方式只能容纳 260 个字符，我在参数添加了 n 个空格作为隐藏，其真实参数为/k calc 为启动一个计算机的操作，运行生成 cmd_shortcut.lnk<br/>  

<br/> 打开属性进行查看,参数也依然被隐藏

点击后弹出计算机

完成了病毒样本做的第一个恶意样本操作之后我们接下来就对 pdf 的隐藏，这块也算比较简单，我直接贴命令演示<br/> attrib +s +h C:\Users.…\Desktop\1.txt 参数后面为需要隐藏的文件，这样也就完成了对该病毒样本的简单分析与制作

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
