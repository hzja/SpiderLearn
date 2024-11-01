# 原创
：  【攻防世界WEB】难度五星15分进阶题：bug

# 【攻防世界WEB】难度五星15分进阶题：bug

## 一、bug

> 

 

<h3>解题方法：</h3>
1、越权，文件上传，payload


> 
<h3>过程：</h3>
注册，和找回密码
不就是到了越权的时候了嘛

随便注册一个

前面还有4个

回去进行登录


点击manage，提示要admin

<hr/>
尝试越权修改密码 
 <img alt="" height="281" src="https://img-blog.csdnimg.cn/0d2aa2ceccb347c0bd67805050a2f1a0.png" width="724"/>
使用bp抓包
发现登录以后修改密码，不会带username
<img alt="" height="544" src="https://img-blog.csdnimg.cn/513c7f2d173c42cb87fdcfc023c5febb.png" width="871"/> 
 想到开始页面也有一个修改密码
 <img alt="" height="272" src="https://img-blog.csdnimg.cn/e0600c4186f04fa786966aa23aeb5133.png" width="679"/>
<img alt="" height="229" src="https://img-blog.csdnimg.cn/fb600d063da04c5993a5a28864703d82.png" width="607"/> 

这里有一个username
改为admin


 
<hr/>
使用admin进行登录

 点击manage
提示ip不被允许

 抓包修改为本地访问（即X-Forwarded-For:127.0.0.1）
 <img alt="" height="590" src="https://img-blog.csdnimg.cn/87ad3913a2314b1b99c33dcf6dde3cb8.png" width="1200"/>
 看到了flag，近了，看一下源码
 看到一个传参页面
index.php?module=filemanage&amp;do=???<img alt="" height="724" src="https://img-blog.csdnimg.cn/f671bd42ca364446b429abe8e8d9627b.png" width="1200"/>
 
 文件管理的行动
一般就是文件上传能利用了
来试一下是不是文件上传upload

 Just image?
考虑：
使用图片马
或者绕过检测

接下来考虑利用文件上传漏洞了
<hr/>
肯定是会有过滤的
我先把文明命名为了shell.jpg（或者改Content-Type）
然后使用bp抓包修改为php6，先提前分析一波结果

 
因该是内容的问题
查阅了发现payload为
&lt;script language="php"&gt;@eval($_POST['1']);&lt;/script&gt;

php3不能被识别为php文件

 然后又说这不是一个php文件

 
<hr/>
 无语啦，打错了一个字母，说我不是php了（我还改了各半小时，最后还是发现问题了）
醉了醉了

 三个部分：（别打错啦）
"shell.php5"（php4也可）
 image/png（jpeg，gif也可）
 &lt;script language="php"&gt; @eval($_POST['cmd']); &lt;/script&gt;（中间内容可改）


---


---

