# 原创
：  【SQL注入】Header注入：基础知识、原理、利用

# 【SQL注入】Header注入：基础知识、原理、利用

**目录**

[一、基础知识](#%E4%B8%80%E3%80%81%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)

[Header头](#Header%E5%A4%B4)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[常见的请求头参数](#%E5%B8%B8%E8%A7%81%E7%9A%84%E8%AF%B7%E6%B1%82%E5%A4%B4%E5%8F%82%E6%95%B0)

[二、Header注入](#%E4%BA%8C%E3%80%81Header%E6%B3%A8%E5%85%A5)

[注入原理：](#%E6%B3%A8%E5%85%A5%E5%8E%9F%E7%90%86%EF%BC%9A)

[注入地方：](#%E6%B3%A8%E5%85%A5%E5%9C%B0%E6%96%B9%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[注入流程：](#%E6%B3%A8%E5%85%A5%E6%B5%81%E7%A8%8B%EF%BC%9A)

[payload:](#payload%3A)

---


## 一、基础知识

> 
<h3>Header头</h3>
HTTP消息包括：客户机向服务器的请求消息（Request）和服务器向客户机的响应消息（Response）（由一个起始行，一个或者多个头域，一个只是头域结束的空行和可选的消息体组成）
<hr/>
HTTP的头域包括通用头，请求头，响应头和实体头四个部分，
HTTP消息头支持自定义
<hr/>
每个头域由一个域名（大小写无关），冒号（:）和域值三部分组成，域值前可以添加任何数量的空格符，头域可以被扩展为多行，在每行开始处，使用至少一个空格或制表符


---


> 
<h3>示例：</h3>
POST /sqli-labs-master/Less-18/ HTTP/1.1<br/> Host: localhost:8080<br/> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0<br/> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8<br/> Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2<br/> Accept-Encoding: gzip, deflate<br/> Referer: http://localhost:8080/sqli-labs-master/Less-11/<br/> Content-Type: application/x-www-form-urlencoded<br/> Content-Length: 94<br/> Origin: http://localhost:8080<br/> Connection: close<br/> Cookie: UM_distinctid=1801d57ba0c6c-0ea17069b11c2e8-4c3e2c73-144000-1801d57ba0f2b2; CNZZDATA1263804910=973780364-1649755840-null%7C1649824812; WSTMART_loginName=huaguoshan; WSTMART_loginPwd=%B3%A8%A3%DC%7Dus%DC%7F%A9r%A8%80x%85%95%93z%8A%9C%8C%A6%9B%9A%BC%9A%A6%D0%7Fz%C5h%B4%96%AC%D0%7Ec%7F%DD%8C%D2%8Ab%8D%85z%CA%87%A3%7Da%81%B9%85%9E%BBb%AD%98%8C%A3%B3k%B4%AB%AF%DE%8A%85%87%99%80%B9%98%AA%80%85%7D%97%86%8A%9B%60%7F%A6%9B%9C%B0t%CF%9A%7Fz%ABk%B3%CE%B3%DE; WSTMART_history_goods=think%3A%5B%2282%22%5D; _octo=GH1.1.1176236109.1654067901; tz=Asia%2FShanghai; PHPSESSID=sm2uedtp0gbr0g6bmcv11k1kb6<br/> Upgrade-Insecure-Requests: 1<br/> Sec-Fetch-Dest: document<br/> Sec-Fetch-Mode: navigate<br/> Sec-Fetch-Site: same-origin<br/> Sec-Fetch-User: ?1<br/> Pragma: no-cache<br/> Cache-Control: no-cache


> 
<h3>常见的请求头参数</h3>
<table align="left" border="1" cellpadding="1" cellspacing="1"><tbody>|Header|解释|示例
|Accept|指定客户端能够接收的内容类型|Accept: text/plain, text/html
|Accept-Charset|浏览器可以接受的字符编码集。|Accept-Charset: iso-8859-5
|Accept-Encoding|指定浏览器可以支持的web服务器返回内容压缩编码类型。|Accept-Encoding: compress, gzip
|Accept-Language|浏览器可接受的语言|Accept-Language: en,zh
|Accept-Ranges|可以请求网页实体的一个或者多个子范围字段|Accept-Ranges: bytes
|Authorization|HTTP授权的授权证书|Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
|Cache-Control|指定请求和响应遵循的缓存机制|Cache-Control: no-cache
|Connection|表示是否需要持久连接。（HTTP 1.1默认进行持久连接）|Connection: close
|Cookie|HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器。|Cookie: $Version=1; Skin=new;
|Content-Length|请求的内容长度|Content-Length: 66
|Content-Type|请求的与实体对应的MIME信息|Content-Type: application/x-www-form-urlencoded
|Date|请求发送的日期和时间|Date: Tue, 15 Nov 2010 08:12:31 GMT
|Expect|请求的特定的服务器行为|Expect: 100-continue
|From|发出请求的用户的Email|From: user@email.com
|Host|指定请求的服务器的域名和端口号|Host: www.zcmhi.com
|If-Match|只有请求内容与实体相匹配才有效|If-Match: “737060cd8c284d8af7ad3082f209582d”
|If-Modified-Since|如果请求的部分在指定时间之后被修改则请求成功，未被修改则返回304代码|If-Modified-Since: Sat, 29 Oct 2010 19:43:31 GMT
|If-None-Match|如果内容未改变返回304代码，参数为服务器先前发送的Etag，与服务器回应的Etag比较判断是否改变|If-None-Match: “737060cd8c284d8af7ad3082f209582d”
|If-Range|如果实体未改变，服务器发送客户端丢失的部分，否则发送整个实体。参数也为Etag|If-Range: “737060cd8c284d8af7ad3082f209582d”
|If-Unmodified-Since|只在实体在指定时间之后未被修改才请求成功|If-Unmodified-Since: Sat, 29 Oct 2010 19:43:31 GMT
|Max-Forwards|限制信息通过代理和网关传送的时间|Max-Forwards: 10
|Pragma|用来包含实现特定的指令|Pragma: no-cache
|Proxy-Authorization|连接到代理的授权证书|Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
|Range|只请求实体的一部分，指定范围|Range: bytes=500-999
|Referer|先前网页的地址，当前请求网页紧随其后,即来路|Referer: http://www.zcmhi.com/archives/71.html
|TE|客户端愿意接受的传输编码，并通知服务器接受接受尾加头信息|TE: trailers,deflate;q=0.5
|Upgrade|向服务器指定某种传输协议以便服务器进行转换（如果支持）|Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11
|User-Agent|User-Agent的内容包含发出请求的用户信息|User-Agent: Mozilla/5.0 (Linux; X11)
|Via|通知中间网关或代理服务器地址，通信协议|Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)
|Warning|关于消息实体的警告信息|Warn: 199 Miscellaneous warning
</tbody></table>










---


---


## 二、Header注入

> 
<h3>注入原理：</h3>
预定义变量 ： $_get (获取GET的传参)、$_post（获取POST传参）、$_cookie（获取COOKIE的值） 、$_SERVER（包含了诸如头信息(header)、路径(path)、以及脚本位置(script locations)等等信息的数组）等
<hr/>
header注入可以理解为：利用后端验证客户端口信息（比如常用的cookie验证）或者通过Header中获取客户端的一些信息，通过对头部信息字段的修改注入，又因为后台没有进过相对应的信息处理所以构成了sql注入，完成对数据库的渗透


> 
<h3>注入地方：</h3>
<h4>简介：</h4>
Header中各种参数中都可以尝试注入，例如User-Agent、Referer、IP、cookie注入或者其他参数注入
<hr/>
<h4>注入流程：</h4>
暴力破解----寻找注入点-------字段注入--------获取数据
暴力破解：平台中有大量的账号，获得平台的账号密码（其实一般可以自己注册一个）
寻找注入点：突破口（过滤不严谨的地方）
字段注入：将构造的payload带入数据库中
获取数据：返回信息
<hr/>
<h4>payload:</h4>
xxx' and updatexml(1,concat(0x7e,database()),1) or'



#### 简介：

---


#### payload:
