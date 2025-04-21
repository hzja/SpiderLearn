# 原创
：  Ruby——httparty使用代理

# Ruby——httparty使用代理

### 本文知识点

### 环境配置:

安装httparty库

```
gem install httparty

```

### 代码样例

使用代理

```
require "httparty"  # 引入httparty模块
require 'zlib'
require 'stringio'

# 代理服务器ip和端口,,由快代理提供
proxy_ip = '47.115.5.19'
proxy_port = 16816

# 要访问的目标网页, 以京东首页为例
page_url = 'https://dev.kuaidaili.com/testproxy'

# 设置headers
headers = {
    "User-Agent" =&gt; "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Accept-Encoding" =&gt; "gzip",
}

# 设置代理ip
options = {
    :headers =&gt; headers, 
    :http_proxyaddr =&gt; proxy_ip, 
    :http_proxyport =&gt; proxy_port,
}

# 发起请求
res = HTTParty.get(page_url, options)

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

运行下，看看结果。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/492706fbfbc6be711e0043db522aa2d7.png"/>

### 进阶学习
