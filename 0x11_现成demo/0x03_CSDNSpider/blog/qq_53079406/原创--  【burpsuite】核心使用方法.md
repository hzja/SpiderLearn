# 原创
：  【burpsuite】核心使用方法

# 【burpsuite】核心使用方法

**目录**

[一、Burp Suite](#%E4%B8%80%E3%80%81Burp%20Suite)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、Proxy模块设置代理](#%E4%BA%8C%E3%80%81Proxy%E6%A8%A1%E5%9D%97%E8%AE%BE%E7%BD%AE%E4%BB%A3%E7%90%86)

[三、Repeater重放模块](#%E4%B8%89%E3%80%81Repeater%E9%87%8D%E6%94%BE%E6%A8%A1%E5%9D%97)

[四、Intruder暴力破解模块](#%E5%9B%9B%E3%80%81Intruder%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3%E6%A8%A1%E5%9D%97)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[设置攻击目标：](#%E8%AE%BE%E7%BD%AE%E6%94%BB%E5%87%BB%E7%9B%AE%E6%A0%87%EF%BC%9A)

[设置方法与攻击位置：](#%E8%AE%BE%E7%BD%AE%E6%96%B9%E6%B3%95%E4%B8%8E%E6%94%BB%E5%87%BB%E4%BD%8D%E7%BD%AE%EF%BC%9A)

[（1）Sniper型](#%EF%BC%881%EF%BC%89Sniper%E5%9E%8B)

[（2）Battering ram型](#%EF%BC%882%EF%BC%89Battering%20ram%E5%9E%8B)

[（3）Pitchfork型](#%EF%BC%883%EF%BC%89Pitchfork%E5%9E%8B)

[（4）Cluster bomb型](#%EF%BC%884%EF%BC%89Cluster%20bomb%E5%9E%8B)

[Payload标签页](#Payload%E6%A0%87%E7%AD%BE%E9%A1%B5)

[Options标签页](#Options%E6%A0%87%E7%AD%BE%E9%A1%B5)

[五、Decoder解码模块](#%E4%BA%94%E3%80%81Decoder%E8%A7%A3%E7%A0%81%E6%A8%A1%E5%9D%97)

[六、Comparer比较模块](#%E5%85%AD%E3%80%81Comparer%E6%AF%94%E8%BE%83%E6%A8%A1%E5%9D%97)

[七、工程选项](#%E4%B8%83%E3%80%81%E5%B7%A5%E7%A8%8B%E9%80%89%E9%A1%B9)

---


> 
<h2>一、Burp Suite </h2>
<h3>简介：</h3>

Burp Suite（简称Burp）是一款Web安全领域的跨平台工具，基于 Java开发。它集成了很多用于发现常见Web漏洞的模块，如Proxy、 Spider、Scanner、Intruder、Repeater等。所有的模块共享一个能处理并显示HTTP消息的扩展框架，模块之间无缝交换信息，可以大大提高效率。



---


---


> 
<h2>二、Proxy模块设置代理</h2>

代理模块是Burp的核心模块，自然也会是我们使用最多的一个模块。它主要用来截获并修改浏览器、手机App等客户端的HTTP/HTTPS数据包。 



<hr/>
要想使用Burp，必须先设置代理端口。


Proxy→Options→Proxy Listeners→Add增加代理


<img alt="" height="266" src="https://img-blog.csdnimg.cn/d035067e80d045a6b6798672f136991c.png" width="697"/>




在Bind to port一栏内填写侦听的端口，这里以8080端口为例。


如果要在本机使用，可以将Bind to address设置为Loopback only；


如果要让局域网内的设备使用代理，则应该选择All interfaces。


<hr/>
点击OK按钮后勾选Running



<img alt="" height="243" src="https://img-blog.csdnimg.cn/1adb43ee66e045cbaee327411e6a4f33.png" width="686"/>



<hr/>




以火狐浏览器为例


（或直接在设置里搜索代理）


在浏览器上依次选择Internet选项→连接→局域网设置，然后在“代理服务器”一栏中填写前文配置的Burp代理IP地址和端口



设置完成后就可以通过Burp代理来抓取火狐浏览器的数据包了，如果使用的是Chrome等其他浏览器，则可在相应浏览器的配置项或插件中进行设置。

<hr/>
在扩展中，下载浏览器的代理插件

<hr/>


接下来，在Proxy→Intercept选项卡下设置Intercept is on，这 样就能截获浏览器的数据包并进行修改等操作了。如果设置Intercept is off，则不会将数据包拦截下来，而是会在HTTP history中记录该 请求



在数据包内容展示界面上单击右键，可以将这个数据包发送给Intruder、Repeater、Comparer、Decoder等模块





---


---


---


---


> 
<h2>三、Repeater重放模块 </h2>

在需要手工测试HTTP Header中的Cookie或User-Agent等浏览器不可修改的字段是否存在注入点，以及需要发现复杂的POST数据包中是否存在SSRF时，一般需要用到Repeater模块。 


<hr/>



在Proxy中单击右键并选择Send to Repeater（或者Ctrl+r）就可以将截获的数据包发向Repeater模块，这个模块应属于实践中最常用的模块。在这个模块中，左边为将要发送的原始HTTP请求，右边为服务器返回的数据。在界面左侧可以方便地修改将要发送的数据包，用于手工测试Payload等操作，修改完成后点击Go按钮，即可在右侧收到服务器的响应。这里以笔者的一台虚拟机为例进行说明


<hr/>

左侧的Headers



Headers标签页既可以方便地添加HTTP头信息，又可以避免在手动修改HTTP头时因缺少空格等原因产生问题。例如，我们有时候会在CTF中遇到检查IP地址的题目，此时就可以添加X-Forwarded-For、XReal-IP等HTTP头尝试绕过。在添加之后，可以在Raw标签页中发现这个新增加的HTTP头信息。 


<hr/>
左侧的Hex标签页


Hex标签页更多用于修改HTTP数据包的十六进制编码。比如，可以将其用在文件上传类型的CTF题目中以截断后缀，或者是使用这些编码来对WAF进行模糊测试，并让我们可以顺利上传Webshell



---


---


---


> 
<h2>四、Intruder暴力破解模块 </h2>
<h3>简介：</h3>

暴力破解（以下简称“爆破”）是一种低成本但可能带来高回报的攻击方式。


大家应该了解过近些年出现的各种撞库漏洞。当然，在撞库的时候需要考虑性能和效率以进行多线程并发。这时候可以用Python或其他语言编写脚本进行撞库。


Burp中也提供了简单易用的Intruder模块来进行爆破。

<hr/>

Intruder模块包含Sniper、Battering ram、Pitchfork、Clusterbomb等四种攻击类型，可以方便地进行Fuzz等测试。


在Proxy等模块中，在想要测试的数据包上点击右键并选择Send to Intruder（或者Ctrl+l）即可将数据包发向Intruder模块。


Intruder模块中包含了Target、Position、Payload、Options这四个标签页，可分别用于设置不同的功能

<hr/>
<h3>设置攻击目标：</h3>

在Target标签页中可以设置攻击目标的地址（Host）和目标端口（Port），并且可以选择是否使用HTTPS


<hr/>
<h3>设置方法与攻击位置：</h3>

在Position标签页中可以设置攻击的位置和攻击的方法。攻击位置可以自动选择（一般自动选择的变量通常会比较多，不推荐自动选择）。手动选择的方法是：如果你的Burp已经进行了自动选择，那么先点击Clear§按钮，然后选择你要爆破的变量，再点击Add§按钮即可



<hr/>
<h3>（1）Sniper型 </h3>

只需要设置一个Payload set，在两个变量的位置逐一替换Payload，每次只替换一个位置，先替换前面再替换后面。如果你的Payload set中有两个Payload，那么在爆破时会发送四次请求



Sniper型攻击请求过程
<hr/>
<h3>（2）Battering ram型 </h3>

只需要设置一个Payload set，在两个变量的位置同时替换相同的Payload。如果你的Payload set中有两个Payload，在爆破时会发送两次请求


<img alt="" height="187" src="https://img-blog.csdnimg.cn/9c3845e7208343e98d7f9ef16d56e210.png" width="697"/>

Battering ram型攻击请求过程

<hr/>
<h3>（3）Pitchfork型 </h3>

需要设置两个Payload set，这时候两个变量的位置和两个Payload set是一一对应的关系。这个类型可以用来进行撞库攻击等，用你已知的账号密码去测试其他网站。爆破时会发送两个请求


<img alt="" height="98" src="https://img-blog.csdnimg.cn/56d148725eb543e5a973ee6aa6dff6cd.png" width="590"/>

Pitchfork型攻击请求过程 


<hr/>


<h3>（4）Cluster bomb型 </h3>

需要设置两个Payload set，这时候每个位置的Payload将在Payload set中进行排列组合。在爆破时共要发送2×2=4个请求
<img alt="" height="147" src="https://img-blog.csdnimg.cn/9468f02319fd4cc3bd95bf3e9126cb0f.png" width="588"/>

Cluster bomb型攻击请求过程

<hr/>
<h3>Payload标签页</h3>
Payload set可用于设置每个位置使用的Payload集合。Payload type可用于设置这个Payload集合的内容。
Payload type中常用的选项具体包含如下几种：

·Runtime file：用于从文件中加载Payload。 


·Numbers：用于设置数字的开始和结束以及步长。 


·Dates：用于设置日期及日期格式。 


·Character blocks：用于设置长度爆破，Fuzz超长的Post变量，有时候可以绕过WAF等

<hr/>
<h3>Options标签页</h3>

在Options标签页中通常需要对Request Engine中的参数进行设置。


第一个参数为线程数量，默认值为1；


第二个参数为网络连接失败时的重传次数，默认为三次；


第三个参数为每次重传前的暂停时间；


第四个参数为调节数据包发送速度的选项；


第五个参数为开始时间。



---


### 设置攻击目标：

---


### （1）Sniper型 

---


### （3）Pitchfork型 

---


### Payload标签页

---


---


> 
<h2>五、Decoder解码模块 </h2>

Decoder模块为我们提供了丰富的编码与解码工具，可以方便地对HTTP/HTTPS中需要的数据进行编码和解码，并且支持用文本格式或十六进制模式进行查看





在这里，将需要处理的数据输入文本框中，然后选择编码或者解码的模式。除了编码和解码以外，Decoder模块还提供了如MD5、SHA等常见的哈希算法，十分方便。不过，在一般情况下不推荐使用Smart decode进行解码，因为在CTF中智能解码一般都不准确。





---


---


> 
<h2>六、Comparer比较模块 </h2>

在某些诸如Bool盲注的正确和错误的回显题目中，有时候两次数据包之间的差别很小，比较难发现，这时可以使用比较模块来进行比较，以发现差异





---


---


> 
<h2>七、工程选项</h2>

在工程选项中，这里只介绍一些比较常用的名称解析相关的模块


自定义名称解析 

这里可以将域名（也可以是不存在的域名）与IP进行绑定，有时候会遇到一些有这方面需求的题目，而且后文中出现的example.com也都是在这里绑定的




