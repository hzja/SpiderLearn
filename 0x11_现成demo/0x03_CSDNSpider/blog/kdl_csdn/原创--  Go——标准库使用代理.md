# 原创
：  Go——标准库使用代理

# Go——标准库使用代理

### 本文知识点

### 环境配置

确认环境都安装好了，看看go的版本。

```
go version

```

### 代码样例

#### 使用代理，发送GET请求

```
package main

import (
    "compress/gzip"
    "fmt"
    "io"
    "io/ioutil"
    "net/http"
    "net/url"
    "os"
)

func main() {
    // 用户名密码(私密代理/独享代理)

    // 代理ip,由快代理提供
    proxy_raw := "47.115.5.19:16816"
    proxy_str := fmt.Sprintf("http://%s:%s@%s", proxy_raw)
    proxy, err := url.Parse(proxy_str)

    // 目标网页
    page_url := "http://dev.kdlapi.com/testproxy"

    //  请求目标网页
    client := &amp;http.Client{Transport: &amp;http.Transport{Proxy: http.ProxyURL(proxy)}}
    req, _ := http.NewRequest("GET", page_url, nil)
    req.Header.Add("Accept-Encoding", "gzip") //使用gzip压缩传输数据让访问更快
    res, err := client.Do(req)

    if err != nil {
        // 请求发生异常
        fmt.Println(err.Error())
    } else {
        defer res.Body.Close() //保证最后关闭Body

        fmt.Println("status code:", res.StatusCode) // 获取状态码
        // 有gzip压缩时,需要解压缩读取返回内容
        if res.Header.Get("Content-Encoding") == "gzip" {
            reader, _ := gzip.NewReader(res.Body) // gzip解压缩
            defer reader.Close()
            io.Copy(os.Stdout, reader)
            os.Exit(0) // 正常退出
        }

        // 无gzip压缩, 读取返回内容
        body, _ := ioutil.ReadAll(res.Body)
        fmt.Println(string(body))
    }
}


```

运行下，看看结果

```
go run demo.go

```

没问题，200 OK的<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/a05401c5ef1f414ec38c1f1132707976.png"/>

#### POST请求

把上面代码中的get，改成post就好了。就是这一句

```
req, _ := http.NewRequest("POST", page_url, nil)

```

### 进阶学习
