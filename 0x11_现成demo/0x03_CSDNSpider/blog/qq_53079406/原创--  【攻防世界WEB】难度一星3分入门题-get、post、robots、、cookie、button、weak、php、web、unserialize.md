# 原创
：  【攻防世界WEB】难度一星3分入门题：get、post、robots、、cookie、button、weak、php、web、unserialize

# 【攻防世界WEB】难度一星3分入门题：get、post、robots、、cookie、button、weak、php、web、unserialize

**目录**

[一、view_source](#%E4%B8%80%E3%80%81view_source)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[ 过程](#%C2%A0%E8%BF%87%E7%A8%8B)

[二、get_post](#%E4%BA%8C%E3%80%81get_post)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[三、robots](#%E4%B8%89%E3%80%81robots)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[知识点：](#%E7%9F%A5%E8%AF%86%E7%82%B9%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[四、backup](#%E5%9B%9B%E3%80%81backup)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[五、cookie](#%E4%BA%94%E3%80%81cookie)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[六、disabled_button](#%E5%85%AD%E3%80%81disabled_button)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[七、weak_auth](#%E4%B8%83%E3%80%81weak_auth)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[八、simple_php](#%E5%85%AB%E3%80%81simple_php)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[九、baby_web](#%E4%B9%9D%E3%80%81baby_web)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十、Training-WWW-Robots](#%E5%8D%81%E3%80%81Training-WWW-Robots)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[ 知识点：](#%C2%A0%E7%9F%A5%E8%AF%86%E7%82%B9%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十一、ics-06](#%E5%8D%81%E4%B8%80%E3%80%81ics-06)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十二、PHP2](#%E5%8D%81%E4%BA%8C%E3%80%81PHP2)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[十三、unserialize3](#%E5%8D%81%E4%B8%89%E3%80%81unserialize3)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[ 知识点：](#%C2%A0%E7%9F%A5%E8%AF%86%E7%82%B9%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

---


## 一、view_source

> 

<h3>解题方法：</h3>
1、使用开发者工具查看源代码（F12、鼠标右键单击、Ctrl+Shift+I、Ctrl+U）
2、在URL头部输入view-source://
3、将html 页面存储到本地查看
4、使用BurpSuite 抓包获得网页源代码
5、关闭浏览器js功能


> 
<h3> 过程</h3>
使用开发者工具查看源代码


<hr/>
view-source:http://61.147.171.105:65305/


<hr/>
html 页面存储到本地查看


<hr/>
BurpSuite 代理抓包获得网页源代码

<hr/>
5、关闭浏览器js功能
不能右键空白页面，可能是js控制的前端
方法一：可以使用js开关插件

方法二：永久关闭js功能
在火狐地址栏输入：about:config
点“接收风险并继续”按钮
搜索javascript.enabled，然后双击该栏，把值变为false即可关闭js


---


---


---


---


## 二、get_post

> 


<h3>解题方法：</h3>
1、使用工具HackBar
2、使用Robots协议（都不能查看）


> 
<h3>过程</h3>
使用工具HackBar



<hr/>
使用Robots协议（都不能查看）




---


---


## 三、robots

> 


<h3>解题方法：</h3>
1、查看robots.txt文件


> 
<h3>知识点：</h3>
[【robots协议】简介、理解<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5502)



> 
<h3>过程</h3>
在网址后加上/robots.txt
查看访问原则<br/><img alt="" height="299" src="https://img-blog.csdnimg.cn/a2c94b84217a42c9b60dbfb373e09113.png" width="816"/>
访问/f1ag_1s_h3re.php页面





---


---


## 四、backup

> 


<h3>解题方法：</h3>
1、备份文件后缀.bak


> 
<h3>过程</h3>
大多数的管理员为了以后方便都会将备份文件的后缀写成.bak，所以，我们这里就是找到.bak的文件
找到index.php的备份文件，所以我们先在url栏中输入index.php.bak



<hr/>
.bak将前面的.php给覆盖了（且无法直接打开）
将.bak给去掉




---


---


## 五、cookie

> 


<h3>解题方法：</h3>
1、使用工具HackBar
2、使用bp抓包


> 
<h3>过程</h3>
使用工具cookie Editor
（或者使用bp抓包）


<hr/>
进入cookie.php这个页面
看见
See the http response
（看返回包，直接在开发者工具里面看）
（或者使用bp抓包）




---


---


## 六、disabled_button

> 


<h3>解题方法：</h3>
1、删除特殊属性


> 
<h3>过程</h3>
打开开发者工具查看页面源代码
删除按钮中的‘disabled=" "’属性，按钮便可正常使用


<hr/>
点击flag按钮，出现flag





---


---


## 七、weak_auth

> 


<h3>解题方法：</h3>
1、使用bp对弱密码进行爆破


> 
<h3>过程</h3>
什么都不输入，直接点击登录
提示admin（账号）

<hr/>
账号输入admin，密码随便输入

<hr/>
 然后使用bp抓包，并对密码进行爆破（发送到intruder）

 设置有效载荷位置，并配置有效载荷字典<img alt="" height="644" src="https://img-blog.csdnimg.cn/91c4d7cc17e34923a83126f3abe05167.png" width="1200"/>
 对结果进行判断，长度明显不一致的就可能是正确密码
查看响应，获得flag




---


---


---


## 八、simple_php

> 


<h3>解题方法：</h3>
1、解读php代码


> 
<h3>过程</h3>


a，b都为get传参
flag1和flag2是我们要获得的
is_numeric()函数：检测变量是否为数字或数字字符串,是则返回TRUE，否则返回FALSE
<hr/>
http://61.147.171.105:51599/index.php?a=a&amp;b=1235b




---


---


## 九、baby_web

> 


<h3>解题方法：</h3>
1、index.php一般为php的初始页面


> 
<h3>过程</h3>
描述的初始页面是那个
php的初始页面一般为index.php

 但是都会跳转到1.php（有重定向）
尝试去掉1.php后缀也是一样



<hr/>
使用bp抓包后发送到repeater

返回包中发现有flag


---


---


## 十、Training-WWW-Robots

> 


<h3>解题方法：</h3>
1、查看robots.txt文件


> 
<h3> 知识点：</h3>
[【robots协议】简介、理解<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_53079406/article/details/125898777?spm=1001.2014.3001.5502)


> 
<h3>过程</h3>
在URL后面加上robots.txt



<hr/>
在URL后面加上/fl0g.php<br/><img alt="" height="223" src="https://img-blog.csdnimg.cn/6fa923d8b36845378a3e9ce5366a54b5.png" width="900"/>​




---


---


## 十一、ics-06

> 



<h3>解题方法：</h3>
1、使用bp对id值进行爆破


> 
<h3>过程</h3>
就这一处可以点进去




<hr/>
 题目说只有一处，使用bp抓包进行爆破
设置有效载荷位置

 设置为数字（后来发现300是不够的，3000）

设置线程（30太慢了）

发现值小了，重新加大


 分析结果，有一项返回数据包大小与其他明显不一样






---


---


## 十二、PHP2

> 



<h3>解题方法：</h3>
1、解读php代码


> 
<h3>过程</h3>
index.php页面什么也没有

<hr/>
进行扫描，我这要扫41w条，太慢了，先丢一个开始图片

 最后扫描到index.phps

<hr/>
在URL后面加上index.phps
关键信息$_GET[id] == "admin"
urldecode($_GET[id])会进行一次解码
而浏览器也会进行一次解码
所以要对admin进行2次编码
（对首字母a编码也是一样的道理）<br/><img alt="" height="884" src="https://img-blog.csdnimg.cn/588a5ed930df43018a964cbddf9bd46b.png" width="1117"/>
%2561dmin
urldecode(%2561)=%61
urldecode(%61)=a




---


---


---


## 十三、unserialize3

> 


<h3>解题方法：</h3>
1、php序列化


> 
<h3> 知识点：</h3>
[【PHP反序列化】PHP反序列化原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124227179?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165836724016781683973795%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165836724016781683973795&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124227179-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124227179?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165836724016781683973795%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165836724016781683973795&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124227179-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&amp;spm=1018.2226.3001.4450)


> 
<h3>过程</h3>
看见__wakeup()就知道涉及到序列化、反序列化
执行unserialize()反序列化时，先会调用__wakeup()函数

 理解了序列化每个字符意思
都可以看着这段代码直接写出序列化结果
?code=O:4:"xctf":1:{s:4:"flag";s:3:"111";}





<hr/>
__wakeup()漏洞：当序列化字符串所表示的对象， 其序列化字符串中属性个数大于真实属性个数时就会跳过__wakeup的执行
将变量1改为2或者其他大于1的数字
?code=O:4:"xctf":2:{s:4:"flag";s:3:"111";}<img alt="" height="887" src="https://img-blog.csdnimg.cn/6a2c073e890a41fa8c5ce8b67ed7b585.png" width="1188"/>



