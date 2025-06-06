# 原创
：  Ruby——net/http使用代理

# Ruby——net/http使用代理

### 本文知识点

### 环境配置:

确认环境。

```
ruby -v

```

环境搭建好之后，直接引入内置模块使用即可。

### 代码样例

使用代理

```
# -*- coding: utf-8 -*-

require 'net/http'  # 引入内置net/http模块
require 'zlib'
require 'stringio'

# 代理服务器ip和端口,由快代理提供
proxy_ip = '47.115.5.19'
proxy_port = 16816

# 要访问的目标网页, 以快代理testproxy页面为例
page_url = "https://dev.kuaidaili.com/testproxy"
uri = URI(page_url)

# 新建代理实例
proxy = Net::HTTP::Proxy(proxy_ip, proxy_port)

# 创建新的请求对象 
req = Net::HTTP::Get.new(uri)

# 设置User-Agent
req['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
req['Accept-Encoding'] = 'gzip'  # 使用gzip压缩传输数据让访问更快

# 使用代理发起请求, 若访问的是http网页, 请将use_ssl设为false
res = proxy.start(uri.hostname, uri.port, :use_ssl =&gt; true) do |http|
    http.request(req)
end

# 输出状态码
puts "status code: #{res.code}"

# 输出响应体
if  res.code.to_i != 200 then
    puts "page content: #{res.body}"
else
    gz = Zlib::GzipReader.new(StringIO.new(res.body.to_s))
    puts "page content: #{gz.read}" 
end

```

运行下试试，看看结果。成功，code200,<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/5ebe1ae3d4d2cd3d1a965a699819f4e9.png"/>

### 进阶学习:
