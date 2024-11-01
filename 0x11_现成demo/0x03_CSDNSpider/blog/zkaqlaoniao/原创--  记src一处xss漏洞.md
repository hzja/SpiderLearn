# 原创
：  记src一处xss漏洞

# 记src一处xss漏洞

### 前言：本来是想挖货拉拉的漏洞，阴差阳错从hunter上搜索相关资产挖到一个存储型XSS。

### 一、hunter上搜索domain.suffix=”huolala.cn”，查找到一处资产。

### 二、访问ip地址，却跳转到了一个博客页面，注册个账号登录。

### 三、进入about模块，发现有评论框，可以测试xss。

### 四、经过三轮测试，成功触发存储型xss。

第一次，payload：

```
&lt;script&gt;alert(1)&lt;/script&gt;
```

<br/> 发现script标签被过滤了，再尝试事件法。payload如下：

```
&lt;img src="1.jpg" onerror=alert(1) /&gt;
```

<br/> 可以看到onerror关键字也被过滤了，这个事件换个呗，经过尝试，onclick事件成功，payload如下：

```
&lt;img src="1.jpg" onclick="alert(1)" /&gt;
```

<br/> 成功写入，一点击就触发。<br/>  

<br/> 这样子也就可以获取cookie了。
