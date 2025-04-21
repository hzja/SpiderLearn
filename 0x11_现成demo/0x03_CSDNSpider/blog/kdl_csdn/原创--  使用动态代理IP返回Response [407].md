# 原创
：  使用动态代理IP返回Response [407]

# 使用动态代理IP返回Response [407]

#### 代理返回Response [407]

### 客户问题

**使用产品类型：**

[私密代理集中提取](https://www.kuaidaili.com/cart?p=month&amp;t=dps&amp;c=10&amp;num=2500)<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/70961b492f65203ba2cfd68bd260bcca.png"/>

**问题描述：**

程序运行的过程中总是有少部分请求拿不到任何响应，服务器没有任何响应，现象和最开始没有使用用户名密码一样。怀疑是快代理的代理IP用户认证是有问题的。

### 技术支持流程

**0x01 排除产品问题**<br/> 首先还是老样子，工程师编写脚本使用用户订单下的代理IP，运行了一段时间后问题并没有出现407 Proxy Authentication Required的情况。

**0x02 询问代码&amp;分析问题**<br/> 但是用户这边是拿出了详细的程序运行日志，统计确实是存在没有任何响应的数据记录，于是我们向用户要来了代码。粗略查看后，用户是使用Python的Requests框架配合多线程进行了二次封装。经过一段时间的调试与排查，我在Requests的返回值里面发现了蹊跷：**用户对于每次请求的response都会进行一次布尔运算。**

代码如下：

```
#!/usr/bin/python
# coding:utf-8
import requests
r = None
proxy_ip = "39.97.170.201:16818"
proxies = {
    "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
    "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
}
try:
    r = requests.get("http://www.baidu.com/", proxies=proxies)
    print r
except Exception, e:
    print e
if r:
    print "True"
else:
    print "False"

```

```
&lt;Response [407]&gt;
False

```

使用一台没有配置白名单IP的电脑，填写上代理IP运行此程序你会发现：

为什么没有输出True？按照常理来说，程序运行并没有出现异常，r此时是请求完成后的返回值，只要返回值不是零值就能够匹配到True的。但是为什么返回的&lt;Response [407]&gt;就会引发if判断异常呢？

```
&gt; type(r)
&gt; requests.models.Response

```

查看Requests关于Response代码：<br/> •Response对象含有了__bool__魔法方法的处理，对象进行布尔运算时，这个魔法函数会被调用。<br/> •Response对象的布尔值取决于self.ok。<br/> •在HTTP状态码为400-500或者是500-600的范围内时，self.ok都为False，其余为True。

```
class Response(object):
    """The :class:`Response &lt;Response&gt;` object, which contains a
    server's response to an HTTP request.
    """
    __attrs__ = [
        '_content', 'status_code', 'headers', 'url', 'history',
        'encoding', 'reason', 'cookies', 'elapsed', 'request'
    ]
    def __init__(self):
        self._content = False
        self._content_consumed = False
        self._next = None
        #: Integer Code of responded HTTP Status, e.g. 404 or 200.
        self.status_code = None
        
    def __repr__(self):
        return '&lt;Response [%s]&gt;' % (self.status_code)
    def __bool__(self):
        """Returns True if :attr:`status_code` is less than 400.
        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        return self.ok


    @property
    def ok(self):
        """Returns True if :attr:`status_code` is less than 400, False if not.
        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        try:
            self.raise_for_status()
        except HTTPError:
            return False
        return True
      
    def raise_for_status(self):
        """Raises :class:`HTTPError`, if one occurred."""
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
        if 400 &lt;= self.status_code &lt; 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)
        elif 500 &lt;= self.status_code &lt; 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)
        if http_error_msg:
            raise HTTPError(http_error_msg, response=self)
            
        ......      

```

### 结论

用户最初没有使用用户名密码进行认证时，代理返回&lt;Response [407]&gt;，随后用户带上了用户名密码，程序正常跑起来。

但是访问的URL中有一部分失效链接或者当时目标网站不稳定等等其他因素，拿到了&lt;Response [404]&gt;，&lt;Response [502]&gt;这样的状态码。

由于Requests框架对与400-600状态码响应进行布尔操作都会返回False，跟之前代理未认证返回的&lt;Response [407]&gt;出现的现象一样，于是误以为是快代理的代理IP出现了问题。

在和用户解释了原因后，用户随即修改代码，通过HTTP状态码来判断代理请求是否成功，完美解决了这个问题。

获取更多经验好文<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/a6074dc4639a9c2ffcc553e5a6f5ce2f.png"/>
