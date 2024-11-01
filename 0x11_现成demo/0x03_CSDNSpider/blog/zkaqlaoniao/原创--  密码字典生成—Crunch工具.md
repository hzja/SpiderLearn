# 原创
：  密码字典生成—Crunch工具

# 密码字典生成—Crunch工具

## Crunch

## 一、简介

Crunch是一种创建密码字典工具，按照指定的规则生成密码字典，可以灵活的制定自己的字典文件。使用Crunch工具生成的密码可以输出到屏幕，保存到文件、或另一个程序。知道密码的一部分细节后，可以针对性的生成字典。

## 二、优缺点

###### 1.优点
1.  Crunch可以以组合和排列的方式生成字典 1.  它可以通过行数或文件大小中止输出 1.  现在支持恢复 1.  现在支持数字和符号模式 1.  现在分别支持大小写字符模式 1.  在生成多个文件时添加状态报告 1.  新的-l选项支持@，%^ 1.  新的-d选项可以限制重复的字符，可以通过man文件查看详细信息 1.  现在支持unicode 
###### 2.缺点
1.  键盘空间字符爆破量太大 
#### 三、安装

1.安装地址

> 
https://github.com/crunchsec/crunch<br/> https://github.com/jaalto/external-sf--crunch-wordlist


2.在Kali上进行安装

> 
输入命令：apt-get install crunch ，即可。


#### 四、主要功能介绍

###### 1.基本语法

> 
crunch &lt;min-len&gt; &lt;max-len&gt; [&lt;charset string&gt;] [options]<br/> crunch 密码最小长度 密码最大长度 [字符集] [命令选项]


###### 2.命令介绍

> 
-o START # 输出字典，输出的字典是从小到大的排序。<br/> crunch 6 6 0123456789 -o start # 生成6位数，由0到9位数字组成的，从小到大排序的字典。


> 
-b 1mb 按大小分割字典文件。<br/> -c 100 按行数分割字典文件。


> 
-d 2 # 同意字符能够连贯出现的数量。比如11X11X<br/> crunch 6 6 0123456789 -d 2 # 生成6位数，由0到9位数字组成的，同一字符最多连续出现2次的字典。


> 
-f /usr/share/crunch/charset.lst lalpha-sv # 使用定义好的字符集<br/> crunch 4 4 -f /usr/share/crunch/charset.lst numeric -o 1.txt # 使用数字的字符集去生成4位数的字典。


> 
-p 1234567890 # 无重复字符，注意-p必须是最后一个参数，最大最小字符失效但必须有，与-s、参数不兼容。<br/> crunch 1 1 -p abc # 生成abc的组合的字典


> 
-s 999 # 指定起始点<br/> crunch 5 5 0123456789 -s 99990 # 生成的字典中是以99990为初始点的。


> 
-q 1.txt # 读取文件中每行内容作为基本字符，以排列组合的方式生成字典<br/> crunch 1 1 -q 1.txt # 以文件中每行内容作为基本字符，以排列组合的方式生成字典，最大最小字符失效但必须有


> 
-t @,%^ 字典组成规则。@小写字母；,大写字母；%数字；^符号<br/> crunch 6 6 -t @,%%^^# # 生成6位数的字典，满足【小写字母+大写字母+数字+数字+符号+符号】的形式。


> 
-z 输出文件压缩，有7z、gzip、bzip2、lzma<br/> crunch 4 4 -t @,%^ -o 1.txt -z 7z # 生成四位数的字典，满足【小写字母+大写字母+数字+符号】的形式，输出文件名为1.txt，压缩成7z格式。


###### 3.高级应用

> 
crunch 4 4 -f /usr/share/crunch/charset.lst mixalpha-numeric-all-space -o w.txt -t @d@@ -s cdab<br/> 解释：生成4个字符形式的字典，选用字符集mixalphanumeric-all-space，输出文件名为w.txt，满足【小写字母+d+小写字母+小写字母】的样式，起始字典为cdab


> 
crunch 4 5 -p dog cat bird<br/> 解释：生成字典的组成为dog、cat、bird。前面的min-length、max-length失效。


> 
crunch 5 5 abc DEF + !@# -t ,@^%,<br/> 解释：生成5个字符形式的字典，字符集从abc、DEF、！@#中其中一个选取，满足【大写字母+小写字母+特殊符号+数字+大写字母】的样式。其中\是转义字符，+是占位符。


> 
crunch 5 5 -t ddd%% -p dog cat bird<br/> 解释：生成字典的组成为dog、cat、bird。前面的min-length、max-length失效。任何不同于-p参数指定的值都是占位符。所以-t后面的ddd是占位符，%是数字，所以生成的字典组成是dogcatbird01等等


> 
crunch 5 5 -d 2@ -t @@@%%<br/> 解释：生成5个字符形式的字典，其中小写字母不能连续超过两个，满足的形式为【小写字母+小写字母+小写字母+数字+数字】。


###### 4.组合应用

由于电脑的原因，这里就不再演示。组合应用是直接将生成的字典提供给其他工具使用，因为如果字典文件过大，保存为一个文件是不适合的，这时候直接与其他工具使用，效率更好。

> 
crunch 2 4 0123456789 | aircrack-ng a.cap -e MyESSID -w-<br/> 解释：生成2~4个字符形式的字典，字典组成为0到9，并将生成的字典直接给aircrack工具使用。
crunch 10 10 12345 -stdout | airolib-ng testdb -import passwd -<br/> 解释：生成10个字符形式的字典，字典组成为1到5，并将生成的字典直接给airolib-ng工具使用。


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
