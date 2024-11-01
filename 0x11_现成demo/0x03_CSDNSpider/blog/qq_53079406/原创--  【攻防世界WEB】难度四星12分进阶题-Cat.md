# 原创
：  【攻防世界WEB】难度四星12分进阶题：Cat

# 【攻防世界WEB】难度四星12分进阶题：Cat

## 一、Cat

> 

 
<h3>解题方法：</h3>
1、注入点、大量代码理解、bp跑过滤、带出文件


> 
<h3>过程：</h3>
输入后url后面接了域名
考虑：
1、能不能访问主机本地
2、?url是否存在注入
（输入框和?url=是同一处）

<hr/>
输入127.0.0.1
发现ping了自己
考虑：
能否拼接命令在后面呢

 payload：
127.0.0.1 | ls
提示无效网址，应该是被过滤了

<hr/>
是用bp对特殊字符进行爆破
看哪些未被过滤
发现有 - . / @未被过滤

<hr/>
 
看是否能通过编码，然后被解码绕过
先测试一下能否使用URL编码

找了几个整数测试
%100没报错
%90报错了
 是html代码<img alt="" height="877" src="https://img-blog.csdnimg.cn/9428e645f1c447838c982230ff5c7c99.png" width="1200"/>
复制到txt中
没找到有用信息

 
再改为html后缀
然后再浏览器打开
 <img alt="" height="294" src="https://img-blog.csdnimg.cn/a7684210b1784a358d67c9bc4c7cb65a.png" width="312"/>

需要去了解Django
Django 是一个开放源代码的 Web 应用框架，由Python编写的
寻找settings，寻找文件的路径

/opt/api/database.sqlite3
<hr/>
我们前面爆破出了@未被过滤
php中可以通过@+完整路径来读取文件（现在CURLFile）
前提：
PHP&lt;=5.5
有个键值，然后value必须是个数组
content-type：multipart/form-data
<hr/>
构造payload：
?url=@/opt/api/database.sqlite3
仔细看了一下，出现了新源码

 
<hr/>
再放到txt中进行查看一番

 
源码里找到flag字样，可能多半就能找到了

查找ctf找到了flag

 

 WHCTF{yoooo_Such_A_G00D_@}


---


---


---

