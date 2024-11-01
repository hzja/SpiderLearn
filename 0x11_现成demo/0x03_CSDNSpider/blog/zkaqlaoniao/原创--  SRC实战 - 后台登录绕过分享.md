# 原创
：  SRC实战 | 后台登录绕过分享

# SRC实战 | 后台登录绕过分享

#### 一.挖掘过程简述：

`通过收集到的账号密码进入后进行测试无果，查看登录返回包后修改role_id参数进入管理员后台，后台存在文件上传功能且对文件后缀和内容有检查，后缀检测时前端进行的，可以通过抓包进行修改，对内容有检测要免杀。此外这里还存在csv注入，后面再详细说。`

#### 二.详细过程

1.通过谷歌语法收集到账号和密码。很多隐藏资产可能存在各种文本文件中，这时候就需要用到谷歌语法进行收集，这里列出一个，其他的敏感关键词可以再自己挖掘漏洞多收集和整理

`site:xxx.edu.cn filetype:pdf intext:密码<br/> site:xxx.edu.cn filetype:xls intext:密码`

2.通过默认账号进入系统，一个观看新闻的网站，测试一遍功能无果。脑子急转直下，总感觉有后台，于是退出登录，查看js代码

3.果然存在后台，于是抓登录的包，修改role_id进入后台<br/>  

<br/> 3.发现有文件上传，查看网站指纹(浏览器插件Wappalyzer)时php站点，于是先上传后缀为php的文件，上传失败；于是抓取上传数据包测试发现可以上传php文件但对内容进行检测，这里免杀马了，但是想到只要证明危害就可以了，于是内容写为&lt;?php echo 1 ?&gt;即可，这个语句正常执行，说明存在任意文件上传漏洞。

<br/> 4.测试了一圈发现导出功能，导出来看来一下，发现是”定制管理”中的内容，这不就是刚刚在ctf中刷过的题吗，csv注入<br/>  

<br/> 5.在”定制管理”中添加词目，内容为=1+cmd|’/C calc’!A0，导出文件，打开，成功执行命令。了解了csv注入我们知道，要想利用还得管理员配置且系统的office要开启DDE协议

##### CSV注入漏洞详细描述

1.csv简介<br/> csv全称“Comma-Separated Values”。是一种逗号分隔值格式的文件，是一种用来存储数据的纯文本格式文件。CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由字段组成，字段间的分隔符是其它字符或字符串。

2.csv注入<br/> csv注入是一种将包含恶意命令的excel公式插入到可以导出csv或xls等格式的文本中，当在excel中打开csv文件时，文件会转换为excel格式并提供excel公式的执行功能，会造成命令执行问题

3.注入原理<br/> 1.excel的一个特性：单元格中的第一个字符是“+、-、@、=”这样???符号时，他会以一个表达式的形式被处理

<br/> 然而“=”的作用远不止如此，其还可以用来执行代码。不过在这之前，我们需要先了解什么是DDE。

###### DDE（Dynamic Data Exchange）协议：

`DDE是Windows下进程间通信协议，是一种动态数据交换机制，使用DDE通讯需要两个Windows应用程序，其中一个作为服务器处理信息，另外一个作为客户机从服务器获得信息。DDE支持Microsoft Excel，LibreOffice和Apache OpenOffice。Excel、Word、Rtf、Outlook都 可以使用这种机制，根据外部应用的处理结果来更新内容。因此，如果我们制作包含DDE公式的CSV文件，那么在打开该文件时，Excel就会尝试执行外部应用`

收集该网站的指纹，hunter搜索发现是通用，可惜edu没有收录该企业，但这可以拿去盒子刷一波分

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
