# 原创
：  【目录爆破工具】信息收集阶段：robots.txt、御剑、dirsearch、Dirb、Gobuster

# 【目录爆破工具】信息收集阶段：robots.txt、御剑、dirsearch、Dirb、Gobuster

**目录**

[一、robots.txt](#%E4%B8%80%E3%80%81robots.txt)

[1.1、简介：](#%C2%A0%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、理解：](#%E7%90%86%E8%A7%A3%EF%BC%9A)

[二、御剑](#%E4%BA%8C%E3%80%81%E5%BE%A1%E5%89%91)

[2.1、下载：](#%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.2、使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[三、dirsearch](#%E4%B8%89%E3%80%81dirsearch)

[3.1、下载：](#%C2%A0%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[3.2、基础使用：](#%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%EF%BC%9A)

[四、Dirb](#articleContentId)

[4.1、简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[4.2、使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[基础：](#%E5%9F%BA%E7%A1%80%EF%BC%9A)

[扫描：](#%E6%89%AB%E6%8F%8F%EF%BC%9A)

[五、Gobuster](#%E4%BA%94%E3%80%81Gobuster)

[5.1、简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[5.2、下载：](#%C2%A0%E4%B8%8B%E8%BD%BD%EF%BC%9A)

---


## 一、robots.txt

> 
<h3>1.1、简介：</h3>
谈到目录，第一个应该想到查看robots.txt文件
<hr/>
<h3>1.2、理解：</h3>
[【robots协议】简介、理解<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5501)


### 1.2、理解：

---


---


## 二、御剑

> 
<h3>2.1、下载：</h3>
网上可以搜到，在此就不放链接了
<hr/>
<h3>2.2、使用：</h3>
一看就会的东西




### 2.2、使用：

---


---


## 三、dirsearch

> 
<h3>3.1、下载：</h3>
kail中是自带的
[GitHub - maurosoria/dirsearch: Web path scanner<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch)Python 3.7及以上
如果是在Windows里面下载
打开使用后，提示：缺少所需的依赖项
然后输入Y，进行安装


> 
<h3>3.2、基础使用：</h3>
dirsearch.py [-u|--url] target（具体URL） [-e|--extensions] extensions（扩展） [options]
<hr/>
-u 指定url
-e 指定网站语言
-w 可以加上自己的字典（带上路径）
-r 递归爆破（查到一个目录后，在目录后再爆破）
--random-agents 代理（代理目录在uesr-agents.txt中，可自己添加）
……


---


---


## 四、Dirb

> 
<h3>4.1、简介：</h3>
作用：
信息收集工具（kail自带）
<hr/>
目的：
基于字典的web目录扫描工具，查找现有的（隐藏的）Web对象
<hr/>
方法：
对Web服务器发起基于字典的攻击并分析响应的数据。 采用递归的方式来获取更多的目录，支持代理和http认证限制访问的网站


---


> 
<h3>4.2、使用：</h3>
<h4>基础：</h4>
格式：dirb &lt;url_base&gt; [&lt;wordlist_file(s)&gt;] [options]
<table border="1" cellpadding="1" cellspacing="1"><tbody>|参数|作用
|-a|设置user-agent
|-p&lt;proxy[:port]&gt;|设置代理
|-c|设置cookie
|-z|添加毫秒延迟，避免洪水攻击
|-o|输出结果
|-X|在每个字典的后面添加一个后缀
|-H|添加请求头
|-i|不区分大小写搜索
</tbody></table>
<h4>扫描：</h4>
基本的扫描：
dirb 加上目标URL
<hr/>
搜索特定文件（这里为php）
dirb 目标URL -X .php
<hr/>
输出到文件（这里为1.txt）
dirb 目标URL -o 1.txt
<hr/>
速度延迟（这里是100us）
dirb 目标URL -z 100
<hr/>
HTTP授权扫描
dirb 目标URL -u username:password
……


#### 扫描：

---


---


---


---


## 五、Gobuster

> 
<h3>5.1、简介：</h3>
GO语言编写的
来对目录、文件、DNS和VHost等对象进行暴力破解攻击
dir：传统的目录爆破模式；
dns：DNS子域名爆破模式；
vhost：虚拟主机爆破模式


> 
<h3>5.2、下载：</h3>
[Releases · OJ/gobuster · GitHub<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://github.com/OJ/gobuster/releases](https://github.com/OJ/gobuster/releases)

