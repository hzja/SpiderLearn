# 原创
：  白捡一个存储型XSS

# 白捡一个存储型XSS

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


### 起因

---


利用fofa搜索时发现

```
1.org="China Education and Research Network Center" &amp;&amp; body="/register"
```

### 任意用户注册

---


在找到该CMS的时候发现存在任意用户注册的情况

http://xxxx.edu.cn/student/Register.ashx

内容都可以伪造<img alt="" height="394" src="https://img-blog.csdnimg.cn/7781a3584adf493db96161b460789332.png" width="1080"/>

注册后得到账号 xxxxxx 密码 xxxx

### 后端姓名处存储XSS/前端限制绕过

---


在个人姓名处发现姓名存在的是前端限制，进行后端抓包突破

```
1.&lt;img src=x onerror=alert(1) //
```

来到分享界面获取我个人的`url` 触发`XSS`

**没看够~？欢迎关注！**
