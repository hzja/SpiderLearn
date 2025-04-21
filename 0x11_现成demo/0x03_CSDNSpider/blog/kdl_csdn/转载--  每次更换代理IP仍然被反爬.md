# 转载
：  每次更换代理IP仍然被反爬

# 每次更换代理IP仍然被反爬

### 每次更换代理IP仍然被反爬

### 客户问题

**使用产品类型：**

隧道代理动态版（每次请求更换IP）。

**问题描述：**

目标网站有反爬机制，两次搜索的间隔时间不得少于25秒。使用了我们的隧道代理后，还是会被检测出来，依旧只能25秒访问一次。遂怀疑是我们的隧道代理没有更换IP。

### 技术支持流程

**0x01 排除产品问题**<br/> 按照流程，我们先使用用户的隧道代理进行访问测试，看看是否每次更换了IP。

在用户的隧道代理订单下添加我们测试机器的外网IP，在Linux/macOS下使用curl命令访问cip.cc进行测试。

```
curl cip.cc -x tps1xx.kdlapi.com:15818

```

可以看到在实际测试中，我们使用隧道代理访问了三次cip.cc都正常每次更换了IP，排除了隧道代理本身产品的问题。在向用户表达了并非隧道代理产品问题后，我们继续刨根问底，帮助客户找到真正的问题。

**0x02 分析网站**<br/> 分析用户访问的网站：

https://www.kquanben.com/modules/article/search.php

发现是一个普通的小说搜索网页，连续搜索两次关键词"霸道总裁"，发现就已经提示错误。果然两次两次搜索间隔不得小于25s。

打开Chrome浏览器控制台，查看发送的请求。可以发现在搜索的过程中，浏览器发送了一个POST请求，携带的参数大致如下。

```
#header
{
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,',
 'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,',
 'Accept-Language': 'zh-CN,zh;q=0.9,',
 'Cache-Control': 'no-cache,',
 'Connection': 'keep,',
 'Host': 'www.kquanben.com,',
 'Pragma': 'no-cache,',
 'Upgrade-Insecure-Requests': '1,',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ',
 'Chrome/86.0.4240.111 Safari/537.36,',
 'sec-ch-ua': ''Google Chrome;v=89, Chromium;v=89, ;Not A Brand;v=99',',
 'sec-ch-ua-mobile': '?0,',
 'Sec-Fetch-Dest': 'document,',
 'Sec-Fetch-Mode': 'navigate,',
 'Sec-Fetch-Site': 'none,',
 'Sec-Fetch-User': '?1,'
 ...
}

```

响应Header如下

```
{
 'content-type': 'text/html; charset=utf-8',
 'date': 'Wed, 14 Apr 2021 02': '53': '09 GMT',
 'location': 'result/?searchid=31435',
 'server': 'nginx',
 'set-cookie': 'alllc111lastsearchtime=1618368789; expires=Thu, 15-Apr-2021 02': '53': '09 GMT; Max-Age=86400; path=/; secure',
 'strict-transport-security': 'max-age=31536000'
 ...
}

```

其中的set cookie字段一下就吸引了我们的注意。<br/> 在alllc111lastsearchtime=1618368789中有一段数字与时间戳非常相似。我们推断在首次浏览器进行小说搜索时，服务器会返回set-cookie字段记录用户上次的搜索时间，当用户进行第二次搜索时，请求会携带上这个cookie字段，如果服务器判断两次搜索时间间隔小于25s，请求就会直接被拒绝。为了验证，我们将时间戳实时生成进行请求，果然没有了搜索限制，每次请求都可以正常得到响应。所以获取网站的主要反爬虫措施是cookie时间戳限制，并不是和客户端IP相关，也就说主要原因并不是隧道代理，可以判断是用户的代码问题了。

**0x03 排查用户代码**<br/> 我们向用户询问了代码，为了便于展示，只保留了关键发送请求的相关逻辑。

```
# coding:utf-8
# 看全本


import requests


def test(info):
    book_name = info[0]
    book_auth = info[1]
    data = {
 "searchkey": book_name.strip(),
 "searchtype": "articlename",
 }
    s = requests.session() # 使用了session
    url = 'https://www.kquanben.com/modules/article/search.php'
    headers = {
 # 省略
 }
    tunnel = "tps1xx.kdlapi.com:15818"
    username = "txxxxxxxxxx"
    password = "password"
    proxies = {
 "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
 "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
 }
    response = s.post(url, headers=headers, data=data, timeout=12.1)
 # 解析response

```

用户使用了Requests[1]框架中的session发送请求，查看文档可知Requests框架有持久 Cookie 的会话的功能，查看session源码可见，在使用session发送请求的过程前会进行prepare_request，将会话的cookie进行合并。

```
class Session(SessionRedirectMixin):
 """A Requests session.


 Provides cookie persistence, connection-pooling, and configuration.
 
 ......
 """
 def prepare_request(self, request):
 """Constructs a :class:`PreparedRequest &lt;PreparedRequest&gt;` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request &lt;Request&gt;` instance and those of the
 :class:`Session`.


 :param request: :class:`Request` instance to prepare with this
            session's settings.
 :rtype: requests.PreparedRequest
 """
        cookies = request.cookies or {}


 # Bootstrap CookieJar.
 if not isinstance(cookies, cookielib.CookieJar):
            cookies = cookiejar_from_dict(cookies)


 # Merge with session cookies
        merged_cookies = merge_cookies(
            merge_cookies(RequestsCookieJar(), self.cookies), cookies)
 # ......


```

有关cookie的更多操作可以查看Requests-Cookie[2]。

所以根据上一步我们分析用户网站得知，用户使用了session发送请求，在首次用户请求中，目标网站返回了set cookie字段。于是Requests框架就将此cookie自动保存了起来，用于下一次请求。所以在第二次访问的过程中，请求会带上上一次访问的时间戳，两者间隔小于了25s，所以请求被拒绝。解决办法也很简单，就是不使用session发送请求，直接使用requests.post()，部分代码如下：

```
import requests
import time
url = 'https://www.kquanben.com/modules/article/search.php'
headers = {
 'cookie': 'alllc111lastsearchtime=%s' % int(time.time())
 # 省略
}
data = {
 # 省略
}
response = s.post(url, headers=headers, data=data, timeout=12.1)

```

在通过快代理工程师的建议下，用户很快地修改了代码，顺利使用上代理进行网站的访问。

### 结论

•对于requests.session要慎用，它会进行cookie存储，使用不当会被目标网站识别。<br/> •并不是所有的网站防爬措施都是限制访问IP，需要进行具体分析。

```
                           ****关注【快代理客户服务】了解更多技术好文****

```
