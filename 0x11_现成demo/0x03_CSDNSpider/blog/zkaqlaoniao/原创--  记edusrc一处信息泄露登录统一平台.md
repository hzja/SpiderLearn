# 原创
：  记edusrc一处信息泄露登录统一平台

# 记edusrc一处信息泄露登录统一平台

> 
<h3>本文由掌控安全学院 - sbhglqy 投稿</h3>


**目录**

[前言](#%E5%89%8D%E8%A8%80)

[测试思路](#%E6%B5%8B%E8%AF%95%E6%80%9D%E8%B7%AF)

[免费领取安全学习资料包！​](#%E5%85%8D%E8%B4%B9%E9%A2%86%E5%8F%96%E5%AE%89%E5%85%A8%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99%E5%8C%85%EF%BC%81%E2%80%8B%E7%BC%96%E8%BE%91)

---


### 前言

我们都知道像大学之类的各种平台的登录账号基本上是学号，初始登录密码基本上是学生身份证的后6位再拼接上一些带有学校缩写的英文字母。所以我们在找漏洞的时候可以换一种思路，先通过去找身份证信息或者是有固定初始密码的平台来尝试，这样子成功的概率就会比较大。

### 测试思路

1.谷歌语法搜索：`inurl:"edu.cn" intext:"初始密码"`，如果看到初始密码是一串固定的字符串，就可以先去测试一下了，这里就找到了一处。<br/>  

<br/> 可以看到该学校的邮箱登录初始密码是stu123456，账号是学籍号。那么下一步我们就可以去搜索学籍号了。<br/> 2.谷歌语法搜索：`inurl:"xxx.edu.cn" intext:"学号"`。此处找的学号尽量找近几年的，因为太早的账号估计都被禁用了，这里找到了一份最近的。<br/>  

<br/> 3.上该学校的邮箱网站，一个一个账号去尝试，发现都登录不进去，大概率是都改密码了吧。<br/>  

<br/> 4.这个不行，但是至少获取到了学号，可以再去看看其他的平台。也是运气好，再搜索学号的时候，发现了另外一条信息。<br/>  

<br/> 有一个网络教学平台，账号为学号，密码为身份证的后6位，那么问题就又回到了寻找身份证号上。<br/>  

<br/> 5.谷歌语法搜索：`inurl:"xxx.edu.cn" intext:"身份证"`，有找到一个表格，下载下来。下面是一部分截图，总共是三千多条数据。它隐去了中间的6位数，但是最后6位没有隐藏。<br/>  

<br/> 6.编写python脚本，把每一条数据的身份证号的后6位存到另外一个文件里。
1.  `import csv` 1.   1.  `xuehao = []` 1.  `with open("1.csv", 'r') as file:` 1.  `reader = csv.reader(file)` 1.  `for row in reader:` 1.  `xuehao.append(row[1])` 1.   1.  `xuehao.remove("身份证号")` 1.  `# print(xuehao[1][-6:])` 1.  `with open("shenfenzhenghao.txt", 'a') as f:` 1.  `for i in xuehao:` 1.  `f.write(i[-6:] + "\n")` 
7.访问网络教学平台，利用收集到的学号和身份证号进行尝试，发现多个账号都可以登录。<br/>  

可以查看当事人的一些相关信息了。

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/3fa9779836d04275b431e00128814776.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/699e7ae690ac4aaa8dfe3e230ed68af7.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/d717af593a5747a48201f69678754167.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/e4a7473f6ee34e6c98997513b332dbbf.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/fd1f3a65016b41cab179b2aae1ed1fae.png" width="665"/>

应急响应笔记

学习路线
