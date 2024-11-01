# 原创
：  【文件缺失/被隐藏】三种递进式方法寻找文件（有点新奇）、丢失文件填补方法（etc/host文件‘丢失’为例）

# 【文件缺失/被隐藏】三种递进式方法寻找文件（有点新奇）、丢失文件填补方法（etc/host文件‘丢失’为例）

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、、确认缺失：](#%E4%BA%8C%E3%80%81%E3%80%81%E7%A1%AE%E8%AE%A4%E7%BC%BA%E5%A4%B1%EF%BC%9A)

[ 2.1、方法一：](#%C2%A02.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[2.1.1、第一步：确认目前无文件](#2.1.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%A1%AE%E8%AE%A4%E7%9B%AE%E5%89%8D%E6%97%A0%E6%96%87%E4%BB%B6)

[2.1.2、第二步：修改文件隐藏设置](#2.1.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E4%BF%AE%E6%94%B9%E6%96%87%E4%BB%B6%E9%9A%90%E8%97%8F%E8%AE%BE%E7%BD%AE)

[2.1.3、第三步：查看结果](#2.1.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5%E7%9C%8B%E7%BB%93%E6%9E%9C)

[ 2.2、方法二：](#%C2%A02.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[2.2.1、第一步：确认目前无文件](#2.2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%A1%AE%E8%AE%A4%E7%9B%AE%E5%89%8D%E6%97%A0%E6%96%87%E4%BB%B6)

[2.2.2、第二步：解压文件（虚晃一枪）](#2.2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%A7%A3%E5%8E%8B%E6%96%87%E4%BB%B6%EF%BC%88%E8%99%9A%E6%99%83%E4%B8%80%E6%9E%AA%EF%BC%89)

[ 2.3、方法三：](#%C2%A02.3%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A)

[2.3.1、第一步：快速搜索](#2.3.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%BF%AB%E9%80%9F%E6%90%9C%E7%B4%A2)

[2.3.2、第二步：直接打开](#2.3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80)

[三、填补丢失文件](#%E4%B8%89%E3%80%81%E5%A1%AB%E8%A1%A5%E4%B8%A2%E5%A4%B1%E6%96%87%E4%BB%B6)

[第一步：在网上下到对应的丢失文件](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%9C%A8%E7%BD%91%E4%B8%8A%E4%B8%8B%E5%88%B0%E5%AF%B9%E5%BA%94%E7%9A%84%E4%B8%A2%E5%A4%B1%E6%96%87%E4%BB%B6)

[第二步：放到对应的位置](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%94%BE%E5%88%B0%E5%AF%B9%E5%BA%94%E7%9A%84%E4%BD%8D%E7%BD%AE)

[四、推荐](#%E5%9B%9B%E3%80%81%E6%8E%A8%E8%8D%90)

[ 4.1、修改host文件权限](#%C2%A04.1%E3%80%81%E4%BF%AE%E6%94%B9host%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90)

---


 （好，你个老六）

---


## 一、简介：

> 
文件不一样，但是方法基本一样
下面的方法是递进式解决的问题的思路（个人见解）
我以C:\Windows\System32\drivers下的etc配置文件为例


---


## 二、、确认缺失：

> 
<h3> 2.1、方法一：</h3>
<h4>2.1.1、第一步：确认目前无文件</h4>
看到C:\Windows\System32\drivers下没有etc配置文件

<hr/>
<h4>2.1.2、第二步：修改文件隐藏设置</h4>
因为系统的版本可能不同
只要找到文件夹选项------&gt;显示隐藏的文件和文件夹-----&gt;应用

<hr/>

<h4>2.1.3、第三步：查看结果</h4>
再返回文件夹中观看是否有了隐藏的文件
还是看不见




#### 2.1.2、第二步：修改文件隐藏设置

---


> 
<h3> 2.2、方法二：</h3>
（这个方法很奇妙）
<h4>2.2.1、第一步：确认目前无文件</h4>
看到C:\Windows\System32\drivers下没有etc配置文件



<h4>2.2.2、第二步：解压文件（虚晃一枪）</h4>
咱们随便找一个压缩文件，然后执行解压
（不是真的解压到某个软件中，而是在对应文件夹中，找有没有对应的被隐藏的文件夹）

奇妙吧
说明这个文件时存在的 


#### 2.2.2、第二步：解压文件（虚晃一枪）

> 
<h3> 2.3、方法三：</h3>
（这个主要就是如何打开这个看不见的文件夹了）

<h4>2.3.1、第一步：快速搜索</h4>
直接在快速搜索栏搜（我用的“我的电脑pro”，秒搜文件）


<h4>2.3.2、第二步：直接打开</h4>
然后找到对应文件以后，可以直接打开这个文件夹
（前提，这个文件存在）


#### 2.3.2、第二步：直接打开

---


## 三、填补丢失文件

> 
<h4>第一步：在网上下到对应的丢失文件</h4>
<h4>第二步：放到对应的位置</h4>


#### 第二步：放到对应的位置

---


## 四、推荐

> 
<h3> 4.1、修改host文件权限</h3>
[【权限不够】修改hosts等系统文件后后，无法保存，只能另存，解？提权罢了。（C:\Windows\System32\drivers\etc）<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://blog.csdn.net/qq_53079406/article/details/123547286?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165202569716782248589980%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165202569716782248589980&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123547286-null-null.nonecase&amp;utm_term=host&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123547286?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165202569716782248589980%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165202569716782248589980&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123547286-null-null.nonecase&amp;utm_term=host&amp;spm=1018.2226.3001.4450)


