# 原创
：  代理访问https网站报ssl错误

# 代理访问https网站报ssl错误

#### 系统环境

#### 代码

```
# -*- coding: utf-8 -*-
"""python3提取api链接并使用requests库进行http代理"""
import requests
import random

page_url = "https://dev.kdlapi.com/testproxy"  # 要访问的目标网页
# API接口，返回格式为json。快代理提供
api_url = "http://kps.kdlapi.com/api/getkps/?orderid=968347822535999&amp;num=1&amp;pt=1&amp;format=json&amp;sep=1"

# API接口返回的ip
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

# 用户名和密码(私密代理/独享代理)
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': random.choice(proxy_ip)},
    "https": "https://%(proxy)s/" % {'proxy': random.choice(proxy_ip)}
}
print(proxies)
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}
r = requests.get(page_url, headers=headers)
# 发送post请求
# r = requests.post("http://dev.kdlapi.com/testproxy", data={"info": "send post request"}, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    # 获取页面内容
    print(r.content)


```

#### 异常信息：

```
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 516, in urlopen
    body=body, headers=headers)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 304, in _make_request
    self._validate_conn(conn)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 724, in _validate_conn
    conn.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 237, in connect
    ssl_version=resolved_ssl_version)
  File "/usr/lib/python3/dist-packages/urllib3/util/ssl_.py", line 123, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib/python3.4/ssl.py", line 364, in wrap_socket
    _context=self)
  File "/usr/lib/python3.4/ssl.py", line 577, in __init__
    self.do_handshake()
  File "/usr/lib/python3.4/ssl.py", line 804, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:600)

```

#### 如何修改

requests.packages.urllib3.disable_warnings() 关闭告警信息<br/> verify=False 不验证certificate

##### 修正后代码

```
# -*- coding: utf-8 -*-
"""python3提取api链接并使用requests库进行http代理"""
import requests
import random

requests.packages.urllib3.disable_warnings() # 关闭告警信息
page_url = "https://dev.kdlapi.com/testproxy"  # 要访问的目标网页
# API接口，返回格式为json。快代理提供
api_url = "http://kps.kdlapi.com/api/getkps/?orderid=968347822535999&amp;num=1&amp;pt=1&amp;format=json&amp;sep=1"

# API接口返回的ip
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

# 用户名和密码(私密代理/独享代理)
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': random.choice(proxy_ip)},
    "https": "https://%(proxy)s/" % {'proxy': random.choice(proxy_ip)}
}
print(proxies)
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}
r = requests.get(page_url, headers=headers, verify=False) # 不验证certificate
# 发送post请求
# r = requests.post("http://dev.kdlapi.com/testproxy", data={"info": "send post request"}, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    # 获取页面内容
    print(r.content)
    # print(r.text)


```

运行结果<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/5434d75b821eaaa96bdab57db3f289c7.png"/><br/> 不过我在win10环境下使用一样的代码不会引发ssl错误，目前怀疑是系统环境ssl的问题。不过最简单粗暴的办法就是不验证，也是最快的方法。

### 进阶学习
