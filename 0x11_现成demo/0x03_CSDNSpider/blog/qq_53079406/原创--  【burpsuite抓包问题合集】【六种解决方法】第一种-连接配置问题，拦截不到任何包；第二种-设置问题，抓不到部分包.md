# 原创
：  【burpsuite抓包问题合集】【六种解决方法】第一种：连接配置问题，拦截不到任何包；第二种：设置问题，抓不到部分包

# 【burpsuite抓包问题合集】【六种解决方法】第一种：连接配置问题，拦截不到任何包；第二种：设置问题，抓不到部分包

**目录**

[一、前言：](#%E5%89%8D%E8%A8%80%EF%BC%9A)

[二、安装插件（便于操作）](#%E4%B8%80%E3%80%81%E5%AE%89%E8%A3%85%E6%8F%92%E4%BB%B6%EF%BC%88%E4%BE%BF%E4%BA%8E%E6%93%8D%E4%BD%9C%EF%BC%89)

[三、问题一：纯属抓不到任何包](#%E4%BA%8C%E3%80%81%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9A%E7%BA%AF%E5%B1%9E%E6%8A%93%E4%B8%8D%E5%88%B0%E4%BB%BB%E4%BD%95%E5%8C%85)

[3.1问题解决：](#2.1%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[3.1.1、解决一：](#2.1.1%E3%80%81%E8%A7%A3%E5%86%B3%E4%B8%80%EF%BC%9A)

[3.1.2、解决二：](#2.1.2%E3%80%81%E8%A7%A3%E5%86%B3%E4%BA%8C%EF%BC%9A)

[ 3.1.3、解决三：](#%C2%A02.1.3%E3%80%81%E8%A7%A3%E5%86%B3%E4%B8%89%EF%BC%9A)

[ 3.1.4、解决四：](#%C2%A02.1.4%E3%80%81%E8%A7%A3%E5%86%B3%E5%9B%9B%EF%BC%9A)

[ 3.1.5、解决五：](#%C2%A02.1.5%E3%80%81%E8%A7%A3%E5%86%B3%E4%BA%94%EF%BC%9A)

[四、问题二：burpsuite抓不到本地靶场数据包（可以抓到浏览器访问网站的包）](#%E4%BA%8C%E3%80%81%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9Aburpsuite%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E9%9D%B6%E5%9C%BA%E6%95%B0%E6%8D%AE%E5%8C%85%EF%BC%88%E5%8F%AF%E4%BB%A5%E6%8A%93%E5%88%B0%E6%B5%8F%E8%A7%88%E5%99%A8%E8%AE%BF%E9%97%AE%E7%BD%91%E7%AB%99%E7%9A%84%E5%8C%85%EF%BC%89)

[4.1、问题解决](#2.1%E3%80%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3)

[ 4.1.1解决一：](#%C2%A02.1.1%E8%A7%A3%E5%86%B3%E4%B8%80%EF%BC%9A)

[五、推荐](#%E6%8E%A8%E8%8D%90%EF%BC%9A)

---


（不断的摸索，所有问题都能解决）

## 一、前言：

> 
我已经把burpsuite玩的明明白白了，我把抓不到包分为2种情况
第一种：连接配置问题，抓不到任何包
第二种：设置问题，抓不到部分包


## 二、安装插件（便于操作）

> 
 为了更好的分析代理的连接状态
在浏览器插件上安装一个Proxy代理相关的插件
避雷：我安装了一个Firefox推荐的FoxyProxy Standard，感觉不是特别便捷

再安装了几个，找到了一个挺友好的，Proxy SwitchyOmega


设置好了以后可以直接在标签栏上进行快速的变换
没必要每次再到设置里面去了

 界面挺中国的，代理设置的时候，最下面的不代理地址删掉
一般本地代理都是127.0.0.1，或者·localhost等
（如果没删，顾名思义就不代理了，哈哈哈）



## 三、问题一：纯属抓不到任何包

> 
这个就是连接与配置问题，很好解决


### 3.1问题解决：

> 
<h4>3.1.1、解决一：</h4>
首先就是上面分析的问题
是否设置的地址在不代理的地址列表里面


> 
<h4>3.1.2、解决二：</h4>
是否是因为端口占用
把代理服务器的设置端口改一下，再把burpsuite的代理监听端口也改一下

 <img alt="" height="311" src="https://img-blog.csdnimg.cn/e58fc7d7c0284868a5c0a5fc8caf216e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="707"/>


> 
<h4> 3.1.3、解决三：</h4>
可能因为你使用的浏览器有某些特殊的设置
 如果不想长时间挣扎，首推换一个浏览器做代理（亲测可以拦截）



> 
<h4> 3.1.4、解决四：</h4>
在被代理的浏览器地址栏中输入代理地址和端口
如果显示出burpsuite，其实就没问题了





> 
<h4> 3.1.5、解决五：</h4>
证书未导入到浏览器，或者证书无效
[【bp问题合集】burpsuite监听端口勾选不了、代理出现安全警告：“有软件正在阻止 Firefox 安全地连接至此网站](https://blog.csdn.net/qq_53079406/article/details/123228293?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164951573516780357254232%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164951573516780357254232&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-123228293.nonecase&amp;utm_term=burpsuite&amp;spm=1018.2226.3001.4450)

这里说一下，如果是证书无效，将burpsuite打开，重新从burpsuite中导出证书
命名时，后缀为.der，如果没命名后缀，那到导出的文件夹改后缀


浏览器中搜证书-----证书颁发机构-----导入----导入第二次导出的证书导浏览器中

 <img alt="" height="803" src="https://img-blog.csdnimg.cn/9389cbe6d3cd410e894953f32eda8731.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


---


## 四、问题二：burpsuite抓不到本地靶场数据包（可以抓到浏览器访问网站的包）

### 4.1、问题解决

> 
<h4> 4.1.1解决一：</h4>
可以是筛选器放过了某些包
把它都给勾上


 快看我抓住了，哈哈哈<img alt="" height="812" src="https://img-blog.csdnimg.cn/19ccdcc811e240b1812acb69900a21bb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


just so so！呕吼

## 五、推荐：

> 
[Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…](https://blog.csdn.net/qq_53079406/article/details/123590641?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164951816016782094817391%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=164951816016782094817391&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-123590641.nonecase&amp;utm_term=burpsuite&amp;spm=1018.2226.3001.4450)

