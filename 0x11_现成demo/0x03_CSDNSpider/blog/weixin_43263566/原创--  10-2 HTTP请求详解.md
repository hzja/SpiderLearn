# 原创
：  10-2 HTTP请求详解

# 10-2 HTTP请求详解

#### HTTP请求格式

请求报文通常包含以下部分：

1.  请求行（Request Line）: 包括请求方法、请求的URL和协议版本。 示例：GET /index.html HTTP/1.1 
<li> 请求头（Request Headers）: 包含了一系列的键值对，用来描述客户端请求的相关信息，比如Accept(告诉服务器客户端能够处理的MIME类型)、User-Agent(用户代理字符串)等等。 示例： <pre><code>Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8</code></pre> </li>
1.  空行（Empty Line）: 请求头和请求体之间必须有一个空行，用来分隔请求头和请求体。 
1.  请求体（Request Body）: 对于一些请求（比如POST请求），请求体包含了客户端发送给服务器的数据。 示例： <pre>`username=johndoe&amp;password=secret&amp;submit=Login`</pre>
