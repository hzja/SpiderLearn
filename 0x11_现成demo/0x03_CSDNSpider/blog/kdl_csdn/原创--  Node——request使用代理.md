# 原创
：  Node——request使用代理

# Node——request使用代理

### 本文知识点

### 环境配置

安装request

```
npm install request

```

确认环境安装无误

```
node -v

```

### 代码样例

使用代理

```
let request = require('request'); // 引入第三方request库
let util = require('util');
let zlib = require('zlib');

// 要访问的目标地址
let page_url = 'http://dev.kdlapi.com/testproxy'

// 代理服务器ip和端口,由快代理提供
let proxy_ip = '47.115.36.94';
let proxy_port = 16816;

// 完整代理服务器url
let proxy = util.format('http://%s:%d', proxy_ip, proxy_port);  

// 发起请求
request({
    url: page_url,
    method: 'GET',
    proxy: proxy,
    headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Accept-Encoding": "gzip"   // 使用gzip压缩让数据传输更快
    },
    encoding: null,  // 方便解压缩返回的数据
}, function(error, res, body) {
    if (!error &amp;&amp; res.statusCode == 200) {
        // 输出返回内容(使用了gzip压缩)
        if (res.headers['content-encoding'] &amp;&amp; res.headers['content-encoding'].indexOf('gzip') != -1) {
            zlib.gunzip(body, function(err, dezipped) {
                console.log(dezipped.toString()); 
            });
        } else {
            // 输出返回内容(没有使用gzip压缩)
            console.log(body);
        }
    } else {
        console.log(error);
    }
});


```

运行下<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/4c872c3aff32ad9cdf3daf7c0decad54.png"/>

### 进阶学习
