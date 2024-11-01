## 收集材料

链接：https://www.gdtv.cn/search?key=七十二家房客



### 负载一

#### 请求头
~~~json
请求 URL:https://gdtv-api.gdtv.cn/api/search/v1/news
请求方法: POST
状态代码: 200
远程地址:127.0.0.1:8080
引用者策略: strict-origin-when-cross-origin
~~~

~~~ json
POST /api/search/v1/news HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 68
Content-Type: application/json
Host: gdtv-api.gdtv.cn
Origin: https://www.gdtv.cn
Referer: https://www.gdtv.cn/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76
X-ITOUCHTV-CLIENT: WEB_PC
X-ITOUCHTV-Ca-Key: 89541443007407288657755311869534
X-ITOUCHTV-Ca-Signature: 2Vwp6Y9ahfHjXzO3QNDf7/Gtg0WEpzscFrH7cF4EfcE=
X-ITOUCHTV-Ca-Timestamp: 1706700795746
X-ITOUCHTV-DEVICE-ID: WEB_64df7380-c026-11ee-ab39-fd12bbb279be
sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
~~~

#### 负载
~~~ json
{"keyword":"七十二家房客","pageNum":1,"type":-1,"pageSize":15}
~~~

### 负载二
####  请求头
~~~ json
请求 URL:
https://gdtv-api.gdtv.cn/api/search/v1/news
请求方法:
POST
状态代码:
200
远程地址:
127.0.0.1:8080
引用者策略:
strict-origin-when-cross-origin
~~~

~~~ json
POST /api/search/v1/news HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 67
Content-Type: application/json
Host: gdtv-api.gdtv.cn
Origin: https://www.gdtv.cn
Referer: https://www.gdtv.cn/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76
X-ITOUCHTV-CLIENT: WEB_PC
X-ITOUCHTV-Ca-Key: 89541443007407288657755311869534
X-ITOUCHTV-Ca-Signature: J4N6byianb/t/pHJGr2DV6f89M8VKI2zsOk2ne6mK6A=
X-ITOUCHTV-Ca-Timestamp: 1706701401388
X-ITOUCHTV-DEVICE-ID: WEB_64df7380-c026-11ee-ab39-fd12bbb279be
sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
~~~

#### 负载
~~~ json
{"keyword":"七十二家房客","pageNum":2,"type":3,"pageSize":15}
~~~