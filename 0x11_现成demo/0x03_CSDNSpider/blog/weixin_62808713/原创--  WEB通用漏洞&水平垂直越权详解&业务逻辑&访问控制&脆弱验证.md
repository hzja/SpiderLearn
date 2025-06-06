# 原创
：  WEB通用漏洞&水平垂直越权详解&业务逻辑&访问控制&脆弱验证

# WEB通用漏洞&amp;水平垂直越权详解&amp;业务逻辑&amp;访问控制&amp;脆弱验证

**目录**

[一、知识点概述](#%E4%B8%80%E3%80%81%E7%9F%A5%E8%AF%86%E7%82%B9%E6%A6%82%E8%BF%B0)

[&lt;分类&gt;](#%3C%E5%88%86%E7%B1%BB%3E)

[&lt;原理简述&gt;](#%3C%E5%8E%9F%E7%90%86%E7%AE%80%E8%BF%B0%3E)

[二、水平越权示例——检测数据比对弱](#%E4%BA%8C%E3%80%81%E6%B0%B4%E5%B9%B3%E8%B6%8A%E6%9D%83%E7%A4%BA%E4%BE%8B%E2%80%94%E2%80%94%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E6%AF%94%E5%AF%B9%E5%BC%B1)

[&lt;越权演示&gt;](#%3C%E8%B6%8A%E6%9D%83%E6%BC%94%E7%A4%BA%3E)

[&lt;如何防护&gt;](#%3C%E5%A6%82%E4%BD%95%E9%98%B2%E6%8A%A4%3E)

[三、垂直越权示例——权限操作无验证](#%E4%B8%89%E3%80%81%E5%9E%82%E7%9B%B4%E8%B6%8A%E6%9D%83%E7%A4%BA%E4%BE%8B%E2%80%94%E2%80%94%E6%9D%83%E9%99%90%E6%93%8D%E4%BD%9C%E6%97%A0%E9%AA%8C%E8%AF%81)

[&lt;越权演示&gt;](#%3C%E8%B6%8A%E6%9D%83%E6%BC%94%E7%A4%BA%3E)

[&lt;漏洞成因&gt;](#%3C%E6%BC%8F%E6%B4%9E%E6%88%90%E5%9B%A0%3E)

[四、访问控制示例——代码未引用验证](#%E5%9B%9B%E3%80%81%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E7%A4%BA%E4%BE%8B%E2%80%94%E2%80%94%E4%BB%A3%E7%A0%81%E6%9C%AA%E5%BC%95%E7%94%A8%E9%AA%8C%E8%AF%81)

[&lt;越权演示&gt;](#%3C%E8%B6%8A%E6%9D%83%E6%BC%94%E7%A4%BA%3E)

[五、脆弱机制示例——Cookie脆弱验证](#%E4%BA%94%E3%80%81%E8%84%86%E5%BC%B1%E6%9C%BA%E5%88%B6%E7%A4%BA%E4%BE%8B%E2%80%94%E2%80%94Cookie%E8%84%86%E5%BC%B1%E9%AA%8C%E8%AF%81)

[&lt;越权演示&gt;](#%3C%E8%B6%8A%E6%9D%83%E6%BC%94%E7%A4%BA%3E)

[&lt;真实案例演示&gt;](#%3C%E7%9C%9F%E5%AE%9E%E6%A1%88%E4%BE%8B%E6%BC%94%E7%A4%BA%3E)

[六、空口令机制示例——Redis&amp;Weblogic 弱机制](#%E5%85%AD%E3%80%81%E7%A9%BA%E5%8F%A3%E4%BB%A4%E6%9C%BA%E5%88%B6%E7%A4%BA%E4%BE%8B%E2%80%94%E2%80%94Redis%26Weblogic%20%E5%BC%B1%E6%9C%BA%E5%88%B6)

[&lt;演示一&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%B8%80%3E)

[&lt;演示二&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%BA%8C%3E)

---


## 一、知识点概述

### &lt;分类&gt;
1. 水平越权——同级用户权限共享。1. 垂直越权——低高用户权限共享。1. 访问控制——验证丢失&amp;取消验证。1. 脆弱验证——Cookie&amp;Token&amp;Jwt。 
### &lt;原理简述&gt;

## 二、水平越权示例——检测数据比对弱

### &lt;越权演示&gt;

1.打开要进行测试的网站的数据库，可以看到数据库内存储了几个用户的账户信息。

2.打开要测试的网站。

3. 登陆一个用户。

4. 打开网站的修改个人信息的页面，点击修改后进行抓包。

5.抓到的数据包如下图所示。 

6.前面查看数据库的时候可以看到有个账户名为xiaodi002的账户。

7.我们将数据包内的账户名修改为xiaodi002，同时将下面的id值更改为2，因为数据库内对应的xiaodi002的账户的id值为2，同时将其它信息也进行修改。

8. 放包后网页内显示“信息编辑成功”。

9. 此时再次查看数据库可以发现刚刚修改的信息被添加到了账户名为xiaodi002的账户上。

### &lt;如何防护&gt;

1.对比当前用户，当前登陆的用户是谁，在修改信息的时候先获取到当前用户的用户名，在进行修改的时候，就在此基础上进行修改，及时用户将账户名改成其它的，依然无效。

2.查看源代码，可以看到其对nickname进行了接收，它不是固定死的，用户发送的是谁，它带入的就是谁，这就导致其可以对其它用户进行操作。

3.如果在用户进行登陆的时候，就将用户的用户名给获取到然后固定死了，就不会发生上面的事情了。

## 三、垂直越权示例——权限操作无验证

### &lt;越权演示&gt;

1.打开要进行测试的网站。

2.点击撰写文章后随便写入内容然后发布。

<img alt="" height="517" src="https://img-blog.csdnimg.cn/294037d404c84551bc78aef06fbf11dd.png" width="1134"/> 3. 可以看到文章已经写入了。

 4. 来到网站的后台。

5. 我们选中回收按钮之后复制它的链接。

<img alt="" height="30" src="https://img-blog.csdnimg.cn/dbf58686d33e4abc9d3a886ae7c8a77b.png" width="512"/>  

6.换一个没有登陆过的浏览器先尝试访问它的后台。

7.上边讲到的那个回收选项只存在于后台内，我们在这个新的浏览器里并没有进行登陆，此状态下来尝试执行刚刚复制出来的回收文章的链接。

8.当我们访问刚刚复制出来的链接后，网页没有发生变化，依然在登陆界面。

9.但是我们来到后台，可以看到刚刚发布的文章已经消失了。 

### &lt;漏洞成因&gt;

1.网站对用户发送的数据包没有进行验证，没有验证触发当前操作的用户权限。

2.有验证，但是逻辑顺序搞错了。

## 四、访问控制示例——代码未引用验证

### &lt;越权演示&gt;

1.先打开网站登陆，验证可以正常登陆。

2.退出登陆。

3.查看网站源代码，可以看到检查登陆的原码。

4. 它检查登陆是要通过下面的代码来跳转到检查登陆的代码里的，我们再这里将其注释掉。

5.此时再回到网站，此时再访问index的时候就可以直接跳转到网站登陆后的页面了。

6.查看网站源代码可以发现很多代码内都调用了验证有没有登陆的那串代码的文件。

7.这就是我们在平时访问网站的时候，有些网页在我们登陆之前就可以访问到，有些网站必须我们登陆后才能进行访问的根本原因。

8.如果有一个文件没有包含那个文件，那么那个文件就可以进行未授权访问。

9.当我们进行漏洞挖掘的时候，就可以查看敏感页面（比如后台页面）有没有引用验证代码，如果没有引用到，那么就存在越权漏洞。

## 五、脆弱机制示例——Cookie脆弱验证

### &lt;越权演示&gt;

1.先打开网站登陆界面。

2. 点击登陆后抓取数据包。

3.给cookie的user随便输入一个值后提交数据包。

 4.可以看到成功进入到了登陆后的页面。

5. 这就是虽然存在验证，但是验证太单一了。

### &lt;真实案例演示&gt;

1.我们使用fofa查找对应的cms。

2.打开一个对用的网站进行测试。

3.来到登陆页面点击登陆后。

4.点击登陆后进行抓包，更改成下面的样式。

5.放包后可以看到成功进入到了后台页面。

## 六、空口令机制示例——Redis&amp;Weblogic 弱机制

### &lt;演示一&gt;

1.来到下面的靶场来查询对应的靶场。

2. 环境介绍。

3.将环境启动。

 <img alt="" height="581" src="https://img-blog.csdnimg.cn/d8e12342881f41288a5489afd508de2c.png" width="997"/>

4. 使用客户端填写对应的ip以及端口来进行访问，发现成功访问进去了。

### &lt;演示二&gt;

1.环境介绍。

2.将环境启动后来到后台登陆页面。

3.在url栏内输入下面的地址后即可进行未授权访问。

4.如图所示成功进入了后台。
