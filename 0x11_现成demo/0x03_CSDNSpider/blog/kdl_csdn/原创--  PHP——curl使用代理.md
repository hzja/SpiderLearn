# 原创
：  PHP——curl使用代理

# PHP——curl使用代理

### 本文知识点

### 环境搭建

安装curl库

```
# ubuntu/debian系统
apt-get install php5-curl 
# centos系统
yum install php-curl

```

确认环境。

```
php -v

```

### 代码样例

使用代理

```
&lt;?php
//要访问的目标页面
$page_url = "http://dev.kdlapi.com/testproxy";

//代理ip,由快代理提供
$proxy = "47.115.5.19:16816";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $page_url);

curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);  
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);

//设置代理
curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_HTTP);
curl_setopt($ch, CURLOPT_PROXY, $proxy);

//自定义header
$headers = array();
$headers[] = 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

//自定义cookie
curl_setopt($ch, CURLOPT_COOKIE,''); 

curl_setopt($ch, CURLOPT_ENCODING, 'gzip'); //使用gzip压缩传输数据让访问更快

curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
$info = curl_getinfo($ch);
curl_close($ch);

echo $result;
echo "\n\nfetch ".$info['url']."\ntimeuse: ".$info['total_time']."s\n\n";
?&gt;


```

运行下

```
php curl.php

```

### 进阶学习
