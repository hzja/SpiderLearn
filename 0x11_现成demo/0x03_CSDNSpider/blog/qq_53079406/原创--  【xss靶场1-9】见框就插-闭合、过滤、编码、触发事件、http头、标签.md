# 原创
：  【xss靶场1-9】见框就插：闭合、过滤、编码、触发事件、http头、标签

# 【xss靶场1-9】见框就插：闭合、过滤、编码、触发事件、http头、标签

**目录**

[一、推荐](#%E4%B8%80%E3%80%81%E6%8E%A8%E8%8D%90)

[Less1（无过滤）](#Less1%EF%BC%88%E6%97%A0%E8%BF%87%E6%BB%A4%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less2（闭合标签）](#Less2%EF%BC%88%E9%97%AD%E5%90%88%E6%A0%87%E7%AD%BE%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less3（'闭合+触发事件）](#Less3%EF%BC%88'%20rel=)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less4（&lt;&gt;被过滤+"闭合+触发事件）](#Less4%EF%BC%88%3C%3E%E8%A2%AB%E8%BF%87%E6%BB%A4%2B%22%E9%97%AD%E5%90%88%2B%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less5（构造链接+"/&gt;闭合）](#Less5%EF%BC%88%E6%9E%84%E9%80%A0%E9%93%BE%E6%8E%A5%2B%22%2F%3E%E9%97%AD%E5%90%88%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less6（构造链接+"/&gt;闭合+大小写混淆绕过）](#Less6%EF%BC%88%E6%9E%84%E9%80%A0%E9%93%BE%E6%8E%A5%2B%22%2F%3E%E9%97%AD%E5%90%88%2B%E5%A4%A7%E5%B0%8F%E5%86%99%E6%B7%B7%E6%B7%86%E7%BB%95%E8%BF%87%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less7（构造链接+"/&gt;闭合+关键字过滤+双写混淆绕过）](#Less7%EF%BC%88%E6%9E%84%E9%80%A0%E9%93%BE%E6%8E%A5%2B%22%2F%3E%E9%97%AD%E5%90%88%2B%E5%85%B3%E9%94%AE%E5%AD%97%E8%BF%87%E6%BB%A4%2B%E5%8F%8C%E5%86%99%E6%B7%B7%E6%B7%86%E7%BB%95%E8%BF%87%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Less8（编码绕过+关键字过滤）](#Less8%EF%BC%88%E7%BC%96%E7%A0%81%E7%BB%95%E8%BF%87%2B%E5%85%B3%E9%94%AE%E5%AD%97%E8%BF%87%E6%BB%A4%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[ Less9（编码绕过+关键字过滤+http头）](#%C2%A0Less9%EF%BC%88%E7%BC%96%E7%A0%81%E7%BB%95%E8%BF%87%2B%E5%85%B3%E9%94%AE%E5%AD%97%E8%BF%87%E6%BB%A4%2Bhttp%E5%A4%B4%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>一、推荐</h2>
[【XSS跨站合集】反射型、存储型、DOM类XSS原理；输出在HTML、CSS、Javascript代码中<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165802668016781818737899%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165802668016781818737899&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.185^v2^control&amp;utm_term=xss&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123694180?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165802668016781818737899%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165802668016781818737899&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-123694180-null-null.185%5Ev2%5Econtrol&amp;utm_term=xss&amp;spm=1018.2226.3001.4450)


---


---


## Less1（无过滤）

> 
<h3>特点：</h3>
参数中插入
无过滤
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;




 

---


---


## Less2（闭合标签）

> 
<h3>特点：</h3>
参数中插入
被HTMLL编码了
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;

<hr/>
右键查看源码
可以看到我们输入的内容被HTML实体编码了
扩展：
HTML实体编码，格式 以&amp;符号开头，以;分号结尾
十进制的ASCLL编码,格式: 以符号&amp;#开头，分号;结尾

 
<hr/>
打开开发者模式（Ctrl+shift+I）
定位到输入框位置
可以看见是在value标签框里

 
<hr/>
尝试闭合标签
"&gt;&lt;script&gt;alert(/xss/)&lt;/script&gt;
可以在URL中输入，也可以再搜索框中输入

 <img alt="" height="926" src="https://img-blog.csdnimg.cn/9c6a42133e254c1586c8b26fb73ef070.png" width="1200"/>
 


---


---


---


## Less3（'闭合+触发事件）

> 
<h3>特点：</h3>
参数中插入
被HTMLL编码了
单引号闭合
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;<img alt="" height="898" src="https://img-blog.csdnimg.cn/fc722225df1c4659a74ab309b5a3c419.png" width="1200"/>
 

<hr/>
右键查看源码
可以看到我们输入的内容被HTML实体编码了
扩展：
HTML实体编码，格式 以&amp;符号开头，以;分号结尾
十进制的ASCLL编码,格式: 以符号&amp;#开头，分号;结尾

<hr/>
 
打开开发者模式（Ctrl+shift+I）
定位到输入框位置
可以看见是在value标签框里

 

<hr/>
尝试闭合标签
"&gt;&lt;script&gt;alert(/xss/)&lt;/script&gt;
从搜索框中输入
发现已经没效果了

 
 前后出现了单引号，考虑单引号闭合他们<img alt="" height="644" src="https://img-blog.csdnimg.cn/62bbe4d9ab954367a15055b0d6ecc87b.png" width="1200"/>
 
<hr/>
尝试使用触发事件函数来弹窗
扩展：
onclick（点击）
onerror（加载外部文件（文档、图像）发生错误时触发）
onmouseover（鼠标滑过）
……
'οnclick='alert()
 然后再点击一下输入框


 


---


---


---


---


## Less4（&lt;&gt;被过滤+"闭合+触发事件）

> 
<h3>特点：</h3>
参数中插入
被HTMLL编码了
&lt;&gt;被过滤为空了
双引号闭合
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;<img alt="" height="798" src="https://img-blog.csdnimg.cn/2defc05e258b4183949268c7a91779e2.png" width="1200"/>
 
<hr/>
右键查看源码
发现&lt;&gt;都变没了，变成了空的

<hr/>
 

打开开发者模式（Ctrl+shift+I）
定位到输入框位置
可以看见是在value标签框里，还是首先考虑闭合

 


<hr/>
使用"&gt;&lt;script&gt;alert(/xss/)&lt;/script&gt;已经无效了
因为&lt;&gt;都被过滤了


<hr/>
尝试使用触发事件函数来弹窗
扩展：
onclick（点击）
onerror（加载外部文件（文档、图像）发生错误时触发）
onmouseover（鼠标滑过）
……
" οnmοuseοver='alert()'
 然后移动鼠标



 <img alt="" height="692" src="https://img-blog.csdnimg.cn/48a4a86ba65541ad8dd08e76c09f05a4.png" width="1200"/>
 


---


---


---


---


## Less5（构造链接+"/&gt;闭合）

> 
<h3>特点：</h3>
参数中插入
特殊标签都被加上了下划线
")闭合
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;​​​​​​​<img alt="" height="710" src="https://img-blog.csdnimg.cn/537d3b3b8b5b4074b746c085ffcb3ae0.png" width="1200"/>
 

<hr/>
右键查看源码
发现标签被加了下划线

<hr/>
 


打开开发者模式（Ctrl+shift+I）
定位到输入框位置
可以看见是在value标签框里，还是考虑绕过，或者闭合

 

<hr/>
测试能否双写绕过
使用&lt;scrscriipt&gt;alert()&lt;/script&gt;
行不通


<hr/>
尝试使用触发事件函数来弹窗
扩展：
onclick（点击）
onerror（加载外部文件（文档、图像）发生错误时触发）
onmouseover（鼠标滑过）
……
都被加上了下划线



<hr/>
 尝试
javascript
可行

<hr/>
通过闭合前面的value,在后面构造一个链接
点击触发弹窗
payload：" /&gt; &lt;a href=javascript:alert()&gt;链接&lt;/a&gt;

 &lt;input name=keyword value=""&gt; &lt;a href=javascript:alert()&gt;something&lt;/a&gt;"&gt;

<img alt="" height="551" src="https://img-blog.csdnimg.cn/ad808709559b4d07adde1fd52ef89702.png" width="1128"/> 
 


---


---


---


---


---


## Less6（构造链接+"/&gt;闭合+大小写混淆绕过）

> 
<h3>特点：</h3>
参数中插入
特殊标签都被加上了下划线
"&gt;闭合
构造链接
大小写绕过
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;

 

<hr/>
右键查看源码
发现标签被加了下划线

<hr/>
 打开开发者模式（Ctrl+shift+I） 
定位到输入框位置
可以看见是在value标签框里，还是考虑绕过，或者闭合



<hr/>
尝试使用触发事件函数来弹窗
扩展：
onclick（点击）
onerror（加载外部文件（文档、图像）发生错误时触发）
onmouseover（鼠标滑过）
……
都被加上了下划线

 



<hr/>
 尝试
javascript
可行<img alt="" height="505" src="https://img-blog.csdnimg.cn/5f2715d5adab4daabdd0427570f3ff66.png" width="768"/>
 

<hr/>
通过闭合前面的value,在后面构造一个链接
点击触发弹窗
payload：" /&gt; &lt;a href=javascript:alert()&gt;链接&lt;/a&gt;

 &lt;input name=keyword value=""&gt; &lt;a href=javascript:alert()&gt;something&lt;/a&gt;"&gt;
发现链接点不了
查看后发现是href被加了下划线


 
<hr/>
考虑绕过
考虑大小写绕过，或者双写绕过
" /&gt; &lt;a hRef=javascript:alert()&gt;链接&lt;/a&gt;
未被过滤了


 


---


---


---


---


---


## Less7（构造链接+"/&gt;闭合+关键字过滤+双写混淆绕过）

> 
<h3>特点：</h3>
参数中插入
首先被全部转换为小写，然后关键字被过滤
"&gt;闭合
构造链接
双写绕过
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;

 
<hr/>
右键查看源码
发现标签被过滤了


<hr/>
尝试使用触发事件函数来弹窗
扩展：
onclick（点击）
onerror（加载外部文件（文档、图像）发生错误时触发）
onmouseover（鼠标滑过）
……
发现也被过滤了


<hr/>
 尝试
javascript
发现也被过滤了

 
<hr/>
考虑绕过过滤
考虑大小写绕过，或者双写绕过
" /&gt; &lt;a hRef=JavaScript:alert()&gt;链接&lt;/a&gt;
发现全部被转换为了小写，且被过滤了


 "&gt; &lt;a hrhrefef='javascriscriptpt:alert()'&gt;链接&lt;/a&gt;

 
<hr/>
或者直接弹窗
"&gt;&lt;scrscriptipt&gt;alert()&lt;/scrscriptipt&gt;

 


---


---


---


---


## Less8（编码绕过+关键字过滤）

> 
<h3>特点：</h3>
参数中插入
首先被全部转换为小写，然后关键字被过滤
编码绕过
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;


<hr/>
右键查看源码

发现关键字被加了下划线<img alt="" height="540" src="https://img-blog.csdnimg.cn/8011abe8c9224315b4d04463d6b96d27.png" width="1200"/>
 

<hr/>
 尝试
javascript
发现也被加了下划线


<hr/>
考虑绕过过滤
考虑大小写绕过，或者双写绕过
javascript:alert()
被进行了编码，和过滤


<hr/>
尝试进行HTML编码绕过
可以选择局部字符编码，也可以全部编码绕过



 
 <img alt="" height="323" src="https://img-blog.csdnimg.cn/faef510d740f4107af33812f1d67ee4f.png" width="1200"/>
就变成了
javascri&amp;#112;&amp;#116;:alert()

 
<hr/>
全部编码就是
&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#41;

 <img alt="" height="540" src="https://img-blog.csdnimg.cn/d01f1c310727427daf89dca62f72b217.png" width="757"/>
 


---


---


---


---


##  Less9（编码绕过+关键字过滤+http头）

> 
<h3>特点：</h3>
参数中插入
首先被全部转换为小写，然后关键字被过滤
编码绕过
添加http头
反射性


> 
<h3>利用：</h3>
见空就插，看见有参数，插
&lt;script&gt;alert()&lt;/script&gt;
提示不合法


http://&lt;script&gt;alert()&lt;/script&gt;
添加链接后，点击无效果

 右键查看源码
关键字是被加上了下划线

 

<hr/>
尝试进行HTML编码绕过
可以选择局部字符编码，也可以全部编码绕过
http://javascript:alert()



就变成了
javascri&amp;#112;&amp;#116;:alert()//http://

 

<hr/>
全部编码就是
&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#41;//http://
 

 ​​​​​​<img alt="" height="537" src="https://img-blog.csdnimg.cn/26d075d365ed45b99268b1e47b2499f3.png" width="773"/>
 


---

