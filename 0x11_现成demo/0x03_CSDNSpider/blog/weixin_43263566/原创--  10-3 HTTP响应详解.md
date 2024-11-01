# 原创
：  10-3 HTTP响应详解

# 10-3 HTTP响应详解

### HTTP响应格式

HTTP响应报文通常由四个部分组成：

1.  响应行（Response Line）：包含协议版本、状态码和状态消息，例如：HTTP/1.1 200 OK。 
1.  响应头（Response Headers）：包含了一系列的键值对，用来描述关于响应的信息，比如内容类型、日期、服务器信息等等。 
1.  空行：即CRLF（回车换行），用来标识响应头的结束，之后是响应体。 
1.  响应体（Response Body）：包含了实际的响应内容，比如HTML页面、JSON数据、文件内容等等。 

当客户端发送一个HTTP请求后，服务器将以HTTP响应的形式返回数据。以下是一个简单的HTTP响应报文的示例：

```
HTTP/1.1 200 OK
Content-Type: text/html
Date: Thu, 17 Nov 2023 12:00:00 GMT
Server: MyServer

&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Example Page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Hello, World!&lt;/h1&gt;
  &lt;p&gt;This is an example page.&lt;/p&gt;
&lt;
```
