# 原创
：  xss-labs靶场的搭建和通关（1-18）

# xss-labs靶场的搭建和通关（1-18）

xss-labs是一个专门练习xss的靶场

### 搭建

下载链接：[GitHub-xss-labs](https://gitcode.net/mirrors/do0dl3/xss-labs?utm_source=csdn_github_accelerator)<br/> (1)下载后直接解压到phpstudy的www目录下，名字改为xss-labs。<br/> (2)打开浏览器，直接进入http://127.0.0.1/xss-labs/，即可访问靶场。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/923a8cbdc73943cfa11a313bba43f026.png"/>

### level-1

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/564d7629f3bb43dc8d9f4a0027510ccf.png"/><br/> 可以看到参数传入name，所以直接在name后参数写上js代码。完美通关。

```
&lt;script&gt;alert("xss")&lt;/script&gt;

```

### level-2

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a9e93ffa593549ddb8c0f4e2ce54c716.png"/><br/> 多了一个搜索框，输入上一关的js代码试试看，发现没有什么卵用。应该是代码经过了过滤。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c1a958cb467b42a39b6824748685629d.png"/><br/> 查看源代码发现内容在value里面，所以我们尝试用&gt;闭合input，构造js代码为:

```
"&gt;&lt;script&gt;alert("xss")&lt;/script&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1c4d34634d444ae1bcfb6809aa0fcc78.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f8c4dff940ff4e96851ff3c2eda567aa.png"/><br/> 完美通关。

### level-3

继续输入前两关的代码，都没有用哎。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7a72e191755246aface94333911d8c9d.png"/><br/> 查看源代码，发现&lt;&gt;全都被转义了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7856a750480a49018694eb1b895eab4c.png"/><br/> 至于为什么被转义，看了半天也看不出来，然后直接看这关的后端代码了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/300b237c39544cfcb3333745e5d0c891.png"/><br/> 网上查了一下htmlspecialchars()函数会将特殊字符进行转义，把预定义的字符 “&lt;” （小于）和 “&gt;” （大于）转换为 HTML 实体。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bfef745a1b624c16b9467ae1af29cb7e.png"/><br/> 所以这里就不能用 &lt; &gt;标签了，那怎么办呢，由于它不会对 ’ 进行转义，所以这里可以用事件闭合标签。这里可以用[onclick](https://www.w3school.com.cn/jsref/event_onclick.asp)事件，它可以在用户单击按钮时执行js代码。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7ae272f09928467fa1f22cc5dfb31881.png"/><br/> 所以构造onclick事件代码为：

```
'οnclick='alert("xss")

```

记得要用’进行闭合。将代码输入搜索框。还要点击一下搜索框触发onclick事件。完美通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3f55383c47374163bd92689ecda5bff6.png"/><br/> 除了onclick以外还可以使用onmouseover，'οnmοuseοver='alert(“xss”)，只需要把鼠标放上去就可以了。

### level-4

输入第三关的代码发现没用。查看源代码发现要用双引号闭合<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ef5306c2c2224b85a4c74b0e60f7253e.png"/><br/> 直接把上一关的代码单引号改为双引号闭合，这里不知道为什么`"onclick="alert(xss)`无法通关，而`"onclick="alert(1)`就可以<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3002bcdd04644d61bac4aaa78910458b.png"/><br/> 完成的不错。

### level-5

输入第四关的payload，一如既往的没用。看一下前端，发现onclick变成了o_nclick。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/37b8bae45daa49ca8e15065ffb4baaa9.png"/>

原因也很简单，看一下后端代码，直接把on转换成了o_n，所以什么onclick、onmouseover都没用，也尝试了大小写ON和`&lt;script&gt;`也还是没用用，肯定是经过了转换。前面几关的方法都不管用那怎么办呢。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2de42e0ca0b14a558438eab46a7f5aec.png"/><br/> 这里可以使用使用a标签`href`构造超链接，利用javascript伪协议进行绕过。参考[xss篇幅-JavaScript伪协议](https://blog.csdn.net/weixin_50464560/article/details/116501498)<br/> 构造一个超链接代码：

```
"&gt;&lt;a href='javascript:alert(1)'&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/da8503a9743d481093217a3cc39c9d00.png"/><br/> 这里出现超链接标签，点击，完美通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/baf77e32bcea4d17b79fe49b3d1762f1.png"/>

### level-6

把第五关的payload丢进来，失败，看一下前端。href直接变成了hr_ef。。。。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/136bfce607644c1eb038fb02872dc74b.png"/><br/> 一看后端，发现script、on、src、data、href什么的都被转换了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4a744cacb9784b9998902fdd36e9ebef.png"/><br/> 尝试了很多方法，发现没有管大小写，直接构造payload：

```
"&gt;&lt;SCRIPT&gt;alert(1)&lt;/SCRIPT&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8b244b270a33494ca01524a4e828f185.png"/><br/> 完成的不错。

### level-7

老规矩将上一关payload放进去，发现直接变成了空值，看一下后端就明白了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7f18355491c145c1b90cbb5302da2a5f.png"/><br/> 上一关的大小写一样没有用，正确的解法是双写绕过。直接构造payload：

```
"&gt;&lt;scscriptript&gt;alert(1)&lt;/scscriptript&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/68742b0085a84e58b269f54809f00643.png"/><br/> 完美通关。

### level-8

这关看到了和前面完全不同的东西，看到这个友情链接，有点像href了<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f7a5c26e603348b496d4d68c7efd4a6d.png"/><br/> 把`"&gt;&lt;a href='javascript:alert(1)'&gt;`放进去，没什么用还是被过滤。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4ca134715e424a5ea2655b5e993a5686.png"/><br/> 其实这关要用到编码绕过，利用unicode在线编码网站https://www.matools.com/code-convert-unicode<br/> 由于这里本身存在`&lt;a href=`所以只需要编码`javascript:alert(1)`，编码后为`&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#49;&amp;#41;`<br/> 放进去试试看。完美通关<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/389d6c7db0444ee59285bba8fac28efe.png"/>

### level-9

直接放第八关payload，没用。看一下后端，不仅有好多过滤，还多了一个strpos()函数，[strpos()介绍](https://www.w3school.com.cn/php/func_string_strpos.asp)，说是查找字符串在另一字符串中第一次出现的位置，在这关中就是用来判断有没有`http://`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/298339be22a24dd4831d21d5814e201e.png"/><br/> 所以构造一个payload为：

```
javascript:alert('xsshttp://)'

```

but页面还是没有反应，原因是忘了还有过滤，所以用第八关的思路将关键词javascript部分字符编码一下：

```
java&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;:alert('xsshttp://')

```

### level-10

没有输入框了，url上玩一波payload也没什么用

```
&lt;script&gt;alert(1)&lt;/script&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/65aac3043a82496c94a13f019d00203d.png"/><br/> 毫无头绪，看一下后端吧。看到了这些东西。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/da8f33a4fd624f668bb22f6ee2a1051c.png"/><br/> 可以看到这关是要通关t_sort表单提交数据。而且有一个函数str_replace,不懂得可以看看[str_replace()函数介绍](https://www.w3school.com.cn/php/func_string_str_replace.asp)，总之告诉我们payload中是不能含有&lt;&gt;的。所以构造一个`"onclick="alert(1)`放进url中，注意是要用t_sort提交数据：

```
?keyword=&lt;script&gt;alert(1)&lt;/script&gt;&amp;t_sort="οnclick="alert(1)

```

但好像没有地方点击来触发onclick啊，所以还得把hidden取消掉。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5c3cf9d9ec0a4e57b269e5aa3f15c79b.png"/><br/> 修改一下payload：

```
?keyword=&lt;script&gt;alert(1)&lt;/script&gt;&amp;t_sort=" type="text" οnclick="alert(1)

```

发现出来了一个文本框，点击一下，完美通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4d12879f62dc44d79961bc7a71f97109.png"/>

### level-11

第十关后难度就很大了，我们直接查看源码吧。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ab462da9921541eb8f3865a8485ef450.png"/><br/> 这两个地方让人怀疑。先看`$str11=$_SERVER['HTTP_REFERER']`，HTTP_REFERER是获取http请求中的Referer字段的，也就是链接到当前页面的前一页面。从这里下手。用burp抓个包看看。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4b19b31aa07a4ecf9a4bfefed2ad95ed.png"/><br/> 可以看到没有referer的消息，构造一个referer发送过去可以看到被t_ref获取了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5a62e2eb6dd64bf788f32c2d0cd9ca39.png"/><br/> 尝试构造代码：

```
" οnclick="alert(1)" type="text

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3510aebe146d42dbb8db2177dab2b73c.png"/><br/> 直接在proxy模块数据包中加上`referer:" onclick="alert(1)" type="text`发送过去，页面出现一个文本框，点击一下，通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ea63bea078fa45a384b179ef5204e693.png"/><br/> 再看一下前端，出现了这样的信息<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/890b8be1789a4d3984e5c98e499b4ad7.png"/>

### level-12

直接看源码，这次是`$_SERVER['HTTP_USER_AGENT']`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0e1cc330eccc4a9dbe157fd4dc8a51aa.png"/><br/> 抓个包先。看到UA消息让t_ua获取了。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8a586b1e7fb44f7bbc744093677d6030.png"/><br/> 直接把UA内容改为`" onclick="alert(1)" type="text`发送，通关辣！<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7762bbd1096943dcbea987315750b58a.png"/>

### level-13

先看源码，有了前两关的经验，一眼就能发现问题，没错就是cookie。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dbed9d5e1ff747fabef32d4aad17fc43.png"/><br/> 老规矩先抓包。cookie消息被t_cook接收。这里还多了一个参数user，所以用hackbar和modify headers构造的同学要注意一下。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bafe4fc271e742e298423ddfbe11cd90.png"/><br/> 我们直接修改cookie为`user=" onclick="alert(1)" type="text`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/11f85d63042e4041a63990d574269a0d.png"/>

### level-14

6，啥都没有。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/02e51a2fea204a44b6da888e0ff4a153.png"/><br/> 看源码吧。只有这点，好像要跳转，可这个网站怎么也打不开。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/81f236902ba944f8b3d96fe1dd35bec4.png"/><br/> F12看了一下网络有一个404的东西，网站跳转不了这关也没法完成。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bbf3793c0f5341c7b40898c761bb0d15.png"/><br/> 网上查了一查，是什么exif xss，有兴趣的同学可以看一下[exif xss 复现](https://blog.csdn.net/qq_32393893/article/details/104814749)

### level-15

啥都没有。。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3351b3c03a464d9faca86e6f24a1d1c4.png"/><br/> 直接看源码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cc0bcbf009c84a92b24d909ca22632be.png"/><br/> ng-include是AngularJS的指令，完全没有接触过，有兴趣的可以看看[AngularJS ng-include 指令](https://www.runoob.com/angularjs/ng-ng-include.html)，总之就是类似于include函数，用于包含外部的 HTML文件。还要注意：

> 
1.ng-include,如果单纯指定地址，必须要加引号
2.ng-include,加载外部html，script标签中的内容不执行
3.ng-include,加载外部html中含有style标签样式可以识别


源码中可以发现是通过src传参，还对 &lt; &gt; 进行了过滤，既然类似于包含，那我们就包含一个level1.php，构造payload：

```
'level1.php?name=&lt;a href="javascript:alert(1)"&gt;'

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d5d4c92371384cbeafb76d7b57a4a0ce.png"/><br/> 点一下蓝色的标签，完美通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/208b888359bb44029bf9f41e96377e15.png"/>

### level-16

url里面写上最简单的xss先试一试。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/11db7dccb67a4c94a516cd03983adf18.png"/><br/> 发现`&lt;script&gt;alert(1)&lt;/script&gt;`变成了`&lt; &gt;alert(1)&lt; &gt;`，看一下源码。发现是把script，空格，/，都转换成了&amp;nbsp，&amp;nbsp就是空格字符。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/70a8e9b50ed54402955228bf62fcbe8a.png"/><br/> 这里用[onerror事件](https://www.runoob.com/jsref/event-onerror.html)进行绕过

```
&lt;img src=1 onerror=alert(1)&gt;

```

这串代码意思就是如果在加载src给的图片时发生错误则执行 js。通过源码看到空格被过滤，那么最常用的就是用回车来代替空格。

```
&lt;img
src=1
onerror=alert(1)&gt;

```

回车的url编码为%0A，所以最终payload为：

```
&lt;img%0Asrc=1%0Aonerror=alert(1)&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b91e02dd08284eb185e2a44e09e31e43.png"/><br/> 通关通关。

### level-17

看一下url应该是arg01和arg02进行传参。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/01eaca9403424b9da67bff04c918d515.png"/><br/> 试一下onclick事件。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/799ff50b1a2e4583a8516e25b26d29b6.png"/>

点一下图片会跳转发现没什么用。换成onmouseover试试。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3fac9a6eced74da8892f7d9526cf7d00.png"/><br/> 鼠标移到图片上，成功通关。

### level-18

一片黑。。。而且通关url看到和上一关一样用arg01，arg02传参。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8157fd019ab84b1d92cadd0ba9a46c22.png"/>继续用onmouseover事件`?arg01= onmouseover&amp;arg02=alert(1)`，直接就过了？？？<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8356bb9935204e1fbd0ca1bfed515c91.png"/>

### level-19/20

url里还是有arg01和arg02传参，继续用上一关的payload。什么都没有。看一下前端，奥原来在双引号里，需要闭合。试了一下也没什么用，原因就是这里依然有htmlspecialchars()函数进行处理，所以无法成功闭合。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f2f7a0317db841a398fd4cbf657376f6.png"/><br/> 网上查了一下，要用到flash反编译，这方面的知识还是空白，先学习一下，后边再发出来。20关也是一样。有兴趣的同学可以看一下别的大佬的writeup：[XSS-labs Level 19 Flash XSS](https://baynk.blog.csdn.net/article/details/103213877)

### 结语

这次的xsslabs通关耗费了挺多时间，由于本人才学疏浅，难免会有一些错误，希望大家能指正批评，如有疑问，可在下方留言，会第一时间进行回复!<br/> 感谢同学愿意花时间阅读这篇文章，希望可以对你有所帮助！
