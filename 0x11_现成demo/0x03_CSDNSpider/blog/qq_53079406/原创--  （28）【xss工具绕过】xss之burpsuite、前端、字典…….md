# 原创
：  （28）【xss工具绕过】xss之burpsuite、前端、字典……

# （28）【xss工具绕过】xss之burpsuite、前端、字典……

**目录**

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[burpsuite抓包](#burpsuite%E6%8A%93%E5%8C%85) 

[ ](#%C2%A0%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%AF%B9%E6%95%B0%E6%8D%AE%E8%BF%9B%E8%A1%8C%E6%A8%A1%E7%B3%8A%E6%B5%8B%E8%AF%95)<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[方法一：对数据进行模糊测试](#%C2%A0%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%AF%B9%E6%95%B0%E6%8D%AE%E8%BF%9B%E8%A1%8C%E6%A8%A1%E7%B3%8A%E6%B5%8B%E8%AF%95)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[方法二：安装插件，进行xss漏洞检测](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%AE%89%E8%A3%85%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%BF%9B%E8%A1%8Cxss%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[XSS Validator](#XSS%20Validator)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[前端绕过](#%E5%89%8D%E7%AB%AF%E7%BB%95%E8%BF%87)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[X-frame被忽略情况](#X-frame%E8%A2%AB%E5%BF%BD%E7%95%A5%E6%83%85%E5%86%B5)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[取值：](#%E5%8F%96%E5%80%BC%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[使用DOM型XSS绕过](#%E4%BD%BF%E7%94%A8DOM%E5%9E%8BXSS%E7%BB%95%E8%BF%87)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[提交方式](#%E6%8F%90%E4%BA%A4%E6%96%B9%E5%BC%8F)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[Get提交](#Get%E6%8F%90%E4%BA%A4)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[Post提交](#Post%E6%8F%90%E4%BA%A4)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[HttpOnly属性](#HttpOnly%E5%B1%9E%E6%80%A7)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[XSS-Fuzzer](#XSS-Fuzzer)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>[XSStrike](#XSStrike)

[ ](#%C2%A0%E4%BB%8B%E7%BB%8D%EF%BC%9A)<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[介绍：](#%C2%A0%E4%BB%8B%E7%BB%8D%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[作用：](#%E4%BD%9C%E7%94%A8%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[特点](#%E7%89%B9%E7%82%B9)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[下载地址：](#%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[环境：](#%E7%8E%AF%E5%A2%83%EF%BC%9A)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第一步：给python3安装pip](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%BB%99python3%E5%AE%89%E8%A3%85pip)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第二步：下载GitHub上的XSStrike文件](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E4%B8%8B%E8%BD%BDGitHub%E4%B8%8A%E7%9A%84XSStrike%E6%96%87%E4%BB%B6)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第三步：进入到目录下](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%BF%9B%E5%85%A5%E5%88%B0%E7%9B%AE%E5%BD%95%E4%B8%8B)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第四步：安装依赖模块](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96%E6%A8%A1%E5%9D%97)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第五步：运行工具](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E8%BF%90%E8%A1%8C%E5%B7%A5%E5%85%B7)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>[第六步：使用方法](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[在线生成Fuzzing字典](#%E5%9C%A8%E7%BA%BF%E7%94%9F%E6%88%90Fuzzing%E5%AD%97%E5%85%B8)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[GitHub上的Fuzzing字典](#GitHub%E4%B8%8A%E7%9A%84Fuzzing%E5%AD%97%E5%85%B8)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[ ImXSS测试平台（Java ）](#%C2%A0ImXSS%E6%B5%8B%E8%AF%95%E5%B9%B3%E5%8F%B0%EF%BC%88Java%20%EF%BC%89)

<img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>[Xwaf](#Xwaf)

---


<img alt="" src="https://img-blog.csdnimg.cn/bb66647ae4534912918ec17418395640.png"/> 

##  推荐：

[【xss绕过集合】一般测试步骤、触发事件、干扰、编码……](https://blog.csdn.net/qq_53079406/article/details/123901260?spm=1001.2014.3001.5501)

## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>burpsuite抓包

> 
<h3><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/> 方法一：对数据进行模糊测试</h3>
<blockquote>
拦截请求------发送到攻击-------配置有效载荷的位置------选择攻击类型-----有效载荷设置
有效载荷设置的时候，添加各种测试字符串（可以提前在网上下一点字典）
通过对错误消息和其他异常的响应来检测许多基于输入的漏洞


### <img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>方法二：安装插件，进行xss漏洞检测

> 
<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>XSS Validator </h4>
（上面没有说需要什么环境，就是可以直接安装）


右下角显示无法验证
还是要得到GitHub下载源码然后手动去安装

 选择下载好后编译好的jar文件，尝试手动安装

 <img alt="" height="328" src="https://img-blog.csdnimg.cn/3b1a266cd7e240b29ca5175265a52458.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_14,color_FFFFFF,t_70,g_se,x_16" width="587"/>

看我解决它：
我在真实加里面也安装一个burpsuite（这次不使用汉化包）
我怀疑是汉化包导致的验证出错了

安装成功了，推理得到验证，漂亮 
 
安装的扩展也出来了





 

## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>前端绕过

> 
<h3><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>X-frame被忽略情况</h3>
<blockquote>
<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>原理：</h4>
HTTP响应报头中X-Frame-Options指示是否被允许在一个以呈现页面&lt;frame&gt;，&lt;iframe&gt;或&lt;object&gt;。
通过确保其内容未嵌入其他网站，可以使用此功能避免点击劫持攻击、或使用iframe引用的xss漏洞

<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>取值：</h4>
DENY        从其他站点加载时，在框架中加载页面失败，从同一站点加载也将失败，无论站点尝试这样做，页面都不能显示在框架中
SAMEORIGIN        只要包含在框架中的站点与为页面提供服务的站点相同，仍然可以在框架中使用该页面，该页面只能显示在与页面本身相同的源框架中
ALLOW-FROM https://example.com/        页面只能显示在指定原点的框架中


<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>利用：</h4>
（利用URL名字进行欺骗，有一点社工意思）用iframe加载一个页面，我们可以控制窗口的名称，这里也可以执行javascript代码

<br/> &lt;iframe
src='http://www.xxx.com?foo="xss  
οnfοcus=location=window.name//'
name="javascript:alert("XSS")"&gt;&lt;
/iframe&gt;

window.name：是当前Window页面的名称，让别人以为是真滴
foo：无什么实际意义，随便命名的
onFocus事件：当光标落在文本框中时发生


#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>取值：

### <img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>使用DOM型XSS绕过

> 
因为这个DOM型XSS是在客户端被执行的，所以就是说传不到服务器那，也就没有服务器过滤这一说了，但是一般客户端也会有过滤的，这时候就要再考虑适不适用了。


## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>提交方式

> 
<h3><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>Get提交</h3>
get型xss通过URL构造payload发给对方打开即可

<h3><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>Post提交</h3>
post型xss无法由对方直接打开提交，需要本地或云上搭一个web环境，并放上一个html文件，里面写上站点的漏洞点和payload，并将完整的html文件url地址发给对方打开，满足这些条件才能触发


### <img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>Post提交

## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>HttpOnly属性

> 
<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>原理：</h4>
为了预防大多数针对会话cookie的盗窃XSS攻击，通过后端服务器对cookie中设置了包含在http返回头Set-Cookie里的一个附加的属性，设置后通过js脚本无法读取cookie（也就是cookie在客户端上不可访问了）

<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>过程：</h4>
客户端脚本代码尝试读取该cookie时，若浏览器（支持HttpOnly）检测到包含HttpOnly标志的cookie，将返回一个空字符串。
查找数据包HTTP响应标头中是否包含HttpOnly标志（不一定会显示出来）
设置以后，就放弃通过js来执行相关操作吧


#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>过程：

<img alt="" src="https://img-blog.csdnimg.cn/cbbbefa04a8d4cf58468b422da4dace9.png"/> 

## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>XSS-Fuzzer

### <img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/9cdf9ad4741c4c908d4d883622bfdcbf.png" width="28"/>XSStrike 

> 
<h4> <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>介绍：</h4>
XSStrike是一款检测Cross Site Scripting的高级检测工具。它集成了payload生成器、爬虫和模糊引擎功能。XSStrike不是像其他工具那样注入有效负载并检查其工作，而是通过多个解析器分析响应，然后通过与模糊引擎集成的上下文分析来保证有效负载。除此之外，XSStrike还具有爬行，模糊测试，参数发现，WAF检测功能。它还会扫描DOM XSS漏洞。

<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>作用：</h4>
找到新的XSS向量，适用于任何浏览器
在GET和POST参数上测试XSS有效载荷
在浏览器中绕过XSS审核员
绕过Web应用程序防火墙
利用HTML白名单特征


<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>特点</h4>
反射和DOM XSS扫描 多线程爬行 上下文分析 可配置的核心 WAF检测与逃避 过时的JS Lib扫描 智能有效载荷发生器 手工制作HTML和JavaScript解析器 强大的模糊发动机 盲目XSS支持 高度研究的工作流程 完整的HTTP支持 从文件中有效载荷 由Photon，Zetanize和Arjun提供动力 有效载荷编码

<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>下载地址：</h4>
[s0md3v/XSStrike: Most advanced XSS scanner. (github.com)](https://github.com/s0md3v/XSStrike)

<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>环境：</h4>
windows、linux系统都可以运行
XSStrike只可以运行在python 3.6 以上版本
我kali上有多个python，然后输入python后显示不了版本，然后输入（对应版本）python3 


<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第一步：给python3安装pip</h4>
（在kali命令符里面输入，别进入到python里输入了，会报错）
sudo apt-get install python3-pip
（我是以前安装过）


<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第二步：下载GitHub上的XSStrike文件</h4>
git clone https://github.com/s0md3v/XSStrike.git



<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第三步：进入到目录下</h4>
cd ./XSStrike  （根据自己安装的位置进入吧）



<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第四步：安装依赖模块</h4>
pip3 install -r requirements.txt

 下面的提示意识，不是报错。
警告：运行pip作为“root”用户可能导致系统包管理器与禁止的权限和冲突行为导致。建议使用虚拟环境：https://pip.pypa.io/warnings/venv


<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第五步：运行工具</h4>
python3 xsstrike.py -u "http://target"



<h4><img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第六步：使用方法</h4>
结合相关功能进行使用
python3 xsstrike.py -u "URL"  （后面接功能模块）


-h, --help //显示帮助信息
-u, --url //指定目标URL
--data //POST方式提交内容
-v, --verbose //详细输出
-f, --file //加载自定义paload字典
-t, --threads //定义线程数
-l, --level //爬行深度
-t, --encode //定义payload编码方式
--json //将POST数据视为JSON
--path //测试URL路径组件
--seeds //从文件中测试、抓取URL
--fuzzer //测试过滤器和Web应用程序防火墙。
--update //更新 --timeout //设置超时时间
--params //指定参数 --crawl //爬行
--proxy //使用代理 --blind //盲测试
--skip //跳过确认提示
--skip-dom //跳过DOM扫描
--headers //提供HTTP标头
-d, --delay //设置延迟


#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>作用：

#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>下载地址：

#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第一步：给python3安装pip

#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第三步：进入到目录下

#### <img alt="" height="28" src="https://img-blog.csdnimg.cn/720e1019e17e435484749f16f3be3e4c.png" width="28"/>第五步：运行工具

<img alt="" src="https://img-blog.csdnimg.cn/d4a89a075652414d81f2e1ab62f9e523.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_8,color_FFFFFF,t_70,g_se,x_16"/> 

## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>在线生成Fuzzing字典

> 
链接：[XSS Fuzzer](https://xssfuzzer.com/fuzzer.html)



## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>GitHub上的Fuzzing字典

> 
 (这个的作者还在不定期更新)
GitHub地址：[TheKingOfDuck/fuzzDicts: Web Pentesting Fuzz 字典,一个就够了。 (github.com)](https://github.com/TheKingOfDuck/fuzzDicts)

内容包括：参数Fuzz字典 Xss Fuzz字典 用户名字典 密码字典 目录字典 sql-fuzz字典 ssrf-fuzz字典 XXE字典 ctf字典 Api字典 路由器后台字典 文件后缀Fuzz js文件字典 子域名字典


## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/> ImXSS测试平台（Java ）

> 
 ImXSS是国内首套Java研发的Xss跨站脚本测试平台，用户在浏览网站、使用即时通讯软件、甚至在阅读电子邮件时，通常会点击其中的链接。攻击者通过在链接中插入恶意代码，就能够盗取用户信息

链接地址：[imxss: 国内首款Java研发并上线的Xss漏洞测试平台。为XssAPP升级版。性能提升数倍，兼容移动端。 (gitee.com)](https://gitee.com/yhtmxl/imxss/#https://gitee.com/link?target=https%3A%2F%2Fwww.oschina.net%2Fp%2Fsimple-debug)


## <img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/><img alt="" height="28" src="https://img-blog.csdnimg.cn/1b83538a859146458237030eebec8cd4.png" width="28"/>Xwaf

> 
 GitHub链接：[3xp10it/xwaf: Automatic bypass (brute force) waf (github.com)](https://github.com/3xp10it/xwaf)
一个python写的waf自动绕过工具，可无人干预,自动暴破waf


<img alt="" src="https://img-blog.csdnimg.cn/dedd0ebd92984628ae34b4b48b9a44e8.png"/> 
