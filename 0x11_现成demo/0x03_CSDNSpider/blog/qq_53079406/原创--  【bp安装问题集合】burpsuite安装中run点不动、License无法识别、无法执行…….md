# 原创
：  【bp安装问题集合】burpsuite安装中run点不动、License无法识别、无法执行……

# 【bp安装问题集合】burpsuite安装中run点不动、License无法识别、无法执行……

**目录**

[一、前言： ](#%E2%80%8B%E2%80%8B%E5%89%8D%E8%A8%80%EF%BC%9A%C2%A0)

[二、下载：](#%E2%80%8B%E2%80%8B%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[三、问题一：错误打开文件](#%E2%80%8B%E2%80%8B%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9A%E9%94%99%E8%AF%AF%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6)

[四、问题二：不会运行文件](#%E2%80%8B%E2%80%8B%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9A%E4%B8%8D%E4%BC%9A%E8%BF%90%E8%A1%8C%E6%96%87%E4%BB%B6)

[4.1、解决：](#%E2%80%8B%E8%A7%A3%E5%86%B3%EF%BC%9A)

[ 4.1.1、首先，配置好jdk环境： ](#%E2%80%8B%E9%A6%96%E5%85%88%EF%BC%8C%E9%85%8D%E7%BD%AE%E5%A5%BDjdk%E7%8E%AF%E5%A2%83%EF%BC%9A%C2%A0)

[4.1.2、然后，更改打开文件 ](#%E2%80%8B%E7%84%B6%E5%90%8E%EF%BC%8C%E6%9B%B4%E6%94%B9%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6%C2%A0)

[4.1.3、最后，可以直接双击打开](#%E2%80%8B%E6%9C%80%E5%90%8E%EF%BC%8C%E5%8F%AF%E4%BB%A5%E7%9B%B4%E6%8E%A5%E5%8F%8C%E5%87%BB%E6%89%93%E5%BC%80)

[五、问题三：run点不动](#%E2%80%8B%E2%80%8B%E9%97%AE%E9%A2%98%E4%B8%89%EF%BC%9Arun%E7%82%B9%E4%B8%8D%E5%8A%A8)

[5.1、解决： ](#%E2%80%8B%E8%A7%A3%E5%86%B3%EF%BC%9A%C2%A0)

[5.1.1、首先，先打开burp-loader-keygen.jar](#%E2%80%8B%E9%A6%96%E5%85%88%EF%BC%8C%E5%85%88%E6%89%93%E5%BC%80burp-loader-keygen.jar)

[5.1.2、然后，点击run是可以点的 ](#%E2%80%8B%E7%84%B6%E5%90%8E%EF%BC%8C%E7%82%B9%E5%87%BBrun%E6%98%AF%E5%8F%AF%E4%BB%A5%E7%82%B9%E7%9A%84%C2%A0)

[5.1.3、最后，License的2边搬家](#%E2%80%8B%E6%9C%80%E5%90%8E%EF%BC%8CLicense%E7%9A%842%E8%BE%B9%E6%90%AC%E5%AE%B6)

[六、问题三：License无法识别](#%E2%80%8B%E2%80%8B%E9%97%AE%E9%A2%98%E4%B8%89%EF%BC%9ALicense%E6%97%A0%E6%B3%95%E8%AF%86%E5%88%AB)

[6.1、解决： ](#6.1%E3%80%81%E8%A7%A3%E5%86%B3%EF%BC%9A%C2%A0)

[七、最后再次安装成功](#%E2%80%8B%E2%80%8B%E6%9C%80%E5%90%8E%E5%86%8D%E6%AC%A1%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F)

---


## 一、前言： 

> 
今天第三次安装burpsuite，遇见的问题都分分钟解决了（哈哈哈）
问题不可能没有，问题只会转移
就像爱情一样，不会凭空消失，只会转移
=======》解决一类问题


## 二、下载：

> 
今天不运行汉包了，用了那么久中文版，英文版已经稳了（盲找都知道位置了）
附带burpsuiteV2版本的安装包（有jdk环境、burpsuite、以及汉化包……）
网盘链接：https://pan.baidu.com/s/1LQVrVFU1CJVxhfayktOEeQ?pwd=hj12 <br/> 提取码：hj12


## 三、问题一：错误打开文件

> 
一上来就将.jar文件解压（一般是因为默认为解压软件解压）
最后变成了文件夹
你将永远找不到exe文件（悄悄说一句，我第一次的时候就是这样，然后到处找exe文件）


## 四、问题二：不会运行文件

> 
那就是无法直接打开jar文件了
默认的打开方式是解压软件，会将你一步一步引入深渊
配置好环境后，jar文件都能使用java环境打开


## 4.1、解决：

> 
<h4> 4.1.1、首先，配置好jdk环境： </h4>
[3分钟复制粘贴配置java环境变量，验证配置是否成功，java文件运行方法](https://blog.csdn.net/qq_53079406/article/details/123482726?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164905838816780366543699%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164905838816780366543699&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123482726.nonecase&amp;utm_term=java&amp;spm=1018.2226.3001.4450)

<h4>4.1.2、然后，更改打开文件 </h4>
要是没有就在电脑里面找，更改以后，文件的图标就变成了java环境的图标了


<h4>4.1.3、最后，可以直接双击打开</h4>
要是想秀一下，可以打开命令提示符
然后输入java -jar (再把文件拖进去，路径就进入了)
同样可以启动


#### 4.1.2、然后，更改打开文件 

## 五、问题三：run点不动

> 
 无论你怎么点击run，都没有反应，就是run不了（就问你气不气）



## 5.1、解决： 

> 
当你把一次把burp-loader-keygen.jar和burpsuite_pro_v2.0.11.jar都直接打开后，你是run不动

<h4>5.1.1、首先，先打开burp-loader-keygen.jar</h4>



<h4>5.1.2、然后，点击run是可以点的 </h4>
大家看一下上面标注出来的那一段代码
不就是相当于是用java启动嘛（java -jar  xxxx.jar）
你如果自己都提前启动了，那还再怎么run
前提检查java环境是否配置好

<h4>5.1.3、最后，License的2边搬家</h4>
就没了，ok了


#### 5.1.2、然后，点击run是可以点的 

## 六、问题三：License无法识别

> 
 License复制粘贴到burpsuite后显示无法识别
在标记地方会出现无法识别，这个是因为启动方法不对



### 6.1、解决： 

> 
这个就是上面那个问题延伸出来的问题，不是它run出来的
是你自己启动的，那license必定不对，你说是把
正确流程是先运行burp-loader-keygen.jar-----run出burpsuite_pro_v2.0.11.jar启动程序


## 七、最后再次安装成功

> 
** **<img alt="" height="521" src="https://img-blog.csdnimg.cn/3c010940c6e74ab0924b2711fff89292.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_12,color_FFFFFF,t_70,g_se,x_16" width="514"/>
 nset------start就进去了

 <img alt="" height="985" src="https://img-blog.csdnimg.cn/ffa2f91124874cd6a789051531ff464c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

