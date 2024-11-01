# 原创
：  【webGoat】Broken Access Control

# 【webGoat】Broken Access Control

**目录**

[Broken Access Control](#Broken%20Access%20Control)

[一、Insecure Direct Object References（不安全的直接对象引用）](#%E4%B8%80%E3%80%81Insecure%20Direct%20Object%20References%EF%BC%88%E4%B8%8D%E5%AE%89%E5%85%A8%E7%9A%84%E7%9B%B4%E6%8E%A5%E5%AF%B9%E8%B1%A1%E5%BC%95%E7%94%A8%EF%BC%89)

[第2题：](#%E7%AC%AC2%E9%A2%98%EF%BC%9A)

[第3题：](#%E7%AC%AC3%E9%A2%98%EF%BC%9A)

[第4题：](#%E7%AC%AC4%E9%A2%98%EF%BC%9A)

[第5题：](#%E7%AC%AC5%E9%A2%98%EF%BC%9A)

[二、Missing Function Level Access Control(缺少功能级别访问控制)](#%E4%BA%8C%E3%80%81Missing%20Function%20Level%20Access%20Control%28%E7%BC%BA%E5%B0%91%E5%8A%9F%E8%83%BD%E7%BA%A7%E5%88%AB%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%29)

[第2题：](#%E7%AC%AC2%E9%A2%98%EF%BC%9A)

[第3题： ](#%E7%AC%AC3%E9%A2%98%EF%BC%9A%C2%A0)

---


## Broken Access Control

> 
<h3>一、Insecure Direct Object References（不安全的直接对象引用）</h3>
<h4>第2题：</h4>
先登陆

提示Tom登陆成功，让我们继续去下一关操作
 <img alt="" height="164" src="https://img-blog.csdnimg.cn/fc6b35482fcb43c2a99a4aedef8df56f.png" width="736"/>

<hr/>
<hr/>
<h4>第3题：</h4>
题目意思：让我们找隐藏数据（即隐藏参数）
点之后有个人信息

 现在对其进行抓包，并发送到repeater
分析数据包中隐藏数据（参数）
隐藏参数一目了然
role,userId

 <img alt="" height="139" src="https://img-blog.csdnimg.cn/edca652d614d40e384515cb0bc1f3616.png" width="811"/>
 <img alt="" height="195" src="https://img-blog.csdnimg.cn/e198186233a84cff9187e2cc33c713c7.png" width="960"/>
<hr/>
<hr/>
<h4>第4题：</h4>
 标题为：以另一种方式查看您自己的个人资料
有userId值，尝试作为下一目录

WebGoat/IDOR/profile/2342384 

然后成功了
 <img alt="" height="195" src="https://img-blog.csdnimg.cn/3ad1122d07a449e3b906886dfec44ea6.png" width="868"/>

<hr/>
<hr/>
<h4>第5题：</h4>
第一处：查看其他个人资料
第二处：编辑其他配置文件
由上面可知道
WebGoat/IDOR/profile/xxxxxxx
可能为7位，获取对应id的账户（可以从1开始往上爆破）
2342388
Buffalo Bill
1、role=3改为1
2、color=brown颜色改为red
{<br/>     "role":"1", <br/>     "color":"red", <br/>     "size":"large",<br/>     "name":"Buffalo Bill",<br/>     "userId":"2342388"<br/> }
3、Content-type改成application/json




4、题目提示使用的是RESTful应用程序（全局修改用PUT请求，局部PATCH）
这里使用PUT请求


将上面的修改后，就成功完成了




---


#### 第3题：

---


---


#### 第5题：

 

> 
<h3>二、Missing Function Level Access Control(缺少功能级别访问控制)</h3>
<h4>第2题：</h4>
我发现一个问题，使用开发者模式查看源码，和使用Ctrl+U查看源码，有区别
开发者模式源码更全，在Ctrl+U的源码中都没找到这些信息


User
Config


<hr/>
<hr/>
<h4>第3题： </h4>
题目为：收集用户信息
上一题得到的
/User
/Config
访问127.0.0.1:8080/WebGoat/users
并抓包，发送到repeater
报500


增加content-type: application/json
返回了Hash值
hMSR8Wnr9XxAhiFLhff1t0tkrE3xAVvlbKVRIYQ6vSc=

 成功完成




---


#### 第3题： 
